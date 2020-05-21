from django.db import models

# Create your models here.
class vicer(models.Model):
    First_name = models.CharField(max_length=50,default='')
    Last_name = models.CharField(max_length=50,default='')
    Email = models.EmailField(max_length=100,unique=True,default='')
    departments = [
    ('FLER', 'FLER'),
    ('IT', 'IT'),
    ('HR', 'HR'),
    ('COMM', 'COMM'),
    ]
    Department = models.CharField(max_length=4,
    choices=departments,
    default='FLER')
    Year_joined_VIC = models.IntegerField(default=0)

    def __str__(self):
        return '{} {}, joined {} in {}\nEmail : {}'.format(self.First_name,self.Last_name,self.Department,self.Year_joined_VIC,self.Email)