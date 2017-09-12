# LTE_GW.gyp
# Author:pengchun
# Data:2017/7/3

# 说明
# LTE_GW.gyp主要用来管理LTE_GW工程，
# 可以使用该文件在Linux平台和Windows平台生
# 相关工程。在Linux下会生成makefile文件在
# Windows平台会生成VS工程文件。

{
  
  # 开始构建工程
  # 工程名称：LTE_GW,
  # 工程类型：生成可执行文件

  'targets':[
    {
       'target_name':'ffmpeg',
       'type':'none',
        'dependencies':[

          'libavcodec.gyp:*',
          'libavfilter.gyp:*',
          'libavformat.gyp:*',
          'libavutil.gyp:*',
          'libswscale.gyp:*',
          'zlib.gyp:*',
           
        ], # sources


        
     }, # target


   ] # targes

} # total file