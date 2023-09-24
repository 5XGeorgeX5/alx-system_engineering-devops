# SSH configuration so that you can connect to a server without typing a password
file_line {'my_ssh_config':
  path => '/etc/ssh/ssh_config',
  line => 'Host 100.26.166.229
    HostName 100.26.166.229
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
