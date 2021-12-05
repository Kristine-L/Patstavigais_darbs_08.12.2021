from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
    UserForm,
    FilterUser,
    FileForm)
from .models import User

def add_user(request):
    form = UserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                e_mail=form.cleaned_data['e_mail'],
            )

            user.save()

        return render(
            request,
            template_name="show_user.html",
            context={"user": user}
        )

    return render(
        request,
        template_name="forms.html",
        context={"form": form}
    )


def get_all_users(request):

    users = User.objects.all()

    context = {"users": users,
               }

    return render(
        request,
        template_name='all_users.html',
        context=context,
    )

def get_user(request, user_id):

    user = User.objects.get(id=user_id)

    context = {
        "user": user,
    }

    return render(
        request,
        template_name="show_user.html",
        context=context,
    )

def filter_users(request):

    form = FilterUser(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = form.cleaned_data['user']
            users = User.objects.filter(username=user)

            context = {
                "users": users,
            }


        return render(
            request,
            template_name="all_users.html",
            context=context,
        )

    context = {
        "form": form,
    }

    return render(
        request,
        template_name="forms.html",
        context=context,
    )

def upload_csv(request):

    form = FileForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid():

            print(request.FILES["csv_file"])

            return HttpResponse("Ok")


    return render(
        request,
        template_name="forms.html",
        context={"form": form}
    )





