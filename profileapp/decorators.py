from django.http import HttpResponseForbidden
from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if not target_profile.owner == requset.user:
            return HttpResponseForbidden()
        else:
            return func(requset, *args, **kwargs)
    return decorated
