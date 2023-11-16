# increase the user limit 

# increase the soft limit
exec { 'soft-limit':
  command => 'sed -i "/holberton soft/s/4/4000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase the hard limit 
exec { 'hard-limit':
  command => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
