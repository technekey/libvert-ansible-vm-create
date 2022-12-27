#!/usr/bin/python3


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_text

from urllib.request import urlopen  
from os.path import basename
import logging
import shutil
from pathlib import Path
import re
logger = logging.getLogger(__name__)


def main():
    module_args = dict(
        url=dict(type='str', required=True),
        download_location=dict(type='str', required=True),
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        msg = '',
        stdout = '',
        stdout_lines = [],
        stderr = '',
        stderr_lines = [],
        rc = 0,
        failed = False,
        changed=False
    )
    url =  module.params['url']
    download_location =  module.params['download_location']

    #if the url contains https* then assume the download location is remote
    if re.search('^http', url):
        try:
            response = urlopen(url,timeout=10)
            file_name = basename(response.url)
        except Exception as e:
            result['stderr'] = "Unable to determine the filename"
            module.fail_json(msg=f"Failed to inspect the supplied remote URL, {to_text(e)}")

        file_location = f"{download_location.rstrip('/')}/{file_name}"
        if Path(file_location).is_file():
            result['stdout'] = f"File is already present which is supposed to be downloaded from {url}, filename={file_name}"
            module.exit_json(**result)
        try:
            with urlopen(url) as response, open(file_location, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)    
        except Exception as e:
            result['stderr'] = f"Unable to download {file_name} from the {url}"
            module.fail_json(msg= f"{result['stderr']} {to_text(e)}")

        result['stdout'] = f"Download completed,filename={file_name}"
    else:
        if Path(url).is_file():
            result['stdout'] = f"File presence validation completed, filename={url}"
        else:
            result['stderr'] = f"Unable to find file at supplied local location, filename={url}"
            module.fail_json(msg = f"{result['stderr']}")
    #if all goes well this exit will be called
    module.exit_json(**result)

if __name__ == '__main__':
    main()
