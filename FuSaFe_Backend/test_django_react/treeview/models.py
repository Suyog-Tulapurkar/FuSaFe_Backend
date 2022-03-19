from configparser import SectionProxy
from django.db import models

# Create your models here.

class Treeviewlist(models.Model):
    part_id = models.CharField(max_length=100)
    part_name = models.CharField(max_length=100)
    section_id = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)
    workproduct = models.CharField(max_length=100)
    wp_type = models.CharField(max_length=100)
    wp_category = models.CharField(max_length=100)
    wp_condition  =  models.CharField(max_length=100)

