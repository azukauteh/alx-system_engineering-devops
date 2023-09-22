# Create a file in /tmp

file { '/tmp/school':
  ensure  => present,
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}

