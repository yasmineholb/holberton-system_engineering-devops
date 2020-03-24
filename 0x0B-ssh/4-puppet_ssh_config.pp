#make changes to our configuration file
exec { 'echo':
path    => '/bin/',
command => 'echo "IdentityFile ~/.ssh/holberton\n PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
