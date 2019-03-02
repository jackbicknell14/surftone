from django.urls import path
from . import views
from users import views as users

urlpatterns = [
    path('', views.home, name="surftone-home"),
    path('blog/', views.blog, name="surftone-blog"),
    path('about/', views.about, name="surftone-about"),
    path('profile/', users.profile, name="surftone-profile"),
    path('upload/', views.model_form_upload, name="surftone-upload"),
    path('play', views.SongListView.as_view(), name="surftone-play"),
    path('dashboard/', views.dashboard, name="surftone-dashboard")

]
