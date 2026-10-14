
# ******************************************************************************
# Programmer:   Yejide Momoh Gbada
#
# Date:         10/14/2026
#
# Description:  This program creates the graphical user interface (GUI) for
#               Portland Community College Food Pantry reusable Notification
#               Template.It allows the user(Manager/ staff) to create and manage
#               reusable template that can be used to send notification messages
#               to subscribed students about food availability without having to
#               write new messages from scratch all the time.
# ******************************************************************************

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class TemplateGUI:

    def __init__(self, root):
        """
        This function acts as the setup blueprint for the template GUI.
        It contains the main window settings.
        """

        self.root = root
        self.root.title("Template Manager")
        self.root.geometry("850x550")
        self.root.configure(bg="#b8cce4")
        self.all_templates = {}

        # -------------------------------------------------
        #  Horizontal Top Menu Bar
        # -------------------------------------------------
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        menu_bar.add_command(label="Account Creation")
        menu_bar.add_command(label="Log In")
        menu_bar.add_command(label="Notification")
        menu_bar.add_command(label="Template")
        menu_bar.add_command(label="Log Review")

        # -------------------------------------------------
        # Builds Main container with Padding and Page title
        # -------------------------------------------------

        main_frame = tk.Frame(self.root, bg="#b8cce4", padx=20, pady=10)
        main_frame.grid(row=0, column=0, sticky="nsew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # ------------------ TITLE ------------------

        title_label = tk.Label(
            main_frame,
            text="Template",
            font=("Arial", 24, "normal"),
            bg="#b8cce4",
            fg="black",
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="n")

        # -------------------------------------------------
        # Builds the Left side
        # -------------------------------------------------

        left_frame = tk.Frame(main_frame, bg="#b8cce4")
        left_frame.grid(row=1, column=0, sticky="nw", padx=(0, 20))

        # Template Name
        tk.Label(
            left_frame, text="Template Name", font=("Arial", 11), bg="#b8cce4"
        ).grid(row=0, column=0, sticky="w", pady=5)
        self.template_name_entry = tk.Entry(left_frame, width=35, font=("Arial", 11))
        self.template_name_entry.grid(row=0, column=1, columnspan=2, sticky="w", padx=10, pady=5)

        # Insert Tag
        tk.Label(
            left_frame, text="Insert Tags", font=("Arial", 11), bg="#b8cce4"
        ).grid(row=1, column=0, sticky="w", pady=5)
        self.tag_list = ["[Food Available]", "[Time]", "[Notification_Date]", "[Location]", "[Fruits]", "[Canned]",
                         "[Prepared Meal]"]

        self.insert_tags_combo = ttk.Combobox(
            left_frame, width=32, font=("Arial", 11), values=self.tag_list, state="readonly"
        )
        self.insert_tags_combo.set("Select Notification Tag")
        self.insert_tags_combo.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=5)
        self.insert_tags_combo.bind("<<ComboboxSelected>>", self.insert_tag_to_textbox)

        # Create Tag Entry + Add Tag Button

        tk.Label(left_frame, text="Create Tag", font=("Arial", 11), bg="#b8cce4").grid(row=2, column=0, sticky="w",
                                                                                       pady=5)
        self.create_tag_entry = tk.Entry(left_frame, width=20, font=("Arial", 11))
        self.create_tag_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        self.add_tag_btn = tk.Button(left_frame, text="Add Tag", font=("Arial", 10), width=10, bg="#e0e0e0",
                                     command=self.create_custom_tags)
        self.add_tag_btn.grid(row=2, column=2, sticky="w", pady=5)

        # Subject
        tk.Label(
            left_frame, text="Subject", font=("Arial", 11), bg="#b8cce4"
        ).grid(row=3, column=0, sticky="w", pady=5)
        self.subject_entry = tk.Entry(left_frame, width=35, font=("Arial", 11))
        self.subject_entry.grid(row=3, column=1, columnspan=2, sticky="w", padx=10, pady=5)

        # Message Box Label
        tk.Label(
            left_frame, text="Message Box", font=("Arial", 11), bg="#b8cce4"
        ).grid(row=4, column=0, sticky="nw", pady=(10, 0))
        message_frame = tk.Frame(left_frame, bg="white", bd=1, relief="solid")
        message_frame.grid(row=5, column=0, columnspan=3, sticky="w", pady=10)

        # Formatting Bar
        format_bar = tk.Frame(message_frame, bg="#f0f0f0", height=30)
        format_bar.pack(fill="x", side="top")

        btn_b = tk.Button(format_bar, text="B", font=("Arial", 9, "bold"), width=2, relief="flat", bg="#f0f0f0")
        btn_b.pack(side="left", padx=2)
        btn_i = tk.Button(format_bar, text="I", font=("Arial", 9, "italic"), width=2, relief="flat", bg="#f0f0f0")
        btn_i.pack(side="left", padx=2)
        btn_u = tk.Button(format_bar, text="U", font=("Arial", 9, "underline"), width=2, relief="flat", bg="#f0f0f0")
        btn_u.pack(side="left", padx=2)

        sep = tk.Label(format_bar, text="|", bg="#f0f0f0", fg="gray")
        sep.pack(side="left", padx=5)

        btn_img = tk.Button(format_bar, text="🖼 Insert Image", font=("Arial", 9), relief="flat", bg="#f0f0f0")
        btn_img.pack(side="left", padx=2)

        # Main Text Editor Area
        self.message_text = tk.Text(
            message_frame, width=55, height=12, font=("Arial", 11), wrap="word"
        )
        self.message_text.pack(fill="both", expand=True)

        # -------------------------------------------------
        # Builds the right side
        # -------------------------------------------------

        right_frame = tk.Frame(main_frame, bg="#b8cce4")
        right_frame.grid(row=1, column=1, sticky="ne", padx=(20, 0), pady=5)

        # Load Existing Template Header
        tk.Label(
            right_frame, text="Load Existing Template", font=("Arial", 11, "bold"), bg="#b8cce4"
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))

        # Select Template Dropdown
        tk.Label(
            right_frame, text="Select Template", font=("Arial", 10), bg="#b8cce4"
        ).grid(row=1, column=0, sticky="w", pady=5)
        self.select_template_combo = ttk.Combobox(
            right_frame, width=20, font=("Arial", 10)
        )
        self.select_template_combo.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------
        buttons_data = [
            ("Load Template", self.load_template),
            ("Save Template", self.save_template),
            ("Clear Template", self.clear_fields),
            ("Exit", self.root.quit),
        ]

        for idx, (btn_text, btn_cmd) in enumerate(buttons_data):
            btn = tk.Button(
                right_frame, text=btn_text, font=("Arial", 10), width=18, height=1, bg="#e8e8e8", command=btn_cmd
            )
            btn.grid(row=3 + idx, column=0, columnspan=2, pady=12, sticky="ew")

        # -------------------------------------------------
        # Functions
        # -------------------------------------------------

    def clear_fields(self):
        """Clears all UI fields and resets dropdown options with a popup alert."""
        self.template_name_entry.delete(0, tk.END)
        self.create_tag_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)
        self.insert_tags_combo.set("Select Notification Tag")
        self.select_template_combo.set("")
        messagebox.showinfo("Clear Complete", "All text fields have been reset successfully.")

    def save_template(self):
        """"
        This function is a validation and storage that saves user inputted fields,
        such as template name, Notification tags, subject and message text.
        :return: None
        """

        try:
            name = self.template_name_entry.get().strip()
            subject = self.subject_entry.get().strip()
            message = self.message_text.get("1.0", tk.END).strip()

            if not name or not subject or not message:
                messagebox.showwarning("Validation Error", " All fields"
                                                           "(Template Name, subject, and messagebox) must be filled.")
                return

            self.all_templates[name] = {
                "subject": subject,
                "message": message
            }

            self.select_template_combo.config(values=list(self.all_templates.keys()))
            messagebox.showinfo("Success", f"Template '{name}' has been saved successfully!")

        except Exception as e:
            print(f"Save helper log error: {e}")

    def create_custom_tags(self):
        """
        Reads text from entry box, adds to dropdown, and alerts user via validation popup.
        :return: None
        """
        try:
            new_tag = self.create_tag_entry.get().strip()
            if not new_tag:
                messagebox.showwarning("Tag Error", "Tag input field cannot be left blank.")
                return

            formatted_tag = f"{{{new_tag}}}"
            current_tags = [*self.insert_tags_combo.cget("values")]

            if formatted_tag in current_tags:
                messagebox.showwarning("Duplicate Tag", f"The tag '{formatted_tag}' already exists in your dropdown.")
                return

            current_tags.append(formatted_tag)
            self.insert_tags_combo.config(values=current_tags)
            self.create_tag_entry.delete(0, tk.END)
            messagebox.showinfo("Tag Added", f"Successfully added '{formatted_tag}' to your available tags list!")

        except Exception as e:
            print(f"Error creating tag: {e}")

    def insert_tag_to_textbox(self, event):
        """
        This function takes selected tag and apply it at the user's cursor point
        :return: None
        """
        selected_tag = self.insert_tags_combo.get()

        if selected_tag != "Select Notification Tag":
            try:
                self.message_text.insert(tk.INSERT, f" {selected_tag} ")
                self.message_text.focus_set()
            except Exception as e:
                print(f"Insertion helper log: {e}")
            self.root.after(500, lambda: self.insert_tags_combo.set("Select Notification Tag"))

    def load_template(self):
        """
        Loads template from text box and adds it to dropdown.
        :return: None
        """
        try:
            selected_name = self.select_template_combo.get().strip()

            if not selected_name or selected_name == "Select Template":
                messagebox.showwarning("Load Error", "Please select a template to load.")
                return
            if selected_name in self.all_templates:
                self.template_name_entry.delete(0, tk.END)
                self.subject_entry.delete(0, tk.END)
                self.message_text.delete("1.0", tk.END)

                template_data = self.all_templates[selected_name]
                self.template_name_entry.insert(0, selected_name)
                self.subject_entry.insert(0, template_data["subject"])
                self.message_text.insert("1.0", template_data["message"])
                messagebox.showinfo("Success", f"Template '{selected_name}' has been loaded successfully!")
            else:
                messagebox.showwarning("Load Error", "Template '{selected_name}' not found.")
        except Exception as e:
            print(f"Load template helper log error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemplateGUI(root)
    root.mainloop()
