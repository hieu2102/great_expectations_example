# Create Datasources
you can create datasource interactively using command
```bash
great_expectations datasource new
```

## Fill in datasource detail
modify `create_datasource.py` to fit your environment
```python
## csv datasource
datasource_dir = "../data"
## sql datasource
host = ""
port = ""
username = ""
password =""
database = ""
schema_name = ""
table_name=""
```

## Create datasource
```bash
python create_datasource.py
```
**notes**: If you are using SQL datasources, the database credential will be stored as plaintext in `great_expectations.yaml`

Update `uncommitted/config_variables.yaml` to store your private variables
```yaml
mysql_datasource_host: xxx.xxx.xxx.xxx
mysql_datasource_port: xxxx
mysql_datasource_username: xxxx
mysql_datasource_password: xxxx
```

Update `great_expectations.yaml` to use the variables specified
```yaml
  mysql_datasource:
    ....
    execution_engine:
      credentials:
        host: ${mysql_datasource_host}
        port: ${mysql_datasource_port}
        username: ${mysql_datasource_username}
        password: ${mysql_datasource_password}
        database: ${mysql_datasource_database}
        drivername: mysql+pymysql
      module_name: great_expectations.execution_engine
      class_name: SqlAlchemyExecutionEngine
    class_name: Datasource

```
