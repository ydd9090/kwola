from kwola.config.logger import getLogger
from ...managers.TrainingManager import TrainingManager
from ..base.TestingStepPluginBase import TestingStepPluginBase
import concurrent.futures
import os



class PrecomputeSessionsForSampleCache(TestingStepPluginBase):
    """
        This plugin creates bug objects for all of the errors discovered during this testing step
    """
    def __init__(self, config):
        self.config = config

    def testingStepStarted(self, testingStep, executionSessions):
        pass

    def beforeActionsRun(self, testingStep, executionSessions, actions):
        pass

    def afterActionsRun(self, testingStep, executionSessions, traces):
        pass

    def testingStepFinished(self, testingStep, executionSessions):
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            futures = []
            for session in executionSessions:
                getLogger().info(f"[{os.getpid()}] Preparing samples for {session.id} and adding them to the sample cache.")
                futures.append(executor.submit(TrainingManager.addExecutionSessionToSampleCache, session.id, self.config))
            for future in futures:
                future.result()

    def sessionFailed(self, testingStep, executionSession):
        pass
