"""
URLs for course_info API
"""
from django.conf import settings
from django.conf.urls import patterns, url

from .views import CourseHandoutsList, CourseUpdatesList

urlpatterns = patterns(
    'mobile_api.course_info.views',
    url(
        r'^{}/handouts$'.format(settings.COURSE_ID_PATTERN),
        CourseHandoutsList.as_view(),
        name='course-handouts-list'
    ),
    url(
        r'^{}/updates$'.format(settings.COURSE_ID_PATTERN),
        CourseUpdatesList.as_view(),
        name='course-updates-list'
    ),
)
