from rest_framework import routers
from App.Voluntario.api.viewsets import VoluntarioViewset
from App.Acoes.api.viewsets import AcaoViewset


router = routers.DefaultRouter()

# voluntarios Endpoint API
router.register(
    r'voluntarios',
    VoluntarioViewset,
    basename='voluntarios',
)

# acoes Endpoint API
router.register(
    r'acoes',
    AcaoViewset,
    basename='acoes',
)