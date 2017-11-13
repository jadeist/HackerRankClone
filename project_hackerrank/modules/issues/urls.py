from django.conf.urls import url
from .views import ListIssues, DetailIssues,index, activities_issues, result

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^activity/$', activities_issues, name='index'),
    url(r'^activity/results/*', result),
    
    url(r'^issues/(?P<id>[\d]*)$',DetailIssues.as_view(), name="ListIssues"),
    url(r'^listissues/$', ListIssues.as_view(), name="ListIssues"),
]
