from django.test import TestCase

from test_yarned_app.models import Person
from test_yarned_app.models import Contact
from test_yarned_app.models import RequestSnapShot


class PersonInfoTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name="Yaroslav",
                                surname="NedashEx")
        self.cskype = Contact.objects.create(person=self.person,
                                ctype="skype", value="43534534534535")
        self.cjabber = Contact.objects.create(person=self.person,
                                ctype="jabber", value="qeqwe@111.com")

    def testCRUD(self):
        person_cur = Person.objects.get(surname="NedashEx")
        self.assertEqual(self.person, person_cur)
        contacts = self.person.contact_set.all()
        self.assertEqual(contacts.count(), 2)
        self.cskype.delete()
        contacts = self.person.contact_set.all()
        self.assertEqual(contacts.count(), 1)

    def testView(self):
        response = self.client.get('/')
        self.assertNotEqual(response.context['person'], None)
        self.assertEqual(response.context['person'].name, 'Yaroslav')
        res = response.content.find('Yaroslav')
        self.assertNotEqual(res, -1)
        res = response.content.find('Nedash')
        self.assertNotEqual(res, -1)


class MiddlewareTest(TestCase):
    def testCRUD(self):
        request_snap_shot = RequestSnapShot.objects.create()
        request_snap_shot_cur = RequestSnapShot.objects.get(id=1)
        self.assertEqual(request_snap_shot, request_snap_shot_cur)
        request_snap_shot_cur.path = '/path/'
        request_snap_shot_cur.save()
        request_snap_shot_cur = RequestSnapShot.objects.get(id=1)
        self.assertEqual(request_snap_shot_cur.path, '/path/')
        request_snap_shot_cur.delete()

    def testView(self):
        response = self.client.get('/requests/')
        requests = RequestSnapShot.objects.all()
        self.assertNotEqual(requests.count(), 0)
        self.assertNotEqual(response.context['requests'], None)


class ContextProcessorTest(TestCase):
    def testView(self):
        response = self.client.get('/')
        self.assertNotEqual(response.context['MEDIA_URL'], None)
        self.assertNotEqual(response.context['settings'], None)
