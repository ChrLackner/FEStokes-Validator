from webapp_client import AppAccessConfig, AppConfig, ComputeEnvironment

from . import __version__
from .app import FeStokesRePair

_DESCRIPTION = """Evaluator for https://fe-nerd-games.github.io/FEStokesRePair/"""

config = AppConfig(
    name="FE-Stokes RE-Pair",
    version=__version__,
    python_class=FeStokesRePair,
    frontend_pip_dependencies=["netgen", "ngsolve", "scipy", "plotly"],
    frontend_dependencies=[],
    description=_DESCRIPTION,
    compute_environments=[],
    access=AppAccessConfig(),
)
