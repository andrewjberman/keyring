# NFRA_PYFIELD.TO-1 — PyFieldRecognizer build (1800–1900Z)

**archetype:** IMPLEMENT

**Agent:** `0.8.0_AE_CloudComp` (base) · **TO:** `NFRA_PYFIELD.TO-1.pyfieldrecognizer` @f6418f78e7
**Commit:** `50ff3747bf` · **PRD:** `docs/architecture/NFRA_PYFIELD_PRD.md` @004588f9cb

---

## Current State

`PyFieldRecognizer` is **built, tested, committed, and its coverage is published with both pins** —
`org/modules/graph/comp_recognizers_pyfield.py`, battery
`org/modules/graph/tests/test_comp_recognizers_pyfield.py` **43/43 PASS including six mutant
controls**, report
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_PYFIELD_COVERAGE_20260807.md`.

It is the **one** new component (PRD §3): the SDK engine, `emit_cse` and the CSE IR are used as-is,
and tree construction follows the inline `ast.parse` pattern the sibling `comp_recognizers_code.py`
already uses at this address — so no second component was added.

**Headline, in the only form the TO permits it:**
resolver=`pyfield-flowlocal/v2` · marker_set=`STRICT_DERIVED`@pandas-2.3.3 (n=227) · vintage
2026-08-07T183904Z · **SWEPT** `data/inf/scripts/gold` + `data/assets/scripts/gold` · **UNSWEPT**
`bd`, `cot`, `mdpf`, the assets monolith and **every silver tree** → **2,295 of 4,413 attemptable
Subscript NODES (52.0%)**; binding 1,555 / usage 478 / iterrows 262; 2,118 unresolved; **491
UNATTEMPTABLE and never scored as misses**; 408 `FLOWS_TO` edges over 124 files, 0 parse failures.

**Criterion 1 is enforced by construction:** `format_coverage()` raises without a `Pins`. The reason
is measured — sweeping the two pins on ONE identical corpus moves coverage **20.3% → 52.1%, a 2.6x
spread**, with no corpus change. The forbidden sentence appears nowhere in the deliverable.

### Three defects found in my own instrument

1. **The battery failed on its first run (39/41), and both failures were real.** The usage axis had
   no site it could ever fire on — the fixture's only marker method sat on an *annotated* param, so
   binding always won it. A green usage assertion would have been measuring nothing.
2. **The resolver delta was scored on the wrong quantity.** v1 and v2 both resolved 13 fixture sites
   — v2 by binding, v1 by falling through to the usage marker on the *same* site. On the total, v2
   reads as "adds nothing"; the 3.6x lift is only visible **per axis**. A number that ties for two
   different reasons is not a tie.
3. **iterrows: a stricter rule produced a BIGGER number (262 > my naive 237), which is backwards** —
   and that is what exposed a real shape: a module-level `for _, row in df.iterrows()` leaking into
   every function taking a `row` **parameter**, mis-calling `row["Records"]` as a column. Fixed.
   **Then the ablation falsified my own attribution:** I measured "24 shadowing sites" and was about
   to report the fix as a catch; run with and without the check on the real corpus it is **262 vs
   262 — zero false positives removed here.** It is a correctness guard against a shape this corpus
   does not contain. Recorded rather than sold.

### Denominator reconciled, not papered over

I count **4,904** string-literal subscripts where the PRD says 4,896. **CRO's own probe, re-run at my
seat on today's tree, also reports 4,904** — two independently written instruments agreeing, so the
delta is corpus movement since the PRD's read, not an instrument disagreement. 491 expr-base and the
v1/v2 binding figures (434 → 1,555) reproduce the TO exactly.

---

## Blockers

**None.** The TO is complete and nothing is waiting on me.

---

## FINDING ROUTED (surface, do not adjudicate) — the PRD's gap statement names a field that does not exist

PRD §2.1: *"`FLOWS_TO` (961) and `PROP_PASSES` (1382) are 100% `layer=portal`."*
**Measured at Phase 3** (`comp-kuzu` @ Nessie HEAD, pin == HEAD, DB age 0.2h):

- `FLOWS_TO` total **961** — all carrying **`layer=aws`**
- `layer` estate-wide has **three** values: `aws` 24,394 / `ms` 11,669 / `semctl` 5,092. **No
  `portal` layer exists.**
- Positive control: **961 of 961** have a src `node_id` containing `portal/`
- Negative control: **0** have a src containing `scripts/`

**The PRD's substance is CONFIRMED and now double-controlled** — field grain exists for the portal
codebase and is exactly zero on the python substrate. Only the *discriminating field* is wrong: the
portal-ness lives in the `node_id` path, not in `layer`. **It survived because the number was right.**
A reader re-deriving the gap with `layer='portal'` gets **0 rows, indistinguishable from a true
zero** — the exact trap PRD §5.2 warns about one line earlier.

Routed to **`1.0.0_SA_CTO~D`** (PRD author, `docs/architecture/` lane) and **`2.0.0_SA_COO`** (TO
issuer). **No edit made by me** — not my lane.

---

## Next Steps

1. **[me / whoever COO routes]** The 408 edges are **emitted but NOT loaded into the graph.** This TO
   built the producer; the graph-load leg was never in its scope and is not claimed. That is the
   next slice, and it is what makes `comp-pipescript` / `comp-dataflow` able to answer Andrew's
   migration question rather than merely be able to in principle.
2. **[me]** UNSWEPT trees remain unswept: `bd`, `cot`, `mdpf`, the assets monolith and **every silver
   tree**. The recognizer runs on them today — no code change needed — but no figure has been
   published for them and none should be quoted until one is.
3. **[`1.0.0_SA_CTO~D`]** The PRD §2.1 `layer=portal` records fix above.

---

## Compiler Tools

| Tool + command | Result | What it did / found |
|---|---|---|
| `comp-which "python field extraction recognizer"` | routed → `comp-find` | **No regression** — the @a3a9df7911 repoint holds; no `comp-grep`/`comp-glob` in output, which the TO named as the failure signature. |
| `comp-find "class .*Recognizer" org/modules/graph` | 16 hits / 413 files | **Rung-2 reuse target found**: the 5 sibling recognizers + the SDK ABC. `comp_recognizers_tsx.py:70 FlowsToRecognizer` is the portal producer whose seven-key schema I had to match. |
| `comp-find PythonAstFrontEnd` (+ positive control `TsxFlowsToFrontEnd`) | 11 hits, DEF at `infra/system/sdk/gensdk/...` | Resolved a PRD-vs-address question: the named front-end exists at the **second** SDK address, unwired to `org/modules/graph`. Chose the sibling inline-`ast.parse` pattern over a new cross-address coupling. |
| `comp-pydeps consumers comp_recognizer_sdk.py` | 5 consumers / 323 files scanned | **Phase 2 blast**: registry consumers are 5 sibling recognizer modules **only** — no gold script, no Lambda, no portal component, no IAM. Exactly the TO's stated expectation. |
| `comp-blast RecognizerRegistry` | NOT-FOUND (denominator 20,601 nodes) | Correctly distinguished **NOT-FOUND from "nothing breaks"** — a python class is not a graph node. Used `comp-pydeps` for the real answer instead. |
| `comp-kuzu` × 5 (Phase 3 census) | 961 / 961 portal-src / 0 scripts-src / 3 layer values | The census above, with both controls. Produced the routed finding. |
| `commit-gate.sh` | rc=0 (after 2 fixes) | Caught 3 × F541 f-strings-without-placeholders and 1 unused import (`locus_at`). Both fixed; battery re-verified green after the lint edits, not assumed. |
| `comp-to NFRA_PYFIELD.TO-1...` | OK | Race-free per-session TO context. |
| CRO's `pyfield_column_probe.py --self-test` | 0 failures | **Gate on lifting from it** — I did not lift from an unverified instrument. Then re-ran it on today's corpus as the independent oracle that reconciled 4,904. |

**Gap found:** none in the comp-tools themselves this session. `comp-blast`'s NOT-FOUND path and
`comp-find`'s denominator/band output both behaved exactly as designed and were load-bearing here.
