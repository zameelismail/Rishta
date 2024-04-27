from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=25)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    # Basic
    Phone_Number = models.CharField(max_length=25)
    Age = models.CharField(max_length=25)
    Height = models.CharField(max_length=25)
    Weight = models.CharField(max_length=25)
    Blood_Group = models.CharField(max_length=25)
    Marital_Status = models.CharField(max_length=25)
    Nationality = models.CharField(max_length=25)
    My_Complexion = models.CharField(max_length=25)
    Workout = models.CharField(max_length=25)
    Smoke = models.CharField(max_length=25)
    # Religious and astro
    Time_of_Birth = models.CharField(max_length=25)
    Date_of_Birth = models.CharField(max_length=25)
    City = models.CharField(max_length=25)
    State = models.CharField(max_length=25)
    Religion = models.CharField(max_length=25)
    Cast = models.CharField(max_length=25)
    # Education and occupation
    About = models.TextField()
    Education = models.CharField(max_length=50, null=True)
    Occupation = models.CharField(max_length=50, null=True)
    Side_Income = models.CharField(max_length=25)
    Annual_Income = models.CharField(max_length=25)
    # Family Details
    Father_Name = models.CharField(max_length=25)
    Father_Occupation = models.CharField(max_length=25)
    Mother_Name = models.CharField(max_length=25)
    Mother_Occupation = models.CharField(max_length=25)
    No_of_Brothers = models.CharField(max_length=25)
    No_of_Sisters = models.CharField(max_length=25)
    # Partner Preference
    Complexion=models.CharField(max_length=25)
    Partner_Height=models.CharField(max_length=25)
    Partner_Educationt=models.CharField(max_length=25)
    Partner_Religion=models.CharField(max_length=25)
    Partner_Preference=models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image=models.ImageField(default="profile_pics/default.png", upload_to="media")
    follow=models.ManyToManyField("self",
                                    related_name="interested_by",
                                    symmetrical=False,
                                    blank=True)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    interested = models.IntegerField(default=0)
    
    def __str__(self):
        return f'"{self.user.username}" sent interest to "{self.user_profile}"'
