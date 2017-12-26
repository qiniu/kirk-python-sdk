# -*- coding: utf-8 -*-

import unittest
from kirk import KirkClient
from .test_helper import USERNAME, PASSWORD

class TestService(unittest.TestCase):
    
    def setUp(self):
        self.mode = 'dev'
        self.username = USERNAME
        self.password = PASSWORD

    def tearDown(self):
        pass

        "%s/v1/resourcespecs"


    # ------ 容器资源规格 ------

    def test_regions_resource_specs(self):
        """获取集群可用容器资源规格
        """
        client = KirkClient(self.username, self.password, self.mode)
        client.get_usertoken()

        region_name = 'cs1'
        res = client.list_regions_resource_specs(region_name)

        self.assertEqual("1U1G", res[0]['name'])
        self.assertEqual(1, res[0]['cpu'])
        self.assertEqual(1024, res[0]['memory'])
        #[{'name': '1U1G', 'cpu': 1, 'memory': 1024, 'desc': '简约型'}, {'name': '1U2G', 'cpu': 1, 'memory': 2048, 'desc': '通用型'}, {'name': '2U2G', 'cpu': 2, 'memory': 2048, 'desc': '通用型'}, {'name': '2U4G', 'cpu': 2, 'memory': 4096, 'desc': '通用型'}]