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
    if "{" in arg:
        return True  # independent trigger, no backslash needed (brace expansion)
    if " " in arg or "\t" in arg:
        return False  # whitespace forces Windows-level quoting; MSYS never reparses it unquoted
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
    shell_cmd = " ".join(shlex.quote(str(c)) for c in cmd)
    return subprocess.run([bash, "-c", shell_cmd], **kwargs)


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
    else:
        print("  [SKIP] 10/11 -- echo.exe not found near the resolved bash.exe; "
              "mutant/positive-control need it")

    n = sum(1 for x in ok if x)
    print(f"--- self-test: {n}/{len(ok)} passed ---")
    sys.exit(0 if n == len(ok) else 1)
