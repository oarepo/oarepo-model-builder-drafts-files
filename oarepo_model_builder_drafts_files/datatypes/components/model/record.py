import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.utils.python_name import convert_config_to_qualified_name
from oarepo_model_builder.validation.utils import ImportSchema



class RecordModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [DefaultsModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        module = datatype.definition["module"]["qualified"]
        profile_module = context["profile_module"]
        record_prefix = datatype.definition["module"]["prefix"]

        record = set_default(datatype, "record", {})
        record.setdefault("generate", True)
        records_module = record.setdefault("module", f"{module}.{profile_module}.api")
        record.setdefault("class", f"{records_module}.{record_prefix}Record")
        record.setdefault("base-classes", ["InvenioRecord"])
        record.setdefault(
            "imports",
            [
                {
                    "import": "invenio_records_resources.records.api.Record",
                    "alias": "InvenioRecord",
                }
            ],
        )
        record.setdefault("extra-code", "")
        convert_config_to_qualified_name(record)