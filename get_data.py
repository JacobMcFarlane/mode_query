# This is an adapted version of this Mode cookbook: https://mode.com/developer/api-cookbook/reports/get-query-results/ 
# with workarounds in place so it actually runs

import json
import requests
import os

from requests.auth import HTTPBasicAuth


host = 'https://modeanalytics.com'
ws = 'neurotrack1'
un = 'pub_key'
pw = 'private_key'
file_name = 'file_name.csv'


def get_query_result(report_token, query_token):
    url = '%s/api/%s/reports/%s/queries/%s/runs' % (host, ws, report_token, query_token)
    r = requests.get(url, auth=(un, pw))
    result = r.json()
    if result['_embedded']['query_runs'][0]['state'] == 'succeeded':
        query_run_result_endpoint = result['_embedded']['query_runs'][0]['_links']['result']['href']
        # Return statement was missing from cookbook??
        return get_run_result(query_run_result_endpoint) 
    else:
        print('There is no results, because query run failed.')


def get_run_result(query_run_result_endpoint):
    url = '%s%s/content' % (host, query_run_result_endpoint)
    print(url)
    r = requests.get(url, auth=HTTPBasicAuth(un, pw))
    # Cookbook was calling r.contents which was throwing errors, replaced with r.text
    return r.text

#report token is the string at the end of a report view URL
#query token is the string at the end of the URL at report view -> View Details -> SQL
text_results_from_query = get_query_result('report_token', 'query_token') 

# Writing output to a text file and then renaming to change it to a csv 
with open("Output.txt", "w") as text_file:
    text_file.write(text_results_from_query)


os.rename('Output.txt', file_name)