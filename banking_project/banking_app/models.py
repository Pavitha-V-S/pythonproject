from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
    ]

    MATERIALS_PROVIDED_CHOICES = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('cheque_book', 'Cheque Book'),
    ]

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # Note: In a real app, use a secure password hashing method
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age=models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    materials_provided = models.ManyToManyField('Material', blank=True)

    def __str__(self):
        return self.username


class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
