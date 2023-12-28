# Caching in Django


Inspired by [J.O. Eriksson "Caching in Django" 2021-07-28](https://testdriven.io/blog/django-caching/)


## Cache some objects from database

```python
from django.core.cache import cache

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    objects = cache.get('objects')

    if objects is None:
        objects = Objects.all()
        cache.set('objects', objects)

    context['objects'] = objects

    return context

# ... do some updates on 'objects' somwhere else and

cache.delete('objects')
```


## Cache a whole page response (the view itself)

```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


BASE_URL = 'https://httpbin.org/'

# Cache the whole view for 5 minutes.
@method_decorator(cache_page(60 * 5), name='dispatch')
class ApiCalls(TemplateView):
    ...
```
