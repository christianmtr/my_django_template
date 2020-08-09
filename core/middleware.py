from tenant_schemas.middleware import BaseTenantMiddleware


class XHeaderTenantMiddleware(BaseTenantMiddleware):
    """
    Determines tenant by the value of the ``X-DTS-SCHEMA`` HTTP header.
    """
    def get_tenant(self, model, hostname, request):
        schema_name = request.META.get('HTTP_X_DTS_SCHEMA', 'public')
        return model.objects.get(schema_name=schema_name)