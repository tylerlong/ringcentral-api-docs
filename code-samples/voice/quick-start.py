#!/usr/bin/env python
from ringcentral import SDK
import os,sys
from dotenv import load_dotenv
load_dotenv()

RECIPIENT = os.environ.get('RINGOUT_RECIPIENT')

rcsdk = SDK( os.environ.get('RC_CLIENT_ID'),
             os.environ.get('RC_CLIENT_SECRET'),
             os.environ.get('RC_SERVER_URL') )
platform = rcsdk.platform()
try:
  platform.login(os.environ.get('RC_USERNAME'),
                 os.environ.get('RC_EXTENSION'),
                 os.environ.get('RC_PASSWORD') )
except Exception as e:
  sys.exit("Unable to authenticate to platform: " + str(e))

resp = platform.post('/restapi/v1.0/account/~/extension/~/ring-out',
              {
                  'from' : { 'phoneNumber': os.environ.get('RC_USERNAME') },
                  'to'   : { 'phoneNumber': RECIPIENT },
                  'playPrompt' : False
              })
print(f'Call placed. Call status: {resp.json().status.callStatus}')
