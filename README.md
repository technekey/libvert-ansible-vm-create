This is a very simple playbook to create virtual machines using ansible, libvert and cloud-init. The playbook would not only create the VM, but also do initial repeated steps a user would wish to automate, like `apt update`, `apt install` or running some commands after the VM is booted. This playbook provide an administrator ability to quickly spawn Virtual machines, with some a ready to use expereince. 

### For more details, see this. I would love to further enhance this playbook or provide any assitance. Feel free to contact via https://technekey.com/an-amazingly-fast-way-to-create-virtual-machines/

#### Note:
1. The playbook is suppose to be executed from the host machine. Meaning, ansible controller. 
2. The playbook must be executed with ```-K``` flag unless passwordless sudo is available for current user.
3. All the default values are present in host_vars/localhost/defaults.yml. #### This file is the supposed to be modified for any customization. (Eg, cpu, memory of VM)
4. The playbbok is tested only with default libvert network.
5. You must upadate your public key in  host_vars/localhost/defaults.yml to enable SSH access to the node. 


#### Syntax:
```
# to create a VM called demo-vm:
ansible-playbook  vm_manage.yml -e vm_name='demo-vm' -e playbook_action=create -K

# to delete a VM called demo-vm:
ansible-playbook  vm_manage.yml -e vm_name='demo-vm' -e playbook_action=delete -K
```

#### Steps: 
####step-1: As the start of the demo, there is no VM present. 

```bash
virsh list
 Id   Name      State
-------------------------
```
#### step-2: Run the playbook with ```playbook_action=create``` and ```vm_name=demo-vm``` to create the vm called ```demo-vm```.

```
ansible-playbook  vm_manage.yml -e vm_name='demo-vm' -e playbook_action=create
```


#### Example output:

```
ansible-playbook  vm_manage.yml -e vm_name='demo-vm' -e playbook_action=create
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Deploy VM using Cloud-init] *********************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:36 2022]
ok: [localhost]

TASK [Starting validation of mandatory variables and dependencies] ************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:37 2022]

TASK [input_validation_and_dependency_installation : Display warnings] ********************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:37 2022]
[WARNING]: Consider checking the host_vars/localhost/defaults.yml file to customize the VM size and login options
ok: [localhost] => {}

TASK [input_validation_and_dependency_installation : Validate the minimum required hostvars configuration] ********************************************************
                                                                                                                                         [Tue Dec 27 15:40:37 2022]
skipping: [localhost] => (item=vm_name)
skipping: [localhost] => (item=download_location)
skipping: [localhost] => (item=vm_disk_location)
skipping: [localhost] => (item=allow_ssh_pass)
skipping: [localhost] => (item=default_username)
skipping: [localhost] => (item=default_password)
skipping: [localhost] => (item=memory_mb)
skipping: [localhost] => (item=vcpus)
skipping: [localhost] => (item=disk_size)
skipping: [localhost] => (item=image_source)
skipping: [localhost] => (item=os_variant)
skipping: [localhost] => (item=ssh_key)
skipping: [localhost] => (item=required_directories)

TASK [input_validation_and_dependency_installation : Create the required directory] *******************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:37 2022]
ok: [localhost] => (item=/home/technekey/vm_images)
ok: [localhost] => (item=/home/technekey/vm_disks)
changed: [localhost] => (item=/home/technekey/vm_disks/demo-vm)

TASK [input_validation_and_dependency_installation : Install the dependencies on the host] ************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:37 2022]
ok: [localhost] => (item=python3-libvirt)
ok: [localhost] => (item=libvirt-clients)
ok: [localhost] => (item=virtinst)
ok: [localhost] => (item=guestfs-tools)
ok: [localhost] => (item=qemu-utils)
ok: [localhost] => (item=qemu-kvm)
ok: [localhost] => (item=cloud-image-utils)

TASK [input_validation_and_dependency_installation : Loading the path of all required binaries in the ansible host] ***********************************************
                                                                                                                                         [Tue Dec 27 15:40:42 2022]
changed: [localhost] => (item=virt-install)
changed: [localhost] => (item=virsh)
changed: [localhost] => (item=virt-ls)
changed: [localhost] => (item=virt-cat)
changed: [localhost] => (item=qemu-img)
changed: [localhost] => (item=cloud-localds)

TASK [input_validation_and_dependency_installation : List the Existing KVM present on the host machine] ***********************************************************
                                                                                                                                         [Tue Dec 27 15:40:42 2022]
ok: [localhost]

TASK [input_validation_and_dependency_installation : Check if the user requested VM is already present in the Host] ***********************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]
ok: [localhost]

TASK [input_validation_and_dependency_installation : Display the presence of the vm(demo-vm)in the Host] **********************************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]
ok: [localhost] => {}

MSG:

"   demo-vm is not present in the host. Continuing the VM creation.
 "


TASK [input_validation_and_dependency_installation : meta] ********************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]
skipping: [localhost]

TASK [input_validation_and_dependency_installation : Determine the valid list of OS-Variants] *********************************************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]
changed: [localhost]

TASK [input_validation_and_dependency_installation : assert the os-variant] ***************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]
ok: [localhost] => {
    "changed": false
}

MSG:

OS Variant assertion passed

TASK [Create a VM] ************************************************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]

TASK [Download Image and resize the image] ************************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]

TASK [image-download : Download the image from remote location] ***************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:43 2022]
ok: [localhost]

TASK [image-download : Set Image file name] ***********************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:44 2022]
ok: [localhost]

TASK [image-download : Get the format of the downloaded image] ****************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:44 2022]
changed: [localhost]

TASK [image-download : Get the format of the downloaded image] ****************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:44 2022]
ok: [localhost]

TASK [image-download : Set the qcow2 file name] *******************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:44 2022]
ok: [localhost]

TASK [image-download : Convert the image to qcow2] ****************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:44 2022]
changed: [localhost]

TASK [image-download : Resize the disk /home/technekey/vm_images/jammy-server-cloudimg-amd64.img] ************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:46 2022]
changed: [localhost]

TASK [Starting cloud-config image buildup] ************************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:47 2022]

TASK [cloud-config-creation : Create a temp cloud-init file] ******************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:47 2022]
changed: [localhost]

TASK [cloud-config-creation : Create a template to add the VM-NAME(demo-vm) to the temp cloud-init file] **********************************************************
                                                                                                                                         [Tue Dec 27 15:40:47 2022]
changed: [localhost]

TASK [cloud-config-creation : Set cloud-config file name] *********************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:47 2022]
ok: [localhost]

TASK [cloud-config-creation : Create a seed image] ****************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:47 2022]
changed: [localhost]

TASK [cloud-config-creation : Cleanup the Default cloud-init file] ************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:47 2022]
changed: [localhost]

TASK [Starting the virt-install] **********************************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:47 2022]

TASK [virt-install : Do the install for Default network] **********************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:48 2022]
changed: [localhost]

TASK [Check for cloud-init completion for demo-vm] ****************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:49 2022]

TASK [cloud_init_check : Check the VM status] *********************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:49 2022]
changed: [localhost]

TASK [cloud_init_check : Wait for cloud-init result file to get created] ******************************************************************************************
                                                                                                                                         [Tue Dec 27 15:40:50 2022]
FAILED - RETRYING: [localhost]: Wait for cloud-init result file to get created (90 retries left).
FAILED - RETRYING: [localhost]: Wait for cloud-init result file to get created (89 retries left).
FAILED - RETRYING: [localhost]: Wait for cloud-init result file to get created (88 retries left).
FAILED - RETRYING: [localhost]: Wait for cloud-init result file to get created (87 retries left).
FAILED - RETRYING: [localhost]: Wait for cloud-init result file to get created (86 retries left).
FAILED - RETRYING: [localhost]: Wait for cloud-init result file to get created (85 retries left).
changed: [localhost]

TASK [cloud_init_check : Waiting for Cloud init to complete] ******************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:05 2022]
changed: [localhost]

TASK [cloud_init_check : Validate the cloud-init execution results] ***********************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:07 2022]
ok: [localhost] => {
    "changed": false
}

MSG:

Cloud-init exeution passed

TASK [cloud_init_check : Capture the Current Status of the VM] ****************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:08 2022]
ok: [localhost]

TASK [cloud_init_check : Grab the IP address of the VM Created] ***************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:08 2022]
changed: [localhost]

TASK [cloud_init_check : Assert that IP address is available for the vm(demo-vm)] *********************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:08 2022]
ok: [localhost] => {
    "changed": false
}

MSG:

IP Address is available for the VM=demo-vm

TASK [cloud_init_check : Remove the old host entry] ***************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:08 2022]
ok: [localhost]

TASK [cloud_init_check : Add IP address of all hosts to all hosts] ************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:08 2022]
changed: [localhost]

TASK [cloud_init_check : Remove the old host entry] ***************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:08 2022]
changed: [localhost]

TASK [cloud_init_check : Add IP address of all hosts to all hosts] ************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:08 2022]
changed: [localhost]

TASK [cloud_init_check : Show VM info] ****************************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:09 2022]
ok: [localhost] => {}

MSG:

[{'state': 'running', 'maxMem': '2097152', 'memory': '2097152', 'nrVirtCpu': 2, 'cpuTime': '31340000000', 'autostart': 0}, '192.168.122.20']

TASK [Delete the VM (demo-vm)] ************************************************************************************************************************************
                                                                                                                                         [Tue Dec 27 15:42:09 2022]
skipping: [localhost]

PLAY RECAP ********************************************************************************************************************************************************
localhost                  : ok=35   changed=18   unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

[localhost]
15:40:36 Gathering Facts                                                                                Passed       1.06s
15:40:37 Starting validation of mandatory variables and dependencies                                    Passed       0.00s
15:40:37 input_validation_and_dependency_installation : Display warnings                                Passed       0.02s
15:40:37 input_validation_and_dependency_installation : Validate the minimum re...                     Skipped       0.04s
15:40:37 input_validation_and_dependency_installation : Create the required dir...                      Passed       0.43s
15:40:37 input_validation_and_dependency_installation : Install the dependencie...                      Passed       4.20s
15:40:42 input_validation_and_dependency_installation : Loading the path of all...                      Passed       0.82s
15:40:42 input_validation_and_dependency_installation : List the Existing KVM p...                      Passed       0.20s
15:40:43 input_validation_and_dependency_installation : Check if the user reque...                      Passed       0.01s
15:40:43 input_validation_and_dependency_installation : Display the presence of...                      Passed       0.01s
15:40:43 input_validation_and_dependency_installation : meta                                           Skipped       0.02s
15:40:43 input_validation_and_dependency_installation : Determine the valid lis...                      Passed       0.54s
15:40:43 input_validation_and_dependency_installation : assert the os-variant                           Passed       0.01s
15:40:43 Create a VM                                                                                    Passed       0.01s
15:40:43 Download Image and resize the image                                                            Passed       0.00s
15:40:43 image-download : Download the image from remote location                                       Passed       0.60s
15:40:44 image-download : Set Image file name                                                           Passed       0.01s
15:40:44 image-download : Get the format of the downloaded image                                        Passed       0.13s
15:40:44 image-download : Get the format of the downloaded image                                        Passed       0.01s
15:40:44 image-download : Set the qcow2 file name                                                       Passed       0.01s
15:40:44 image-download : Convert the image to qcow2                                                    Passed       1.57s
15:40:46 image-download : Resize the disk /home/technekey/vm_images/jammy-server-cloud...               Passed       0.71s
15:40:47 Starting cloud-config image buildup                                                            Passed       0.00s
15:40:47 cloud-config-creation : Create a temp cloud-init file                                          Passed       0.20s
15:40:47 cloud-config-creation : Create a template to add the VM-NAME(demo-vm) ...                      Passed       0.43s
15:40:47 cloud-config-creation : Set cloud-config file name                                             Passed       0.01s
15:40:47 cloud-config-creation : Create a seed image                                                    Passed       0.13s
15:40:47 cloud-config-creation : Cleanup the Default cloud-init file                                    Passed       0.13s
15:40:47 Starting the virt-install                                                                      Passed       0.00s
15:40:48 virt-install : Do the install for Default network                                              Passed       1.85s
15:40:49 Check for cloud-init completion for demo-vm                                                    Passed       0.01s
15:40:49 cloud_init_check : Check the VM status                                                         Passed       0.17s
15:40:50 cloud_init_check : Wait for cloud-init result file to get created                              Passed      75.28s
15:42:05 cloud_init_check : Waiting for Cloud init to complete                                          Passed       2.56s
15:42:07 cloud_init_check : Validate the cloud-init execution results                                   Passed       0.05s
15:42:08 cloud_init_check : Capture the Current Status of the VM                                        Passed       0.15s
15:42:08 cloud_init_check : Grab the IP address of the VM Created                                       Passed       0.16s
15:42:08 cloud_init_check : Assert that IP address is available for the vm(demo...                      Passed       0.01s
15:42:08 cloud_init_check : Remove the old host entry                                                   Passed       0.21s
15:42:08 cloud_init_check : Add IP address of all hosts to all hosts                                    Passed       0.12s
15:42:08 cloud_init_check : Remove the old host entry                                                   Passed       0.12s
15:42:08 cloud_init_check : Add IP address of all hosts to all hosts                                    Passed       0.13s
15:42:09 cloud_init_check : Show VM info                                                                Passed       0.01s
15:42:09 Delete the VM (demo-vm)                                                                       Skipped       0.01s
Total Playbook execution time: 92.82563495635986 sec
```

Now, a VM is created with a name ```demo-vm```:

```
virsh list
 Id   Name      State
-------------------------
 31   demo-vm   running
```

#### Cleanup/Deleting the VM:

```
ansible-playbook  vm_manage.yml -e vm_name='demo-vm' -e playbook_action=delete
```

#### General Note:
Its highly recommanded to check the host_vars defaults to have a better understanding of the playbook internals. There are many customization possible using the ```host_vars/localhost/defaults.yml``` file. 

#### Some customizations advantage:

If you want to do ```apt-update``` and install list of packages after the VM creation you can mention them as list in this file under ```package_list```. 
Similarly if you wish to run some commands, after the VM is up, you can mention them under ```run_command``` or ```boot_command```.  

```yaml
#######################################################
# This file contains, some of the default values
# user should change as per their need
#######################################################

######################################################################################
# The default action of the playbook is to create the VM, if you want to delete vm
# set this playbook_action=delete via extra var
######################################################################################
playbook_action: create

######################################################################################
# STRING: location at which ISO will be downloaded if URL is provided as image_source
#######################################################################################
download_location: ~/vm_images

#######################################################################################
# STRING: location at which VM Virtual disk will be kept, location should have enough
# space and any loss to the files in this dir, will cause VM corruption.
########################################################################################
vm_disk_location: ~/vm_disks


########################################################################################
# STRING: default user and pass for the VM
########################################################################################
allow_ssh_pass: True  # If this is set to false, VM will not be accessible via user/pass
default_username: technekey
default_password: technekey

########################################################################################
# default sizing of VM, either change here or using extra-vars
# INT: vcpus and memory_mb
# STRING: disk_size, Must use suffix of unit. Eg: 120G
########################################################################################

memory_mb: 2048
vcpus: 2
disk_size: 40G


########################################################################################
# STRING: Image location, could be a URL(https://.......) or a local path(/foo/bar/.....)
########################################################################################
image_source: "https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img"

#########################################################################################
# STRING: value can be obtained by  'virt-install --osinfo list'
#
#########################################################################################
os_variant: ubuntufocal


###########################################################################################
# STRING: SSH public key to login to the VM
###########################################################################################
ssh_key: "FILL THIS WITH A VALID PUBLIC KEY"

###########################################################################################
# LIST: Tools you would want to install automatically after VM creation
###########################################################################################

package_list:
- vim
- build-essential
- python3-pip


##############################################################################################
# List: Boot commands, the commands to be executed just after boot before anything else
#
##############################################################################################
boot_commands:
- date
- touch /tmp/start

##############################################################################################
# LIST: Run commands, the commands to be executed just before the cloud-init finishes
#
##############################################################################################
run_commands:
- date
- touch /tmp/end
```
