#!/usr/bin/env python3
"""test_comp_read.py -- acceptance battery for `.tools/comp-read` (NFRA_SCRIPTGEN Part B).

WEIGHTED TO THE FAILURE DIRECTIONS, NOT THE HAPPY PATH. comp-read exists to stop the
right-file-wrong-conclusion class (Andrew-direct 2026-08-05), so a battery that only proves it
renders output would pass against every specimen the tool was built for. Each test below names the
DEFECT it holds shut, and every one of them was a LIVE break in this tool at some point:

  W  match-CENTRED windowing      -- fixed-offset truncation cut the answer 3/3 on long rule lines
  B  BOLD-LED sectioning          -- '#'-only headings collapsed an incident file to ONE section
  T  TITLE must not outrank       -- a 2-line keyword-dense title beat every section with a body
  P  PLURAL folding               -- "detectors" vs "detector" had literally ZERO overlap
  C  CONTENT-KEYED ast cache      -- id()-keyed cache served ANOTHER FILE'S sections (demonstrated)
  U  UNPARSEABLE disclosure       -- a .py that failed to parse rendered as a structureless file
  L  UNREAD LEDGER + denominators -- the behavioral half; absence of it is the whole thesis lost

THE ANTI-FABRICATION ASSERTS ARE MUTATION-CHECKED. A test that passes today but would ALSO pass
against the defect is not a control, so W/T/C/U assert on the discriminating value, never on rc and
never on "some output appeared" (precedent: the rc=2 mutant that survives an rc-only assertion).

Fixtures are synthetic and written to tmp_path -- no estate file is read, so the battery cannot go
red because a doc was edited, and it asserts nothing about content it does not itself author.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]
_TOOL = _WS / ".tools" / "comp-read"


def _load():
    """comp-read is EXTENSIONLESS -- spec_from_file_location cannot infer a loader, so name one."""
    loader = importlib.machinery.SourceFileLoader("comp_read_under_test", str(_TOOL))
    spec = importlib.util.spec_from_loader("comp_read_under_test", loader)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["comp_read_under_test"] = mod
    loader.exec_module(mod)
    return mod


R = _load()


def _run(monkeypatch, capsys, *args):
    monkeypatch.setattr(sys, "argv", ["comp-read"] + [str(a) for a in args])
    rc = R.main()
    return rc, capsys.readouterr().out


# --------------------------------------------------------------------------- fixtures
_POSTMORTEM = """# MDPF Postmortem -- MDPF_REVAMP / MDPF_3FIRMS / MDPF_CANRTE

**Scope note.** Unrelated prose about scheduling windows and promote ordering.

**Finding.** Every mdpf detector we own keyed on the producer, so the mdpf defect class
was invisible to all of them for the whole window.
Supporting mdpf prose so this section carries real body tokens to score against.
A third mdpf line of body, deliberately, so the span defeats short-section damping.

**Remedy.** Something else entirely, about buckets and prefixes.
"""

# A >1000-char single line whose ANSWER sits at the very END -- the exact shape that a fixed-offset
# excerpt truncates. The token is unique so its presence cannot be satisfied by any other text.
_LONGLINE = (
    "# Doc\n\n"
    "**Rule 9.** "
    + ("padding words about unrelated matters " * 30)
    + " and the ANSWERTOKEN9 is that comp-iam is NECESSARY, NOT SUFFICIENT for a new bucket.\n"
)


def _write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return p


# --------------------------------------------------------------------------- W: windowing
def test_W_window_is_match_centred_not_offset_truncated(tmp_path, monkeypatch, capsys):
    """The answer sits ~1200 chars into a single line. A fixed-offset excerpt returns the padding.

    MUTANT this survives: `_window` returning `t[:width]` unconditionally. That renders the RIGHT
    file and the RIGHT line and still loses the answer -- right-file-wrong-conclusion one level
    down, inside the tool built to prevent it.
    """
    p = _write(tmp_path, "long.md", _LONGLINE)
    rc, out = _run(monkeypatch, capsys, p, "--for", "does comp-iam suffice for a new bucket")
    assert rc == 0
    assert "ANSWERTOKEN9" in out, "excerpt truncated before the answer -- offset, not match-centred"
    # and it must be an EXCERPT, not the whole line dumped (the panel is an index, not a substitute)
    assert "..." in out


def test_W_short_line_is_not_elided(tmp_path, monkeypatch, capsys):
    """Negative direction: a line under the window width is returned whole, with no ellipsis noise."""
    p = _write(tmp_path, "short.md", "# Doc\n\n**Rule 1.** the bucket answer is SHORTTOKEN7 here.\n")
    rc, out = _run(monkeypatch, capsys, p, "--for", "bucket answer")
    assert rc == 0
    assert "SHORTTOKEN7" in out


# --------------------------------------------------------------------------- B: sectioning
def test_B_bold_led_lines_are_sections(tmp_path, monkeypatch, capsys):
    """ONE '#' heading + three bold-led rules must yield >1 section.

    MUTANT this survives: `_sections_md` recognising only `_MD_HEAD`. That collapses this estate's
    postmortems and CLAUDE.md-shaped prose to a single section, so SALIENT renders "top 1 of 1" and
    comp-read adds nothing on exactly the corpus it is most used against.
    """
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    rc, out = _run(monkeypatch, capsys, p, "--for", "why did detectors miss the defect")
    assert rc == 0
    assert "4 section(s) via markdown-headings" in out
    assert out.count(" bold ") >= 3, "bold-led rules did not become sections"


def test_B_shape_prints_every_section_never_truncated(tmp_path, monkeypatch, capsys):
    """SHAPE is the denominator panel -- it declares its own count and prints that many rows."""
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "remedy")
    assert "SHAPE (all 4, never truncated):" in out
    shape = out.split("SHAPE (all 4")[1].split("SALIENT")[0]
    assert shape.count("\n    ") >= 4


# --------------------------------------------------------------------------- T: title damping
def test_T_keyword_dense_title_does_not_outrank_the_answering_section(tmp_path, monkeypatch, capsys):
    """The h1 title is PURE keywords -- 'mdpf' three times in a two-line section. The answering
    section is bold:5-9.

    THE QUERY DELIBERATELY CONTAINS 'mdpf' so the title actually scores; a query that misses the
    title would pass this test against the unfixed tool and measure nothing.
    MUTANT this survives: name weight 3.0 with no short-section damping -- the run-1 neutral corpus
    ranked the title at 9.90 while the one-sentence finding sat unranked.
    """
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    rc, out = _run(monkeypatch, capsys, p, "--for",
                   "why did our mdpf detectors miss the mdpf defects", "--top", "3")
    assert rc == 0
    salient = out.split("SALIENT")[1]
    first = [ln for ln in salient.splitlines() if ln.strip().startswith("[")][0]
    assert first.strip().startswith("[bold:5-9]"), "rank-1 was not the answering section: %s" % first
    assert "MDPF Postmortem" not in first


# --------------------------------------------------------------------------- P: plural folding
def test_P_plural_query_reaches_singular_text(tmp_path, monkeypatch, capsys):
    """'detectors'/'defects' must reach 'detector'/'defect'. Without folding the overlap is ZERO
    and the answering section does not rank at all (measured on the run-1 neutral corpus)."""
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    rc, out = _run(monkeypatch, capsys, p, "--for", "detectors defects", "--top", "2")
    assert rc == 0
    assert "NO region matched" not in out
    assert "[bold:5-9]" in out.split("SALIENT")[1]


def test_P_folding_does_not_strip_double_s(tmp_path, monkeypatch, capsys):
    """Bound the fold: 'class' must not become 'clas'. A stemmer that over-strips manufactures
    matches, which is the same failure as missing them, pointed the other way."""
    assert "clas" not in R._toks("class")
    assert "detector" in R._toks("detectors")
    assert "defect" in R._toks("defects")


# --------------------------------------------------------------------------- C: cache keying
def test_C_ast_cache_never_serves_another_files_sections(monkeypatch, capsys):
    """DEMONSTRATED DEFECT (2026-08-06): `_scan_tree` keyed on id(src), and CPython reuses the id of
    a freed string -- scan A, drop it, scan B, and B received A's sections. Collision reproduced on
    trial 10 of 200.

    This asserts the PROPERTY (content-keying) rather than racing the allocator, because a test that
    only passes when an id happens to be reused is a test that mostly passes for the wrong reason.
    MUTANT it survives: reverting `key = src` to `key = id(src)` -- the keys become ints and this
    fails immediately.
    """
    R._SCAN_CACHE.clear()
    R._TREE_CACHE.clear()
    R._scan_tree("def alpha():\n    pass\n")
    assert R._SCAN_CACHE, "nothing cached -- the test is measuring nothing"
    assert all(isinstance(k, str) for k in R._SCAN_CACHE), \
        "AST scan cache is identity-keyed; a freed id can be reused and serve another file's shape"
    assert all(isinstance(k, str) for k in R._TREE_CACHE), \
        "AST parse cache is identity-keyed; same collision, one layer down"


def test_C_two_files_in_one_process_get_their_own_shapes(tmp_path, monkeypatch, capsys):
    """End-to-end form of the same defect: reading two .py files in ONE process must not bleed."""
    a = _write(tmp_path, "a.py", "def alpha_one():\n    return 1\n")
    b = _write(tmp_path, "b.py", "class BetaTwo:\n    pass\n")
    _rc, out_a = _run(monkeypatch, capsys, a, "--for", "alpha")
    _rc, out_b = _run(monkeypatch, capsys, b, "--for", "beta")
    assert "alpha_one" in out_a and "BetaTwo" not in out_a
    assert "BetaTwo" in out_b and "alpha_one" not in out_b


# --------------------------------------------------------------------------- U: unparseable
def test_U_unparseable_python_says_so_loudly(tmp_path, monkeypatch, capsys):
    """A .py that fails to parse must NAME that, not render as a file with no structure.

    MUTANT this survives: the pre-fix fallthrough to `via whole-file`, which is BYTE IDENTICAL to a
    valid module that defines nothing. The reader is then told the file HAS no shape rather than the
    tool COULD NOT SEE it.
    """
    p = _write(tmp_path, "broken.py", "def f(:\n    pass\n")
    rc, out = _run(monkeypatch, capsys, p, "--for", "what does f do")
    assert rc == 0
    assert "UNPARSEABLE" in out
    assert "syntax error" in out.lower()


def test_U_unparseable_contradiction_zero_is_declared_blind(tmp_path, monkeypatch, capsys):
    """The CONTRADICTIONS detector needs the AST it never got. It must not print 'none detected'.

    This is the anti-correlated-pass class: an instrument that could not have said otherwise
    reporting a clean zero.
    """
    p = _write(tmp_path, "broken.py", "def f(:\n    pass\n")
    _rc, out = _run(monkeypatch, capsys, p, "--for", "anything")
    assert "NOT CHECKED" in out and "BLIND zero" in out
    assert "none detected" not in out


def test_U_valid_python_is_not_flagged_unparseable(tmp_path, monkeypatch, capsys):
    """Positive control -- the flag must discriminate, not fire on every .py."""
    p = _write(tmp_path, "ok.py", "def g(x):\n    return x\n")
    _rc, out = _run(monkeypatch, capsys, p, "--for", "what does g do")
    assert "UNPARSEABLE" not in out
    assert "python-ast" in out


# --------------------------------------------------------------------------- L: ledger / honesty
def test_L_unread_ledger_is_always_present_with_both_denominators(tmp_path, monkeypatch, capsys):
    """The forcing function. It does not make an agent read; it removes the ability to NOT NOTICE,
    so its ABSENCE is the whole thesis lost."""
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "remedy")
    assert "UNREAD LEDGER" in out
    assert "of 10 line(s)" in out and "of 4 section(s)" in out


def test_L_no_match_is_a_MEASURED_zero_naming_its_denominator(tmp_path, monkeypatch, capsys):
    """A zero must never read as 'the file does not say it'."""
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "quarkgluon zzz")
    assert "MEASURED zero over 4 section(s)" in out
    assert "Do not read this" in out


def test_L_qualifier_panel_counts_file_total_and_near_separately(tmp_path, monkeypatch, capsys):
    """QUALIFIERS is the load-bearing panel: it must print the FILE total beside the near-count, so
    a filtered view can never be mistaken for the file's whole qualifier set."""
    text = ("# Doc\n\n**Claim.** the loader is fine and reads the bucket.\n"
            "**Correction.** this is DEPRECATED and must not be used for the bucket.\n")
    p = _write(tmp_path, "q.md", text)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "bucket loader")
    line = [ln for ln in out.splitlines() if ln.strip().startswith("QUALIFIERS:")][0]
    assert "in file" in line and "near your regions" in line
    assert "!!" in out, "a STRONG qualifier (deprecated/must not) was not flagged"


def test_L_excerpts_are_verbatim_with_line_numbers(tmp_path, monkeypatch, capsys):
    """Rule 1 of the tool: NEVER SUMMARIZE PRIMARY TEXT. Every shown line carries its line number
    and its own bytes, so the output indexes the file and cannot become the thing agents satisfice
    on instead."""
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "mdpf detector producer")
    assert "5: **Finding.** Every mdpf detector we own keyed on the producer" in out


def test_L_authority_tag_separates_code_from_prose_about_code(tmp_path, monkeypatch, capsys):
    """WRONG AUTHORITY was specimen 1: a docstring read as the code. A docstring BODY line must tag
    DESCRIPTIVE (the first cut only checked the OPENING quotes), and a `help=` line AUTHORITATIVE."""
    src = ('def cli():\n'
           '    """usage: this tool detects the widget in every case.\n'
           '    it always detects the widget, no exceptions.\n'
           '    """\n'
           '    p.add_argument("--x", help="detects the widget only when --force is given")\n')
    p = _write(tmp_path, "cli.py", src)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "does it detect the widget")
    assert "DESCRIPTIVE" in out and "AUTHORITATIVE" in out
    doc_body = [ln for ln in out.splitlines() if " 3: " in ln]
    assert doc_body and "DESCRIPTIVE" in doc_body[0], \
        "a docstring BODY line tagged AUTHORITATIVE -- prose about the code reading as the code"


def test_L_contradiction_detector_catches_arity_drift(tmp_path, monkeypatch, capsys):
    """The `.owned-paths.yaml` specimen: prose documents a 2-arg call, the def takes 4. The claim
    and its disproof sat in one file and nobody read both."""
    src = ('# see `check_agent(serial, path)` for the rule\n'
           'def check_agent(serial, path, mode, strict):\n'
           '    return True\n')
    p = _write(tmp_path, "own.py", src)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "check_agent")
    assert "CONTRADICTIONS (1)" in out
    assert "documents check_agent() with 2 arg(s)" in out and "takes 4" in out


# --------------------------------------------------------------------------- contract
def test_missing_file_is_rc2_and_named(monkeypatch, capsys):
    rc, out = _run(monkeypatch, capsys, "no/such/file_xyz.md")
    assert rc == 2
    assert "not a file" in out and "no/such/file_xyz.md" in out


def test_no_args_is_help_rc0(monkeypatch, capsys):
    rc, out = _run(monkeypatch, capsys)
    assert rc == 0
    assert "comp-read <file>" in out


def test_no_question_says_so_rather_than_ranking_nothing(tmp_path, monkeypatch, capsys):
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    _rc, out = _run(monkeypatch, capsys, p)
    assert "no --for question given" in out
    assert "SHAPE (all 4" in out, "SHAPE must render without a question -- it is the denominator"


def test_at_line_pins_the_containing_section_into_the_ranking(tmp_path, monkeypatch, capsys):
    """--at is the escape hatch when salience misses: the section containing LINE is force-ranked.

    AND THE PIN MUST DECLARE ITSELF. A force-inserted section rendered identically to a section that
    EARNED rank 1 would let the reader's own override read back as the tool's judgement -- a
    self-comparison dressed as evidence.
    """
    p = _write(tmp_path, "post.md", _POSTMORTEM)
    _rc, out = _run(monkeypatch, capsys, p, "--for", "quarkgluon", "--at", "10")
    salient = out.split("SALIENT")[1]
    assert "[bold:10-10]" in salient
    assert "PINNED by --at" in salient and "did NOT rank on its own" in salient


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
