import boto3


"""
Get Github credentials from AWS parameter store
"""
class Credential(object):
    def get(self, user_key, password_key):
        ssm = boto3.client('ssm')
        resp = ssm.get_parameters(
            Names=[
                user_key,
                password_key
            ],
            WithDecryption=True
        )
        for invalid in resp.get('InvalidParameters'):
            raise KeyError("Invalid parameter: %s" % invalid)
        ret = dict(
            username=resp['Parameters'][0]['Value'],
            password=resp['Parameters'][1]['Value']
        )
        return ret
    
    def store(self):
        pass
    
    def erase(self):
        pass
