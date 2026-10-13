import tkinter as tk
from tkinter import ttk, messagebox


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
    ).place(x=5, y=80)

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
        state="readonly",
        values=[
            "Produce",
            "Dairy",
            "Meat",
            "Bakery",
            "Canned Goods",
            "Dry Goods",
            "Frozen",
            "Other"
        ]
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
        state="readonly",
        values=[
            "1-10",
            "11-25",
            "26-50",
            "51-100",
            "100+"
        ]
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
        values=[
            "10/14/2026",
            "10/15/2026",
            "10/16/2026",
            "10/17/2026",
            "10/18/2026"
        ],
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

    location_vars = {}

    def update_locations(location):
        """Select all campuses when All Campus is checked."""
        if location == "All Campus":
            select_all = location_vars["All Campus"].get()

            for campus, variable in location_vars.items():
                variable.set(select_all)
        else:
            location_vars["All Campus"].set(False)

    for location in locations:
        location_vars[location] = tk.BooleanVar()

        tk.Checkbutton(
            location_frame,
            text=location,
            variable=location_vars[location],
            command=lambda name=location: update_locations(name),
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
    # Button functions
    # ---------------------------------------------------------

    def validate_notification():
        """Check that all required notification fields are filled in."""
        subject = subject_entry.get().strip()
        message = message_text.get("1.0", tk.END).strip()

        if not subject:
            messagebox.showerror(
                "Missing Subject",
                "Please enter a notification subject."
            )
            subject_entry.focus_set()
            return False

        if not message:
            messagebox.showerror(
                "Missing Message",
                "Please enter a notification message."
            )
            message_text.focus_set()
            return False

        if not food_category.get():
            messagebox.showerror(
                "Missing Food Category",
                "Please select a food category."
            )
            food_category.focus_set()
            return False

        if not quantity.get():
            messagebox.showerror(
                "Missing Quantity",
                "Please select a quantity."
            )
            quantity.focus_set()
            return False

        if not available_until.get():
            messagebox.showerror(
                "Missing Availability Date",
                "Please select an available-until date."
            )
            available_until.focus_set()
            return False

        selected_locations = [
            location for location, variable in location_vars.items()
            if variable.get()
        ]

        if not selected_locations:
            messagebox.showerror(
                "Missing Location",
                "Please select at least one campus."
            )
            return False

        return True

    def preview_notification():
        """Display a preview of the notification."""
        subject = subject_entry.get().strip()
        message = message_text.get("1.0", tk.END).strip()

        if not validate_notification():
            return

        selected_locations = [
            location for location, variable in location_vars.items()
            if variable.get()
        ]

        preview = (
            f"Subject: {subject}\n\n"
            f"Message:\n{message}\n\n"
            f"Format: {format_choice.get().upper()}\n"
            f"Food Category: {food_category.get() or 'Not selected'}\n"
            f"Quantity: {quantity.get() or 'Not selected'}\n"
            f"Available Until: {available_until.get() or 'Not selected'}\n"
            f"Locations: {', '.join(selected_locations) or 'None selected'}"
        )

        messagebox.showinfo("Notification Preview", preview)

    def clear_form():
        """Clear the subject and message fields."""
        subject_entry.delete(0, tk.END)
        message_text.delete("1.0", tk.END)
        template_combo.set("")
        food_category.set("")
        quantity.set("")
        available_until.set("")
        format_choice.set("email")

    def send_notification():
        """Validate the notification before sending."""
        if not validate_notification():
            return

        subject = subject_entry.get().strip()
        message = message_text.get("1.0", tk.END).strip()
        category = food_category.get()
        food_quantity = quantity.get()
        available_date = available_until.get()

        selected_locations = [
            location for location, variable in location_vars.items()
            if variable.get() and location != "All Campus"
        ]

        messagebox.showinfo(
            "Notification Ready",
            "Your notification passed validation.\n\n"
            f"Subject: {subject}\n"
            f"Food Category: {category}\n"
            f"Quantity: {food_quantity}\n"
            f"Available Until: {available_date}\n"
            f"Locations: {', '.join(selected_locations)}\n"
            f"Format: {format_choice.get().upper()}\n\n"
            "No email or SMS has been sent yet."
        )

    # ---------------------------------------------------------
    # Right-side buttons
    # ---------------------------------------------------------
    button_width = 18

    tk.Button(
        content,
        text="Clear Form",
        width=button_width,
        command=clear_form
    ).place(x=750, y=135)

    tk.Button(
        content,
        text="Preview",
        width=button_width,
        command=preview_notification
    ).place(x=750, y=295)

    tk.Button(
        content,
        text="Send Notification",
        width=button_width,
        command=send_notification
    ).place(x=750, y=360)

    window.mainloop()
