from .models import Contact


def my_context(request):
    profile = Contact.objects.get(id=2)
    return {"profile": profile}
