from .models import Apiadress

class saveipadressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        try:
            ip_adress = Apiadress.objects.get(api_adress=ip)

        except Apiadress.DoesNotExist:
            ip_adress = Apiadress(api_adress=ip)
            ip_adress.save()

        request.user.ip_adress = ip_adress



        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response