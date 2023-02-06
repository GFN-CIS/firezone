#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '0.1',
    'status': ['preview'],
    'supported_by': 'GFN-CIS'
}

DOCUMENTATION = """
---


"""

EXAMPLES = """
---
"""

RETURN = """
---
:

"""

import subprocess
import logging
import json
import string
import base64
from ansible.module_utils.basic import AnsibleModule


def main():
    ansible = AnsibleModule(
        argument_spec=dict(oidc=dict(type='dict',
                                     required=True), ),
        supports_check_mode=True)
    r = list()
    redirects = list()
    for key, value in ansible.params['oidc'].items():
        p = {"id": key.translate({ord(c): None for c in string.whitespace}).lower(),
             "client_id": value['client_id'], "client_secret": value['client_secret'],
             'discovery_document_uri': value.get(
                 'discovery_document_uri', 'https://accounts.google.com/.well-known/openid-configuration'),
             'redirect_uri': value.get('redirect_uri', None),
             'scope': value.get('scope', 'openid email profile'),
             'auto_create_users': value.get('auto_create_users', True),
             'label': value.get('label', key),
             'response_type': value.get('response_type', 'code'),
             }
        r.append(p)
        redirects.append("/auth/oidc/" + p['id'] + "/callback/")

    ansible_result = dict(
        changed=True,
        result={"config": base64.b64encode(json.dumps(r).encode('utf-8')), "redirects": redirects}
    )

    ansible.exit_json(**ansible_result)


if __name__ == '__main__':
    main()
