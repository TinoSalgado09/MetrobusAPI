import requests
import json
import pandas as pd



def download():
    """Get all open data Metrobus CDMX System
    Args:
        Does not require parameters
    Returns:
        data (pd.DataFrame) : Open data dataframe of the CDMX Metrobus System
    """

    url = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=100000'  
    response_API = requests.get(url)
    print(response_API.status_code)
    data = response_API.text
    data = json.loads(data)
    data = data['result']['records']
    dataframe = pd.DataFrame(data)
    return dataframe