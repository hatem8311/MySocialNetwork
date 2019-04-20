from django.conf.urls import url,include
from django.contrib import admin
from thenetwork import views
##هذا ن السطران متعلقان بتحميل الوسائط
##واعتقد انهما للوصول الى الوسائط نفسها على الموقع بواسط الزائر عن طرريق انشاء رابط لكل صور عند تحميلها بواسطة المسنخدم
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
##this line below is for redirecting the user to the login page when he open the website
    url(r'^$' , views.login_redirect , name = 'login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls' ,namespace='account') ),
    url(r'^home/', include('home.urls' ,namespace='home') ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
