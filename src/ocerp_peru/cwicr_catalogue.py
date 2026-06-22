from dataclasses import dataclass

@dataclass(frozen=True)
class CwicrV3Catalogue:
    region: str; country_iso: str; city: str; language: str; currency: str
    ddc_path: str; size_mb: int; available: bool; default_classification_standard: str = "masterformat"
    @property
    def collection(self): return f"cwicr_es_v3"

PE_AMAZONAS = CwicrV3Catalogue(region="PE_AMAZONAS", country_iso="PE", city="Amazonas", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_AMAZONAS_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=True)
PE_ANCASH = CwicrV3Catalogue(region="PE_ANCASH", country_iso="PE", city="Ancash", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_ANCASH_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_APURIMAC = CwicrV3Catalogue(region="PE_APURIMAC", country_iso="PE", city="Apurimac", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_APURIMAC_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_AREQUIPA = CwicrV3Catalogue(region="PE_AREQUIPA", country_iso="PE", city="Arequipa", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_AREQUIPA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_AYACUCHO = CwicrV3Catalogue(region="PE_AYACUCHO", country_iso="PE", city="Ayacucho", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_AYACUCHO_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_CAJAMARCA = CwicrV3Catalogue(region="PE_CAJAMARCA", country_iso="PE", city="Cajamarca", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_CAJAMARCA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_CALLAO = CwicrV3Catalogue(region="PE_CALLAO", country_iso="PE", city="Callao", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_CALLAO_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_CUSCO = CwicrV3Catalogue(region="PE_CUSCO", country_iso="PE", city="Cusco", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_CUSCO_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_HUANCAVELICA = CwicrV3Catalogue(region="PE_HUANCAVELICA", country_iso="PE", city="Huancavelica", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_HUANCAVELICA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_HUANUCO = CwicrV3Catalogue(region="PE_HUANUCO", country_iso="PE", city="Huanuco", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_HUANUCO_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_ICA = CwicrV3Catalogue(region="PE_ICA", country_iso="PE", city="Ica", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_ICA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_JUNIN = CwicrV3Catalogue(region="PE_JUNIN", country_iso="PE", city="Junin", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_JUNIN_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_LALIBERTAD = CwicrV3Catalogue(region="PE_LALIBERTAD", country_iso="PE", city="Lalibertad", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_LALIBERTAD_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_LAMBAYEQUE = CwicrV3Catalogue(region="PE_LAMBAYEQUE", country_iso="PE", city="Lambayeque", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_LAMBAYEQUE_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_LIMA = CwicrV3Catalogue(region="PE_LIMA", country_iso="PE", city="Lima", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_LIMA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_LORETO = CwicrV3Catalogue(region="PE_LORETO", country_iso="PE", city="Loreto", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_LORETO_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_MADREDEDIOS = CwicrV3Catalogue(region="PE_MADREDEDIOS", country_iso="PE", city="Madrededios", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_MADREDEDIOS_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_MOQUEGUA = CwicrV3Catalogue(region="PE_MOQUEGUA", country_iso="PE", city="Moquegua", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_MOQUEGUA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_PASCO = CwicrV3Catalogue(region="PE_PASCO", country_iso="PE", city="Pasco", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_PASCO_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_PIURA = CwicrV3Catalogue(region="PE_PIURA", country_iso="PE", city="Piura", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_PIURA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_PUNO = CwicrV3Catalogue(region="PE_PUNO", country_iso="PE", city="Puno", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_PUNO_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_SANMARTIN = CwicrV3Catalogue(region="PE_SANMARTIN", country_iso="PE", city="Sanmartin", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_SANMARTIN_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_TACNA = CwicrV3Catalogue(region="PE_TACNA", country_iso="PE", city="Tacna", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_TACNA_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_TUMBES = CwicrV3Catalogue(region="PE_TUMBES", country_iso="PE", city="Tumbes", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_TUMBES_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)
PE_UCAYALI = CwicrV3Catalogue(region="PE_UCAYALI", country_iso="PE", city="Ucayali", language="es", currency="PEN", ddc_path="PE___DDC_CWICR/PE_UCAYALI_workitems_costs_resources_EMBEDDINGS_BGEM3_V3_DDC_CWICR.snapshot", size_mb=420, available=False)

PE_CATALOGUES = (PE_AMAZONAS, PE_ANCASH, PE_APURIMAC, PE_AREQUIPA, PE_AYACUCHO, PE_CAJAMARCA, PE_CALLAO, PE_CUSCO, PE_HUANCAVELICA, PE_HUANUCO, PE_ICA, PE_JUNIN, PE_LALIBERTAD, PE_LAMBAYEQUE, PE_LIMA, PE_LORETO, PE_MADREDEDIOS, PE_MOQUEGUA, PE_PASCO, PE_PIURA, PE_PUNO, PE_SANMARTIN, PE_TACNA, PE_TUMBES, PE_UCAYALI)
