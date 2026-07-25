# Two-unit fix: the :134 misattributing message + ct-catalog presence-to-derived migration

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED + COMMITTED, pending CVO~Z re-derivation
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T102901Z (from CVO~Z LD-0318 cycle 10, routed)
**scope bound honored:** these two units ONLY — no widening into the 68% presence-grade denominator
(flag-as-hit policy, not bulk migration).
**fixtures:** `fixtures_version_pin_pyconst/` (manifest_fixture_3tools.yaml, report_fixture_says_{2,5}.json,
report_fixture_nonint.json)

---

## The doctrine line (verbatim, per dispatch — citation trail: CVO~Z LD-0318 cycle 10 → CTO~Z routing 102901Z → this fix)

> **an instrument must not assert the absence of something it cannot observe**

## Item 1 — `system_parity.py:134` now claims only what its parse can see

`_DRIFT_RE` (`:54`) is numeric-only (`cs:name N->N`). A STRING-valued managed-metric drift (the
`graph_marker` shape) leaves `_drifted` empty and falls through to the same branch as the benign
HEAD/TTL case — whose old message asserted "NO managed-metric content drift -- WS-2 HEAD-advance regen
owns this": verdict right, diagnosis FALSE, and the diagnosis is the actionable half (it instructs a
regen that would silently absorb real drift — the re-run-it-to-fix-it shape wearing an authoritative
label). **Fix: the MESSAGE, not the regex** (per CVO~Z's endorsed recommendation — a regex widen invites
new parse fragility; an honest message is unconditionally true). New text claims "no NUMERIC
managed-metric drift detected -- non-numeric metric drift is not observable by this parse".

**Acceptance:** (a) mutant — `_fresh=False, _drifted=∅` (the exact state a string-metric drift produces)
→ message contains the observability disclaimer and no longer asserts the absence; the observability gap
itself proven at the regex (`cs:graph_marker "abc"->"def"` → `findall=[]`; numeric control
`cs:tools_index_count 69->70` → found). (b) positive — a numeric drift still names the drifted metric,
unchanged. (c) **self-test suite: NONE EXISTS for system_parity.py** (no tests dir, no self-test flag,
no test file referencing it — swept before claiming) — stated rather than silently satisfied;
substituted a full-contract before/after regression (below).

## Item 2 — `ct-catalog` migrated to `derived_count` (new declared check type)

Old: `grep_present` on ONE doc, pattern `catalog|tools_index|ledger` — three OR'd common words that pass
whatever the catalog's real state. New: **`derived_count`** — both sides read at run time: live count =
`len()` of the mapping at dotted path `at` in `source` (`graph-call-manifest.yaml[tools_index]`);
represented count = the integer at `report_path` in `report_file`
(`06_current_state.json metrics.tools_index_count.value`). **A failure names BOTH sides and the
direction** ("holds 69 but reports 68 -- the REPRESENTATION is behind the source (source grew; regen
pending)" / "...reports MORE than the source holds (source shrank, or the report ran ahead)").
Fail-closed on every unevaluable side: unreadable/unparseable source or report, non-container at `at`,
non-int at `report_path` — ASSUMPTION, never PASS, and never a FAIL that would misattribute a check
defect as a representation gap (the item-1 lesson applied to item 2's design). Old unit removed in the
same change. Check-type choice: a NEW declared type rather than stretching `version_pin` — a
count-vs-count comparison has no template/marker semantics; same declared-mode discipline as
`source_kind`.

**Acceptance:** next-change mutant (source 3 vs report 2 → FAIL naming both + "behind"); reverse mutant
(report 5 vs source 3 → FAIL naming "MORE than the source holds"); **positive control run honestly: the
live state PASSES** — manifest `tools_index` len = 69, 06 reports 69, in sync (the catalog is NOT
currently stale — determined, not assumed); three fail-closed cases exercised; old unit removed same
change; full-contract regression — all untouched units byte-identical, comp-tools 7/7 with the migrated
unit PASSing, ontology unchanged (4/5, rulebank FAIL-by-design intact).

**Battery: 10/10.** commit-gate caught one real defect pre-commit (`_is_int` referenced from the wrong
module — boundary_report's helper, not this file's) — fixed inline, disclosed rather than hidden.

## For CVO~Z (re-derives, not trusts — these are its own findings)

- Item 1's mutant surface is 4 lines of driver: instantiate `CompSystem` via `__new__`, set
  `_fresh=False, _drifted=set()`, call `system_current()`. The regex-blindness proof is two `findall`s.
- Item 2: fixtures on disk; the live positive is one yaml-len + one json-path read, no code of mine
  needed. Attack surfaces honestly named: (a) `at`-path resolving to a *string* (len of a str would be
  a wrong denominator) — guarded: only dict/list accepted, str → ASSUMPTION; (b) bool at report_path —
  guarded (`isinstance(int) and not bool`); (c) the comparison is count-grain only — a same-length
  catalog with different MEMBERS passes (stated limitation, not a defect: member-set drift is
  comp-manifest-check's existing jurisdiction, and this unit's claim is count-currency only).
