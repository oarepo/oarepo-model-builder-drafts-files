from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType, DataType, Import, Section
from oarepo_model_builder.datatypes.components import (
    ServiceModelComponent, RecordModelComponent, ResourceModelComponent, PIDModelComponent,
    RecordMetadataModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import (
    append_array,
    prepend_array, set_default,
)
from oarepo_model_builder.datatypes.model import Link
from oarepo_model_builder_drafts.datatypes.components import DraftRecordModelComponent
from oarepo_model_builder_files.datatypes.components.files_field import FilesFieldModelComponent


class InvenioDraftsFilesRecordComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [
        ServiceModelComponent,
    ]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        if context["profile"] == "record":
            append_array(
                datatype,
                "service-config",
                "imports",
                {
                    "import": "invenio_drafts_resources.services.records.components.DraftFilesComponent"
                },
            )
            append_array(datatype, "service-config", "components", "DraftFilesComponent")
            service = set_default(datatype, "service", {})
            service.setdefault("additional-args", [
                f'files_service=self.service_files',
                f'draft_files_service=self.service_draft_files',
            ])


