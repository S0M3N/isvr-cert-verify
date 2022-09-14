from django.template.defaultfilters import slugify
import string
import random




def generate_slug(text):
    new_slug = slugify(text)
    return new_slug
