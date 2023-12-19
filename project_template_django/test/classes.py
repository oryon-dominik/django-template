from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExpectedClosureContract:
    """
    Dataclass for wrapping the expected *result* for any given functions contract (it's input args + kwargs)
    """

    args: tuple | list = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)
    expected: Any = None

    def __post_init__(self):
        if isinstance(self.args, list):
            self.args = tuple(self.args)
