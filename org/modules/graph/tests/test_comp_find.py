#!/usr/bin/env python3
"""test_comp_find.py -- acceptance battery for `.tools/comp-find` (NFRA_SCRIPTGEN Part B).

comp-find is the rail that GATES Rule-21 raw-search denial. That is what sets the bar here: an
agent who is DENIED a raw grep has no second instrument, so every way this tool can under-report is
a way the estate manufactures a confirmed absence. The battery is therefore weighted almost entirely
to the honesty properties, not to "did it find the thing":

  E  EXACTLY ONE BAND per hit     -- an ungraded or double-graded hit breaks the reject-first ladder
  D  DENOMINATOR is the TRUE total -- band counts must be the whole universe, never the page's
  Z  a zero is a MEASURED zero     -- naming its denominator, incl. files it could NOT read
  P  pagination cannot hide        -- "no more results" must never read as "nothing else exists"
  F  --band / --files / --name     -- the filters narrow the VIEW, never the reported denominator
  W  the BRE footgun warning       -- \\| \\( \\) are literals in python re; a silent 0 is the harm

MUTATION NOTE: the D and Z asserts pin NUMBERS derived from a fixture whose contents this file
authors, so a mutant that reports the page count instead of the total (the `--query 'length(...)'`
class CLAUDE.md names) fails here rather than passing on a plausible-looking figure.

The scan is pointed at a tmp fixture tree via a pathspec, so the battery never depends on estate
content and cannot go red because a real file was edited.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]
_TOOL = _WS / ".tools" / "comp-find"


def _load():
    """comp-find is EXTENSIONLESS -- name the loader explicitly."""
    loader = importlib.machinery.SourceFileLoader("comp_find_under_test", str(_TOOL))
    spec = importlib.util.spec_from_loader("comp_find_under_test", loader)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["comp_find_under_test"] = mod
    loader.exec_module(mod)
    return mod


F = _load()


# --------------------------------------------------------------------------- fixture tree
# One file per BAND, so the ladder is exercised end to end and the band arithmetic is knowable.
_TREE = {
    "src/widget_engine.py":   "def apply_widget(x):\n    return x  # widget\n",   # HEAD (name)
    "src/other_engine.py":    "def apply_widget(x):\n    return x\n",             # DEF
    "src/plain.py":           "value = call(apply_widget)  # a widget mention\n"
                              "another_line_with_widget = 1\n",                   # SURFACED (x1)
    "conf/settings.json":     '{"widget": true}\n',                               # CONFIG
    "tests/test_thing.py":    "def test_widget():\n    assert apply_widget(1)\n",  # TEST
    "docs/notes.md":          "the widget is described here\n",                   # DOC
}
# Deliberate counts, hand-derived from the fixture above and asserted below:
#   HEAD 2 (both lines of widget_engine.py)  DEF 1  SURFACED 2  CONFIG 1  TEST 2  DOC 1  = 9 hits


@pytest.fixture()
def tree(tmp_path, monkeypatch):
    """Build the fixture tree and point comp-find's universe at it.

    `_comprail.gitignore_aware_files` is stubbed rather than mocked away: it still returns
    repo-relative paths, so the banding, sorting and rendering all run on the REAL code path.
    """
    for rel, text in _TREE.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    rels = sorted(_TREE)
    monkeypatch.setattr(F, "WS", str(tmp_path))
    monkeypatch.setattr(F._comprail, "gitignore_aware_files",
                        lambda ws, pathspec, include_held=False, corpus="default": (list(rels), "", None))
    monkeypatch.setattr(F._comprail, "systems_context", lambda files: [])
    monkeypatch.setattr(F._comprail, "log_rail", lambda *a, **k: None)
    return tmp_path


def _run(monkeypatch, capsys, *args):
    monkeypatch.setattr(sys, "argv", ["comp-find"] + [str(a) for a in args])
    rc = F.main()
    return rc, capsys.readouterr().out


def _band_counts(out):
    """Parse the BANDS line back into a dict -- reading the tool's own reported totals."""
    line = [ln for ln in out.splitlines() if "BANDS (true totals" in ln][0]
    tail = line.split(":", 1)[1].strip()
    if tail == "none":
        return {}
    return {k: int(v) for k, v in (p.split("=") for p in tail.split())}


# --------------------------------------------------------------------------- E: banding
def test_E_every_hit_lands_in_exactly_one_band(tree, monkeypatch, capsys):
    """The band counts must sum to the hit denominator -- no hit ungraded, none double-counted.

    An UNGRADED hit is the failure that matters: it would be present in the universe and absent from
    every band view, so a `--band` sweep across all seven bands would silently miss it.
    """
    rc, out = _run(monkeypatch, capsys, "widget")
    assert rc == 0
    counts = _band_counts(out)
    total_line = [ln for ln in out.splitlines() if "DENOMINATOR:" in ln][0]
    hits = int(total_line.split("DENOMINATOR:")[1].split("hit(s)")[0].strip())
    assert sum(counts.values()) == hits, "band counts do not sum to the hit total: %r vs %d" % (
        counts, hits)


def test_E_the_ladder_grades_each_fixture_file_as_designed(tree, monkeypatch, capsys):
    """Pin the ladder itself. Each fixture file exists to occupy exactly one rung."""
    _rc, out = _run(monkeypatch, capsys, "widget")
    counts = _band_counts(out)
    assert counts == {"HEAD": 2, "DEF": 1, "SURFACED": 2, "CONFIG": 1, "TEST": 2, "DOC": 1}


def test_E_reject_first_ordering_puts_HEAD_before_DOC(tree, monkeypatch, capsys):
    """Reject-first is the whole point of grading: the tail is what you SKIP, not what you MISSED."""
    _rc, out = _run(monkeypatch, capsys, "widget", "--all")
    order = [ln.strip()[1:].split("]")[0] for ln in out.splitlines() if ln.strip().startswith("[")]
    assert order == ["HEAD", "DEF", "SURFACED", "CONFIG", "TEST", "DOC"]


def test_E_a_test_file_is_never_graded_DEF(tree, monkeypatch, capsys):
    """Discrimination check: `tests/test_thing.py` HAS a `def` line. TEST must win, or a battery's
    own assertion reads as the definition of the thing it asserts about."""
    assert F._band("tests/test_thing.py", "def test_widget():\n", ["widget"]) == "TEST"
    assert F._band("src/other_engine.py", "def apply_widget(x):\n", ["widget"]) == "DEF"


# --------------------------------------------------------------------------- D/P: denominator
def test_D_band_counts_are_TRUE_totals_not_the_pages(tree, monkeypatch, capsys):
    """A one-hit page must still report all 9 hits and all six bands.

    MUTANT this kills: computing the counts AFTER slicing the page -- the same shape as
    `aws --query 'length(...)'` returning the page count, which CLAUDE.md records reporting 100
    when the truth was 142, with no error and no warning.
    """
    _rc, out = _run(monkeypatch, capsys, "widget", "--limit", "1")
    assert _band_counts(out) == {"HEAD": 2, "DEF": 1, "SURFACED": 2, "CONFIG": 1, "TEST": 2, "DOC": 1}
    assert "PAGE 1 of 9  (showing 1 of 9)" in out


def test_P_a_partial_page_says_how_many_are_not_shown(tree, monkeypatch, capsys):
    """'no more results on this page' must never be confusable with 'nothing else exists'."""
    _rc, out = _run(monkeypatch, capsys, "widget", "--limit", "2")
    assert "MORE: 7 hit(s) not shown" in out
    assert "--page 2" in out


def test_P_the_last_page_does_not_claim_more(tree, monkeypatch, capsys):
    _rc, out = _run(monkeypatch, capsys, "widget", "--all")
    assert "MORE:" not in out
    assert "PAGE 1 of 1  (showing 9 of 9)" in out


def test_P_pagination_covers_the_universe_exactly_once(tree, monkeypatch, capsys):
    """Walk every page and reassemble: the pages must partition the 9 hits with no gap, no dupe.

    A page-walk is the only assertion that catches an off-by-one in the slice bounds; the per-page
    header would look correct on either side of it.
    """
    seen = []
    for page in range(1, 10):
        _rc, out = _run(monkeypatch, capsys, "widget", "--limit", "1", "--page", str(page))
        rows = [ln.strip() for ln in out.splitlines()
                if ln.startswith("    ") and ":" in ln and not ln.strip().startswith("[")]
        seen.extend(rows)
    assert len(seen) == 9
    assert len(set(seen)) == 9, "a hit appeared on two pages"


def test_P_page_beyond_the_end_clamps_and_says_so(tree, monkeypatch, capsys):
    """An over-range page must not render an empty page that reads as exhaustion."""
    _rc, out = _run(monkeypatch, capsys, "widget", "--limit", "5", "--page", "99")
    assert "PAGE 2 of 2" in out


# --------------------------------------------------------------------------- Z: honest zero
def test_Z_zero_hits_is_a_MEASURED_zero_naming_the_scanned_denominator(tree, monkeypatch, capsys):
    _rc, out = _run(monkeypatch, capsys, "zzz_no_such_token_9999")
    assert "MEASURED zero over 6 scanned file(s)" in out
    assert "not a claim the term is absent from the estate" in out
    assert "BANDS (true totals, not this page): none" in out


def test_Z_unreadable_files_are_counted_and_disclosed(tree, monkeypatch, capsys):
    """A file that could not be OPENED was never searched. Excluding it from `scanned` is correct;
    saying nothing about it is not -- the zero then covers a universe smaller than it names.

    MUTANT this kills: the pre-fix bare `continue`, which dropped unreadable files silently. Rule 22:
    print the denominator of every scan you reason from, including the part you could not reach.
    """
    real_open = open

    def _boom(path, *a, **k):
        if str(path).endswith("plain.py"):
            raise OSError("permission denied")
        return real_open(path, *a, **k)

    monkeypatch.setattr("builtins.open", _boom)
    _rc, out = _run(monkeypatch, capsys, "zzz_no_such_token_9999")
    assert "1 UNREADABLE, NOT searched" in out
    assert "never searched" in out and "does NOT cover them" in out


def test_Z_a_blocked_scope_is_loud_and_rc2_never_a_clean_empty(tree, monkeypatch, capsys):
    """A scope resolution failure must NOT render as zero hits. A blocked search and an empty
    search are the same output right up until you act on it."""
    monkeypatch.setattr(F._comprail, "gitignore_aware_files",
                        lambda ws, pathspec, include_held=False, corpus="default": (None, "", "bad pathspec"))
    rc, out = _run(monkeypatch, capsys, "widget")
    assert rc == 2
    assert "BLOCKED" in out and "bad pathspec" in out
    assert "MEASURED zero" not in out


def test_Z_sovereign_held_note_is_surfaced(tree, monkeypatch, capsys):
    """When the rail withholds a firm path, absence is NOT confirmed and the run must say so."""
    monkeypatch.setattr(F._comprail, "gitignore_aware_files",
                        lambda ws, pathspec, include_held=False, corpus="default":
                        (sorted(_TREE), "HELD: 3 sovereign path(s) excluded", None))
    _rc, out = _run(monkeypatch, capsys, "widget")
    assert "HELD: 3 sovereign path(s) excluded" in out


# --------------------------------------------------------------------------- F: filters
def test_F_band_filter_narrows_the_view_not_the_denominator(tree, monkeypatch, capsys):
    """The filtered count is reported ALONGSIDE the full one -- a narrowed view must never
    overwrite the universe it was taken from."""
    _rc, out = _run(monkeypatch, capsys, "widget", "--band", "DOC")
    assert "band=DOC -> 1" in out
    assert _band_counts(out) == {"HEAD": 2, "DEF": 1, "SURFACED": 2, "CONFIG": 1, "TEST": 2, "DOC": 1}
    assert "docs/notes.md" in out and "src/widget_engine.py" not in out


def test_F_unknown_band_is_rc2_and_lists_the_valid_set(tree, monkeypatch, capsys):
    """A typo'd band must not silently return zero -- that is indistinguishable from a real zero."""
    rc, out = _run(monkeypatch, capsys, "widget", "--band", "NOPE")
    assert rc == 2
    assert "unknown band 'NOPE'" in out
    assert "HEAD, DEF, SURFACED, CONFIG, TEST, DOC, COLD" in out


def test_F_files_collapses_to_one_row_per_file(tree, monkeypatch, capsys):
    _rc, out = _run(monkeypatch, capsys, "widget", "--files", "--all")
    rows = [ln.strip() for ln in out.splitlines()
            if ln.startswith("    ") and not ln.strip().startswith("[")]
    rows = [r for r in rows if r.endswith((".py", ".md", ".json"))]
    assert len(rows) == len(set(rows)) == 6


def test_F_name_mode_matches_filenames_not_content(tree, monkeypatch, capsys):
    """`plain.py` CONTAINS 'widget' but is not NAMED for it; name mode must exclude it."""
    _rc, out = _run(monkeypatch, capsys, "--name", "*widget*")
    assert "src/widget_engine.py" in out
    assert "src/plain.py" not in out
    assert "[name]" in out


def test_F_bare_name_query_is_wrapped_in_wildcards(tree, monkeypatch, capsys):
    """A user typing a plain word into --name must not get a zero because they omitted the stars."""
    _rc, out = _run(monkeypatch, capsys, "--name", "widget")
    assert "src/widget_engine.py" in out


def test_F_ignore_case_flag_discriminates(tree, monkeypatch, capsys):
    """Positive AND negative direction -- a flag that changes nothing is not a flag."""
    _rc, no_i = _run(monkeypatch, capsys, "WIDGET")
    assert "MEASURED zero" in no_i
    _rc, with_i = _run(monkeypatch, capsys, "WIDGET", "-i")
    assert "MEASURED zero" not in with_i
    assert _band_counts(with_i)["HEAD"] == 2


# --------------------------------------------------------------------------- W: BRE footgun
def test_W_bre_escapes_raise_the_silent_zero_warning(tree, monkeypatch, capsys):
    r"""`\|` is ALTERNATION in grep and a LITERAL in python re. A BRE-muscle-memory pattern matches
    nothing, and the 0 reads as confirmed absence -- the exact harm this rail exists to prevent."""
    _rc, out = _run(monkeypatch, capsys, r"widget\|gadget")
    assert "WARNING" in out and "LITERAL characters" in out
    assert "may be this, not a real absence" in out


def test_W_a_clean_pattern_raises_no_warning(tree, monkeypatch, capsys):
    """Negative control: the warning must discriminate, not decorate every run."""
    _rc, out = _run(monkeypatch, capsys, "widget|gadget")
    assert "WARNING" not in out


def test_W_name_mode_does_not_warn_on_glob_syntax(tree, monkeypatch, capsys):
    """A glob is not a regex -- the BRE warning is scoped to content mode and must stay there."""
    _rc, out = _run(monkeypatch, capsys, "--name", r"*\(x\)*")
    assert "WARNING" not in out


def test_W_an_invalid_regex_falls_back_to_literal_rather_than_crashing(tree, monkeypatch, capsys):
    """An unbalanced paren must degrade to a literal search, not kill the rail an agent is forced
    to use -- AND MUST SAY IT DID.

    The fallback silently changes WHAT WAS SEARCHED FOR, from a pattern to a literal, and the
    results render identically to a successful regex search. That is the BRE warning's failure
    inverted: not a silent zero, but silent WRONG hits, which is the harder one to notice because
    the output looks like success.
    """
    rc, out = _run(monkeypatch, capsys, "widget(")
    assert rc == 0
    assert "not a valid regex" in out and "as a LITERAL" in out
    assert "tests/test_thing.py:2" in out, "the literal fallback did not actually search"


# --------------------------------------------------------------------------- contract
def test_no_args_prints_usage_rc0(monkeypatch, capsys):
    rc, out = _run(monkeypatch, capsys)
    assert rc == 0
    assert "comp-find <pattern>" in out and "--name" in out


def test_usage_names_every_band_it_accepts(monkeypatch, capsys):
    """The help must enumerate the same seven bands the filter validates against -- a help text
    listing a band the code rejects sends the agent at a dead flag."""
    _rc, out = _run(monkeypatch, capsys, "--help")
    for b in F._BANDS:
        assert b in out


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
