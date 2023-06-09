from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder_files.datatypes import FileDataType

from oarepo_model_builder_drafts.datatypes.components import DraftParentComponent


class DraftFilesParentComponent(DraftParentComponent):
    eligible_datatypes = [FileDataType]
    affects = [DraftParentComponent]


    def before_model_prepare(self, datatype, *, context, **kwargs):
        if context["profile"] == "files":
            draft_parent_record = set_default(datatype, "draft-parent-record", {})
            draft_parent_record_metadata = set_default(
                datatype, "draft-parent-record-metadata", {}
            )
            draft_parent_record_state = set_default(
                datatype, "draft-parent-record-state", {}
            )
            draft_parent_record.setdefault("skip", True)
            draft_parent_record_state.setdefault("skip", True)
            draft_parent_record_metadata.setdefault("skip", True)
