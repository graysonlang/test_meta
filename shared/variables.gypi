{
    # ==========================================================================
    #   Variables
    # ==========================================================================
    'variables': {
        'CWD': '',
        'conditions': [
            ['OS=="mac"', { 'CWD': '<!(pwd)' } ],
            ['OS=="win"', { 'CWD': '<!(cd)' } ],
        ],

        # ......................................................................

        'DIR_ROOT':       '<(DEPTH)',
        'DIR_SHARED':     '<(DIR_ROOT)/shared',
        'DIR_SCRIPTS':    '<(DIR_SHARED)/scripts',
        'DIR_XCCONFIG':   '<(DIR_SHARED)/xcconfig',

        # ......................................................................

        'DEP_LIBPNG':     '<(DIR_SHARED)/libpng/libpng.gyp',
        'DEP_ZLIB':       '<(DIR_SHARED)/zlib/zlib.gyp',
    }, # variables
}
