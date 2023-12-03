# Installs Flask

class flask {
  package { 'python3-pip':
    ensure => 'latest',
  }

  exec { 'install_flask':
    command => '/usr/bin/pip3 install Flask',
    path    => ['/usr/bin'],
    require => Package['python3-pip'],
  }
}

class { 'flask':
  ensure => '2.1.0',
}
