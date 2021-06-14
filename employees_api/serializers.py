  
from rest_framework import serializers
from datetime import datetime

def convert_time(time_str):
	return datetime.strptime(str(time_str), "%H:%M:%S").strftime("%H:%M")

''' serializer to view all employees'''
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

''' serializer to view meeting slots'''
class MeetingSlotSerializer(serializers.Serializer):
    meeting_from_time = serializers.SerializerMethodField()
    meeting_to_time = serializers.SerializerMethodField()

    def get_meeting_from_time(self,obj):
    	return convert_time(obj[0])

    def get_meeting_to_time(self, obj):
        return convert_time(obj[1])


''' serializer to book a meeting via put request'''
class BookMeetingSerializer(serializers.Serializer):
    meeting_from_time = serializers.TimeField()
    meeting_to_time = serializers.TimeField()
    class Meta:
        fields = (
            'meeting_from_time',
            'meeting_to_time'        
         )

''''
serializer to view booked meeting slots
inherit meeting slot serializer to get meeting time
'''
class ViewBookedMeetingSerializer(MeetingSlotSerializer):
	employee1_id = serializers.SerializerMethodField()
	employee1_name = serializers.SerializerMethodField()
	employee2_id = serializers.SerializerMethodField()
	employee2_name = serializers.SerializerMethodField()

	def get_employee1_id(self,obj):
		return obj[2]

	def get_employee1_name(self,obj):
		return obj[3]

	def get_employee2_id(self,obj):
		return obj[4]
	
	def get_employee2_name(self, obj):
		return obj[5]
