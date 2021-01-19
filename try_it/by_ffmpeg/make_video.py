#import os
import subprocess

#run_dest = os.popen("rm *.mp4")
p=subprocess.Popen("rm *.mp4",shell=True)
p.wait()

i=0
text = 'x'
f = open('pic_list.txt')
f_v = open('video_list.txt', 'w' )
cmd_str_templete = 'ffmpeg -loop 1 -i pics/%s -pix_fmt yuv420p -vcodec libx264 -b:v 600k -preset medium -crf 30 -s 1920x1080 -r 30 -t %s %d.mp4'
for line in f:
    i = i+1
    name_during = line.split()
    #print('\n%d: '% i)
    cmd_current = cmd_str_templete%(name_during[0],name_during[1],i)
    print('%s: %s'%(name_during[0],name_during[1]))
    print("--------------%s--------------"%cmd_current)
    #nowtime = os.popen(cmd_current)
    #print( nowtime.read() )
    p=subprocess.Popen(cmd_current,shell=True)
    p.wait()

    f_v.write('file %d.mp4\n'%i)
    
f.closed
f_v.closed

cmd_concat = 'ffmpeg -f concat -i video_list.txt -c copy output.mp4'
#os.popen(cmd_concat)
p=subprocess.Popen(cmd_concat,shell=True)
p.wait()

""" merge mp4 & mp3 """
cmd_merge = 'ffmpeg -i output.mp4 -i audio.mp3 -c:v copy -c:a aac -strict experimental final.mp4'
#os.popen(cmd_merge)
p=subprocess.Popen(cmd_merge,shell=True)
p.wait()