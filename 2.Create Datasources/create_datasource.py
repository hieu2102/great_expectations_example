import great_expectations as gx
from great_expectations.cli.datasource import sanitize_yaml_and_save_datasource, check_if_datasource_name_exists

# connect to gx
context = gx.get_context()

# datasources variables
datasource_name = "my_datasource"
## csv datasource
# datasource_dir = "../data"

## sql datasource
# host = ""
# port = ""
# username = ""
# password =""
# database = ""
# schema_name = ""
# table_name=""

datasource_yaml_template=""
with open(datasource_yaml_template, 'r') as file:
    datasource_config = file.read()

sanitize_yaml_and_save_datasource(context, datasource_config, overwrite_existing=False)
