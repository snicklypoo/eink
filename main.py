import asana

# replace with your personal access token. 
personal_access_token = '0/07e9bf464e40c8b8cbbf3e55e7fc3073'

# Construct an Asana client
client = asana.Client.access_token(personal_access_token)
# Set things up to send the name of this script to us to show that you succeeded! This is optional.
client.options['client_name'] = "hello_world_python"

# Get your user info
me = client.users.me()

# Print out your information
print "Hello world! " + "My name is " + me['name'] + " and I my primary Asana workspace is " + me['workspaces'][0]['name'] + "."

workspaces = client.workspaces.find_all(item_limit=1)
print workspaces.next()
print workspaces.next() # raises StopIteration if there are no more items