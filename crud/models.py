from django.db import models

# Create your models here.

class Genders(models.Model):
    class Meta:
        db_table = 'tbl_genders'

    gender_id = models.BigAutoField(primary_key=True, blank=False) # gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False) # gender VARCCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

class Users(models.Model):
    class Meta:
        db_table = 'tbl_users'
        
    user_id = models.BigAutoField(primary_key=True, blank=False) # user_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    full_name = models.CharField(max_length=55, blank=False) # full_name VARCHAR(55) NOT NULL
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE) # gender_id BIGINT NOT NULL // FOREIGN KEY(gender_id) REFERENCES tbl_genders(gender_id) ON DELETE CASCADE
    birth_date = models.DateField(blank=False) # birth_date DATE NOT NULL
    address = models.TextField(max_length=255, blank=True) # address VARCHAR(255) DEFAULT NULL
    contact_number = models.CharField(max_length=55, blank=False) # contact_number VARCHAR(55) NOT NULL
    email = models.EmailField(max_length=55, blank=True) # email VARCHAR(55) DEFAULT NULL
    username = models.CharField(max_length=55, blank=False, unique=True) # username VARCHAR(55) NOT NULL UNIQUE
    password = models.CharField(max_length=255, blank=False) # password VARCHAR(255) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    