from rest_framework import serializers, status

from .models import Car


class LicenseSerializer(serializers.Serializer):
    plate_number = serializers.CharField()
    tech_pass = serializers.CharField(required=False)

    def to_representation(self, instance):
        return instance

    def create(self, validated_data):
        plate_number = validated_data['plate_number']
        tech_pass = validated_data['tech_pass']

        if plate_number is not None:
            raise serializers.ValidationError(
                {"message": "Plate number is invalid", "code": status.HTTP_400_BAD_REQUEST})
        return {plate_number: tech_pass}


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'number', 'order')


class OrderCarSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(),
        source='car',
    )
    order = serializers.IntegerField()

    def validate_car(self, car: Car):
        request = self.context['request']
        user = request.user
        if user != car.user:
            raise serializers.ValidationError('Not found.')
        return car

    def create(self, validated_data):
        car = validated_data['car']
        car.order = validated_data['order']
        car.save()
        return {'id': car.id, 'order': car.order}
