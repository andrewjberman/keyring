# CTO session — base reinstantiation through the MDPF staleness diagnosis (2026-08-07 1345Z → 2026-08-10 1605Z)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (primary), COORDINATE, SCRIBE

**Serial:** `1.0.0_SA_CTO` (base) · **Window:** 2026-08-07 ~13:45Z → 2026-08-10 ~16:05Z
(includes a weekend dormancy: zero commits fabric-wide 08-08/08-09) · **30 commits this author line.**

---

## What this window was

Fresh base-CTO reinstantiation on Andrew's order, ramped on the governance-night state brief, then
two distinct pushes: **08-07** — plan-of-attack, spawns, law repoint, and the MDPF remediation
program transitioning to this fabric; **08-10** — the MDPF served-staleness diagnosis, which
inverted twice and ended by refuting its own central claim.

## Commits — see commit messages for per-file detail

`5c5873f8d2` `54efb341e6` `620890b552` `9ddd6a4855` `3b3714e946` `02f12a2629` `087938fa61`
`3aac2c3e32` `1dbfcdac90` `f79a538ab9` `d40a12194e` `5261bde7a2` `22208eb2c9` `38c8edb1c6`
`3537aa8fbd` `63c9d269ff` `8b4e285cc2` `10cd135458` `69488ba070` `251605d939` `98c0991fb0`
`a3a9df7911` `5d9684ca69` `2a3b1ea408` `5411d0c0ac` `6559ad2b1d` `28908da66e` `a03f2ceb95`
`46d3bf3f32` `004588f9cb`

## Rulings issued

| ruling | disposition |
|---|---|
| **Rule-21 repoint** — `comp-grep`/`comp-glob` → `comp-find` | LANDED `@a3a9df7911`, law + router in one commit, exercised. Old binaries deliberately NOT deleted (consumers first, binary last) |
| **Arch-gate DISCHARGE** — 17 advisor-of-record files | `@10cd135458`. NEVER never-widen sign-off RETAINED |
| **C3.ii reuses the Kimi coverage contract** | Build Ladder rung 2; adopted from COO's finding |
| **CRO inherits `~C`'s VERTHARVEST spec** | decided at seat, not routed upward |
| **EC2 leg = CUTOVER RESIDUE** (R-31) | decommission, do NOT schedule. NEVER#4 does not fire on a deliberately-closed path |
| **Bronze prefix ownership** | `cot-rebalancer-runner` OWNS it. The mirror's guard is CORRECT but over-scoped — narrow the assertion, never disable |
| **INF-owned pulls** | DO NOT re-time. Move our own consumer |
| **Surfacing is discharged by the act of surfacing** | standing, fabric-wide |
| **PRD cadence input STRUCK, rule KEPT** | `@5c5873f8d2` |
| **§2.4 lock-in row ANNOTATED, not rewritten** | `@5c5873f8d2` |

## Andrew rulings received + recorded

`"All your recs are approved, proceed"` (6 calls, 08-07) · `"Yes their history should be persisted"` ·
`"Have 0.7.0_AE_CloudOps Handle it"` · the FLOW LAW (*"we make a plan, we complete the plan, we then
review the work"*) + surprise-channel routing · the four-month priority structure (08-10) ·
`"B on call 1, Call 2 … more clarity from 4.0.0_SA_CRO shortly, Call 3 A is fine"` (08-10).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | repointed + then dogfooded all window | **PASS** | found `cot-rebalancer-runner` via `page_%03d` key signature — the producer AWS enumeration missed |
| `comp-which` | `_run_primitive` repointed to comp-find | **PASS** | exercised: denied-grep intent now RESOLVES (907 hits, denominator printed) |
| `comp-state` | `--self-test` | **PASS 3/3** | gate cleared before the /exec-sum drift read |
| `comp-estate` | `--definitions` | **PASS** | C3.ii = "DECLARED never discovered" — the ruling's whole basis |
| `comp-pipescript` | `deployed --pipeline mdpf` | **PASS** | correctly REFUSED flagless (rc=2, no guess) |
| `comp-iam` / `comp-blast` | not run by me | — | COO ran `comp-blast` for the multi-entry census |
| `comp-trigger` | **deliberately NOT relied on** | **WARN** | COO measured a false-absence: interpolated names invisible to text search → reads "not in Terraform" → invites a console fix |

**What worked:** `comp-find`'s band classification + printed denominator; `comp-estate --definitions`
as a ratified-vocabulary source. **What failed:** `comp-trigger`'s false absence (above).
**Gap found:** CloudTrail cannot attribute writes on `opal-data-assets` — data-event selectors cover
two other buckets and are `ReadOnly`; access logging off; object `Metadata {}`. **NOT-MEASURABLE**,
reported as such.

## Blockers

**NONE at this seat.** Both spawned seats were BLOCKED-ON-CTO at 1513Z and were unblocked at
1515/1516Z; one of the two blocks was an already-issued ruling I had failed to confirm receipt of.

## Current State (zero-context handoff)

### THE STALENESS CAUSE IS FOUND AND IT IS NOT SCHEDULING
`mdpf-scheduled-floor` fires **13:00:5xZ daily** (08-08, 08-09, 08-10 confirmed). Three of four
scopes **REFUSE TO EMIT INSIDE IT**. The publisher then fires 13:50Z and **republishes the last good
content** — which is why all four served objects carry today's S3 mtime while their
`meta.generated_at` reads 08-07.

```
08-07 13:00:54Z  PASS (inflection), axis 439 dates -> 6/12, errors=[cottonwood, global]
08-10 13:00:59Z  FAIL limb (v),     axis 440 dates -> 3/12, errors=[cottonwood, inflection, global]
```

**LOCALISED (`0.7.0_AE_CloudOps` `@e026bc973c`): all 7 presence disagreements are on ONE date —
`2026-08-06` — and that date is exactly the one the axis GREW BY between the two fires.** Five
printed rows are Opal model bands (`opal_ultra_short_term` 12 · `opal_short_term` 29 ·
`opal_intermediate` 203 · `opal_long_term_conservative` 91 · `opal_long_term_aggressive` 32), each
`model_value=None account_count=<n>` — *"count and value disagree about whether this date exists."*
Limb (vi) **never fired** (`grep -c FOREIGN-DAY ROSTER` = 0).

⚠ **BOUNDS:** `pres[:5]` prints **5 of 7** — 2 rows are NOT-MEASURABLE from the log. `2026-08-06` is
also the date measured missing from **both** eclipse and orion feeds, and `ce99054e44` applied
`2026-08-06T00:04:48Z` — **two observations naming one date is a reason to look, NOT a conclusion.**
Cottonwood fails on a **different** error class (VALUE_DATE COLLISION) with a **rolling** value_date.

### FILES / RESOURCES a successor will open
- `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` — gate `:1569-1594`, evidence
  emitters `:1590-1594`, 49F skip `:1562-1567`
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_TRIGGER_SEQUENCE_DIAGNOSIS_20260810.md` — carries
  its own RESOLVED banner voiding its original framing
- `docs/architecture/MDPF_REMEDIATION_REGISTER.md` — R-25..R-32 banked this window
- `org/tier1_exec/1.0.0_SA_CTO/handoffs/2026-08-07_2330Z.md` — the cross-axis handoff

### CORRECTIONS TO MY OWN WORK (5, one class)
`22:30Z "cot" mirror is an INFLECTION intake` · `BD lands 06:00:44Z not 02:00Z (my anchor would have
fired 3.5h EARLY and installed this workstream's own defect)` · `the CAUSE column refuted, 49f
downgraded unprompted` · `the diagnosis was never in git when I told two seats to execute it` ·
`R-18's control misattribution`. **One family: reasoning from a description to a mechanism.**
Banked: `memory/feedback_a_reference_is_not_a_failure_reachable_and_counterpart.md`.

## Next Steps

1. **[1.0.0_SA_CTO]** Cottonwood causation — the `(a)`/`(b)` reads (what data date the 06:00:44Z
   write CONTAINS; what the floor actually reads for cottonwood). Mine, unstarted.
2. **[0.7.0_AE_CloudOps]** the 2 unprinted disagreement rows are only obtainable by re-running the
   gate or reading the source join — not from the log.
3. **[2.0.0_SA_COO]** strike W1-5's floor clause (Andrew ruled B); NNA backfill armed on RESTORED.
4. **[0.4.0_DS_ClientPlatform / not yet assigned]** INF rep-10 allowlist fix is **DISPATCHED BUT NOT
   LANDED** — verified `INFLECTION_REP_IDS` unchanged in git since 08-07. It gates the NNA backfill.
5. **[ANDREW]** re-lock §2.4 against measurement; the category axis (deferred to CRO).
