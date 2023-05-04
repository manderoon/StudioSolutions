from django import forms
from .models import Skill, IlcActivity, StudentIlcActivity, Product, Student
from users.models import Profile

class AddSkillForm(forms.ModelForm):
    skill_id = forms.IntegerField(required=True, label='Skill ID (choose any unique number)')
    skill_name = forms.CharField(max_length=255, required=False, label='Skill Name')

    class Meta:
        model = Skill
        fields = ['skill_id', 'skill_name']

class AddActivityForm(forms.ModelForm):

    RESOURCE_CHOICES = (
        (' ', '-------'),
        ('YOUTUBE', 'YouTube'),
        ('LINKEDIN LEARNING', 'LinkedIn Learning'),
        ('DATACAMP', 'Datacamp'),
        ('UDEMY', 'Udemy'),
        ('COURSERA', 'Coursera'),
        ('CODECADEMY', 'Codecademy'),
        ('EDX', 'edX'),
        ('BOOK', 'Book'),
    )
    activity_id = forms.IntegerField(required=True, label='Activity ID (choose any unique number)')
    activity_name = forms.CharField(max_length=255, required=False, label='Activity Name')
    resource_type = forms.ChoiceField(choices=RESOURCE_CHOICES, required=False, label='Resource Type')
    link = forms.CharField(max_length=255, required=False, label='Link (if online course)')
    completion_time = forms.DateTimeField(required=False, label='Completion Time')


    class Meta:
        model = IlcActivity
        fields = ['activity_id', 'activity_name', 'resource_type', 'link', 'completion_time']

class AddStudentActivityForm(forms.ModelForm):

    STUDIO_CHOICES =  (
        (' ', '--------'),
        ('fundamentals a', 'Fundamentals A'),
        ('fundamentals b', 'Fundamentals B'),
        ('applications a', 'Applications A'),
        ('applications b', 'Applications B'),
        ('professionals a', 'Professionals A'),
        ('professionals b', 'Professionals B'),
    )

    student = forms.ModelChoiceField(queryset=Student.objects.all(), to_field_name='student_id', label='Student (Select yourself)')  # Field name made lowercase.
    activity = forms.ModelChoiceField(queryset=IlcActivity.objects.all(), to_field_name='activity_id', label='Activity (Refer to activities page if unsure)')  # Field name made lowercase.
    product = forms.ModelChoiceField(queryset=Product.objects.all(), to_field_name='product_name', label='Product')  # Field name made lowercase.
    engagement_ranking = forms.ChoiceField(choices=[(i, i) for i in range(0, 6)], required=False, label='Engagement Ranking (1 being low engagament) ')  # Field name made lowercase.   
    relevancy_ranking = forms.ChoiceField(choices=[(i, i) for i in range(0, 6)], required=False, label='Relevancy Ranking (1 being low ranking)')  # Field name made lowercase.     
    year_completed = forms.CharField(required=False, max_length=10, label='Year_Completed')  # Field name made lowercase.
    studio_level = forms.ChoiceField(choices=STUDIO_CHOICES, required=False, label='Studio_Level')  # Field name made lowercase.   
    completion_time = forms.DateTimeField(required=False, label='Completion Time')  # Field name made lowercase.        



    class Meta:
        model = StudentIlcActivity
        fields = ['student', 'activity', 'product', 'engagement_ranking', 'relevancy_ranking', 
                  'year_completed', 'studio_level', 'completion_time' ]
