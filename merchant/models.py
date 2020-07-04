from django.db import models
from django.conf import settings
from django.shortcuts import reverse
import django

CREDIT_CHOICES = (
    ('L', 'Low'),
    ('M', "Medium"),
    ('H', 'High')
)

class Company(models.Model):
    title = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    credit = models.CharField(max_length=1, choices=CREDIT_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField()
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    costumer_name = models.CharField(max_length=32)
    costumer_last_name = models.CharField(max_length=32)
    order = models.CharField(max_length=128)
    costumer_company = models.CharField(max_length=32)
    start_date = models.DateTimeField(default=django.utils.timezone.now())
    telephone_number = models.IntegerField()
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    slug = models.SlugField()
    image = models.ImageField()
    additional_info = models.TextField()

    def __str__(self):
        return f"{self.order} order by {self.costumer_name} {self.costumer_last_name}"

    def get_absolute_url(self):
        return reverse("merchant:order-detail", kwargs={
            'slug': self.slug
        })

    def get_confirm_order_url(self):
        return reverse("merchant:confirm-order", kwargs={
            'slug': self.slug
        })

    def get_remove_order_url(self):
        return reverse("merchant:remove-order", kwargs={
            'slug': self.slug
        })

class ActiveOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order} has been confirmed"

