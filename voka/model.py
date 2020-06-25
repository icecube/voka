'''
The model module currently consists solely of the Voka class.
'''

import math
import collections
import voka.lof

class Voka:
    '''
    Class to handle determination of the outlier detection thresholds
    for a given set of benchmark histograms.
    '''
    def __init__(self):
        # the reference collection is a dictionary containing
        # as values dictionaries with the same structure as the test
        # dictionary.  The keys are arbitrary names for the different
        # sets.
        # Reference {'', {'', []}}
        # Test {'', []}
        self.__reference_collection = dict()
        self.__k = int()
        self.__thresholds = dict()

    def train(self,
              reference_collection,
              k=3,
              tolerance_factor=math.sqrt(2)):
        '''
        Calculate LOF thresholds from the reference set.
        '''
        self.__reference_collection = reference_collection
        self.__k = k

        # we use each one as a test and the others
        # as a benchmark set and determine the
        lof_values = collections.defaultdict(list)
        for test_collection in reference_collection.values():
            # No need to remove the set from itself.
            # Identity should resolve to 0 in each test
            # contributing nothing to the calculation of
            # the average.
            result = self.execute(test_collection)

            for key, lof in result.items():
                lof_values[key].append(lof)

        self.__thresholds = {histogram_name: tolerance_factor*max(lofs)
                             for histogram_name, lofs in lof_values.items()}

    def execute(self, test):
        '''
        calculate the thresholds from the benchmark set
        '''
        result = dict()
        for test_key, test_sequence in test.items():

            # pull the reference sequences out of the collection
            reference_sequences = list()
            for ref_set in self.__reference_collection.values():
                if test_key in ref_set:
                    reference_sequences.append(ref_set[test_key])

            lof = voka.lof.LOF(test_sequence,
                               self.__k,
                               reference_sequences)

            result[test_key] = lof
        return result

    def results(self, results):
        '''
        Apply the thresholds determined during training
        and indicate pass/fail.
        '''
        result = dict()
        for key, lof in results.items():
            result[key] = {'pass': lof <= self.__thresholds[key],
                           'lof': lof,
                           'threshold': self.__thresholds[key]}
        return result
