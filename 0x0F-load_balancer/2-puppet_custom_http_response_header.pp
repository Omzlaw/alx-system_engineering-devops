class nginx {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/var/www/html':
    ensure  => 'directory',
    recurse => true,
  }

  file { '/var/www/html/index.html':
    ensure  => 'file',
    content => 'ALX School',
  }

  file { '/var/www/html/404.html':
    ensure  => 'file',
    content => 'Ceci n\'est pas une page',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $hostname;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}
",
    notify => Service['nginx'],
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }
}

include nginx
