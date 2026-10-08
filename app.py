"""Desktop GUI for the AI chatbot (Tkinter, dark theme, chat bubbles)."""

import sys
import threading
import tkinter as tk
from tkinter import ttk

from chatbot import ask_ai, reset_conversation

# ==========================
# Colors
# ==========================
BG_COLOR = "#1E1E1E"
CHAT_BG = "#252526"
USER_COLOR = "#0B93F6"
AI_COLOR = "#3A3A3A"
TEXT_COLOR = "#FFFFFF"
ENTRY_BG = "#2D2D30"


# ==========================
# Functions
# ==========================

def add_message(sender, message):
    """Add one chat bubble (right side for the user, left side for the AI)."""
    message_frame = tk.Frame(chat_frame, bg=CHAT_BG)
    message_frame.pack(fill="x", padx=10, pady=5)

    if sender == "You":
        bubble_color, side = USER_COLOR, "right"
    else:
        bubble_color, side = AI_COLOR, "left"

    bubble = tk.Label(
        message_frame,
        text=message,
        bg=bubble_color,
        fg="white",
        font=("Arial", 11),
        padx=12,
        pady=8,
        wraplength=450,
        justify="left",
    )
    bubble.pack(side=side)

    chat_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(1.0)


def finish_ai_response(response):
    add_message("AI", response)
    status_label.config(text="Ready", fg="lightgreen")
    button.config(state="normal")
    entry.focus_set()


def get_ai_response(message):
    """Runs in a background thread so the window never freezes."""
    response = ask_ai(message)
    # Tkinter is not thread-safe: hand the result back to the main thread
    window.after(0, lambda: finish_ai_response(response))


def send_message():
    # Ignore sends while the AI is still answering (e.g. Enter key)
    if str(button["state"]) == "disabled":
        return

    message = entry.get().strip()

    if message == "":
        return

    add_message("You", message)
    entry.delete(0, tk.END)

    status_label.config(text="🤖 AI is thinking...", fg="orange")
    button.config(state="disabled")

    threading.Thread(
        target=get_ai_response, args=(message,), daemon=True
    ).start()


def new_chat():
    """Clear the screen and the model's memory."""
    # Don't reset while a reply is still being generated
    if str(button["state"]) == "disabled":
        return

    reset_conversation()

    for child in chat_frame.winfo_children():
        child.destroy()

    chat_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(0.0)


def enter_pressed(event):
    send_message()


def configure_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def resize_chat_frame(event):
    canvas.itemconfigure(chat_window, width=event.width)


def mouse_scroll(event):
    """Mouse-wheel scrolling that works on Windows, macOS and Linux."""
    if event.num == 4:        # Linux scroll up
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:      # Linux scroll down
        canvas.yview_scroll(1, "units")
    elif sys.platform == "darwin":
        canvas.yview_scroll(int(-1 * event.delta), "units")
    else:                     # Windows
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


# ==========================
# Window
# ==========================

window = tk.Tk()
window.title("My AI ChatBot")
window.geometry("900x650")
window.configure(bg=BG_COLOR)

# ==========================
# Menu Bar
# ==========================

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Chat", command=new_chat)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# ==========================
# Title & Status
# ==========================

title = tk.Label(
    window,
    text="🤖 My AI ChatBot",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
title.pack(pady=10)

status_label = tk.Label(
    window, text="Ready", bg=BG_COLOR, fg="lightgreen", font=("Arial", 10)
)
status_label.pack()

# ==========================
# Chat area (canvas + scrollbar + frame)
# ==========================

chat_container = tk.Frame(window, bg=BG_COLOR)
chat_container.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(chat_container, bg=CHAT_BG, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(chat_container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

chat_frame = tk.Frame(canvas, bg=CHAT_BG)
chat_window = canvas.create_window((0, 0), window=chat_frame, anchor="nw")

chat_frame.bind("<Configure>", configure_scroll)
canvas.bind("<Configure>", resize_chat_frame)

canvas.bind_all("<MouseWheel>", mouse_scroll)   # Windows / macOS
canvas.bind_all("<Button-4>", mouse_scroll)     # Linux
canvas.bind_all("<Button-5>", mouse_scroll)     # Linux

# ==========================
# Input row
# ==========================

bottom_frame = tk.Frame(window, bg=BG_COLOR)
bottom_frame.pack(fill="x", padx=10, pady=10)

entry = tk.Entry(
    bottom_frame,
    font=("Arial", 12),
    bg=ENTRY_BG,
    fg="white",
    insertbackground="white",
)
entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
entry.bind("<Return>", enter_pressed)
entry.focus_set()

button = tk.Button(bottom_frame, text="Send", width=10, command=send_message)
button.pack(side="right")

# ==========================
# Start Application
# ==========================

window.mainloop()
