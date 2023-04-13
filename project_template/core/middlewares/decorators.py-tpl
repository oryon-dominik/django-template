from django.utils.decorators import method_decorator, decorator_from_middleware
from functools import wraps


def middleware_on_class(middleware):
    """
        A class decorator to attach the designated middleware to a class-based view.

        Use as
        @middleware_on_class(MiddlewareClass)
        class View:
            ...

        Takes a single parameter, ``MiddlewareClass'', which must
        be a django middleware class (not an instance).

        The decorated class is modified in place.
        e.g.: from django.middleware.csrf import CsrfViewMiddleware
            if CsrfViewMiddleware is not in settings.MIDDLEWARE = [
                ...
                'django.middleware.csrf.CsrfViewMiddleware',
                ...
            ]

        ... this leads to:

        from core.middlewares import middleware_on_class
        from django.middleware.csrf import CsrfViewMiddleware
        middleware_on_class(CsrfViewMiddleware)

    """
    def decorator(cls):
        dispatch = cls.dispatch

        @wraps(dispatch)
        @method_decorator(decorator_from_middleware(middleware))
        def wrapper(self, *args, **kwargs):
            return dispatch(self, *args, **kwargs)

        cls.dispatch = wrapper
        return cls
    return decorator
