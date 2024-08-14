import pandas as pd
from chembl_webresource_client.new_client import new_client

available_resources = [resource for resource in dir(new_client) if not resource.startswith('_')]
print(available_resources)

brain_target = new_client.target.search('brain')
print(brain_target)