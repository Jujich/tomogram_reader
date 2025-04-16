import matplotlib
from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D

matplotlib.use('TkAgg')

example_filename = 'data/BraTS2021_00000_flair.nii'
img = nib.load(example_filename)
print(img)
print(img.header['db_name'])  # output header information

# shape has four parameters patient001_4d.nii.gz
# shape has three parameters patient001_frame01.nii.gz patient001_frame12.nii.gz
# shape has three parameters patient001_frame01_gt.nii.gz patient001_frame12_gt.nii.gz
width, height, queue = img.dataobj.shape
OrthoSlicer3D(img.dataobj).show()

num = 1
for i in range(0, queue, 10):
    img_arr = img.dataobj[:, :, i]
    plt.subplot(5, 4, num)
    plt.imshow(img_arr, cmap='gray')
    num += 1

plt.show()