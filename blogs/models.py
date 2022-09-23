from django.db import models
from .config import *

# Create your models here.
class Course(models.Model):
    course = models.CharField(max_length=50)
    course_fee_01 = models.CharField(max_length=10)
    course_fee_03 = models.CharField(max_length=10)
    course_fee_06 = models.CharField(max_length=10)
    course_desc = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        val = self.course
        return val
    
    def save(self, *args, **kwargs):
        val = self.course
        self.slug = generate_slug(val)
        super(Course, self).save(*args, **kwargs)
