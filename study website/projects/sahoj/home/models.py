from django.db import models


# Create your models here.

class Quiz(models.Model):
    Questions=models.ImageField(upload_to="home/images1", default="")
    option1=models.CharField(max_length=100, default="")
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correctAns=models.CharField(max_length=100)
    questionNO=models.CharField(max_length=100, default="")
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Exam_hs(models.Model):
    Questions=models.ImageField(upload_to="home/images2", default="")
    option1=models.CharField(max_length=100, default="")
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correctAns=models.CharField(max_length=100)
    questionNO=models.CharField(max_length=100, default="")

    def __str__(self):
        return self.questionNO

class Item(models.Model):
    contentvedio=models.FileField(upload_to="home/videos1", default="")
    heading=models.CharField(max_length=100, default="")
    supportimages=models.ImageField(upload_to="home/images3", default="")
    contentNO=models.CharField(max_length=100, default="")

    def __str__(self):
        return self.contentNO
