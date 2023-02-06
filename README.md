Firezone
=========

The role to deploy [Firezone](https://firezone.dev) onto Ubuntu.

The conntrack-log container is used to get logs of clients communications.

Requirements
------------
When using OIDC with Google, the redirect url must be set to the following:

```https://SERVER_FQDN/auth/oidc/google/callback```
The redirect urls will be out in the debug log, or on the firezone configuration page after the install 

Role Variables
--------------

| Variable                  | Required | Default                   | Choices                                                                                                                      | Comments                                                                                   |
|---------------------------|----------|---------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| server_url                | yes      |                           | FQDN                                                                                                                         | The domain where FireZone site will be installed and endpoint adress to connect. FQDN only |
| google_oidc.client_id     | no       |                           | The Client ID for [Google OIDC](https://docs.firezone.dev/authenticate/google) if you want "Login with Google" functionality |
| google_oidc.client_secret | no       |                           | The Secret for Google OIDC if you want "Login with Google" functionality                                                     |
| firezone_redeploy         | no       | false                     | Whether to reinstall firezone even if config unchanged and no updates available                                              |
| vpn_subnet                | no       | 10.##.0.0/16              | The firezone internal subnet . The third octet is derived from server_url                                                    |
| admin                     | no       | fz-admin@{{ansible_host}} | The admin username                                                                                                           |
| wireguard_port            | no       | 51620                     | The wireguard port                                                                                                           |

Dependencies
------------
**geerlingguy.swap** : adds swap space to the system when running below 1GB RAM. So you can use cheap VPS.

Example Playbook
----------------

##### requirements.yml

    - src: https://github.com/GFN-CIS/firezone

##### ansible-playbook.yml

    - hosts: firezone_host
      roles:
        - role: firezone
          vars:
            server_url: "your_firezone_host.tld"
            fz_oidc:
                google:
                  client_id: "100283733733-iuefhoi2398iurdskfhjqoe3yr.apps.googleusercontent.com"
                  client_secret: "GOIRE-SIUE4KJREFFF4OIRFF"
            firezone_redeploy: false

After installation, you will find admin login/password in `/opt/firezone/.env` file. key DEFAULT_ADMIN_PASSWORD
Firezone heavily uses HTTP api, the api token is available in `/opt/firezone/api-token` file.

