from django.db import models

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    blog_pic=models.ImageField(upload_to='blog_pic/')

    summary = models.CharField(max_length=3000)



    def __str__(self):
        return self.title

    def body(self):
        return self.summary[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
