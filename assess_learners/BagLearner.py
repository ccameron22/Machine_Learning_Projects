import numpy as np
import random
import LinRegLearner as lrl
import DTLearner as dt
import RTLearner as rt

class BagLearner:
    def __init__(self, learner, kwargs={"argument1": 1, "argument2": 2}, bags=20, boost=False, verbose=False):
        """
        Bootstrap Aggregation Learner (BagLearner).

        Parameters:
            learner (class): Points to any arbitrary learner class that will be used in the BagLearner.
            kwargs (dict): Keyword arguments passed on to the learner's constructor.
            bags (int): The number of learners you should train using Bootstrap Aggregation.
            boost (bool): If True, implement boosting (optional implementation).
            verbose (bool): If True, print out information for debugging. If False, no output generated.
        """
        # Initialize attributes
        self.learner = learner
        self.kwargs = kwargs
        self.bags = bags
        self.verbose = verbose
        self.learners = []

    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner.

        Parameters:
            data_x (numpy.ndarray): A set of feature values used to train the learner.
            data_y (numpy.ndarray): The value we are attempting to predict given the X data.
        """


        # Find the length of a row (number of features)
        num = len(data_x[0])
        # Created subsets of x and y with the same datatype as x and y to avoid issues
        # when passing in as parameters to called learners
        # Used this documentation to determine how to assign a datatype
        # https://numpy.org/doc/stable/reference/generated/numpy.empty.html
        data_x_subset = np.empty((self.bags, num), dtype=data_x.dtype)
        data_y_subset = np.empty(self.bags, dtype=data_y.dtype)

        # Loop through the process to create the desired number of learners
        for i in range(0, self.bags):
            # Generate subsets of data with 'bags' number of samples
            for j in range(0, self.bags):
                # ensure subset of data have the correct dimensions and matching rows (samples) for x and y
                data_x_subset[j] = random.choice(data_x)
                data_y_subset[j] = random.choice(data_y)
            # create 'bag' number of learners and store in a list for later reference during query
            learnerInstance = self.learner(**self.kwargs)
            learnerInstance.add_evidence(data_x_subset, data_y_subset)
            self.learners.append(learnerInstance)

    def author(self):
        """
        Returns:
            str: The username of the student.
        """
        return "xxx"

    def study_group(self):
        """
        Returns:
            str: A comma-separated string of User_Name of each member of your study group.
        """
        return "xxx"

    def query(self, points):
        """
        Estimate a set of test points given the model we built.

        Parameters:
            points (numpy.ndarray): A numpy array with each row corresponding to a specific query.

        Returns:
            numpy.ndarray: The predicted result of the input data according to the trained model.
        """
        # Call each learner with the list of points
        results = []
        for learner in self.learners:
            result = learner.query(points)
            results.append(result)
        return np.mean(results, axis=0)

def author():
    """
    Returns:
        str: The username of the student
    """
    return "xxx"
