from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import base64




class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    amount = models.PositiveIntegerField(default=0)
    status = models.BooleanField()
    image = models.ImageField(upload_to="image/")
    base_64 = models.CharField(max_length=5000000, blank=True)
    def save(
         self, force_insert=False, force_update=False, using=None, update_fields=None
                ):
                    self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')
                    super(Product,self).save()
    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    comment = models.TextField(max_length=1000)


class RegistrationMod(models.Model):
    login = models.CharField(max_length=30)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=30)

    # Додайте інші поля, які вам потрібні для реєстрації

    def __str__(self):
        return self.login


    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)