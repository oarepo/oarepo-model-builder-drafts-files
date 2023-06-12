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
    """
        links_item = {
        "self": ConditionalLink(
            cond=is_record,
            if_=RecordLink("{+api}/mocks/{id}"),
            else_=RecordLink("{+api}/mocks/{id}/draft"),
        ),
        "self_html": ConditionalLink(
            cond=is_record,
            if_=RecordLink("{+ui}/mocks/{id}"),
            else_=RecordLink("{+ui}/uploads/{id}"),
        ),
        "latest": RecordLink("{+api}/mocks/{id}/versions/latest"),
        "latest_html": RecordLink("{+ui}/mocks/{id}/latest"),
        "draft": RecordLink("{+api}/mocks/{id}/draft", when=is_record),
        "record": RecordLink("{+api}/mocks/{id}", when=is_draft),
        "publish": RecordLink("{+api}/mocks/{id}/draft/actions/publish", when=is_draft),
        "versions": RecordLink("{+api}/mocks/{id}/versions"),
    }
    """

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

            """
            service.setdefault("additional-args", [
                f'files_service=app.config["{file_record_datatype.definition["service"]["config-key"]}"](config=app.config["{file_record_datatype.definition["service-config"]["config-key"]}"]())',
                f'draft_files_service=app.config["{datatype.definition["service"]["config-key"]}"](config=app.config["{datatype.definition["service-config"]["config-key"]}"]())',
            ])
            """

