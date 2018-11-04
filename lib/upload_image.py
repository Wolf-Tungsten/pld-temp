# -*- coding: utf-8 -*-
from qiniu import Auth, put_file, etag, put_data
import qiniu.config
import cv2

access_key = 'u5_mJLM8gy6foLG3cWzVJoSquljCX5eSnd9Vc9v1'
secret_key = 'aayaBz9bk_326nZLGgfjTMLR9O9311fFwlILH0nA'
base_url = 'phkbfnd2y.bkt.clouddn.com/'
bucket_name = 'pld-temp'

def upload(image, name):
    q = Auth(access_key, secret_key)
    token = q.upload_token(bucket_name, name, 3600)
    cv2.imwrite(name, image)
    _, info = put_file(token, name, name)
    assert info.status_code == 200
    return info, base_url + name

if __name__ == '__main__':
    localfile = './one.png'
    image = cv2.imread(localfile)
    
    inf, imgurl = upload(image, 'testimg.png')
    print(imgurl)