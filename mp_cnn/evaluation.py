from mp_cnn.evaluators.sick_evaluator import SICKEvaluator
from mp_cnn.evaluators.msrvid_evaluator import MSRVIDEvaluator
from mp_cnn.evaluators.trecqa_evaluator import TRECQAEvaluator
from mp_cnn.evaluators.wikiqa_evaluator import WikiQAEvaluator
from nce.nce_pairwise_mp.evaluators.trecqa_evaluator import TRECQAEvaluatorNCE
from nce.nce_pairwise_mp.evaluators.wikiqa_evaluator import WikiQAEvaluatorNCE

class MPCNNEvaluatorFactory(object):
    """
    Get the corresponding Evaluator class for a particular dataset.
    """
    evaluator_map = {
        'sick': SICKEvaluator,
        'msrvid': MSRVIDEvaluator,
        'trecqa': TRECQAEvaluator,
        'wikiqa': WikiQAEvaluator
    }

    evaluator_map_nce = {
        'trecqa': TRECQAEvaluatorNCE,
        'wikiqa': WikiQAEvaluatorNCE
    }

    @staticmethod
    def get_evaluator(dataset_cls, model, data_loader, batch_size, device, nce=False):
        if data_loader is None:
            return None

        if nce:
            evaluator_map = MPCNNEvaluatorFactory.evaluator_map_nce
        else:
            evaluator_map = MPCNNEvaluatorFactory.evaluator_map

        if not hasattr(dataset_cls, 'NAME'):
            raise ValueError('Invalid dataset. Dataset should have NAME attribute.')

        if dataset_cls.NAME not in evaluator_map:
            raise ValueError('{} is not implemented.'.format(dataset_cls))

        return evaluator_map[dataset_cls.NAME](
            dataset_cls, model, data_loader, batch_size, device
        )
