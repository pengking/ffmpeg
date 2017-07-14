# Author:pengchun
# Data:2017/7/3
# 说明：
# common.gypi中定义了一些公用的信息包括：
# 设置一些变量以及定义在某个环境下才能使用条件

{

   # 创建工程默认选项
	'target_defaults': {

    #创建编译条件如果操作系统是Windows则定义设置一些Windows下才能执行的条件
    'conditions': [

      #编译环境如果是Windows系统
      ['OS == "win"', {

        # 定义在Debug和Release中的公用信息
        'defines': [

          '_CRT_SECURE_NO_WARNINGS',
          '_CRT_NONSTDC_NO_WARNINGS',
          '_SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS',
          
          'WIN32',

        ],
        # END DEFINES

        # 定义链接库，这个可能要根据不同编译器而定
        'link_settings': {
          'libraries': [
            'kernel32.lib',
            'user32.lib',
            'gdi32.lib',
            'winspool.lib',
            'comdlg32.lib',
            'advapi32.lib',
            'shell32.lib',
            'ole32.lib',
            'oleaut32.lib',
            'uuid.lib',
            'odbc32.lib',
            'odbccp32.lib',

            # comctl32 miss will result 
            # error LNK2019 unresolved external symbol __imp__InitCommonControls
            # ref http //bbs.csdn.net/topics/280070106

            'comctl32.lib',
            #'Riched20.lib',
            ],
          },

        # 配置编译环境
    
        'configurations': {

          # Debug情况下配置VS相关信息
          'Debug': {

            'msvs_settings': {
              'VCCLCompilerTool': {
                # 多线程调试 DLL (/MD)
                'RuntimeLibrary': '3',
                # 不优化 /Od
                'Optimization': '0',
                'DebugInformationFormat': '4',
                'AdditionalOptions':[
                  '/wd4244',
                  '/wd4267',
                  '/wd4018',
                  '/wd4355',
                  '/wd4800',
                  '/wd4251',
                  '/wd4996',
                  '/wd4146',
                  '/wd4305',
                ],
                'ForcedIncludeFiles':['config.h'],
              },
              'VCLinkerTool': {
                'GenerateDebugInformation': 'true',
                'GenerateMapFile': 'false',
                'IgnoreDefaultLibraryNames': [
                    #'Libcmtd.lib'
                  ],
              },
            },

            'defines':[
              '_CONSOLE',
              '_DEBUG',
            ],
          }, # Debug

          'Release': {

            'msvs_settings': {

              # VS编译器设置
              'VCCLCompilerTool': {

                # 多线程 DLL (/MD)
                'RuntimeLibrary': '2',
                # 完全优化 /Os
                'Optimization': '2',
                # 使用内部函数 /Oi
                'EnableIntrinsicFunctions': 'true',
                # 程序数据库 (/Zi)
                'DebugInformationFormat': '3',
                'ForcedIncludeFiles':['config.h'],
              },
              # END VCCLCOMPILERTOOL

              # VS链接器相关设置
              'VCLinkerTool': {

                'GenerateDebugInformation': 'true',
                'GenerateMapFile': 'false',
                'IgnoreDefaultLibraryNames': [
                  #'Libcmtd.lib'
                ],
              },
              # END VCLINKERTOOL
            },
            # END MSVS_SETTINGS

            'defines':[
              'NDEBUG',
            ],
            
          }, # Release

        },# END CONFIGURATIONS

      }],# END 'OS == "win"'

    ], # END 'conditions'
  }, #END TARGET_DEFAULTS

}