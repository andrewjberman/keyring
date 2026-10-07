#!/usr/bin/env python3
"""Write the root requirements.txt from the import census (3.0.0_SA_CVO, 2026-10-07).

    python build_requirements.py <import_census.json> <out requirements.txt>

One line per DISTRIBUTION that the workspace's own tracked code imports, pinned to the version installed on the box
the census ran on, with the number of files that import it. Sections are by where the import is used, so a box that
only runs the tooling can stop after the first block. Distributions that tracked code imports but that are NOT
installed on the census box are written as COMMENTED lines: they were never exercised here, so they carry no pin and
are not installed by `pip install -r`. Nothing is taken from memory: every active line is a census row or a RULED
entry below, each with its reason.
"""
from __future__ import annotations

import importlib.metadata as md
import json
import sys

# first-party names that an installed distribution also provides: decided by reading the import lines
RULED_THIRD_PARTY = {"mcp": "mcp", "playwright": "playwright"}       # `from mcp.server.fastmcp`, `from playwright.sync_api`
RULED_FIRST_PARTY = {"coverage", "authorization", "run"}             # data/etfs/scripts/coverage/, local modules
# import names with no distribution on this box that are LOCAL modules reached by a path insert, not packages
LOCAL_NOT_PACKAGES = {"canonical_factor_mapping", "emit_manifest", "narrative_build", "p2base_odh",
                      "security_ticker_mapping_complete", "surgical_repair"}
# tools the gates call as programs; no tracked file imports them
TOOLS = {"ruff": ".tools/commit-gate.sh and safe-commit.sh run it on every .py commit (CLAUDE.md rule 14)",
         "awscli": "the .tools/aws shim forwards to it",
         "pytest-cov": "installed beside pytest; no tracked config requires it"}
SKIP_DISTS = {"pip"}
# Left to the resolver, with the reason printed on the line. MEASURED on the census box by `pip check`: boto3 1.42.54
# and awscli 1.44.44 both require botocore 1.42.54, while botocore 1.43.0 is installed (pulled by aiobotocore 3.7.0 for
# s3fs 2026.6.0, which needs botocore >= 1.42.90). The box's own set is inconsistent, so its three exact pins together
# cannot be installed from a clean start. boto3 and awscli keep their pins (the gates and 1,853 files use them).
UNPINNED = {"botocore": "no pin: boto3 and awscli fix it (1.42.54); the census box holds 1.43.0, which `pip check` reports as a conflict",
            "s3fs": "no pin: 2026.6.0 on the census box needs a botocore that boto3 1.42.54 refuses; the resolver picks one that fits"}
WINDOWS_ONLY = {"pywin32"}
NOT_INSTALLED_NOTES = {
    "blpapi": "Bloomberg API; the terminal machine only; from Bloomberg's own index, not PyPI",
    "moto": "AWS mocks for the opal-gateway acceptance tests",
    "nbclient": "the Bloomberg daily pull runner (integrations/bloomberg); terminal machine",
    "nbformat": "the Bloomberg daily pull runner (integrations/bloomberg); terminal machine",
    "polars": "one Black Diamond gold script (C_00.canonical_performance.py)",
    "opensearchpy": "distribution opensearch-py; one news-scanner utility",
    "mss": "one research-seat screen-capture script",
    "nopecha": "one worker deliverable under AMGT_HARVST",
    "graph_tool": "graph-tool; not on PyPI (conda or a container); infra/aws/c3materialize-b4/run_sbm.py",
}
CORE_AREAS = {".tools", "lib", "org/mcp", "sdk", ".claude/skills", "rcg"}
PIPELINE_AREAS = {"data", "infra/lambda", "infra/other", "integrations"}


def main() -> int:
    census = json.load(open(sys.argv[1], encoding="utf-8"))
    rows = dict(census["third_party"])
    for name in RULED_THIRD_PARTY:
        rows[name] = census["shadowed"][name]
    by_dist, missing = {}, {}
    for name, r in rows.items():
        if name in LOCAL_NOT_PACKAGES:
            continue
        if not r["distributions"]:
            missing[name] = r
            continue
        for dist, ver in r["installed"].items():
            if dist in SKIP_DISTS:
                continue
            e = by_dist.setdefault(dist, {"version": ver, "files": 0, "areas": {}, "imports": []})
            e["files"] += r["files"]
            e["imports"].append(name)
            for a, c in r["by_area"].items():
                e["areas"][a] = e["areas"].get(a, 0) + c
    core, pipeline, other = [], [], []
    for dist, e in by_dist.items():
        areas = set(e["areas"])
        (core if areas & CORE_AREAS else pipeline if areas & PIPELINE_AREAS else other).append(dist)

    def line(dist):
        e = by_dist[dist]
        marker = '; sys_platform == "win32"' if dist in WINDOWS_ONLY else ""
        where = ", ".join("%s %d" % (a, c) for a, c in sorted(e["areas"].items(), key=lambda x: -x[1])[:3])
        imp = "" if [dist.lower().replace("-", "_")] == [i.lower() for i in e["imports"]] else " | import %s" % ", ".join(sorted(e["imports"]))
        if dist in UNPINNED:
            return "%-44s # %d files: %s%s | %s" % (dist, e["files"], where, imp, UNPINNED[dist])
        return "%-44s # %d files: %s%s" % ("%s==%s%s" % (dist, e["version"], marker), e["files"], where, imp)

    d = census["denominators"]
    out = [
        "# Opal Capital (ajb_workspace) -- the Python packages this workspace's own code imports.",
        "# GENERATED, do not hand-edit: org/tier1_exec/3.0.0_SA_CVO/deliverables/REQUIREMENTS_CENSUS/build_requirements.py",
        "# from import_census.py (an `ast` read of every tracked .py file; no code executed).",
        "# Census: %d tracked .py files, %d vendored ones excluded, %d read, %d unparsed; Python %s."
        % (d["tracked_py"], d["excluded_vendored_py"], d["scanned_py"], d["unparsed"], census["python"]),
        "# Every pin is the version installed on the box the census ran on (the laptop), where this code runs today.",
        "# Two lines carry no pin, each with its reason: the laptop's own set fails `pip check` on botocore.",
        "# NOT VERIFIED: that pip resolves this file from a clean start (no install or dry run was made).",
        "# NOT covered: what each Lambda bundles for AWS (its own requirements file beside it); the portal (bun);",
        "# programs that are not Python packages (git, terraform, shellcheck, jq).",
        "#",
        "# Install:  python -m pip install -r requirements.txt     then, for browser automation:  python -m playwright install",
        "",
        "# --- 1. Tooling, shared libraries and the agent broker (.tools, lib, org/mcp, sdk, skills) ---",
    ]
    out += [line(x) for x in sorted(core, key=str.lower)]
    out += ["", "# --- 2. Programs the commit and deploy gates call (no file imports them) ---"]
    for dist, why in TOOLS.items():
        try:
            out.append("%-44s # %s" % ("%s==%s" % (dist, md.version(dist)), why))
        except md.PackageNotFoundError:
            out.append("# %-42s # NOT INSTALLED on the census box: %s" % (dist, why))
    out += ["", "# --- 3. Data pipelines, Lambda sources and their tests (data, infra, integrations) ---"]
    out += [line(x) for x in sorted(pipeline, key=str.lower)]
    out += ["", "# --- 4. Imported only by seat deliverables, deck generation and one-off tools (org, deck_generation, tools) ---"]
    out += [line(x) for x in sorted(other, key=str.lower)]
    out += ["", "# --- 5. Imported by tracked code but NOT INSTALLED on the census box: unpinned, never exercised here ---",
            "# Uncomment a line on the box that needs it."]
    for name, r in sorted(missing.items(), key=lambda kv: -kv[1]["files"]):
        dist = {"opensearchpy": "opensearch-py", "graph_tool": "graph-tool"}.get(name, name)
        out.append("# %-42s # %d files: %s" % (dist, r["files"], NOT_INSTALLED_NOTES.get(name, r["examples"][0])))
    with open(sys.argv[2], "w", encoding="ascii", newline="\n") as fh:
        fh.write("\n".join(out) + "\n")
    print("active lines: core %d, tools %d, pipeline %d, other %d; commented not-installed %d; local modules skipped %d"
          % (len(core), sum(1 for row in out if row.split("==")[0] in TOOLS), len(pipeline), len(other), len(missing),
             len(LOCAL_NOT_PACKAGES)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
