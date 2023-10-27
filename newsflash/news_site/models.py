from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Tag(models.Model):
    tag = models.CharField(_("Tag"), max_length=25)
    slug = models.SlugField(_("Slug"), unique=True, max_length=100, default="")

    def __str__(self):
        return self.tag

class Author(models.Model):
    first_name = models.CharField(_("First_Name"), max_length=50)
    last_name = models.CharField(_("Last_Name"), max_length=50)
    author_desc = models.CharField(_("Author_Decription"), max_length=500, default="")
    slug = models.SlugField(_("Slug"), unique=True, max_length=100, default="")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name())
        super().save(*args, **kwargs)

class Site(models.Model):
    site_origin = models.CharField(_("Site_Country"), max_length=100)

    def __str__(self):
        return self.site_origin

class Post(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    post_field = RichTextField(_("Post_Field"))
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True)
    site_origin = models.ForeignKey(Site, verbose_name=_("Site_Origin"), on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post/', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail-page', kwargs={'slug': self.slug})
    





