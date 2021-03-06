import aplpy
import numpy as np
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib import rc
rc('text', usetex=True)
font = {'weight' : 'normal','size':20,'family':'sans-serif','sans-serif':['Helvetica']}
rc('font', **font)

sehdu1 = fits.open('mom0_SE_mask_c18o_pix_2_Tmb.fits')[0]
nwhdu1 = fits.open('mom0_NW_mask_c18o_pix_2_Tmb.fits')[0]

SEmom0 = 1
NWmom0 = 1

if SEmom0 == 1:
    xcenter = 314.0150412
    ycenter = 43.70085501
    wid = 1.1022223
    hei = 0.7527778
    xpanels = 1
    ypanels = 1
    fig=plt.figure(figsize=(3*xpanels*1.1*(wid/(wid+hei))*10.,3*ypanels/1.1*(hei/(wid+hei))*10.))
    ff = aplpy.FITSFigure(sehdu1, figure=fig)
    ff.recenter(xcenter,ycenter,width=wid,height=hei) 
    ff.set_theme('publication')
    #ff.set_system_latex(True)
    maxcolor = 20.
    mincolor = 0.
    ff.show_colorscale(cmap='afmhot', vmin=mincolor, vmax=maxcolor, stretch='sqrt')
    #ff.show_regions('olay.reg')
    #ff.show_regions('olay1.reg')
    ff.add_colorbar() 
    ff.colorbar.set_pad(0.5)
    ff.colorbar.set_axis_label_text('K km s$^{-1}$')
    ff.add_scalebar(0.1,corner='top right',pad=1) # degree for 1pc at 550 pc
    ff.scalebar.set_label('1 pc') 
    beamx = xcenter + wid/2.*1.2
    beamy = ycenter - hei/2.*9./10.
    bmaj = sehdu1.header['BMAJ']
    bmin = sehdu1.header['BMIN']
    beamangle = sehdu1.header['BPA'] 
    ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
    textx = xcenter - wid/2.*9./10.
    texty = ycenter - hei/2.*9./10.
    ff.add_label(textx,texty,'0th-moment C$^{18}$O(1-0)',weight='bold')
    #ff.tick_labels.set_xformat('dd')
    #ff.tick_labels.set_yformat('dd')
    pdfname = 'mom0_SE_c18o_pix_2_Tmb.pdf'
    os.system('rm '+pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMANan/'))

if NWmom0 == 1:
    xcenter = 312.5676799
    ycenter = 44.5018964
    wid = 0.3561111
    hei = 0.5444445
    xpanels = 1
    ypanels = 1
    fig=plt.figure(figsize=(3*xpanels*1.1*(wid/(wid+hei))*10.,3*ypanels/1.1*(hei/(wid+hei))*10.))
    ff = aplpy.FITSFigure(nwhdu1, figure=fig)
    ff.recenter(xcenter,ycenter,width=wid,height=hei) 
    ff.set_theme('publication')
    #ff.set_system_latex(True)
    maxcolor = 20.
    mincolor = 0.
    ff.show_colorscale(cmap='afmhot', vmin=mincolor, vmax=maxcolor, stretch='sqrt')
    #ff.show_regions('olay.reg')
    #ff.show_regions('olay1.reg')
    ff.add_colorbar() 
    ff.colorbar.set_pad(0.5)
    ff.colorbar.set_axis_label_text('K km s$^{-1}$')
    ff.add_scalebar(0.05,corner='bottom right',pad=1) # degree for 0.5 pc at 550 pc
    ff.scalebar.set_label('0.5 pc') 
    beamx = xcenter + wid/2.*1.3
    beamy = ycenter - hei/2.*9./10.
    bmaj = nwhdu1.header['BMAJ']
    bmin = nwhdu1.header['BMIN']
    beamangle = nwhdu1.header['BPA'] 
    ff.show_ellipses(beamx,beamy,bmaj,bmin,angle=beamangle-90,facecolor='black',edgecolor='black')
    textx = xcenter + wid/2.*4./5.
    texty = ycenter + hei/2.*9./10.
    ff.add_label(textx,texty,'0th-moment C$^{18}$O(1-0)',weight='bold')
    #ff.tick_labels.set_xformat('dd')
    #ff.tick_labels.set_yformat('dd')
    pdfname = 'mom0_NW_c18o_pix_2_Tmb.pdf'
    os.system('rm '+pdfname)
    plt.savefig(pdfname,bbox_inches='tight')
    os.system('open '+pdfname)
    os.system('cp '+pdfname+os.path.expandvars(' /Users/shuokong/GoogleDrive/imagesCARMANan/'))


