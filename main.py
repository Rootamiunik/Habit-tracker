import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
#----------Constant-----------#
USERNAME = os.getenv('username')
TOKEN =  os.getenv('token')
GRAPH_ID =  os.getenv('id')
PIXELA_ENDPOINT = f'https://pixe.la/v1/users/{USERNAME}/graphs'
PIXELA_ENDPOINT_GRAPHS = f'{PIXELA_ENDPOINT}/{GRAPH_ID}'

#------------Header------------#
PIXELA_HEADER = {
    'X-USER-TOKEN': TOKEN,
}

#---------------time spent----------#
today_time = ''.join(str(dt.datetime.now().date()).split('-'))
pixela_parms = {
    'date':today_time,
    'quantity':input('Total time spend in the gym: ')
}

#---------------server request--------------#
server_requests = requests.post(url=PIXELA_ENDPOINT_GRAPHS, json=pixela_parms,headers=PIXELA_HEADER )
print(server_requests.json())
