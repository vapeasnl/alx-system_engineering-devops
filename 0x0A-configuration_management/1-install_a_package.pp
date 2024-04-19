# install flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}

# Install Werkzeug using pip3
package { 'Werkzeug':
  ensure => '2.1.1',
  provider => 'pip3',
}

