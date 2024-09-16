import unittest
from bs4 import BeautifulSoup

class TestUpdateBookingHTML(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the HTML file and create a BeautifulSoup object for parsing
        with open('update_booking.html', 'r') as file:
            cls.soup = BeautifulSoup(file, 'html.parser')

    def test_doctype(self):
        # Check if the doctype is present and correct
        doctype = str(self.soup).split('\n')[0]
        self.assertIn('<!DOCTYPE html>', doctype, "DOCTYPE declaration is missing or incorrect")

    def test_title(self):
        # Check if the title contains "Update Booking"
        title = self.soup.title.string
        self.assertEqual(title, 'Update Booking', "The title is incorrect")

    def test_form_method(self):
        # Check if the form method is POST
        form = self.soup.find('form')
        self.assertIsNotNone(form, "Form not found in the HTML")
        self.assertEqual(form.get('method'), 'POST', "Form method is not POST")

    def test_csrf_token(self):
        # Check if the CSRF token placeholder is present
        csrf_token = self.soup.find(text="{% csrf_token %}")
        self.assertIsNotNone(csrf_token, "CSRF token placeholder is missing")

    def test_submit_button(self):
        # Check if there is a submit button with the correct text
        submit_button = self.soup.find('button', type='submit')
        self.assertIsNotNone(submit_button, "Submit button is missing")
        self.assertEqual(submit_button.text.strip(), 'Update Booking', "Submit button text is incorrect")

    def test_cancel_link(self):
        # Check if the cancel link is present and contains the correct URL pattern
        cancel_link = self.soup.find('a', href="{% url 'view_booking' %}")
        self.assertIsNotNone(cancel_link, "Cancel link is missing")
        self.assertEqual(cancel_link.text.strip(), 'Cancel', "Cancel link text is incorrect")

    def test_custom_css(self):
        # Check if custom CSS is included
        custom_css = self.soup.find('link', href="{% static 'backgroundcode/CSS/style.css' %}")
        self.assertIsNotNone(custom_css, "Custom CSS link is missing or incorrect")


if __name__ == '__main__':
    unittest.main()
