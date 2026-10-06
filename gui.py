import tkinter as tk
from tkinter import ttk


def create_application():
    window = tk.Tk()
    window.title("Food Pantry Notification System")
    window.geometry("1075x585")
    window.configure(bg="#b8cce4")

    # ---------------------------------------------------------
    # Navigation
    # ---------------------------------------------------------
    menu_bar = tk.Menu(window)

    menu_bar.add_command(label="Account Creation")
    menu_bar.add_command(label="Log In")
    menu_bar.add_command(label="Notification")
    menu_bar.add_command(label="Template")
    menu_bar.add_command(label="Log Review")

    window.config(menu=menu_bar)

    # ---------------------------------------------------------
    # Main title
    # ---------------------------------------------------------
    title = tk.Label(
        window,
        text="Notification",
        font=("Arial", 28),
        bg="#b8cce4"
    )
    title.pack(pady=(8, 25))

    # Main content frame
    content = tk.Frame(window, bg="#b8cce4")
    content.pack(fill="both", expand=True, padx=85)

    # ---------------------------------------------------------
    # Template Name
    # ---------------------------------------------------------
    tk.Label(
        content,
        text="Template Name",
        font=("Arial", 12),
        bg="#b8cce4"
    ).place(x=5, y=0)

    template_combo = ttk.Combobox(
        content,
        width=23,
        state="readonly"
    )
    template_combo.place(x=165, y=0)

    # ---------------------------------------------------------
    # Subject
    # ---------------------------------------------------------
    tk.Label(
        content,
        text="Subject",
        font=("Arial", 12),
        bg="#b8cce4"
    ).place(x=5, y=46)

    subject_entry = tk.Entry(
        content,
        width=36,
        font=("Arial", 11)
    )
    subject_entry.place(x=165, y=46)

    # ---------------------------------------------------------
    # Message Box
    # ---------------------------------------------------------
    tk.Label(
        content,
        text="Message Box",
        font=("Arial", 12),
        bg="#b8cce4"
    ).place(x=5, y=90)

    message_frame = tk.Frame(
        content,
        bg="#b8cce4",
        bd=1,
        relief="solid"
    )
    message_frame.place(x=5, y=110, width=630, height=165)

    # Formatting toolbar
    toolbar = tk.Frame(
        message_frame,
        bg="#b8cce4",
        height=40
    )
    toolbar.pack(fill="x")

    tk.Button(
        toolbar,
        text="B",
        width=3,
        font=("Arial", 10, "bold")
    ).pack(side="left", padx=(175, 2), pady=7)

    tk.Button(
        toolbar,
        text="I",
        width=3,
        font=("Arial", 10, "italic")
    ).pack(side="left", padx=2, pady=7)

    tk.Button(
        toolbar,
        text="U",
        width=3,
        font=("Arial", 10, "underline")
    ).pack(side="left", padx=2, pady=7)

    tk.Button(
        toolbar,
        text="Insert Image",
        width=12
    ).pack(side="left", padx=5, pady=7)

    message_text = tk.Text(
        message_frame,
        wrap="word",
        font=("Arial", 11)
    )
    message_text.pack(fill="both", expand=True)

    # ---------------------------------------------------------
    # Food Availability
    # ---------------------------------------------------------
    food_frame = tk.LabelFrame(
        content,
        text="Food Availability",
        font=("Arial", 11),
        bg="#b8cce4"
    )
    food_frame.place(x=0, y=290, width=635, height=65)

    tk.Label(
        food_frame,
        text="Food Category",
        bg="#b8cce4"
    ).pack(side="left", padx=(8, 5))

    food_category = ttk.Combobox(
        food_frame,
        width=10,
        state="readonly"
    )
    food_category.pack(side="left")

    tk.Label(
        food_frame,
        text="Quantity",
        bg="#b8cce4"
    ).pack(side="left", padx=(15, 5))

    quantity = ttk.Combobox(
        food_frame,
        width=7,
        state="readonly"
    )
    quantity.pack(side="left")

    tk.Label(
        food_frame,
        text="Available Until",
        bg="#b8cce4"
    ).pack(side="left", padx=(15, 5))

    available_until = ttk.Combobox(
        food_frame,
        width=12,
        values=["10/5/2026"],
        state="readonly"
    )
    available_until.pack(side="left")

    # ---------------------------------------------------------
    # Location
    # ---------------------------------------------------------
    location_frame = tk.LabelFrame(
        content,
        text="Location",
        font=("Arial", 11),
        bg="#b8cce4"
    )
    location_frame.place(x=0, y=365, width=635, height=65)

    locations = [
        "All Campus",
        "Cascade",
        "Rock Creek",
        "South East",
        "Sylvana"
    ]

    for location in locations:
        tk.Checkbutton(
            location_frame,
            text=location,
            bg="#b8cce4",
            activebackground="#b8cce4"
        ).pack(side="left", padx=8)

    # ---------------------------------------------------------
    # Choose Format
    # ---------------------------------------------------------
    format_frame = tk.LabelFrame(
        content,
        text="Choose Format",
        font=("Arial", 11),
        bg="#b8cce4"
    )
    format_frame.place(x=750, y=195, width=145, height=75)

    format_choice = tk.StringVar(value="email")

    tk.Radiobutton(
        format_frame,
        text="E-mail",
        variable=format_choice,
        value="email",
        bg="#b8cce4",
        activebackground="#b8cce4"
    ).pack(anchor="w", padx=8)

    tk.Radiobutton(
        format_frame,
        text="SMS",
        variable=format_choice,
        value="sms",
        bg="#b8cce4",
        activebackground="#b8cce4"
    ).pack(anchor="w", padx=8)

    # ---------------------------------------------------------
    # Right-side buttons
    # ---------------------------------------------------------
    button_width = 18

    tk.Button(
        content,
        text="Clear Form",
        width=button_width
    ).place(x=750, y=135)

    tk.Button(
        content,
        text="Preview",
        width=button_width
    ).place(x=750, y=295)

    tk.Button(
        content,
        text="Send Notification",
        width=button_width
    ).place(x=750, y=360)

    window.mainloop()
