__author__ = 'Yejide Momohgbada'


class TemplateLogic:
    all_templates = {}
    DEFAULT_LOGS = ["Food Availability", "Fruits", "Vegetables", "Specials", "Location", "Date"]

    @staticmethod
    def validate_and_save(name, subject, message):
        """
        Checks if all fields are filled before saving to storage.
        :param name: String value, the name of the template.
        :param subject: String value, the subject of the template.
        :param message: string value, the message of the template.
        :return: None
        """
        if not name:
            return "ERROR_NAME"
        if not subject:
            return "ERROR_SUBJECT"
        if not message:
            return "ERROR_MESSAGE"

        TemplateLogic.all_templates[name] = {
            "subject": subject,
            "message": message
        }
        return "SUCCESS"

    @staticmethod
    def format_custom_tag(new_tag, current_dropdown_values):
        """
        Formats string inputs and checks duplicate bounds.
        """
        if not new_tag:
            return "ERROR_EMPTY"

        if new_tag in current_dropdown_values:
            return "ERROR_DUPLICATE"

        return "SUCCESS"

    @staticmethod
    def get_saved_template(selected_name):
        """
        Fetches stored profile profiles directly from the class dictionary.
        """
        if not selected_name or selected_name == "Select Template":
            return "ERROR_SELECTION"

        if selected_name in TemplateLogic.all_templates:
            return TemplateLogic.all_templates[selected_name]

        return "ERROR_MISSING"


