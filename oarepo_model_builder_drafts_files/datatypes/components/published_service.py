from typing import Dict

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import convert_config_to_qualified_name
from oarepo_model_builder_drafts.datatypes.components import PublishedServiceComponent
from oarepo_model_builder_files.datatypes import FileDataType


class DraftFilesPublishedServiceComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [PublishedServiceComponent]
    def before_model_prepare(self, datatype, *, context, **kwargs):
        if datatype.root.profile in {"record"}:
            service = set_default(datatype, "published-service", {})
            extra = """
    @property
    def files(self):
        return {{invenio_records_resources.proxies.current_service_registry}}.get("published_documents_file")
                          """
            extra_code = service.setdefault("extra-code", "")
            service["extra-code"] += extra

            config = set_default(datatype, "published-service-config", {})
            extra = """
    @property
    def components(self):
        return [*super().components, {{oarepo_runtime.services.files.FilesComponent}}, CreatePublishedBucketComponent]         
            """
            extra_code = service.setdefault("extra-code", "")
            config["extra-code"] += extra

class FilesPublishedServiceComponent(PublishedServiceComponent):
    eligible_datatypes = [FileDataType]
    dependency_remap = PublishedServiceComponent
    def before_model_prepare(self, datatype, *, context, **kwargs):
        if datatype.root.profile in {"files"}:
            profile_module = context["profile_module"]
            module = datatype.definition["module"]["qualified"]
            module_base_upper = datatype.definition["module"]["base-upper"]
            record_prefix = datatype.definition["module"]["prefix"]

            service_package = f"{module}.services.{profile_module}.published"

            config = set_default(datatype, "published-service-config", {})

            #config.setdefault(
            #    "config-key",
            #    f"{module_base_upper}_{context['profile_upper']}_PUBLISHED_SERVICE_CONFIG",
            #)
            config_module = config.setdefault(
                "module",
                f"{service_package}.config",
            )
            config.setdefault(
                "class",
                f"{config_module}.{record_prefix}PublishedServiceConfig",
            )
            config.setdefault("extra-code", "")
            config.setdefault(
                "service-id",
                "published_" + datatype.definition["service-config"]["service-id"],
            )
            config.setdefault(
                "base-classes",
                [
                    datatype.definition["service-config"]["class"]
                ],
            )
            convert_config_to_qualified_name(config)

            service = set_default(datatype, "published-service", {})

            service.setdefault("generate", True)
            config.setdefault("generate", service["generate"])

            #service.setdefault(
            #    "config-key",
            #    f"{module_base_upper}_{context['profile_upper']}_PUBLISHED_SERVICE_CLASS",
            #)
            #service.setdefault("proxy", "current_published_service")
            service_module = service.setdefault("module", f"{service_package}.service")
            service.setdefault("class", f"{service_module}.{record_prefix}PublishedService")
            service.setdefault("extra-code", "")
            service.setdefault(
                "base-classes",
                ["invenio_records_resources.services.FileService"],
            )
            service.setdefault(
                "imports",
                [
                    # {
                    #     "import": "oarepo_published_service.services.service.PublishedService",
                    #     "alias": "PublishedService",
                    # }
                ],
            )
            convert_config_to_qualified_name(service)





