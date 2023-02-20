from ruamel.yaml import YAML
import great_expectations as gx
from pprint import pprint

yaml = YAML()
context = gx.get_context()
checkpoint_name = "csv_mysql_chkpoint" # This was populated from your CLI command.

data_asset = "yellow_tripdata_sample"
expectations_suite_name="csv_suite"
yaml_config = f"""
name: {checkpoint_name}
config_version: 1.0
class_name: SimpleCheckpoint
run_name_template: "%Y%m%d-%H%M%S-getting_started_checkpoint"
validations:
  - batch_request:
      datasource_name: mysql_datasource
      data_connector_name: default_inferred_data_connector_name
      data_asset_name: {data_asset}
      data_connector_query:
        index: -1
    expectation_suite_name: {expectations_suite_name}
"""
context.add_checkpoint(**yaml.load(yaml_config))

context.run_checkpoint(checkpoint_name=checkpoint_name)
context.open_data_docs()