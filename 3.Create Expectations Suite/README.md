# Create Expectations Suite
## About Expectations Suite
an `Expectations Suite` is a test suite to validate data

an `Expectations Suite` contains
- list of test cases
- sample data


## Creating Expectations Suite

### Define test data
```python
datasource = "csv_datasource"
data_asset_name = "sample.csv"
batch_request = {
    "datasource_name": datasource,
    "data_connector_name": "default_inferred_data_connector_name",
    "data_asset_name": data_asset_name,
    "limit": 1000,
}
```

### Create Default Expectations with Onboarding Assistant

```python

context = gx.get_context()

expectation_suite_name = "csv_suite"

validator = context.get_validator(
    batch_request=BatchRequest(**batch_request),
    expectation_suite_name=expectation_suite_name,
)

result = context.assistants.onboarding.run(
    batch_request=batch_request
)
validator.save_expectation_suite(discard_failed_expectations=False)
```
