from django.shortcuts import redirect ,render


def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'erp/home.html')
    else:
        return redirect('/sign-in')