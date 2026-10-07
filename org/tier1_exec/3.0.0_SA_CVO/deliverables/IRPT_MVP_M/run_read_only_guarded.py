#!/usr/bin/env python3
"""Run another seat's read script UNCHANGED, with every AWS call that is not a read refused in-process.

    python run_read_only_guarded.py <script.py> [the script's own arguments ...]

WHY. A read script that calls a producer's build function reaches code this seat cannot read to the end before running it
(`1.0.0_SA_CTO` msg 106211: "if a put, copy, delete or invoke is reachable, do not run it"). Reading the source says what
the author meant; this guard says what the process may do. It wraps botocore's one call path
(`BaseClient._make_api_call`), so it covers every client and resource of every service created in the process,
whoever creates it. An operation whose name does not start with one of READ_PREFIXES raises before any request is sent.
Each allowed call is counted; the counts and any refusal are printed at the end. Nothing in the target script is edited.

COST: one function wrap; no extra AWS call. NON-APPLICATION: local file writes (a temp file, the script's own --out) are
not AWS calls and are not guarded.
"""
from __future__ import annotations

import collections
import runpy
import sys

import botocore.client

READ_PREFIXES = ("Get", "List", "Head", "Describe", "BatchGet", "Query", "Scan", "Select")
CALLS = collections.Counter()
REFUSED = []
_real = botocore.client.BaseClient._make_api_call


class WriteRefused(RuntimeError):
    pass


def _guarded(self, operation_name, api_params):
    service = self.meta.service_model.service_name
    if not operation_name.startswith(READ_PREFIXES):
        REFUSED.append("%s:%s" % (service, operation_name))
        raise WriteRefused("REFUSED by run_read_only_guarded.py: %s:%s is not a read; nothing was sent"
                           % (service, operation_name))
    CALLS["%s:%s" % (service, operation_name)] += 1
    return _real(self, operation_name, api_params)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    botocore.client.BaseClient._make_api_call = _guarded
    target = sys.argv[1]
    sys.argv = sys.argv[1:]
    rc = 0
    try:
        runpy.run_path(target, run_name="__main__")
    except SystemExit as exc:
        rc = exc.code if isinstance(exc.code, int) else (0 if exc.code is None else 1)
    finally:
        print("GUARD: AWS calls allowed, by operation: %s" % dict(sorted(CALLS.items())))
        print("GUARD: AWS calls refused: %s" % (REFUSED or "none"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
