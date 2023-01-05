from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    text = "Это главная страница проекта Yatube"
    context = {'title' : text}
    return render(request, template, context)

def group_posts(request):
    text = "Здесь будет информация о группах проекта Yatube"
    context = {'title' : text}
    template = 'posts/group_list.html'
    return render(request, template, context)


# def group_posts(request, slug):
#     return HttpResponse(f'Страница сообщества {slug}')