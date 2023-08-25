# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db import models
# from main.models import Type, Company
# from account.models import Account
#
#
# class CategoryJobs(models.Model):
#     title = models.CharField(max_length=221)
#
#     def __str__(self):
#         return self.title
#
#
# class TagJobs(models.Model):
#     title = models.CharField(max_length=221)
#
#     def __str__(self):
#         return self.title
#
#
# class Jobs(models.Model):
#     author = models.ForeignKey(Account, on_delete=models.CASCADE)
#     title = models.CharField(max_length=221)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     category = models.ForeignKey(CategoryJobs, on_delete=models.CASCADE)
#     type = models.ManyToManyField(Type)
#     price = models.DecimalField(decimal_places=4, max_digits=100, null=True, blank=True)
#     working_day = models.IntegerField(default=15, validators=[MaxValueValidator(30), MinValueValidator(15)])
#     tags = models.ManyToManyField(TagJobs)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
#
# class SelectionList(models.Model):
#     author = models.ForeignKey(Account, on_delete=models.CASCADE)
#     jobs = models.OneToOneField(Jobs, on_delete=models.CASCADE, unique=True)
#
