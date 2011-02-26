from test_yarned.test_yarned_app.models import RequestSnapShot


class RequestFilterMiddleware(object):
    def process_request(self, request):
        if request.user.is_anonymous():
            user = None
        else:
            user = request.user
        ress = RequestSnapShot()
        ress.user = user
        ress.path = request.META['PATH_INFO']
        ress.save()
