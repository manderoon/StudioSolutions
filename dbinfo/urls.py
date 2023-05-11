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
    path('ilcactivities/<int:pk>', views.ActivitiesDetailView.as_view(), name="activities.detail"),
    path('addactivity', views.addActivity, name="addactivity"),
    path('studentactivities', views.StudentActivitiesList.as_view(), name="studentactivities.list"),
    path('studentactivities/<int:pk>', views.StudentActivitiesDetailView.as_view(), name="studentactivities.detail"),
    path('addstudentactivity', views.addStudentActivity, name="addstudentactivity"),
    path('addpreference', views.addPreference, name="addPreference"),
    path('testproducts', views.TestProductListView.as_view(), name="testproducts.list"),
]