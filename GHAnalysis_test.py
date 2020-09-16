import unittest
from GHAnalysis import Data
from GHAnalysis import Run

class Test( unittest.TestCase):
#D:\学习\软工实践\2020-personal-python
    def test_init(self):
        data = Data('D:\学习\软工实践\2020-personal-python',1)
        #若初始化成功 则为Ture      
        self.assertTrue(data)
   
    def test_getEventsUsers(self):
        data = Data()
        result = data.getEventsUsers('hl1123','PushEvent')
        #若成功 则返回0
        self.assertEqual(result,0)
    
    def test_getEventsRepos(self):
        data = Data()
        result = data.getEventsRepos('hl1123/6','PushEvent')
        #若成功 则返回0
        self.assertEqual(result,0)
    
    def test_getEventsUsersAndRepos(self):
        data = Data()
        result = data.getEventsUsersAndRepos('hl1123','hl1123/6','PushEvent')
        #若成功 则返回0
        self.assertEqual(result,0)       

if __name__ == '__main__':
    unittest.main()
