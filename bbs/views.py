from django.shortcuts import render,redirect

from django.views import View
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Topic
from .forms import TopicForm


class BbsView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):


        data    = Topic.objects.all().order_by("-dt")
        context = { "data":data }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        copied          = request.POST.copy()
        copied["dt"]    = timezone.now()
        copied["age"]   = request.user.age

        form    = TopicForm(copied)
        
        if form.is_valid():
            form.save()
        else:
            print("バリデーションエラー")

        return redirect("bbs:index")

index   = BbsView.as_view()

