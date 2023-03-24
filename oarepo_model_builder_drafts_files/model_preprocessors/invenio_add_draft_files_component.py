import os

import lazy_object_proxy
from oarepo_model_builder.model_preprocessors import ModelPreprocessor
from oarepo_model_builder.utils.camelcase import snake_case


class InvenioAddDraftFilesComponentModelPreprocessor(ModelPreprocessor):
    TYPE = "invenio_add_draft_files_component"

    def transform(self, schema, settings):
        current_model = schema.current_model
        current_model.record_service_config_components.append()
