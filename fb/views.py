from django.shortcuts import render
from forms import EmailForm , LoginForm , UserProfileForm
from fb.models import Join , UserProfile
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):

	return render(request, 'fb/home.html', {})


def register(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = EmailForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect('/fb/login/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = EmailForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'fb/register.html', {'form': form})


def login(request):
    """
    Log in view
    """
    try:
        if request.session['email']:
            return  HttpResponseRedirect('/fb/sucess/')
    except:
        pass
    if request.method == 'POST':
        #print request.POST
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = Join.objects.filter(email=form.cleaned_data['email'], passwrd=form.cleaned_data['passwrd'])
                if len(user) == 1:
                    request.session['email'] = user[0].email
                    return HttpResponseRedirect('/fb/sucess/')
                else:
                    return HttpResponse("Login Credentials didn't match, Please try again")
            except User.DoesNotExist:
                return None
    else:
        form = LoginForm()
    return render(request, 'fb/login.html', {'form': form})



def about(request):

    return render(request, 'fb/about.html', {})

def sucess(request):
    if request.session['email']:
        return render(request,'fb/loggedin.html',{})
    else:
        return HttpResponseRedirect('/fb/login/')

def logout(request):
    del request.session['email']
    return HttpResponseRedirect('/fb/login/')

def user_profile(request):
    if request.session['email']:
        if request.method =='POST':
            a=Join.objects.get(email=request.session['email'])
            try:
                b=UserProfile.objects.get(user=a)
            except:
                b = UserProfile(user=a)
                b.save()
                b=UserProfile.objects.get(user=a)
            form = UserProfileForm(request.POST,instance=b)
            if form.is_valid():
                f= form.save(commit=False)
                f.user=a
                f.save()
                return HttpResponseRedirect('/fb/login/')
            else:
                return render(request,'fb/profile.html',{'form':form})
        else:
            a=Join.objects.get(email=request.session['email'])
            try:
                b=UserProfile.objects.get(user=a)
            except:
                b = UserProfile(user=a)
                b.save()
                b=UserProfile.objects.get(user=a)
            form=UserProfileForm(instance=b)
            return render(request,'fb/profile.html',{'form':form})
    else:
        return HttpResponseRedirect('/fb/login/')

#def loggedin(request):
#    HttpResponseRedirect('/fb/loggedin')
