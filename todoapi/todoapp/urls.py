from rest_framework import routers
from .views import TODOViewset

router = routers.DefaultRouter()
router.register('todo',TODOViewset)