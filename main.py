import instaloader
import tkinter as tk
from tkinter import simpledialog, messagebox, Scrollbar, ttk
import webbrowser
import threading
import random
import time
from tkinter import filedialog

def download_instagram_data(username, password):
    L = instaloader.Instaloader()
    try:
        L.login(username, password)
    except instaloader.exceptions.BadCredentialsException:
        raise ValueError("Incorrect username or password")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        raise ValueError("Two-factor authentication is enabled on this account. Please disable it and try again.")
    except instaloader.exceptions.TwoFactorAuthInvalidCodeException:
        raise ValueError("Invalid 2FA code. Please try again.")

    profile = instaloader.Profile.from_username(L.context, username)
    
    followers = set()
    following = set()

    total_followers = profile.followers
    total_following = profile.followees

    progress['maximum'] = total_followers + total_following
    progress['value'] = 0

    for follower in profile.get_followers():
        followers.add(follower.username)
        time.sleep(random.uniform(0.1, 0.5)) 
        progress['value'] += 1
        progress_label.config(text=f"Progress: {int(progress['value'])}/{total_followers + total_following}")

    for followee in profile.get_followees():
        following.add(followee.username)
        time.sleep(random.uniform(0.1, 0.5)) 
        progress['value'] += 1
        progress_label.config(text=f"Progress: {int(progress['value'])}/{total_followers + total_following}")

    return followers, following, L

def find_non_followers(followers, following):
    return following - followers

def on_submit():
    username = entry_username.get()
    password = entry_password.get()
    
    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty")
        return

    submit_button.config(state=tk.DISABLED)
    threading.Thread(target=process_data, args=(username, password)).start()

def process_data(username, password):
    try:
        followers, following, L = download_instagram_data(username, password)
        non_followers = find_non_followers(followers, following)
        update_result_list(non_followers)
        L.close()
        messagebox.showinfo("Completed", "İşlem tamamlandı ve çıkış yapıldı. Lütfen şifrenizi güncellemeyi unutmayınız!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        submit_button.config(state=tk.NORMAL)

def update_result_list(non_followers):
    result_list.delete(0, tk.END)
    result_list.insert(tk.END, f"Total non-followers: {len(non_followers)}")
    for user in non_followers:
        result_list.insert(tk.END, user)

def save_to_file():
    non_followers = [result_list.get(i) for i in range(1, result_list.size())]  
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as f:
            for user in non_followers:
                f.write(f"https://instagram.com/{user}\n")
        messagebox.showinfo("Success", "File saved successfully!")

def on_select(event):
    w = event.widget
    if w.curselection():
        index = int(w.curselection()[0]) - 1  
        value = w.get(index + 1)  
        webbrowser.open(f"https://instagram.com/{value}")

def open_link(url):
    webbrowser.open_new(url)

root = tk.Tk()
root.title("Instagram Non-Followers Finder")

root.geometry('400x450')
root.resizable(False, False)

tk.Label(root, text="Instagram Username:").grid(row=0)
tk.Label(root, text="Instagram Password:").grid(row=1)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

submit_button = tk.Button(root, text='Submit', command=on_submit)
submit_button.grid(row=2, column=1, sticky=tk.W, pady=4)

result_list = tk.Listbox(root, width=50)
result_list.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)

scrollbar = Scrollbar(root, orient=tk.VERTICAL, command=result_list.yview)
scrollbar.grid(row=4, column=2, sticky=tk.NS)
result_list.config(yscrollcommand=scrollbar.set)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.grid(row=3, column=0, columnspan=2, pady=10)

progress_label = tk.Label(root, text="Progress: 0/0")
progress_label.grid(row=5, column=0, columnspan=2)

result_list.bind('<<ListboxSelect>>', on_select)

save_button = tk.Button(root, text='Save to File', command=save_to_file)
save_button.grid(row=6, column=1, sticky=tk.W, pady=4)

link_website = tk.Label(root, text="mucahitarslan.com", fg="blue", cursor="hand2")
link_website.grid(row=7, column=0, pady=4)
link_website.bind("<Button-1>", lambda e: open_link("https://mucahitarslan.com"))

link_github = tk.Label(root, text="GitHub", fg="blue", cursor="hand2")
link_github.grid(row=7, column=1, pady=4)
link_github.bind("<Button-1>", lambda e: open_link("https://github.com/mucahitarslan"))

root.mainloop()
