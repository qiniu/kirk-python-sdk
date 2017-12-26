# -*- coding: utf-8 -*-

import unittest
from kirk import KirkClient
from .test_helper import USERNAME, PASSWORD

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.mode = 'dev'
        self.username = USERNAME
        self.password = PASSWORD

    def tearDown(self):
        pass

    # ------ 获取用户token ------

    def test_user_token_valid(self):
        """
        有效用户登陆，获得token
        """
        client = KirkClient(self.username, self.password, self.mode)
        client.get_usertoken()
        self.assertIsNotNone(client.usertoken)

    def test_user_token_invalid(self):
        """
        无效登陆，返回404
        """
        username = 'invaliduser@wru.com'
        password = 'invalidpassword'
        client = KirkClient(username, password, self.mode)
        
        #AttributeError: 'NoneType' object has no attribute 'token'
        self.assertRaises(AttributeError, client.get_usertoken())

    # ------ 获取项目token ------

    def test_projects_token(self):
        client = KirkClient(self.username, self.password, self.mode)
        client.get_usertoken()

        projects = client.get_users_projects()
        project0 = projects[0]

        project_name = project0['name']

        client.get_project_token(project_name)
        self.assertIsNotNone(client.get_projecttoken(project_name))

    # ------  获取用户的所有项目信息 ------ 

    def test_users_projects(self):
        # TODO: 准备环境清理环境
        client = KirkClient(self.username, self.password, self.mode)
        client.get_usertoken()

        projects = client.get_users_projects()

        # [{'name': 'pythonsdk', 'description': ''}]

        self.assertEqual(1, len(projects))
        self.assertEqual('pythonsdk', projects[0]['name'])

    # ------ 列举所有region ------

    def test_regions(self):
        client = KirkClient(self.username, self.password, self.mode)
        client.get_usertoken()

        regions = client.get_regions()
        r0 = regions[0]
        self.assertEqual("cs1", r0['id'])

        r1 = regions[1]
        self.assertEqual("RegionDefault", r1['id'])
        # [{'id': 'cs1', 'description': '测试一区'}, {'id': 'RegionDefault', 'description': ''}]