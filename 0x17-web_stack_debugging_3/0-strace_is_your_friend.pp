# Fixes typo in php file

exec { 'fix_typo_in_php_file':
  command => '/bin/sed -i \'s/.phpp/.php/g\' /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],  # Include additional common paths
  unless  => '/bin/grep -q ".phpp" /var/www/html/wp-settings.php',
}
