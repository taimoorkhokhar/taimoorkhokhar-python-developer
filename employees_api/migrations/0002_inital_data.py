from django.db import migrations, models
import django.db.models.deletion
import os

from django.db import connection, migrations
from django.db import connection
import re
# from StringIO import StringIO
from django.conf import settings
import os



def load_data_from_sql(app, schema_editor):
    file_path = os.path.join(os.path.dirname(__file__), '../sql/', 'sampleData.sql')
    sql_statement = open(file_path,'r').read()

    with connection.cursor() as c:
        c.executescript(sql_statement)



class Migration(migrations.Migration):

    # initial = True


    dependencies = [
        ('employees_api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data_from_sql),
    ]