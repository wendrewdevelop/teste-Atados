from rest_framework import serializers
from App.Acoes.models import Acao


class AcaoSerializer(serializers.ModelSerializer):
    local = serializers.SerializerMethodField()

    class Meta:
        model = Acao
        fields = '__all__'

    def get_local(self, obj):
        return '%s, %s, %s' % (obj.cidade, obj.bairro, obj.endereco)