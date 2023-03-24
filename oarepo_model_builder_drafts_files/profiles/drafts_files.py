from pathlib import Path
from typing import Union

from oarepo_model_builder.builder import ModelBuilder
from oarepo_model_builder.schema import ModelSchema
from oarepo_model_builder.profiles import Profile


class DraftsFilesProfile(Profile):

    def build(
            self,
            model: ModelSchema,
            output_directory: Union[str, Path],
            builder: ModelBuilder,
    ):
        original_model_preprocessors = [model_preprocessor for model_preprocessor in builder.model_preprocessor_classes
                                        if "oarepo_model_builder." in str(model_preprocessor)]
        builder._validate_model(model)
        for model_preprocessor in original_model_preprocessors:
            model_preprocessor(builder).transform(model, model.settings)

        model.model_field = "files"
        builder.build(model, output_directory)