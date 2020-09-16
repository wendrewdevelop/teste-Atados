from rest_framework import serializers
from App.Voluntario.models import Voluntario


class VoluntarioSerializer(serializers.ModelSerializer):
    nome_completo = serializers.SerializerMethodField()

    class Meta:
        model = Voluntario
        fields = '__all__'

    def get_nome_completo(self, obj):
        return '%s %s' % (obj.nome, obj.sobrenome)
