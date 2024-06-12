from django.db import models

# Create your models here.

from django.db import models

import hashlib

class File(models.Model):
    filename = models.CharField(max_length=255)
    file_hash = models.CharField(max_length=64, unique=True)
    upload = models.FileField(upload_to='uploads/')

    def save(self, *args, **kwargs):
        if not self.file_hash:
            self.file_hash = hashlib.md5(self.upload.read()).hexdigest()
            self.upload.seek(0)
        super().save(*args, **kwargs)


class Conversation(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


#easy1234 - password
#bhargavi@2769 - postgree password
