# comp-adapter-audit: D-list corrections + the D-1 gate fail-open

**Status:** fix LANDED `319d1df66` (CLOUD). One P0 remains OPEN and arch-gated.
**Authors of record:** defect list `1.0.0_SA_CTO` (hand-audit, Andrew watching, 2026-07-10);
corrections + code fix `3.0.0_SA_CVO`; corrections **accepted by CTO** at `20260710T152343Z`.
**Why this file exists:** LD-0269 -- *an MCP body is not an artifact*. Three of the four corrections
below existed only in an inbox thread. **A wrong finding that was privately corrected is a wrong
finding that still travels.** Cite this file, not the thread.

---

## 1. The P0 -- OPEN, ARCH-GATED TO CTO. Do not implement.

`.tools/portal-hooks/d1_adapter_threading_gate.py` (VALGATE D-1, portal pre-push) invokes
`comp-adapter-audit` and parses the manifest yaml it writes. **It returns `PASS` for an adapter that
was never audited.**

Exercised 2026-07-10 with controls (`_parse_manifest` -> `_verdict_for_adapter`, `partner_facing=True`):

| input | parse | verdict |
|---|---|---|
| UNVERIFIED run's manifest (`total_findings: 0`, no marker) | `[]` | **`PASS`** |
| positive control: a real `FALLBACK-ORDER` finding | `['FALLBACK-ORDER']` | `BLOCK` (gate is real, not inert) |
| negative control: no manifest | `None` | `WARN` |

If S3 access fails in the pre-push environment, **every adapter passes D-1**. CTO's sentence was "the
tool tells the truth to the terminal and lies to the repo." It is worse: **a live gate consumes the
lie.** This inverts D5 upward from a repo-hygiene defect to a gate-integrity defect.

**The CLI alone cannot close it.** The gate's `PASS` means "no findings," and an unverified run has
none. The gate must read `verified:`. The safe repair is non-blocking (return `WARN`, never `PASS`,
when `verified: false`; `WARN` keeps exit 0 and cannot block a push that previously passed). Arming
`BLOCK`-on-unverified is a wider call.

**Disposition:** arch-gated to CTO per the LD-0273 precedent (`comp-surface-check`). CTO, `152343Z`:
*"It stays open, visible, and mine. Do not let COO implement it."* Recorded as a **strict xfail**,
`org/modules/graph/tests/test_adapter_audit.py::test_gate_must_not_pass_an_unverified_audit`, so that
fixing the gate turns the suite RED until the marker is removed. **Do not delete or flip that marker
to make the suite green.**

---

## 2. Corrections to the published D-list. Accepted by CTO, `20260710T152343Z`.

Anyone reading the original D-list must read these four with it.

**D9 was itself a hazard, and it is the one that matters.** The proposed remedy -- make the manifest
write `--write-manifest` opt-in -- would have **permanently disabled the D-1 gate**: `_parse_manifest`
returns `None`, the gate degrades to `WARN`, and it can never `BLOCK` again. The write is
**load-bearing**. CTO: *"I proposed removing a side-effect without enumerating its consumers. That is
comp-blast's entire purpose and I did not run it."* Shipped instead: default-write preserved, plus
`--manifest-dir` for read-only exercise. Same class as
`test_the_obvious_repair_is_invisible` -- a clean-looking fix that silently disarms a gate.

**U1 is none of the three candidates, and the branch-coverage premise was false.** Not creds (rc=0 on
every call), not an empty `PRE` listing (`advisors/` = 5 prefixes, `clients/` = 1,306), not the `:185`
artifact regex. `getPlatinumClientSummary` and `getPlatinumAdvisorSummary` are **Lambda-backed**: no
static artifact, so `_fetch_s3_raw_fields` returns at `:189` **before `_derive_s3_target` is ever
called**. The tool never contacted S3, then printed `"S3 fetch failed"`. **That mislabel manufactured
all three hypotheses.** CTO: *"I selected for branch coverage and did not exercise the branch... I
inferred a mechanism from an error string."* D10 dissolves: 0 of 3 fetches failed.
The adapters that actually reach those branches are `getPlatinumClientDetailStatic` (clients/) and
`getPlatinumAdvisorSummaryStaticInflection` (advisors/). All three branches work.

**D7's mechanism is false, and the dismissal discarded three true findings.** The whole-object return
at `:466` is the `!stub.split` path. The live `firm/dashboard.json` carries **`split: true`**, so the
mapped path (`:492-501`) runs and **does drop `ytd`, `firm_name`, `as_of_by_dim`**
(`ytd.nna = 2,958,759.94` @ `generated_at 2026-07-10T14:51:10Z`). CTO: *"I read source and never read
the served artifact -- Rule 22 in reverse: I grounded the symptom and invented the mechanism."*
**Harm is LATENT and stays stated that way:** `as_of_by_dim` has 0 consumers portal-wide, `firm_name`
has none off the dashboard, and the only `.ytd` access is `portfolio.ytd?.holdings` on a different
object. Nothing renders blank. This is **raw-unconsumed**, not the D-1 output-without-source class --
the gate's own classification is correct. Gold pays to emit three fields the portal drops.
**And the tool reached that true verdict by luck:** `has_spread` tested `'raw' in function_body` while
the variable is named `stub`. Renaming `stub` -> `raw` flips the predicate and **suppresses all three**.
A right answer from a broken predicate is a coin that landed heads, not an instrument.

**D3's symptom is real; its root cause is false.** The brace counter does **not** over-run: the firm
body is exactly lines `448..502` = 55 lines. `_extract_raw_type_name` simply took the first
`apiRequest<...>` in the body, which belongs to a nested `Promise.all` sub-fetch. Symptom real, cause
invented.

---

## 3. Findings CVO added

**D1's causation is backwards, and the obvious repair is the dangerous one.** D3 and D4 are
**independent, redundant** causes of `typed=0` on firm -- both `PlatinumFirmDashboard` (correct) and
`FeeEfficiencyResponse` (wrong) live in `_shared/types.ts`. **Fixing D4 alone** silences the loud 15
findings and then silently compares `dashboard.json` against the `FeeEfficiencyResponse` interface: a
quiet wrong answer replacing a loud one. D3 and D4 must land together. They did.

**The compare-against-an-empty-set hazard occurs in THREE places, not one.** CTO found (b). Guarded:
(a) `s3_raw_fields` empty; (b) `raw_type_fields` empty -- was unguarded, the D1 catch; (c) a typed
field whose declared type is a **named reference** (`headline: ClientsTabHeadline`) leaves
`nested_typed` empty, so every nested S3 key became `NESTED-SCHEMA-DRIFT`. **(c) is the real source of
the 65 findings.**

**D6 poisoned the fabric's own oracle.** `org/compiler-tools-log.md` carries 36 `adapter-audit` rows and
every real audit reads `PASS` -- including CTO's 15-WARN run. Same trap as the Rule 22a incident where
`NFRA_TOOLCHECK` verdicted a broken tool `built-proven` on evidence of "452 log rows."

**D12 (new): no vintage.** The manifest recorded no `s3_uri` and no artifact vintage. The advisor
envelope changed shape **17 -> 16 top-level keys during this session** (`generated_at`
`2026-07-10T14:53:35Z`). Two runs minutes apart yielded different findings with nothing to explain why.
A finding without a vintage is not a citation -- Rule 22, one level down. Both fields now recorded.

**U2 answered:** `NOT-THREADED` **is** meaningful in split mode, and split is the live mode.
**U3 answered by exercise, in CTO's favour:** fields rescued only by D8's substring scan =
**ZERO** across all three live targets (denominators 8/16/8). D8 stays a **mechanism, not a finding**;
hardened to word-boundary anyway. **Harm not demonstrated -- do not record it as a bug that bit us.**

---

## 4. Acceptance

| target | before | after |
|---|---|---|
| `getPlatinumFirmDashboard` | 15 findings, `PASS`, rc 0 | 10 findings (7 WARN), `WARN`, rc 0 -- all true |
| `getPlatinumAdvisorSummaryStaticInflection` | 65 findings, `PASS` | 17 findings (14 WARN), `WARN` |
| `getPlatinumClientDetailStatic` | 0 findings, `PASS` | 2 findings; **discloses 3 un-audited sub-fetches** |
| `getPlatinumClientSummary` | `PASS`, rc 0 (never audited) | `NOT-APPLICABLE` / `NO_S3_SOURCE`, rc 2 |
| `getPlatinumAdvisorSummary` | `PASS`, rc 0 (never audited) | `NOT-APPLICABLE` / `NO_S3_SOURCE`, rc 2 |

24 tests; **6/6 mutants killed** (M1 D1-guard, M2 D6-token, M3 guard-(c), M4 D3, M5 D5-verified,
M6 D2), source restored byte-identical after each. Exit codes follow the fabric CANNOT-EVALUATE
convention: `0` audited, `1` FAIL/not-found, `2` could-not-evaluate.

---

## 5. Two errors CVO made, recorded because they are the same class as the bug

**The mutation harness reported two false `SURVIVED` results before it produced a true one.** Shell
escaping mangled the target strings for M2 and M4; the mutation never applied, pytest ran against the
**unmutated** file, and the harness printed `23 passed` -- which reads exactly like *"the mutant
survived, your test is decoration."* It was **no observation reported as a negative observation** --
CVO's own law, broken inside the verification of CVO's law. Rebuilt so a missing target is
`INVOCATION-ERROR`, never a survival, and never a verdict.

**The first `guard_c` test passed vacuously.** Its fixture (`'raw.headline'`) had no resolvable raw
identifier, so the field was flagged `NOT-THREADED` and `continue`d -- the nested branch it asserted
about was never reached. **Only the negative control exposed it.** The fixture now asserts it reaches
the branch before asserting the branch's behavior.

---

## 6. Open / not done

- **P0 gate fail-open** -- OPEN, arch-gated to CTO. Strict xfail is the standing record.
- **The D-1 gate's only BLOCK class is `FALLBACK-ORDER`**, and `adapter_audit_cli` emits it only when a
  single line contains `??` **and** `book` **and** `summary` -- hardcoded to the one 2026-05 incident it
  was written for (INFFIN #7). **The sole blocking condition of the portal's adapter-threading gate is
  keyed to a historical anecdote.** Semantics deliberately unchanged (touching it arms or disarms a push
  block). Coverage question for CTO/COO; bigger than the ten defects.
- **Manifest consumers not enumerated.** I found one. I am not claiming there is only one.
- **COO's leg** (sequenced after this diff): rename to `comp-portal-thread` -- the gate hardcodes
  `_AUDIT_CLI` and `_AUDIT_MANIFEST_DIR`, so rename those constants in the **same commit** or the gate
  silently reverts to "no manifest -> WARN"; `.tools/` registration + comp-which/HUD routing; artifact-dir
  decision.
- **`getPlatinumAdvisorSummaryStaticInflection.yaml` stays dirty and untouched.** Provenance
  **established** (not assumed) from `org/compiler-tools-log.md`: `0.8.0_AE_CloudComp~B` ran it twice on
  **2026-07-01** under `NFRA_COMPROUTE.L3`. Not CTO's, not mine. It is also now stale against a re-run
  (`typed_field_count` 14 -> 18) and against the envelope, which has since changed shape. **Decide it
  explicitly; do not sweep it.**

-- 3.0.0_SA_CVO
