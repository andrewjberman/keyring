"""_compbudget.py -- RULE T's shared budget carrier (NFRA_COMPEFFICACY PRD v0.4 s.4.4 "RULE T's
FORM", landed by 3.0.0_SA_CVO's decision record @790d92c6fa / msg 92932, L4 by 1.0.0_SA_CTO
@19bf1c7322). ONE sibling module, never per-tool copies (build ladder rung 2) -- the whole point
of naming a shared carrier is that fifteen tools re-implementing "print something at expiry"
drift into fifteen dialects, and a grader (or a caller's script) then has to special-case each one.

First application: .tools/comp-find --corpus aws (NFRA_COMPEFFICACY CE-t-1). Any other comp-*
tool bringing a subprocess or a corpus-width-dependent loop under Rule T imports this module for
its budget resolution, its disclosure line, and its two terminal tokens -- so the wording is
enforced by import, not by copy-paste.

THE FORM, verbatim from the PRD (this module is the FORM made executable, not a reinterpretation):
  carrier         --budget <seconds>  >  env COMP_BUDGET_S  >  the tool's documented default
  default         90 s -- BELOW the 120 s outer ceiling, so the tool always speaks before the
                  harness kills it
  unbounded       --budget 0 -> "budget: unbounded (--budget 0)"
  on every run    "budget: <S> s (flag | env COMP_BUDGET_S | default)" -- the SOURCE word travels
                  with the value (a value must carry its claim: CLAUDE.md s.4)
  at expiry       "BUDGET REACHED: <S> s (<source>); scanned <n> of <N> <unit>; results are a
                  PREFIX, not the answer; resume: <tool> <args> --cursor <last-unit>" -- rc stays
                  0 (the LINE is the rejectable state, not the rc)
  on completion   "WITHIN BUDGET: scanned <N> of <N> <unit>; budget: <S> s (<source>), used <t> s"
  cursor          the last FULLY processed unit in the tool's DETERMINISTIC scan order
  subprocesses    every timeout= derives from remaining(); a call that would outlive the budget
                  is DEFERRED in the T-16 always-printed bucket, never silently skipped

TWO INDEPENDENT DISCRIMINATORS (the PRD's own falsifier pair): D1 the token itself (WITHIN BUDGET
vs BUDGET REACHED); D2 "scanned n of N" with n == N vs n < N. Either alone separates a completed
run from a deferred one; a caller greps whichever it prefers.

KILLED-OUTSIDE is the named uncovered member: if the HARNESS kills the process before this module
ever gets to print (a Bash-tool ceiling below the tool's own budget), no line prints at all and
that is indistinguishable from a crash by construction -- mitigated by keeping the default below
120s, never eliminated. This module does not and cannot fix that; it is the harness's ceiling, not
the tool's.
"""
from __future__ import annotations

import os
import time

DEFAULT_BUDGET_S = 90.0
ENV_VAR = "COMP_BUDGET_S"


def fmt(seconds: float) -> str:
    """Print an int-looking float without a trailing '.0' (100.0 -> '100', 0.5 -> '0.5')."""
    if seconds == int(seconds):
        return str(int(seconds))
    return str(seconds)


def resolve_budget(flag_value=None, default_s: float = DEFAULT_BUDGET_S):
    """THE CARRIER, in precedence order: flag > env COMP_BUDGET_S > the tool's own default.

    Returns (budget_s, source). budget_s == 0.0 means UNBOUNDED (the caller decides what
    "unbounded" means for its own subprocess calls -- e.g. timeout=None); this module only
    resolves the VALUE and its source, never the effect.
    Raises ValueError on a non-numeric or negative flag_value -- the caller should report that
    as a usage error (rc 2), not silently fall through to the env/default rung.
    """
    if flag_value is not None:
        v = float(flag_value)
        if v < 0:
            raise ValueError("budget must be >= 0 (0 = unbounded), got %r" % flag_value)
        return v, "flag"
    env_val = os.environ.get(ENV_VAR)
    if env_val not in (None, ""):
        try:
            v = float(env_val)
            if v >= 0:
                return v, "env %s" % ENV_VAR
        except ValueError:
            pass  # an unparseable env value is not this module's error to raise -- fall through
    return default_s, "default"


def disclosure_line(budget_s: float, source: str) -> str:
    """The line every run prints, healthy or not -- 'a value must carry its claim' (CLAUDE.md)."""
    if budget_s == 0:
        return "budget: unbounded (--budget 0)"
    return "budget: %s s (%s)" % (fmt(budget_s), source)


def within_budget_line(n: int, total: int, unit: str, budget_s: float, source: str, used_s: float) -> str:
    return ("WITHIN BUDGET: scanned %d of %d %s; %s, used %s s"
            % (n, total, unit, disclosure_line(budget_s, source), fmt(used_s)))


def budget_reached_line(budget_s: float, source: str, n: int, total: int, unit: str,
                        resume_args: str, cursor: str) -> str:
    return ("BUDGET REACHED: %s s (%s); scanned %d of %d %s; results are a PREFIX, not the "
            "answer; resume: %s --cursor %s" % (fmt(budget_s), source, n, total, unit,
                                                 resume_args, cursor))


def deferred_bucket(k: int, total: int, unit: str, reasons: list) -> list:
    """The T-16 always-printed bucket -- literal PRD wording: 'DEFERRED: k of K <unit>(s) did not
    return -- each names its reason below' (k may be 0; prints on a healthy run too, so absence of
    a deferral is a stated zero, never a silent one). `reasons` is a list of one-line strings, each
    naming the deferred unit and why; len(reasons) should equal k (not asserted here -- the caller
    owns that invariant)."""
    lines = ["DEFERRED: %d of %d %s(s) did not return -- each names its reason below" % (k, total, unit)]
    lines.extend("  " + r for r in reasons)
    return lines


class Clock:
    """Wall-clock remaining() against a resolved budget -- 'every timeout= derives from
    remaining()'. budget_s == 0 (unbounded) makes remaining() always return None, which callers
    should treat as 'no ceiling' (e.g. pass timeout=None to subprocess.run)."""

    def __init__(self, budget_s: float):
        self.budget_s = budget_s
        self.start = time.monotonic()

    def elapsed(self) -> float:
        return time.monotonic() - self.start

    def remaining(self):
        if self.budget_s == 0:
            return None
        return max(0.0, self.budget_s - self.elapsed())
