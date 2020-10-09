import django_tables2 as tables
from .models import Traffic
from django_tables2.utils import A 
#Use MultiTableMixin to add more than one table in a single view


class TrafficTable(tables.Table):
    docname = tables.LinkColumn('logger:traffic_detail', args=[A('traffic_slug')])
    class Meta:
        model = Traffic
        #template_name = "django_tables2/bootstrap4.html"
        fields = ('docname', 'docdate','category', 'PIR', 'source','status','user')
        order_by = ('-docdate')