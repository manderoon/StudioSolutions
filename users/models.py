from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    ENGINEERING_CHOICES = (
        ('data', 'Data'),
        ('electronics', 'Electronics'),
        ('electrical', 'Electrical'),
    )

    STUDIO_LEVEL_CHOICES = (
        ('fundamentals a', 'Fundamentals A'),
        ('fundamentals b', 'Fundamentals B'),
        ('applications a', 'Applications A'),
        ('applications b', 'Applications B'),
        ('professionals a', 'Professionals A'),
        ('professionals b', 'Professionals B'),
    )
    GRADE_CHOICES = (
        ('p', 'P'),
        ('c', 'C'),
        ('d', 'D'),
        ('hd', 'HD'),
    )
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    engineering_discipline = models.CharField(
        max_length=12,
        choices=ENGINEERING_CHOICES,
        blank=True
    )
    student_id_number = models.IntegerField(default=0)
    student_first_name = models.CharField(max_length=255, default='Stu')
    student_last_name = models.CharField(max_length=255, default='Dent')
    studio_level = models.CharField(
        max_length=20,
        choices=STUDIO_LEVEL_CHOICES,
        blank=True
    )
    student_year = models.IntegerField(default=1)
    on_campus = models.BooleanField(default=True)
    desired_grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        default='P'
    )


    def __str__(self):
        return f'{self.user.username} Profile'
    
    # Override the save method of the model
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
