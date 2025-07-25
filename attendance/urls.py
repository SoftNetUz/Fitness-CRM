from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import AttendanceViewSet, CheckInAPIView, TodayAttendanceListAPIView

router = DefaultRouter()
router.register('attendance', AttendanceViewSet, basename='attendance')

urlpatterns = router.urls + [
    path('check-in/', CheckInAPIView.as_view(), name='attendance-check-in'),
    path('today/', TodayAttendanceListAPIView.as_view(), name='attendance-today'),
]
