import unittest
from bs4 import BeautifulSoup

class TestHTML(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the HTML file and create a BeautifulSoup object for parsing
        with open('create_booking.html', 'r') as file:
            cls.soup = BeautifulSoup(file, 'html.parser')

    def test_doctype(self):
        # Check if the doctype is present and correct
        doctype = str(self.soup).split('\n')[0]
        self.assertIn('<!DOCTYPE html>', doctype, "DOCTYPE declaration is missing or incorrect")

    def test_title(self):
        # Check if the title contains "Create Booking"
        title = self.soup.title.string
        self.assertEqual(title, 'Create Booking', "The title is incorrect")

    def test_bootstrap_inclusion(self):
        # Check if the Bootstrap CSS is included correctly
        bootstrap_link = self.soup.find('link', href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css")
        self.assertIsNotNone(bootstrap_link, "Bootstrap CSS link is missing or incorrect")

    def test_form_method(self):
        # Check if the form method is POST
        form = self.soup.find('form')
        self.assertIsNotNone(form, "Form not found in the HTML")
        self.assertEqual(form.get('method'), 'post', "Form method is not POST")

    def test_csrf_token(self):
        # Check if the CSRF token placeholder is present
        csrf_token = self.soup.find(text="{% csrf_token %}")
        self.assertIsNotNone(csrf_token, "CSRF token placeholder is missing")

    def test_form_errors(self):
        # Check if the form error block is present
        form_errors = self.soup.find('div', class_='alert alert-danger')
        self.assertIsNotNone(form_errors, "Form error block is missing")

    def test_submit_button(self):
        # Check if there is a submit button with the btn-primary class
        submit_button = self.soup.find('button', type='submit')
        self.assertIsNotNone(submit_button, "Submit button is missing")
        self.assertIn('btn-primary', submit_button.get('class', []), "Submit button does not have 'btn-primary' class")

    def test_custom_css(self):
        # Check if custom CSS is included
        custom_css = self.soup.find('link', href="{% static 'backgroundcode/CSS/style.css' %}")
        self.assertIsNotNone(custom_css, "Custom CSS link is missing or incorrect")


if __name__ == '__main__':
    unittest.main()
