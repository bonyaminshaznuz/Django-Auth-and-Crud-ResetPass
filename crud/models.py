from django.db import models  

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    Image=models.ImageField(upload_to="Media/Profile_pic",null=True)
    def __str__(self):
        return self.ename 

    class Meta:  
        db_table = "employee" 
        
        
    