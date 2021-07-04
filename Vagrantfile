Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "django-profiles"
  config.vm.boot_timeout = 500

  config.vm.provider :virtualbox do |p|
        p.customize ["modifyvm", :id, "--memory", 2048]
        p.customize ["modifyvm", :id, "--cpus", 2]
        p.customize ["modifyvm", :id, "--cpuexecutioncap", 50]
  end

  if Vagrant.has_plugin? "vagrant-vbguest"
      config.vbguest.no_install  = true
      config.vbguest.auto_update = false
      config.vbguest.no_remote   = true
  end
  # To forward ports
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # For OSX/LINUX
  # config.vm.network "private_network", ip: "10.10.10.10"

  # For WINDOWS (comment the OSX/LINUX and uncomment this line)
  # For WINDOWS, you can access it using http://127.0.0.1:8080/
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"

  config.vm.synced_folder ".", "/home/vagrant/site"
  config.vm.provision "shell", path: "vagrant_setup.sh"
end
