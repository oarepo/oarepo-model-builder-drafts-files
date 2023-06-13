import marshmallow as ma
from oarepo_model_builder.datatypes import (
    DataType,
    DataTypeComponent,
    Import,
    ModelDataType,
    Section,
)
from oarepo_model_builder.datatypes.components import (
    DefaultsModelComponent,
    RecordMetadataModelComponent,
)
from oarepo_model_builder.datatypes.components.model.pid import process_pid_type
from oarepo_model_builder.datatypes.components.model.utils import (
    append_array,
    place_after,
    set_default,
)
from oarepo_model_builder.datatypes.model import Link
from oarepo_model_builder.utils.python_name import split_base_name


def get_draft_file_schema():
    from ..draft_file import DraftFileDataType

    return DraftFileDataType.validator()


class DraftFileComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    affects = [DefaultsModelComponent]

    class ModelSchema(ma.Schema):
        draft_files = ma.fields.Nested(get_draft_file_schema, attribute="draft-files", data_key="draft-files")

    def process_mb_invenio_record_service_config(self, *, datatype, section, **kwargs):
        if self.is_draft_files_profile:
            # override class as it has to be a parent class
            section.config.setdefault("record", {})[
                "class"
            ] = datatype.parent_record.definition["record"]["class"]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        if context["profile"] == "record":
            service = set_default(datatype, "service", {})
            service.setdefault("additional-args", ["files_service=service_thesis_file(app)", "draft_files_service=service_thesis_file_draft(app)"])
        self.is_draft_files_profile = context["profile"] == "draft_files"
        if not self.is_draft_files_profile:
            return

        parent_record_datatype: DataType = context["parent_record"]
        file_record_datatype: DataType = context["file_record"]
        datatype.parent_record = parent_record_datatype




        parent_file_record_prefix = file_record_datatype.definition["module"]["prefix"]
        parent_file_record_alias = file_record_datatype.definition["module"]["alias"]

        module = set_default(datatype, "module", {})
        module.setdefault(
            "qualified", file_record_datatype.definition["module"]["qualified"]
        )
        module.setdefault("prefix", f"{parent_file_record_prefix}Draft")
        module.setdefault("alias", f"{parent_file_record_alias}_draft")

        record = set_default(datatype, "record", {})
        record.setdefault("class", f"{parent_file_record_prefix}Draft")
        record.setdefault("base-classes", ["FileRecord"])
        record.setdefault(
            "imports", [{"import": "invenio_records_resources.records.api.FileRecord"}]
        )

        record_metadata = set_default(datatype, "record-metadata", {})
        record_metadata.setdefault("base-classes", file_record_datatype.definition["record-metadata"]["base-classes"])
        record_metadata.setdefault("imports", file_record_datatype.definition["record-metadata"]["imports"])

        resource_config = set_default(datatype, "resource-config", {})
        file_record_url = file_record_datatype.definition["resource-config"][
            "base-url"
        ]
        resource_config.setdefault("base-url", f"{file_record_url}/draft")
        resource_config.setdefault("base-classes", ["FileResourceConfig"])
        resource_config.setdefault(
            "imports",
            [{"import": "invenio_records_resources.resources.FileResourceConfig"}],
        )

        resource = set_default(datatype, "resource", {})
        resource.setdefault("base-classes", ["FileResource"])
        resource.setdefault(
            "imports",
            [
                {
                    "import": "invenio_records_resources.resources.files.resource.FileResource"
                }
            ],
        )



        service_config = set_default(datatype, "service-config", {})
        service_config.setdefault(
            "config-key",
            f"{split_base_name(module['qualified']).upper()}_{context['profile_upper']}_SERVICE_CONFIG",
        )
        service_config.setdefault(
            "base-classes", ["PermissionsPresetsConfigMixin", "FileServiceConfig"]
        )
        service_config.setdefault(
            "imports",
            [
                {"import": "invenio_records_resources.services.FileServiceConfig"},
                {
                    "import": "oarepo_runtime.config.service.PermissionsPresetsConfigMixin"
                },
            ],
        )

        service = set_default(datatype, "service", {})
        service.setdefault("base-classes", ["FileService"])
        service.setdefault(
            "imports", [{"import": "invenio_records_resources.services.FileService"}]
        )
        service.setdefault(
            "config-key",
            f"{split_base_name(module['qualified']).upper()}_{context['profile_upper']}_SERVICE_CLASS",
        )

        set_default(datatype, "search-options", {}).setdefault("skip", True)
        set_default(datatype, "json-schema-settings", {}).setdefault("skip", True)
        set_default(datatype, "mapping-settings", {}).setdefault("skip", True)
        set_default(datatype, "record-dumper", {}).setdefault("skip", True)

        set_default(datatype, "pid", file_record_datatype.definition["pid"])

        api = set_default(datatype, "api-blueprint", {})
        api.setdefault(
            "module",
            f"{module['qualified']}.views.{context['profile']}.api",
        )

        ma = set_default(datatype, "marshmallow", {})
        ma.setdefault("class", file_record_datatype.definition["marshmallow"]["class"])



