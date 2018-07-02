{
    # ==========================================================================
    #   Xcode Project-Level Settings
    # ==========================================================================
    'configurations': {
        'Debug':   { 'xcode_config_file': '<(DIR_XCCONFIG)/project_debug.xcconfig' },
        'Release': { 'xcode_config_file': '<(DIR_XCCONFIG)/project_release.xcconfig' },
    }, # configurations

    # ==========================================================================
    #   Target Defaults
    # ==========================================================================
    'target_defaults': {
        'configurations': {
            'Debug':   { },
            'Release': { },
        }, # configurations
        'default_configuration': 'Release',
        'xcode_config_file': '<(DIR_XCCONFIG)/target_blank.xcconfig',
        'target_conditions': [
            ['OS=="mac" and (_type=="loadable_module" or _type=="shared_library" or _type=="static_library")', {
                'xcode_settings' :  {
                    'SKIP_INSTALL': 'YES',
                }, # xcode_settings
            } ], # OS=="mac" and (_type=="loadable_module" or _type=="shared_library" or _type=="static_library")
        ], # target_conditions
    }, # target_defaults
}
