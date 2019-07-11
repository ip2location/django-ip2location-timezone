# Django IP2Location Timezone

Django IP2Location Timezone is a Django package that can help you easily display your website visitor the time according to their location. This package used **[IP2Location Web Service](https://www.ip2location.com/web-service/ip2location)** to get time zone information. 

## Requirements

1. Python 2.7 and above.
2. Django 1.11 and above.
3.  **[IP2Location Web Service](https://www.ip2location.com/web-service/ip2location)** API Key. You can get a trial API key from [IP2Location](https://www.ip2location.com/register?id=1005). 

## Quick Start

1. Install this package by using PYPI: 
	```bash
	pip install django-ip2location-timezone
	```
	
2. Add "*ip2location_timezone*" to your INSTALLED_APPS setting in settings.py:
	```python
    INSTALLED_APPS = (
      ...
      'ip2location_timezone',
    )
   ```
   
1. Add "*IP2locationTimezoneMiddleware*" to your MIDDLEWARE_CLASSES in settings.py:
	```python
	MIDDLEWARE_CLASSES = (
      ...
      'ip2location_timezone.middleware.IP2locationTimezoneMiddleware',
    )
   ```
   
4. Add your **[IP2Location Web Service](https://www.ip2location.com/web-service/ip2location)** API Key in settings.py:
	```python
	IP2LOCATION_API_KEY = 'YOUR_API_KEY'
   ```
   
5. In your template, add the following code to display the user time zone and current time:
	```python
	{% load tz %}
	{% localtime on %}
		{% get_current_timezone as TIME_ZONE %}
		Your timezone is {{ TIME_ZONE }}.<br/><br/>
		It is {% now "DATETIME_FORMAT" %}
	{% endlocaltime %}
	```


## Support

Email: [support@ip2location.com](mailto:support@ip2location.com).

URL: [https://www.ip2location.com](https://www.ip2location.com/)