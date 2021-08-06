from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

DEFAULT_ID = 2

class Coworker(models.Model):
	name = models.CharField(max_length=400, blank=False, default="user")
	coworker_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_ID)
	phone_number = models.CharField(max_length=13, blank=False, default="XXX-XXXX-XXXX")
	email = models.CharField(max_length=100, blank=False, default="xxx@xxx.xxx")
	portfolio_url = models.URLField(default=" ")

	def __str__(self):
		return self.name

class Banner(models.Model):
	title = models.CharField(max_length=400, blank=False, default="제목")
	contents1 = models.TextField(blank = True)
	contents2 = models.TextField(blank = True)
	image = models.FileField(default = "image/fruit.jpg")

	def __str__(self):
		return self.title

class Introduce(models.Model):
	title_big = models.CharField(max_length=400, blank=False, default="제목")
	title_small1 = models.CharField(max_length=400, blank=False, default="test title1")
	contents1 = models.TextField(blank=True)
	image1 = models.FileField(default = "image/orange.svg")
	title_small2 = models.CharField(max_length=400, blank=False, default="test title2")
	contents2 = models.TextField(blank=True)
	image2 = models.FileField(default = "image/orange.svg")

	def __str__(self):
		return self.title_big

class Portfolio(models.Model):
	video_contents = models.FileField(default='video/test.mp4')
	descriptions = models.TextField(blank=True, null=True)
	submitted_time = models.DateTimeField(default=timezone.now)
	coworker_name = models.ForeignKey(Coworker, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return str(self.descriptions)

class Request(models.Model):
	#author = model.ForeignKey(settings.AUTH_USER_MODEL, on_delete=moels.CASCADE)
	video_contents = models.FileField(null=True, blank=True)
	title = models.CharField(max_length=400, blank=False, default="test title")
	contents = models.TextField(blank=False)
	submitted_time = models.DateTimeField(default=timezone.now)
	company = models.CharField(max_length=400, blank=False)
	coworker_name = models.ForeignKey(Coworker, on_delete=models.CASCADE, blank=True, null=True)
	phone_number = models.CharField(max_length=13, blank=False, default="XXX-XXXX-XXXX")
	email = models.CharField(max_length=100, blank=False, default="xxx@xxx.xxx")

	def __str__(self):
		return self.title