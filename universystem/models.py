from django.db import models
from django.contrib.auth.models import User

class Roles(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.category
        
class Profile(models.Model):
    information = models.TextField(null=True ,blank=True)
    photo = models.ImageField(upload_to='images/profile', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True ,blank=True)
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True ,blank=True)
    adress = models.TextField()
    def __str__(self):
        return self.user.username

class Course(models.Model):#Курс
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Lesson(models.Model):#Урок
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200,null=True ,blank=True)
    price = models.IntegerField(null=True)
    information = models.TextField()
    image = models.ImageField(upload_to='images/lesson', null=True)
    document = models.FileField(upload_to='pdf/document', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    youtube = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class SRP(models.Model):#Урок
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    information = models.TextField()
    document = models.FileField(upload_to='pdf/document', null=True)
    def __str__(self):
        return self.title

class laboratorywork(models.Model):#Урок
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    information = models.TextField()
    document = models.FileField(upload_to='pdf/document', null=True)
    def __str__(self):
        return self.title


class EnrollCource(models.Model):#Зарегистрироваться Курс
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.username

class Message(models.Model):
    recipient = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'recipient')
    sender = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'sender')
    message = models.TextField()
    sent = models.DateTimeField(auto_now = True)

    def __str__(self):
        return 'Message from ' + str(self.sender)

class Comment(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name

class News(models.Model):#Урок
    title = models.CharField(max_length=200)
    information = models.TextField()
    image = models.ImageField(upload_to='images/lesson', null=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title