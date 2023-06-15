import marshmallow as ma
from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder_tests.datatypes.components import ModelTestComponent
from oarepo_model_builder_drafts.datatypes.components.draft_tests import DraftModelTestComponent
from oarepo_model_builder_files.datatypes.components import FilesModelTestComponent


class DraftFilesModelTestComponent(DraftModelTestComponent):
    eligible_datatypes = [ModelDataType]
    dependency_remap = DraftModelTestComponent

    def process_tests(self, datatype, section, **extra_kwargs):
        super().process_tests(datatype, section, **extra_kwargs)
        section.constants["revision_id1"] = 3
        section.constants["revision_id2"] = 8
        section.constants["revision_id3"] = 13




class DraftFilesFilesModelTestComponent(FilesModelTestComponent):
    eligible_datatypes = [ModelDataType]
    dependency_remap = FilesModelTestComponent

    def process_files_tests(self, datatype, section, **extra_kwargs):
        super().process_files_tests(datatype, section, **extra_kwargs)
        section.constants["skip_continous_disable_files_test"] = True