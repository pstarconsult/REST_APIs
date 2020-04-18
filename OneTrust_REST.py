import requests
import json
import pdb
from pprint import pprint

header = {
    'APIKey': '95de41bf1458991a6f1cdd70c4480990',
    'Content-Type': 'application/json'
}

# for syntax, see this page for format string: https://developer.onetrust.com/data-mapping. You will see this:
# [ Base URL: /api/inventory/v2 ] and then follow with the "endpoint" which is the snippets that follow. For
# example, the first Get method at the above webpage shows /inventories with poassible values of
# type type: ['processing-activities', 'vendors', 'assets', 'entities'].
# I tried the below on 3/27/20 and I get error code 401 which is auth error. I added 0.0.0.0/1 to CIDR settings
# in API key Advanced Settings here as required in Overview instructions: https://app.onetrust.com/app/#/pia/integrations/connections/manage?id=ad2d6f7c-976b-4491-8a49-8499cbb3a666&system=1d709ba3-32fd-4052-a1a5-1ac5b9c27e7e
# 3-27-20: decided to change to assessment automation since API is indicated as "interacts with assessment automation." I have a few
# of these assessments so this should return something. This did not work - got same error.
# next I removed the CIDR restriction above to see if that was blocking the connection. Same error.
# 3-30-20 tried different syntax as found in BigID format with GET as parameter. This worked!

#pdb.set_trace()

response = requests.request("GET" ,"https://app.onetrust.com/api/inventory/v2/inventories/assets", headers=header)
#response = requests.request("GET" ,"https://app.onetrust.com/api/inventory/v2/inventories/assets/dafb3cdf-2016-45d2-8073-267a440d1d3d", headers=header)
print(response.status_code)
print(header)
pprint(response.json())

response_dict = response.json()
pprint(response_dict)

# turns JSON, a dict in Python, into a string.
response_dict = json.dumps(response_dict)
print(response_dict)

# write JSON to a file.
with open('OT_assets.txt', 'w') as outfile:
    json.dump(response_dict, outfile)

# NOTE THAT THIS CALL IS NOT NECESSARY IN PRODUCION. read JSON from a file and return a dict.
with open('OT_assets.txt') as json_file:
    data = json.load(json_file)