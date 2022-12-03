from __future__ import annotations

# Built-in
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generator, Type
if TYPE_CHECKING:
    from slobypy.react import BaseElement

__all__ = (
    "Component",
)

class Component(ABC):

    def __init__(self, props=None) -> None:
        if props is None:
            self.props = {}
        else:
            self.props = props

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Name of the component.
        """
        pass

    @abstractmethod
    def body(self) -> Generator[Type[BaseElement], None, None]:
        """
        Use the elements here with yield syntax.
        """
        pass

    def render(self):
        """
        Get the component body with html elements and tags.
        """
        return ''.join([element.render() for element in self.body()])

    # noinspection PyMethodMayBeStatic
    def render_js(self):
        """
        Non-mandatory method to render/include the js of the component
        """
        return ""

    def __str__(self) -> name:
        return self.name

    def __repr__(self) -> str:
        return f"Component({self.name})"
