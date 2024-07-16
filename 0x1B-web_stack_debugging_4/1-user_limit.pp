# Fixes "Too many files open" error for user Holberton

exec { 'fix holberton user hard limit':
  command => 'sed -i "s/^holberton hard nofile.*/holberton hard nofile 10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
}

exec { 'fix holberton user soft limit':
  command => 'sed -i "s/^holberton soft nofile.*/holberton soft nofile 10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
}
