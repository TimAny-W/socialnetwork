from django.conf import settings

def context_processor(request):
    """Context processor
       :return: media_url for all templates
    """
    return {'media_url': settings.STATIC_ROOT}