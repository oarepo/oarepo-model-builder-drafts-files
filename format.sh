black oarepo_model_builder_drafts_files build-tests --target-version py310
autoflake --in-place --remove-all-unused-imports --recursive oarepo_model_builder_drafts_files build-tests
isort oarepo_model_builder_drafts_files build-tests  --profile black
