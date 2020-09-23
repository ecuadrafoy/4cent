import django_tables2 as tables
from .models import Traffic

#Use MultiTableMixin to add more than one table in a single view


class TrafficTable(tables.Table):
    class Meta:
        model = Traffic
        template_name = "django_tables2/bootstrap4.html"
        fields = ('docname', 'docdate','category', 'PIR', 'status','source', 'fulltext' )