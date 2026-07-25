"""
Canonical spawn-boundary guard for native-Python -> MSYS-linked-binary calls on the Windows fabric.
Import this; do not spawn `grep`/`sed`/`awk`/`find`/`sort`/`xargs` (or any MSYS-linked binary)
directly from native Windows Python via bare `subprocess.run([binary, ...])`.

THE CLASS this closes (CVO~Z, argv echo-back, confirmed not inferred, 2026-07-25 -- third confirmed
member of the native-Python<->MSYS-binary boundary family, sibling to `.tools/aws`'s leading-`/`
mangling and the `--delimiter /` CommonPrefixes silent-empty; see CLAUDE.md's aws-shim/`.tools/aws.cmd`
section for the first two): `subprocess.list2cmdline()` leaves an argv element UNQUOTED on the Windows
command line whenever it contains no whitespace. This box's MSYS-linked binaries, spawned from a
non-MSYS (native Windows Python) parent, then re-parse that raw command line themselves -- and if an
unquoted element contains a backslash TOGETHER WITH any of five glob metacharacters (`* ? [ ( {`), the
MSYS runtime routes it through glob expansion, which DE-ESCAPES every backslash before the target
binary ever sees the argument (`\\s` -> `s`, `\\w` -> `w`). The de-escaped pattern is usually still
syntactically valid, so the binary runs it and HONESTLY reports "no match" -- rc=1 (or whatever the
tool's own empty-result code is), empty stdout, NO stderr: indistinguishable from a genuine empty
result. Independently, `{` alone (with NO backslash) also mangles via brace expansion.

TRIGGER MATRIX (CVO~Z, measured via argv echo-back -- `echo.exe` spawned with the SAME argument,
diffing what arrives against what was sent; grep's own verdict is NOT a valid oracle for this class,
since a de-escaped pattern can still coincidentally match, exactly how this mechanism first evaded
detection):
    backslash + one of `* ? [ ( {`, no whitespace in the arg  -> MANGLED
    `{` present at all (even with no backslash)                -> MANGLED (independent trigger)
    backslash + any of `+ . ^ $ ~`                             -> safe (not glob metachars)
    a glob metachar with NO backslash present                  -> safe (metachar alone is harmless)
    any whitespace present anywhere in the arg                 -> safe (forces Windows-level quoting;
                                                                    the MSYS runtime never reparses it)

FIX: route the WHOLE spawn through `bash -c` (via the estate's canonical `git_bash_resolver`) instead
of invoking the MSYS binary directly. Bash's own argument parsing/quoting resolves and delivers each
argument to the child unmangled -- verified (CVO~Z): the identical pattern that mangled under a direct
native-Python spawn arrived correct through `bash -c`. This makes the hazard UNREPRESENTABLE (the
precondition -- an MSYS binary receiving an unquoted risky argv element from a non-MSYS parent -- simply
never occurs) rather than merely detected-and-patched per call site.

Usage (drop-in for subprocess.run when cmd[0] is or may be an MSYS-linked binary):
    from msys_argv_guard import msys_safe_run
    result = msys_safe_run(["grep", "-rnE", pattern, path], capture_output=True, text=True, timeout=15)
    # NOT subprocess.run(["grep", ...]) directly -- that is the vulnerable call this guard replaces.

Also exports `is_msys_risky(arg)` -- the pure detection predicate, for lint/sweep use (CVO~Z's
estate-wide sweep migrates flagged call sites to `msys_safe_run`, using this predicate to find them).

Self-test: `python .tools/msys_argv_guard.py` -> predicate matrix (9 cases) + a live mutant (a
known-mangling argv arrives INTACT through msys_safe_run, oracle-verified via echo-back, never via a
downstream tool's verdict) + a positive control (a plain call is unaffected).

First isolated 2026-07-25 (0.8.0_AE_CloudComp~A, `comp-types blast` fail-closed follow-on -- caught a
self-introduced false "0 known types" against a REAL, present type before shipping; mechanism confirmed
by 3.0.0_SA_CVO~Z via argv echo-back after ~A's own first-pass attribution under-covered the true
trigger set). CTO~Z-dispatched as the estate-wide gate (20260725T100123Z); CVO~Z's parallel sweep
migrates flagged call sites to this interface. Owner: 0.8.0_AE_CloudComp.
"""
from __future__ import annotations

import shlex
import subprocess
from pathlib import Path

from git_bash_resolver import git_bash

#: The five confirmed glob metacharacters that trigger MSYS de-escaping WHEN a backslash is also
#: present in the same unquoted argv element. `+ . ^ $ ~` are confirmed NOT triggers.
_TRIGGER_METACHARS = frozenset("*?[({")


def is_msys_risky(arg) -> bool:
    """True iff `arg`, passed as an unquoted argv element to an MSYS-linked binary spawned from a
    native-Windows-Python parent, would be silently de-escaped/glob-mangled on this host class --
    the pure detection predicate (module docstring has the full trigger matrix + its grounding).
    Non-string args (e.g. an already-int/Path) are never risky -- str()-coerced by the caller before
    this predicate would ever see them, so False is the correct/only sound answer here."""
    if not isinstance(arg, str):
        return False
    # Whitespace check FIRST (CVO~Z verify finding, 2026-07-25): whitespace forces Windows-level
    # quoting, so MSYS never reparses the element unquoted -- this protects the independent '{'
    # trigger too, not just the backslash+metachar class. Checking '{' before whitespace (the
    # original ordering) made the predicate CONTRADICT its own documented matrix -- '{a, b}' and
    # 'a\s {x}' both false-flagged as risky despite the docstring's own "whitespace -> safe" claim.
    # Fail-safe direction (over-flagging, not a hole), but a gate whose code and documented matrix
    # disagree is its own declarative-drift defect -- fixed here, not left for the next reader to
    # discover which of the two to trust.
    if " " in arg or "\t" in arg:
        return False
    if "{" in arg:
        return True  # independent trigger, no backslash needed (brace expansion)
    return "\\" in arg and any(c in arg for c in _TRIGGER_METACHARS)


def msys_safe_run(cmd: list, **kwargs) -> subprocess.CompletedProcess:
    """Drop-in replacement for subprocess.run(cmd, **kwargs) when cmd[0] is (or may be) an
    MSYS-linked binary (grep, sed, awk, find, sort, xargs, ...) -- makes the class UNREPRESENTABLE
    rather than merely detected: routes the whole call through `bash -c '<shlex-quoted argv>'` via
    the estate's canonical `git_bash_resolver`, instead of spawning the MSYS binary directly.

    ALWAYS routes through bash, whether or not any individual argument is currently risky -- callers
    should use this for every MSYS-binary spawn, not just ones they believe are risky today (a
    binary or a later-added argument nobody thought to re-check is exactly how this class hides;
    see the module docstring's history). `is_msys_risky()` remains available separately for
    lint/sweep use where a call SITE, not a call, needs to be flagged.

    COST (CVO~Z, measured, 2026-07-25): the extra `bash -c` hop adds roughly 2.2x per call versus a
    direct subprocess.run of the MSYS binary (~29.4ms -> ~63.6ms per invocation on this host, single
    grep call). Always-route makes this unavoidable BY DESIGN (see above -- selective routing would
    reopen the classifier-completeness problem this design deliberately avoids). Fine for the
    per-CLI-invocation call shape this was built for; a caller migrating a HOT LOOP that spawns an
    MSYS binary hundreds of times (e.g. per-file in a large tree walk) should know this from here,
    not discover it from wall-clock -- consider batching into fewer, larger invocations rather than
    avoiding the guard.

    `cmd` -- list-form argv ONLY (cmd[0] the binary, the rest its arguments); does not accept a
    pre-built shell string (build the argv list as you normally would for subprocess.run, unquoted --
    this function does the quoting). `**kwargs` forwarded to subprocess.run unchanged
    (capture_output, text, timeout, cwd, env, ...) EXCEPT `shell`, which is rejected -- this helper
    already IS the shell-routing, and a caller-supplied `shell=True` would conflict with it."""
    if kwargs.get("shell"):
        raise ValueError("msys_safe_run already routes through bash -c; do not also pass shell=True")
    bash = git_bash()
    if not bash:
        raise RuntimeError(
            "no Git Bash found (git_bash_resolver); refusing to fall back to a direct, "
            "unguarded MSYS-binary spawn"
        )
    # shlex.quote is LOAD-BEARING, not cosmetic -- do not make it conditional (e.g. "only quote if
    # is_msys_risky(arg)"). Measured (CVO~Z, 2026-07-25): WITHOUT it, 4 of the 5 confirmed trigger
    # shapes reach bash -c unquoted and come back rc=0 with the backslash silently stripped -- the
    # ORIGINAL corruption, reproduced INSIDE this fix (only the `(` shape throws a loud bash syntax
    # error and would tip you off; the other four fail exactly as silently as the bug this guard
    # exists to close). This quoting -- not "bash's own arg parsing" as a separate mechanism -- is
    # what closes hazards A and B; only hazard C (System32-shadowing) is independently closed by
    # bash's own MSYS PATH rewrite. Selective/conditional quoting would make is_msys_risky's
    # completeness load-bearing for CORRECTNESS again, exactly the mistake this module's docstring
    # already explains why "always route" avoids.
    shell_cmd = " ".join(shlex.quote(str(c)) for c in cmd)
    result = subprocess.run([bash, "-c", shell_cmd], **kwargs)
    # A direct subprocess.run(["missing-binary", ...]) raises FileNotFoundError -- LOUD. Routing
    # through bash -c instead reports a missing/misspelled binary as rc=127 -- QUIET, and every
    # migrated call site written as `if result.returncode == 0:` (a real, live pattern found in
    # this estate's own `find` call sites, CVO~Z verify finding 2026-07-25) would then silently
    # read a nonexistent binary as "zero results" -- exactly the silent-empty shape this whole
    # guard exists to eliminate, reintroduced one layer down by the fix itself. Re-raise to
    # preserve the ORIGINAL loud semantics. Confirmed message text (this host, Git-for-Windows
    # bash): "bash: line N: <name>: command not found"; bash's exit code 127 is otherwise a
    # legitimate exit code a real invoked command could return on its own, so both signals
    # (rc==127 AND the message) are required when stderr is inspectable -- only rc==127 alone
    # (stderr not captured by the caller, so unreadable) is treated as inconclusive-but-still-raise,
    # since staying loud is the safer default for a probe that cannot fully verify the cause.
    if result.returncode == 127:
        stderr = result.stderr
        if stderr is None or "command not found" in (
            stderr if isinstance(stderr, str) else stderr.decode(errors="replace")
        ):
            raise FileNotFoundError(
                f"msys_safe_run: {cmd[0]!r} not found via bash -c (rc=127) -- raised to preserve "
                f"the loud subprocess.run(FileNotFoundError) semantics a direct spawn would have "
                f"given; do not catch this as 'zero results'."
            )
    return result


def _find_echo() -> str | None:
    """Self-test only: locate echo.exe near the resolved bash.exe (same MSYS/usr/bin tree)."""
    bash = git_bash()
    if not bash:
        return None
    candidate = Path(bash).parent / "echo.exe"
    return str(candidate) if candidate.is_file() else None


if __name__ == "__main__":
    import sys

    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

    print("=== msys_argv_guard self-test ===")

    # 1-9. detection predicate against CVO~Z's measured trigger matrix, one case per limb.
    chk("1 detect: backslash + '*' -> risky", is_msys_risky(r"a\s*"))
    chk("2 detect: backslash + '(' -> risky", is_msys_risky(r"a\s("))
    chk("3 detect: backslash + '[' -> risky", is_msys_risky(r"a\s["))
    chk("4 detect: backslash + '?' -> risky", is_msys_risky(r"a\s?"))
    chk("5 detect: backslash + '{' -> risky", is_msys_risky(r"a\s{"))
    chk("6 detect: bare '{', NO backslash -> risky (independent trigger)", is_msys_risky("ab{"))
    chk("7 detect: backslash + safe chars (+ . ^ $ ~) -> NOT risky",
        not is_msys_risky(r"a\sb+") and not is_msys_risky(r"a\sb.c")
        and not is_msys_risky(r"^a\sb$") and not is_msys_risky(r"a\s~"))
    chk("8 detect: glob metachar alone, no backslash -> NOT risky",
        not is_msys_risky("ab*") and not is_msys_risky("ab[") and not is_msys_risky("ab("))
    chk("9 detect: whitespace present -> NOT risky (forces Windows-level quoting)",
        not is_msys_risky(r"a\s (x)"))
    chk("9a detect: whitespace protects the INDEPENDENT '{' trigger too (CVO~Z verify finding, "
        "predicate-vs-docstring precision fix -- was a false positive before the ordering fix)",
        not is_msys_risky("{a, b}") and not is_msys_risky(r"a\s {x}") and not is_msys_risky("{x} y"))
    chk("9b detect: '{' with NO whitespace still risky (the ordering fix must not over-correct "
        "into a false negative on the genuine independent trigger)",
        is_msys_risky("{a,b}") and is_msys_risky("ab{"))

    # 10-11. the spawn helper itself: mutant (known-mangling argv arrives INTACT) + positive
    #        control (a plain safe call, unaffected) -- BOTH measured via the echo-back oracle
    #        (what arrived, not the downstream tool's verdict -- the exact substitution that
    #        produced CVO~Z's own false non-reproduction earlier today; not repeated here).
    echo = _find_echo()
    if echo:
        known_mangling = r"export\s+interface\s+(\w+)"
        r = msys_safe_run([echo, known_mangling], capture_output=True, text=True, timeout=10)
        chk("10 mutant: a known-mangling argv arrives INTACT through msys_safe_run (echo-back oracle)",
            r.returncode == 0 and r.stdout.rstrip("\n") == known_mangling)

        safe_arg = "plain-safe-argument"
        r2 = msys_safe_run([echo, safe_arg], capture_output=True, text=True, timeout=10)
        chk("11 positive control: a plain safe call is unaffected through msys_safe_run",
            r2.returncode == 0 and r2.stdout.rstrip("\n") == safe_arg)

        # 12. adversarial: shlex.quote()'s OWN escaping must itself survive the same MSYS boundary
        #     this class lives at -- single/double quotes, backticks, `$`, and a combined
        #     backslash+paren+quote shape (CVO~Z's own follow-up ask, checked before waiting for
        #     the sweep to find it).
        adversarial = [
            "contains'single'quotes",
            "contains`backtick`",
            'contains"double"quotes',
            "contains$dollar${braces}",
            "mixed \\ backslash and 'quote' and (paren)",
        ]
        adv_ok = True
        for a in adversarial:
            ra = msys_safe_run([echo, a], capture_output=True, text=True, timeout=10)
            if not (ra.returncode == 0 and ra.stdout.rstrip("\n") == a):
                adv_ok = False
        chk("12 adversarial: quotes/backticks/$/mixed-backslash-paren-quote all arrive INTACT",
            adv_ok)
    else:
        print("  [SKIP] 10/11/12 -- echo.exe not found near the resolved bash.exe; "
              "mutant/positive-control/adversarial need it")

    # 13. regression (CVO~Z verify finding, 2026-07-25): a missing/misspelled binary must raise
    #     FileNotFoundError, matching direct subprocess.run's own loud semantics -- NOT rc=127
    #     silently returned, which is the exact silent-empty shape this guard exists to eliminate,
    #     reintroduced one layer down by the fix itself.
    raised = False
    try:
        msys_safe_run(["definitely_nonexistent_binary_zzz_9999"], capture_output=True, text=True,
                      timeout=10)
    except FileNotFoundError:
        raised = True
    chk("13 regression: a missing binary raises FileNotFoundError (loud), not a silent rc=127",
        raised)

    n = sum(1 for x in ok if x)
    print(f"--- self-test: {n}/{len(ok)} passed ---")
    sys.exit(0 if n == len(ok) else 1)
