from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.core.files.storage import FileSystemStorage
from .forms import SongForm
from .models import Song
from django.views.generic import ListView


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/dashboard.html', {'title': 'Welcome to Divyd!'})
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'home/home.html', {'form': form})


def about(request):
    return render(request, 'home/about.html', {'title': 'About'})


def blog(request):
    return render(request, 'home/blog.html', {'title': 'About'})


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home/upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('surftone-home')
    else:
        form = SongForm()
    return render(request, 'home/model_form_upload.html', {
        'form': form
    })


def play(request):
    data = Song.objects.last()
    print(data)
    return render(request, 'home/play.html', {'data': data})


class SongListView(ListView):
    model = Song
    template_name = 'home/play.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'songs'
    ordering = ['-uploaded_at']
    paginate_by = 5


def dashboard(request):
    return render(request, 'home/dashboard.html', {'title': 'About'})

