from django.shortcuts import redirect, render
from sc_home.models import feedback_model


def welcome(request):
    return render(request, "welcome.html")

def contact(request):

    if request.method=="POST" and "submit_feedback" in request.POST:
        topic = request.POST["topic"]
        message = request.POST["message"]
        
        fd_model = feedback_model.objects.create(topic=topic,feed=message,author=request.user)
        fd_model.save()
        return redirect('products:all_pr')


    return render(request, "contact.html")
