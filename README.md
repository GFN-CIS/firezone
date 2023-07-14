Firezone
=========

The role to deploy [Firezone](https://firezone.dev) onto Ubuntu.

The conntrack-log container is used to get logs of clients communications.

Requirements
------------

Controller node should have `netaddr` pip package installed.

For target node the only requirement is to have Docker installed.

When using OIDC with Google, the redirect url must be set to the following:

```https://SERVER_FQDN/auth/oidc/google/callback```
The redirect urls will be out in the debug log, or on the firezone configuration page after the install

Role Variables
--------------

| Variable                      | Required | Default              | Choices | Comments |
|-------------------------------|----------|----------------------|---------|----------|
| server_url | yes |  | URL | The URL where FireZone site will be accessible. |
| fz_oidcs.google.client_id | no |  | The Client ID for [Google OIDC](https://docs.firezone.dev/authenticate/google) if you want "Login with Google" functionality |
| fz_oidcs.google.client_secret | no | | The Secret for Google OIDC |
| firezone_redeploy | no | false | Whether to reinstall firezone even if config unchanged and no updates available |
| mgmt_subnet | no | 172.30.201.0/24 | The firezone internal subnet |
| client_subnet | no | 172.30.224.0/20 | The firezone client subnet |
| firezone_admin | no | fz-admin@localhost | The admin email |
| wireguard_port | no | 51620 | The wireguard port |
| firezone_dir | no | /opt/firezone | Location of firezone configuration and data |

Dependencies
------------
None.

Example Playbook
----------------

##### requirements.yml

    - src: https://github.com/GFN-CIS/firezone

##### ansible-playbook.yml

```yaml
- name: Prerequisites
  hosts: firezone_host
  tasks:
  - set_fact:
      mem_available: "{{ (ansible_facts.memory_mb.real.free + ansible_facts.memory_mb.swap.free | default(0)) }}"
  - include_role:
      name: geerlingguy.swap
    vars:
      swap_file_size_mb: '{{ ansible_facts.memory_mb.swap.free | default(0) + 1024 }}'
    when: mem_available|int < 768
  - include_role:
      name: geerlingguy.docker
    vars:
      docker_edition: 'ce'
      docker_install_compose: false
      docker_install_compose_plugin: false
- name: Install Firezone
  hosts: firezone_host
  roles:
  - firezone
  vars:
    server_url: http://your_firezone_host.tld
    fz_oidc:
      google:
        client_id: "100283733733-iuefhoi2398iurdskfhjqoe3yr.apps.googleusercontent.com"
        client_secret: "GOIRE-SIUE4KJREFFF4OIRFF"
```
After installation, you will find admin login/password in `/opt/firezone/.env` file. key DEFAULT_ADMIN_PASSWORD
Firezone heavily uses HTTP api, the api token is available in `/opt/firezone/api-token` file.

Testing
-------

There is a sample environment for testing the playbook in `testing` directory.
If you want to play with it, write `testing/host_vars/ubuntu` next values:
```yaml
ansible_host: 10.107.153.252
ansible_user: ubuntu
server_url: http://10.107.153.252
```

And just run `ansible-playbook -b play.yml`
