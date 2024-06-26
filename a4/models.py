import nn


class PerceptronModel(object):
    def __init__(self, dim):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dim` is the dimensionality of the data.
        For example, dim=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dim)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x_point):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x_point: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        return nn.DotProduct(self.w, x_point)

    def get_prediction(self, x_point):
        """
        Calculates the predicted class for a single data point `x_point`.

        Returns: -1 or 1
        """
        return -1 if nn.as_scalar(self.run(x_point)) < 0 else 1

    def train_model(self, dataset):
        """
        Train the perceptron until convergence.
        """
        missed = 1
        while missed > 0:
            missed = 0
            for x, y in dataset.iterate_once(1):
                predicted = self.get_prediction(x)
                expected = nn.as_scalar(y)

                if predicted != expected:
                    self.w.update(expected, x)
                    missed += 1


class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """

    def __init__(self):
        # Initialize your model parameters here
        # why negative???
        self.learning_rate = -0.0069  # minimum allowed (0.001, 1.0)
        self.batch_size = 50  # must divide dataset evenly (dataset is 200?)

        # first layer starts with 1
        # last layer ends with 1
        self.w1 = nn.Parameter(1, 25)  # (input size, output size)
        self.b1 = nn.Parameter(1, 25)  # (1, same as weight)
        self.w2 = nn.Parameter(25, 50)  # (input size, output size)
        self.b2 = nn.Parameter(1, 50)   # (1, same as weight)
        self.w3 = nn.Parameter(50, 1)  # (input size, output size)
        self.b3 = nn.Parameter(1, 1)   # (1, same as weight)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        l1 = nn.ReLU(nn.AddBias(nn.Linear(x, self.w1), self.b1))
        l2 = nn.ReLU(nn.AddBias(nn.Linear(l1, self.w2), self.b2))
        l3 = nn.AddBias(nn.Linear(l2, self.w3), self.b3)
        return l3

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        return nn.SquareLoss(self.run(x), y)

    def train_model(self, dataset):
        """
        Trains the model.
        """
        cur_loss = 1.0
        for x, y in dataset.iterate_forever(self.batch_size):
            if cur_loss <= 0.0003:
                break
            # Calculates loss
            loss = self.get_loss(x, y)
            cur_loss = nn.as_scalar(loss)

            # Updates weights from gradients
            [w1_grad, b1_grad, w2_grad, b2_grad, w3_grad, b3_grad] = nn.gradients(
                [self.w1, self.b1, self.w2, self.b2, self.w3, self.b3], loss)
            self.w1.update(self.learning_rate, w1_grad)
            self.b1.update(self.learning_rate, b1_grad)
            self.w2.update(self.learning_rate, w2_grad)
            self.b2.update(self.learning_rate, b2_grad)
            self.w3.update(self.learning_rate, w3_grad)
            self.b3.update(self.learning_rate, b3_grad)


class DigitClassificationModel(object):
    """
    A model for handwritten digit classification using the MNIST dataset.

    Each handwritten digit is a 28x28 pixel grayscale image, which is flattened
    into a 784-dimensional vector for the purposes of this model. Each entry in
    the vector is a floating point number between 0 and 1.

    The goal is to sort each digit into one of 10 classes (number 0 through 9).

    (See RegressionModel for more information about the APIs of different
    methods here. We recommend that you implement the RegressionModel before
    working on this part of the project.)
    """

    def __init__(self):
        # Initialize your model parameters here
        # why negative???
        self.learning_rate = -0.05  # minimum allowed (0.001, 1.0)
        self.batch_size = 32

        # first layer starts with 1
        # last layer ends with 1
        self.w1 = nn.Parameter(784, 256)  # (input size, output size)
        self.b1 = nn.Parameter(1, 256)  # (1, same as weight)
        self.w2 = nn.Parameter(256, 10)  # (input size, output size)
        self.b2 = nn.Parameter(1, 10)   # (1, same as weight)

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Your model should predict a node with shape (batch_size x 10),
        containing scores. Higher scores correspond to greater probability of
        the image belonging to a particular class.

        Inputs:
            x: a node with shape (batch_size x 784)
        Output:
            A node with shape (batch_size x 10) containing predicted scores
                (also called logits)
        """
        l1 = nn.ReLU(nn.AddBias(nn.Linear(x, self.w1), self.b1))
        l2 = nn.AddBias(nn.Linear(l1, self.w2), self.b2)
        return l2

    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        The correct labels `y` are represented as a node with shape
        (batch_size x 10). Each row is a one-hot vector encoding the correct
        digit class (0-9).

        Inputs:
            x: a node with shape (batch_size x 784)
            y: a node with shape (batch_size x 10)
        Returns: a loss node
        """
        return nn.SoftmaxLoss(self.run(x), y)

    def train_model(self, dataset):
        """
        Trains the model.
        """
        while dataset.get_validation_accuracy() < 0.975:
            for x, y in dataset.iterate_once(self.batch_size):
                # Calculates loss
                loss = self.get_loss(x, y)

                # Updates weights from gradients
                [w1_grad, b1_grad, w2_grad, b2_grad] = nn.gradients([self.w1, self.b1, self.w2, self.b2], loss)

                self.w1.update(self.learning_rate, w1_grad)
                self.b1.update(self.learning_rate, b1_grad)
                self.w2.update(self.learning_rate, w2_grad)
                self.b2.update(self.learning_rate, b2_grad)
