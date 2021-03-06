# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
MultiAverage
"""


from ..utils.entrypoints import Component
from ..utils.utils import try_set


def multi_average(
        normalize=True,
        **params):
    """
    **Description**
        None

    :param normalize: Whether to normalize the output of base models
        before combining them (settings).
    """

    entrypoint_name = 'MultiAverage'
    settings = {}

    if normalize is not None:
        settings['Normalize'] = try_set(
            obj=normalize, none_acceptable=True, is_of_type=bool)

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='EnsembleMulticlassOutputCombiner')
    return component
