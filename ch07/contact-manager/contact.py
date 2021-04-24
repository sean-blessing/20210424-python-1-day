class Contact:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def __str__(self):
        print(f"Contact Details:\nFName: {self.first_name}\n"
              f"LName: {self.last_name}\n"
              f"Email: {self.email}\n"
              f"Phone: {self.phone}")
