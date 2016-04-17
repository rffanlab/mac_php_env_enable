#encoding:utf8
import os
def read_file(file_path):
    the_file = open(file_path,'r')
    whole_file = the_file.read()
    the_file.close()
    return whole_file

def write_file(file_path,data):
    the_file= open(file_path,'w')
    whole_file = the_file.write(data)
    the_file.close()
def add_file(file_path,data):
    the_file = open(file_path,'a')
    the_file.write(data)
    the_file.close()

auth_data = """<Directory />
    AllowOverride none
    Require all denied
</Directory>"""
new_auth_data = """<Directory />
    Options FollowSymLinks
    AllowOverride None
    Order deny,allow
    allow from all
</Directory>"""

php_data = "#LoadModule php5_module libexec/apache2/libphp5.so"
new_php_data = "LoadModule php5_module libexec/apache2/libphp5.so"
vhost_data = "#Include /private/etc/apache2/extra/httpd-vhosts.conf"
new_vhost_data = "Include /private/etc/apache2/extra/httpd-vhosts.conf"
file_path = os.path.join('/Users/rffanlab/workspace/bash','setupmamp.sh')
apache_config_file = "/etc/apache2/httpd.conf"
vhost_file = "/etc/apache2/extra/httpd-vhosts.conf"
host_file = "/etc/hosts"
def setup():
    the_whole_file = read_file(apache_config_file)
    new_file =  the_whole_file.replace(php_data,new_php_data).replace(vhost_data,new_vhost_data).replace(auth_data,new_auth_data)
    write_file(apache_config_file,new_file)
    write_file(vhost_file,"")

def add_vhost(domain,root_path):
    vhost_config_ori = """
<VirtualHost *:80>
    ServerAdmin admin@rffan.com
    DocumentRoot "/usr/docs/dummy-host.example.com"
    ServerName dummy-host.example.com
    ServerAlias www.dummy-host.example.com
    ErrorLog "/private/var/log/apache2/dummy-host.example.com-error_log"
    CustomLog "/private/var/log/apache2/dummy-host.example.com-access_log" common
</VirtualHost>"""
    new_vhost_config = vhost_config_ori.replace("/usr/docs/dummy-host.example.com",root_path).replace("dummy-host.example.com",domain)
    hosts_file = "\n127.0.0.1  "+domain+"\n127.0.0.1  www"+domain+"\n"
    print new_vhost_config
    add_file(vhost_file, new_vhost_config)
    add_file(host_file, hosts_file)
    os.system("chmod 7777 "+root_path)
    os.system("sudo apachectl restart")
def main():
    print "1.启用MAC的php环境"
    print "2.添加虚拟主机"
    choice = raw_input("请问你是选择启用PHP环境还是添加虚拟主机:")
    if choice == "1":
        print "你选择了启用MAC的PHP环境."
    elif choice =="2":
        print "你选择了添加虚拟主机"
        domain = raw_input("请输入要绑定的域名:")
        root_path = raw_input("请输入文件路径:")
        add_vhost(domain, root_path)



if __name__ == '__main__':
    main()
