from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from bs4 import BeautifulSoup
import requests
from django.contrib import messages


# Create your views here.
def home_view(request, tag=None):
    # print(request)
    # # print(request.META)    
    # print('Request Method: ', request.method)
    
    # if request.method == 'POST':
    #     print('Data: ', request.POST)
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
        
    categories = Tag.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
        'tag': tag
    }
    return render (request, 'a_posts/home.html', context)
    
    
    
    



def post_create_view(request):
    form = PostCreateForm()
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # dont commit to database yet we have to add some more data
            
            website = requests.get(form.data['url']) # established the connection with flicker page
            sourcecode = BeautifulSoup(website.text, 'html.parser')  # parse the html code of the page
            
            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')
            image = find_image[0]['content']
            post.image = image
            
            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
            
            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist
            
            post.save()   # when webcrwal is done save the post to the database
            form.save_m2m() # save the tags to the database as well because its in the defferent table
            messages.success(request, 'Post Created Successfully')
            return redirect('home')
        # else:
        #     print('Form is not valid')
    return render(request, 'a_posts/post_create.html', {'form': form})

def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post Deleted Successfully')
        return redirect('home')
    return render(request, 'a_posts/post_delete.html', {'post': post})

def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post)
    context = {
        'post': post,
        'form': form
        }
    
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated Successfully')
            return redirect('home')
    return render(request, 'a_posts/post_edit.html', context)

def post_page_view(request, pk):
    # post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=pk) # this will return 404 error page if the post with the given id is not found
    return render(request, 'a_posts/post_page.html', {'post': post})