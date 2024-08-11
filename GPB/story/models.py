from django.db import models

class UserStory(models.Model):
    personality_type = models.CharField(max_length=4)
    story = models.TextField()

    def __str__(self):
        return self.personality_type
