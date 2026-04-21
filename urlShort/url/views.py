import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import cache
from .forms import Url
from .models import UrlData


# ---------------------------
# Helper: generate unique slug
# ---------------------------
def generate_slug(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_unique_slug():
    for _ in range(5):  # retry limit
        slug = generate_slug()
        if not UrlData.objects.filter(slug=slug).exists():
            return slug
    raise Exception("Failed to generate unique slug")


# ---------------------------
# View: create short URL
# ---------------------------
def urlShort(request):
    if request.method == "POST":
        form = Url(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            slug = create_unique_slug()

            UrlData.objects.create(url=url, slug=slug)

            return redirect('/')  # could improve UX later
    else:
        form = Url()

    # limit data for performance
    data = UrlData.objects.order_by('-id')[:10]

    context = {
        'form': form,
        'data': data
    }

    return render(request, 'urlapp/index.html', context)


# ---------------------------
# View: redirect + analytics + caching
# ---------------------------
def urlRedirect(request, slugs):
    # try cache first
    data = cache.get(slugs)

    if not data:
        data = get_object_or_404(UrlData, slug=slugs)
        cache.set(slugs, data, timeout=300)  # cache for 5 minutes

    # increment clicks
    data.clicks += 1
    data.save(update_fields=['clicks'])

    return redirect(data.url)