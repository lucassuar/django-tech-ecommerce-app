from django.db import models

"""
Suggestion Model below
"""
    
class Suggestion(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title