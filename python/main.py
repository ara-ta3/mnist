import numpy as np

import pickle

from mnist.dataload import load_mnist
from mnist.simplenetwork import SimpleNetWork


def main():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)
    network = SimpleNetWork(input_size=784, hidden_size=50, output_size=10)
    x_batch = x_train[:3]
    t_batch = t_train[:3]
    grad_numerical = network.numerical_gradient(
        x_batch, t_batch
    )
    grad_backprop = network.gradient(
        x_batch, t_batch
    )

    with open('grad_numerical.pkl', mode='wb') as f:
        pickle.dump(grad_numerical, f)

    for key in grad_numerical.keys():
        diff = np.average(
            np.abs(grad_backprop[key] - grad_numerical[key])
        )
        print(key + ":" + str(diff))


if __name__ == '__main__':
    main()
