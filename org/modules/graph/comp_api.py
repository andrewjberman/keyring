"""comp_api -- in-process python facade over the comp-tool CLI modules.

F1 / Layer-3 of NFRA_COMPTOOL_USEPATHS (Andrew-direct 2026-06-25). THE KEYSTONE: a python
tool/scorer (e.g. the TO-D3 canon multi-source reconciler) must COMPOSE several comp-* answers,
but on Windows it cannot subprocess the bash-launcher comp-* (FileNotFoundError -- the banked
python-subprocess-bash-launcher limitation). The comp-tools are already bash-launcher -> python
module (comp-pipescript->pipeline_cli, comp-routes->routes_cli, comp-iam->iam_cli,
pipescript->pipescript_cli; comp-freshness/comp-which are already pure python). So composition needs
NO subprocess at all -- import + call those modules IN-PROCESS. This facade exposes that.

Two tiers:
  1. STRUCTURED accessors (preferred) -- return the model OBJECT directly from each module's
     data-builder (_build_rt / load / _build / _build_dag), bypassing the print/cmd_ layer.
     Use these when you want data, not text: routes(), pipescript_threads(), iam_analysis(),
     pipeline_dag().
  2. run(tool, argv) -- universal in-process CLI invocation with stdout captured -> returns text.
     The Windows-safe "run any comp-tool from python" path for the cmd_-only surfaces (io/deployed/
     resource) that don't yet expose a clean data-return. No subprocess, no bash.

Read-only: every wrapped builder is a read-path (graph/source/json reads). ASCII-only.

Usage (python, no subprocess):
    from comp_api import routes, pipescript_threads, run
    rt = routes()                          # RouteTable model: rt.behaviors, ...
    threads = pipescript_threads()         # the named-thread dict
    io_text = run("comp-pipescript", ["io", "INF_D_04"])   # captured text, in-process
"""
from __future__ import annotations

import contextlib
import importlib
import inspect
import io
import os
import sys

_GRAPH_DIR = os.path.dirname(os.path.abspath(__file__))  # org/modules/graph
if _GRAPH_DIR not in sys.path:
    sys.path.insert(0, _GRAPH_DIR)

# comp-tool name (and its CLI alias) -> the python module under org/modules/graph
_MODULES = {
    "comp-pipescript": "pipeline_cli",
    "pipescript": "pipescript_cli",
    "comp-routes": "routes_cli",
    "comp-iam": "iam_cli",
}


def _import(mod_name: str):
    return importlib.import_module(mod_name)


def run(tool: str, argv=None) -> str:
    """Run a comp-tool's CLI IN-PROCESS (no subprocess) and return its captured stdout.

    tool: a key of _MODULES ('comp-pipescript', 'pipescript', 'comp-routes', 'comp-iam').
    argv: list of CLI args WITHOUT the tool name, e.g. ['io', 'INF_D_04'].
    Windows-safe (no bash launcher). SystemExit from argparse is swallowed.
    """
    if tool not in _MODULES:
        raise ValueError("comp_api.run: unknown tool %r (known: %s)" % (tool, sorted(_MODULES)))
    mod = _import(_MODULES[tool])
    if not hasattr(mod, "main"):
        raise AttributeError("comp_api.run: %s has no main()" % _MODULES[tool])
    args = list(argv or [])
    buf = io.StringIO()
    _saved_argv = sys.argv
    sys.argv = [tool] + args
    try:
        with contextlib.redirect_stdout(buf):
            # Two entry conventions: main(argv) (pipescript_cli) vs main() reading sys.argv (rest).
            try:
                if len(inspect.signature(mod.main).parameters) >= 1:
                    mod.main(args)
                else:
                    mod.main()
            except SystemExit:
                pass
    finally:
        sys.argv = _saved_argv
    return buf.getvalue()


# --- STRUCTURED accessors (the model objects -- preferred over run() for composition) ----------

def routes():
    """The CloudFront/route model (routes_cli._build_rt()). Has .behaviors etc. -- the source for
    AUTH-canon shape + auth-edge deviations (comp-routes use-path)."""
    return _import("routes_cli")._build_rt()


def routes_behaviors():
    """The CloudFront behaviors list directly (each: .path_pattern, .origin_id, .has_auth, ...)."""
    return list(getattr(routes(), "behaviors", []))


def pipescript_threads():
    """The named-thread estate dict (pipescript_cli.load()) -- producer->served->consumer lineage."""
    return _import("pipescript_cli").load()


def iam_analysis():
    """The IAM analysis model (iam_cli._build()) -- roles/perms/gaps, condition-aware caveats apply."""
    return _import("iam_cli")._build()


def pipeline_dag(pipeline: str = "bd-gold"):
    """The gold-pipeline DAG (pipeline_cli._build_dag(pipeline)) -- io/feeds/consumers structure."""
    return _import("pipeline_cli")._build_dag(pipeline)


# --- convenience captured-text wrappers for the common cmd_-only surfaces ----------------------

def pipescript_io(script: str) -> str:
    """comp-pipescript io <script> -- column-gaps + consumers, in-process text."""
    return run("comp-pipescript", ["io", script])


def pipescript_deployed(script: str = None) -> str:
    """comp-pipescript deployed [script] -- MATCH/STALE/MISSING, in-process text."""
    return run("comp-pipescript", ["deployed"] + ([script] if script else []))


def routes_behaviors_text() -> str:
    """comp-routes behaviors -- the full CF behavior list as text (when the model isn't enough)."""
    return run("comp-routes", ["behaviors"])
