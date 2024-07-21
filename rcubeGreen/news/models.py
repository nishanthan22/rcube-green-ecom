from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=500)
    urlToImage = models.URLField(max_length=500, null=True, blank=True)
    publishedAt = models.DateTimeField()
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
