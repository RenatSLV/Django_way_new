from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class LoginRequiredMixinPlus(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_active:
            raise PermissionDenied("Ваш аккаунт деактивирован.")
        return super().dispatch(request, *args, **kwargs)
