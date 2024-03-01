from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Log(models.Model):
    title = models.CharField(blank=False, max_length=500)
    content = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, null=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(
        upload_to='images', blank=True)

    def save(self, *args, **kwargs):
        super().save()
        self.slug = self.slug or slugify(self.title + '-' + str(self.id))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Log")
        verbose_name_plural = ("Logs")

    def __str__(self):
        return f"{self.title}"


    def get_absolute_url(self):
        return reverse("log-detail", kwargs={"question": self.slug})
    

class Solutions(models.Model):
    log = models.ForeignKey(
        Log, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    solution = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, null=False, blank=True)
    image = models.ImageField(
        upload_to='images', blank=True)

    def save(self, *args, **kwargs):
        super().save()
        self.slug = self.slug or slugify(self.solution + '-' + str(self.id))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Solution")
        verbose_name_plural = ("Solutions")

    def __str__(self):
        return f"  {self.solution} "

    def get_absolute_url(self):
        return reverse("log-solution", kwargs={"solution": self.slug})


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"like by {self.user.username} for {self.log.title}"


class Comments(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    log = models.ForeignKey(
        Solutions, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = ("Comment")

        verbose_name_plural = ("Comments")

    def __str__(self):
        return f"{self.comment}"


class Notification(models.Model):
    notification_for = models.CharField(null=True, blank=True,max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title = models.ForeignKey(Log, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return str(f"{self.user} {self.notification_for}")
    