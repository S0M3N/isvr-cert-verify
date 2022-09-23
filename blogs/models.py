from django.db import models
from .config import *

# Create your models here.
class Course(models.Model):
    course = models.CharField(max_length=50)
    fee_1_not = models.CharField(max_length=10, default='14999/-')
    course_fee_01 = models.CharField(max_length=10)
    fee_3_not = models.CharField(max_length=10, default='24999/-')
    course_fee_03 = models.CharField(max_length=10)
    fee_6_not = models.CharField(max_length=10, default='34999/-')
    course_fee_06 = models.CharField(max_length=10)
    course_cont = models.TextField(null=True, blank=True)
    course_heading_01 = models.CharField(max_length=100, null=True, blank=True)
    course_desc_01 = models.TextField()
    course_heading_02 = models.CharField(max_length=100, null=True, blank=True)
    course_desc_02 = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    git_img = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        val = self.course
        return val
    
    def save(self, *args, **kwargs):
        val = self.course
        self.slug = generate_slug(val)
        super(Course, self).save(*args, **kwargs)


class Application(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    course = models.CharField(max_length=50)
    month = models.CharField(max_length=10)

    def __str__(self):
        val = self.first_name+" "+self.course+" "+self.month
        return val