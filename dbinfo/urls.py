from django.urls import path

from . import views

urlpatterns = [
    # app and any parameters pass in, the function name in views 
    path('products', views.ProductListView.as_view(), name="products.list"),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name="products.detail"),
    path('productsowners', views.ProductOwnerListView.as_view(), name="productsowners.list"),
    path('productsowners/<int:pk>', views.ProductOwnerDetailView.as_view(), name="productsowners.detail"),
    path('skills', views.SkillListView.as_view(), name="skills.list"),
    path('addskill', views.addSkill, name="addskill"),
    path('ilcactivities', views.ActivitiesList.as_view(), name="activities.list"),
    path('addactivity', views.addActivity, name="addactivity"),
    path('studentactivities', views.StudentActivitiesList.as_view(), name="studentactivities.list"),
    path('addstudentactivity', views.addStudentActivity, name="addstudentactivity"),
]