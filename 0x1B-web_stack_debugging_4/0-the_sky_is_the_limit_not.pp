# fix our stack so that we get to 0
exec { 'fixing file':
  command => "sed -i 's/15/5000/g' /etc/default/nginx; service nginx restart",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  }