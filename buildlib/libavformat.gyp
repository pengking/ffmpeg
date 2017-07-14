
{
	'targets':[
		{
			'target_name':'libavformat',
			'type':'shared_library',
			'includes':[
				'common.gypi',
			],
			'variables':{
				'src_path':'../libavformat',
			},
			'sources':[
				'../config.h',
				'<(src_path)/4xm.c',
				'<(src_path)/adtsenc.c',
				'<(src_path)/aea.c',
				'<(src_path)/aiffdec.c',
				'<(src_path)/aiffenc.c',
				'<(src_path)/allformats.c',
				'<(src_path)/amr.c',
				'<(src_path)/anm.c',
				'<(src_path)/apc.c',
				'<(src_path)/ape.c',
				'<(src_path)/apetag.c',
				'<(src_path)/asf.c',
				'<(src_path)/asfcrypt.c',
				'<(src_path)/asfdec.c',
				'<(src_path)/asfenc.c',
				'<(src_path)/assdec.c',
				'<(src_path)/assenc.c',
				'<(src_path)/au.c',
				'<(src_path)/audiointerleave.c',
				'<(src_path)/avc.c',
				'./avformat-52.def',
				'<(src_path)/avi.c',
				'<(src_path)/avidec.c',
				'<(src_path)/avienc.c',
				'<(src_path)/avio.c',
				'<(src_path)/aviobuf.c',
				'<(src_path)/avisynth.c',
				'<(src_path)/avlanguage.c',
				'<(src_path)/avs.c',
				'<(src_path)/bethsoftvid.c',
				'<(src_path)/bfi.c',
				'<(src_path)/bink.c',
				'<(src_path)/c93.c',
				'<(src_path)/caf.c',
				'<(src_path)/cafdec.c',
				'<(src_path)/cdg.c',
				'<(src_path)/concat.c',
				'<(src_path)/crcenc.c',
				'<(src_path)/cutils.c',
				'<(src_path)/daud.c',
				'./external/DllEntry.c',
				'<(src_path)/dsicin.c',
				'<(src_path)/dv.c',
				'<(src_path)/dvenc.c',
				'<(src_path)/dxa.c',
				'<(src_path)/eacdata.c',
				'<(src_path)/electronicarts.c',
				'<(src_path)/ffmdec.c',
				'<(src_path)/ffmenc.c',
				'<(src_path)/file.c',
				'<(src_path)/filmstripdec.c',
				'<(src_path)/filmstripenc.c',
				'<(src_path)/flacdec.c',
				'<(src_path)/flacenc.c',
				'<(src_path)/flacenc_header.c',
				'<(src_path)/flic.c',
				'<(src_path)/flvdec.c',
				'<(src_path)/flvenc.c',
				'<(src_path)/framecrcenc.c',
				'<(src_path)/gif.c',
				'<(src_path)/gopher.c',
				'<(src_path)/gxf.c',
				'<(src_path)/gxfenc.c',
				'<(src_path)/http.c',
				'<(src_path)/httpauth.c',
				'<(src_path)/id3v1.c',
				'<(src_path)/id3v2.c',
				'<(src_path)/idcin.c',
				'<(src_path)/idroq.c',
				'<(src_path)/iff.c',
				'<(src_path)/img2.c',
				'<(src_path)/ipmovie.c',
				'<(src_path)/isom.c',
				'<(src_path)/iss.c',
				'<(src_path)/iv8.c',
				'<(src_path)/libnut.c',
				'<(src_path)/librtmp.c',
				'<(src_path)/lmlm4.c',
				'<(src_path)/matroska.c',
				'<(src_path)/matroskadec.c',
				'<(src_path)/matroskaenc.c',
				'<(src_path)/metadata.c',
				'<(src_path)/metadata_compat.c',
				'<(src_path)/mm.c',
				'<(src_path)/mmf.c',
				'<(src_path)/mov.c',
				'<(src_path)/movenc.c',
				'<(src_path)/movenchint.c',
				'<(src_path)/mp3.c',
				'<(src_path)/mpc.c',
				'<(src_path)/mpc8.c',
				'<(src_path)/mpeg.c',
				'<(src_path)/mpegenc.c',
				'<(src_path)/mpegts.c',
				'<(src_path)/mpegtsenc.c',
				'<(src_path)/mpjpeg.c',
				'<(src_path)/msnwc_tcp.c',
				'<(src_path)/mtv.c',
				'<(src_path)/mvi.c',
				'<(src_path)/mxf.c',
				'<(src_path)/mxfdec.c',
				'<(src_path)/mxfenc.c',
				'<(src_path)/ncdec.c',
				'<(src_path)/nsvdec.c',
				'<(src_path)/nut.c',
				'<(src_path)/nutdec.c',
				'<(src_path)/nutenc.c',
				'<(src_path)/nuv.c',
				'<(src_path)/oggdec.c',
				'<(src_path)/oggenc.c',
				'<(src_path)/oggparsedirac.c',
				'<(src_path)/oggparseflac.c',
				'<(src_path)/oggparseogm.c',
				'<(src_path)/oggparseskeleton.c',
				'<(src_path)/oggparsespeex.c',
				'<(src_path)/oggparsetheora.c',
				'<(src_path)/oggparsevorbis.c',
				'<(src_path)/oma.c',
				'<(src_path)/options.c',
				'<(src_path)/os_support.c',
				'<(src_path)/psxstr.c',
				'<(src_path)/pva.c',
				'<(src_path)/qcp.c',
				'<(src_path)/r3d.c',
				'<(src_path)/raw.c',
				'<(src_path)/rdt.c',
				'<(src_path)/riff.c',
				'<(src_path)/rl2.c',
				'<(src_path)/rm.c',
				'<(src_path)/rmdec.c',
				'<(src_path)/rmenc.c',
				'<(src_path)/rpl.c',
				'<(src_path)/rtmppkt.c',
				'<(src_path)/rtmpproto.c',
				'<(src_path)/rtp.c',
				'<(src_path)/rtpdec.c',
				'<(src_path)/rtpdec_amr.c',
				'<(src_path)/rtpdec_asf.c',
				'<(src_path)/rtpdec_h263.c',
				'<(src_path)/rtpdec_h264.c',
				'<(src_path)/rtpdec_xiph.c',
				'<(src_path)/rtpenc.c',
				'<(src_path)/rtpenc_aac.c',
				'<(src_path)/rtpenc_amr.c',
				'<(src_path)/rtpenc_h263.c',
				'<(src_path)/rtpenc_h264.c',
				'<(src_path)/rtpenc_mpv.c',
				'<(src_path)/rtpproto.c',
				'<(src_path)/rtsp.c',
				'<(src_path)/rtspenc.c',
				'<(src_path)/sdp.c',
				'<(src_path)/seek.c',
				'<(src_path)/segafilm.c',
				'<(src_path)/sierravmd.c',
				'<(src_path)/siff.c',
				'<(src_path)/smacker.c',
				'<(src_path)/sol.c',
				'<(src_path)/soxdec.c',
				'<(src_path)/soxenc.c',
				'<(src_path)/spdif.c',
				'<(src_path)/swfdec.c',
				'<(src_path)/swfenc.c',
				'<(src_path)/tcp.c',
				'<(src_path)/thp.c',
				'<(src_path)/tiertexseq.c',
				'<(src_path)/timefilter.c',
				'<(src_path)/tmv.c',
				'<(src_path)/tta.c',
				'<(src_path)/txd.c',
				'<(src_path)/udp.c',
				'<(src_path)/utils.c',
				'<(src_path)/vc1test.c',
				'<(src_path)/vc1testenc.c',
				'<(src_path)/voc.c',
				'<(src_path)/vocdec.c',
				'<(src_path)/vocenc.c',
				'<(src_path)/vorbiscomment.c',
				'<(src_path)/vqf.c',
				'<(src_path)/wav.c',
				'<(src_path)/wc3movie.c',
				'<(src_path)/westwood.c',
				'<(src_path)/wv.c',
				'<(src_path)/xa.c',
				'<(src_path)/yop.c',
				'<(src_path)/yuv4mpeg.c',

				'<(src_path)/adts.h',
				'<(src_path)/aiff.h',
				'<(src_path)/apetag.h',
				'<(src_path)/asf.h',
				'<(src_path)/asfcrypt.h',
				'<(src_path)/audiointerleave.h',
				'<(src_path)/avc.h',
				'<(src_path)/avformat.h',
				'<(src_path)/avi.h',
				'<(src_path)/avio.h',
				'<(src_path)/avlanguage.h',
				'<(src_path)/caf.h',
				'<(src_path)/dv.h',
				'<(src_path)/ffm.h',
				'<(src_path)/flacenc.h',
				'<(src_path)/flv.h',
				'<(src_path)/gxf.h',
				'<(src_path)/httpauth.h',
				'<(src_path)/id3v1.h',
				'<(src_path)/id3v2.h',
				'<(src_path)/internal.h',
				'<(src_path)/isom.h',
				'<(src_path)/matroska.h',
				'<(src_path)/metadata.h',
				'<(src_path)/movenc.h',
				'<(src_path)/mpeg.h',
				'<(src_path)/mpegts.h',
				'<(src_path)/mxf.h',
				'<(src_path)/network.h',
				'<(src_path)/nut.h',
				'<(src_path)/oggdec.h',
				'<(src_path)/os_support.h',
				'<(src_path)/qtpalette.h',
				'<(src_path)/raw.h',
				'<(src_path)/rdt.h',
				'<(src_path)/riff.h',
				'<(src_path)/rm.h',
				'<(src_path)/rtmp.h',
				'<(src_path)/rtmppkt.h',
				'<(src_path)/rtp.h',
				'<(src_path)/rtpdec.h',
				'<(src_path)/rtpdec_amr.h',
				'<(src_path)/rtpdec_asf.h',
				'<(src_path)/rtpdec_h263.h',
				'<(src_path)/rtpdec_h264.h',
				'<(src_path)/rtpdec_xiph.h',
				'<(src_path)/rtpenc.h',
				'<(src_path)/rtsp.h',
				'<(src_path)/rtspcodes.h',
				'<(src_path)/seek.h',
				'<(src_path)/sox.h',
				'<(src_path)/swf.h',
				'<(src_path)/timefilter.h',
				'<(src_path)/voc.h',
				'<(src_path)/vorbiscomment.h',

			],
			'dependencies':[
				'libavutil.gyp:*',
				'libavcodec.gyp:*',
			],
			'link_settings':{

				'libraries':[
					'Ws2_32.lib',
					'Vfw32.lib',
				],
			},
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
