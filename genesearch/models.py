# from django.db import models



# class Exceldata(models.Model):
#     variant_id = models.IntegerField(null=True, blank=True)
#     disease = models.TextField()
#     genes = models.TextField()
#     genes_id = models.TextField()
#     variant = models.TextField()
#     clinvar_id = models.IntegerField(null=True, blank=True)
#     chr = models.TextField()
#     position = models.IntegerField(null=True, blank=True)
#     ref_allle = models.TextField()
#     alt_allel = models.TextField()
#     af = models.TextField()
#     clinical_significance = models.TextField()

    

#     def __str__(self):
#         return str(self.variant_id)



from django.db import models



class Exceldata(models.Model):
    variant_id = models.IntegerField(null=True, blank=True,db_index=True)
    disease = models.CharField(max_length=255, db_index=True)
    genes = models.CharField(max_length=255, db_index=True)
    genes_id = models.CharField(max_length=255, db_index=True)
    variant = models.CharField(max_length=255, db_index=True)
    clinvar_id = models.IntegerField(null=True, blank=True, db_index=True)
    chr = models.CharField(max_length=255, db_index=True)
    position = models.CharField(max_length=255, db_index=True)
    ref_allle = models.TextField()
    alt_allel = models.TextField()
    af = models.TextField()
    clinical_significance = models.CharField(max_length=255, db_index=True)

    

    def __str__(self):
        return str(self.variant_id)



from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# password_reset_app/models.py
from django.db import models
from django.contrib.auth.models import User

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
