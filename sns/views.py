from django.shortcuts import render,redirect
from django.views import View

from .models import Park
from .forms import ParkForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        context["parks"]    = Park.objects.all()

        return render(request, "sns/index.html", context)

    def post(self, request, *args, **kwargs):

        form    = ParkForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)


        return redirect("sns:index")



index   = IndexView.as_view()
