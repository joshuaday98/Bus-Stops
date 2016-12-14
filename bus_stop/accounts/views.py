from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'GET':
        user_form = UserCreationForm()
        reg_form = MemberRegistrationForm()

    elif request.method == 'POST':
        querydict = request.POST
        reg_form = UserCreationForm(data=querydict)
        user_form = MemberRegistrationForm(data=querydict)

        if user_form.is_valid() and reg_form.is_valid():
            reg = reg_form.save(commit=False)
            user = user_form.save(commit=False)

            reg.save()
            user.user = user
            user.save()

            return redirect('/')

    context = {'reg_form': reg_form,
               'user_form': user_form}
    return render(request, 'acct/acct_create.html', context)
