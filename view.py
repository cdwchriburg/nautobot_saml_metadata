from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View
from onelogin.saml2.errors import OneLogin_Saml2_Error
from social_django.utils import load_backend, load_strategy


class MetadataView(View):
    """Simple metadata view to display metadata on a nautobot page.
    Import this view into your url file then add a uri path:
    path("metadata/", MetadataView.as_view(), name="metadata"),
    """

    def get(self, request):
        complete_url = reverse("social:complete", args=("saml",))
        saml_backend = load_backend(
            load_strategy(request),
            "saml",
            redirect_uri=complete_url,
        )
        try:
            metadata, errors = saml_backend.generate_metadata_xml()
            if not errors:
                return HttpResponse(content=metadata, content_type="text/xml")
        except OneLogin_Saml2_Error as saml_error:
            config = saml_backend.generate_saml_config()
            return HttpResponse(
                content=f"ERROR: {saml_error}, SAML backend config is {config}",
                content_type="text/plain"
            )
