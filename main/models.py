# from django.db import models
#
#
# class Country(models.Model):
#     title = models.CharField(max_length=221)
#
#     def __str__(self):
#         return self.title
#
#
# class City(models.Model):
#     title = models.CharField(max_length=221)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#
# class Type(models.Model):
#     title = models.CharField(max_length=221)
#
#     def __str__(self):
#         return self.title
#
#
# class Contact(models.Model):
#     name = models.CharField(max_length=221)
#     email = models.EmailField(max_length=221, unique=True)
#     subject = models.CharField(max_length=221)
#     message = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Company(models.Model):
#     title = models.CharField(max_length=221)
#     location = models.ForeignKey(City, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#
# class Position(models.Model):
#     title = models.CharField(max_length=221)
#
#     def __str__(self):
#         return self.title
#
#
# class Subscribe(models.Model):
#     email = models.EmailField(unique=True)
#
#     def __str__(self):
#         return self.email
#
#
