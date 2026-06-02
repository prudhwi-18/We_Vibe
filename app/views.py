from django.shortcuts import render
from .models import Song, PlaylistItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

@csrf_exempt
@login_required
def add_to_playlist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        PlaylistItem.objects.get_or_create(
            user=request.user,
            title=data['title'],
            audio=data['audio'],
            cover=data.get('cover', '')
        )
        return JsonResponse({'status': 'added'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def get_playlist(request):
    items = PlaylistItem.objects.filter(user=request.user)
    result = [
        {'title': i.title, 'audio': i.audio, 'cover': i.cover}
        for i in items
    ]
    return JsonResponse(result, safe=False)

def edit_profile(request):
    if request.method == 'POST':
        # Handle profile editing logic here
        pass
    return render(request, 'edit_profile.html')

def playlist_view(request):
    return render(request, 'playlist.html')