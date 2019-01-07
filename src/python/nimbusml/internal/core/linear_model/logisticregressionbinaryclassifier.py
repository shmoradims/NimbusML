# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
LogisticRegressionBinaryClassifier
"""

__all__ = ["LogisticRegressionBinaryClassifier"]


from ...entrypoints.trainers_logisticregressionbinaryclassifier import \
    trainers_logisticregressionbinaryclassifier
from ...utils.utils import trace
from ..base_pipeline_item import BasePipelineItem, DefaultSignatureWithRoles


class LogisticRegressionBinaryClassifier(
        BasePipelineItem,
        DefaultSignatureWithRoles):
    """

    Machine Learning Logistic Regression

    .. remarks::
        Logistic Regression is a classification method used to predict the
        value
        of a categorical dependent variable from its relationship to one or
        more
        independent variables assumed to have a logistic distribution. If the
        dependent variable has only two possible values (success/failure),
        then
        the logistic regression is binary. If the dependent variable has more
        than two possible values (blood type given diagnostic test results),
        then the logistic regression is multinomial.

        The optimization technique used for
        ``LogisticRegressionBinaryClassifier`` is the limited memory
        Broyden-Fletcher-Goldfarb-Shanno (L-BFGS). Both the L-BFGS and
        regular
        BFGS algorithms use quasi-Newtonian methods to estimate the
        computationally intensive Hessian matrix in the equation used by
        Newton's method to calculate steps. But the L-BFGS approximation uses
        only a limited amount of memory to compute the next step direction,
        so
        that it is especially suited for problems with a large number of
        variables. The ``memory_size`` parameter specifies the number of past
        positions and gradients to store for use in the computation of the
        next
        step.

        This learner can use elastic net regularization: a linear combination
        of
        L1 (lasso) and L2 (ridge) regularizations. Regularization is a method
        that can render an ill-posed problem more tractable by imposing
        constraints that provide information to supplement the data and that
        prevents overfitting by penalizing models with extreme coefficient
        values. This can improve the generalization of the model learned by
        selecting the optimal complexity in the bias-variance tradeoff.
        Regularization works by adding the penalty that is associated with
        coefficient values to the error of the hypothesis. An accurate model
        with extreme coefficient values would be penalized more, but a less
        accurate model with more conservative values would be penalized less.
        L1
        and L2 regularization have different effects and uses that are
        complementary in certain respects.

        * ``l1_weight``: can be applied to sparse models, when working
          with high-dimensional data. It pulls small weights associated
        features
          that are relatively unimportant towards 0.
        * ``l2_weight``: is preferable for data that is not sparse. It pulls
          large weights towards zero.

        Adding the ridge penalty to the regularization overcomes some of
        lasso's
        limitations. It can improve its predictive accuracy, for example,
        when
        the number of predictors is greater than the sample size. If ``x =
        l1_weight`` and ``y = l2_weight``, ``ax + by = c`` defines the linear
        span of the regularization terms. The default values of x and y are
        both
        ``1``. An agressive regularization can harm predictive capacity by
        excluding important variables out of the model. So choosing the
        optimal
        values for the regularization parameters is important for the
        performance of the logistic regression model.


        **Reference**

            `Wikipedia: L-BFGS <http://en.wikipedia.org/wiki/L-BFGS>`_

            `Wikipedia: Logistic
            regression <http://en.wikipedia.org/wiki/Logistic_regression>`_

            `Scalable
            Training of L1-Regularized Log-Linear Models
            <http://research.microsoft.com/apps/pubs/default.aspx?id=78900>`_

            `Test Run - L1
            and L2 Regularization for Machine Learning
            <https://msdn.microsoft.com/en-us/magazine/dn904675.aspx>`_


    :param normalize: If ``Auto``, the choice to normalize depends on the
        preference declared by the algorithm. This is the default choice. If
        ``No``, no normalization is performed. If ``Yes``, normalization always
        performed. If ``Warn``, if normalization is needed by the algorithm, a
        warning message is displayed but normalization is not performed. If
        normalization is performed, a ``MaxMin`` normalizer is used. This
        normalizer preserves sparsity by mapping zero to zero.

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
        :py:class:`LogisticRegressionClassifier
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        `Types </nimbusml/concepts/types#column-types>`_

    .. index:: models, classification

    Example:
       .. literalinclude:: /../nimbusml/examples/LogisticRegressionBinaryClassifier.py
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
            **params):
        BasePipelineItem.__init__(
            self, type='classifier', **params)

        self.normalize = normalize
        self.caching = caching
        self.l2_weight = l2_weight
        self.l1_weight = l1_weight
        self.opt_tol = opt_tol
        self.memory_size = memory_size
        self.enforce_non_negativity = enforce_non_negativity
        self.init_wts_diameter = init_wts_diameter
        self.max_iterations = max_iterations
        self.sgd_init_tol = sgd_init_tol
        self.quiet = quiet
        self.use_threads = use_threads
        self.train_threads = train_threads
        self.dense_optimizer = dense_optimizer

    @property
    def _entrypoint(self):
        return trainers_logisticregressionbinaryclassifier

    @trace
    def _get_node(self, **all_args):
        algo_args = dict(
            feature_column=self._getattr_role('feature_column', all_args),
            label_column=self._getattr_role('label_column', all_args),
            weight_column=self._getattr_role('weight_column', all_args),
            normalize_features=self.normalize,
            caching=self.caching,
            l2_weight=self.l2_weight,
            l1_weight=self.l1_weight,
            opt_tol=self.opt_tol,
            memory_size=self.memory_size,
            enforce_non_negativity=self.enforce_non_negativity,
            init_wts_diameter=self.init_wts_diameter,
            max_iterations=self.max_iterations,
            sgd_initialization_tolerance=self.sgd_init_tol,
            quiet=self.quiet,
            use_threads=self.use_threads,
            num_threads=self.train_threads,
            dense_optimizer=self.dense_optimizer)

        all_args.update(algo_args)
        return self._entrypoint(**all_args)
