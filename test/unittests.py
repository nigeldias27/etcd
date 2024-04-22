import unittest
import requests
import etcd3
import json
etcd = etcd3.client(host = "Etcd-server",port = 2379)
class TestETCD(unittest.TestCase):

    def test_list(self):
        # Unit test for list keys
        key = "ListUnitTest"
        val = "One"  
        etcd.put(key,val)
        res = requests.get("http://backend:8000/listKeys")
        self.assertTrue(key in json.loads(res.content.decode('utf-8') ))   
        etcd.delete(key)   
    def test_put(self):
        # Unit test for PUT
        key = "PutUnitTest"
        val = "One"
        res = requests.post("http://backend:8000/putKeyVal",{key:key,val:val})
        if res.content == "Successfully Added":
            value,metadata = etcd.get(key)
            self.assertEqual(value.decode('utf-8'),val)
            etcd.delete(key)

    def test_get(self):
        # Unit test for GET
        key = "GetUnitTest"
        val = "One"
        etcd.put(key,val)
        res = requests.get("http://backend:8000/getVal?key="+key.replace(" ","+"))
        self.assertEqual(val,res.content.decode("utf-8").strip('"'))
        etcd.delete(key)

    def test_delete(self):
        # Unit test for DELETE
        key = "DeleteUnitTest"
        val = "One"
        etcd.put(key,val)
        res = requests.get("http://backend:8000/deleteVal?key="+key.replace(" ","+"))
        value,metadata = etcd.get(key)
        self.assertEqual(value,None)

if __name__ == '__main__':
    unittest.main()