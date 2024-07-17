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