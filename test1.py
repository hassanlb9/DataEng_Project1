import unittest
from main import app



class site_test(unittest.TestCase):
   def test_home(self):
       tester=app.test_client(self)
       response = tester.get("/sent")
       statuscode=response.status_code
       self.assertEqual(statuscode,200)
       

     
if __name__ == "__main__":
    unittest.main()


