from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import ListNames
from .forms import ListNamesForm


class NameTestCase(TestCase):
    def setUp(self):
        ListNames.objects.create(name='Donatello')

    def test_name_content(self):
        '''
        Test name creation.
        '''
        obj = ListNames.objects.get(name='Donatello')
        self.assertTrue(obj.name == 'Donatello')

    def test_string_representation(self):
        obj = ListNames.objects.get(name='Donatello')
        self.assertEqual(str(name), obj.name)

    def test_list_view(self):
        '''
        Test status code for list view.
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_notes_count(self):
        '''
        Checks count of the names.
        '''
        response = self.client.get('/')
        self.assertTrue('object_list' in response.context)
        object_list = ListNames.objects.count()
        object_list_from_context = len(response.context['object_list'])
        self.assertEqual(object_list, object_list_from_context)


class ListNamesFormTestCase(TestCase):
    def test_valid_form(self):
        '''
        Testing form validation.
        '''
        name = 'Michelangelo'
        obj = ListNames.objects.create(name=name)
        data = {'name': obj.name}
        form = ListNamesForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('name'), obj.name)
        self.assertNotEqual(form.cleaned_data.get("name"), "Leonardo")

    def test_invalid_form(self):
        '''
        Testing form invalidation.
        '''
        name = 'R'  # Less than 2 symbols
        obj = ListNames.objects.create(name=name)
        data = {'name': obj.name}
        form = ListNamesForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)

    def test_adding_new_note(self):
        '''
        Test name will be added succesfully to database.
        '''
        count = ListNames.objects.count()
        name = 'Raffaello'
        obj = ListNames.objects.create(name=name)
        data = {'name': obj.name}
        form = ListNamesForm(data=data)
        new_count = ListNames.objects.count()
        self.assertEqual(count+1, new_count)
