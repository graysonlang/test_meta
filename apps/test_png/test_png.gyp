{
    # ==========================================================================
    #   Includes
    # ==========================================================================
    'includes': [ '../config.gypi' ],

    # ==========================================================================
    #   Targets
    # ==========================================================================
    'targets': [
        {
            'target_name': 'test_png',
            'type': 'executable',
            'dependencies': [
                '<(DEP_LIBPNG):libpng',
                '<(DEP_ZLIB):zlib',
            ], # dependencies
            'sources': [ 'main.cpp' ],
            'copies': [
                {
                    'destination': '<(PRODUCT_DIR)',
                    'files': [
                        'test.png',
                    ], # files
                },
            ], # copies
            'xcode_config_file': 'test_png.xcconfig',
        }, # test_png

        # ----------------------------------------------------------------------
    ], # targets
}
