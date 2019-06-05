import numpy as np
import os
import sys
import math
import aplpy
import matplotlib as mpl
import matplotlib.pyplot as plt
import pyfits

fitsfiles={'color':{'fname':'chan1_NW_mask_c18o_pix_2_Tmb.fits','title':'C18O(1-0)','bmaj':0,'bmin':0,'galpa':0},
        'template':{'fname':'chan1_NW_mask_c18o_pix_2_Tmb.fits'},
         'channel':{'fname':'../NW_mask_c18o_pix_2_Tmb.fits','title':r'C18O(1-0)','mincolor':1.,'maxcolor':3.},
           }

os.system('cp '+fitsfiles['template']['fname']+' '+'template_'+fitsfiles['template']['fname'])
templatehdulist = pyfits.open('template_'+fitsfiles['template']['fname'])
templatedata = templatehdulist[0].data
nanpixels = np.isnan(templatedata) # maybe this can be broadcast to the entire channeldata array. tbd
channelhdulist = pyfits.open(fitsfiles['channel']['fname'])
channeldata = channelhdulist[0].data

def currentvel(hdulistheader,currentchannel):
    vref = hdulistheader['CRVAL3']
    vdelt= hdulistheader['CDELT3']
    return (vref + (currentchannel - 1) * vdelt)/1.e3

ypanels=3
xpanels=4
xcenter = 312.5676799
ycenter = 44.5018964
wid = 0.3561111
hei = 0.5444445

firstchannelstart=1
lastchannel=120

for startchan in range(firstchannelstart,lastchannel,ypanels*xpanels):

    channelstart=startchan # start from which channel, note the different starting index. tbd
    currentchannel=channelstart
    pdfname='NW_chan_c18o'+str(startchan)+'.pdf'
    
    fig=plt.figure(figsize=(3*xpanels,4*ypanels))
    for j in range(0,ypanels): # this order first follows row
        for i in range(0,xpanels):
            templatedata[0,0,:,:]=channeldata[0,currentchannel-1,:,:]
            templatedata[nanpixels] = np.nan
            templatehdulist.writeto('template_channel.fits',output_verify='exception',clobber=True,checksum=False) # use this as template to output every single channel
            subpos=[0.1+0.8/xpanels*i,0.1+0.9/ypanels*(ypanels-1-j),0.8/xpanels*0.99,0.9/ypanels*0.99]
            ff = aplpy.FITSFigure('template_channel.fits',figure=fig,subplot=subpos)
            ff.recenter(xcenter,ycenter,width=wid,height=hei) 
            ff.set_theme('publication')
            mincolor = fitsfiles['channel']['mincolor']
            maxcolor = fitsfiles['channel']['maxcolor']
            ff.show_colorscale(vmin=mincolor,vmax=maxcolor,cmap='afmhot',stretch='sqrt')
            ff.tick_labels.set_yformat('dd.d')
            ff.tick_labels.set_xformat('dd.d')
            beamx = xcenter + wid/2.*1.3
            beamy = ycenter - hei/2.*9./10.
            bmaj = channelhdulist[0].header['BMAJ']
            bmin = channelhdulist[0].header['BMIN']
            beamangle = channelhdulist[0].header['BPA'] 
            ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
            textx = xcenter + wid/2.*4./5.
            texty = ycenter + hei/2.*9./10.
            ff.add_label(textx,texty,'{0:.2f}'.format(currentvel(channelhdulist[0].header,currentchannel))+'km/s',color='black',horizontalalignment='left',verticalalignment='top')
            if j != ypanels-1:
                ff.hide_xaxis_label()
                ff.hide_xtick_labels()
            if i != 0:
                ff.hide_yaxis_label()
                ff.hide_ytick_labels()
            currentchannel = currentchannel + 1
            os.system('rm template_channel.fits')
    ax1 = fig.add_axes([0.90,0.697,0.01,0.9/ypanels])
    cmap = mpl.cm.afmhot
#    norm = mpl.colors.Normalize(vmin=mincolor, vmax=maxcolor)
    norm = mpl.colors.PowerNorm(gamma=0.5,vmin=mincolor, vmax=maxcolor)
    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical',format='%.1f')#,ticks=colorticks)
    
    # close and save file
    fig.canvas.draw()
    os.system('rm '+pdfname)
    #plt.savefig(pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    plt.close(fig)
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMANan/'))

templatehdulist.close()
channelhdulist.close()

