
from django.contrib import admin
from django.urls import path
from lms.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index , name="home"),
    path("student/",student,name="student"),
    path("search/",search, name="search"),

    path("book/",book,name="book"),
    path ("studentdelete/<int:id>",deletestudent, name="studentdelete"),
    path ("bookdelete/<int:id>",deletebook, name="bookdelete"),
]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
