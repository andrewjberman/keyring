#!/usr/bin/env python3
"""ADHC_COMMITGATE -- consolidated commit-gate runner (ONE python process, not ~6 forks/file).

Replaces .tools/ds-commit-gate.sh's per-file loop of 6 forked python subprocesses
(py_compile, ds-precommit-check.py, ruff, comp_constants_cli.py, manifest_check_cli.py,
log_open_lint.py) with direct in-process calls to the SAME functions each of those scripts'
own CLI wrapper calls -- not a reimplementation of their checks or their output formatting.

WHY THIS IS SAFE FOR PARITY (CTO condition 1): every check below calls the exact same
function the standalone CLI calls (scan_file / cmd_check / cmd_scan / main(argv=[...])) --
none of these inner functions call sys.exit() themselves (confirmed by reading all 5
source scripts; only each script's OWN `if __name__ == "__main__":` guard calls
sys.exit(), which this runner never reaches). So there is no SystemExit to catch and no
import-time side effect to worry about (CTO condition 2) -- this was verified by reading
every one of the 5 scripts top-to-bottom before writing this file, not assumed.

RUFF STAYS A SUBPROCESS (one per file, unchanged from today): the `ruff` PyPI package is a
compiled Rust binary with no stable public Python API for programmatic checks (only a CLI
entry point) -- importing its internal bindings would be fragile and version-coupled against
the CLAUDE.md-pinned ruff==0.15.11 contract. py_compile IS trivially importable (stdlib) and
is consolidated here rather than kept as a subprocess (better than ADHC_COMMITGATE's own
"py_compile may stay distinct if consolidating it isn't straightforward" allowance).

ORDER PRESERVED EXACTLY (per-file, per-check, fail-fast) to guarantee identical pass/fail +
output vs today's gate: py_compile -> ds-precommit-check -> ruff -> comp-constants ->
comp-manifest-check -> log-open-lint for .py; comp-shell (in-scope only) -> comp-manifest-check
for .sh. The first failing check on a file BLOCKS immediately (matching the bash `|| exit 1`
chain) -- files after a blocked file are never reached, exactly as today.

Usage: python .tools/commit_gate_runner.py <file1> [file2 ...]
Exit 0 on clean; exit 1 on the first blocking failure (message on stderr, same text as today).
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import py_compile
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

# Force line-buffering (Python defaults to FULLY buffered when not attached to a TTY, e.g.
# redirected to a file/pipe -- as every real caller of this gate does). Without this, stdout
# writes from the in-process checks (cmd_check/cmd_scan/log_open_lint's own prints) can
# appear AFTER later stderr writes when both streams are merged (2>&1), even though this
# script emits them in the correct order -- an interleaving artifact that does NOT occur
# with today's one-subprocess-per-check design (each subprocess's own stdio is freshly
# flushed at process exit). Verified via the before/after parity fixture set (ADHC_COMMITGATE
# requirement 3) -- this fix was REQUIRED, not precautionary. Newline translation is
# DELIBERATELY left at Python's default (CRLF on Windows) here: text re-emitted from an
# imported check (py_compile's own traceback text, cmd_check's captured stdout, ...) must
# look exactly like a real `python some_script.py` subprocess wrote it -- which is what the
# parity baseline actually does on this platform. `_echo()` below is the separate path for
# THIS wrapper's own bash-`echo`-equivalent lines, which must stay bare-LF (bash's echo does
# not CRLF-translate) -- conflating the two was an earlier bug caught by the parity fixtures.
for _stream in (sys.stdout, sys.stderr):
    # defensive: a test harness or embedding caller may have replaced stdout/stderr with
    # something that doesn't support reconfigure() (e.g. io.StringIO) -- this must not
    # crash a plain `import commit_gate_runner` in that context.
    with contextlib.suppress(AttributeError):
        _stream.reconfigure(line_buffering=True)


def _echo(msg: str, stream) -> None:
    """Write msg + bare LF, bypassing the stream's platform newline translation --
    matches bash's `echo ... [>&2]` exactly (never CRLF, unlike a python subprocess's
    default text-mode stdout on Windows). Use this ONLY for this wrapper's own
    ds-commit-gate-equivalent messages, never for text re-emitted from an imported check."""
    stream.flush()
    stream.buffer.write((msg + "\n").encode("utf-8"))
    stream.buffer.flush()


SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = SCRIPT_DIR.parent
GRAPH_DIR = WORKSPACE / "org" / "modules" / "graph"
COMPPROOF_DIR = GRAPH_DIR / "compproof"

# ds-precommit-check.py has a hyphenated filename -- not a valid `import` identifier,
# so it's loaded via importlib.util (standard technique for a non-module-name .py path).
def _load_hyphenated(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

ds_precommit_check = _load_hyphenated("ds_precommit_check", SCRIPT_DIR / "ds-precommit-check.py")

for _p in (str(GRAPH_DIR), str(COMPPROOF_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import comp_constants_cli   # noqa: E402
import manifest_check_cli   # noqa: E402
import shell_cli            # noqa: E402
import log_open_lint        # noqa: E402
import ses_sender_lint_cli as ses_sender_lint  # noqa: E402

# Rule-16 in-scope path prefixes for the shell scan (mirrors ds-commit-gate.sh _SHELL_SCOPE).
_SHELL_SCOPE = (".tools/", "org/mcp/", "org/threads/", "infra/aws/lambda/ci/", "infra/aws/terraform/")


def _shell_in_scope(f: str) -> bool:
    try:
        rel = os.path.relpath(f, WORKSPACE).replace("\\", "/")
    except ValueError:
        rel = f
    return any(rel.startswith(prefix) for prefix in _SHELL_SCOPE)


def _run_ruff(f: str) -> int:
    """The one subprocess this runner still shells out to (no stable ruff Python API)."""
    proc = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--target-version", "py39", "--extend-select", "FA", f],
        cwd=str(WORKSPACE),
    )
    return proc.returncode


def _comp_constants_check(f: str, config: dict) -> int:
    """Mirrors `comp_constants_cli.py check --file <f>` exactly (same function, same args
    shape) -- captures stdout so a BLOCK can echo it after the wrapper message, matching
    bash's `_cc_out=$(...) || { echo BLOCKED; echo "$_cc_out"; }` (silent on success)."""
    ns = SimpleNamespace(file=f, lane=None)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = comp_constants_cli.cmd_check(ns, config)
    if rc != 0:
        _echo(f"BLOCKED: comp-constants drift detected on {f}", sys.stderr)
        # Re-emitted cmd_check output. bash's `_cc_out=$(...)` strips the subprocess's
        # trailing newline (POSIX command-substitution semantics), then `echo "$_cc_out"`
        # re-appends exactly one bare-LF -- so every EMBEDDED line keeps the subprocess's
        # own CRLF (print(), default translation) but the final line ends bare-LF (_echo's
        # raw write), matching that two-step bash behavior exactly (parity-fixture-caught).
        content = buf.getvalue()
        if content.endswith("\n"):
            content = content[:-1]
        print(content, file=sys.stderr, end="")
        _echo("", sys.stderr)
        return 1
    return 0


_COMPLETENESS_SUBSTRATE_EXACT = (
    "org/modules/graph/graph-call-manifest.yaml",     # tools_index -- registers the tool
    "org/modules/graph/comp-coverage-map.yaml",       # tools[]/meta_tools[] -- sets the role
    "org/modules/graph/comp_capability_provider.py",  # _ROUTABLE_META_ROLES -- opts the role in
    ".tools/comp-which",                              # the router itself (member-3's corpus)
)


def _is_completeness_substrate(f: str) -> bool:
    """True for any staged path that can INTRODUCE a completeness defect.

    Suffix-independent BY DESIGN: the substrate is two YAML files, one .py, the extensionless
    router, and any .tools/comp-* (a new comp-tool -- member 2's trigger). Keying this off the
    file EXTENSION is what made the family unreachable for 3 of its 4 substrate classes.
    """
    n = f.replace("\\", "/")
    if any(n.endswith(s) for s in _COMPLETENESS_SUBSTRATE_EXACT):
        return True
    if n.startswith(".tools/") or "/.tools/" in n:
        tail = n.split(".tools/", 1)[-1]
        return "/" not in tail and (tail.startswith("comp-") or tail.split(".")[0] == "pipescript")
    return False


def _completeness_batch(substrate: list) -> int:
    """ONE cmd_check over the whole commit's substrate (CTO ruling: batch, not per-file).

    Per-file would re-run member-3's full 42-tool sweep once per substrate file. _completeness_-
    invariants() already takes a list, so the corpus bound is computed once for the commit.
    """
    if not substrate:
        return 0
    ns = SimpleNamespace(file=list(substrate), mode=None, completeness_only=True)
    rc = manifest_check_cli.cmd_check(ns)
    if rc == 1:
        _echo("BLOCKED: comp-manifest-check completeness family (registered-implies-reachable / "
              "one-map-home / self-routes)", sys.stderr)
        return 1
    return 0


def _manifest_check_one(f: str) -> int:
    """Mirrors `manifest_check_cli.py check --file <f>` exactly (blocking only on an
    ERROR-class finding in blocking mode, per that script's own config-driven mode).

    `skip_completeness` -- the family is dispatched ONCE, batched, by _completeness_batch();
    running it again per .py file would re-run member-3's 42-tool sweep for every source file
    in the commit.
    """
    ns = SimpleNamespace(file=[f], mode=None, skip_completeness=True)
    rc = manifest_check_cli.cmd_check(ns)
    if rc == 1:
        _echo(f"BLOCKED: comp-manifest-check flagged non-canonical graph access in {f} (blocking mode)", sys.stderr)
        return 1
    return 0


def _log_open_lint_one(f: str) -> int:
    """Mirrors `log_open_lint.py <f>` (no --advisory flag, matching today's non-blocking-off
    invocation) including its own crash-fail-open guard (CTO safeguard 2, replicated here
    since we call main() directly rather than through its `if __name__` top-level guard)."""
    try:
        rc = log_open_lint.main([f])
    except Exception as e:  # noqa: BLE001 -- crash-fail-open, mirrors log_open_lint's own __main__ guard
        _echo(f"WARN (log-open-lint): unexpected error -- failing open, not blocking: {e!r}", sys.stderr)
        rc = 0
    if rc == 1:
        _echo(
            f"BLOCKED: strict-utf8 log read without errors= in {f} -- add errors=\"replace\", or an "
            f"audited '# log-open-ok: <reason>' override. This is the class that bricked COMPLEARN "
            f"corpus load fabric-wide (2026-07).",
            sys.stderr,
        )
        return 1
    return 0


def _ses_sender_lint_one(f: str) -> int:
    """CLAUDE.md Rule 23 (ses-sender-lint TO, 2026-07-07): flag any SES sender not on
    opalinvest.dev -- a Python send_email/send_raw_email Source= literal or EMAIL_FROM/
    SES_SENDER env-default, or a Terraform EMAIL_FROM/SES_SENDER literal. BLOCK mode: the
    check is cheap + deterministic (a hardcoded string literal, no false-positive surface)
    and the failure mode it prevents is a SILENT nondeterministic delivery quarantine
    (the 2026-07-07 partner-etl-ops-alerts incident) -- worth blocking on first sight rather
    than waiting for a WARN to be noticed."""
    try:
        findings = ses_sender_lint.check_file(f)
    except OSError:
        return 0
    if not findings:
        return 0
    for fd in findings:
        _echo(
            f"{fd['file']}:{fd['line']}  non-opalinvest.dev SES sender ({fd['kind']}): {fd['value']!r}",
            sys.stderr,
        )
    _echo(
        f"BLOCKED: {len(findings)} SES sender(s) not on opalinvest.dev in {f} (CLAUDE.md Rule 23) -- "
        f"opalinvest.com is unauthenticated (nondeterministic quarantine risk), opalcapital.com is "
        f"unverified. Use an opalinvest.dev sender.",
        sys.stderr,
    )
    return 1


def _shell_scan_one(f: str) -> int:
    """Mirrors `shell_cli.py scan <f>` exactly (same cmd_scan function -> identical printed
    findings/summary), then the wrapper's own BLOCKED line on an ERROR-class finding."""
    ns = SimpleNamespace(paths=[f], all=False, guard_lookback=shell_cli.GUARD_LOOKBACK_DEFAULT)
    rc = shell_cli.cmd_scan(ns)
    if rc != 0:
        _echo(f"BLOCKED: comp-shell found ERROR-level forbidden utility in {f}", sys.stderr)
        return 1
    return 0


def process_files(files: list[str]) -> int:
    checked = 0
    # comp-constants config loaded ONCE (read-only; re-reading it per file, like the
    # original per-file subprocess did, would be safe too, but this cheap in-process
    # optimization changes nothing observable -- cmd_check never mutates it).
    cc_config = comp_constants_cli._load_config(comp_constants_cli.DEFAULT_CONFIG_PATH)

    # COMPLETENESS SUBSTRATE (NFRA_TOOLCHECK, CTO GO 104602Z). The completeness family lives in
    # manifest_check_cli._completeness_invariants, but the per-suffix dispatch below only ever fed
    # it .py/.sh/.tf -- so a commit that REGISTERS a tool (a YAML manifest/coverage-map edit) or
    # adds a .tools/comp-* (extensionless) never reached it. The gate built to block comp-fedobs
    # and comp-system would not have seen either: both are born by editing YAML. Collected here and
    # dispatched ONCE after the loop (batched -- member-3's corpus bound is computed over the whole
    # commit, not re-run per substrate file at ~38s each).
    substrate = [f for f in files if _is_completeness_substrate(f)]

    for f in files:
        # A DELETION has no file on disk. py_compile/ruff would raise FileNotFoundError -- an
        # UNCAUGHT exception (only PyCompileError is handled), so the gate CRASHED with a traceback
        # instead of deciding, and there was no sanctioned path to commit a .py deletion through
        # the wrapper. A deleted file is not a gate subject: nothing to compile, nothing to lint.
        # (DS~B hit this deleting a driver during EDGES P2; routed by COO~B 2026-07-09. Same
        # crash-instead-of-decide shape as the fail-open-in-disguise found in the family's own
        # scope computation.)
        if not os.path.exists(f):
            continue
        if f.endswith(".py"):
            try:
                py_compile.compile(f, doraise=True)
            except py_compile.PyCompileError as e:
                # order matters for parity: py_compile's OWN traceback prints first (as it
                # would mid-subprocess in the original), the wrapper's BLOCKED line after.
                # print() (not _echo) for e's own text -- matches a real subprocess's
                # default-CRLF-on-Windows traceback text; _echo for the wrapper's own line.
                print(str(e), file=sys.stderr, end="")  # str(e) already ends in '\n'
                _echo(f"BLOCKED: py_compile failed on {f}", sys.stderr)
                return 1

            rc = ds_precommit_check.scan_file(f, verbose=False, strict=False)
            if rc != 0:
                _echo(f"BLOCKED: undefined-name scan failed on {f}", sys.stderr)
                return 1

            rc = _run_ruff(f)
            if rc != 0:
                _echo(f"BLOCKED: ruff check failed on {f}", sys.stderr)
                return 1

            if _comp_constants_check(f, cc_config) != 0:
                return 1

            if _manifest_check_one(f) != 0:
                return 1

            if _log_open_lint_one(f) != 0:
                return 1

            if _ses_sender_lint_one(f) != 0:
                return 1

            checked += 1

        elif f.endswith(".sh"):
            if _shell_in_scope(f):
                if _shell_scan_one(f) != 0:
                    return 1
                checked += 1

            # manifest-check runs on ALL .sh regardless of Rule-16 scope (mirrors bash:
            # this call sits OUTSIDE the _shell_in_scope block) -- does NOT bump `checked`.
            if _manifest_check_one(f) != 0:
                return 1

        elif f.endswith(".tf"):
            # NEW file type for this gate (ses-sender-lint TO, 2026-07-07) -- Terraform
            # doesn't need py_compile/ruff/etc, just the SES-sender scan (requirement 2:
            # Lambda EMAIL_FROM/SES_SENDER env values live in .tf, not .py).
            if _ses_sender_lint_one(f) != 0:
                return 1
            checked += 1
        else:
            continue

    # THE COMPLETENESS FAMILY -- dispatched ONCE, over the whole commit's substrate, AFTER the
    # per-suffix loop. Suffix-independent: this is the call the YAML manifest/coverage-map edits
    # and the extensionless .tools/comp-* files could never reach before, which is why the family
    # was wired for only 1 of its 4 substrate classes. Fail-closed inside cmd_check.
    if _completeness_batch(substrate) != 0:
        return 1
    # Count only substrate files the per-suffix loop did NOT already count, so a provider .py
    # (checked as .py AND as substrate) is reported once, not twice.
    checked += sum(1 for f in substrate if not f.endswith((".py", ".sh", ".tf")))

    _echo(f"OK: pre-commit gate clean for {checked} file(s)", sys.stdout)
    return 0


def main() -> int:
    files = sys.argv[1:]
    return process_files(files)


if __name__ == "__main__":
    sys.exit(main())
