
  
from rest_framework import serializers

class EmployeesSerializer(serializers.Serializer):
    FirstName= serializers.SerializerMethodField()
    MiddleName= serializers.SerializerMethodField()

    def get_FirstName(self, obj):
        return obj[1]

    def get_MiddleName(self, obj):
        return obj[2]    # index value at which last_name in tuple