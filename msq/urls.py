from django.conf.urls import patterns, include, url

from django.contrib import admin
from questionnaire.views import questionnaire_form, submit_form
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', questionnaire_form, name="form"),
    url(r'^submit/$', submit_form, name="submit"),
    url(r'^admin/', include(admin.site.urls)),
)
