from django.shortcuts import render
from forms import EmailForm
# Create your views here.

def home(request):

	return render(request, 'fb/home.html', {})


def login(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = EmailForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return home(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = EmailForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'fb/login.html', {'form': form})

