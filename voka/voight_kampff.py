import voka.lof

class VoightKampff(object):

    def __init__(self, reference_collection):
        # the reference should be a collection (iterable)
        # of reference dictionaries.
        # Reference {'', {'', []}}
        # Test {'', []}
        self.__reference_collection = reference_collection
        self.__k = 3
        
    def determine_parameters(self):
        # calculate the thresholds from
        # the reference set
        # we should also be able to determine
        # a reasonable k-distance
        pass

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
                    
            result[test_key] = voka.lof.LOF(test_sequence,
                                            self.__k,
                                            reference_sequences)
        return result
    
