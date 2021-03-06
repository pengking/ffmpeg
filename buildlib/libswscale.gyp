
{
  'targets':[
    {
      'target_name':'libswscale',
      'type':'shared_library',
      'includes':[
        'common.gypi',
      ],
      'variables':{
        'src_path':'../libswscale',
      },
      'sources':[
        '../config.h',
        './external/DllEntry.c', 
        '<(src_path)/options.c', 
        '<(src_path)/rgb2rgb.c', 
        '<(src_path)/swscale.c', 
        '<(src_path)/utils.c', 
        '<(src_path)/yuv2rgb.c', 
        'swscale-0.def', 
        '<(src_path)/rgb2rgb.h', 
        '<(src_path)/swscale.h', 
        '<(src_path)/swscale_internal.h',
      ],
      'dependencies':[
        "libavutil.gyp:*",
      ],
      'defines':[
        'WIN32',
        '_USRDLL',
        'LIBAVUTIL_EXPORTS',
      ],
      'include_dirs':[
        './external/include',
        '../',
      ],

    },
  ]
}
