# Lets practice using Puppet to make changes to our configuration file
exec { 'ssh_config':
    command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
    path    => '/bin',
}
