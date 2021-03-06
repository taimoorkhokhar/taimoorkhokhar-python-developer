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
        '''
        API CALL: view all available employees for a specific date
        example route: http://127.0.0.1:8000/api/employees/2021-06-15/

        returns:
            dictionaray containing employees id, firstname, middlename
            and lastname for that date
        '''
        try:
            cursor = connection.cursor()
            sql_query = f"""
                            select emp.* from employees_employeeslots emp_slots 
                            inner join employees_employee emp on emp.EmployeeId = emp_slots.EmployeeId1 
                            where emp_slots.MeetingDate = '{date}' GROUP BY emp_slots.EmployeeId1
                        """

            cursor.execute(sql_query)
            res = cursor.fetchall()
            serializer = serializers.EmployeesSerializer(res, many=True)
            a_viewset = [
                'Uses actions (GET)',
            ]
            return Response({'a_viewset': a_viewset, 'response': serializer.data})
        except:
            return Response({'response':'404 Not Found'})


class AvailableMeetingSlots(APIView):
        serializer_class = serializers.BookMeetingSerializer
        renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

        def get(self, request, date, emp1_id, emp2_id):
            '''
            API CALL: view all available meeting slots for a specific date for two employees
            query params: date, employee1_id, employee2_id
            example route: http://127.0.0.1:8000/api/meeting_slots/2021-06-15/1/3/

            returns:
                dictionaray containing available meeting slots for both employees for that date
            '''
            try:
                cursor = connection.cursor()

                sql_query = f"""
                                SELECT t1.* from (SELECT MeetingFromTime, MeetingToTime FROM employees_employeeslots 
                                where EmployeeId1='{emp1_id}' and MeetingDate='{date}'and message IS NULL) t1 
                                JOIN (SELECT MeetingFromTime, MeetingToTime FROM employees_employeeslots 
                                where EmployeeId1='{emp2_id}' and MeetingDate='{date}' and message IS NULL) t2 
                                ON t1.MeetingFromTime = t2.MeetingFromTime AND t1.MeetingToTime = t2.MeetingToTime
                                Except SELECT MeetingFromTime, MeetingToTime FROM employees_employeeslots WHERE message='booked'
                                """
                cursor.execute(sql_query)
                res = cursor.fetchall()
                serializer = serializers.MeetingSlotSerializer(res, many=True)
                a_viewset = [
                    'Uses actions (GET)',
                ]

                return Response({'a_viewset': a_viewset, 'response': serializer.data})
            except:
                return Response({'response':'404 Not Found'})


        def put(self, request, date, emp1_id, emp2_id):
            '''
            API CALL: put request book meeting slot for a specific date for two employees
            query params: date, employee1_id, employee2_id
            example route: http://127.0.0.1:8000/api/meeting_slots/2021-06-15/1/3/
            json params: {"meeting_from_time": 12:00, "meeting_to_time": 13:00 }

            database changes:
            It will update meeting slots' message to booked.
            It will update Employee2Id for both employee slots.
            '''
            serializer = serializers.BookMeetingSerializer(data=request.data)
            try:
                if serializer.is_valid():
                    meeting_from_time = serializer.data['meeting_from_time']
                    meeting_to_time = serializer.data['meeting_to_time']
                    cursor = connection.cursor()
                    sql_query = f"""
                                    update employees_employeeslots set message='booked', EmployeeId2='{emp2_id}'
                                    where EmployeeId1='{emp1_id}' and MeetingDate='{date}'
                                    and MeetingFromTime = '{meeting_from_time}' and MeetingToTime = '{meeting_to_time}'
                                    """
                    cursor.execute(sql_query)
                    sql_query = f"""
                                    update employees_employeeslots set message='booked', EmployeeId2='{emp1_id}'
                                    where EmployeeId1='{emp2_id}' and MeetingDate='{date}'
                                    and MeetingFromTime = '{meeting_from_time}' and MeetingToTime = '{meeting_to_time}'
                                    """
                    cursor.execute(sql_query)
                    return Response({'response':"Meeting Booked"})

                return Response({'response':"Invalid time slots"})
            
            except:
                return Response({'response':'404 Not Found'})



class BookedMeetingSlots(APIView):

    def get(self, request, date):
        '''
        API CALL: view all booked meeting slots for a specific date
        example route: http://127.0.0.1:8000/api/booked_slots/2021-06-15/
        
        returns:
            dictionaray containing meeting slot, employee_1 id, employee_1 firstname, 
            employee_2 id, employee_2 firstname for that date
        '''
        try:
            cursor = connection.cursor()
            sql_query = f"""
                            select emp_slots.MeetingFromTime, emp_slots.MeetingToTime ,emp1.EmployeeId,emp1.FirstName,
                            emp2.EmployeeId,emp2.FirstName from employees_employeeslots emp_slots 
                            inner join employees_employee emp1 on (emp1.EmployeeId = emp_slots.EmployeeId1)
                            inner join employees_employee emp2 on (emp2.EmployeeId = emp_slots.EmployeeId2)
                            where emp_slots.MeetingDate = '{date}' and message='booked' group by emp_slots.MeetingFromTime  
                        """

            cursor.execute(sql_query)
            res = cursor.fetchall()
            serializer = serializers.ViewBookedMeetingSerializer(res, many=True)
            a_viewset = [
                'Uses actions (GET)',
            ]

            return Response({'a_viewset': a_viewset,'response': serializer.data})
        except:
                return Response({'response':'404 Not Found'})
