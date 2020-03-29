from keras.models import load_model
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def predict_digit(img):
    #img=Image.open(img)
    #resize image to 28x28 pixels
    img = img.resize((28,28))
    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    #reshaping to support our model input and normalizing
    img = img.reshape(1,28,28,1)
    img = img/255.0
    img=img.reshape(1,28,28,1)
    #predicting the class
    plt.imshow(img.reshape(28,28),cmap=plt.cm.binary)
    plt.show()
    print('now predicting the digit')
    res = model.predict([img])
    return np.argmax(res), max(res)


model = load_model('model/collabmnist.h5')

img=Image.open('saveImage/1.png')

digit, accuracy = predict_digit(img)
print(digit)
#print(accuracy)
