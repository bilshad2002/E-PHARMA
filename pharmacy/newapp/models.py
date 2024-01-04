from django.db import models


class user(models.Model):
    UserName = models.CharField(max_length=50)
    Email = models.EmailField()
    Address = models.CharField(max_length=40)
    PhoneNo = models.IntegerField()
    Password = models.CharField(max_length=20)
    type = models.IntegerField()
    status =(('APPROVED','APPROVED'),
             ('PENDING','PENDING'),
             ('REJECT','REJECT'))
    entry = models.CharField(choices=status,max_length=20,default='PENDING')

    def __str__(self):
        return self.UserName

class Product(models.Model):
    Image = models.FileField()
    MedicineName = models.CharField(max_length=50)
    Price = models.IntegerField()

    def __str__(self):
        return self.MedicineName

class cart(models.Model):
    Medicineid = models.ForeignKey(Product,on_delete=models.CASCADE)
    Userid = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.Medicineid.MedicineName

class booking(models.Model):
    userid = models.ForeignKey(user,on_delete=models.CASCADE)
    medicineid = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True,blank=True)

    def __str__(self):
        return self.medicineid.MedicineName


