from django.urls import path, include

urlpatterns = [
    path('', include('logreg_app.urls')),
]
