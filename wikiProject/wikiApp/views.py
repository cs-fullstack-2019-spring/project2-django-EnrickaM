from django.shortcuts import render,redirect, get_object_or_404
from .forms import newuserForm, relativeItemsForm,wikipostForm
from django.contrib.auth.models import User
from .models import newuserModel,relativeItemsModel,wikipostModel
from django.contrib.auth.decorators import login_required

# Create your views here.
# When. the user is logged in it will do the code below.

def index(request):
    # allpost will get all the stored information in my wikipost model
    allposts=wikipostModel.objects.all()
    context={
        'allposts': allposts
    }
    return render(request,'wikiApp/homepage.html',context)


# this code below is for a new user to be able to create a profile.
def create(request):
    form=newuserForm(request.POST or None)
#code above is just gettignt the post of the form.
    if form.is_valid():
        form.save()
        User.objects.create_user(request.POST["username"], "", request.POST["password"])
        return render(request,'wikiApp/homepage.html',{'name':request.user.username})
# code above says that if the form is valid then save it and save the user's user name and password.

    context={
        'form':form
    }

    return render(request,'wikiApp/newuser_form.html',context)
# code below just post all the infomation for the wikiposr model and put it on my all post page.
def allpost(request):
    allposts=wikipostModel.objects.all()
    context={
        'allposts':allposts
    }
    return render(request,'wikiApp/allpost.html',context)
@login_required
# the @login_required for the user to be logged in before the can try to enter a new entry.
def newentry(request):
    form=wikipostForm(request.POST or None)
    # code above just just post the form from my wikipost form
    context={
        'form':form
    }
    # code below just says that if the form is valid save it then redirect to the index page
    if form.is_valid():
        form.save()
        return redirect('index')
    # code below does whatever else if the form is not valid it will print out an error and render it back to the newentry form.
    else:
        print(form.errors)
        print(form)
    return render(request,'wikiApp/newentry.html',context)
@login_required
# the login_required is just there to make sure the user is logged in before they can update
def update(request,id):
    # the code below shows that i made a variable to get all the stored information in the wikipost moddel and priamy key to identy the object id
    editrelative=wikipostModel.objects.get(pk=id)
    update=wikipostForm(request.POST or None,instance=editrelative)
    context={
        'editrelative':editrelative
    }
    if update.is_valid():
        update.save()
        return redirect("allpost")
    return render(request,'wkikapp/update.html')


    return render(request,'wikiApp/newentry.html')
def delete(request,id):
    return render(request,'wikiApp/newentry.html')

def logout(request):
    return render(request,'registration/logout.html')

def newrelative(request):
    form=relativeItemsForm(request.POST or None)
    allrelative=relativeItemsModel.objects.all
    context={
        'form':form,
        'allrelative':allrelative
    }
    if form.is_valid():
        form.save()
        return redirect('detail')
    else:
        print(form.errors)
    return render(request,'wikiApp/relativeitems.html',context)


def details(request, wikiPostID):

    wikiPost = get_object_or_404(wikipostModel,pk=wikiPostID)

    context = {
        "wikiPost": wikiPost
    }
    return render(request, "wikiApp/detail.html", context)






# def login(request):
#     form=newuserForm(request.POST or None)
#     context={
#         'form':form
#     }
#     return render(request,'registration/login.html')


# def updatewiki(request):
#     return render(request,'wikiApp/profile.html')







