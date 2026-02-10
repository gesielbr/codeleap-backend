from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # ... suas rotas ...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # UI do Swagger:
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]