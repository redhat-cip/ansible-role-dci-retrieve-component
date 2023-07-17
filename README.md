# ansible-role-dci-retrieve-component

An Ansible role that retrieve DCI component.


## Pre-requisites

This role relies on [python-dciclient](https://github.com/redhat-cip/python-dciclient) and [dci-ansible](https://github.com/redhat-cip/dci-ansible).

If those are not installed, they should be installed before using this role.

## Role Variables

| Variable name | Required | Default | Type | Description |
|---------------|----------|---------|------|-------------|
| dci_retrieve_component_component_id | True | N/A | UUID | ID of the component to retrieve |
| dci_retrieve_component_component_name | False | N/A | String | Name of the component directory on disk |
| dci_retrieve_component_local_repo | True | N/A | Path | Path where to store the component locally |
| dci_retrieve_component_arch | False | x86_64 | String | Processor architecture to synchronize |


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
