# from django.db import models
# from django.contrib.auth.models import User
# from enum import Enum

# class RoleMaster(models.Model):

#     role_id = models.AutoField(primary_key=True)
#     role_name = models.CharField(blank=False,null=False,max_length=50)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at =  models.DateTimeField(auto_now=True)
    
#     class Meta:
#         db_table = 'role_master'


# class OrgMaster(models.Model):
#     org_id = models.AutoField(primary_key=True)
#     org_name = models.CharField(blank=False, null=False, max_length=50)
#     org_abbr = models.CharField(blank=True, null=True, max_length=25)
#     org_long_name = models.CharField(blank=True, null=True, max_length=100)
#     parent_org = models.ForeignKey('self', on_delete=models.RESTRICT, db_column='fk_parent_org', null=True, blank=True)
#     org_location = models.CharField(blank=False, null=False, max_length=50)
#     org_graph = models.CharField(blank=False, null=False, max_length=50,default="")

#     class Meta:
#         db_table = 'org_master'

# class QualificationChoice(Enum):
#     BD = "Bachelor's degree"
#     MD = "Master's degree"
#     PHD = "Doctorate or higher"

# class OrgRoleChoice(Enum):
#     ADMIN = "Admin"
#     GENETICIST = "Geneticist"
#     SCIENTIST = "Scientist"

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.RESTRICT,db_column='fk_profile_user')
#     title = models.CharField(blank=True,null=True,max_length=10)
#     role_id = models.ForeignKey(RoleMaster,on_delete=models.RESTRICT,db_column='fk_profile_role',null=True)
#     org_role = models.CharField(blank=False,null=False,max_length=20,choices=[(role, role.value) for role in OrgRoleChoice])
#     qualification = models.CharField(blank=False,null=False,max_length=20,choices=[(role, role.value) for role in QualificationChoice])
#     org_id = models.ForeignKey(OrgMaster, on_delete=models.RESTRICT, db_column='fk_org_id', null=True, blank=True)
#     country = models.CharField(blank=False,null=False,max_length=20)
#     mobile_number = models.CharField(max_length=100, blank=True)
#     gender = models.CharField(max_length=10, blank=True)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     ins_upd_user = models.ForeignKey(User,on_delete=models.RESTRICT,db_column='fk_profile_ins_upd_user',null=True,related_name='profile_update_user')
#     short_name = models.CharField(max_length=20, blank=True)
#     access_type = models.BooleanField(null=True)
    

#     class Meta:
#         db_table = 'users_profile'