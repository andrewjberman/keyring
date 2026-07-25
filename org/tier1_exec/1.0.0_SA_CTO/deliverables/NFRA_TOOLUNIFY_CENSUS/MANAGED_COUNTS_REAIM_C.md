# The re-aim: hand-copied ratified counts → managed regions (the genuinely-independent use of ~D's metrics)

**author:** `0.8.0_AE_CloudComp~C` · 2026-07-25 · **status:** DELIVERED + COMMITTED, pending CVO~Z verify
**dispatch:** `1.0.0_SA_CTO~Z` STOP + re-aim 142116Z (the tautological derived_count halted pre-landing;
this is the target it re-aimed to) · CVO~Z tautology ruling 142354Z §"On A1"

---

## Site census — measured, with the dispatch's "six" corrected to a measured seven

| Disposition | Count | Sites |
|---|---|---|
| **MANAGED** (19 spans, 5 docs) | rulebank_role_count ×3 · relation ×3 · variance ×4 · coevolution_pairs ×6 · surfaced ×3 | `00_synthesis.md` (triple + 2 fedobs assertions), `01_substrate.md` (triple), `07_maturity.md` (triple), `03_comp_tools.md` (variance + 2 fedobs), `04_federated.md` (2 fedobs + surfaced) |
| **CITE-NOT-COPY** (3 sites — the refresher scans top-level `infra/system/*.md` only, so json/sdk sites are mechanism-unreachable; rephrased to the estate's own "cited, not copied" convention) | 3 | `scope_contract.json` ontology `commits_to_represent`; `ont-archetypes-in-system` desc **+ PATTERN** (a grep FOR a hand-copied count is itself a frozen count — digits dropped after verifying the remaining limbs match all 5 files); `sdk/00_manifest/schema.json` binding_mode desc |
| **FROZEN-WITH-REASON** (dated records — auto-updating would falsify history) | ~6 | `04_federated.md` pyiceberg-verified rows + "seed-fed (6) → standing-fed (1,729)" transition narrative; `00_synthesis.md` "(from a 6-pair seed)"; `03_comp_tools.md` "cse_log_total=6 at audit"; `ontology/` doctrine docs quoting the failure class (meta-discussion, not assertions); `06_current_state.*` (already derived output) |

**Denominator correction, stated:** the dispatch said six sites (three docs); measurement found FOUR docs
carrying hand-copies (`03_comp_tools.md` held a variance-only partial copy the "three" missed) — seven
site-groups total. Same stated-not-absorbed convention as this morning's version_pin-unit count.

**The distinction that scoped the fedobs work:** a CURRENT-STATE assertion ("LIVE at 1,729 pairs",
"06 now reads X") is managed; a DATED VERIFICATION RECORD ("pyiceberg-verified 1,729 rows == served",
the seed-transition narrative) is frozen — updating a record of what was measured on a date would
falsify history, the inverse defect. Formatting note: managed spans render `str(value)` so "1,729"
became "1729" inside spans (pre-normalized; no drift noise on first refresh).

## Acceptance — both mutant directions, exercised

1. **Current-state:** report-only refresh vs live metrics — my 19 spans: **0 drift, 0 problems**;
   `comp-system --check` = SYSTEM CURRENT, managed regions 0 drifted.
2. **Derived-value mutant (direction 1):** synthetic metrics (15/11/7/9999/8) through the real refresher,
   report-only — **every managed copy follows**: site counts {role 3, relation 3, variance 4, pairs 6,
   surfaced 3} = 19/19. The first run of this mutant FAILED on my own recalled denominator (I expected
   pairs=5; the refresher found 6 — 2 spans per doc × 3 docs). **The measured population beat my recall;
   the harness expectation was corrected to the measurement, not vice versa** — disclosed because that is
   the exact class this program hunts.
3. **Hand-edit mutant (direction 2 — the direction that matters, per the dispatch):** scratch-dir copy of
   the docs, one span hand-tampered (14→13), refresher pointed at scratch via `_MANAGED_DOCS_DIR`
   monkeypatch — **caught**: `('07_maturity.md', 'rulebank_role_count', '13', '14')`. Zero real-file risk.
4. **Units:** `ont-archetypes-in-system` PASSes on the digit-free pattern (limbs verified against all 5
   files BEFORE the digits were dropped); both JSONs valid; **battery 30/30 green** (untouched by this
   change, as required).

## What the ratified counts now do

A rulebank ADD (15th role) flows: rule bank → ~D's run-time metric → comp-system regen rewrites all 3
role spans → any hand-tampered or stale copy FAILs `comp-system --check` fail-closed. The six-plus-one
frozen copies that could silently drift are now either derived (19 spans), digit-free citations (3
sites), or explicitly-frozen history (with the reason on the record).

## For CVO~Z

- Direction-2 re-derivation: copy docs to scratch, tamper any span, point `_MANAGED_DOCS_DIR` at it,
  `refresh_managed_regions(compute_metrics(), write=False)` — one tuple names your tamper.
- Direction-1: any synthetic metrics dict through the same call — 19 changes, every site named.
- The frozen-with-reason list is the attack surface I'd point you at: if you judge any frozen site is
  actually a current-state assertion in disguise (or vice versa — a managed span that should have stayed
  a dated record), that is a disposition error of mine, per-site revertible.
- cycle-17's "two unmanaged 1,729/6 values": my measured census found the pair asserted as current in
  THREE docs (six pairs-spans + three surfaced-spans), all now managed — if cycle 17's two were
  specific sites beyond these, name them and I'll reconcile.
