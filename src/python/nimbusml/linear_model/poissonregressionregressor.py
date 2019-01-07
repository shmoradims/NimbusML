# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
PoissonRegressionRegressor
"""

__all__ = ["PoissonRegressionRegressor"]


from sklearn.base import RegressorMixin

from ..base_predictor import BasePredictor
from ..internal.core.linear_model.poissonregressionregressor import \
    PoissonRegressionRegressor as core
from ..internal.utils.utils import trace


class PoissonRegressionRegressor(
        core, BasePredictor, RegressorMixin):
    """

    Train an Poisson regression model.

    .. remarks::
        `Poisson regression
        <https://en.wikipedia.org/wiki/Poisson_regression>`_ is a
        parameterized
        regression method. It assumes that the log of the conditional mean of
        the dependent variable follows a linear function of
        the dependent variables. Assuming that the dependent variable follows
        a Poisson distribution,
        the parameters of the regressor can be estimated by maximizing the
        likelihood of the obtained observations.


        **Reference**

            `Poisson regression
            <https://en.wikipedia.org/wiki/Poisson_regression>`_


    :param feature: see `Columns </nimbusml/concepts/columns>`_.

    :param label: see `Columns </nimbusml/concepts/columns>`_.

    :param weight: see `Columns </nimbusml/concepts/columns>`_.

    :param normalize: Specifies the type of automatic normalization used:

        * ``"Auto"``: if normalization is needed, it is performed
          automatically. This is the default choice.
        * ``"No"``: no normalization is performed.
        * ``"Yes"``: normalization is performed.
        * ``"Warn"``: if normalization is needed, a warning
          message is displayed, but normalization is not performed.

        Normalization rescales disparate data ranges to a standard scale.
        Feature
        scaling insures the distances between data points are proportional
        and
        enables various optimization methods such as gradient descent to
        converge
        much faster. If normalization is performed, a ``MaxMin`` normalizer
        is
        used. It normalizes values in an interval [a, b] where ``-1 <= a <=
        0``
        and ``0 <= b <= 1`` and ``b - a = 1``. This normalizer preserves
        sparsity by mapping zero to zero.

    :param caching: Whether learner should cache input training data.

    :param l2_weight: L2 regularization weight.

    :param l1_weight: L1 regularization weight.

    :param opt_tol: Tolerance parameter for optimization convergence. Low =
        slower, more accurate.

    :param memory_size: Memory size for L-BFGS. Lower=faster, less accurate.
        The technique used for optimization here is L-BFGS, which uses only a
        limited amount of memory to compute the next step direction. This
        parameter indicates the number of past positions and gradients to store
        for the computation of the next step. Must be greater than or equal to
        ``1``.

    :param enforce_non_negativity: Enforce non-negative weights. This flag,
        however, does not put any constraint on the bias term; that is, the
        bias term can be still a negtaive number.

    :param init_wts_diameter: Sets the initial weights diameter that specifies
        the range from which values are drawn for the initial weights. These
        weights are initialized randomly from within this range. For example,
        if the diameter is specified to be ``d``, then the weights are
        uniformly distributed between ``-d/2`` and ``d/2``. The default value
        is ``0``, which specifies that all the  weights are set to zero.

    :param max_iterations: Maximum iterations.

    :param sgd_init_tol: Run SGD to initialize LR weights, converging to this
        tolerance.

    :param quiet: If set to true, produce no output during training.

    :param use_threads: Whether or not to use threads. Default is true.

    :param train_threads: Number of threads.

    :param dense_optimizer: If ``True``, forces densification of the internal
        optimization vectors. If ``False``, enables the logistic regression
        optimizer use sparse or dense internal states as it finds appropriate.
        Setting ``denseOptimizer`` to ``True`` requires the internal optimizer
        to use a dense internal state, which may help alleviate load on the
        garbage collector for some varieties of larger problems.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:func:`FastLinearRegressor
        <nimbusml.linear_model.FastLinearRegressor>`,
        :py:func:`OrdinaryLeastSquaresRegressor
        <nimbusml.linear_model.OrdinaryLeastSquaresRegressor>`,
        :py:func:`LightGbmRegressor <nimbusml.ensemble.LightGbmRegressor>`,
        :py:func:`FastForestRegressor <nimbusml.ensemble.FastForestRegressor>`,
        :py:func:`FastTreesRegressor <nimbusml.ensemble.FastTreesRegressor>`,
        :py:func:`GamRegressor <nimbusml.ensemble.GamRegressor>`.

    .. index:: models, regression, linear

    Example:
       .. literalinclude:: /../nimbusml/examples/PoissonRegressionRegressor.py
              :language: python
    """

    @trace
    def __init__(
            self,
            normalize='Auto',
            caching='Auto',
            l2_weight=1.0,
            l1_weight=1.0,
            opt_tol=1e-07,
            memory_size=20,
            enforce_non_negativity=False,
            init_wts_diameter=0.0,
            max_iterations=2147483647,
            sgd_init_tol=0.0,
            quiet=False,
            use_threads=True,
            train_threads=None,
            dense_optimizer=False,
            feature=None,
            label=None,
            weight=None,
            **params):

        if 'feature_column' in params:
            raise NameError(
                "'feature_column' must be renamed to 'feature'")
        if feature:
            params['feature_column'] = feature
        if 'label_column' in params:
            raise NameError(
                "'label_column' must be renamed to 'label'")
        if label:
            params['label_column'] = label
        if 'weight_column' in params:
            raise NameError(
                "'weight_column' must be renamed to 'weight'")
        if weight:
            params['weight_column'] = weight
        BasePredictor.__init__(self, type='regressor', **params)
        core.__init__(
            self,
            normalize=normalize,
            caching=caching,
            l2_weight=l2_weight,
            l1_weight=l1_weight,
            opt_tol=opt_tol,
            memory_size=memory_size,
            enforce_non_negativity=enforce_non_negativity,
            init_wts_diameter=init_wts_diameter,
            max_iterations=max_iterations,
            sgd_init_tol=sgd_init_tol,
            quiet=quiet,
            use_threads=use_threads,
            train_threads=train_threads,
            dense_optimizer=dense_optimizer,
            **params)
        self.feature = feature
        self.label = label
        self.weight = weight

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
