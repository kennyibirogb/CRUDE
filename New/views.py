from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib import messages

def form_create_or_edit(request, post_id=None):
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        name = post.name
        address = post.address
        phone = post.phone
        age = post.age
        posts = Post.objects.all()  
    else:
        post = None
        name = ''
        address = ''
        phone = ''
        age = ''
        posts = Post.objects.all() 

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        
        if not all([name, address, phone, age]):
            messages.error(request, "All fields are required.")
            return render(request, 'CRUDE/form.html', {
                'posts': posts,
                'post': post,
                'name': name,
                'address': address,
                'phone': phone,
                'age': age
            })
        
        if post:
            post.name = name
            post.address = address
            post.phone = phone
            post.age = age 
        else:
            post = Post(name=name, address=address, phone=phone, age=age)
        
        try:
            age = int(age)
        except ValueError:
            messages.error(request, "Invalid input for age.")
            return render(request, 'CRUDE/form.html', {
                'posts': posts,
                'post': post,
                'name': name,
                'address': address,
                'phone': phone,
                'age': age
            })
        else:
            post.save()
            messages.success(request, "Form submission successful!")
            return redirect('form_create') 
    else:
        return render(request, 'CRUDE/form.html', {
            'posts': posts,
            'post': post,
            'name': name,
            'address': address,
            'phone': phone,
            'age': age
        })
        
def form_delete(request, post_id):
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('form_create')
    else:
        post = None
    