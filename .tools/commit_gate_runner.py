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
comp-manifest-check -> log-open-lint for .py; bash -n (ALL .sh) -> comp-shell (in-scope only) -> comp-manifest-check
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


def _gao_name() -> str:
    """The git-author-override audit log name for THIS box: one file per box (shape (a), MSTR consensus 2026-10-11),
    the legacy shared name when AGENTBUS_DEVICE is unset or malformed."""
    dev = os.environ.get("AGENTBUS_DEVICE", "").strip()
    ok = bool(dev) and all(c in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in dev)
    return "git-author-override-audit.%s.log" % dev if ok else "git-author-override-audit.log"


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
from git_bash_resolver import git_bash  # noqa: E402
from msys_argv_guard import msys_safe_run  # noqa: E402

# Rule-16 in-scope path prefixes for the shell scan (mirrors ds-commit-gate.sh _SHELL_SCOPE).
_SHELL_SCOPE = (".tools/", "org/mcp/", "org/threads/", "infra/aws/lambda/ci/", "infra/aws/terraform/")


def _shell_in_scope(f: str) -> bool:
    try:
        rel = os.path.relpath(f, WORKSPACE).replace("\\", "/")
    except ValueError:
        rel = f
    return any(rel.startswith(prefix) for prefix in _SHELL_SCOPE)


def _run_ruff(f: str) -> int:
    """The one subprocess this runner still shells out to (no stable ruff Python API).

    TWO ROOTS HAD TO BE MADE TO AGREE. This subprocess runs with cwd=WORKSPACE so ruff
    resolves the workspace config identically for every caller -- but `f` arrives RELATIVE
    TO THE CALLER'S cwd, which is where every other check in this runner reads it. Any
    invocation from a SUBDIRECTORY therefore handed ruff a path resolved against the wrong
    root, and ruff reported the miss as E902 "The system cannot find the path specified"
    AT LINE 1 COLUMN 1 OF A FILE THAT IS FINE.

    THAT PRESENTATION IS THE REAL COST: an IO error wearing a lint finding's clothes sends
    the author looking for a lint problem in correct code, while a bare `ruff check` on the
    same file passes -- the gate and the direct run disagree, and only the gate is right
    that something is wrong, while being wrong about what. Re-anchor to WORKSPACE here.

    Found by 0.4.0_DE_ClientPlatform~Z on a portal-submodule .py (msg 9880), with a
    same-file/two-cwds discriminating test. Their report scoped it to the submodule; the
    class is ANY subdirectory -- measured 2026-08-27 on a plain workspace subdir, no
    submodule involved.
    """
    target = os.path.abspath(f)
    try:
        # Prefer the workspace-relative form so ruff's diagnostics stay readable and
        # identical to what root-invoked callers have always seen.
        target = os.path.relpath(target, str(WORKSPACE))
    except ValueError:
        # Windows: relpath across drives is impossible. The absolute path is still correct
        # under cwd=WORKSPACE -- only the diagnostic prefix gets longer.
        pass
    proc = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--target-version", "py39", "--extend-select", "FA", target],
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


def _is_routing_surface(n: str) -> bool:
    """A HUD / prompt / skill -- the surfaces that ROUTE an agent to a tool.

    MIRRORS manifest_check_cli._is_routing_surface EXACTLY, and the two must not drift: this
    predicate decides what REACHES the family, that one decides what gets SCANNED. A file that
    is substrate here but not a surface there is a wasted family run; a file that is a surface
    there but not substrate here is INVISIBLE -- which is precisely the state that existed until
    2026-08-06.

    Until then NO routing surface was substrate at all, so the retired-alias member's citation
    check ran on ZERO files on every commit while printing PASS. Exercised before the fix: fed a
    citing skill file directly it returns rc=1 and names the tool; a real commit staging four
    citing files produced substrate=[] and rc=0. It had never fired, while CLAUDE.md Rule 20
    cites it verbatim as the thing that polices exactly this.

    SCOPE, deliberately narrow: this makes a commit TOUCHING one of these files run the check on
    THAT FILE. It is not an estate sweep and it does not gate unrelated work -- a clean skill
    commit scans itself, finds nothing, and passes. The estate-wide read lives in the human-facing
    `comp-manifest-check retired-alias` subcommand, which blocks nothing.
    """
    return (n.endswith(".tools/hooks/comp-tool-hud.sh")
            or n.endswith("/prompt.md") or n == "prompt.md"
            or "/.claude/skills/" in "/" + n)


def _is_completeness_substrate(f: str) -> bool:
    """True for any staged path that can INTRODUCE a completeness defect.

    Suffix-independent BY DESIGN: the substrate is two YAML files, one .py, the extensionless
    router, and any .tools/comp-* (a new comp-tool -- member 2's trigger). Keying this off the
    file EXTENSION is what made the family unreachable for 3 of its 4 substrate classes.
    """
    n = f.replace("\\", "/")
    if any(n.endswith(s) for s in _COMPLETENESS_SUBSTRATE_EXACT):
        return True
    if _is_routing_surface(n):
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


# VENDORED TREES -- never gate-subjects. THIS EXCLUSION IS LOAD-BEARING: without it, shebang-aware
# dispatch starts linting pip, pygmentize, tqdm and every other console-script in a venv/lambda
# bundle. We do not own that code, ruff has never seen it, and blocking a commit on it would be a
# fabric-wide halt caused by a vendored file.
#
# STRUCTURAL, NOT NAME-BASED (CTO GO 20260709T122537Z, forward-hardening). The first cut used a
# path-marker DENYLIST -- ("/bin/", "/package/", ...) -- which is itself a PROXY for "we don't own
# this code". Demonstrated hole: a first-party tool at `.tools/bin/comp-future` or
# `org/modules/graph/package/comp_future` was SILENTLY EXCLUDED, because the marker matched while
# ownership did not. `/bin/` and `/package/` are entirely ordinary directory names; `/package/` was
# in that list only because one vendored lambda bundle happens to use it. One `mkdir bin/` from a
# silent coverage hole -- the same silent-coverage-loss class as the ordering bug caught in the
# predicate below.
#
# So bind the PROPERTY: a tree is vendored when it is PACKAGE-MANAGED, evidenced by an artifact only
# a package manager creates --
#     * an ancestor holding `pyvenv.cfg`      (a virtualenv)
#     * an ancestor holding any `*.dist-info` (a pip-installed bundle: the lambda `package/` dirs)
#     * an ancestor literally named `site-packages` or `node_modules`
# Grounded prove-the-universe: all 97 tracked python files under the old name-markers are captured by
# these three signals; 0 unidentifiable. No first-party file is.
#
# FAILS-SAFE-TOWARD-INCLUSION (CTO's design invariant, not a nice-to-have): any uncertainty --
# unreadable dir, unknown layout -- resolves to NOT-vendored, i.e. the file IS gated. A misconfig
# therefore over-INCLUDES (loud: a commit blocks and someone investigates) and can never silently
# exclude (invisible: a file quietly stops being checked). That asymmetry is exactly why the
# denylist was the wrong shape.
_VENDOR_DIRNAMES = ("site-packages", "node_modules")
_vendor_cache: dict = {}


def _dir_is_vendor_root(d: str) -> bool:
    if d in _vendor_cache:
        return _vendor_cache[d]
    try:
        if os.path.basename(d) in _VENDOR_DIRNAMES:
            hit = True
        elif os.path.isfile(os.path.join(d, "pyvenv.cfg")):
            hit = True
        else:
            hit = any(n.endswith(".dist-info") for n in os.listdir(d))
    except OSError:
        hit = False          # fails-safe: uncertainty -> NOT vendored -> the file is gated
    _vendor_cache[d] = hit
    return hit


def _is_vendored(f: str) -> bool:
    """True only when a PACKAGE MANAGER owns the tree. Never inferred from a directory's name."""
    d = os.path.dirname(f.replace("\\", "/"))
    seen = 0
    while d and d not in (".", "/") and seen < 40:
        if _dir_is_vendor_root(d):
            return True
        parent = os.path.dirname(d)
        if parent == d:
            break
        d, seen = parent, seen + 1
    return False


def _is_python_source(f: str) -> bool:
    """True when the gate should treat `f` as Python.

    THE DEFECT THIS CLOSES: the dispatch keyed on `f.endswith(".py")` -- the FILENAME (a proxy) --
    for "this file is Python" (the property). Every extensionless python-by-shebang script therefore
    bypassed py_compile / ruff / the AST scan entirely. 28 such files are tracked; 14 are first-party
    .tools/ scripts including comp-which (the mandated router) and THREE gates (comp-routable-check,
    comp-coverage-check, comp-kit-striplist-gate). It hid live violations -- comp-honesty's E401+E702
    and loop-quiescence's F541, the latter being the exact rule of the 18c92b9ac audited bypass whose
    remediation was certified "closed". CLAUDE.md Rule 14 says "every .py edit passes commit-gate";
    the gate must key on what the file IS, not what it is named.

    STRICTLY ADDITIVE. A `.py` file keeps its existing treatment UNCONDITIONALLY -- including a
    vendored one, which the old `f.endswith(".py")` already gated. Applying the vendored exclusion to
    `.py` as well would have QUIETLY REMOVED 87 files from enforcement while this change advertised
    itself as widening it (measured: gate saw 4769 .py before; a vendored-first predicate saw 4697).
    Narrowing a gate inside a commit that claims to widen it is precisely the kind of silent
    coverage loss these gates exist to prevent. So: the exclusion guards ONLY the new shebang path,
    where the danger lives (vendored console-scripts -- pip, pygmentize, tqdm -- are extensionless).
    """
    if f.endswith(".py"):
        return True                  # unchanged from the pre-existing dispatch; never narrowed
    if _is_vendored(f):
        return False                 # the new shebang path only: do not start linting pip
    if not os.path.isfile(f):        # a deletion: nothing to read, and the loop skips it anyway
        return False
    if os.path.splitext(f)[1]:       # any other extension (.sh/.tf/.md/...) keeps its own dispatch
        return False
    try:
        with open(f, "rb") as fh:
            first = fh.readline(256)
    except OSError:
        return False
    return first.startswith(b"#!") and b"python" in first.lower()


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


def _nonascii_lint_one(f: str) -> int:
    """CLAUDE.md Code Quality: no non-ASCII in production code, logs, or anything that runs on
    AWS -- the rule names this failure by name ("breaks CloudWatch/charmap, grep, CI stdout").

    WARN-ONLY (announce-then-enforce). Always returns 0: it must not block a commit while it
    beds in, and a new gate that can block every agent in the fabric is not something to ship
    unexercised at first sight.

    SCOPE: authored .sh/.py under infra/** and .tools/** -- the paths whose output crosses into
    AWS/CI/Windows-console encoding boundaries.

    >> THE HONEST LIMIT, AND IT MUST TRAVEL WITH THIS CHECK: THIS CANNOT CATCH THE DEFECT THAT
    MOTIVATED IT. Measured 2026-07-31 -- an m365-gateway deploy stranded its EC2_MANIFEST.json
    leg (Rule 8 source-of-truth left asserting the PREVIOUS commit while new code ran) because
    pip drew 40x U+2501 on the REMOTE box and those bytes crossed into a cp1252 stdout via SSM
    StandardOutputContent. BOTH scripts involved were already ASCII-clean and always had been.
    A SCANNER POINTED ONLY AT YOUR OWN FILES CANNOT SEE THE FAILURE THAT ARRIVES IN SOMEONE
    ELSE'S OUTPUT. The other limb -- constraining what THIRD-PARTY tools emit into a channel
    that crosses an encoding boundary (e.g. `pip --progress-bar off`) -- is the real control,
    and this check is NOT it. Do not record this gate as closing that class. <<
    """
    try:
        norm = f.replace("\\", "/")
        if not (norm.startswith("infra/") or norm.startswith(".tools/")):
            return 0
        if _is_vendored(f):
            return 0
        raw = Path(f).read_bytes()
    except Exception:  # noqa: BLE001 -- fail open; a lint must never break the gate
        return 0

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        _echo(f"WARN (non-ascii): {f} is not valid UTF-8 -- not scanned.", sys.stderr)
        return 0

    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        bad = {ch for ch in line if ord(ch) > 127}
        if bad:
            hits.append((lineno, sorted(bad, key=ord)))
    if not hits:
        return 0

    shown = hits[:5]
    for lineno, chars in shown:
        cps = " ".join(f"U+{ord(c):04X}" for c in chars[:6])
        _echo(f"  {f}:{lineno}  non-ASCII: {cps}", sys.stderr)
    if len(hits) > len(shown):
        _echo(f"  ... and {len(hits) - len(shown)} more line(s)", sys.stderr)
    _echo(
        f"WARN (non-ascii): {len(hits)} line(s) in {f} carry non-ASCII (CLAUDE.md Code Quality). "
        f"Use OK:/WARN:/ERROR:/SKIP:/BLOCKED:. WARN-only for now -- not blocking.",
        sys.stderr,
    )
    return 0


def _bash_syntax_check_one(f: str) -> int:
    """`bash -n <f>` -- parse-only syntax check, run on EVERY .sh whatever its path (ZC-2).

    WHY THIS IS NOT comp-shell WIDENED, which the TO forbids: comp-shell answers a
    LOCAL-RUNTIME question -- does this script use a utility Git Bash 3.6.7 lacks (CLAUDE.md
    Rule 16) -- and its path scope is CORRECT, because an EC2 script is not a Git Bash
    subject. `bash -n` answers a DIFFERENT question that has no scope at all: is this file
    parseable as bash. A syntax error is a defect everywhere the file runs, on every host,
    so this check is deliberately scope-free while _SHELL_SCOPE is left byte-unchanged.

    FAILS LOUD, NEVER OPEN. If Git Bash cannot be resolved this BLOCKS rather than recording
    a check that did not run -- recording an unrun check is the exact class the zero-check
    refusal below exists to close, and it would be absurd to reopen it here.

    Spawns through msys_argv_guard.msys_safe_run per CLAUDE.md (native Python -> MSYS binary),
    which routes the argv through `bash -c` with shlex quoting so a path carrying a glob
    metacharacter cannot be de-escaped into a different argument.

    COST: ~64 ms per .sh (the guard's measured ~2.2x on a ~29 ms direct spawn), paid only on
    files this gate already dispatches. NON-APPLICATION: nothing that is not a .sh.
    """
    bash = git_bash()
    if not bash:
        _echo("BLOCKED (bash -n): no Git Bash resolved -- refusing to record a syntax check "
              f"that did not run on {f}", sys.stderr)
        return 1
    r = msys_safe_run([bash, "-n", f], capture_output=True, text=True)
    if r.returncode != 0:
        _echo(f"BLOCKED (bash -n): {f} is not syntactically valid bash:", sys.stderr)
        for line in (r.stderr or "").strip().splitlines():
            _echo(f"    {line}", sys.stderr)
        return 1
    _echo(f"OK: bash -n syntax-checked {f}", sys.stdout)
    return 0


def _shell_scan_one(f: str) -> int:
    """Mirrors `shell_cli.py scan <f>` exactly (same cmd_scan function -> identical printed
    findings/summary), then the wrapper's own BLOCKED line on an ERROR-class finding."""
    ns = SimpleNamespace(paths=[f], all=False, guard_lookback=shell_cli.GUARD_LOOKBACK_DEFAULT)
    rc = shell_cli.cmd_scan(ns)
    if rc != 0:
        _echo(f"BLOCKED: comp-shell found ERROR-level forbidden utility in {f}", sys.stderr)
        return 1
    return 0


# ---------------------------------------------------------------------------
# OVERSIZE REFUSAL (CTO exception 2026-07-14, via COO). GitHub's pre-receive hook
# hard-rejects any blob >100MB. A commit carrying one is STRUCTURALLY UNPUSHABLE:
# not "risky", not "discouraged" -- it can never reach origin, and the only remedy
# is a history rewrite, which on a shared branch needs a sovereign override.
#
# THE INCIDENT (2026-07-14): a 685MB terraform provider .exe was swept into a
# commit from an un-ignored .terraform/ cache. It froze CLOUD for EVERY agent and
# cost an Andrew-authorized history rewrite. It passed commit-gate and
# comp-surface-check IN SILENCE -- this runner RECEIVED the path and ran ZERO
# checks on it, because the per-suffix dispatch below has no branch for .exe, so
# it printed "clean for 0 file(s)" and exited 0.
#
#   >> THE ONLY THING THAT STOPPED IT WAS GITHUB'S LIMIT. We were saved by someone
#      else's control. This check is ours. <<
#
# It is deliberately the least alarm-like control that exists: it mirrors an
# EXTERNAL HARD CONSTRAINT exactly (100MB, GitHub's number, not a taste), so it
# requires ZERO judgment and has no threshold to argue about. It cannot false-alarm
# on anything that would have pushed successfully.
#
# SUFFIX-INDEPENDENT BY DESIGN -- it runs BEFORE the per-suffix dispatch, on every
# file. Scoping it to known suffixes would rebuild the exact blind spot that let the
# .exe through: the gate must not be able to miss a type nobody thought of.
#
# OVERRIDE (audited, mirrors SAFE_COMMIT_ALLOW_SENSITIVE -- a binary cannot carry an
# inline `# never-override:` comment, so the reason travels by env):
#     COMMIT_GATE_ALLOW_LARGE="<reason>" .tools/safe-commit.sh ...
# Audited ONLY when it actually SUPPRESSED A REAL BLOCK (RV-0048 F-020: a log that
# records overrides which never suppressed anything is theater in an audit trail's
# clothes). COMMIT_GATE_AUDIT routes the test suite's records to a scratch file so
# the suite cannot poison the governance log it is meant to protect (same F-020).
# ---------------------------------------------------------------------------
MAX_FILE_BYTES = 100 * 1024 * 1024  # GitHub's pre-receive hard limit, exactly.


def _check_file_size(f: str) -> int:
    """0 = pass (silent). 1 = BLOCK. Runs on EVERY file, whatever its suffix."""
    try:
        size = os.path.getsize(f)
    except OSError:
        return 0  # unreadable/vanished -- not this check's business
    if size < MAX_FILE_BYTES:
        return 0

    mb = size / (1024 * 1024)
    reason = os.environ.get("COMMIT_GATE_ALLOW_LARGE", "").strip()
    if reason:
        # THE OVERRIDE'S LEGALITY IS CONDITIONED ON ITS AUDIT. So if the audit
        # cannot be written, the condition is UNMET and the override is REFUSED --
        # it does NOT fail open (COO review 2026-07-14). "override set -> real block
        # suppressed -> audit write fails -> pass silently" is an UNAUDITED
        # SUPPRESSION OF A REAL BLOCK, the F-020 class one layer deeper, delivered
        # on the failure path nobody tests. Refusing loudly when the log is
        # unwritable is not a crash -- it is the condition doing its job.
        if not _audit_oversize(f, size, reason):
            _echo("", sys.stderr)
            _echo(f"BLOCKED: {f} is {mb:.1f}MB and the override could NOT be "
                  "audited.", sys.stderr)
            _echo("  The large-file override is legal ONLY when it is recorded. "
                  "The audit log at", sys.stderr)
            _echo(f"  {_audit_path()} is not writable -- fix that first, then "
                  "retry.", sys.stderr)
            _echo("  An override that leaves no record is exactly what the audit "
                  "exists to prevent.", sys.stderr)
            return 1
        _echo(f"WARN: oversize file ALLOWED by audited override: {f} "
              f"({mb:.1f}MB) reason={reason}", sys.stderr)
        return 0

    _echo("", sys.stderr)
    _echo(f"BLOCKED: {f} is {mb:.1f}MB -- at or over GitHub's 100MB limit.",
          sys.stderr)
    _echo("  This commit could NEVER be pushed: GitHub's pre-receive hook "
          "rejects any blob >100MB,", sys.stderr)
    _echo("  and the only remedy after the fact is a HISTORY REWRITE of a "
          "shared branch.", sys.stderr)
    _echo("", sys.stderr)
    _echo("  UNSTAGE IT:", sys.stderr)
    _echo(f"      git reset -q HEAD -- {f}", sys.stderr)
    _echo("", sys.stderr)
    hint = _ignore_suggestion(f)
    if hint:
        _echo("  IF IT IS BUILD/TOOL OUTPUT (a provider cache, a venv, a zip, a "
              "model file), IGNORE IT:", sys.stderr)
        _echo(f"      echo '{hint}' >> .gitignore", sys.stderr)
    else:
        _echo("  This looks like SOURCE, not build output -- so do NOT reach for "
              ".gitignore.", sys.stderr)
        _echo("  A source file this large is almost always data that got pasted "
              "into it, or a", sys.stderr)
        _echo("  generated file in a source file's clothing. Look at it before "
              "you do anything.", sys.stderr)
    _echo("", sys.stderr)
    _echo("  IF IT IS DELIBERATE, the override is AUDITED:", sys.stderr)
    _echo('      COMMIT_GATE_ALLOW_LARGE="<reason>" .tools/safe-commit.sh ...',
          sys.stderr)
    return 1


#: Suffixes we will suggest ignoring by GLOB. Deliberately a SHORT ALLOWLIST of
#: things that are always build/tool output. NEVER a source suffix.
#:
#: The first version of this returned f"*{suffix}" for anything -- so an oversize
#: .py produced the remediation `echo '*.py' >> .gitignore`, which would have
#: untracked EVERY PYTHON FILE IN THE REPO. A gate that hands you a
#: repo-destroying command as its "help" is worse than a gate that says nothing:
#: the block is what earns your trust, and then you follow the advice. Caught by
#: reading the test's own output instead of just its OK column.
_IGNORABLE_SUFFIXES = {".exe", ".dll", ".so", ".dylib", ".zip", ".tar", ".gz",
                       ".7z", ".rar", ".jar", ".whl", ".pkl", ".pickle", ".bin",
                       ".pt", ".pth", ".onnx", ".h5", ".model", ".iso", ".dmg",
                       ".mp4", ".mov", ".parquet"}

#: Directories that are always tool output, whatever they contain.
_CACHE_DIRS = {"node_modules", "venv", ".venv", "dist", "build", "__pycache__",
               "target", ".terraform", ".gradle", ".next", ".cache"}


def _ignore_suggestion(f: str) -> str:
    """A .gitignore line, or "" when we should NOT suggest one.

    Returning "" is a real answer, not a fallback: for an oversize SOURCE file the
    correct advice is to go look at it, never to ignore it.
    """
    parts = f.replace("\\", "/").split("/")
    for p in parts[:-1]:
        if p in _CACHE_DIRS:
            return f"**/{p}/"
    suffix = Path(f).suffix.lower()
    if suffix in _IGNORABLE_SUFFIXES:
        return f"*{suffix}"
    return ""


def _audit_path() -> str:
    return os.environ.get("COMMIT_GATE_AUDIT") or str(
        Path(__file__).resolve().parents[1] / "org" / _gao_name())


def _audit_oversize(f: str, size: int, reason: str) -> bool:
    """Record an override that suppressed a REAL block. Returns True iff the
    record was durably written. A False return is load-bearing: the caller REFUSES
    the override on it (fail-closed), because the override is legal only when
    audited. This runs ONLY on the override-suppression path -- never on a pass,
    where there is nothing to audit and an OSError is correctly ignored."""
    audit = _audit_path()
    agent = os.environ.get("OPAL_AGENT_SERIAL", "unknown")
    ts = __import__("datetime").datetime.now(
        __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        os.makedirs(os.path.dirname(audit), exist_ok=True)
        with open(audit, "a", encoding="utf-8") as fh:
            fh.write(f"{ts} OVERSIZE-OVERRIDE  {agent}  {f}  {size}B  "
                     f"reason={reason}\n")
        return True
    except OSError:
        return False  # unwritable -> caller fails CLOSED, never open


def process_files(files: list[str]) -> int:
    checked = 0
    # ZC-1: files whose suffix this gate DECLARES it reads. Counted IN THE DISPATCH
    # rather than re-derived at the tail on purpose -- a second predicate describing the
    # same set is a divergence waiting to happen, and it would fail OPEN (a declared file
    # the tail's copy did not recognise would slip back to rc=0, which is this whole bug).
    declared = 0
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
            # LOUD, never silent (pure-deletion TO AC-2, the ZERO_CHECKS lesson): a gate
            # run that skipped a path must stay distinguishable from one that checked it.
            _echo("SKIP: deleted (nothing to compile/lint): " + f, sys.stdout)
            continue

        # OVERSIZE REFUSAL -- FIRST, and BEFORE the per-suffix dispatch below.
        # Placement is the control: the dispatch has no branch for .exe/.zip/.pkl,
        # so anything checked only INSIDE it is invisible to this gate. That blind
        # spot is exactly how a 685MB binary reached origin's doorstep. A size check
        # that only ran on .py would be an instrument that cannot fail.
        # Deliberately does NOT increment `checked`: it is a pure refusal, silent on
        # pass, so the "clean for N file(s)" line keeps its existing meaning.
        if _check_file_size(f) != 0:
            return 1

        if _is_python_source(f):
            declared += 1
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
                # scan_file enforces THREE things (Rule 14): the AST undefined-name scan, the silver
                # `coerce_silver_ids()` requirement, and the Rule-15 `from __future__ import
                # annotations` check. Labelling every non-zero rc "undefined-name scan failed" names
                # ONE of the three as the cause of all of them. The violation itself is printed above
                # this line, so nothing is hidden -- but the summary contradicts it, and a reader who
                # trusts the summary chases the wrong defect. (Cost a real detour on
                # data/black_diamond/.../C_05: the summary said undefined-name; the actual violation
                # was a missing __future__ import, and `ds-precommit-check` alone reported zero
                # undefined names.) Name the CHECK, not one of its assertions.
                _echo(f"BLOCKED: ds-precommit-check failed on {f} "
                      f"(undefined-name / silver-ids / future-annotations -- see above)", sys.stderr)
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

            # WARN-only, never blocks (see its docstring for the limit it does NOT close).
            _nonascii_lint_one(f)

            checked += 1

        elif f.endswith(".sh"):
            declared += 1

            # ZC-2: EVERY .sh, whatever its path. This is what makes a .sh outside
            # _SHELL_SCOPE a CHECKED file instead of a silent zero -- the defect this TO
            # closes. comp-shell's scope is NOT widened; see _bash_syntax_check_one.
            if _bash_syntax_check_one(f) != 0:
                return 1

            if _shell_in_scope(f):
                if _shell_scan_one(f) != 0:
                    return 1

            # ONE increment per FILE, not per instrument: `checked` is a file counter (the
            # summary reads "N of {len(files)} file(s)"), so bumping it once per check would
            # make N exceed the denominator on an in-scope .sh.
            checked += 1

            # Runs on ALL .sh regardless of Rule-16 scope: the deploy wrapper that motivated
            # this check is NOT local-runtime-scoped, so gating it behind _shell_in_scope would
            # have excluded the exact file whose non-ASCII stranded a manifest. Does not bump
            # `checked` (mirrors manifest-check: this is a lint, not a scoped gate).
            _nonascii_lint_one(f)

            # manifest-check runs on ALL .sh regardless of Rule-16 scope (mirrors bash:
            # this call sits OUTSIDE the _shell_in_scope block) -- does NOT bump `checked`.
            if _manifest_check_one(f) != 0:
                return 1

        elif f.endswith(".tf"):
            declared += 1
            # NEW file type for this gate (ses-sender-lint TO, 2026-07-07) -- Terraform
            # doesn't need py_compile/ruff/etc, just the SES-sender scan (requirement 2:
            # Lambda EMAIL_FROM/SES_SENDER env values live in .tf, not .py).
            if _ses_sender_lint_one(f) != 0:
                return 1
            checked += 1

        elif f.endswith(".json") and f.replace("\\", "/").startswith("org/projects/"):
            declared += 1
            # NEW 2026-07-13 (CTO). A MALFORMED PROJECT JSON IS A SILENT-INVISIBILITY BUG, and it
            # has already happened: `org/projects/BD_RPSAUTO.json` carried two unescaped inner
            # double-quotes (`DO NOT "RECONCILE" THEM`) and was **1 of 240** that would not parse.
            #
            # EVERY consumer of the project registry wraps its load in a bare try/except and SKIPS
            # a bad file SILENTLY -- so that project was INVISIBLE TO THE ENTIRE FABRIC (11 tools:
            # fabric-check, registry-check, to-check, prd-check, prd-delta, loop-resolve, operator,
            # validator, activity-check, fabric-commits, fabric-projects) and NOTHING EVER SAID A
            # WORD. *A project that vanishes because its file broke is indistinguishable from a
            # project that does not exist.* (Surfaced by COO's F-013 loader, which WARNs instead of
            # skipping -- which is the whole reason it was findable.)
            #
            # A bare `except: continue` over a data file is the same ERROR LAUNDERING as F4's
            # C_02 try/except: it converts a loud parse failure into a silent absence.
            # So: block it at the WRITE, where the author is present to fix it, instead of
            # discovering it months later from a tool that never mentioned it.
            # NARROW except, deliberately. My FIRST version of this check used a bare
            # `except Exception` -- and because `json` was not imported, `json.load` raised
            # NameError, which the bare except swallowed and REPORTED AS "not valid JSON".
            # The gate then BLOCKED A PERFECTLY VALID FILE, and fired IDENTICALLY on valid and
            # malformed input. A GATE THAT ALWAYS FIRES IS EXACTLY AS USELESS AS ONE THAT NEVER
            # DOES -- and the bare except had LAUNDERED A BUG IN THE INSTRUMENT INTO A VERDICT
            # ABOUT THE DATA (the same error-laundering class as F4's C_02 try/except).
            # Caught only by the POSITIVE control; the mutant alone would have "passed."
            # >> THE EXCEPT MUST BE NARROW ENOUGH THAT A BUG IN THE CHECKER CANNOT BE REPORTED
            #    AS A FAULT IN THE CHECKED. <<
            import json as _json
            try:
                with open(f, encoding="utf-8") as _fh:
                    _json.load(_fh)
            except (_json.JSONDecodeError, UnicodeDecodeError, OSError) as e:
                _echo(f"BLOCKED: {f} is not valid JSON -- {type(e).__name__}: {e}", sys.stderr)
                _echo("         A malformed project JSON is SILENTLY SKIPPED by all 11 registry "
                      "consumers, so the project becomes invisible to the whole fabric with no "
                      "error anywhere. Fix the syntax (commonly: an unescaped \" inside a string "
                      "value -- escape it as \\\").", sys.stderr)
                return 1
            checked += 1

        elif os.path.basename(f).lower().startswith("buildspec") and f.lower().endswith((".yml", ".yaml")):
            declared += 1
            # AMGT_HARVST-D1-W183-S10: a CodeBuild buildspec used to fall through this loop unread
            # ("checked 0 of 1 -- NOTHING WAS CHECKED"), and an unquoted colon-space list item in one
            # failed the live build. A YAML load is the minimum the commit path can do at the write.
            # NARROW except: a bug in this checker must not be reported as a fault in the file.
            import yaml as _yaml
            try:
                with open(f, encoding="utf-8") as _fh:
                    _yaml.safe_load(_fh)
            except (_yaml.YAMLError, UnicodeDecodeError, OSError) as e:
                _echo(f"BLOCKED: {f} is not valid YAML -- {type(e).__name__}: {e}", sys.stderr)
                _echo("         A malformed buildspec fails the CodeBuild run, not the commit. "
                      "Common cause: an unquoted ': ' inside a list item -- quote the item.",
                      sys.stderr)
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
    # Count only substrate files the dispatch loop did NOT already count, so a file that is BOTH a
    # gate subject and substrate (the provider .py; any extensionless .tools/comp-* python script)
    # is reported once, not twice.
    checked += sum(1 for f in substrate
                   if not (_is_python_source(f) or f.endswith((".sh", ".tf"))))

    # ZERO CHECKED IS NOT A PASS AND MUST NOT BE FORMATTED AS ONE.
    #
    # This gate dispatches on .py / .sh / .tf / org/projects/*.json. Every other suffix --
    # .ts, .tsx, .mjs, .js, .md, and every .json outside org/projects/ -- falls through the
    # loop untouched, and this line then printed "OK: ... clean for 0 file(s)" with rc=0.
    #
    # MEASURED 2026-08-27, FOUR SEATS INSIDE IT SIMULTANEOUSLY: 0.4.0_DE_ClientPlatform~Y read
    # it as a pass across 10 commits / 24 files / 0 checked; 0.4.0_DE_ClientPlatform~Z across 4;
    # 2.0.0_SA_COO~Z across 6; and this seat reported the estate-wide blind spot as 2 files when
    # comp-find puts it at 25. Every one of those readers spends their session hunting exactly
    # this shape. THE DENOMINATOR WAS ON SCREEN EVERY TIME.
    #
    # >> SO PRINTING THE DENOMINATOR IS NOT THE REMEDY. "OK:" and "clean" carry the verdict,
    #    "0 file(s)" carries the truth, and the eye takes the verdict. A DENOMINATOR PRINTED BUT
    #    NOT READ IS AS USELESS AS ONE NOT PRINTED (2.0.0_SA_COO~Z's formulation). The remedy is
    #    to make a zero-denominator result UNABLE to read as a pass. <<
    #
    # Sibling: the identical class in safe_deploy_core.py -- "all files deployed and verified"
    # printed after deploying ZERO (found by 0.0.0_AB_MSTR~Z, ruled and fixed by this seat the
    # same evening). One class, two tools; fixing one without the other is why this survived.
    # rc: a commit carrying ONLY non-dispatched files (a .md, a .ts) is a legitimate no-op and
    # keeps WARN + rc=0 -- turning THAT into a refusal would break every such commit, which is why
    # the 2026-08-27 fix stopped at the wording. What that fix could not reach is the case below:
    # a file whose suffix this gate DECLARES it reads, that reached ZERO checks anyway. There the
    # zero is not a no-op, it is the gate failing to do the one job its own header advertises, and
    # rc=0 makes that indistinguishable from a clean pass. MEASURED on the pre-fix gate: a .sh with
    # a planted syntax error and a syntactically clean .sh -- same directory, both outside
    # _SHELL_SCOPE -- produced BYTE-IDENTICAL output and rc=0. The exit code carried no information
    # about content at all. (ADHC_COMMITGATE.TO-ZEROCHECK-REFUSE, ZC-1; ruling 1.0.0_SA_CTO 87633.)
    if checked == 0:
        _echo(f"WARN: commit-gate checked 0 of {len(files)} file(s) -- NOTHING WAS CHECKED.",
              sys.stdout)
        _echo("      This line is NOT evidence of a clean gate. This gate reads only "
              ".py / .sh / .tf / org/projects/*.json / buildspec*.yml; every other suffix falls through "
              "unexamined.", sys.stdout)
        _echo("      Do NOT cite it as validation for a frontend artifact -- use the "
              "language-appropriate instrument (tsc -b, eslint, a read render).", sys.stdout)
        if declared:
            _echo(f"REFUSED (rc=2): {declared} of {len(files)} file(s) carry a suffix this gate "
                  "DECLARES it reads (.py / .sh / .tf / org/projects/*.json), and NOTHING was "
                  "checked on any of them. A declared subject reaching zero checks is a GATE "
                  "DEFECT, not a clean commit -- rc=2 exists so it can never be read as a pass. "
                  "Fix the gate (or say why the file is out of scope); do not re-run for a 0.",
                  sys.stderr)
            return 2
        return 0
    _echo(f"OK: pre-commit gate clean for {checked} of {len(files)} file(s)", sys.stdout)
    return 0


def main() -> int:
    files = sys.argv[1:]
    return process_files(files)


if __name__ == "__main__":
    sys.exit(main())
