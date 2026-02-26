from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    event_date = models.DateTimeField()

    def book_ticket(self, user):
        self.capacity = self.capacity - 1
        ticket  = Ticket(event=self, user=user)
        self.save()
        ticket.save()

    def get_event_detail(self):
        pass



TICKET_CHOICES = (
    ("PENDING" , "pending"),
    ("CONFIRMED" , "confirmed"),
    ("CANCELED" , "canceled"),
)

class Ticket(models.Model):
    event = models.ForeignKey(to=Event,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=TICKET_CHOICES, default="PENDING")

    def confirm_booking(self):
        self.status = TICKET_CHOICES.CONFIRMED
        self.save()

    def cancel_booking(self):
        self.event.capacity = self.event.capacity + 1
        self.status = TICKET_CHOICES.CANCELED
        self.event.save()
        self.save()
