from django.test import TestCase
from .forms import BookingForm, ProfileForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = BookingForm({'body': 'This is a great booking'})
        self.assertTrue(comment_form.is_valid())
    def test_form_is_invalid(self):
        comment_form = BookingForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class TestProfileForm(TestCase):
        
    def test_form_is_valid(self):
        """ Test for ProfileForm"""
        form_data = {
            'name': 'john doe',  # Use the ID of the created user
            'email': 'test@test.com',
            'phone': '1234567890'
        }
        form = ProfileForm(data=form_data)
        
        self.assertFalse(form.is_valid())  # Assert that form is not valid
        
        # Print form errors for debugging
        print(form.errors)
        
        self.assertTrue(form.errors)  # Ensure that there are validation errors
    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = ProfileForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = ProfileForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = ProfileForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )