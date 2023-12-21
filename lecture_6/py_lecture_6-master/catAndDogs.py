import numpy as np
from keras.layers import Convolution2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import MaxPooling2D
from keras.models import Sequential
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

# initializing the cnn
classifier = Sequential()
# step1-convolution
classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))
# step2-maxpooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))
# step3-flattening
classifier.add(Flatten())
# step4-fullconnection
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=1, activation='sigmoid'))

# part2-fitting the cnn to the images
train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

# Generating images for the Test set
test_datagen = ImageDataGenerator(rescale=1. / 255)

# Creating training set
training_set = train_datagen.flow_from_directory(
    'dataset/training_set',
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary')

# Creating the Test set
test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

classifier.compile(loss='binary_crossentropy')
classifier.fit_generator(training_set, steps_per_epoch=8000, epochs=25, validation_data=test_set,
                         validation_steps=2000)


# to predict new images
def predict_image(image_path, cl):
    predict = image.load_img(image_path, target_size=(64, 64))
    predict_modified = image.img_to_array(predict)
    predict_modified = predict_modified / 255
    predict_modified = np.expand_dims(predict_modified, axis=0)
    result = cl.predict(predict_modified)
    if result[0][0] >= 0.5:
        prediction = 'dog'
        probability = result[0][0]
    else:
        prediction = 'cat'
        probability = 1 - result[0][0]

    print("probability = " + str(probability))
    print("Prediction = " + prediction)


predict_image("dataset/test_set/Cats/5.jpg", classifier)
