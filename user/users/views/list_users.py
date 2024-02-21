from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ListUser(ListView):

    paginate_by = 10
    template_name = "list_user.html"

    def get(self, request):
        users = User.objects.all()
        page_num = request.GET.get('page', 3)

        paginator = Paginator(users, 6) # 6 employees per page

        page_obj = None
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            # if page is not an integer, deliver the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if the page is out of range, deliver the last page
            page_obj = paginator.page(paginator.num_pages)
        request.session['to_username'] = str(page_obj.object_list[0])

        return render(self.request, self.template_name, context={"page_obj": page_obj, "users": page_obj.object_list[0]})

    def post(self, request):


        return render(self.request, self.template_name)