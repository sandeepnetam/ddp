from django.urls import path, include

from . import views

app_name = 'livestock'
urlpatterns = [
  
    path('', views.LiveStockBaseView, name="livestock"),
    # path('entry/', views.LiveStockView.as_view(), name="livestock_entry" ),

    path('entry/district/', views.LiveStockDistrictView.as_view(), name="district_entry" ),
    path('entry/year/', views.LiveStockYearView.as_view(), name="year_entry" ),
    path('entry/livestockgroup/', views.LiveStockGroupView.as_view(), name="group_entry" ),
    path('entry/unit/', views.UnitView.as_view(), name="unit_entry" ),
    path('entry/item/', views.LiveStockItemView.as_view(), name="item_entry" ),
    path('entry/livestockdata/', views.LiveStockDataView.as_view(), name="data_entry" ),

	path('entry/district/<int:pk>/delete/', views.LiveStockDistrictView.DeleteDistrictView, name="delete_district_entry" ),
    path('entry/year/<int:pk>/delete/', views.LiveStockYearView.DeleteYearView, name="delete_year_entry" ),
    path('entry/livestockgroup/<int:pk>/delete/', views.LiveStockGroupView.DeleteGroupView, name="delete_group_entry" ),
    path('entry/unit/<int:pk>/delete/', views.UnitView.DeleteUnitView, name="delete_unit_entry" ),
    path('entry/item/<int:pk>/delete/', views.LiveStockItemView.DeleteItemView, name="delete_item_entry" ),
    path('entry/livestockdata/<int:pk>/delete/', views.LiveStockDataView.DeleteDataView, name="delete_data_entry" ),

    path('entry/district/<int:pk>/update/', views.LiveStockDistrictView.UpdateDistrictView, name="update_district_entry" ),
    path('entry/year/<int:pk>/update/', views.LiveStockYearView.UpdateYearView, name="update_year_entry" ),
    path('entry/livestockgroup/<int:pk>/update/', views.LiveStockGroupView.UpdateGroupView, name="update_group_entry" ),
    path('entry/unit/<int:pk>/update/', views.UnitView.UpdateUnitView, name="update_unit_entry" ),
    path('entry/item/<int:pk>/update/', views.LiveStockItemView.UpdateItemView, name="update_item_entry" ),
    path('entry/livestockdata/<int:pk>/update/', views.LiveStockDataView.UpdateDataView, name="update_data_entry" ),

 
    # path('entry/', views.YearListView.as_view(), name='yearlist'),
    # path('entry/<slug:year>/', views.DistrictListView.as_view(), name='districtlist'),
    # path('entry/<slug:year>/<slug:district>/', views.LiveStockGroupListView.as_view(), name='livestockgrouplist'),
    # path('entry/<slug:year>/<slug:district>/<slug:livestockgroup>/', views.LiveStockItemListView.as_view(), name='livestockitemlist'),
    # path('entry/<slug:year>/<slug:district>/<slug:livestockgroup>/<slug:livestockitem>/', views.LiveStockDataListView.as_view(), name='livestockdatalist'),
    # path('entry/<slug:year>/<slug:district>/<slug:livestockgroup>/<slug:livestockitem>/<int:pk>/', views.LiveStockDataDetailView.as_view(), name="livestockdatadetail" ),
    
    # path('entry/district/', views.LiveStockDistrictView.as_view(), name="livestock_district_entry" ),
]