from user.api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', userviewsets, base_name='user_api')
