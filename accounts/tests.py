
from django.test import TestCase
from accounts.models import Reservation
from django.utils import timezone
from django.core.urlresolvers import reverse
from accounts.forms import ReservationForm

# Create your tests here.
class Test(TestCase):

    def create_Reservation(self, name="only a test", surname="yes, this is only a test"):
        return Reservation.objects.create(name=name, surname=surname, created_at=timezone.now())

    def forms_creation(self):
        w = self.create_Reservation()
        self.assertTrue(isinstance(w,ReservationForm))
        self.assertEqual(w.__unicode__(), w.title)