from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)


def custom_login_required(function):
    # logger.debug(f'---custom_login_required---funn---')
    def wrapper(request, *args, **kw):
        # logger.debug(f'---custom_login_required---wrapper---funn---')
        user=request.user
        # if not (user.id and request.session.get('code_success')):
        if not (request.user.is_authenticated and request.user.last_name == 'customer'):
            return HttpResponseRedirect('/customer/login/')
        else:
            return function(request, *args, **kw)
    return wrapper