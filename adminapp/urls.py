from django.urls import path
from . import views


urlpatterns = [
    path("", views.admin_login, name="admin_login"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("users/", views.admin_users, name="admin_users"),
    path("users/<int:user_id>/", views.edit_user, name="edit_user"),
    path("category/", views.admin_category, name="admin_category"),
    path("brand/", views.admin_brand, name="admin_brand"),
    path("products/", views.admin_products, name="admin_products"),
    path("add_product/", views.add_product, name="add_product"),
    path("admin_orders/", views.admin_orders, name="admin_orders"),
    path("admin_coupon/", views.admin_coupon, name="admin_coupon"),
    path("admin_offers/", views.admin_offers, name="admin_offers"),
    path("edit_offers/<int:offer_id>/", views.edit_offers, name="edit_offers"),
    path("add_coupon/", views.add_coupon, name="add_coupon"),
    path("add_offers/", views.add_offers, name="add_offers"),
    path("edit_coupon/<int:c_id>/", views.edit_coupon, name="edit_coupon"),
    path("edit_product/<int:pid>/", views.edit_product, name="edit_product"),
    path("add_variant/", views.add_variant, name="add_variant"),
    path("edit_variant/<int:pv_id>/", views.edit_variant, name="edit_variant"),
    path(
        "update_status/<int:order_item_pk>", views.update_status, name="update_status"
    ),
    # path('add_variant/<int:pid>/', views.add_variant, name='edit_variant'),
    path(
        "admin_product/<int:product_id>/product-listing/",
        views.product_listing,
        name="product_listing",
    ),
    # path('admin_variant/<int:pv_id>/', dlt_variant, name='dlt_variant'),
    path("variants/", views.admin_variant, name="admin_variant"),
    path(
        "variants/<int:pv_id>/toggle-listing/",
        views.toggle_listing,
        name="toggle_listing",
    ),
    path(
        "admin_category/<int:category_id>/unlist_category/",
        views.unlist_category,
        name="unlist_category",
    ),
    path(
        "admin_brand/<int:brand_id>/unlist_brand/",
        views.unlist_brand,
        name="unlist_brand",
    ),
    path("logout/", views.logout_view, name="admin_logout"),
    path("report/", views.report, name="report"),
    path("admin_blog/", views.admin_blog, name="admin_blog"),
    path("add_blog/", views.add_blog, name="add_blog"),
    path("edit_blog/<int:blog_id>", views.edit_blog, name="edit_blog"),
    path("admin_request/", views.admin_request, name="admin_request"),
]
