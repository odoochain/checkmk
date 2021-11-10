#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from contextlib import suppress
from typing import Dict, List, NamedTuple, Tuple, TypedDict

from .agent_based_api.v1 import (
    all_of,
    check_levels,
    contains,
    exists,
    not_contains,
    OIDEnd,
    register,
    render,
    Service,
    SNMPTree,
)
from .agent_based_api.v1.type_defs import CheckResult, DiscoveryResult, StringTable


class CPUInfo(NamedTuple):
    util: float


Section = Dict[str, CPUInfo]


class Params(TypedDict):
    levels: Tuple[float, float]


def parse_cisco_cpu_multiitem(string_table: List[StringTable]) -> Section:
    ph_idx_to_desc = {}
    for idx, desc in string_table[1]:
        if desc.lower().startswith("cpu "):
            desc = desc[4:]
        ph_idx_to_desc[idx] = desc

    parsed = {}
    for idx, util in string_table[0]:
        name = ph_idx_to_desc.get(idx, idx)
        with suppress(ValueError):
            parsed[name] = CPUInfo(util=float(util))
    return parsed


def discover_cisco_cpu_multiitem(section: Section) -> DiscoveryResult:
    for item in section:
        yield Service(item=item)


def check_cisco_cpu_multiitem(item: str, params: Params, section: Section) -> CheckResult:
    value = section[item].util
    yield from check_levels(
        value,
        levels_upper=params["levels"],
        metric_name="util",
        render_func=render.percent,
        boundaries=(0, 100),
        label="Utilization in the last 5 minutes",
    )


register.snmp_section(
    name="cisco_cpu_multiitem",
    detect=all_of(
        contains(".1.3.6.1.2.1.1.1.0", "cisco"),
        not_contains(".1.3.6.1.2.1.1.1.0", "nx-os"),
        exists(".1.3.6.1.4.1.9.9.109.1.1.1.1.2.*"),
    ),
    parse_function=parse_cisco_cpu_multiitem,
    fetch=[
        SNMPTree(
            base=".1.3.6.1.4.1.9.9.109.1.1.1.1",
            oids=[
                "2",  # cpmCPUTotalPhysicalIndex
                "8",  # cpmCPUTotal5minRev
            ],
        ),
        SNMPTree(
            base=".1.3.6.1.2.1.47.1.1.1",
            oids=[
                OIDEnd(),  # OID index
                "1.7",  # entPhysicalName
            ],
        ),
    ],
)


register.check_plugin(
    name="cisco_cpu_multiitem",
    service_name="CPU utilization %s",
    discovery_function=discover_cisco_cpu_multiitem,
    check_default_parameters={"levels": (80.0, 90.0)},
    check_ruleset_name="cpu_utilization_multiitem",
    check_function=check_cisco_cpu_multiitem,
)
