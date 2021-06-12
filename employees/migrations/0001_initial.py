# Generated by Django 3.2.4 on 2021-06-11 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('departmentid', models.AutoField(db_column='DepartmentId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('createdon', models.DateTimeField(auto_now_add=True, db_column='CreatedOn')),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('designationid', models.AutoField(db_column='DesignationId', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
                ('createdon', models.DateTimeField(auto_now_add=True, db_column='CreatedOn')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeid', models.AutoField(db_column='EmployeeId', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=100)),
                ('middlename', models.CharField(db_column='MiddleName', max_length=100)),
                ('lastname', models.CharField(db_column='LastName', max_length=100)),
                ('employeecode', models.CharField(db_column='EmployeeCode', max_length=30)),
                ('createdon', models.DateTimeField(auto_now_add=True, db_column='CreatedOn')),
                ('modifiedon', models.DateTimeField(auto_now=True, db_column='ModifiedOn')),
                ('department', models.ForeignKey(db_column='DepartmentId', on_delete=django.db.models.deletion.DO_NOTHING, to='employees.department')),
                ('designation', models.ForeignKey(db_column='DesignationId', on_delete=django.db.models.deletion.DO_NOTHING, to='employees.designation')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSlots',
            fields=[
                ('employeeslotid', models.AutoField(db_column='EmployeeSlotId', primary_key=True, serialize=False)),
                ('meetingdate', models.DateField(blank=True, db_column='MeetingDate', null=True)),
                ('meetingfromtime', models.TimeField(blank=True, db_column='MeetingFromTime', null=True)),
                ('meetingtotime', models.TimeField(blank=True, db_column='MeetingToTime', null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('createdon', models.DateTimeField(auto_now_add=True, db_column='CreatedOn')),
                ('employee1', models.ForeignKey(blank=True, db_column='EmployeeId1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employee')),
                ('employee2', models.ForeignKey(blank=True, db_column='EmployeeId2', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employeeslot', to='employees.employee')),
            ],
        ),
    ]
