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
        sql_query = f"""
                        select emp.* from employees_employeeslots emp_slots 
                        inner join employees_employee emp on emp.EmployeeId = emp_slots.EmployeeId1 
                        where emp_slots.MeetingDate = '{date}' GROUP BY emp_slots.EmployeeId1
                    """

        cursor.execute(sql_query)
        res = cursor.fetchall()
        print("res == ", res)
        serializer = serializers.EmployeesSerializer(res, many=True)
        a_viewset = [
            'Uses actions (GET)',
        ]

        return Response({'a_viewset': a_viewset, 'response': serializer.data})


class AvailableMeetingSlots(APIView):

        def get(self, request, date, emp1_id, emp2_id):
            print(f" date {date}")
            print(f" date {emp1_id}")
            print(f" date {emp2_id}")
            cursor = connection.cursor()
            # sql_query = f"""
            #                 select e1.* from employees_employeeslots e1, employees_employeeslots e2 
            #                 WHERE e1.MeetingFromTime = e2.MeetingFromTime AND e1.MeetingTimeTo = e2.MeetingTimeTo
            #             """
            sql_query = f"""
                            SELECT t1.* from (SELECT MeetingFromTime, MeetingToTime FROM employees_employeeslots where EmployeeId1='{emp1_id}' and MeetingDate='{date}'
                            and message IS NULL) t1 
                            JOIN (SELECT MeetingFromTime, MeetingToTime FROM employees_employeeslots where EmployeeId1='{emp2_id}' and MeetingDate='{date}'
                            and message IS NULL) t2 
                            ON t1.MeetingFromTime = t2.MeetingFromTime AND t1.MeetingToTime = t2.MeetingToTime
                            """
            cursor.execute(sql_query)
            res = cursor.fetchall()
            print("res == ", res)
            serializer = serializers.MeetingSlotSerializer(res, many=True)
            a_viewset = [
                'Uses actions (GET)',
            ]

            return Response({'a_viewset': a_viewset, 'response': serializer.data})

