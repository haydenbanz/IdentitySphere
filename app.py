import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QIcon  # Import QIcon
from faker import Faker
from faker.providers import bank, company, credit_card, currency, geo, internet, isbn, job, passport, person, phone_number, user_agent

class IdentityGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Identity Generator')
        self.setWindowIcon(QIcon('icon.png'))  # Set the application icon
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit()
        self.generate_button = QPushButton('Generate Identity')
        self.generate_button.clicked.connect(self.generate_identity)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def generate_identity(self):
        faker = Faker()
        faker.add_provider(bank)
        faker.add_provider(company)
        faker.add_provider(credit_card)
        faker.add_provider(currency)
        faker.add_provider(geo)
        faker.add_provider(internet)
        faker.add_provider(isbn)
        faker.add_provider(job)
        faker.add_provider(passport)
        faker.add_provider(person)
        faker.add_provider(phone_number)
        faker.add_provider(user_agent)

        identity = f"Name: {faker.name()}\n"
        identity += f"Address: {faker.address()}\n"
        identity += f"Date of Birth: {faker.date_of_birth()}\n"
        identity += f"Email: {faker.email()}\n"
        identity += f"Phone Number: {faker.phone_number()}\n"
        identity += f"Social Security Number: {faker.ssn()}\n"
        identity += f"Company: {faker.company()}\n"
        identity += f"Credit Card Number: {faker.credit_card_number()}\n"
        identity += f"Currency Code: {faker.currency_code()}\n"
        identity += f"Country: {faker.country()}\n"
        identity += f"ISBN Number: {faker.isbn13()}\n"
        identity += f"Job Title: {faker.job()}\n"
        identity += f"Passport Number: {faker.passport_number()}\n"
        identity += f"Username: {faker.user_name()}\n"
        identity += f"User Agent: {faker.user_agent()}\n"

        self.text_edit.setPlainText(identity)

def main():
    app = QApplication(sys.argv)
    window = IdentityGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
