import boto3


class Credential(object):
    def get(self, user_key, password_key):
        ssm = boto3.client('ssm')
        resp = ssm.get_parameters(
            Names=[
                user_key,
                password_key],
            WithDecryption=True)
        for invalid in resp['InvalidParameters']:
            raise KeyError("Invalid parameter: %s" % invalid)

        ret = dict()
        for param in resp['Parameters']:
            if param['Name'] == user_key:
                ret['username'] = param['Value']
            elif param['Name'] == password_key:
                ret['password'] = param['Value']

        return ret
