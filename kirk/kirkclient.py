# -*- coding: utf-8 -*-

"""
This module contains the Client API for Qiniu Kirk Services
"""

import json
import requests

from .config import KIRK_HOST_PRO, KIRK_HOST_DEV
from .entity import LoginConfig, KirkUser, AuthToken

class KirkClient(object):

    """
    token 获取流程
    1. 使用七牛的(用户名+密码)，换取一个UserToken
    UserToken, 可以获取集群信息和集群下Project信息

    2. 使用UserToken，换取一个特定Project的ProjectToken，
    ProjectToken，可以列取Project下的App，Volume等等

    3. 使用ProjectToken，拉取某个特定Region下，特定Project的所有App
    """

    def __init__(self, username, password, mode = 'pro'):

        if mode == 'dev':
            self.host = KIRK_HOST_DEV 
        elif mode == 'pro':
            self.host = KIRK_HOST_PRO

        self.username = username
        self.password = password

        self.auth_token = None
        self.kirk_user = None 

        self.project_tokens = {}

    @property
    def usertoken(self):
        return self.auth_token.token

    def get_projecttoken(self, project_name):
        return self.project_tokens[project_name].token

    # --------- account/账户管理 ---------

    def get_usertoken(self):
        """获取用户token
        """

        payload = {
            'name':self.username,
            'password':self.password
            }
        r = requests.post("%s/v1/usertoken" % (self.host,), data=json.dumps(payload))

        if r.status_code == 200:
            res = r.json()

            _token = res['token']
            self.auth_token =  AuthToken(_token['id'], _token['issued_at'], _token['expires_at'])
            _user = res['user']
            self.kirk_user = KirkUser(_user['id'], _user['name'])

        elif r.status_code == 400:
            # （错误）请求中的参数存在错误
            pass
        elif r.status_code == 404:
            # 通用, （错误）不正确的访问路径，请参考开放 API 文档
            pass

    def get_project_token(self, project_name):
        """获取项目token 
        """

        headers = {"X-Auth-Token": self.auth_token.token}

        r = requests.get("%s/v1/projects/%s/token" % (self.host, project_name), headers=headers)
        uri = "%s/v1/projects/%s/token" % (self.host, project_name)

        if r.status_code == 200:
            res = r.json()

            _token = res['token']
            self.project_tokens[project_name] =  AuthToken(_token['id'], _token['issued_at'], _token['expires_at'])

            _user = res['user']

        elif r.status_code == 400:
            # （错误）请求中的参数存在错误
            pass
        elif r.status_code == 404:
            # 通用, （错误）不正确的访问路径，请参考开放 API 文档
            pass

    def get_regions(self):
        """列举所有region(可用区)
        """
        #TODO: 官方文档补充可用区列表
        # [{'id': 'RegionDefault', 'description': ''}, {'id': 'nb', 'description': '宁波内网'}, {'id': 'xq', 'description': '华东一区'}]
        # TODO: 大区进行细分 china-华东-1 china-nb-1
        headers = {"X-Auth-Token": self.auth_token.token}
        r = requests.get("%s/v1/regions" % (self.host,), headers=headers)
        return r.json()

    def get_users_projects(self, includeType=True):
        """获取用户的所有项目信息
        """
        headers = {"X-Auth-Token": self.auth_token.token}
        r = requests.get("%s/v1/users/%s/projects?includetype=%s" % (self.host, self.kirk_user.userid , includeType), headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            pass

    # --------- service/服务接口 ---------

    def list_regions_resource_specs(self, region_name):
        """获取集群可用容器资源规格 
        """
        headers = {"X-Auth-Token": self.auth_token.token}
        print("%s/regions/%s/v1/resourcespecs" % (self.host, region_name))
        r = requests.get("%s/regions/%s/v1/resourcespecs" % (self.host, region_name), headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            pass

    def post_service(self):
        """创建无状态服务
        """
        pass

    def post_app(self):
        """创建应用
        """
        pass

    def delete_app(self):
        """删除应用
        """
        pass

    def stop_service(self):
        """停止服务
        """
        pass

    def start_service(self):
        """启动服务
        """
        pass

    def scale_service(self):
        """伸缩服务
        """
        pass

    def upgrade_service(self):
        """升级服务
        """
        pass

    def rollback_service(self):
        """回滚当前服务到某个历史版本
        """
        pass


    # --------- storage/存储接口 ---------

    # --------- 配置接口/存储接口 ---------

    # --------- ALB/应用负载均衡接口 ---------
