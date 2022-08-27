from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from short_url.models import ShortUrl

from short_url.utils import get_random_id

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    return render(request, 'short_url/index.html')


@require_http_methods(['POST'])
def add_url(request):
    print(request.POST)
    account_name = '_'.join(request.POST['user_name'].split(' '))
    full_url = request.POST['full_url']
    url_name = request.POST['url_name']
    short_url = ShortUrl(account_name=account_name, full_url=full_url, url_name=url_name,slug=get_random_id())
    short_url.save()
    
    protocol = 'https' if request.is_secure() else 'http'
    
    return redirect('short_urls:list')


@require_http_methods(['GET'])
def url_list(request):
    all_url_set = ShortUrl.objects.all()
    url_collection = {}
    for url in all_url_set:
        account_name = url.account_name
        if account_name not in url_collection:
            url_collection[account_name] = []
            
        url_collection[account_name].append((url.url_name, url.slug))

    return render(request, 'short_url/list.html', {"url_collection": url_collection})


@require_http_methods(['GET'])
def go_to_page(request, slug):
    slug = get_object_or_404(ShortUrl, slug=slug)
    
    
    return redirect(slug.full_url)
    
    