from django.views import generic
from blog import models as bmodels


class BlogIndex(generic.ListView):
    queryset = bmodels.Entry.objects.filter(publish=True)
    template_name = 'blog/home.html'
    paginate_by = 2
