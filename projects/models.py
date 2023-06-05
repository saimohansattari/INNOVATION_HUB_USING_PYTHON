from asyncio import streams
from operator import mod
from pyexpat import model
from sre_constants import BRANCH, CATEGORY
from statistics import mode
from django.db import models

import projects

# Create your models here.
BRANCHES = (
    ('Civil', 'Civil'),
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE', 'EEE'),
    ('Mech', 'Mech'),
)
BATCHES = (
    ('2017-2021', '2017-2021'),
    ('2018-2022', '2018-2022'),
    ('2019-2023', '2019-2023'),
    ('2020-2024', '2020-2024'),
    ('2021-2025', '2021-2025'),
    )
CATEGORY = (
    ('MINI_PROJECT', 'MINI_PROJECT'),
    ('FINAL_PROJECT', 'FINAL_PROJECT'),
    ('HACKAHTON_PROJECT', 'HACKAHTON_PROJECT'),
)


class Project(models.Model):
    
    roll_no = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    branch = models.CharField(choices=BRANCHES, max_length=20)
    batch = models.CharField(choices=BATCHES, max_length=20, null=True, blank=True)
    category = models.CharField(choices=CATEGORY, max_length=20)
    year = models.CharField(max_length=10)
    project_title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    document = models.CharField(max_length=100)
    video = models.CharField(max_length=200,null=True)


    date_created = models.DateField(auto_now_add=True, null=True)