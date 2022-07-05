This is a very simple playbook to create virtual machines using cloud-init files. 
The expectation is, user would supply the cloud-init file as an input to the playbook.
Users may choose to use extra-vars or any other way to supply the input.(Eg. groupvars, hostvars etc)


#### Note:
1. The playbook is suppose to be executed from the host machine. Meaning, ansible controller and the VM host should be same.
2. Tthe playbook must be executed with ```-K``` flag unless passwordless sudo is available for current user.
3. All the default values are present in host_vars/localhost/defaults.yml. Feel free to modify them if you understand what it is.


#### Syntax:
```
ansible-playbook  automated_vm_creation.yml -e vm_name=<vm-name> \ 
 -e vcpus=<number-of-cpu> \
 -e memory_mb=<memory-in-mb> \
 -e os_variant=<os-variant> \
 -e disk_size=<disk-size-in-Gig>G \
 -e image_source=<image-download-url-or-local-path>
 -e cloud_init_file=[<cloud-init-file-path-optional>] -K
```

#### Example:

```
ansible-playbook  automated_vm_creation.yml   -e vm_name=test-vm -e vcpus=4 -e memory_mb=4096 -e os_variant=ubuntu22.04 -e disk_size=100G -e image_source=/home/ps/vm_images/jammy-server-cloudimg-amd64.img -K
```




