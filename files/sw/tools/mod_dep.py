#!/usr/bin/env python3
import os
from lxml import etree
from collections import namedtuple

from typing import List

PPRZ_SRC = os.getenv("PAPARAZZI_SRC")
PPRZ_HOME = os.getenv("PAPARAZZI_HOME")
if PPRZ_SRC is None:
    PPRZ_SRC = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + "/../../..")
    print("PAPARAZZI_SRC not set. Use {} as paparazzi home.".format(PPRZ_SRC))
if PPRZ_HOME is None:
    PPRZ_HOME = PPRZ_SRC

Module = namedtuple('Module', ['name', 'depends', 'provides'])


def get_modules() -> List[Module]:
    """
    Return all modules
    """
    file_list = os.listdir(PPRZ_SRC + "/conf/modules")
    filtered = filter(lambda x: os.path.splitext(x)[1] == ".xml", file_list)
    modules = []
    for module in filtered:
        file_path = PPRZ_SRC + "/conf/modules/" + module
        root = etree.parse(file_path).getroot()
        module_name = root.attrib['name']
        dep = root.find("dep")
        if dep is None:
            modules.append(Module(name=module_name, depends=[], provides=[]))
        else:
            e_depends = dep.find("depends")
            depends = []
            if e_depends is not None:
                depends = e_depends.text.split(',')

            e_provides = dep.find("provides")
            provides = []
            if e_provides is not None:
                provides = e_provides.text.split(',')

            modules.append(Module(name=module_name, depends=depends, provides=provides))
    return modules


def list_provides() -> List[str]:
    provides = set()
    for module in get_modules():
        provides = provides.union(set(module.provides))
    return list(provides)


def get_dependents(moi: str, modules: List[Module]) -> List[Module]:
    deps = []
    sec = []
    for module in modules:
        if moi in module.depends:
            deps.append(module)
            sec += get_dependents(module.name, modules)
    return deps + sec


if __name__ == '__main__':
    modules = get_modules()
    deps = get_dependents("uart", modules)
    for m in deps:
        pass
        print(m)
    #provides = list_provides()
    #print(provides)
