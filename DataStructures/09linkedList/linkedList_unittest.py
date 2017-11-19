import unittest
import linkedList

class TestAppend(unittest.TestCase):
    
    def setUp(self):
        self.mockList = linkedList.UnorderedList()
        print("SETUP PHASE: Created an empty list")
    
    def test_Append(self):
        print("TESTING: Append()")
        #self.assertEqual(print(self.mockList.at(0)),'[]')
        # Above does not work so created toString() in linkedList class same as __str__
        self.assertEqual(self.mockList.toString(),'[]')
        self.mockList.append(5)
        self.assertEqual(self.mockList.toString(),'[5]')
        self.mockList.append(6)
        self.assertEqual(self.mockList.toString(),'[5, 6]')
        
    def tearDown(self):
        self.mockList = None
        print("TEARDOWN PHASE: Deleting list")
         
if __name__ == "__main__":
    unittest.main()
    