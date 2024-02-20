from django import template
from core.models import Post

register = template.Library()

@register.simple_tag(name='totallike')
def function(request):
    username = request.user.username
    total_likes_count = 0
    posts = Post.objects.filter(user=username)
    for post in posts:
        total_likes_count += post.no_of_likes
    return total_likes_count



