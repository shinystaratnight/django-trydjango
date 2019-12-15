from django.shortcuts import render

def home_view(request):
    return render(request, "home.html", {})

def contact_view(request):
    return render(request, "contact.html", {})

def about_view(request):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 12313, 'ABC']
    }
    return render(request, "about.html", my_context)

def social_view(request):
    return render(request, "social.html", {})