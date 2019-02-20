from django.db import models


class Ni(models.Model):
    text = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        unique_together = (
            ('text', 'user_id', 'chat_id'),
        )

    def __str__(self):
        return self.text


class Job(models.Model):
    ADD = 'AD'
    EDIT = 'ED'
    DELETE = 'DE'

    STATUS_CHOICES = (
        (ADD, 'Add'),
        (EDIT, 'Edit'),
        (DELETE, 'Delete'),
    )

    user_id = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    target = models.ForeignKey(Ni, models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        unique_together = (
            ('user_id', 'chat_id'),
        )

    def __str__(self):
        return self.user_id
