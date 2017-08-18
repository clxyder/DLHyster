import numpy as np
import random
import pickle

def create_feature_sets_and_labels(training, test_size = 0.15):
    dt = np.dtype([('x1', float), ('x2', float), ('x3', float), ('x4', float), ('soc', float)])
    data = np.loadtxt(training, usecols = range(5), dtype = dt)
    
    features = data
    random.shuffle(features)
    features = np.array(features)
    
    testing_size = int(test_size * len(features))
    print(testing_size)
    print(len(features))
    print(len(features[0]))
    print(features[0])

    train_x = list(features[['x1', 'x2', 'x3', 'x4']][:-testing_size])
    train_y = list(features[['soc']][:-testing_size])

    test_x = list(features[['x1', 'x2', 'x3', 'x4']][-testing_size:])
    test_y = list(features[['soc']][-testing_size:])
    
##    train_x = list(features[:4][:-testing_size])
##    train_y = list(features[5][:-testing_size])
##
##    test_x = list(features[:4][-testing_size:])
##    test_y = list(features[5][-testing_size:])

    print(len(train_x))
    print(len(train_x[0]))
    return train_x, train_y, test_x, test_y

if __name__ == '__main__':
    train_x, train_y, test_x, test_y = create_feature_sets_and_labels('new_training1.dat')
    with open('hyster_set.pickle', 'wb') as f:
        pickle.dump([train_x, train_y, test_x, test_y], f)
