from django.db import models

# Create your models here.


class Books(models.Model):

    def __str__(self):
        return self.book_name

    category_CHOICE = (
        (u'1', u'法律'),
        (u'2', u'人文'),
        (u'3', u'综合'),
        (u'4', u'理工'),
        (u'5', u'机械'),
        (u'6', u'财经'),
        (u'7', u'经济'),
        (u'8', u'政治'),
        (u'9', u'生物'),
        (u'10', u'商业'),
        (u'11', u'科学'))
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100, name="book_name", verbose_name="test")
    book_press = models.CharField(max_length=100, name="book_press")
    book_category = models.CharField(max_length=4, choices=category_CHOICE, name="book_category")
    book_year = models.CharField(max_length=10, name="book_year")
    book_price = models.DecimalField(max_digits=8, decimal_places=2, name="book_price")
    book_stock_nums = models.IntegerField(max_length=3, name="book_stock_nums")
    book_borrow_nums = models.IntegerField(max_length=3, name="book_borrow_nums")
    book_create_data = models.DateTimeField("create_date")


class Users(models.Model):

    def __str__(self):
        return self.user_name

    GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, name="user_name", unique=True)
    user_email = models.EmailField(max_length=100, name="user_email", unique=True)
    user_phone = models.CharField(max_length=11, name="user_phone")
    user_number = models.CharField(max_length=20, name="user_number", unique=True)
    user_class = models.CharField(max_length=20, name="user_class")
    user_major = models.CharField(max_length=20, name="user_major")
    user_gender = models.CharField(max_length=2, choices=GENDER_CHOICE)
    user_password = models.CharField(max_length=20, name="user_password")


class BookUser(models.Model):
    user_id = models.IntegerField(max_length=11)
    book_id = models.IntegerField(max_length=11)
