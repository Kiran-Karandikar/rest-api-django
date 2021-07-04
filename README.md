# rest-api-django
Repo for Udemy course "Build Backend Rest Api with Django and Python"

----------------------------------------------------
## Table of contents
- [ ] Need to add Table of contents here

### Project Cheat Sheet
- [ ] Add Link to resource Page here

- [ ] Fix the vagrant.sh setup file to reflect the venv changes
----------------------------------------------------
* Environment Setup
```shell script
pip install --user pipenv
pipenv install -r requirements.txt
```

### System Dependencies

* [VirtualBox with Guest Additions](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* Vagrant plugin Install
    * `vagrant plugin install vagrant-librarian-chef-nochef`
    * `vagrant plugin uninstall vagrant-vbguest`
    * `vagrant plugin install vagrant-vbguest --plugin-version 0.21`
* Windows only: [Git](https://git-scm.com/download/win), for using `vagrant ssh` on Windows easily

> * Make Sure you change the git to run as administrator,
to do this go to git installation and right click on git.exe, bash.exe and under compatibility click on run as administrator
> * Do same for git-bash.exe and git-cmd.exe
### Usage

##### First Run

1. `vagrant up` _to start the VM and run initial provisioning_
3. `vagrant reload` _to restart following the updates installed during provisioning_

##### Subsequent Runs

* `vagrant up`
2. `vagrant ssh`

##### Destory VM
``vagrant destroy --force``

### Vagrant Issues
#### Public or private ssh key issue
* create ssh key using ``ssh-keygen`` inside of your host machine

#### Any PIP related issues 
 
```shell script
sudo apt-get remove --purge python-pip
sudo apt-get remove --purge python3-pip
sudo apt-get autoremove
mkdir ${project_name}
cd ${project_name}
curl  https://bootstrap.pypa.io/pip/3.5/get-pip.py -o get-pip.py
python3 get-pip.py
sudo pip3 install virtualenv
```
> !!! Crate Virtual Environment outside of  /vagrant/ shared folder...
If you go to the home folder of your vagrant user, you can create the virtualenv in there without this problem!
>
>
> Just the venv must be out of this /vagrant/ directory... after that you can go work as usually activating this venv and working with your sorce code in the usual /vagrat/ shared dir...
>
```shell script
cd ~
mkdir virutal_envs
virtualenv virutal_envs/project_name_venv  
```

