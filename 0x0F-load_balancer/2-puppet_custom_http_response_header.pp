# creating a custom HTTP header response with Puppet.
package { 'nginx':
  ensure => 'latest',
}

file { '/etc/nginx/sites-available/default':
  ensure => 'file',
}

exec { 'add_to_server':
  command => "/bin/sed -i \"/listen 80 default_server/a\\\\
        add_header X-Served-By ${hostname};\" /etc/nginx/sites-available/default",
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
