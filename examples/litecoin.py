import helper

from kirk import KirkClient

import pdb

if __name__ == '__main__':

    username = 'pythonsdk@dev.com'
    password = 'aslanteam'
    mode = 'dev'

    client = KirkClient(username, password, mode)
    usertoken = client.get_usertoken()

    ps = client.get_users_projects()

    project_name = 'pythonsdk'
    project_token = client.get_project_token(project_name)

    regions = client.get_regions()
    print(regions)

    microservice = {
        "name": "block002",
        "type": "stateless",
        "resourceSpec": "1U1G",
        "instanceNumber": 1,
        "ports": [{
            "port": 8001,
            "protocol": "TCP"
        }, {
            "port": 8001,
            "protocol": "UDP"
        }],
        "containers": [{
            "name": "container002",
            "image": "reg-staging.qiniu.io/pythonsdk/blocksaasapi:v3", 
            "workingDir": "",
            "command": [],
            "args": [],
            "volumeMounts": [],
            "configs": [
            ],
            "envs": [
            ]
        }]
    }

    region_name = 'cs1'
    app_name = 'blocksaas'
    client.post_service(region_name, project_name, app_name, microservice)