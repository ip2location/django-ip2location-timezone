import django
from django.conf import settings
from django.utils import timezone
import requests
import json

if django.VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin
    middleware_base_class = MiddlewareMixin
else:
    middleware_base_class = object

class IP2locationTimezoneMiddleware(middleware_base_class):
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        api_key = getattr(settings, 'IP2LOCATION_API_KEY')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        url = 'https://api.ip2location.com/v2/?ip=' + ip_address + '&key=' + api_key + '&package=WS11&format=json&addon=time_zone_info'
        response = requests.get(url)
        rec = json.loads(response.content)
        # if ip is localhost(127.0.0.1), use default timezone
        if ip_address == '127.0.0.1':
            tz = timezone.get_default_timezone()
        else:
            tz = rec['time_zone_info']['olson']
            timezone.activate(tz)
        request.ip_address = ip_address
        request.country_code = rec['country_code']
        request.country_name = rec['country_name']
        request.region_name = rec['region_name']
        request.city_name = rec['city_name']
        request.latitude = rec['latitude']
        request.longitude = rec['longitude']
        request.zip_code = rec['zip_code']
        request.time_zone = rec['time_zone']
        request.credits_consumed = rec['credits_consumed']
        request.olson_time_zone = rec['time_zone_info']['olson']
        request.current_time = rec['time_zone_info']['current_time']
        request.gmt_offset = rec['time_zone_info']['gmt_offset']
        request.is_dst = rec['time_zone_info']['is_dst']
        response = self.get_response(request)
        return response