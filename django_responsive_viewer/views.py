from django.shortcuts import render
from django.conf import settings


def responsive_listing(request):
    pages_to_show = settings.RESPONSIVE_VIEWER
    layouts = getattr(settings, 'RESPONSIVE_SPECS', [])

    if request.GET.get('select-url'):
        first_url = request.GET.get('select-url')
    else:
        first_url = pages_to_show[0]

    return render(request,
                  'django_responsive_viewer/listing.html',
                  context={
                      'url_list': pages_to_show,
                      'first_url': first_url,
                      'layouts': layouts
                  })
