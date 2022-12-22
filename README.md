Firezone
=========

The role to deploy [Firezone](https://firezone.dev) onto Ubuntu.

Requirements
------------
When using OIDC with Google, the redirect url must be set to the following:

```https://SERVER_FQDN/auth/oidc/google/callback/```

Role Variables
--------------

| Variable                  | Required | Default      | Choices                                                                                                                      | Comments                                                                                   |
|---------------------------|----------|--------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| use_letsencrypt           | no       | false        | true, false                                                                                                                  | Whether to use LetsEncrypt for SSL. It also sets auto-renew                                |
| server_url                | yes      | ansible_host | FQDN                                                                                                                         | The domain where FireZone site will be installed and endpoint adress to connect. FQDN only |
| google_oidc.client_id     | no       |              | The Client ID for [Google OIDC](https://docs.firezone.dev/authenticate/google) if you want "Login with Google" functionality |
| google_oidc.client_secret | no       |              | The Secret for Google OIDC if you want "Login with Google" functionality                                                     |
| firezone_redeploy         | no       | false        | Whether to reinstall firezone even if config unchanged and no updates available                                              |

Dependencies
------------
**geerlingguy.swap** : adds swap space to the system when running below 1GB RAM. So you can use cheap VPS.

Example Playbook
----------------

##### requirements.yml

    - src: https://github.com/GFNRussia/firezone

##### ansible-playbook.yml

    - hosts: firezone_host
      roles:
        - role: firezone
          vars:
            server_url: "your_firezone_host.tld"
            google_oidc:
              client_id: "100283733733-iuefhoi2398iurdskfhjqoe3yr.apps.googleusercontent.com"
              client_secret: "GOIRE-SIUE4KJREFFF4OIRFF"
            use_letsencrypt: true

After installation, you will find admin login/password in `/opt/firezone/firezone_admin_password`

Firezone installation logs are available in `/opt/firezone/firezone_install.log`