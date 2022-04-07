from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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
    'dec': "Learn MySQL for at least 30 minutes every day.",
}


def index(request):
    months = list(challenge_text.keys())
    list_items = ""
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-str", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    
    response_data = f"<h1>Challenges</h1><ul>{list_items}</ul>"
    return HttpResponse(response_data)


##################################################
# Normal view execution as per the associate url #
##################################################

def hello(request):
    return HttpResponse("Hello world")

##########################################
# Dynamic Path Segments & Capture Values #
##########################################

# This code is commented as it was for the purpose of getting start with Django views concept and was not optimized
#  
# def month(request, month):
#     challenge_text = None
#     if month == 'jan':
#         challenge_text = "Jump for at least 10 minutes every day."
#     elif month == 'feb':
#         challenge_text = "Walk for at least 20 minutes every day."
#     elif month == 'mar':
#         challenge_text = "Learn Django for at least 30 minutes every day."
#     else:
#         return HttpResponseNotFound("<h1>No such month</h1>")
#     return HttpResponse(f"<h1>{challenge_text}</h1>")

def month(request, month):
    try:
        page = challenge_text[month]
        return HttpResponse(f"<h1>{page}</h1>")
    except KeyError:
        return HttpResponseNotFound("<h1>No such month</h1>")


####################################################################
# Path Convertor - URL's route can be fixed to a specific datatype #
####################################################################

# This view will be triggered only when dynamically url is entered of int datatype
def month_int(request, month):
    months = list(challenge_text.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>No such month</h1>")
    else:
        redirect_month = months[month-1]

        # Problem with below return is that we have hardcoded the url to redirect to. What if in future someone changes
        # this 'challenges' url to something else?
        # To overcome, we will know about 'Reverse function and Named URL'
        
        #return HttpResponseRedirect("/challenges/"+redirect_month)

        redirect_path = reverse("month-str", args=[redirect_month]) # /challenges/<str:month>
        return HttpResponseRedirect(redirect_path)

