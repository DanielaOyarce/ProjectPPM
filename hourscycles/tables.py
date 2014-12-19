import django_tables2 as tables


class mainTable(tables.Table):
	aircraft = tables.Column(order_by=())