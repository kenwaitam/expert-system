from random import choice
from pyknow import *


class Score():
    points: 0


class Advice(KnowledgeEngine):

    @Rule()
    def ask_prior_education(self):
        self.declare(Fact(education=input(
            "What's was your previous education? ")))
    
    @Rule(
        Fact(education=MATCH.education))
    def show_information(self, education):
        print("%s! " % (education))


engine = Advice()
engine.reset()  # Prepare the engine for the execution.
engine.run()  # Run it!
