from django.db import models

class Draw(models.Model):
    draw_title = models.CharField(max_length=200)
    draw_payload = models.TextField()

    def __str__(self):
        return self.draw_title

