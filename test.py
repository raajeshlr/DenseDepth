import os
import glob
import argparse
import matplotlib

# Keras / TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from keras.models import load_model
from layers import BilinearUpSampling2D
from utils import predict, load_images, display_images, write_images
from matplotlib import pyplot as plt

# Argument Parser
#parser = argparse.ArgumentParser(description='High Quality Monocular Depth Estimation via Transfer Learning')
#parser.add_argument('--model', default='nyu.h5', type=str, help='Trained Keras model file.')
#parser.add_argument('--input', default='examples/*.jpg', type=str, help='Input filename or folder.')
#parser.add_argument('--start', default=1, type=str, help='start of file name.') #change
#parser.add_argument('--end', default=11, type=str, help='end-1 of file name.') #change
#args = parser.parse_args()

# Custom object needed for inference and training
#custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': None}

#print('Loading model...')

# Load model into GPU / CPU
#model = load_model(args.model, custom_objects=custom_objects, compile=False)

#print('\nModel loaded ({0}).'.format(args.model))

# Input images
#inputs = load_images( glob.glob(args.input) )
#print('\nLoaded ({0}) images of size {1}.'.format(inputs.shape[0], inputs.shape[1:]))

# Compute results
#outputs = predict(model, inputs)

#matplotlib problem on ubuntu terminal fix
#matplotlib.use('TkAgg')   

# Display results
#display_images(outputs.copy(), inputs.copy(),start = int(args.start), end = int(args.end))
#viz = display_images(outputs.copy(), inputs.copy())
#plt.figure(figsize=(10,5))
#plt.imshow(viz)
#plt.savefig('test.png')
#plt.show()

def loadmodel():
    custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': None}
    print('Loading model...')
    # Load model into GPU / CPU
    model = load_model('nyu.h5', custom_objects=custom_objects, compile=False)
    return model

def predict_output(model, inputs, log=False):

    #inputs = load_images(inpath, start, end)
    #if log:
    #    print('Loaded images from :', start, ' till: ', end)
    #    print('\nLoaded ({0}) images of size {1}.'.format(inputs.shape[0], inputs.shape[1:]))
    # Compute results
    outputs = predict(model, inputs)
    # Display results
    #write_images(outpath, start, outputs.copy(), inputs.copy(), log=log)
    #if log:
        #print('Finished generating images from :', start, ' till: ', end)

    return outputs  



