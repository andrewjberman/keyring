# The field→call map is printed, and two of the four v1 fields have no call behind them — 0.6.0_AE_PartnerETL

**Date:** 2026-08-25
**Task Order:** ADVI_INSURE.TO-A1-AE (surface (a); cells INS-a-1, INS-a-2, INS-a-3)
**Status:** IN PROGRESS — AC2 COMPLETE; AC1/AC3 held on a sovereign vendor-egress call
**Session:** ~2204Z–2245Z
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (ADVI_INSURE PRD s.3, Andrew ~16:1xZ).

---

## Objective

Brought online by Andrew ~22:0xZ into a live GO from `2.0.0_SA_COO` (71566). One project this
instance: ADVI_INSURE surface (a). Deliver `INS-a-2` — the field→call map that
`0.4.0_DS_ClientPlatform~J` named as the binding reason they declined the gold builder, leaving four
acceptance criteria on their TO at UNCOMPUTABLE-BY-DEPENDENCY. AC1/AC3 held on Andrew's per-use
vendor-egress word.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `"how do I grep the repo"` (A.3 exercise) | forwarder RAN — 104/104 resolve bare **and** one executed |
| `comp-find` | `-i "insurance_exploration" --files` | 1 hit / 26652 — **the HAR-2 file is not in the estate**; redirected me onto the captured payloads |
| `comp-find` | `-i "insurancerelationshiplist"` / `"accountdetailsearch"` / `"insuranceCharacteristics"` | 11 / 43 / 34 hits over 26659 files; `insurancerelationshiplist` **SURFACED=0** — exists in no executable source |
| `comp-find` | `-i "session/token" --files` | 42 hits, SURFACED=6 → located the vehicle and the already-implemented auth authority |
| `to-check` | `--all --assignee 0.6.0_AE_PartnerETL` | `total=1 scanned=2111 unresolved_serials=0` |
| `proof-of-spec-check` | positional, with all three criterion ids | `RC=0 … violations=0 … VALID` |

**What worked:** `comp-find`'s BAND classification did the decisive work twice. `SURFACED=0` on
`insurancerelationshiplist` answered "does this call exist in code anywhere?" in one read, and
`SURFACED=6` on `session/token` found the vehicle after a filename-shaped search had missed it.

**What failed:** a raw `grep -rl` census over five file globs **timed out at 120s** and returned
nothing — I had reached for it instead of the rail. The rail answered the same question in seconds
*with* a denominator.

**Gap found:** none new. The `comp-find | head` trap and the DENOMINATOR-certifies-the-sweep caveat
both held as documented.

## Work Completed

### 1. Startup — `/watcher` + `org/XXX.md`
NOT REGISTERED at entry → registered (PID 21056). `ps` for my serial: **0 matches**, positive-controlled
against 28 `inbox-watch` processes fabric-wide, so the predicate was live and there was no orphan to
reap. Armed the persistent Monitor (task `bsefoausx`, confirmed `running` by `TaskOutput`). A1 serial
file written; A.2 audit-archive deferred (non-exec lane) with 2 findings to FINDINGS.md; A.3 PATH
**104 of 104 + exercised**. Drained 7 backlog messages. The GO (71566) landed ~90s after arming —
the arm proved itself live rather than by assertion.

### 2. `INS-a-2` — the field→call map (AC2)
Derived from captured payload bytes, the committed API catalogue and vehicle source. **Zero vendor
calls; the 49F principal was not touched.** Artifact: `ADVI_INSURE.TO-A1-AE_FIELD_CALL_MAP.md`
`@b2514ec61a`. Domain 10 v1 fields (PRD s.11 Rulings 2/3/6) → 6 supplied-measured, 1 recorded-only,
**3 ABSENT**, 0 unmapped, 6 calls enumerated, no ellipsis.

**The binding question, answered:** `currentEmv` comes from `RelationshipAccountDetailSearch`
(MEASURED on bytes) and is also listed on `accountdetailsearch`; `insuranceCharacteristics` comes
from `accountdetailsearch` **only** — the field name does not exist anywhere on the other call's
27-field projection — and its populated shape **has never been observed by anyone** (1 specimen
estate-wide, empty `{}`).

### 3. Four findings that were not in the decomp
1. **Two different `AccountDetailSearch` endpoints, and the sanctioned one masks the join key.**
   Ruling 2 joins "on account number"; `/portfolioreporting/*` returns `XXXX5115` and accepts no
   exact-number filter (Andrew-authorized live probe 2026-07-21, `taxsma_resolver.py:10-19
   @0ac99a72cb`). The unmasked key is only on the separately-gated `/account-api/*`. **The egress
   grant is load-bearing for the v1 join itself** — measured three weeks before Ruling 2 was written.
2. **Case-variant keys + a type divergence** across the two calls on the same account:
   `dataFormatID`/`dataFormatId`, `custodianID`/`custodianId`, `taxStatus` int `1` vs string
   `"Taxable"`. A parser keyed on one spelling returns `None` against the other and does not raise.
3. **`asOfDate` is four different dates on one record** plus `currentEmv`'s own `asOf`. Ruling 7's
   cadence trigger and Ruling 5's client-facing "statement as of MM/DD" both depend on which — and
   no estate evidence determines it.
4. **The primary evidence file is mis-named.** `account_detail_search.json` captures
   `RelationshipAccountDetailSearch`. **0 of 3 payload files hold an `/account-api/*` response**,
   while the catalogue calls that endpoint "the insurance-relevant endpoint".

### 4. Controls — exercised, not asserted
**Sealed planted mutant** on the load-bearing zero: copied the payload tree, planted one
`insuranceCharacteristics` object, re-ran the identical census → **0 → 1, FIRED**. The zero is a
measurement, not a blind instrument. **Determinism:** two same-input runs, census and the 27-field
extraction both identical → STABLE.

## Decisions Made

- **Did not act past the hold.** I measured that AC1's oracle is a SOURCE-layer claim and the vehicle
  already ships DRY-gated, so the *build* half looks reachable with zero egress. That is the issuer's
  call under a frozen spec, so I surfaced it and did not build.
- **Reported AC1 as `UNCOMPUTABLE-BY-CONSTRUCTION` with both halves printed** rather than a bare
  status — one half (both token authorities, `/session/token` distinct) is satisfied at source; the
  other (the insurance leg) does not exist. A single verdict would have hidden a satisfied check.
- **AC3 discipline applied pre-emptively.** Zero surfaces called means zero per-surface results, so
  the criterion is uncomputable — but each gap in the map names *its own* dependency and nothing is
  generalised to "insurance data is unavailable".

## Files Modified

| file | commit |
|---|---|
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/ADVI_INSURE.TO-A1-AE_FIELD_CALL_MAP.md` | `b2514ec61a` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/ADVI_INSURE.TO-A1-AE_PROOF_OF_SPEC.json` | this commit |
| `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-08-25/session_…_2200Z.md` | this commit |

## Blockers

**None.** The vendor hold is a **SPEC CONSTRAINT, not a blocker**, per the TO — explicitly not to be
reported as BLOCKED. AC1/AC3 return `UNCOMPUTABLE-BY-CONSTRUCTION` with the dependency named, which
the TO defines as a complete answer.

## Surprise channel — 5 items, all OBSERVATION, one ARMED and disarmed same-turn

Four are recorded in the proof-of-spec `surprises[]` (AC1 reachable without egress; the decomp's I3
scope; the masked join key; the mis-named payload). The fifth was **ARMED**:

⚠ **`.tools/proof-of-spec-check.py:245` crashes (`AttributeError`) when `decomp_ref` is a string, and
the crash exits `rc=1` — the same code as a legitimate INVALID verdict.** The TO's own comment
instructs callers to check the rc, so a crash and a verdict are indistinguishable to a compliant
caller. Reproduced on a **peer's committed instance**
(`0.7.0_AE_CloudOps/deliverables/ADVI_STITCH.TO-A1-AE_PROOF_OF_SPEC.json`), so it is not local to me.
**DISARM OWNER: `0.6.0_AE_PartnerETL`, same turn** — my instance was converted to the object form and
now validates `rc=0 / violations=0`, so no work of mine rides the defect. **DISARMED ≠ REMEDIATED:**
the tool fix and the peer's instance are not mine and are routed, not taken.

## Current State

AC2 **COMPLETE and validated** (`proof-of-spec-check` rc=0, violations=0, alignment 3/3 forward-1,
3/3 forward-2, 3/3 backward against a 22-cell decomp id space). `0.4.0_DS_ClientPlatform~J`'s gold
builder can now be specified against 6 measured fields plus the spine joins; it **cannot** be
specified against `carrier`/`product` without a populated specimen or a Ruling-6 amendment.

Commits landed **LOCAL on CLOUD**, riding integration — not yet on `origin/CLOUD`.

## Next Steps

1. Report AC2 to `2.0.0_SA_COO` with evidence (RAVC close on the startable third of the TO).
2. Await Andrew's per-use vendor-egress word. On GO: build the insurance leg (AC1), then exercise
   per-surface with denominators (AC3). On decline/defer: both stand as answered-with-dependency.
3. The issuer's call on whether the **build** half of AC1 releases ahead of the egress word.
