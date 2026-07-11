#!/usr/bin/env python3
r"""comp-transform standing guard: a field used only inside a RETURN-TYPE-ANNOTATED useMemo is
rendered, not false-UNUSED.

Author: 3.0.0_SA_CVO~A. NFRA_TOOLPASS comp-transform (CTO GO 20260711T002344Z, gated fix).

THE DEFECT (found + source-established on PartnerAnalytics, NOT bd): comp-transform schema-check's
"UNUSED" verdict means "typed but never rendered." The rendered signal for a fetch var comes from
useMemo/useCallback field-access extraction (extract_transforms._extract_transform_chains). The
`_USE_MEMO` regex required `useMemo(() => ...)` and did NOT match the idiomatic-TS
`useMemo((): ReturnType => ...)` form -- so EVERY return-type-annotated useMemo was skipped and any
field accessed ONLY inside one read as FALSE-UNUSED. On PartnerAnalytics.tsx (4 annotated useMemos)
the field `views` -- accessed as `data.views.aua` in the AUA-donut useMemos -- was reported UNUSED,
though it is the component's primary data source. A dev told "views is unused" could delete it.

THE FIX (extract_transforms.py:_USE_MEMO): allow an optional `: ReturnType` between the empty param
list and the arrow (`useMemo\s*\(\s*\(\)\s*(?::[^=]+?)?=>`). After it, `chains PartnerAnalytics`
captures 3 more chains reading `data`, and `views` leaves UNUSED (11->10; the remaining 10 are the
genuine root-level unused fields with zero `data.<root>` access). Portal-wide chains 25->29, no
regression.

THIS TEST -- bidirectional, fully SYNTHETIC (.tsx source strings in pytest tmp_path; NO portal or bd
file is read): a field used only in an annotated useMemo is captured (the fix); a plain-useMemo
field and a direct-JSX field are captured (baselines); a genuinely-absent field is NOT (true
negative). The neuter-audit reverts `_USE_MEMO` to the pre-fix regex and asserts the annotated
field DROPS OUT -> the false-UNUSED returns -> proving the fix is load-bearing.

`fields_used()` is exactly the rendered-signal input to schema-check's `unused = type_roots -
rendered_roots`; a field present there cannot be flagged UNUSED. bd-CLEAN: comp-transform reads
portal/src only (source-confirmed), and this test reads neither -- it feeds source strings directly.
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

_GRAPH = Path(__file__).resolve().parents[4] / "org" / "modules" / "graph"
sys.path.insert(0, str(_GRAPH))


def _load():
    spec = importlib.util.spec_from_file_location("extract_transforms_sut", _GRAPH / "extract_transforms.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["extract_transforms_sut"] = m
    spec.loader.exec_module(m)
    return m


M = _load()

# The pre-fix regex, kept verbatim for the neuter-audit (proves the fix is load-bearing).
_OLD_USE_MEMO = re.compile(
    r'const\s+(\w+)\s*(?::\s*[\w<>\[\]|]+\s*)?=\s*useMemo\s*\(\s*\(\)\s*=>\s*\{?')

# NOTE ON FIDELITY: _extract_jsx_refs has a SECOND capture path -- it matches the component's own
# `function Widget()` declaration as an inline function and scans the next ~1000 chars of its body
# for `data.<field>` (extract_transforms.py:452-471). In a TINY component every access falls inside
# that 1000-char window, so annotatedField would be captured EVEN with the broken regex, and the
# neuter-audit could not bite (observed: the first draft of this fixture false-passed the neuter).
# The real defect lived on PartnerAnalytics.tsx (2375 lines) where the `views` accesses at L198+ are
# far outside that window, so ONLY the useMemo chain could reach them. The padding below reproduces
# that: it pushes the annotated-useMemo field access past the 1000-char fallback window, so the
# annotated-useMemo CHAIN is the sole path -- exactly the condition under which the regex fix matters.
_PAD = "  // ---- filler to push the annotated useMemo past the 1000-char body-scan window ----\n" * 18

_TSX = """\
import {{ useQuery }} from '@tanstack/react-query'
import {{ getThing }} from '@/api/endpoints/thing'

export function Widget() {{
  const {{ data }} = useQuery<ThingResponse>({{ queryKey: ['t'], queryFn: () => getThing() }})
{pad}
  // accessed ONLY inside a RETURN-TYPE-ANNOTATED useMemo, and PAST the body-scan window above,
  // so the annotated-useMemo chain is the ONLY path that can render it (the pattern the fix restored)
  const donut = useMemo((): number | null => {{
    return data.annotatedField.x
  }}, [data])

  // accessed inside a PLAIN useMemo (always worked -- baseline, independent of the fix)
  const plain = useMemo(() => {{
    return data.plainField.y
  }}, [data])

  return (
    <div>
      {{data.jsxField}}
      {{donut}}
      {{plain}}
    </div>
  )
}}
""".format(pad=_PAD)

_TYPES = """\
export interface ThingResponse {
  annotatedField: Foo
  plainField: Foo
  jsxField: string
  unusedField: string
}
"""


def _used(tmp_path):
    (tmp_path / "types.ts").write_text(_TYPES, encoding="utf-8")
    comp = tmp_path / "Widget.tsx"
    comp.write_text(_TSX, encoding="utf-8")
    flow = M.build_component_dataflow(comp, tmp_path)
    assert flow is not None, "the fixture component failed to parse"
    return flow.fields_used()


def _has_field(used, field):
    return any(field in p for p in used)


def test_field_in_annotated_usememo_is_rendered(tmp_path):
    """THE FIX: a field accessed only inside `useMemo((): T => ...)` must be captured -> not UNUSED."""
    used = _used(tmp_path)
    assert _has_field(used, "annotatedField"), (
        f"a field used only in a return-type-annotated useMemo was NOT captured -> it would be "
        f"reported false-UNUSED. used={sorted(used)}"
    )


def test_field_in_plain_usememo_is_rendered(tmp_path):
    """BASELINE: the plain `useMemo(() => ...)` form (always matched) still captures its field."""
    assert _has_field(_used(tmp_path), "plainField"), "a plain-useMemo field regressed"


def test_field_directly_in_jsx_is_rendered(tmp_path):
    """BASELINE: a field read directly in JSX (`{data.jsxField}`) is captured."""
    assert _has_field(_used(tmp_path), "jsxField"), "a direct-JSX field was not captured"


def test_genuinely_absent_field_is_not_rendered(tmp_path):
    """TRUE NEGATIVE: a typed field never accessed anywhere must NOT appear as rendered (so it is
    correctly UNUSED). Without this control a tool that marked everything rendered would pass above."""
    assert not _has_field(_used(tmp_path), "unusedField"), (
        "a field that is never accessed was reported as rendered -- the UNUSED verdict would never fire"
    )


def test_reverting_the_regex_reintroduces_the_false_unused(tmp_path, monkeypatch):
    """NEUTER-AUDIT / non-vacuity: swap `_USE_MEMO` back to the pre-fix regex. The annotated-useMemo
    field MUST drop out of the rendered set (the false-UNUSED returns) while the plain-useMemo and
    direct-JSX fields survive -- proving the fix is what captures the annotated form, and that this
    test discriminates the fix from its absence."""
    monkeypatch.setattr(M, "_USE_MEMO", _OLD_USE_MEMO)
    used = _used(tmp_path)
    assert not _has_field(used, "annotatedField"), (
        "with the pre-fix regex the annotated-useMemo field should be INVISIBLE (that was the defect); "
        "it was captured anyway -> this test is not actually exercising the regex fix"
    )
    # the fix is specific: the always-captured forms must still be captured under the old regex
    assert _has_field(used, "plainField"), "plain-useMemo capture must be independent of the fix"
    assert _has_field(used, "jsxField"), "direct-JSX capture must be independent of the fix"
