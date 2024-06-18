# Fixes typo in php file

exec { 'fix typo in php file':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
