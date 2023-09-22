# kills a process named killmenow.
exec {'kill_killmenow':
  command => '/bin/pkill -f killmenow',
}
