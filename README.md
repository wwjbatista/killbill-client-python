# killbill
Kill Bill is an open-source billing and payments platform

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.19.15-SNAPSHOT
- Package version: 0.0.1-SNAPSHOT
- Build package: org.killbill.billing.codegen.languages.KillbillPythonGenerator

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import killbill 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import killbill
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
killbill.configuration.username = 'YOUR_USERNAME'
killbill.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = killbill.AccountApi()
account_id = 'account_id_example' # Str | 
body = killbill.BlockingState() # BlockingState | 
created_by = 'x_killbill_created_by_example' # Str | 
api_key = 'x_killbill_api_key_example' # Str | 
api_secret = 'x_killbill_api_secret_example' # Str | 
requested_date = '2013-10-20' # Date |  (optional)
plugin_property = ['plugin_property_example'] # List[Str] |  (optional)
reason = 'x_killbill_reason_example' # Str |  (optional)
comment = 'x_killbill_comment_example' # Str |  (optional)

try:
    # Block an account
    api_response = api_instance.add_account_blocking_state(account_id, body, created_by, api_key, api_secret, requested_date=requested_date, plugin_property=plugin_property, reason=reason, comment=comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->add_account_blocking_state: %s\n" % e)

```
