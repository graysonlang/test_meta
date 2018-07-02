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

        # ......................................................................

        'conditions': [
            ['OS=="win"', {
                'CharacterSet': 'Unicode',
                'msvs_configuration_platform': 'x64',
                'msvs_cygwin_shell': 0,
                'msvs_target_platform': 'x64',
                'win_delay_load_hook': 'false',

                'defines': [
                    '_HAS_EXCEPTIONS=1',
                    '_UNICODE',
                    'CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES=1',
                    'CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES_MEMORY=1',
                    'NOMINMAX',
                    'UNICODE',
                    'WIN32',
                    'WIN64',
                ], # defines

                'libraries': [
                    '-lkernel32.lib',
                    '-lshell32.lib',
                    '-luser32.lib',
                ], # libraries

                'msbuild_settings': {
                    'ClCompile': {
                        'DisableSpecificWarnings': [
                            4068, # unknown pragmas (https://msdn.microsoft.com/en-us/library/w099eeey.aspx)
                        ],
                        'AdditionalOptions': [
                            '/std:c++14',
                            '/bigobj', # increase number of sections in object files (https://msdn.microsoft.com/en-us/library/ms173499.aspx)
                        ],
                        'DebugInformationFormat': 'ProgramDatabase', # programDatabase (/Zi) (Note: a value of 4 (i.e. editAndContiue /ZI) is only supported when building for 32 bit x86)
                        'ExceptionHandling': 'SyncCThrow', # /EHs (https://msdn.microsoft.com/en-us/library/1deeycx5.aspx)
                        'MultiProcessorCompilation': 'true', # /MP
                    }, # ClCompile
                    'Link': {
                        'AdditionalOptions': [ '/ignore:4099' ],
                    }, # Link
                }, # msbuild_settings

                'configurations': {
                    'Debug': {
                        'defines': [
                            '_DEBUG',
                            '_ITERATOR_DEBUG_LEVEL=2', # Supersedes and combines _SECURE_SCL and _HAS_ITERATOR_DEBUGGING (https://msdn.microsoft.com/en-us/library/hh697468.aspx)
                            'DEBUG',
                        ], # defines
                        'msbuild_settings': {
                            'ClCompile': {
                                'Optimization': 'Disabled', # optimizeDisabled (/Od)
                                'RuntimeLibrary': 'MultiThreadedDebugDLL', # dynamic debug (/MDd)
                                'RuntimeTypeInfo': 'true', # /GR (https://msdn.microsoft.com/en-us/library/2kzt1wy3.aspx)
                            }, # ClCompile
                            'Link': {
                                # 'LinkIncremental': 'true', # /INCREMENTAL
                                'GenerateDebugInformation': 'true', # /DEBUG
                            }, # Link
                        } # msbuild_settings
                    }, # Debug
                    'Release': {
                        'defines': [
                            '_HAS_EXCEPTIONS=1',
                            '_ITERATOR_DEBUG_LEVEL=0', # Supersedes and combines _SECURE_SCL and _HAS_ITERATOR_DEBUGGING (https://msdn.microsoft.com/en-us/library/hh697468.aspx)
                            'NDEBUG',
                        ], # defines
                        'msbuild_settings': {
                            'ClCompile': {
                                'FavorSizeOrSpeed': 'Speed', # speed (/Ot)
                                'Optimization': 'MaxSpeed', # speed (/02)
                                'RuntimeLibrary': 'MultiThreadedDLL', # dynamic release (/MD)
                                'RuntimeTypeInfo': 'true', # /GR (https://msdn.microsoft.com/en-us/library/2kzt1wy3.aspx)
                                'BufferSecurityCheck': 'true', # /GS (https://msdn.microsoft.com/en-us/library/8dbf701c.aspx)
                            }, # ClCompile
                            'Link': {
                                'DataExecutionPrevention': 'true', # /NSCOMPAT (https://msdn.microsoft.com/en-us/library/ms235442.aspx)
                                'RandomizedBaseAddress': 'true', # /DYNAMICBASE (https://msdn.microsoft.com/en-us/library/bb384887.aspx)
                                'GenerateDebugInformation': 'false',
                            }, # Link
                        }, # msbuild_settings
                    }, # Release
                }, # configurations
            } ], # OS=="win"
        ], # conditions

        # ----------------------------------------------------------------------
    }, # target_defaults
}
