import splitfolders
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio("datasets/face_dataset_train_images/", output="output",
    seed=1337, ratio=(.8, .2), group_prefix=None, move=True) # default values