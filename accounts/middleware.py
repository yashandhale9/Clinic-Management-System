from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware


class DisableCSRFForAPI(MiddlewareMixin):
    """Disable CSRF for API endpoints"""
    
    def process_request(self, request):
        # Disable CSRF for API endpoints
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True)
        return None

