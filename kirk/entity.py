# -*- coding: utf-8 -*-

# Account
class LoginConfig(object):
    def __init__(self, host, username, password):
        self.host = host                # API 服务器地址
        self.username = username        # 用户名
        self.password = password        # 密码

class KirkUser(object):
    def __init__(self, userid, username):
        self.userid = userid            # 用户id
        self.username = username        # 用户名

class AuthToken(object):
    def __init__(self, token, issued_at, expires_at):
        self.token = token              # 用户Token
        self.issued_at = issued_at      # 用户登陆时间
        self.expires_at = expires_at    # 用户失效时间

class Project(object):
    def __init__(self, projectid, name, description):
        self.projectid = projectid
        self.name = name
        self.description = description

# MicroService
class KirkApp(object):
    pass

class MicroService(object):
    def __init__(self):
        self.app_name = ''
        self.name = ''
        #self.gpu_spec = ''
        self.status = ''
        #self.pods = []
        self.type = ''
        self.microservice_ports = []
        self.containers = []

    def to_payload(self):
        pass

class MicroServicePort(object):
    def __init__(self):
        self.port = ''
        self.protocol = ''

class Container(object):
    def __init__(self):
        self.name = ''
        self.image = ''
        self.working_dir = ''
        self.command = []
        self.args = []
        self.container_volume_mounts = []
        self.container_configs = []
        self.container_envs = []

    def to_payload(self):
        pass

class GPUSpec(object):
    pass

class ContainerVolumeMount(object):
    pass

class ContainerConfig(object):
    pass

class ContainerEnv(object):
    pass

class MicroserviceRevision(object):
    pass