from django.middleware.csrf import get_token as get_csrf_token
from django.middleware.csrf import CsrfViewMiddleware


class EnsureCsrfCookie(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        retval = super().process_view(request, callback, callback_args, callback_kwargs)
        # Force process_response to send the cookie
        get_csrf_token(request)
        return retval
