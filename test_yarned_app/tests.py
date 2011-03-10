from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.core import management
import sys
import StringIO

from test_yarned_app.models import Person, Contact, RequestSnapShot
from test_yarned_app.models import OperationLog


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
        self.assertEqual(response.context['settings'].TIME_ZONE,
                                settings.TIME_ZONE)


class EditPersonInfoTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('555', '555@5.com', '555')

    def testView(self):
        response = self.client.get('/person_info_edit/')
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/accounts/login/',
                                        {'username': '555', 'password': '555'})
        self.assertEqual(response.status_code, 302)
        res = response.content.find('password didn\'t match')
        self.assertEqual(res, -1)
        response = self.client.get('/person_info_edit/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nedash')

        #test reversed order input fields
        self.assertTrue(response.content.find('id_surname') >
                        response.content.find('id_bio'))

        #test template tag
        response = self.client.get('/')
        res = response.content.find('admin/test_yarned_app/person/1/')
        self.assertNotEqual(res, -1)

        response = self.client.post('/accounts/login/',
                             {'username': '333', 'password': '333'})
        self.assertEqual(response.status_code, 200)
        res = response.content.find('password didn\'t match')
        self.assertNotEqual(res, -1)
        response = self.client.post('/accounts/logout/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/person_info_edit/')
        self.assertEqual(response.status_code, 302)


class DjangoCommandTest(TestCase):
    def testCmd(self):
        sout = StringIO.StringIO()
        sys.stdout = sout
        management.call_command('printmodel')
        sys.stdout = sys.__stdout__

        contents = sout.getvalue()

        res = contents.find('Model:test_yarned.test_yarned_app.models')
        self.assertNotEqual(res, -1)
        res = contents.find('Person 1')
        self.assertNotEqual(res, -1)
        res = contents.find('Contact 4')
        self.assertNotEqual(res, -1)
        sout.close()


class SignalProcessorTest(TestCase):
    def setUp(self):
        self.person = Person.objects.get(surname="Nedash")
        self.cskype = Contact.objects.create(person=self.person,
                                ctype="skype", value="43534534534535")

    def testProc(self):
        log = OperationLog.objects.all()
        count = log.count()
        self.assertNotEqual(log.count(), 0)
        self.person.surname = "NedashEx"
        self.person.save()
        self.cskype.delete()
        log = OperationLog.objects.all()
        self.assertTrue(log.count() > count)
