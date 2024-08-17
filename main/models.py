from django.db import models
from django.core.validators import MaxValueValidator

from ckeditor.fields import RichTextField


class Vars(models.Model):
    aboutme = RichTextField()
    kherad = models.URLField(blank=True)
    name1 = models.CharField(max_length=255)
    number1 = models.PositiveIntegerField(default=0)
    name2 = models.CharField(max_length=255)
    number2 = models.PositiveIntegerField(default=0)
    name3 = models.CharField(max_length=255)
    number3 = models.PositiveIntegerField(default=0)

    what_can_i_do_title1 = models.CharField(max_length=355)
    wcid_des1 = RichTextField(blank=True)
    sub_des1 = RichTextField(blank=True)
    wcid_img1 = models.ImageField(upload_to="cover", blank=True)

    what_can_i_do_title2 = models.CharField(max_length=355)
    wcid_des2 = RichTextField(blank=True)
    sub_des2 = RichTextField(blank=True)
    wcid_img2 = models.ImageField(upload_to="cover", blank=True)

    what_can_i_do_title3 = models.CharField(max_length=355)
    wcid_des3 = RichTextField(blank=True)
    sub_des3 = RichTextField(blank=True)
    wcid_img3 = models.ImageField(upload_to="cover", blank=True)

    aboutme_title = models.CharField(max_length=355)
    aboutme_des = RichTextField(blank=True)
    aboutme_image = models.ImageField(upload_to="cover")
    file = models.FileField(upload_to='pdfs/', blank=True)

    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=555)
    phone = models.CharField(max_length=150)

    instagram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, editable=False)


class Skills(models.Model):
    vars = models.ForeignKey(Vars, on_delete=models.CASCADE, related_name="skill")
    Skill = models.CharField(max_length=100)
    percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.Skill


class Customer(models.Model):
    Customer = models.ForeignKey(Vars, on_delete=models.CASCADE, related_name='Customer')
    image = models.ImageField(upload_to="Customers")
    name = models.CharField(max_length=150)
    des = models.CharField(max_length=150)
    Customer_opinion = RichTextField(max_length=3000)

    def __str__(self):
        return self.name


class Blog(models.Model):
    Blog = models.ForeignKey(Vars, on_delete=models.CASCADE, related_name='blog')
    blog_img = models.ImageField(upload_to="cover")
    blog_title = models.CharField(max_length=455)
    des = models.TextField()
    sub_des = RichTextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, editable=False)


class ComImages(models.Model):
    Customer = models.ForeignKey(Vars, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to="company")
    url = models.URLField(blank=True)


class UserRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    text = models.TextField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    Job = models.ForeignKey(Vars, on_delete=models.CASCADE, related_name='Job')
    img1 = models.ImageField(upload_to="cover")
    title = models.CharField(max_length=400)
    des = RichTextField()

    def __str__(self):
        return self.title