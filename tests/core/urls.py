try:
    from django.conf.urls import patterns, url, include
except ImportError:
    from django.conf.urls.defaults import patterns, url, include

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, FacetedSearchView


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns(
    'haystack.views',
    url(r'^$', SearchView(load_all=False), name='haystack_search'),
    url(
        r'^faceted/$',
        FacetedSearchView(
            searchqueryset=SearchQuerySet().facet('author'),
            form_class=FacetedSearchForm
        ),
        name='haystack_faceted_search'),
    url(
        r'^basic/$',
        'basic_search',
        {'load_all': False},
        name='haystack_basic_search'
    ),
)
