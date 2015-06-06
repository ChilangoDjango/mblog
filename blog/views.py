from django.views import generic
from blog import models as bmodels


class BlogIndex(generic.ListView):
    queryset = bmodels.Entry.objects.filter(publish=True)
    template_name = 'blog/index.html'
    paginate_by = 2


class PostDetail(generic.DetailView):
    model = bmodels.Entry
    template_name = 'blog/post.html'
