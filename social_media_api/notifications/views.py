from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Notification

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    """Fetch notifications for the current user"""
    notifications = Notification.objects.filter(recipient=request.user, is_read=False)
    data = [{"message": f"{n.actor} {n.verb}", "time": n.created_at} for n in notifications]
    
    return Response(data, status=200)