from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import User
User.__str__ = lambda user_instance: user_instance.first_name + ' ' + user_instance.last_name + ' ' +  user_instance.username

# Create your models here.


class AccessLevel(models.Model):
    id = models.IntegerField(primary_key=True,unique=True,verbose_name='id')
    title = models.CharField(max_length=100, blank=True,null=True,verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    
    class Meta:
        verbose_name_plural = "سطح های دسترسی"
        verbose_name = 'سطح دسترسی'
        
    def __str__(self):
        return self.title
     
    

class Role(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True,)
    description = models.TextField(verbose_name='توضیحات')
    
    class Meta:
        verbose_name_plural = "نقش ها"
        verbose_name = 'نقش'
        
    def __str__(self):
        return self.title
    

class UserAccessLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_level = models.ForeignKey(AccessLevel, on_delete=models.SET_NULL,null=True, verbose_name="سطح دسترسی")
    class Meta:
        verbose_name_plural = "سطح دسترسی کاربرها"
        verbose_name = 'سطح دسترسی کاربر'
        
    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)
    
    
class Profile(models.Model):
    Jensiat_CHOICES = (
    ("مرد", "مرد"),
    ("زن", "زن"),)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,null=True, verbose_name="نقش")
    # bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=30, blank=True,null=True,)
    birth_date = models.CharField(max_length=30,null=True, blank=True)
    jensiat = models.CharField(max_length=15,
                    choices=Jensiat_CHOICES,
                    null=True,
                    blank=True,
                    default="مرد")
    
    class Meta:
        verbose_name_plural = "پروفایل ها"
        verbose_name = 'پروفایل'
        
    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("******** profile created ********")
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print("******** instance saved ********")
    instance.profile.save()






