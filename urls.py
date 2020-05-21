from rest_framework import routers
from .api import vicerviewset

router=routers.DefaultRouter()
router.register('api/vicers',vicerviewset,'vicers')
urlpatterns=router.urls