# ansible-role-dci-retrieve-component

An Ansible role that retrieve DCI component.


## Pre-requisites

This role relies on [python-dciclient](https://github.com/redhat-cip/python-dciclient) and [dci-ansible](https://github.com/redhat-cip/dci-ansible).

If those are not installed, they should be installed before using this role.

Also `yum-utils` should be installed.


## Role Variables

| Variable name | Required | Default | Type | Description |
|---------------|----------|---------|------|-------------|
| dci_retrieve_component_component_id | True | N/A | UUID | ID of the component to retrieve |
| dci_retrieve_component_component_name | False | N/A | String | Name of the component directory on disk |
| dci_retrieve_component_local_repo | True | N/A | Path | Path where to store the component locally |
| dci_retrieve_component_repo_url | False | https://repo.distributed-ci.io | URL | URL where the components are stored |
| dci_retrieve_component_sslclientcert | False | /etc/ssl/repo/dci.crt | Path | Path to the DCI client certificate |
| dci_retrieve_component_sslclientkey | False | /etc/ssl/repo/dci.key | Path | Path to the DCI client key |
| dci_retrieve_component_sslverify | False | yes | Bool | Wether to verify the certificate of dci_retrieve_component_repo_url |
| dci_retrieve_component_arch | False | x86_64 | String | Processor architecture to synchronize via reposync |


### Example

```
- hosts: localhost
  vars:
    dci_retrieve_component_component_id: XXX
    dci_retrieve_component_component_name: XXX # Optional, if not present take the topic name
    dci_retrieve_component_local_repo: /var/www/html
  roles:
    - dci-retrieve-component
```

To download an alternative architecture than the current one.

```
- hosts: localhost
  tasks:
    - name: Retrieve component
      vars:
        dci_retrieve_component_component_id: XXX
        dci_retrieve_component_local_repo: /var/www/html
        dci_retrieve_component_arch: ppc64le
      include_role:
        name: dci-retrieve-component
```

### License

Apache 2.0


### Author Information

Distributed-CI Team  <distributed-ci@redhat.com>
