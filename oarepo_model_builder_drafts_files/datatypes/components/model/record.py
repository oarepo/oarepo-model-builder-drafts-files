from oarepo_model_builder.datatypes import DataTypeComponent, DataType
from oarepo_model_builder.datatypes.components import RecordModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import base_name, split_base_name, split_package_base_name
from oarepo_model_builder_drafts.datatypes import DraftDataType
from oarepo_model_builder_drafts_files.datatypes import DraftFileDataType


class DraftFileRecordModelComponent(RecordModelComponent):
    eligible_datatypes = [DraftFileDataType]
    dependency_remap = RecordModelComponent


    def before_model_prepare(self, datatype, *, context, **kwargs):
        # todo refactor files into this pattern? it makes more sense to inherit this from file component
        file_record_datatype: DataType = context["file_record"]
        parent_file_record_prefix = file_record_datatype.definition["module"]["prefix"] #todo use section here?

        draft_file_record = set_default(datatype, "record", {})
        draft_file_record.setdefault("class", f"{parent_file_record_prefix}Draft")
        draft_file_record.setdefault("base-classes", ["FileRecord"])
        draft_file_record.setdefault(
            "imports", [{"import": "invenio_records_resources.records.api.FileRecord"}]
        )
        super().before_model_prepare(datatype, context=context, **kwargs)