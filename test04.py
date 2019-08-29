import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import asana
import json
from six import print_

client = asana.Client.access_token('0/07e9bf464e40c8b8cbbf3e55e7fc3073')
me = client.users.me()
#print_("me=" + json.dumps(me, indent=2))
##projects = client.projects.find_all({'workspace': workspace['id']})
##print_(json.dumps(projects, indent=4))
print "Hello " + me['name']

workspace_id = me['workspaces'][0]['id']
#project = client.projects.create_in_workspace(workspace_id, { 'name': 'blabi' })
#print "Created project with id: " + str(project['id'])

#for task in client.projects.user_task_list.find_all():
#  print task
taskList = {}
projList = {}
i = 0
projects = client.projects.find_all({'workspace': workspace_id})
for project in projects:   
        item = ""
        tasks = client.tasks.find_by_project(project['id'], {"opt_fields":"name, projects, workspace, id, due_on, created_at, modified_at, completed, completed_at, assignee, assignee_status, parent, notes"})
        for task in tasks:
            if task['assignee'] != None:
                if task['assignee']['gid'] == '1135189468361652':
                   item = task['name']
                if (len(item) > 55):
                    item = item[0:55] + '...'
                taskList.update({ item : task['due_on']})
                projList.update({ item : project['name']})
for item in taskList:
    print item
    print taskList[item]
    print projList[item]
print taskList



#for task in tasks: 
    #print_(json.dumps(task, indent=4))
    #if task['assignee'['']]0['id'] == 1135189468361652:
    #if task['assignee'][0] != 'None':
        #print task['name']
    #if task['assignee'] != None:
        #if task['assignee']['gid'] == '1135189468361652':
            #print(task['name'])
            #print(task['due_on'])
            #print('completed:' + str(task['completed']))
    