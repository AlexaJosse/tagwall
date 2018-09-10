from django.shortcuts import render, redirect, get_object_or_404, reverse

from django.contrib.auth.decorators import login_required

from posts.models import Post, Tag

# Create your views here.

@login_required()
def home(request):
    posts = Post.objects.order_by('-votes_total')

    return render(request, 'posts/home.html', {'posts': posts})

@login_required()
def newpost(request):
    if request.method == 'POST':
        if request.POST['title']:
            if request.POST['body'] or request.FILES:
                post = Post()
                post.title = request.POST['title']

                if request.POST['url']:
                    if request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://'):
                        post.url = request.POST['url']
                    else:
                        posts.url = "http://" + request.POST['url']

                if request.POST['body']:
                    post.body = request.POST['body']

                if request.FILES:
                    if request.FILES['image']:
                        post.image = request.FILES['image']

                post.author = request.user

                post.save()
                return redirect('home')
            else:
                return render(request, 'posts/newpost.html', {'error': "Il faut au moins du texte ou une image"})
    else:
        return render(request, 'posts/newpost.html')

@login_required()
def upvote(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post,id=post_id)
        post.votes_total += 1
        post.save()

    return redirect(reverse('posts:postdetails', args=[post_id]))

@login_required()
def downvote(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post,id=post_id)
        post.votes_total -= 1
        post.save()
    return redirect(reverse('posts:postdetails', args=[post_id]))

@login_required()
def postdetails(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    tags = post.tag_set.all()
    tagslen = len(tags)
    return render(request, 'posts/postdetails.html', {'post': post,'tags':tags,'tagslen':tagslen})


def newtag(request, post_id):
    if request.method=='POST':
        if request.POST['body'] :
            tag = Tag()
            tag.body = request.POST['body']
            tag.post = get_object_or_404(Post,id=post_id)
            tag.author = request.user

            tag.save()

            return redirect(reverse('posts:postdetails', args=[post_id]))
        else:
            return redirect(reverse('posts:postdetails', args=[post_id]))

def whoiam(request):
    return render(request,'posts/whoiam.html')
