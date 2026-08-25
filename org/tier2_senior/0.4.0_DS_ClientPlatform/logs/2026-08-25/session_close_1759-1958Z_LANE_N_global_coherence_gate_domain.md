# 0.4.0_DS_ClientPlatform~N -- global's 5-day dark: the coherence gate was applying clause (vi) outside its domain (2026-08-25 17:59-19:58Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

Lane `~N`, seated by `2.0.0_SA_COO` 70998 on ONE project. Lane folder does not exist; logged under
the base with the lane named in the title.

## Current State

**GLOBAL IS RESTORED.** Served `platinum/mdpf/global/aggregate-aua-timeseries.json` reads
`as_of_last = 2026-08-24`, `_provenance.source_keys` =
`s3://opal-data-assets/portal/gold/mdpf/global/aggregate-aua-timeseries/2026-08-24.json`,
`n_dates = 461`. Five client-facing days closed. **The restore act is `1.0.0_SA_CTO`'s**
(Andrew-direct ~19:42Z), not this seat's -- see Attribution below.

**THE DEFECT, and it was not what anyone thought.** `global` had refused to emit since
2026-08-20T13:31:05Z on `(vi) FOREIGN-DAY ROSTER: 1` / `2026-08-19: 7791 -> 8260 -> 7791`.
**There was no foreign-day roster.** In
`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`, clause (vi) of
`_assert_cross_axis_coherence` compares `tot[i-1], tot[i], tot[i+1]` where `tot` is a **SUM OVER
LEGS WHOSE MEMBERSHIP VARIES BY DATE**. Cottonwood contributes a roster on **18 of 461** dates, and
`2026-08-19` is the **only** date in the series whose neighbours BOTH lack it -- so cottonwood's own
measured roster (`228+11+109+109+12 = 469`) entered and left beside its own measured values, and the
clause read that step as a roster imported from another day.

Arithmetic, reproduced from the leg artifacts independently of the pipeline:
```
49F core 7144 + inflection 562 + 49F SMA carry 85 (both frozen 2026-07-17) = 7791   <- the gate's a, c
7791 + cottonwood 2026-08-19 469                                           = 8260   <- the gate's b
```
49financial and inflection do not move at all across the three dates.

**WHY IT SURFACED ONLY ON 08-24:** clause (vi) loops `range(1, len(dates)-1)` -- **the last date is
structurally untestable.** `global`'s last good artifact ended at `2026-08-19`, so the island sat on
the one index the clause could not reach. The cottonwood repair extended the series and made it
interior. *The defect did not appear; its TESTABILITY did.*

**VENDOR SIGNATURE (outlives this fix).** `meta.value_date_rekey`: BD partitions carry an internal
value date lagging the partition date, and **FIVE partitions -- 08-20, 21, 22, 23, 24 -- all collapse
onto `value_date 2026-08-19`.** Black Diamond kept DELIVERING while every delivery carried 08-19
valuations, so nothing watching ARRIVAL could see it. Value dates 08-18, 08-20, 08-21 were never
delivered -- 08-19 is a **permanent** island, so waiting was ruled out on measurement, not preference.

**THE FIX (`1234c8779e`):** a DOMAIN PRECONDITION -- clause (vi) compares a triple only where the
same legs contribute a roster at i-1, i, i+1. Membership is **accumulated by the composition itself**
(a leg is recorded only where it actually appends a count), not re-derived. Skips are LOGGED with
their dates and leg sets. `count_membership` defaults to `None`, so every per-firm call site is
byte-identical to before.

**DEPLOY:** `mdpf-gold-lambda` **VENDORS** the module -- it fetches no code from S3, so the
`code/scripts/gold/` sync does not reach it. Shipped by `0.5.0_AE_OpalETL~B` at hotfix pin
`530ba66971` (= `1234c8779e` cherry-picked onto deployed pin `1daf1913dd`), applied 19:38:55Z.
Deployed package verified from the LIVE function: spine 175,795 B, `count_membership` = 14;
consolidator 55,629 B, `scopes_for` = 0 (D1_CATVIEWS absent).

**LEDGER:** `org/critical_paths/change_management/mdpf-global-coherence-clause-vi-domain-20260825.md`
-- **CLOSED** at `222fdf3042`, amended through `4abb254713`. All 8 commits ON `origin/CLOUD`.

## Work Completed

| # | Item | Evidence |
|---|---|---|
| 1 | Diagnosed the refusal; falsified the handed lead | every S3 read site in the gate script enumerated -- `_aggregate_aua/{date}.json` is read by NONE of them (different producer `mdpf_aggregate_aua.py:80`, different consumer `build_mdpf_etf_ownership_timeseries.py:76`) |
| 2 | Arithmetic closure + island census | 7791/8260 reproduced from leg artifacts; **1 isolated contributing date in 461** |
| 3 | Fix + committed control set | `1234c8779e`; `tests/test_cross_axis_membership_domain.py`, 5/5, no S3/network |
| 4 | Four-arm control set vs the REAL implementation | A refuses [08-19] / B passes / C refuses [07-06, 08-19] / D refuses [07-06] |
| 5 | Caught a defect in my OWN first patch | keyed on `d in cot_covered` (62 dates incl. 44 INTERPOLATED where the band contributes values but never counts) -- found by exercising `_cot_provenance_maps`, not by trusting my reimplementation of it |
| 6 | Second-blocker test nobody asked for | `_assert_global_composition` (`:2601`) sits AFTER the failing gate and had **no evidence either way** in 5 days -- exercised it, PASS |
| 7 | Vendor-scope measurement before AE built | 21 manifest entries hashed vs the pin: **2 would change**, the second being 6 un-deployed D1_CATVIEWS commits (+15,275 B) |
| 8 | Exercise gate through the PRODUCTION entry point | tree identity 21/21 vs pin FIRST, then `lambda_handler({"qa_local":true})` -> green, 12/12, `global as_of_last=2026-08-24`, CATVIEWS absent |
| 9 | Deployed-bytes verification from the live function | matched pin on both members; `CodeSha256` deliberately NOT used as the claim |
| 10 | Ad-hoc invocation (COO-assigned) | `{"status":"green","errors":[],"a4_objects_built":12}` -- discharged the residual that local py3.12 left: the deployed package in py3.11 + real layers + real IAM is now EXERCISED |
| 11 | AC4 both arms | 49financial 12,310 leaf fields -> **1** differing; inflection 12,375 -> **1**; both `_provenance.written_at` |

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| `comp-which` | "where is the cross-axis coherence gate" | PARTIAL | routed to `comp-find`; no rich tool for source-location |
| `comp-find` | `-i "FOREIGN-DAY ROSTER"`, `-i "mdpf_revamp/_aggregate_aua"` | PASS | located the gate + the two distinct `_aggregate_aua` owners; denominators printed |
| `comp-pipescript deployed` | `--pipeline mdpf` | PASS | STALE verdict that started the deploy-path investigation |
| `comp-pipescript postdeps` | `--firm mdpf` | WARN | **UNCOVERED** -- honest tool-blindness, correctly NOT read as zero-deps |
| `comp-find --name` | `mdpf-daily-dispatch.sh`, `build-and-upload*` | PASS | resolved the EC2 dispatch + ruled out the wrong deploy mechanism |
| `comp-aws` | `mdpf-gold-lambda` | FAIL | not a resource-lookup tool; wrong subcommand shape |

**What worked:** `comp-pipescript deployed --pipeline mdpf` printing STALE with both md5s is what
made the vendored-Lambda question askable at all. `comp-find`'s denominators were load-bearing every
time.
**What failed:** `comp-aws <name>` is not a describe-a-resource entry point despite the HUD nudge
suggesting it for exactly that.
**Gap found:** **nothing in the estate maps a SCRIPT to its EXECUTOR.** `comp-pipescript deployed`
answers "is the S3 copy current" and is silent that a Lambda VENDORS the same module -- the deployed
copy read MATCH-able while the executing artifact was 5 days stale. This is `1.0.0_SA_CTO`'s D10
motivating instance (71206). Surfaced, not built.

## Briefs Written (DS role addition)

| To | Msg | Subject |
|---|---|---|
| `2.0.0_SA_COO` | 71xxx | DIAGNOSIS: cause found, NOT a foreign-day roster (+ remedy classes A/B/C) |
| `2.0.0_SA_COO` | 71xxx | EVIDENCE for remedy (C): the four-arm control set |
| `1.0.0_SA_CTO`+`2.0.0_SA_COO` | 71143/4 | URGENT: CTO was briefing Andrew on a retired blocking act |
| `2.0.0_SA_COO`+3 | 71194-6 | HOLD the fire: the SCHEDULED executor is the Lambda, pre-patch |
| `0.5.0_AE_OpalETL~B` | 71xxx | HANDOFF: exact bytes to vendor, + the push is not a prerequisite |
| all | 71209/71242 | vendor scope measured; then: NEITHER pairing is exercised |
| all | 71267 | EXERCISE GATE: PASS, with the three residuals it does NOT cover |
| all | 71323 | `trigger.kind` cannot attribute a run |

## Attribution (recorded against my own interest)

The gold write is **19:44:22Z**; this seat fired **19:45:21Z**. Two invocations exist
(`5aa64b78` 19:44:22Z, `51e5f8dc` 19:45:54Z); mine completed green but `conditional_put` found
byte-identical content and correctly no-op'd. **`1.0.0_SA_CTO` claimed it (71318), Andrew-direct.**
I **withdrew** my own "two ad-hoc runs, doubly-owned edge" framing: it was two authorization chains
~40s apart (`2.0.0_SA_COO` assigning me 19:41:22Z; Andrew instructing CTO ~19:42Z as COO went
non-live), both legitimate. `0.5.0_AE_OpalETL~B` withdrew their amplification of it and corrected me
usefully: I called `conditional_put`'s no-op luck; it is a **designed idempotency control working**.

## Blockers

**None.** Nothing is held on this seat and nothing is owed by it.

## Next Steps

1. **[`1.0.0_SA_CTO` -- OWNED; corrected 21:2xZ, this log first said UNOWNED]** The **2026-08-26
   scheduled acceptance**. `1.0.0_SA_CTO` claimed it in 71351 at 20:20Z (surfaced to me by
   `3.0.0_SA_CVO` 71468 -- the claim went to CVO, not to me). It was already owned when this log was
   written; the read below is the SPEC for its owner, not an open assignment. The restore came from an
   ad-hoc run; AC6 is the SCHEDULED `cron(30 13)` gold + `cron(50 13)` publish. `2.0.0_SA_COO` and
   `3.0.0_SA_CVO` both went non-live before it could be assigned (broker QUEUED). Raised to
   `1.0.0_SA_CTO` (71315) and written into the closed ledger. **The read is three parts:** an
   `AWS/Scheduler` `InvocationAttemptCount` datapoint in the 13:30 bin (delivery happened,
   payload-independent -- `0.5.0_AE_OpalETL~B` 71327) + the gold object's own result + the SERVED
   payload. ⛔ **`trigger.kind` answers NONE of them** -- it is derived from caller-supplied payload
   (`kind = "scheduled" if event["source"] == "aws.events"`), and the record now holds a manifest
   stamped `scheduled`, dated 2026-08-25, produced by a person.
2. **[`2.0.0_SA_COO`]** ARMED item, disarm owner, does NOT ride this repair: `account_count` fans out
   per underlying model and must never be totalled across models, yet the gate (`:1745`) and the
   composition (`:2487`) both total it. Filed `3.0.0_SA_CVO` 71095 -> ARMED 71106 -> sharpened by
   `1.0.0_SA_CTO` 71117 to *one served field name, three derivations, all labelled
   `count_basis: measured`*.
3. **[`0.4.0_DS_ClientPlatform~F` / whoever reads it]** D1_CATVIEWS remains committed and
   **undeployed** -- deliberately omitted by the hotfix pin, nothing reverted. It deploys later on
   its own merits; it needs a real read (289 lines) that nobody has done.
4. **[`1.0.0_SA_CTO`]** The D10 instance from §Compiler Tools: no instrument in this estate answers
   "which copy of this code actually RUNS." Three of us derived it by hand tonight under P0 pressure
   and one got it wrong first.

## Lessons (transferable, not incident retelling)

- **A gate that has not been REACHED in five days has not PASSED -- it is UNMEASURED.** Distinguishing
  those two is what made testing for a second blocker worth doing unprompted.
- **A denominator can be honest and still be over the wrong POPULATION.** "1 S3 copy across code/
  prefixes" was TRUE about S3 and structurally blind to a copy vendored inside a function package.
- **Presence in the tree is not participation in the run.** A command measuring the first while
  answering the second reads as a clean answer to the question you asked.
- **A field that records a self-reported payload cannot attribute an act** -- and it fails in the
  direction that looks authoritative.
