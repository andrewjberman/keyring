#!/usr/bin/env python3
"""CG-8 SEAM-RETIRED battery -- NFRA_CLDGRPH TO-CG-D-7 (cell CG-s-8, PRD R7 / FWD-7).

WHY THIS FILE EXISTS. TO-CG-D-7 removed the local canonical Kuzu rebuild seam from
`infra/aws/globgrph/_canonical.py`. Two batteries pinned that seam's behaviour:

    infra/aws/globgrph/tests/test_canonical_rebuild_liveness.py       (232 lines, DELETED)
        the #17 rebuild-winner liveness protocol: the mkdir mutex, the heartbeat, the
        stale-lock steal, per-unique tmp paths, ownership-check-at-swap.
    infra/aws/globgrph/tests/test_canonical_refresh_failure_signal.py  (97 lines, DELETED)
        the #25 refresh-failure marker lifecycle: written on a genuine rebuild failure,
        surfaced LOUD by the provenance header, cleared on the next successful refresh.

A TEST MOVES WITH THE BEHAVIOUR IT PINS. Most of what those two pinned no longer exists to be
wrong: with no local database there is no rebuild, hence no winner, no lock, no heartbeat, no
steal, no swap and no rebuild failure to mark. Deleting those arms is correct -- but deleting
them SILENTLY would leave the retirement unpinned, so the properties that outlive the seam are
carried here, and each one that asserts an ABSENCE carries a RED MUTANT proving the arm can
actually fire. An absence arm with no mutant beside it passes on a broken matcher exactly as it
passes on a clean estate.

WHAT SURVIVED, AND FROM WHICH BATTERY:
  arm 1  (liveness)  the seam's machinery is GONE from _canonical.py -- no rebuild subprocess,
                     no mkdir mutex, no heartbeat thread, no fallback sink, no status writer.
  arm 2  (liveness)  a retired symbol REFUSES loudly rather than resolving; the refusal is a
                     RuntimeError, not an AttributeError, so `getattr(m, "ensure_fresh", None)`
                     cannot silently degrade to "no refresh available, carry on".
  arm 3  (liveness)  the module still IMPORTS and dunder lookup still behaves -- the tombstone
                     must not read as a broken install to inspect/pytest.
  arm 4  (#25)       the failure-marker READER in _provenance (untouched by TO-CG-D-7, and now
                     orphaned of its writer) is INERT BUT SOUND: no marker reads healthy (None),
                     and a CORRUPT marker still reads as a failure rather than a healthy None.
                     That was the defect DS~B caught, and removing the writer must not un-fix it.
  arm 5  (both)      no user-facing tool surface imports the seam any more -- a census with its
                     own printed denominator and a positive control, not a bare zero.
  arm 6  (both)      the replacement transport is present and is a SERVED client: connect() /
                     query() / vintage_line(), and no kuzu.Database open anywhere in it.

NO NETWORK. Every arm here is hermetic: source-text reads, one import of the tombstone, and one
temp directory for arm 4. Nothing calls the gateway, reads a secret or opens a database -- there
is no database left to open. The live end-to-end exercise of the served graph belongs to
D7-AC3/D7-AC4 and to test_g2_disclosure_battery's arm 7, not here.

READ-ONLY TO THE CLOUD ENGINE (the CG-s-8 bound): kuzu_nessie_load.py, kuzu_incremental_refresh.py,
projection_server.py and projection_worker.py are never edited, imported or monkeypatched here.

Run direct:  python .tools/tests/test_cg8_seam_retired_battery.py   -> prints PASS + denominator.
Run pytest:  pytest .tools/tests/test_cg8_seam_retired_battery.py   -> the same test_* functions.
"""
from __future__ import annotations

import os
import re
import sys
import tempfile
from pathlib import Path

_WORKSPACE = Path(__file__).resolve().parents[2]
_GLOBGRPH = _WORKSPACE / "infra" / "aws" / "globgrph"
_CANONICAL = _GLOBGRPH / "_canonical.py"
_CLIENT = _GLOBGRPH / "projection_client.py"

if str(_GLOBGRPH) not in sys.path:
    sys.path.insert(0, str(_GLOBGRPH))

_DENOMINATORS: dict = {}

# The seam's own machinery, by the token each part is unmistakably named by in the source that
# implemented it. These are SOURCE-TEXT tokens, so the arm reads the file rather than trusting an
# import to have failed for the right reason.
_SEAM_TOKENS = (
    "os.mkdir",                 # the build mutex (atomic create; Rule 16 -- no flock on Git Bash)
    "subprocess.run",           # the supervised rebuild child
    "threading.Thread",         # the liveness heartbeat
    "os.replace",               # the build-to-temp atomic swap
    "_append_fallback_sink",    # the .fallback.jsonl sink writer
    "_write_refresh_failure",   # the ._refresh_status.json failure-marker writer
    "HEARTBEAT_STALE_S",        # the stale-lock steal threshold
    "MUTEX_WAIT_S",             # the loser wait before serving stale
    "REBUILD_TIMEOUT_S",        # the no-immortal-rebuild ceiling
    "kuzu_nessie_db",           # the local database this module used to name and open
)

# The RED MUTANT for arms 1 and 6: a source string that DOES carry the machinery. If the matcher
# in those arms is broken (a typo'd token, a regex that cannot fire), the mutant passes too and
# the arm fails loudly instead of certifying a clean estate it never actually inspected.
_RED_MUTANT_SOURCE = (
    '"""A pre-retirement _canonical.py, for the arm to convict."""\n'
    "MUTEX_WAIT_S = 180.0\n"
    "HEARTBEAT_STALE_S = 90.0\n"
    "REBUILD_TIMEOUT_S = 1800.0\n"
    "CANONICAL_DB_PATH = os.path.join(_HERE, 'kuzu_nessie_db')\n"
    "def ensure_fresh(db_path):\n"
    "    os.mkdir(lock)\n"
    "    threading.Thread(target=_loop).start()\n"
    "    subprocess.run([sys.executable, 'kuzu_nessie_load.py'], timeout=REBUILD_TIMEOUT_S)\n"
    "    os.replace(tmp, db_path)\n"
    "    _write_refresh_failure(db_path, 'rebuild-failed')\n"
    "    _append_fallback_sink(db_path, 0, None, 'inc-served-labeled-stale', log)\n"
)


def _code_only(src: str) -> str:
    """The file's CODE, with its module docstring and every `#` comment removed.

    THE ARM'S SUBJECT IS THE MACHINERY, NOT THE WORD. A retirement tombstone has to be able to
    SAY what it removed -- this module's own docstring names `kuzu_nessie_db` and the atomic
    replace in the course of explaining why neither is here any more -- and a raw substring sweep
    convicts that prose exactly as it would convict a live call. Stripping the docstring and the
    comments makes the arm measure what it claims to measure. String literals INSIDE functions are
    deliberately kept: a database path in a constant is machinery, not commentary."""
    import ast
    import io
    import tokenize

    lines = src.splitlines(keepends=True)
    try:
        mod = ast.parse(src)
    except SyntaxError:
        return src
    doc = ast.get_docstring(mod, clean=False)
    if doc is not None and mod.body:
        node = mod.body[0]
        start, end = node.lineno - 1, getattr(node, "end_lineno", node.lineno)
        lines = lines[:start] + ["\n"] * (end - start) + lines[end:]
    # Blank each COMMENT in place rather than re-joining tokens: joining a token stream breaks
    # every multi-token substring the arm looks for (`os.mkdir` becomes `os`, `.`, `mkdir`), so
    # the sweep would find nothing anywhere -- including in a source that plainly carries it.
    # Blanking preserves offsets, so what remains is the file's code exactly as written.
    out = list(lines)
    try:
        for tok in tokenize.generate_tokens(io.StringIO("".join(lines)).readline):
            if tok.type != tokenize.COMMENT:
                continue
            (srow, scol), (erow, ecol) = tok.start, tok.end
            if srow != erow or srow - 1 >= len(out):
                continue
            line = out[srow - 1]
            out[srow - 1] = line[:scol] + " " * (ecol - scol) + line[ecol:]
    except (tokenize.TokenError, IndentationError, SyntaxError):
        pass
    return "".join(out)


def _tokens_present(src: str) -> list:
    return sorted({t for t in _SEAM_TOKENS if t in _code_only(src)})


# ---- arm 1 (from the LIVENESS battery): the machinery is gone from the source ----------------

def test_seam_machinery_absent_from_canonical_source():
    """The mutex, the heartbeat, the rebuild child, the swap, the sink and the status writer are
    absent from _canonical.py -- measured on the source text, with a RED MUTANT that IS convicted
    by the same matcher."""
    src = _CANONICAL.read_text(encoding="utf-8")
    found = _tokens_present(src)
    assert not found, (
        "the retired rebuild seam is still present in %s: %s"
        % (_CANONICAL.name, found))

    mutant_found = _tokens_present(_RED_MUTANT_SOURCE)
    assert len(mutant_found) >= 8, (
        "RED MUTANT NOT CONVICTED: the matcher found only %s of the %d seam tokens in a source "
        "that carries them, so its zero on the real file proves nothing"
        % (mutant_found, len(_SEAM_TOKENS)))
    _DENOMINATORS["seam_machinery"] = len(_SEAM_TOKENS)
    print("OK seam_machinery: 0 of %d seam token(s) in %s; RED MUTANT convicted on %d of %d"
          % (len(_SEAM_TOKENS), _CANONICAL.name, len(mutant_found), len(_SEAM_TOKENS)))


# ---- arm 2 (from the LIVENESS battery): a retired symbol refuses, and refuses LOUDLY ----------

def test_retired_symbols_raise_runtimeerror_not_attributeerror():
    """Every retired name refuses with a RuntimeError naming R7 and the replacement.

    NOT AttributeError, and this is the load-bearing half: a caller doing
    `getattr(_canonical, "ensure_fresh", None)` would read an AttributeError as "older build, no
    refresh available" and carry on over whatever it found locally. There is no local database to
    carry on over any more, so the loud stop IS the safe behaviour."""
    import _canonical

    retired = ("ensure_fresh", "CANONICAL_DB_PATH", "CANONICAL_DB_NAME", "needs_refresh",
               "is_canonical", "refresh_failure", "_refresh_status_path", "_full_rebuild_only",
               "_incremental_or_serve_stale", "_incremental_or_full_rebuild",
               "_FALLBACK_SINK_SUFFIX", "_append_fallback_sink", "_atomic_swap", "_Heartbeat",
               "_owns_lock", "_beat", "_run_child_supervised",
               # a name that never existed: the refusal must not be an enumeration that can
               # drift, so an unknown attribute refuses exactly like a known one.
               "a_symbol_that_never_existed")
    for name in retired:
        try:
            getattr(_canonical, name)
        except RuntimeError as ex:
            assert "RETIRED" in str(ex) and "R7" in str(ex), \
                "the refusal for %r must name the retirement: %s" % (name, ex)
            assert "projection_client" in str(ex), \
                "the refusal for %r must name the replacement: %s" % (name, ex)
        except AttributeError as ex:
            raise AssertionError(
                "_canonical.%s raised AttributeError -- a defensive getattr(..., None) would read "
                "that as 'no refresh available' and continue silently: %s" % (name, ex)) from None
        else:
            raise AssertionError(
                "_canonical.%s RESOLVED -- the seam is still reachable by attribute" % name)

    # The soft-probe forms a real caller uses must ALSO stop, not degrade to a falsy default.
    for probe in (lambda m: getattr(m, "ensure_fresh", None), lambda m: hasattr(m, "ensure_fresh")):
        try:
            probe(_canonical)
        except RuntimeError:
            pass
        else:
            raise AssertionError(
                "a soft probe for ensure_fresh returned instead of raising -- a caller could "
                "silently skip the refresh it thinks it is doing")
    _DENOMINATORS["retired_symbols"] = len(retired)
    print("OK retired_symbols: %d of %d name(s) refused with RuntimeError (incl. 1 never-existed "
          "control); both soft-probe forms also refused" % (len(retired), len(retired)))


# ---- arm 3 (from the LIVENESS battery): the tombstone is not a broken install -----------------

def test_module_still_imports_and_dunders_behave():
    """The module imports and dunder lookup follows the normal protocol.

    A tombstone that raised on `__all__` / `__path__` / `__wrapped__` would break `inspect`,
    pytest collection and the import machinery, and the retirement would be indistinguishable
    from a broken checkout. This is the POSITIVE CONTROL for arm 2: it proves the refusal is
    selective rather than a module that raises on everything."""
    import _canonical

    assert _canonical.__doc__ and "RETIRED" in _canonical.__doc__, \
        "the module docstring must state the retirement -- it is the first thing a reader hits"
    assert "projection_client" in _canonical.__doc__, \
        "the docstring must name the replacement"
    for dunder in ("__name__", "__file__", "__doc__", "__spec__", "__loader__"):
        getattr(_canonical, dunder)          # must not raise
    try:
        _canonical.__all__
    except AttributeError:
        pass
    except RuntimeError as ex:
        raise AssertionError(
            "dunder lookup went through the refusal (%s) -- inspect/pytest would break" % ex)
    _DENOMINATORS["import_sane"] = 1
    print("OK import_sane: tombstone imports; 5 dunders resolve; __all__ -> AttributeError")


# ---- arm 4 (from the #25 REFRESH-FAILURE battery): the reader is inert but still sound --------

def test_refresh_failure_reader_is_inert_but_sound():
    """_provenance's failure-marker reader is UNTOUCHED by this order and now has no writer.

    Two properties carry from the #25 battery, and only two, because the marker can no longer be
    written: (a) a database with NO marker reads healthy -- the reader must not manufacture a
    failure now that nothing ever clears one; (b) a PRESENT-but-UNREADABLE marker still reads as
    a FAILURE, not as a healthy None. (b) is the defect DS~B caught (RAVC b50855e20) and it is
    exactly the property that would silently regress if someone later 'simplified' a reader whose
    writer is gone. Residue from a pre-retirement crash can still be on a developer's disk."""
    import _provenance

    with tempfile.TemporaryDirectory() as td:
        healthy = os.path.join(td, "db_no_marker")
        with open(healthy, "w", encoding="utf-8") as fh:
            fh.write("HEALTHY")
        assert _provenance._read_refresh_failure(healthy) is None, \
            "a DB with no failure marker must read None (healthy), not a manufactured failure"
        assert "REFRESH FAILED" not in _provenance.format_provenance_header(healthy), \
            "the header must not surface a failure for a DB that never had one"

        corrupt = os.path.join(td, "db_corrupt")
        with open(corrupt + _provenance._REFRESH_STATUS_SUFFIX, "w", encoding="utf-8") as fh:
            fh.write("{truncated-half-written-not-json")
        rf = _provenance._read_refresh_failure(corrupt)
        assert isinstance(rf, dict) and rf.get("kind") == "unreadable-marker", \
            "an UNREADABLE marker must still read as a FAILURE dict, not a healthy None: %r" % (rf,)
        assert "REFRESH FAILED" in _provenance.format_provenance_header(corrupt), \
            "the header must still surface the unreadable marker (the modal crash residue)"
    _DENOMINATORS["marker_reader"] = 4
    print("OK marker_reader: 4 of 4 -- absent reads None, corrupt reads unreadable-marker, "
          "header agrees with both")


# ---- arm 5 (from BOTH batteries): no tool surface imports the seam ---------------------------

_TOOL_HOMES = (
    _WORKSPACE / ".tools",
    _WORKSPACE / "org" / "modules" / "graph",
    _WORKSPACE / "org" / "modules" / "heatmap",
    _GLOBGRPH,
)
# TWO anchors, and both are load-bearing.
#   TRAILING: a bare `import _canonical` also matches `import _canonical_silver_lib`, a different
#     module in another lane (twelve files under data/canonical/schwab/). `(?![\w])` excludes it.
#   LEADING: `^\s*` requires the import at STATEMENT position, so a file that merely NAMES the
#     token -- a forbidden-token list in a test, this battery's own arms -- is not convicted for
#     talking about the thing. A lazy import inside a function is indented, and still matches.
_IMPORT_RE = re.compile(r"^[ \t]*(?:import|from)\s+_canonical(?![\w])", re.M)


def _python_files() -> list:
    """Every .py under the four tool homes, minus two files that are the SUBJECT rather than the
    population: this battery (it quotes the import it forbids) and the tombstone itself (it is the
    seam, so it cannot be one of the seam's importers)."""
    skip = {Path(__file__).resolve(), _CANONICAL.resolve()}
    out = []
    for home in _TOOL_HOMES:
        for path in home.rglob("*.py"):
            if path.resolve() in skip:
                continue
            out.append(path)
    return out


def test_no_tool_surface_imports_the_seam():
    """A census, not a bare zero: the denominator is printed and a POSITIVE CONTROL on the same
    matcher over the same population returns non-zero, so a zero here is a measured absence
    rather than a matcher that cannot fire."""
    files = _python_files()
    assert len(files) > 100, \
        "OUT-OF-CORPUS: only %d python file(s) found under the tool homes -- a zero over an " \
        "empty population is not an absence" % len(files)

    importers, control_hits = [], []
    for path in files:
        try:
            src = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # CODE only: `# Run as a SUBPROCESS from _canonical (...)` in the cloud engine is a
        # comment about history, not an import, and convicting it would be a wrong-object error.
        if _IMPORT_RE.search(_code_only(src)):
            importers.append(str(path.relative_to(_WORKSPACE)).replace("\\", "/"))
        if "import projection_client" in src or "import _provenance" in src:
            control_hits.append(path)

    assert not importers, (
        "a tool surface still imports the retired seam: %s" % importers)
    assert control_hits, (
        "POSITIVE CONTROL FAILED: the same sweep found 0 files importing projection_client or "
        "_provenance across %d file(s) -- the sweep is not reading the corpus it claims" % len(files))
    # And the matcher itself must convict a real import, at top level and lazily inside a
    # function, while sparing the two things that look like one and are not.
    assert _IMPORT_RE.search("import _canonical  # noqa\n"), "matcher cannot fire on a real import"
    assert _IMPORT_RE.search("def f():\n    import _canonical\n"), \
        "matcher must fire on a LAZY import inside a function -- that is the form every repointed "\
        "consumer used"
    assert not _IMPORT_RE.search("import _canonical_silver_lib\n"), \
        "matcher must not drag in _canonical_silver_lib (another lane, shared prefix)"
    assert not _IMPORT_RE.search('forbidden = ("import _canonical", "kuzu.Database(")\n'), \
        "matcher must not convict a file for NAMING the token in a forbidden-token list"
    _DENOMINATORS["no_importers"] = len(files)
    print("OK no_importers: 0 importer(s) across %d python file(s) in 4 tool home(s); "
          "POSITIVE CONTROL %d file(s) import projection_client/_provenance; matcher convicts a "
          "real import and spares _canonical_silver_lib" % (len(files), len(control_hits)))


# ---- arm 6 (from BOTH batteries): the replacement is a SERVED client -------------------------

def test_replacement_transport_is_served_not_local():
    """projection_client offers the shape the retired consumers needed, and opens nothing local."""
    src = _CLIENT.read_text(encoding="utf-8")
    for symbol in ("def connect(", "def query(", "def vintage_line(", "class ServedConnection",
                   "class ServedResult"):
        assert symbol in src, "projection_client is missing %r -- the replacement is incomplete" % symbol
    for forbidden in ("kuzu.Database(", "kuzu.Connection(", "kuzu_nessie_db"):
        assert forbidden not in src, \
            "projection_client must not open or name a local database: found %r" % forbidden
    # RED MUTANT: the same forbidden-token check must convict a source that DOES open one.
    mutant = "db = kuzu.Database('kuzu_nessie_db')\n"
    assert any(f in mutant for f in ("kuzu.Database(", "kuzu_nessie_db")), \
        "RED MUTANT NOT CONVICTED: the forbidden-token check cannot fire"
    _DENOMINATORS["replacement"] = 5
    print("OK replacement: 5 of 5 client symbols present; 0 of 3 local-DB tokens; RED MUTANT convicted")


_ALL_TESTS = [
    test_seam_machinery_absent_from_canonical_source,
    test_retired_symbols_raise_runtimeerror_not_attributeerror,
    test_module_still_imports_and_dunders_behave,
    test_refresh_failure_reader_is_inert_but_sound,
    test_no_tool_surface_imports_the_seam,
    test_replacement_transport_is_served_not_local,
]


def main() -> int:
    failures = []
    for t in _ALL_TESTS:
        try:
            t()
        except Exception as ex:  # noqa: BLE001 -- collect every arm, never stop at the first
            failures.append((t.__name__, ex))
            print("FAIL: %s: %s" % (t.__name__, ex))
    print("DENOMINATOR: %d of %d arm(s) recorded a pass (%s)"
          % (len(_DENOMINATORS), len(_ALL_TESTS), sorted(_DENOMINATORS)))
    if failures:
        print("FAIL: %d of %d arm(s) failed" % (len(failures), len(_ALL_TESTS)))
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
