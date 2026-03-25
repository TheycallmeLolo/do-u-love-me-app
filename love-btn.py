import tkinter as tk
from tkinter import messagebox
import random
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


phrases = [
    "Are you sure?", "Try harder! 😎", "Nope!", "Wrong way!",
    "Not today!", "Maybe next time?", "Nice try!", "Run, run, run!",
    "You'll never catch me!", "I'm too fast for you!", "Catch me if you can!"
]

attempts = 0
no_font_size = 12
no_width = 12
MAX_ATTEMPTS = 20


def play_escape_sound():
    if sys.platform == "win32":
        import winsound
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    else:
        root.bell()


def play_win_sound():
    if sys.platform == "win32":
        import winsound
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
    else:
        root.bell()


def show_popup():
    play_win_sound()

    if attempts == 0:
        msg = "Zero attempts?! You didn't even hesitate!\nTrue love confirmed. 💖"
    elif attempts == 1:
        msg = "Only 1 attempt and you gave up trying to say No?\nAdorable. Coffee soon? ☕✨"
    else:
        msg = f"It took you {attempts} attempts to give up!\nI knew you couldn't resist. ☕✨"

    messagebox.showinfo("Yay! ❤️", msg)
    root.destroy()


def move_button(event=None):
    global attempts, no_font_size, no_width

    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    progress = min(attempts / MAX_ATTEMPTS, 1.0)
    progress_bar.coords(progress_fill, 0, 0, progress * 340, 18)

    if attempts >= MAX_ATTEMPTS:
        no_button.place_forget()
        gave_up_label.config(text="The button gave up on you 😭")
        no_button.unbind("<Enter>")
        return

    play_escape_sound()

    window_width = root.winfo_width()
    window_height = root.winfo_height()
    btn_w = no_button.winfo_width() or 100
    btn_h = no_button.winfo_height() or 36

    x = random.randint(20, max(20, window_width - btn_w - 20))
    y = random.randint(20, max(20, window_height - btn_h - 60))

    no_button.place(x=x, y=y)
    no_button.config(text=random.choice(phrases))

    if no_font_size > 7:
        no_font_size = max(7, no_font_size - 0.4)
    if no_width > 5:
        no_width = max(5, no_width - 0.5)

    no_button.config(
        font=("Helvetica", int(no_font_size), "bold"),
        width=int(no_width)
    )

    if attempts > 10:
        no_button.config(bg="#C0392B")
    if attempts > 15:
        no_button.config(bg="#96281B")


# ── Root window ───────────────────────────────────────────────
root = tk.Tk()
try:
    root.iconbitmap(resource_path("assets/heart.ico"))
except Exception:
    pass

root.title("Do U Love me? 💖")
root.geometry("450x580")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# ── Question label ────────────────────────────────────────────
question_label = tk.Label(
    root,
    text="Do you love me?",
    font=("Helvetica", 22, "bold"),
    bg="#2C3E50",
    fg="#ECF0F1"
)
question_label.pack(pady=(45, 4))

# ── Attempts counter ──────────────────────────────────────────
attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Helvetica", 10),
    bg="#2C3E50",
    fg="#BDC3C7"
)
attempts_label.pack()

# ── Progress bar ──────────────────────────────────────────────
progress_frame = tk.Frame(root, bg="#2C3E50")
progress_frame.pack(pady=(8, 0))

progress_bg_label = tk.Label(
    progress_frame,
    text="Progress to button death:",
    font=("Helvetica", 9),
    bg="#2C3E50",
    fg="#7F8C8D"
)
progress_bg_label.pack()

progress_bar = tk.Canvas(
    progress_frame,
    width=340,
    height=18,
    bg="#1A252F",
    highlightthickness=1,
    highlightbackground="#7F8C8D",
    bd=0
)
progress_bar.pack(pady=(4, 0))
progress_fill = progress_bar.create_rectangle(0, 0, 0, 18, fill="#E74C3C", outline="")

# ── "Gave up" message ─────────────────────────────────────────
gave_up_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 11, "italic"),
    bg="#2C3E50",
    fg="#E74C3C"
)
gave_up_label.pack(pady=(6, 0))

# ── Yes button ────────────────────────────────────────────────
yes_button = tk.Button(
    root,
    text="Yes, I do! 💖",
    font=("Helvetica", 12, "bold"),
    bg="#2ECC71",
    fg="white",
    width=15,
    height=2,
    command=show_popup,
    cursor="heart",
    relief="flat",
    activebackground="#27AE60",
    activeforeground="white"
)
yes_button.pack(pady=35)

# ── No button ─────────────────────────────────────────────────
no_button = tk.Button(
    root,
    text="No",
    font=("Helvetica", int(no_font_size), "bold"),
    bg="#E74C3C",
    fg="white",
    width=int(no_width),
    command=move_button,
    cursor="spider",
    relief="flat",
    activebackground="#C0392B",
    activeforeground="white"
)
no_button.pack()
no_button.bind("<Enter>", move_button)

root.mainloop()