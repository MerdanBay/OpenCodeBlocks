# OpenCodeBlock an open-source tool for modular visual programing in python
# Copyright (C) 2021 Mathïs FEDERICO <https://www.gnu.org/licenses/>

""" Module for the Serializable base class """

from typing import OrderedDict


class Serializable():

    def __init__(self) -> None:
        self.id = id(self)

    def serialize(self) -> OrderedDict:
        raise NotImplementedError()

    def deserialize(self, data:OrderedDict) -> None:
        raise NotImplementedError()
