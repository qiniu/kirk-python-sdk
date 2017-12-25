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