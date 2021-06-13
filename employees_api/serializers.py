
  
from rest_framework import serializers

class EmployeesSerializer(serializers.Serializer):
    employee_id = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    middle_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_employee_id(self,obj):
    	return obj[0]

    def get_first_name(self, obj):
        return obj[1]

    def get_middle_name(self, obj):
        return obj[2]

    def get_last_name(self, obj):
        return obj[3]