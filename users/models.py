from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=25)
    date_of_birth = models.DateField(null=True, blank=True)


# blank: for form validation purposes. True means it allows empty values; False, it doesn't.
# null: for database validation. True means it will store values as NULL in DB; False will not.
# unique: to avoid duplication. True means it will not allow; False, yes.
