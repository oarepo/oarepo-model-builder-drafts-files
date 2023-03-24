import os

import lazy_object_proxy
from oarepo_model_builder.model_preprocessors import ModelPreprocessor
from oarepo_model_builder.utils.camelcase import snake_case


class InvenioDraftsFilesDraftModelPreprocessor(ModelPreprocessor):
    TYPE = "invenio_drafts_files_draft"
    def transform(self, schema, settings):
        files = schema.schema.files
        model = schema.schema.model

        files_record_prefix = f"{model.record_prefix}File"

        files.setdefault("record-prefix", f"{model.record_prefix}DraftFile")
        files.setdefault("collection-url", f'{model["collection-url"]}<pid_value>/draft')

        files.setdefault("record-resource-class", lazy_object_proxy.Proxy(lambda: f"{files.record_resources_package}.resource.{files_record_prefix}Resource"))
        files.setdefault("record-service-class",
                         lazy_object_proxy.Proxy(lambda: f"{files.record_services_package}.service.{files_record_prefix}Service"))
        #files.setdefault("record-dumper-class", model.record_dumper_class)

