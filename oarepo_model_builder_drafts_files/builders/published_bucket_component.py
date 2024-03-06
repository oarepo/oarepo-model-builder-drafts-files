from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class PublishedBucketComponentBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "published_bucket_component"
    section = "published-service-config"
    template = "published-bucket-component"