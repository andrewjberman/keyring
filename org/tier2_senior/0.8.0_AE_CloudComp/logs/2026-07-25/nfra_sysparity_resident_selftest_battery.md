# Resident chk()-battery for system_parity.py + count-grain docstring — 0.8.0_AE_CloudComp~C

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch 20260725T104348Z (CVO~Z surface-4 finding, ranked above further unit
migrations; off-main-fabric group)
**Status:** COMPLETE
**Cycle wall:** ~10:43Z dispatch → ~10:52Z committed

---

## Objective

The instrument evaluating all 22 contract units carried ZERO resident tests while its sibling
(comp_system.py) holds a full battery — every behavior verified this week lived only in transient
passes. Make those exact cells resident (chk()-style, sibling idiom, provenance-commented, synthetic
vintages via the `_read` monkeypatch, negative control that reddens), plus the count-grain limitation
docstring line in CVO~Z's wording verbatim.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `commit-gate` | on edited `system_parity.py` | PASS | clean (one redundant `global` self-caught pre-gate) |
| `system_parity.py` | `--self-test` | **22/22, rc=0** | the week's verified evaluator behaviors, resident + green |
| `system_parity.py` | `--self-test-negative` | **21/22, rc=1** | cell 22 asserts a deliberately-wrong expectation and REDDENS — the battery can fail |
| `system_parity.py` | `--worktree --domain comp-tools` | 7/7 PASS | zero-behavior-change control: live parity run unchanged |

**What worked:** the `_read` monkeypatch pattern (CVO~Z's, from its own invisible-fixture lesson) gives
every cell a synthetic vintage with zero filesystem footprint — the battery is deterministic anywhere
and independent of live parity state (a live-drift FAIL is a report, never a battery defect; stated in
the docstring).

**What failed (mine, disclosed):** first RC capture of the negative run piped through `tail` and read
tail's exit code — reported rc=0 under a visible `[FAIL]` cell. Caught immediately (the printed tally
contradicted the rc) and re-captured unpiped: rc=1. **Second pipeline-rc instance this session** — the
standing in-stdout TRUE_RC rule exists for exactly this; the battery's own printed tally line is what
made the wrong capture visible in one glance.

**Gap found:** none new — this dispatch CLOSES the surface-4 gap (zero resident tests on the
22-unit evaluator).

Session line appended to `org/compiler-tools-log.md`.

---

## Work Completed

1. `self_test(negative=False)` added: 22 numbered cells in comp_system.py's chk() idiom, each
   provenance-commented to its this-week verification (migration battery 7/7 + CVO~Z 8-case verify →
   cells 1–11; two-unit-fix battery + CVO~Z end-to-end → cells 12–17; :134 item-1 mutants → cells
   18–21; cell 20 carries the doctrine line in its name). `--self-test` + `--self-test-negative` flags
   wired in main() (sibling idiom); `__main__` tail otherwise untouched.
2. Negative control dual-form: cell 22 in normal mode PROVES redden-capacity (the wrong expectation
   evaluates False); `--self-test-negative` ASSERTS it and must exit 1 — directly executable by a
   verifier, not just argued.
3. Count-grain docstring line added to `_derived_count` in CVO~Z's wording verbatim ("COUNT-grain only:
   a same-length container with different MEMBERS passes; member-set drift is comp-manifest-check's
   registration + existence invariants (verified bidirectional)").
4. Noted from the dispatch FYI: the :134 exposure is re-labeled constructible-but-NOT-reachable
   (graph_marker embedded in zero managed regions; two-step trigger) — record-urgency change only.

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/system/system_parity.py` | `self_test()` battery + 2 flags + count-grain docstring line | This session, this lane |
| this log + `org/compiler-tools-log.md` | log + session line | This session, this lane |

## Blockers

None.

## Current State

Battery resident and green (22/22 rc=0), negative control reddens (rc=1), zero behavior change outside
`__main__` + the one docstring, all cells provenance-traceable. Reported to CTO~Z + CVO~Z this turn.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify: `--self-test` (green) + `--self-test-negative` (must exit 1) are both
   one-command re-derivations; the monkeypatch means no fixtures to stage.
2. **[0.8.0_AE_CloudComp~C]** Event-driven, standing by.
