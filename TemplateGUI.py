# ******************************************************************************
# Programmer:   Yejide Momoh Gbada
#
# Date:         10/13/2026
#
# Description:  This program is the graphical user interface (GUI) for Portland
#               Community College Food Pantry Notification Template.It allows
#               the user(Manager) to create and manage reusable template that
#               will be used to send notification messages to subscribers about
#               food availability messages.
#
# ******************************************************************************

import tkinter as tk
from tkinter import ttk, messagebox


class TemplateGUI(tk.Tk):

    def __init__(self):
        """
        This function acts as the setup blueprint for the template GUI.
        It contains the main window settings.
        """
        super().__init__()
        self.title("PCC Food Pantry - Template")
        self.geometry("1100x600")
        self.minsize(900, 600)
        self.configure(bg="#b8cce4")
        self.build_menu()
        self.build_gui()

    # -------------------------------------------------
    # Top Menu Bar
    # -------------------------------------------------
    def build_menu(self):
        bar = tk.Frame(self, bg="#e6e6e6")
        bar.pack(fill="x")

        for name in ["Account Creation", "Log In", "Notification", "Template", "Log Review"]:
            tk.Button(
                bar,
                text=name,
                bd=0,
                bg="#e6e6e6",
                command=lambda n=name:
                messagebox.showinfo(
                    "Navigation",
                    n + " page selected."
                )
            ).pack(side="left", padx=7, pady=6)

    def build_gui(self):
        # Stores templates while application is running
        saved_templates = {}

        # -------------------------------------------------
        # Functions
        # -------------------------------------------------
        def format_text(fmt):
            """
            This function applies rich text styling to selected text
            :param fmt: Specifically bold, italic, underline
            :return:None
            """
            try:
                start = message.index("sel.first")
                end = message.index("sel.last")

                tag = {
                    "B": "bold",
                    "I": "italic",
                    "U": "underline"
                }[fmt]

                message.tag_configure(
                    tag,
                    font=(
                        "Arial",
                        11,
                        "bold" if fmt == "B"
                        else "italic" if fmt == "I"
                        else "normal"
                    ),
                    underline=(fmt == "U")
                )

                message.tag_add(tag, start, end)

            except tk.TclError:
                pass

        def save_template():
            """
            This function is a validation and storage that saves user inputted fields,
            such as template name, Notification tags, subject and message text.
            :return: None
            """
            name = template_name.get().strip()
            tag = tags.get().strip()
            subject_text = subject.get().strip()
            message_text = message.get("1.0", "end-1c").strip()

            if not name:
                messagebox.showerror("Missing name", "Please enter a template name")
                template_name.focus_set()
                return

            if not tag or tag == "Select Notification Tag":
                messagebox.showerror("Missing information", "Please select a notification tag")
                tags.focus_set()
                return

            if not subject_text:
                messagebox.showerror("Missing information", "Please enter a subject ")
                subject.focus_set()
                return

            if not message_text:
                messagebox.showerror("Missing information", "Please enter a message")
                message.focus_set()
                return

            # saved_template.append((name, tag, subject_text, message))
            saved_templates[name] = {"tag": tag, "subject": subject_text, "message": message_text}

            # update the template selection list.
            names = sorted(saved_templates.keys())
            select_template["values"] = names
            template_name["values"] = names

            status.delete(0, "end")
            status.insert(0, "Saved")

            messagebox.showinfo("Template ", "Template saved successfully")

        def delete_template():
            """
            This function confirm and delete the selected template
            :return:None
            """
            if messagebox.askyesno("Delete Template", "Delete this template?"):
                clear_template()

                status.delete(0, "end")
                status.insert(0, "Deleted")

        def clear_template():
            """
            This function clear selected template input field.
            :return:None
            """
            template_name.set("")
            tags.set("Select Notification Tag")
            subject.delete(0, "end")
            message.delete("1.0", "end")

        def load_template(event=None):
            """
            Load the selected template into the editor
            :param event: Which UI event cause this function call.
            """

            name = select_template.get().strip()
            if not name:
                messagebox.showerror("Missing information", "Select a Template to load")
                return
            if name in saved_templates:
                data = saved_templates[name]
                template_name.set(name)
                tags.set(data["tag"])

                subject.delete(0, "end")
                subject.insert(0, data["subject"])

                message.delete("1.0", "end")
                message.insert("1.0", data["message"])

                status.delete(0, "end")
                status.insert(0, "Loaded")

            else:
                messagebox.showerror("Template not found", "This Template has not been saved yet.")

        # -------------------------------------------------
        #  Builds the Page Title
        # -------------------------------------------------

        tk.Label(
            self,
            text="Template",
            font=("Arial", 30),
            bg="#b8cce4",
        ).pack(pady=(28, 18))

        # -------------------------------------------------
        # Builds the Main Area
        # -------------------------------------------------

        main_frame = tk.Frame(self, bg="#b8cce4")
        main_frame.pack(
            fill="both",
            expand=True,
            padx=55,
            pady=10
        )

        # -------------------------------------------------
        # Builds the Left Side
        # -------------------------------------------------

        left = tk.Frame(main_frame, bg="#b8cce4")
        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 30)
        )

        # For Template Name combo box
        tk.Label(
            left,
            text="Template Name",
            font=("Arial", 13),
            bg="#b8cce4",
        ).grid(row=0, column=0, sticky="w", pady=14)

        template_name = ttk.Combobox(
            left,
            width=50
        )
        template_name.grid(
            row=0,
            column=1,
            sticky="w",
            padx=20
        )

        # For Tags combobox
        tk.Label(
            left,
            text="Tags",
            font=("Arial", 13),
            bg="#b8cce4",
        ).grid(row=1, column=0, sticky="w", pady=14)

        tags = ttk.Combobox(
            left,
            width=25,
            values=["Food Availability", "Fruits", "Vegetables", "Canned Food", "Dry Food", "Prepared Meals",
                    "Date and Time", "Location"]
        )
        tags.set("Fruits and Vegetables")

        tags.grid(
            row=1,
            column=1,
            sticky="w",
            padx=20
        )

        #  For the Subject text box
        tk.Label(
            left,
            text="Subject",
            font=("Arial", 13),
            bg="#b8cce4",
        ).grid(row=2, column=0, sticky="w", pady=14)

        subject = tk.Entry(
            left,
            width=62,
            font=("Arial", 11)
        )

        subject.grid(
            row=2,
            column=1,
            sticky="w",
            padx=20
        )

        # For Message Rich textBox
        tk.Label(
            left,
            text="Message Box",
            font=("Arial", 13),
            bg="#b8cce4",
        ).grid(
            row=3,
            column=0,
            sticky="nw",
            pady=14
        )

        editor = tk.Frame(
            left,
            bg="white",
            bd=1,
            relief="solid"
        )

        editor.grid(
            row=3,
            column=1,
            sticky="w",
            padx=20
        )

        # Formatting Toolbar in the message textbox
        toolbar = tk.Frame(
            editor,
            bg="#f2f2f2"
        )
        # Container frame for the buttons in the message box
        toolbar.pack(expand=True)

        # Create buttons
        col = 1
        for t in ["B", "I", "U"]:
            btn = tk.Button(
                toolbar,
                text=t,
                width=3,
                bd=0,
                font=(
                    "Arial",
                    10,
                    "bold" if t == "B" else "normal"
                ),
                command=lambda x=t: format_text(x)
            )

            btn.grid(row=0, column=col, padx=5)
            col += 1

        # Insert Image
        b4 = tk.Button(
            toolbar,
            text="Insert Image",
            bd=0,
            command=lambda:
            messagebox.showinfo(
                "Insert Image",
                "Connect this button to a file picker when needed."
            )
        )

        b4.grid(row=0, column=col, padx=5)
        toolbar.grid_columnconfigure(0, weight=1)
        toolbar.grid_columnconfigure(5, weight=1)

        # Message Text Box
        message = tk.Text(
            editor,
            width=62,
            height=12,
            font=("Arial", 11),
            wrap="word",
            bd=0
        )
        message.pack(
            padx=2,
            pady=2
        )

        # -------------------------------------------------
        # Builds the Right Side of the Template
        # -------------------------------------------------

        right = tk.Frame(
            main_frame,
            bg="#b8cce4",
        )
        right.pack(
            side="right",
            fill="both", expand=True
        )

        # Load Existing Template
        box = tk.LabelFrame(
            right,
            text="Load Existing Template",
            font=("Arial", 12),
            bg="#b8cce4",
            padx=18,
            pady=14
        )
        box.pack(fill="x")
        box.grid_columnconfigure(1, weight=1)

        # Select Template

        tk.Label(
            box,
            text="Select Template",
            bg="#b8cce4",
            font=("Arial", 11)
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=9
        )

        select_template = ttk.Combobox(
            box,
            width=25,
            values=["Food Availability", "Weekly Produce", "Specials", "Location"]
        )

        select_template.grid(
            row=0,
            column=1,
            padx=12,
            sticky="ew", pady=9
        )

        select_template.bind(
            "<<ComboboxSelected>>",
            load_template
        )

        # Last Updated
        tk.Label(
            box,
            text="Last updated:",
            bg="#b8cce4",
            font=("Arial", 11)
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=9
        )

        last_updated = tk.Entry(
            box,
            width=27
        )

        last_updated.insert(
            0,
            "MM/DD/YYYY"
        )

        last_updated.grid(
            row=1,
            column=1,
            padx=12
        )

        # Status
        tk.Label(
            box,
            text="Status:",
            bg="#b8cce4",
            font=("Arial", 11)
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=9
        )

        status = tk.Entry(
            box,
            width=27
        )

        status.insert(
            0,
            "Ready..."
        )

        status.grid(
            row=2,
            column=1,
            padx=12
        )

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        buttons = [
            ("Save Template", save_template),
            # ("Delete Template", delete_template),
            ("Clear Template", clear_template),
            ("Exit", self.destroy)

        ]

        for text, command in buttons:
            tk.Button(
                right,
                text=text,
                width=25,
                font=("Arial", 11),
                command=command
            ).pack(pady=9)


if __name__ == "__main__":
    TemplateGUI().mainloop()
