# creating a custom HTTP header response with Puppet.
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

package { 'nginx':
  ensure => 'latest',
  require => Exec['update'],
}

file { '/etc/nginx/sites-available/default':
  ensure => 'file',
}

file_line { 'header':
  ensure  => file,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require => File_line['header'],
}
