from django.http import HttpResponsePermanentRedirect

class FixRedirectMiddleware(object):
    
    def process_request(self, request):
        if request.get_host() == "www.pacsee.hu":
            return HttpResponsePermanentRedirect("http://pacsee.hu")