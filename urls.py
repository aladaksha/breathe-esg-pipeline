from django.contrib import admin
from django.urls import path
from core.views import ActivityListView, AuditActionReviewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/activities/', ActivityListView.as_view()),
    path('api/activities/<int:pk>/review/', AuditActionReviewView.as_view()),
]
