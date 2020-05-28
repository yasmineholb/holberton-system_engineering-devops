#Change the OS configuration so that it is possible to login with the holberton
exec { 'fixing':
  command  => "sudo /bin/sed -i 's/nofile 5000/g' /etc/security/limits.conf",
  provider => shell,
}
