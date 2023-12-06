from rest_framework import serializers
from .models import HaikuModel


class HaikuSerialzer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = HaikuModel
        fields = '__all__'

    def save(self, **kwargs):
        kwargs["author"] = self.fields['author'].get_default()
        return super().save(**kwargs)
