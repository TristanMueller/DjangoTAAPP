from django.contrib import admin

from .models import User
admin.site.register(User)
from .models import Courses
admin.site.register(Courses)
from .models import Labs
admin.site.register(Labs)
from .models import Contacts
admin.site.register(Contacts)