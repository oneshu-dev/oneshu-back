from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.contrib.auth.models import Permission

from django.utils.translation import gettext_lazy as _ #国际化
# Create your models here.

class User(AbstractUser):
    #继承的abstractuser和permission足够
    #后续可考虑增加的内容:
    '''
    用户所在的项目数量
    
    '''
    nickname=models.CharField(max_length=250, null=False, blank=False,
                            verbose_name=_("昵称"))
    '''
    groups=None
    user_permissions=None #解决与初始默认表冲突
    permissions_ptr=None
    '''

    class Meta:
        verbose_name = "user"
        verbose_name_plural="users"
        ordering = ["username"]

    def __str__(self):
        return self.get_full_name()


    

