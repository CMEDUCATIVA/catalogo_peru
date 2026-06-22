from app.core.partner_pack.manifest import PartnerBranding, PartnerPackManifest

MANIFEST = PartnerPackManifest(
    slug="peru",
    partner_name="Peru Construction Pack",
    partner_url="https://github.com/CMEDUCATIVA/ocerp-peru",
    pack_version="0.1.0",
    description="Peru: PEN, Lima, es-PE.",
    default_locale="es-PE",
    additional_locales={"es-PE": "locales/es-PE.json"},
    cwicr_regions=["cwicr-spa-peru"],
    default_currency="PEN",
    default_tax_template="peru_vat",
    validation_rule_packs=[],
    default_modules=[],
    hidden_modules=[],
    demo_template_ids=[],
    branding=PartnerBranding(primary_color="#D91023", accent_color="#FFFFFF", logo_path="logo.svg"),
    onboarding_script_path="onboarding.yaml",
    metadata={"country": "PE", "country_name_es": "Peru", "iso_3166_1_alpha_2": "PE", "currency": "PEN", "utc": -5, "support_email": "info@cmeducativa.com"},
)
