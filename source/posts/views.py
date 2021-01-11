from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,reverse
from posts.models import Post, Author, PostView
from posts.forms import CommentForm, PostForm
from django.db.models import Count
from django.db.models import Q



def search(request,*args,**kwargs):
    queryset = Post.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

    return render(request,"search_results.html",context={'queryset':queryset})    



def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

def get_author(user):
    queryset = Author.objects.filter(user=user)
    if queryset.exists():
        return queryset[0]
    return None    


def blog(request,*args,**kwargs):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    article_list = Post.objects.all()
    paginator = Paginator(article_list,4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)    
    return render(request, 'blog.html',context={'queryset':paginated_queryset, 
    'page_request_var':page_request_var, 'most_recent':most_recent, 'category_count':category_count})  

def post(request,id,*args,**kwargs):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post = Post.objects.get(id = id)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user,post=post)
    
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post_detail", kwargs={'id':post.id}))

    return render(request, 'post.html', context={'form': form,'post':post, 'most_recent':most_recent, 'category_count':category_count})

def post_create(request,*args,**kwargs):
    title = "Create"
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post_detail", kwargs={'id':form.instance.id}))

    return render(request,"post_create.html",context={'title':title,'form':form}) 

def post_update(request,id,*args,**kwargs):
    title = 'Update'
    post = Post.objects.get(id = id)
    form = PostForm(request.POST or None, request.FILES or None,instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post_detail", kwargs={'id':form.instance.id}))

    return render(request,"post_create.html",context={'title':title,'form':form})

def post_delete(request,id,*args,**kwargs):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(reverse("post_list"))

def about_us(request,*args,**kwargs):
    return render(request,'about_us.html')    