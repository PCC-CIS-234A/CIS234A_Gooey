
# ******************************************************************************
# Programmer:   Yejide Momoh Gbada
#
# Date:         10/16/2026
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
from Logic import TemplateLogic


class TemplateGUI:
    """
    This function acts as the setup blueprint for the template GUI.
     It contains the main window settings.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Template Creation")
        self.root.geometry("1050x600")
        self.root.configure(bg="#b8cce4")

        # Link instantiation to manage clean system transactions
        self.logic = TemplateLogic()

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # -------------------------------------------------------------
        # Horizontal Top Menu Bar
        # -------------------------------------------------------------
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        menu_bar.add_command(label="Account Creation")
        menu_bar.add_command(label="Log In")
        menu_bar.add_command(label="Notification")
        menu_bar.add_command(label="Template")
        menu_bar.add_command(label="Log Review")

        # -------------------------------------------------------------
        # Main Layout Grid
        # -------------------------------------------------------------
        main_frame = tk.Frame(self.root, bg="#b8cce4", padx=30, pady=20)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=3)

        # Header Title
        header_lbl = tk.Label(main_frame, text="Template", font=("Arial", 25, "bold"), bg="#b8cce4", fg="#333333")
        header_lbl.grid(row=0, column=0, columnspan=3, pady=(0, 25))

        # -------------------------------------------------------------
        # Builds the Left Column of GUI
        # lbl represents Label
        # btn represents Button
        # -------------------------------------------------------------
        left_frame = tk.Frame(main_frame, bg="#b8cce4")
        left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 30))
        left_frame.columnconfigure(0, weight=0)
        left_frame.columnconfigure(1, weight=3)
        left_frame.columnconfigure(2, weight=1)

        # Template Name Input
        lbl_template_name = tk.Label(left_frame, text="Template Name", font=("Arial", 11), bg="#b8cce4")
        lbl_template_name.grid(row=0, column=0, sticky="w", pady=8)
        self.template_name_entry = tk.Entry(left_frame, font=("Arial", 11))
        self.template_name_entry.grid(row=0, column=1, sticky="ew", pady=8, padx=(10, 0))

        # Insert Tags List Combo Dropdown
        lbl_insert_tags = tk.Label(left_frame, text="Insert Tags", font=("Arial", 11), bg="#b8cce4")
        lbl_insert_tags.grid(row=1, column=0, sticky="w", pady=8)
        self.select_log_combobox = ttk.Combobox(left_frame, values=TemplateLogic.DEFAULT_LOGS, font=("Arial", 11),
                                                state="readonly")
        self.select_log_combobox.set("Select Notification Tag")
        self.select_log_combobox.grid(row=1, column=1, sticky="ew", pady=8, padx=(10, 0))
        self.select_log_combobox.bind("<<ComboboxSelected>>", self.select_log_combobox_select)

        # Create Tag & Add Tag
        lbl_create_tag = tk.Label(left_frame, text="Create Tag", font=("Arial", 11), bg="#b8cce4")
        lbl_create_tag.grid(row=2, column=0, sticky="w", pady=8)

        tag_input_frame = tk.Frame(left_frame, bg="#b8cce4")
        tag_input_frame.grid(row=2, column=1, sticky="ew", pady=8, padx=(10, 0))
        tag_input_frame.columnconfigure(0, weight=1)

        self.create_log_entry = tk.Entry(tag_input_frame, font=("Arial", 11))
        self.create_log_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        btn_add_tag = tk.Button(tag_input_frame, text="Add Tag", font=("Arial", 10), command=self.add_custom_logs,
                                width=10)
        btn_add_tag.grid(row=0, column=1, sticky="e")

        # Subject Entry Field
        lbl_subject = tk.Label(left_frame, text="Subject", font=("Arial", 11), bg="#b8cce4")
        lbl_subject.grid(row=3, column=0, sticky="w", pady=8)
        self.subject_entry = tk.Entry(left_frame, font=("Arial", 11))
        self.subject_entry.grid(row=3, column=1, columnspan=2, sticky="ew", pady=8, padx=(10, 0))

        # Rich-Text Message Box (lbl means label)
        lbl_message_box = tk.Label(left_frame, text="Message Box", font=("Arial", 11), bg="#b8cce4")
        lbl_message_box.grid(row=4, column=0, sticky="nw", pady=(10, 2))

        message_container = tk.Frame(left_frame, bg="#ffffff", bd=1, relief="solid")
        message_container.grid(row=4, column=1, columnspan=2, sticky="nsew", pady=(10, 2), padx=(10, 0))
        message_container.columnconfigure(0, weight=1)

        toolbar = tk.Frame(message_container, bg="#f0f0f0", height=26)
        toolbar.grid(row=0, column=0, sticky="ew")

        btn_b = tk.Button(toolbar, text="B", font=("Arial", 9, "bold"), relief="flat", bg="#f0f0f0", width=3)
        btn_b.grid(row=0, column=0, padx=2, pady=2)
        btn_i = tk.Button(toolbar, text="I", font=("Arial", 9, "italic"), relief="flat", bg="#f0f0f0", width=3)
        btn_i.grid(row=0, column=1, padx=2, pady=2)
        btn_u = tk.Button(toolbar, text="U", font=("Arial", 9, "underline"), relief="flat", bg="#f0f0f0", width=3)
        btn_u.grid(row=0, column=2, padx=2, pady=2)

        self.message_text = tk.Text(message_container, height=12, font=("Arial", 11), bd=0)
        self.message_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # -------------------------------------------------------------
        # Builds right column (Template Controls Panel)
        # lbl represents Label
        # btn represents Button
        # -------------------------------------------------------------

        right_frame = tk.Frame(main_frame, bg="#b8cce4")
        right_frame.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
        right_frame.columnconfigure(0, weight=1)

        # Section Header Text Item
        lbl_load_section = tk.Label(right_frame, text="Load Existing Template", font=("Arial", 12, "bold"),
                                    bg="#b8cce4", wraplength=180, justify="left")
        lbl_load_section.grid(row=0, column=0, sticky="w", pady=(0, 15))

        # Select Template
        self.select_template_combobox = ttk.Combobox(right_frame, font=("Arial", 11), state="readonly", width=30)
        self.select_template_combobox.set("Select Template")
        self.select_template_combobox.grid(row=1, column=0, sticky="ew", pady=(0, 25))
        self.select_template_combobox.bind("<<ComboboxSelected>>", self.load_template)

        # Buttons for Template interface ( btn means Button)
        btn_load = tk.Button(right_frame, text="Load Template", font=("Arial", 11), height=2,
                             command=lambda: self.load_template(None))
        btn_load.grid(row=2, column=0, sticky="ew", pady=8)

        btn_save = tk.Button(right_frame, text="Save Template", font=("Arial", 11), height=2,
                             command=self.save_template)
        btn_save.grid(row=3, column=0, sticky="ew", pady=8)

        btn_clear = tk.Button(right_frame, text="Clear Template", font=("Arial", 11), height=2,
                              command=self.clear_entries)
        btn_clear.grid(row=4, column=0, sticky="ew", pady=8)

        btn_exit = tk.Button(right_frame, text="Exit", font=("Arial", 11), height=2, command=self.root.quit)
        btn_exit.grid(row=5, column=0, sticky="ew", pady=(40, 8))

    # -------------------------------------------------------------
    # Functions
    # -------------------------------------------------------------
    def clear_entries(self):
        """
        Clears all UI fields and resets dropdown options with a popup alert.
        :return:None
        """
        self.template_name_entry.delete(0, tk.END)
        self.create_log_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)
        self.select_log_combobox.set("Select Notification Tag")
        self.select_template_combobox.set("Select Template")

    def save_template(self):
        """
        This function validates and saves user inputted fields,
        such as template name, Notification tags, subject and message text.
        :return: None
        """
        name = self.template_name_entry.get().strip()
        subject = self.subject_entry.get().strip()
        message = self.message_text.get("1.0", tk.END).strip()
        result_code = TemplateLogic.validate_and_save(name, subject, message)

        if result_code == "ERROR_NAME":
            messagebox.showerror("Error", "Template name cannot be left blank.")
        elif result_code == "ERROR_SUBJECT":
            messagebox.showerror("Error", "Template subject cannot be left blank.")
        elif result_code == "ERROR_MESSAGE":
            messagebox.showerror("Error", "Template message cannot be left blank.")
        elif result_code == "SUCCESS":
            self.select_template_combobox.config(values=list(TemplateLogic.all_templates.keys()))
            messagebox.showinfo("Success", f"Template'{name} successfully saved.")

    def add_custom_logs(self):
        """
        This function passes custom user tag options through input validation.
        """
        new_tag = self.create_log_entry.get().strip()
        current_dropdown_values = list(self.select_log_combobox["values"])
        result_code = TemplateLogic.format_custom_tag(new_tag, current_dropdown_values)

        if result_code == "ERROR_EMPTY":
            messagebox.showerror("Error", "Tag input field cannot be empty")
        elif result_code == "ERROR_DUPLICATE":
            messagebox.showerror("Error", "Tag input already exists")
        elif result_code == "SUCCESS":
            current_dropdown_values.append(new_tag)
            self.select_log_combobox.config(values=current_dropdown_values)
            messagebox.showinfo("Success", f" New tag'{new_tag}' successfully added")
            self.create_log_entry.delete(0, tk.END)

    def select_log_combobox_select(self, event):
        """
        This function selects a log entry from the dropdown menu.
        """
        selected_log = self.select_log_combobox.get()
        if selected_log != "Select Notification Tag":
            self.message_text.insert(tk.END, f" [{selected_log}] ")

    def load_template(self, event):
        """
        This function loads a template from the dropdown menu.
        """
        try:
            selected_name = self.select_template_combobox.get().strip()
            result = TemplateLogic.get_saved_template(selected_name)

            if result == "ERROR_SELECTION" or result == "ERROR_MISSING":
                messagebox.showwarning("Load Error", "Please select a valid template.")
                return

            self.template_name_entry.delete(0, tk.END)
            self.subject_entry.delete(0, tk.END)
            self.message_text.delete("1.0", tk.END)

            self.template_name_entry.insert(0, selected_name)
            self.subject_entry.insert(0, result["subject"])
            self.message_text.insert(tk.END, result["message"])
            messagebox.showinfo("Success", f"Template '{selected_name}' loaded successfully")

        except Exception as e:
            messagebox.showwarning("Load Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = TemplateGUI(root)
    root.mainloop()
