from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import RecordModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import base_name
from oarepo_model_builder_drafts.datatypes.components import DraftRecordModelComponent
from oarepo_model_builder_drafts_files.datatypes import DraftFileDataType
from oarepo_model_builder_files.datatypes.components.files_field import FilesFieldSchema, FilesFieldModelComponent
import marshmallow as ma


class DraftFilesFieldModelComponent(FilesFieldModelComponent):
    eligible_datatypes = [DraftFileDataType]
    depends_on = [RecordModelComponent]
    dependency_remap = FilesFieldModelComponent


    def before_model_prepare(self, datatype, *, context, **kwargs):
        if context["profile"] == "draft_file":
            record_class = datatype.definition["record"]["class"]

            files_field = set_default(datatype, "files-field", {})
            files_field.setdefault("file-class", base_name(record_class))
            files_field.setdefault("field-args", ["store=False","delete=False"])
            files_field.setdefault(
                "imports",
                [
                    {
                        "import": "invenio_records_resources.records.systemfields.FilesField"
                    },
                    {
                        "import": record_class
                    },
                ],
            )

            super().before_model_prepare(datatype, context=context, **kwargs)