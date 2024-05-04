from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False,
                            verbose_name=_("name"))
    slug = models.SlugField(max_length=250, unique=True, null=False, blank=True,
                            verbose_name=_("slug"))#副标题
    
    description = models.TextField(null=False, blank=False,
                                   verbose_name=_("description"))
    
    created_date = models.DateTimeField(null=False, blank=False,
                                    verbose_name=_("created date"),
                                    default=timezone.now)
    
    modified_date = models.DateTimeField(null=False, blank=False,
                                         verbose_name=_("modified date"))
    
