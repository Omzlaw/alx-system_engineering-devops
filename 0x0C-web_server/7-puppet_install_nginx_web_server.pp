class { 'nginx':
  manage_repo => true,
  package_source => 'nginx-mainline',
}

package { 'curl': ensure => installed }

nginx::resource::server { 'default':
  listen_port => 80,
  location '/' {
    root => '/var/www/html',
  },
  location '/redirect_me' {
    return 301 'https://www.youtube.com/watch?v=QH2-TGUlwu4';
  },
}

file { '/var/www/html/index.html':
  ensure => present,
  content => 'Hello World!',
}

