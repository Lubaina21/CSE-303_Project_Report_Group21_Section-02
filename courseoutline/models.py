from django.db import models


# Create your models here.

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver

def upload_location(instance,filename,**kwargs):
    file_path = 'courseoutline/{author_id}/{title}-{filename}'.format(
         author_id = str(instance.author.id),title=str(instance.title),filename = filename
      )
    return file_path
class CourseOutline(models.Model):
    course_code                        =models.CharField(max_length=50,null=False,blank =False)
    course_type            =models.TextField(max_length=5000,null=False,blank= False)
    course_title              =models.TextField(max_length=5000,null=False,blank= False)
    credit_value                 =models.TextField(max_length=5000,null=False,blank= False)
    course_description           =models.TextField(max_length=5000,null=False,blank= False)
    course_objective     =models.TextField(max_length=5000,null=False,blank= False)
    course_policy      =models.TextField(max_length=5000,null=False,blank= False)
    academic_dishonesty                 =models.TextField(max_length=5000,null=False,blank= False)
    non_discreminatory_policy       =models.TextField(max_length=5000,null=False,blank= False)
   
    def __str__(self):
        return self.title 
@receiver(post_delete,sender=CourseOutline)
def submission_delete(sender,instance,**kwargs):
    instance.image.delete(False)
def pre_save_course_outline_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username +"_"+ instance.title)
pre_save.connect(pre_save_course_outline_receiver,sender=CourseOutline)