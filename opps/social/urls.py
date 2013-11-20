#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from tastypie.api import Api

from .api import Liked, Favorited


_api = Api(api_name=u"{}/social".format("v1"))
_api.register(Liked())
_api.register(Favorited())

urlpatterns = patterns(
    '',
    url(r'^api/', include(_api.urls)),
)