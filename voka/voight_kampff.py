import math
import collections
import voka.lof

class VoightKampff(object):

    def __init__(self):
        # the reference should be a collection (iterable)
        # of reference dictionaries.
        # Reference {'', {'', []}}
        # Test {'', []}
        pass

    def determine_parameters(self,
                             reference_collection,
                             k=3,
                             tolerance_factor = math.sqrt(2)):
        '''
        Calculate LOF thresholds from the reference set.
        '''
        self.__reference_collection = reference_collection
        self.__k = k
        # Determining a reasonable value for k on the fly
        # is going to be difficult, I think.

        # we use each one as a test and the others
        # as a benchmark set and determine the

        # we just need an example collection because we want
        # to retain the same structure
        #collection = list(reference_collection.values())[0]
        #lof_values = {name:list() for name in collection.keys()}

        lof_values = collections.defaultdict(list)
        for test_name, test_collection in reference_collection.items():
            # I don't have to remove the set from itself.
            # Identity should resolve to 0 in each test
            # contributing nothing to the calculation of
            # the average.
            result = self.go(test_collection)

            for key, lof in result.items():
                lof_values[key].append(lof)

        self.__thresholds = {histogram_name: tolerance_factor*max(lofs)
                             for histogram_name, lofs in lof_values.items()}

    def go(self, test):
        # calculate the thresholds from
        # the benchmark set
        # we should also be able to determine
        # a reasonable k-distance
        result = dict()
        for test_key, test_sequence in test.items():

            # pull the reference sequences out of the collection
            reference_sequences = list()
            for reference_name, reference_set in self.__reference_collection.items():
                if test_key in reference_set:
                    reference_sequences.append(reference_set[test_key])

            lof = voka.lof.LOF(test_sequence,
                               self.__k,
                               reference_sequences)

            result[test_key] = lof
        return result

    def calculate_results(self, results):
        result = dict()
        for key, lof in results.items():
            result[key] = {'pass': lof < self.__thresholds[key],
                           'lof': lof,
                           'threshold': self.__thresholds[key]}
        return result
