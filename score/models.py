from email.policy import default
from django.db import models
from content.models import Content
from django.contrib.auth.models import User
# Create your models here.



class Score(models.Model):
    content = models.ForeignKey(Content,on_delete=models.SET_NULL,null=True, verbose_name='مطلب')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, verbose_name="کاربر")
    score = models.IntegerField(default=0, verbose_name='امتیاز')
    
    class Meta:
        verbose_name_plural = "امتیازات"
        verbose_name = 'امتیاز'
        
    def __str__(self):
        return self.content.title