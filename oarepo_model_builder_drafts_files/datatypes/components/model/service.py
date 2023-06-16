from oarepo_model_builder.datatypes.components import RecordModelComponent, ResourceModelComponent, \
    ServiceModelComponent
from oarepo_model_builder_drafts_files.datatypes import DraftFileDataType
from oarepo_model_builder_files.datatypes.components import FilesServiceModelComponent


class DraftFilesServiceModelComponent(FilesServiceModelComponent):
    eligible_datatypes = [DraftFileDataType]
    dependency_remap = ServiceModelComponent

    def before_model_prepare(self, datatype, *, context, **kwargs):
        super().before_model_prepare(datatype, context=context, **kwargs)