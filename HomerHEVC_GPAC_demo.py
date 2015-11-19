/*****************************************************************************
 * HomerHEVC_GPAC_demo.py : Creating HEVC content in mp4 and ts files
/*****************************************************************************
 * Copyright (C) 2014 homerHEVC project
 *
 * Juan Casal <jcasal@homerhevc.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02111, USA.
 *****************************************************************************/

HOMER_app = "C:\\homerHEVC\\homer_app.exe"
GPAC_MP4_app = "C:\\Program Files\\GPAC\\MP4Box"
GPAC_TS_app = "C:\\Program Files\\GPAC\\mp42ts"

from os import remove
from os import system
from subprocess import call

def DEL(file):
	try:
		remove(file)
	except IOError:
		print ("File " + file + " does not exist and cannot be deleted")
	
	

def CALL(file):
	system(file)



def Homer_GPAC_test(input_file, output_mp4_file, intra_period, horiz, vert, frame_rate, bitrate, perf_mode, sao, num_frames):
	output_265_file = output_mp4_file.replace(".mp4", ".265")	
	output_ts_file = output_mp4_file.replace(".mp4", ".ts")	
	widthxheight = str(horiz) + "x" + str(vert)	
	DEL(output_mp4_file)
	DEL(output_ts_file)
#	print(hevc_file0)
	print("\n------------------------- Using HomerHEVC to encode " + input_file + " to HEVC format -------------------------")
#	print(output_265_file)
	homer_args =[HOMER_app, "-i", input_file, "-o", output_265_file, "-widthxheight", widthxheight, "-intra_period", str(intra_period), "-n_frames", str(num_frames), "-sao", str(sao), "-frame_rate", str(frame_rate), "-bitrate", str(bitrate), "-performance_mode", str(perf_mode)]
#	print(homer_args)
	call(homer_args)
	print("\n\n\n------------------------- Using GPAC to encapsulate" + output_mp4_file + " in MP4 and TS -------------------------")
	gpac_mp4_args =[GPAC_MP4_app, "-add", output_265_file+":fps="+str(frame_rate), "-new", output_mp4_file]
#	print(gpac_mp4_args)	
	call(gpac_mp4_args)
	gpac_ts_args =[GPAC_TS_app, "-prog", output_mp4_file, "-dst-file", output_ts_file]
	print(gpac_ts_args)	
	call(gpac_ts_args)	
#	DEL(output_265_file)




intra_period = 100
sao = 1
perf_mode = 2

#HD content
input_name = "C:\Content\hd_demo_video.yuv"
output_name = "C:\Content\hd_demo_video.mp4"
horizontal = 1280
vertical = 720
frame_rate = 25
bitrate = 800
num_frames = 1400

Homer_GPAC_test(input_name, output_name, intra_period, horizontal, vertical, frame_rate, bitrate, perf_mode, sao, num_frames)
#Play calling
#"C:\Program Files\GPAC\mp4client.exe" "C:\Content\hd_demo_video.mp4"

#SD content
input_name = "C:\Content\sd_demo_video.yuv"
output_name = "C:\Content\sd_demo_video.mp4"
horizontal = 720
vertical = 576
frame_rate = 25
bitrate = 500
num_frames = 1360

Homer_GPAC_test(input_name, output_name, intra_period, horizontal, vertical, frame_rate, bitrate, perf_mode, sao, num_frames)
#Play calling
#"C:\Program Files\GPAC\mp4client.exe" "C:\Content\sd_demo_video.mp4"


