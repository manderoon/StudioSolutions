from django.db import models

"""
Models with no foreign keys
"""
class IlcActivity(models.Model):

    activity_id = models.IntegerField(db_column='Activity_ID', primary_key=True)  # Field name made lowercase.
    activity_name = models.CharField(db_column='Activity_Name', max_length=50, blank=True, null=True)  # Field name made lowercase. 
    resource_type = models.CharField(db_column='Resource_Type', max_length=50, blank=True, null=True)  # Field name made lowercase. 
    link = models.CharField(db_column='Link', max_length=50, blank=True, null=True)  # Field name made lowercase.
    completion_time = models.DateTimeField(db_column='Completion_Time', blank=True, null=True)  # Field name made lowercase.        

    def __str__(self):
        return self.activity_name
    class Meta:
        db_table = 'ILC_Activity'


class ProductOwner(models.Model):
    product_owner_id = models.IntegerField(db_column='Product_Owner_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Product_Owner'


class Skill(models.Model):
    skill_id = models.IntegerField(db_column='Skill_ID', primary_key=True)  # Field name made lowercase.
    skill_name = models.CharField(db_column='Skill_Name', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'Skill'


class Staff(models.Model):
    staff_id = models.IntegerField(db_column='Staff_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.       
    last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expertise = models.CharField(db_column='Expertise', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Staff'


"""
Foreign keys: skill, product owner, product, team registration
"""

class Product(models.Model):
    product_id = models.IntegerField(db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    product_owner = models.ForeignKey(ProductOwner, models.DO_NOTHING, db_column='Product_Owner_ID', blank=True, null=True)  # Field name made lowercase.
    skill = models.ForeignKey(Skill, models.DO_NOTHING, db_column='Skill_ID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    min_skill_required = models.CharField(db_column='Min_Skill_Required', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'Product'


class TeamRegistration(models.Model):
    team_id = models.IntegerField(db_column='Team_ID', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID', blank=True, null=True)  # Field name made lowercase.
    registration_date = models.DateField(db_column='Registration_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Team_Registration'

class Student(models.Model):
    student_id = models.IntegerField(db_column='Student_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studio_level = models.CharField(db_column='Studio_Level', max_length=50, blank=True, null=True)  # Field name made lowercase.
    on_campus = models.SmallIntegerField(db_column='On_Campus', blank=True, null=True)  # Field name made lowercase.
    engineering_discipline = models.CharField(db_column='Engineering_Discipline', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    desired_grade = models.CharField(db_column='Desired_Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    team = models.ForeignKey('TeamRegistration', models.DO_NOTHING, db_column='Team_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Student'

"""
Many foreign keys 
"""

class StudentSkill(models.Model):
    skill = models.OneToOneField('Skill', models.DO_NOTHING, db_column='Skill_ID', primary_key=True)  # Field name made lowercase.  
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='Student_ID')  # Field name made lowercase.

    class Meta:
        db_table = 'Student_Skill'
        unique_together = (('skill', 'student'),) 
        

class StudentPreference(models.Model):
    student = models.OneToOneField('Student', models.DO_NOTHING, db_column='Student_ID', primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID')  # Field name made lowercase.
    preference = models.IntegerField(db_column='Preference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Student_Preference'
        unique_together = (('student', 'product'),) 


class StudentIlcActivity(models.Model):
    student = models.OneToOneField('Student', models.DO_NOTHING, db_column='Student_ID', primary_key=True)  # Field name made lowercase.
    activity = models.ForeignKey('IlcActivity', models.DO_NOTHING, db_column='Activity_ID')  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID')  # Field name made lowercase.
    engagement_ranking = models.IntegerField(db_column='Engagement_Ranking', blank=True, null=True)  # Field name made lowercase.   
    relevancy_ranking = models.IntegerField(db_column='Relevancy_Ranking', blank=True, null=True)  # Field name made lowercase.     
    year_completed = models.CharField(db_column='Year_Completed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    studio_level = models.CharField(db_column='Studio_Level', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    completion_time = models.DateTimeField(db_column='Completion_Time', blank=True, null=True)  # Field name made lowercase.        

    class Meta:
        db_table = 'Student_ILC_Activity'
        unique_together = (('student', 'activity', 'product'),)


class StaffProduct(models.Model):
    staff = models.OneToOneField('Staff', models.DO_NOTHING, db_column='Staff_ID', primary_key=True)  # Field name made lowercase.    
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='Product_ID')  # Field name made lowercase.

    class Meta:
        db_table = 'Staff_Product'
        unique_together = (('staff', 'product'),)


