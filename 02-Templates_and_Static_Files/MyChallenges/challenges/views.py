from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


challenge_text = {
    'jan': "Jump for at least 10 minutes every day.",
    'feb': "Walk for at least 20 minutes every day.",
    'mar': "Learn Django for at least 30 minutes every day.",
    'apr': "Learn Python for at least 30 minutes every day.",
    'may': "Learn JavaScript for at least 30 minutes every day.",
    'jun': "Learn React for at least 30 minutes every day.",
    'jul': "Learn Angular for at least 30 minutes every day.",
    'aug': "Learn Vue for at least 30 minutes every day.",
    'sep': "Learn Node for at least 30 minutes every day.",
    'oct': "Learn Express for at least 30 minutes every day.",
    'nov': "Learn MongoDB for at least 30 minutes every day.",
    'dec': None,
}


def index(request):
    months = list(challenge_text.keys())
    list_items = ""
    
    return render(request, "challenges/index.html", {"months": months})


##########################################
# Dynamic Path Segments & Capture Values #
##########################################

def month(request, month):
    try:
        page = challenge_text[month]

        # Rendering templates
        # 1. You can below way to render the template
        # response_data = render_to_string("challenges/challenge_page.html", {"text": page})
        # return HttpResponse(response_data)

        # OR
        # 2. Since rendering is a frequent process, Django has a way to combine above steps by using render function
        return render(request, "challenges/challenge_page.html", {"text": page, "month": month})
         
    except KeyError:

        # Below way of rendering 404 template will work however, there is also another concise way available
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        # Http404 is a class that you raise as an error. You can then pass an error message queue in it 
        # Now, what this will do automatically (because it's built into Django) is it will look 
        # or a 404 HTML file in your templates folders. So you should place such a file in your root templates
        # folder then and it also has to be named 404.html for Django to find it because it will look for
        # specifically that file.

        raise Http404()

####################################################################
# Path Convertor - URL's route can be fixed to a specific datatype #
####################################################################

# This view will be triggered only when dynamically url is entered of int datatype
def month_int(request, month):
    months = list(challenge_text.keys())
    if month > len(months):

        # We can also redirect here to 404 page, however, keeping it this implementation for reference purposes
        return HttpResponseNotFound("<h1>No such month</h1>")
    else:
        redirect_month = months[month-1]
        redirect_path = reverse("month-str", args=[redirect_month]) # /challenges/<str:month>
        return HttpResponseRedirect(redirect_path)