import BagLearner as bl
import LinRegLearner as lrl
class InsaneLearner:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.bag_learners = [bl.BagLearner(learner=lrl.LinRegLearner, kwargs={}, bags=20, boost=False, verbose=False) for i in range(20)]
    def add_evidence(self, data_x, data_y):
        self.bag_learner_predictions = []
        for learner in self.bag_learners:
            learner.add_evidence(data_x, data_y)
            self.bag_learner_predictions.append(learner.query(data_x))
    def author(self):
        return "xxx"
    def query(self, points):
        predictions = []
        for learner in self.bag_learners:
            predictions.append(learner.query(points))
        return predictions
