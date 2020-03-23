#manifest that kills a process named killmenow
exec { 'killmenow':
  command => 'pkill /usr/bin/killmenow'
}
