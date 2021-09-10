import os
from re import M
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import math
from app import app
from models import setup_db, Servant, Master

MASTER_TOKEN = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhDZWEyMlBZaGxKZ2xXbmhjckRNdiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zYW1zbmotMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzMzY4NzlmNDNhNjIwMDZhOGQ3MzkwIiwiYXVkIjoiZmF0ZSIsImlhdCI6MTYzMTIxMjg4NiwiZXhwIjoxNjMxMjk5Mjg2LCJhenAiOiIzTWpjTnJ3ZDNkejN0emllVVZWRzlKRXNmVXdDMmxZciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0Om1hc3RlcnMiLCJnZXQ6c2VydmFudHMiXX0.PpmWmzP7hCt4FqzazS7ptXmzQESwn8u6qQADjaksw_fr391xvYq91WfSP27BS16IciZHk-R2YkFBSt89DuJcu1luX_-O7w73pjydrWa8CgNZC0h6AqFFZCgimM1OPmeGj8-nx2pt74FYKPwRCVp6lEHFrZ08x9nOtfyRnekPzVsZX_3H3YyfwandCWB2zBXpakUVnriI6sHpjaFMuZtK7J7UMwHODgUyimtDscz6ckpOjUW2G5eWEhX3lyvkLRqV3MwWjDPY9-mTxPyca_aSVm9TO1oxTMme65kmgLpVFeQMJ_qWhTXNkt-US7ilXuNGM9zu_3b9_p2NNSr7ZD4RAQ'
JUDGE_TOKEN = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhDZWEyMlBZaGxKZ2xXbmhjckRNdiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zYW1zbmotMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzMzY4NWE4ZmZiNzQwMDcxZDllYTYxIiwiYXVkIjoiZmF0ZSIsImlhdCI6MTYzMTIxMjk0MywiZXhwIjoxNjMxMjk5MzQzLCJhenAiOiIzTWpjTnJ3ZDNkejN0emllVVZWRzlKRXNmVXdDMmxZciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1hc3RlcnMiLCJkZWxldGU6c2VydmFudHMiLCJnZXQ6bWFzdGVycyIsImdldDpzZXJ2YW50cyIsInBhdGNoOnNlcnZhbnRzIiwicG9zdDptYXN0ZXJzIiwicG9zdDpzZXJ2YW50cyJdfQ.dug3H3xo6tchKNe-u13iB1QZEHegz-o3O3uloF3ZX4I88SaG6Q-fkCfbDq8mUd5E4hX0Glh20mJ3DL71mXG89oD7ZcRw2E-E--yB_jyffDAb72Kuiham_AIJrQiDp2_Hf0UHYKkdXd5xARIubeB9To-VpEu-gr0Suxxe70MdHOZQp3FZU_-__54iGAeUw5mG9lFxz2O0SX-O8e6FX1oxVKrwGQ0iYZ6lDsDpDP5WyfCAPBwPdVtC-d7Ue3--OPy13xqrYvIGrt2MS9ukjAi07Utd6-ASZEVYlnOJXX45XOIM5kQSxVi1q64Oq4WiBS0SQafqrscKRtdSYkvZkH4Prw'
FALSE_TOKEN = 'bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImhDZWEyMlBZaGxKZ2xXbmhjckRNdiJ9.eyJpc3MiOiJodHRwczovL2Rldi1zYW1zbmotMy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzMzY4NWE4ZmZiNzQwMDcxZDllYTYxIiwiYXVkIjoiZmF0ZSIsImlhdCI6MTYzMTIxMjk0MywiZXhwIjoxNjMxMjk5MzQzLCJhenAiOiIzTWpjTnJ3ZDNkejN0emllVVZWRzlKRXNmVXdDMmxZciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm1hc3RlcnMiLCJkZWxldGU6c2VydmFudHMiLCJnZXQ6bWFzdGVycyIsImdldDpzZXJ2YW50cyIsInBhdGNoOnNlcnZhbnRzIiwicG9zdDptYXN0ZXJzIiwicG9zdDpzZXJ2YW50cyJdfQ.dug3H3xo6tchKNe-u13iB1QZEHegz-o3O3uloF3ZX4I88SaG6Q-fkCfbDq8mUd5E4hX0Glh20mJ3DL71mXG89oD7ZcRw2E-E--yB_jyffDAb72Kuiham_AIJrQiDp2_Hf0UHYKkdXd5xARIubeB9To-VpEu-gr0SuMdHOZgfdgfdgdsfgsdfgQp3FZU_-__54iGAeUw5mG9lFxz2O0SX-O8e6FX1oxVKrwGQ0iYZ6lDsDpDP5WyfCAPBwPdVtC-d7Ue3--OPy13xqrYvIGrt2MS9ukjAi07Utd6-ASZEVYlnOJXX45XOIM5kQSxVi1q64Oq4WiBS0SQafqrscKRtdSYkvZkH4Prw'
class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')  
        self.DB_USER = os.getenv('DB_USER', 'postgres')  
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')  
        self.DB_NAME = os.getenv('DB_NAME', 'fate')  
        self.DB_PATH = 'postgresql://{}:{}@{}/{}'.format(self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME)
        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        pass

    def test_valid_get_index(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
    
    def test_valid_get_servants(self):
        res = self.client().get('/servants' , headers ={'Authorization':MASTER_TOKEN})
        servants = [servant.format() for servant in Servant.query.all()]
        data = json.loads(res.data)
        self.assertEqual(servants, data['servants'])
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def test_invalid_get_servants(self):
        res = self.client().get('/servants' , headers ={'Authorization':''})
        data = json.loads(res.data)
        print(f'DATA {data}')
        self.assertEqual(data['message']['description'], 'Authorization header must be a "Bearer" token.')
        self.assertEqual(res.status_code, 401)

    def test_valid_get_masters(self):
        res = self.client().get('/masters' , headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        masters = [master.format() for master in Master.query.all()]
        self.assertEqual(data['masters'], masters)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_invalid_get_masters(self):
        res = self.client().get('/masters' , headers ={'Authorization':FALSE_TOKEN})
        data = json.loads(res.data)
        print(f'DATA {data}')
        self.assertEqual(data['message']['description'], 'Unable to parse authentication token.')
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_valid_post_servant(self):
        body = {'name':'Achilles'}
        res = self.client().post('/servants', json=body, headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        self.assertIn(Servant.query.filter_by(name=body['name']).first(), Servant.query.all())
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)


    def test_invalid_post_servant(self):
        body = {'type':'saber'} #Must contain name attribute (key)
        res = self.client().post('/servants', json=body, headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])

    def test_valid_post_master(self):
        body = {'name':'Hatem'}
        res = self.client().post('/masters', json=body, headers ={'Authorization':JUDGE_TOKEN})
        self.assertIn(Master.query.filter_by(name=body['name']).first(), Master.query.all())
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def test_invalid_post_master(self): # No permission.
        body = {'name':'Yamin'} 
        res = self.client().post('/servants', json=body, headers ={'Authorization':MASTER_TOKEN}) 
        data = json.loads(res.data)
        self.assertEqual(data['message']['description'], 'permission not allowed or found.')
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code, 403)

    def test_valid_patch_servant(self):
        body = {'type':'test_saber'}
        servant = Servant.query.first()
        res = self.client().patch('/servants/{}'.format(servant.id), json=body, headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        print(f'DATA {data}')
        self.assertEqual(Servant.query.filter_by(id=servant.id).first().type, 'test_saber')
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code, 200)

    def test_invalid_patch_servant(self):
        body = {'type':'saber'} 
        id=10000
        res = self.client().patch('/servants/{}'.format(id), json=body, headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
    
    def test_valid_delete_servant(self):
        servant = Servant.query.first()
        #id=3
        res = self.client().delete('/servants/{}'.format(servant.id),  headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        self.assertIsNone(Servant.query.filter_by(id=servant.id).first())
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_invalid_delete_servant(self):
        id=10000
        res = self.client().delete('/servants/{}'.format(id),  headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_valid_delete_master(self):
        master =  Master.query.first()
        res = self.client().delete('/masters/{}'.format(master.id),  headers ={'Authorization':JUDGE_TOKEN})
        data = json.loads(res.data)
        self.assertNotIn(master, Master.query.all())
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_invalid_delete_master(self):
        id=0 # an ID that does not exist.
        res = self.client().delete('/masters/{}'.format(id),  headers ={'Authorization':MASTER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(data['message']['description'], 'permission not allowed or found.')
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code, 403)



if __name__ == "__main__":
    unittest.main()