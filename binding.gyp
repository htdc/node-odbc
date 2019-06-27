{
  'targets' : [
    {
      'target_name' : 'odbc_bindings',
      'sources' : [ 
        'src/odbc.cpp',
        'src/odbc_connection.cpp',
        'src/odbc_statement.cpp',
        'src/odbc_result.cpp',
        'src/dynodbc.cpp'
      ],
      'cflags' : ['-Wall', '-Wextra', '-Wno-unused-parameter'],
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'defines' : [
        'dynodbc'
      ],
      'conditions' : [
        [ 'OS == "linux"', {
          'libraries' : [ 
          ],
          'cflags' : [
            '-g'
          ]
        }],
        [ 'OS == "mac"', {
          'include_dirs': [
            '/usr/local/include'
          ],
          'libraries' : [
          ]
        }],
        [ 'OS=="win"', {
          'sources' : [
            'src/strptime.c',
            'src/odbc.cpp'
          ],
          'libraries' : [ 
          ]
        }],
        [ 'OS=="aix"', {
          'variables': {
            'os_name': '<!(uname -s)',
          },
          'conditions': [
             [ '"<(os_name)"=="OS400"', {
               'ldflags': [
                  '-Wl,-brtl,-bnoquiet,-blibpath:/QOpenSys/pkgs/lib,-lodbc'
                ]
             }]
          ]
        }]
      ]
    }
  ]
}
