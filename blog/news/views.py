from django.shortcuts import render
from .models import News, Restaurants, Article, Video
from django.views.generic import DetailView
from django.core.mail import send_mail


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news})


def recommended(request):
    rest = Restaurants.objects.all()
    article = Article.objects.all()
    video = Video.objects.all()
    return render(request, 'news/recommended.html', {'rest': rest, 'article': article, 'video': video})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article.html'
    context_object_name = 'article'


def about_us(request):
    if request.method == 'POST':
        name_input = request.POST['name-input']
        email_input = request.POST['email-input']
        topic_input = request.POST['topic-input']
        info = request.POST['info']

        send_mail(
            name_input + ', ' + topic_input,
            info,
            email_input,
            ['andrii.zinko.knm.2020@lpnu.ua']
        )

    return render(request, 'news/about-us.html')


def about_me(request):
    return render(request, 'news/about-me.html')
