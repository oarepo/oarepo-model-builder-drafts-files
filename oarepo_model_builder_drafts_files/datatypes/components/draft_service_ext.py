from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import DefaultsModelComponent


class DraftServiceExtComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [
        DefaultsModelComponent,
    ]

    """
    def after_model_prepare(self, datatype, *, context, **kwargs):
        if context["profile"] != "record":
            return
        #da
        draft_section = datatype.schema.get_schema_section("files", ["record", "draft"], prepare_context={"parent_record": datatype})
        file_module = datatype.schema.get_schema_section("files", ["record", "files"], prepare_context={"parent_record": datatype})
        file_section = datatype.schema.get_schema_section("files", ["record", "files"], prepare_context={"parent_record": datatype})
        draft_section = datatype.schema.get_schema_section("draft-files", ["record", "draft-files"], prepare_context={"parent_record": datatype, "file_record": file_section, "switch_profile": False})
        print()
    """
