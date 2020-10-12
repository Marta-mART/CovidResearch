import zipfile
import os

local_zip = './img/archive.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/img/archive')
zip_ref.close()

# Directory with our training covid pictures
train_covid_dir = os.path.join('/img/archive/TrainImages/COVID-19')

# Directory with our training normal pictures
train_normal_dir = os.path.join('/img/archive/TrainImages/Normal')

train_covid_names = os.listdir(train_covid_dir)
print(train_covid_names[:5])

train_normal_names = os.listdir(train_normal_dir)
print(train_normal_names[:5])

print('total training covid images:', len(os.listdir(train_covid_dir)))
print('total training normal images:', len(os.listdir(train_normal_dir)))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Parameters for our graph; we'll output images in a 4x4 configuration
nrows = 4
ncols = 4

# Index for iterating over images
pic_index = 0

# Set up matplotlib fig, and size it to fit 4x4 pics
fig = plt.gcf()
fig.set_size_inches(ncols * 4, nrows * 4)

pic_index += 8

next_covid_pix = [os.path.join(train_covid_dir, fname)
                  for fname in train_covid_names[pic_index-8:pic_index]]
next_normal_pix = [os.path.join(train_normal_dir, fname)
                  for fname in train_normal_names[pic_index-8:pic_index]]

for i, img_path in enumerate(next_covid_pix+next_normal_pix):
  # Set up subplot
  sp = plt.subplot(nrows, ncols, i + 1)
  sp.axis('Off')

  img = mpimg.imread(img_path)
  plt.imshow(img, cmap='inferno')

plt.show()

