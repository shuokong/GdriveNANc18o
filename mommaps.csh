#!/bin/csh

rm -rf mom0_NW_mask_c18o_pix_2_Tmb.mir
rm -rf mom0_SE_mask_c18o_pix_2_Tmb.mir
moment in=NW_mask_c18o_pix_2_Tmb.mir mom=0 region="kms,images(-10,10)" out=mom0_NW_mask_c18o_pix_2_Tmb.mir
moment in=SE_mask_c18o_pix_2_Tmb.mir mom=0 region="kms,images(-10,10)" out=mom0_SE_mask_c18o_pix_2_Tmb.mir
rm -rf mom0_NW_mask_c18o_pix_2_Tmb.fits
rm -rf mom0_SE_mask_c18o_pix_2_Tmb.fits
fits in=mom0_NW_mask_c18o_pix_2_Tmb.mir op=xyout out=mom0_NW_mask_c18o_pix_2_Tmb.fits
fits in=mom0_SE_mask_c18o_pix_2_Tmb.mir op=xyout out=mom0_SE_mask_c18o_pix_2_Tmb.fits
rm -rf mom0_NW_mask_c18o_pix_2_Tmb.mir
rm -rf mom0_SE_mask_c18o_pix_2_Tmb.mir

rm -rf mom1_NW_mask_c18o_pix_2_Tmb.mir
rm -rf mom1_SE_mask_c18o_pix_2_Tmb.mir
moment in=NW_mask_c18o_pix_2_Tmb.mir mom=1 region="kms,images(-10,10)" clip="-10000,3.0" out=mom1_NW_mask_c18o_pix_2_Tmb.mir
moment in=SE_mask_c18o_pix_2_Tmb.mir mom=1 region="kms,images(-10,10)" clip="-10000,3.0" out=mom1_SE_mask_c18o_pix_2_Tmb.mir
rm -rf mom1_NW_mask_c18o_pix_2_Tmb.fits
rm -rf mom1_SE_mask_c18o_pix_2_Tmb.fits
fits in=mom1_NW_mask_c18o_pix_2_Tmb.mir op=xyout out=mom1_NW_mask_c18o_pix_2_Tmb.fits
fits in=mom1_SE_mask_c18o_pix_2_Tmb.mir op=xyout out=mom1_SE_mask_c18o_pix_2_Tmb.fits
rm -rf mom1_NW_mask_c18o_pix_2_Tmb.mir
rm -rf mom1_SE_mask_c18o_pix_2_Tmb.mir

rm -rf mom2_NW_mask_c18o_pix_2_Tmb.mir
rm -rf mom2_SE_mask_c18o_pix_2_Tmb.mir
moment in=NW_mask_c18o_pix_2_Tmb.mir mom=2 region="kms,images(-10,10)" clip="-10000,3.0" out=mom2_NW_mask_c18o_pix_2_Tmb.mir
moment in=SE_mask_c18o_pix_2_Tmb.mir mom=2 region="kms,images(-10,10)" clip="-10000,3.0" out=mom2_SE_mask_c18o_pix_2_Tmb.mir
rm -rf mom2_NW_mask_c18o_pix_2_Tmb.fits
rm -rf mom2_SE_mask_c18o_pix_2_Tmb.fits
fits in=mom2_NW_mask_c18o_pix_2_Tmb.mir op=xyout out=mom2_NW_mask_c18o_pix_2_Tmb.fits
fits in=mom2_SE_mask_c18o_pix_2_Tmb.mir op=xyout out=mom2_SE_mask_c18o_pix_2_Tmb.fits
rm -rf mom2_NW_mask_c18o_pix_2_Tmb.mir
rm -rf mom2_SE_mask_c18o_pix_2_Tmb.mir
