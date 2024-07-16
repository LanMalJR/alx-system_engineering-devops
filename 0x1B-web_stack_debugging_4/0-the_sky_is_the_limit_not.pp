# Fixes "Too many files open" error

exec { 'fix ulimit':
  command  => 'sed -i "s/^ULIMIT=\"-n.*/ULIMIT=\"-n $(ulimit -n)\"/" /etc/default/nginx && service nginx restart',
  provider => shell,
}
