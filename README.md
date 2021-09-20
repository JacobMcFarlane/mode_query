# mode_query
A fixed and updated version of this mode cookbook template: https://mode.com/developer/api-cookbook/reports/get-query-results/ that pulls down query results and saves them as a csv. To use, change pub_key and private_key in the script to public and private keys and file_name to your desired file name. 

``` 
un = 'pub_key'
pw = 'private_key'
file_name = 'file_name.csv'
```

I usually store keys in a json not pushed to a repo with the script. Instructions for generating the keys can be found in the mode cookbook template.
