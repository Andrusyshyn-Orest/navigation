# Purpose  

The purpose of a project is to he;p user navigate through .json object.

## Example of usage  

(venv) D:\path\to\folder\with\navigation>python navigation.py  
Enter your bearer token: f  
Enter endpoint (press Enter for default value "1.1/friends/list.json"):  
Enter screenname (press Enter for default value "@BarackObama"):  
Enter count (press Enter for default value "2"):  
Do you want to see the whole object? [y/n]: y  
{'errors': [{'code': 89, 'message': 'Invalid or expired token.'}]}  
Do you want to check available fields? [y/n]: y  
['errors']  
Enter the name of the field or press Enter to finish: errors  
Do you want to see whole array? [y/n]: y  
[{'code': 89, 'message': 'Invalid or expired token.'}]  
Do you want to choose an object [y/n]: n  

## License
[MIT](https://choosealicense.com/licenses/mit/)
