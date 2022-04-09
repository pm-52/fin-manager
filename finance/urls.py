from rest_framework import routers

from finance.views import CategoryViewSet, WaterfallViewSet

finance_router = routers.SimpleRouter()
finance_router.register(r"waterfall", WaterfallViewSet, "waterfall")
finance_router.register(r"category", CategoryViewSet, "finance_categorty")
