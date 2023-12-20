from django.db import models

# Create your models here.
from django.utils import timezone
 
 
class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.title

def index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tod')
    form = TodoForm()


    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'tod/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('tod')


