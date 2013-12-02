#coding=utf-8
"""
__create_time__ = '13-10-17'
__author__ = 'Madre'
"""
import json
from django.http import HttpResponse
from utils.json_serializer import json_serializer


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    response_class = HttpResponse

    def json_required(self, request):
        if request.GET.get("format") == "json":  # or "json" in request.META.get("CONTENT_TYPE"):
            return True
        return False

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(
            self.convert_context_to_json(context),
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        """Convert the context dictionary into a JSON object"""
        context = json_serializer(context)
        return json.dumps(context)