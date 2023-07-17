#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import os
import urllib.request
import pathlib
from urllib.request import urlopen
from os.path import basename

def expand_user(path):
    return str(pathlib.Path(path).expanduser())

def download_file(url, download_location):
    #file_name = os.path.basename(url)
    #file_path = os.path.join(expand_user(download_location), file_name)
    try:
        os.makedirs(expand_user(download_location), exist_ok=True)
        urllib.request.urlretrieve(url, file_path)
        return True, file_path
    except Exception as e:
        return False, str(e)

def run_module():
    module_args = dict(
        url=dict(type='str', required=True),
        download_location=dict(type='path', required=True),
    )
    module = AnsibleModule(argument_spec=module_args)
    url = module.params['url']
    download_location = module.params['download_location']
    response = urlopen(url)
    file_name = os.path.basename(url)
    file_path = os.path.join(expand_user(download_location),basename(response.url))

    if os.path.exists(file_path):
        module.exit_json(changed=True, file_path=file_path, stdout=file_path, msg=f'File({file_path}) already present in the system. Skipping download')
    else:    
        success, file_path = download_file(url, download_location)
        if success:
            module.exit_json(changed=True, file_path=file_path, stdout=file_path, msg=f'File({file_path}) downloaded successfully')
        else:
            module.fail_json(msg=f'Unable to download file: {file_path}')

def main():
    run_module()

if __name__ == '__main__':

    main()


