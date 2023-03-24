from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.outputs.python import PythonOutput
from oarepo_model_builder.utils.hyphen_munch import HyphenMunch


class InvenioDraftsTestResourcesBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_files_test_resources"
    template = "drafts-files-test-resources"
    MODULE = "tests.files.test_resources_draft"
    # todo PREVENT FILES PLUGIN
    def finish(self, **extra_kwargs):
        module = self.MODULE
        python_path = self.module_to_path(module)

        self.process_template(
            python_path,
            self.template,
            current_package_name=module,
            model=self.schema.model,
            **extra_kwargs,
        )