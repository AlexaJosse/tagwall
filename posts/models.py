from django.db import models
from django.conf import settings


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    url = models.TextField(null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    publication_date = models.DateTimeField(editable=True, auto_now_add=True)
    votes_total = models.IntegerField(default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, )

    def __str__(self):
        return self.title

    def normal_date(self):
        return self.publication_date.strftime('%b %e %Y')

    def body_summary(self):
        if len(self.body) > 99:
            chain = self.body[:100] + "..."
        else:
            chain = self.body

        return chain


class Tag(models.Model):
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE, )
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + "/"+self.post.title[:15]+"/" + self.body[:15]
