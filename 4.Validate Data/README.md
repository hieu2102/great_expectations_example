# Validate Data

## Define dataset

```python
datasource = "mysql_datasource"
data_asset_name = "yellow_tripdata_sample"
batch_request = {
    "datasource_name": datasource,
    "data_connector_name": "default_inferred_data_connector_name",
    "data_asset_name": data_asset_name,
    "limit": 1000,
}
```

## Run validation

Create checkpoint
```python
expectation_suite_name = "csv_suite"
checkpoint_config = {
    "class_name": "SimpleCheckpoint",
    "validations": [
        {
            "batch_request": batch_request,
            "expectation_suite_name": expectation_suite_name,
        }
    ],
}
checkpoint = SimpleCheckpoint(
    f"{validator.active_batch_definition.data_asset_name}_{expectation_suite_name}",
    context,
    **checkpoint_config,
)

```

Run validation
```python
checkpoint_result = checkpoint.run()
context.build_data_docs()
```

View result
```python
context.open_data_docs()
```