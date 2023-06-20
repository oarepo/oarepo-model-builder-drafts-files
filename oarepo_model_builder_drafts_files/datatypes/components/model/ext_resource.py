from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
import marshmallow as ma

from oarepo_model_builder.datatypes.components import ExtResourceModelComponent, DefaultsModelComponent
from oarepo_model_builder.datatypes.components.model.ext_resource import ExtResourceSchema
from oarepo_model_builder.datatypes.components.model.utils import set_default


class DraftFilesExtResourceModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [DefaultsModelComponent]

    class ModelSchema(ma.Schema):
        ext_resource = ma.fields.Nested(
            ExtResourceSchema,
            attribute="ext-resource",
            data_key="ext-resource",
        )
    def process_ext_resource(self, datatype, section, **kwargs):
        if self.is_draft_files_profile:
            cfg = section.config
            cfg["ext-service-name"] = "service_draft_files"
            cfg["ext-resource-name"] = "resource_draft_files"

    def before_model_prepare(self, datatype, *, context, **kwargs):
        self.is_draft_files_profile = context["profile"] == "draft_files"
        if not self.is_draft_files_profile:
            return
        ext = set_default(datatype, "ext-resource", {})

        ext.setdefault("generate", True)
        ext.setdefault("skip", False)

