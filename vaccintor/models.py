from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField
from decimal import Decimal
from datetime import date
from datetime import timedelta

# Create your models here.

class Parent(models.Model):
    # User contains first name, last name, email, pw
    user = models.ForeignKey(User)
    phone_number = PhoneNumberField()
    address = AddressField()
    doctors = models.ForeignKey('Doctor', related_name='Patients', related_query_name='patient', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

class Child(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField()
    parent = models.ForeignKey(Parent, related_name='children', related_query_name='child')

    class Meta:
        verbose_name_plural = "Children"

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} - child of {}".format(self.full_name, str(self.parent))

    def save(self, *args, **kwargs):
        create_completions = False
        if not self.pk:
            create_completions = True
        super(Child, self).save(*args, **kwargs)
        if create_completions:
            for vaccine in Vaccine.objects.all():
                vc = VaccineCompletion(child=self, vaccine=vaccine, completed=False, needed_before_registration=False)
                vc.save()

class Doctor(models.Model):
    # User contains first name, last name, email, pw
    user = models.ForeignKey(User)
    phone_number = PhoneNumberField()
    address = AddressField()

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

class Vaccine(models.Model):
    complex_name = models.CharField(max_length=100)
    simple_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    age_days = models.PositiveSmallIntegerField()
    cost = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    subsidized = models.BooleanField()

    def __str__(self):
        return "{} ({}) - ${}".format(self.complex_name, self.simple_name, self.cost)

    def save(self, *args, **kwargs):
        create_completions = False
        if not self.pk:
            create_completions = True
        super(Vaccine, self).save(*args, **kwargs)
        if create_completions:
            for child in Child.objects.all():
                vc = VaccineCompletion(child=child, vaccine=self, completed=False, needed_before_registration=False)
                vc.save()

class VaccineCompletion(models.Model):
    """
    When a child object is created, it will also be given a VaccineCompletion for each vaccine. (or vice versa)
    """
    child = models.ForeignKey(Child)
    vaccine = models.ForeignKey(Vaccine)
    completed = models.BooleanField(default=False)
    needed_before_registration = models.BooleanField(default=False)

    @property
    def days_until_needed(self):
        return (date.today() - self.child.dob - timedelta(days=self.vaccine.age_days)).days * -1

    @property
    def needed(self):
        return self.days_until_needed <= 0

    def __str__(self):
        return "{} {}".format(self.child.full_name, self.vaccine.simple_name)
