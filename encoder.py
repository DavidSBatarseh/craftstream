import numpy
import math
numpy.float = numpy.float64
numpy.int = numpy.int_
import skvideo
skvideo.setFFmpegPath(r'C:\Users\David Batarseh\Desktop\ffmpeg-master-latest-win64-gpl\bin')
import skvideo.io
import skvideo.datasets
import skvideo.utils
import skimage
import time

def color_encoder(r,g,b):
    colors = [[240,240,240],[242,178,51],[229,127,216],[153, 178, 242],[222, 222, 108],[127, 204, 25],[242, 178, 204],[76, 76, 76],[153, 153, 153],[76, 153, 178],[178, 102, 229],[51, 102, 204],[127, 102, 76],[87, 166, 78],[204, 76, 76],[17, 17, 17]]
    min = 10000
    index = 0
    for x in range(len(colors)):
        distance = math.sqrt((r-colors[x][0])**2+(g-colors[x][1])**2+(b-colors[x][2])**2)
        if distance<min:
            min = distance
            index = x
    return f'{index:x}'
f= open("server/src/videoEncoding.txt", "w")
filename_yuv = "fm.mp4"
vid = skvideo.io.vread("fm.mp4")
T, M, N, C = vid.shape
#for i in range(T):
test = 0
print(M)
print(N)    
chunkHeight = int((M/20))
chunkLength = int((N/28))
chunkSize = chunkLength * chunkHeight
vid_r,vid_g,vid_b = numpy.split(vid, 3, 3)
vid_r = numpy.squeeze(vid_r)
vid_g = numpy.squeeze(vid_g)
vid_b = numpy.squeeze(vid_b)
for t in range(T):
    for y in range(int(M/chunkHeight)):
        for x in range(int(N/chunkLength)):
            yVal = y * chunkHeight
            xVal = x * chunkLength
            chunkR = numpy.sum(vid_r[t][yVal:yVal+chunkHeight,xVal:xVal+chunkLength])/chunkSize
            chunkG = numpy.sum(vid_g[t][yVal:yVal+chunkHeight,xVal:xVal+chunkLength])/chunkSize
            chunkB = numpy.sum(vid_b[t][yVal:yVal+chunkHeight,xVal:xVal+chunkLength])/chunkSize
            f.write(color_encoder(chunkR,chunkG,chunkB))
        f.write("\n")
    print(t)
f.close()