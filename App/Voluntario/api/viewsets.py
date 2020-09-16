from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from App.Voluntario.models import Voluntario
from App.Voluntario.api.serializers import VoluntarioSerializer


class VoluntarioViewset(viewsets.ModelViewSet):
    serializer_class = VoluntarioSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome')

    def get_queryset(self):
        #Definindo parametros de busca
        '''
            O paramêtro poderia ser definido como uma lista, porém
            se não fosse preenchido o sistema apresentaria um erro.

            id = self.request.query_params['id']
        '''
        nome = self.request.query_params.get('nome', None)
        
        #Instanciando a queryset
        queryset = Voluntario.objects.all()
        
        if nome:#se o NOME existir
            queryset.filter(nome__iexact = nome)#busca NOME

        return queryset

    def list(self, request, *args, **kwargs):
        return super(VoluntarioViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(VoluntarioViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VoluntarioViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VoluntarioViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(VoluntarioViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(VoluntarioViewset, self).partial_update(request, *args, **kwargs)
