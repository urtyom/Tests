import requests
from yd_token import yd_toke


def new_folder(name):
  yd_t = yd_toke
  url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
  params_f = {'path': '/'+name}
  headers_f = {'Authorization': 'OAuth '+yd_t}
  put = requests.put(url_folder, headers=headers_f, params=params_f)
  return put.status_code
