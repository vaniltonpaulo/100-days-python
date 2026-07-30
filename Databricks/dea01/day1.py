
print("hello")
print('bye')
print("hello again")

# %sql
# SELECT "HELLO"

env =  "dev"

import os
import platform
def print_env_info():
    print(f"Python version: {platform.python_version()}")
    runtime_version  = os.environ,get("DATABRICKS_RUNTIME_VERSION", "Uknown")
    print(f"Databricks Runtime Version: {runtime_version}")


# %fs ls /databricks-datasets/

# %md
# ### Python skript

# %pip list

# %pip install Faker

# print_env_info()
# %sh ps

# %sql
# SELECT current_metastore();