from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField("Title",max_length=100)
    info = models.CharField("Info",max_length=500)
    cover = models.ImageField("Cover",upload_to = "cover")
    book_pdf = models.FileField("Book_PDF",upload_to="book_pdf")
    datetime = models.DateTimeField("DateTime",auto_now_add=True)


















