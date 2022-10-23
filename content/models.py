from django.db import models

# Create your models here.



class Content(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    text = models.TextField(null=True,blank=True,verbose_name='متن')
    
    class Meta:
        verbose_name_plural = "مطالب"
        verbose_name = 'مطلب'
        
    def __str__(self):
        return self.title