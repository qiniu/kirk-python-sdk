# -*- coding: utf-8 -*-

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
    pass

class KirkApp(object):
    pass