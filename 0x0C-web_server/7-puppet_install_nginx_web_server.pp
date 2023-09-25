# configuration Nginx using puppet
package { 'nginx':
  ensure => 'latest',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/error_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

exec { 'add_to_server':
  command => '/bin/sed -i "/listen 80 default_server/a \\
    location /redirect_me { \\
        return 301 https://github.com/5XGeorgeX5; \\
    } \\
    error_page 404 /error_404.html; \\
    location = /error_404.html{ \\
        root /var/www/html; \\
        internal; \\
    }" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}
