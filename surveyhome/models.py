from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import uuid
from django.conf import settings

# Create your models here.

class SurveyType(models.Model):
    """docstring for SurveyType."""
    name = models.CharField(max_length=200, help_text='Enter the survey Type')

    def __str__(self):
        return self.name

class Logo(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the logo name")
    logo_image = models.ImageField(upload_to='logo_images', blank=True)

    def get_absolute_url(self):
        return reverse('dashboard', args=[str(self.id)])

class QuestionType(models.Model):
    displayname = models.CharField(max_length=200, help_text="Enter the type of question")

    def __str__(self):
        return self.displayname

class Questionarie(models.Model):
    surveyid = models.ForeignKey('SurveyTitle', on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=200, help_text="Enter the Survey question")
    questiontype = models.ForeignKey('QuestionType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.surveyid.title} ({self.question} {self.questiontype.displayname})'


class SurveyTitle(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the survey")
    surveytype = models.ForeignKey('SurveyType', on_delete=models.SET_NULL, null=True)
    logo = models.ForeignKey('Logo', on_delete=models.SET_NULL, null=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} ({self.surveytype.name})'


class ResponseCollector(models.Model):
    responseid = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Response ID')
    response = models.CharField(max_length=500)
    questionarieid = models.ForeignKey('Questionarie', on_delete=models.SET_NULL, null=True)
    surveyid = models.ForeignKey('SurveyTitle', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['surveyid']
    def __str__(self):
        return self.responseid



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profilepic = models.ImageField(upload_to='userprofile', blank=True)
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('profile', args=[str(self.id)])

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profilepic']
