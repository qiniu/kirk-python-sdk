# -*- coding: utf-8 -*-

import collections
try:
  # Python 2.7+
  basestring
except NameError:
  # Python 3.3+
  basestring = str 

def todict(obj):
    """ 
    Recursively convert a Python object graph to sequences (lists)
    and mappings (dicts) of primitives (bool, int, float, string, ...)
    """
    if isinstance(obj, basestring):
        return obj 
    elif isinstance(obj, dict):
        return dict((key, todict(val)) for key, val in obj.items())
    elif isinstance(obj, collections.Iterable):
        return [todict(val) for val in obj]
    elif hasattr(obj, '__dict__'):
        return todict(vars(obj))
    elif hasattr(obj, '__slots__'):
        return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
    return obj

# --------- Account Entity ---------

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

# --------- LB Entity ---------

class TlbService(object):
    def __init__(self, appName, serviceName):
        self.appName = appName
        self.serviceName = serviceName

class TlbRule(object):
    def __init__(self, lbPort, servicePort, protocol):
        self.lbPort = lbPort
        self.servicePort = servicePort
        self.protocol = protocol

class CreateTlbArgs(object):
    def __init__(self, name, description, ipType, chargeMode, bandwidthLimit, policy, tlb_services, tlb_rules):
        self.name = name
        self.description = description
        self.ipType = ipType
        self.chargeMode = chargeMode
        self.bandwidthLimit = bandwidthLimit
        self.policy = policy
        self.services = tlb_services
        self.rules = tlb_rules

# --------- MicroService Entity ---------

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