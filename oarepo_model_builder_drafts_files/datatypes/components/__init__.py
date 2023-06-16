from oarepo_model_builder_drafts_files.datatypes.components.draft_file_profile import DraftFileComponent
from oarepo_model_builder_drafts_files.datatypes.components.draft_files_tests import DraftFilesModelTestComponent, \
    DraftFilesFilesModelTestComponent
from oarepo_model_builder_drafts_files.datatypes.components.draft_service_ext import DraftServiceExtComponent
from oarepo_model_builder_drafts_files.datatypes.components.drafts_files_files import InvenioDraftsFilesComponent
from oarepo_model_builder_drafts_files.datatypes.components.drafts_files_field import DraftFilesFieldModelComponent
from oarepo_model_builder_drafts_files.datatypes.components.drafts_files_record import InvenioDraftsFilesRecordComponent
from oarepo_model_builder_drafts_files.datatypes.components.model import DraftFilesDefaultsModelComponent, \
    DraftFilesMarshmallowModelComponent, DraftFilesRecordModelComponent, DraftFilesRecordMetadataModelComponent, \
    DraftFilesResourceModelComponent, DraftFilesServiceModelComponent, DraftFilesPIDModelComponent, \
    DraftFilesBlueprintsModelComponent

DRAFTS_FILES_COMPONENTS = [InvenioDraftsFilesComponent,  DraftFilesFieldModelComponent, DraftFileComponent, InvenioDraftsFilesRecordComponent,
                           DraftServiceExtComponent, DraftFilesModelTestComponent, DraftFilesFilesModelTestComponent,
                           DraftFilesDefaultsModelComponent,
                           DraftFilesMarshmallowModelComponent,
                           DraftFilesRecordModelComponent,
                           DraftFilesRecordMetadataModelComponent,
                           DraftFilesResourceModelComponent,
                           DraftFilesServiceModelComponent,
                           DraftFilesPIDModelComponent,
                           DraftFilesBlueprintsModelComponent
                           ]