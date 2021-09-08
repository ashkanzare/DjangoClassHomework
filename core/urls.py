from django.urls import path, include



urlpatterns = [
    path('Education/', include('Education.api.urls')),
    path('library/', include('library.api.urls')),
]