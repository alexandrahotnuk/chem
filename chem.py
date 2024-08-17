import pandas as pd
from chembl_webresource_client.new_client import new_client

available_resources = [resource for resource in dir(new_client) if not resource.startswith('_')]
print(available_resources)

target = new_client.target.search('coronavirus')
target_df = pd.DataFrame.from_dict(target)
print(target_df)

selected_target = target_df.target_chembl_id[6]

activity = new_client.activity.filter(target_chembl_id = selected_target).filter(standard_type = 'IC50')
activity_df = pd.DataFrame.from_dict(activity)
print(activity_df)


bioactivity_class = []
for i in activity_df.standard_value:
    if float(i) >= 10000:
        bioactivity_class.append('inactive')
    elif float(i) <= 1000:
        bioactivity_class.append('active')
    else:
        bioactivity_class.append('intermediate')

s = ['molecule_chembl_id', 'canonical_smiles', 'standard_value']
df = activity_df[s]
bioactivity_series = pd.Series(bioactivity_class, name = 'bioactivity_class')
final_df = pd.concat([df, bioactivity_series], axis = 1)
print(final_df)

final_df.to_csv('bioactivity.csv', index = False)
