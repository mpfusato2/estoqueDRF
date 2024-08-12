from django.urls import path
#from django.conf.urls import url

#from .views import ProdutoApiView
from .views import ProdutoApiView

urlpatterns = [
    path('produtos/', ProdutoApiView.as_view(), name='produtos'),    

]