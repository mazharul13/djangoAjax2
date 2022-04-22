from django.db import models


# Create your models here.

class Test1(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'test1'

class Contact(models.Model):
    eid = models.IntegerField(help_text='Enter your ID', verbose_name='Enter EID')
    ename = models.CharField(max_length=10, help_text='Enter Name:')
    eemail = models.EmailField(null=False)
    econtact = models.CharField(max_length=30)
    Add_field = models.IntegerField(default=-9, blank=True)
    list2 = Test1.objects.all()
    CHOICES = []
    print(list2)
    for i in list2:
        print(i.id)
        CHOICES[i.id] = i.name;

    CHOICES = [('1', 'First'), ('2', 'Second')]
    choice_field = models.CharField(max_length=1,  choices=CHOICES)

    # class Meta:
    #     db_table = "contact_info"
