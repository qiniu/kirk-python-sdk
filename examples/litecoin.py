import helper

from kirk import KirkClient

import pdb

if __name__ == '__main__':

    username = 'pythonsdk@dev.com'
    password = 'aslanteam'
    mode = 'dev'

    client = KirkClient(username, password, mode)
    usertoken = client.get_user_token()

    ps = client.get_user_projects()
    pdb.set_trace()

    project_name = 'pythonsdk'
    client.get_project_token(project_name)