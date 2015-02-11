from django.contrib import admin
from .models import Question, LikeQuestion

admin.site.register(Question)
admin.site.register(LikeQuestion)