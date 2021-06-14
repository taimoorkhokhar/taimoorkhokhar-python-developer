from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import (
                                        HTMLFormRenderer,
                                        JSONRenderer,
                                        BrowsableAPIRenderer,
                                    )

from . import serializers
from django.db import connection




class AvailableEmployees(APIView):

    def get(self, request,date):
        print(f" date {date}")
        cursor = connection.cursor()
        sql_query = f"""select emp.* from employees_employeeslots emp_slots 
                            inner join employees_employee emp on emp.EmployeeId = emp_slots.EmployeeId1 
                            where emp_slots.MeetingDate = '{date}' GROUP BY emp_slots.EmployeeId1"""
        cursor.execute(sql_query)

        res = cursor.fetchall()
        print("res == ", res)
        serializer = serializers.EmployeesSerializer(res, many=True)
        a_viewset = [
            'Uses actions (GET)',
        ]

        return Response({'a_viewset': a_viewset, 'response': serializer.data})


# class Employees(APIView):

#     def get(self, request):
#         cursor = connection.cursor()
#         cursor.execute('select * from employees_employee')
#         res = cursor.fetchall()
#         print("res == ", res)
#         serializer = serializers.EmployeesSerializer(res, many=True)
#         a_viewset = [
#             'Uses actions (GET)',
#         ]

#         return Response({'a_viewset': a_viewset, 'response': serializer.data})


# class EmployeesSlots()
