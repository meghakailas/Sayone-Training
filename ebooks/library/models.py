from django.db import models



class Category(models.Model):
    cname = models.CharField(max_length=300)

    def __str__(self):
        return self.cname

class Book(models.Model):
    bname = models.CharField(max_length=300)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    price = models.PositiveIntegerField(help_text='in Rs',)
    image = models.ImageField(upload_to= 'bookimg',blank=True)
    download_link = models.URLField()

    def __str__(self):
        return self.bname




