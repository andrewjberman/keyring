# The criterion was pointed at a plane it cannot discharge on, and the six-vs-seven mismatch nobody read as a plane error was the tell — 0.4.0_DS_ClientPlatform~M

**Date:** 2026-08-29
**Task Order:** ETFS_INGEST.TO-9-DS.industry-group-truncation-fix
**Status:** COMPLETE

---

## Objective

Score the two event-gated criteria of `ETFS_INGEST.TO-9-DS` — `INGEST-TO9-AC3` (exercised on a
scheduled fire) and `INGEST-TO9-AC4` (no regression in coverage) — against the artifact produced
by the Saturday 2026-08-29 13:00Z `etf-positioning-producer-daily` fire. Both had stood
`UNCOMPUTABLE` at `364656f444` because the deploy (08-28T18:49:14Z) post-dated the last scheduled
run (08-28T13:01:26Z), so no scheduled run had yet executed the deployed decode.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance> INGEST-TO9-AC1..AC5` | PASS | VALID, 5 rows, violations=0, coverage checked against the TO's declared set. Run twice — before and after the edit. |
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 exercise leg; produced its own banner, so the forwarder RAN rather than merely resolving. |
| comp-system | `comp-system` | PASS | Regenerated `06_current_state.{md,json}` @`a05957ab0b` to discharge the two-phase override. Clean — no `BLOCKED-ON-PEER-LANDING`. |
| .tools/aws (s3api / lambda / events) | head-object, list-objects-v2, get-object, get-function-configuration, describe-rule, list-targets-by-rule | PASS | The shim, never bare `aws`. |
| python + boto3 | versioned get-object, `read_parquet`, `hashlib.sha256` | PARTIAL | See **What failed** — my first structural walk was wrong. |

**What worked:** `proof-of-spec-check` run *before* editing gave a baseline that made the
post-edit `VALID` meaningful rather than decorative. Printing the served document's own top-level
key list beside my walk's result is the only reason I caught a broken matcher.

**What failed:** My own instrument, and it failed in the most dangerous direction. The first
structural walk guessed the served container key as `books`/`funds`; it is `portfolios`. It
returned 0 rows, 0 distinct values and an empty basis distribution — a shape that reads exactly
like a catastrophic coverage regression and would have been the loudest possible false FAIL on
AC4. Nothing about a wrong key name announces itself; it returns a clean number.

**Gap found:** none. The estate's tools answered everything; the two errors this session were both
in hand-written matchers, not in tooling coverage.

---

## Work Completed

### 1. Resolved WHICH PLANE the criteria live on — before measuring anything

The re-address instructed: *"Score AC3/AC4 against `gold/holding/date=2026-08-28`."* I read where
the decode executes before pointing an instrument at that path.

```
  imported ONLY by   etf_positioning_publisher.py:79
                     from etf_classifications_dynamodb import resolve as _resolve_industry_group
  applied in         _industry_group()  :258-288          <- SERVING TIER
  gold producer      etf_positioning_gold.py -- ZERO occurrences of the module
                     POSITIVE CONTROL: same grep enumerates its 14 real imports, so the zero
                     is an absence and not a broken matcher
```

The publisher's own comment states the design in terms: *"Serving-tier by design: gold keeps the
vendor's own faithful string, and the repair is a DISPLAY act."* A third carrier nobody consulted
agrees: the gold run's own manifest reports `industry_group_basis_counts.inferred-from-truncation
= 0` at stage gold.

**Consequence: scoring AC3 on the gold parquet returns NO CHANGE and records FAIL against a fix
that works exactly as specified.** Measured both gold partitions to confirm the gold plane is
static in this respect — 6 of 23 values at exactly 30 chars in *both* 08-27 and 08-28.

I surfaced this to `2.0.0_SA_COO~Z` **before** measuring rather than reporting a clean no-change
afterwards. They withdrew the path (msg 16760, then `9048bf12d7`): *"That named a PLANE I ASSUMED.
I did not read where the decode executes."* `0.7.0_AE_CloudOps~M` reached the same conclusion
independently while closing `TO-10-AE`.

### 2. AC3 — scored PASS on `platinum/etfs/positioning_data.json`

The run: gold `run_id 0f277195f2d7` (generated 13:00:44Z, wrote gold 13:01:22Z) and platinum
`run_id 027f2d7f9fc7` (generated 13:01:21Z, wrote the served key 13:01:25Z). Exactly one manifest
per stage in the 2026-08-28 partition — full listings, counted client-side — so no ad-hoc run
wrote alongside the scheduled one.

**`run_class: "scheduled"` is ONE signal, not two.** `etf_positioning_gold.py:1829` classifies the
run once in `lambda_handler` and threads the same value into both stages' manifests, so
gold-agreeing-with-platinum is repetition, not corroboration. What makes the single signal sound
is its *failure direction*, read at `classify_run()` :1649: it returns `scheduled` only on
`event.get("source") == "aws.events"` and returns `adhoc` for every other shape by construction —
the author's own comment calls the reverse *"the lying direction"*. A false `scheduled` is not
reachable from an unclassified caller.

Independent corroboration on a genuinely different plane: EventBridge RULES —
`etf-positioning-producer-daily`, `cron(0 13 * * ? *)`, `ENABLED`, one target, the producer's ARN.
Plus the served key's own write history: 20 versions, the last four consecutive days each a single
13:01Z write; all 15 off-cadence writes predate 2026-08-26 and belong to the build window.

The bytes read are that run's own: served `sha256 80c128dc…` is byte-equal to the publisher
manifest's recorded `body_sha256`, and `body_bytes 148372 == ContentLength 148372`. **Negative
control fired** — the immediately-prior served version (146944 B) hashes `600171da…` and does not
match, so the comparison discriminates.

Deployed `CodeSha256 qQk9ohLihOInJnvj/NncAms1IuoEIkkjRwpb8EIFouQ=` — the same value `TO-10-AE`
recorded immediately after its apply — unmoved since 08-28T18:49:14Z, which predates the fire.

`0.4.0_DS_ClientPlatform~Q`'s pre-registered discriminator held exactly: 7 of 23 distinct values
changed to full names, all 7 carrying `inferred-from-truncation`; at-cap values 6 of 23 → 0 of 23;
max value length 30 → 46.

### 3. AC4 — scored PASS, both images re-derived from bytes at this seat

Not carried over from the recorded before-image — read from the actual prior VersionId, so the
comparison is two measurements rather than one measurement and one citation.

```
                              BEFORE (@08-28 13:01:26Z)    AFTER (@08-29 13:01:25Z)
  structural walk             30+45+90+24 = 189            30+45+90+24 = 189
  industry_group KEY PRESENT  189 of 189                   189 of 189
  basis KEY PRESENT           189 of 189                   189 of 189
  observed                    180                          121   (-59)
  inferred-from-truncation      0                           59   (+59)
  not-applicable-non-equity     8                            8   (+0)
  absent-from-source            1                            1   (+0)
  TOTAL                       189                          189
  at exactly 30 chars         6 of 23                      0 of 23 ; max len 30 -> 46
```

Row-level, not just totals: all 7 changed labels preserve their row counts exactly — 1→1, 7→7,
1→1, 8→8, 14→14, 15→15, 13→13, summing to 59 — and the 16 unchanged labels are identical
row-for-row. **59 rows changed LABEL; 0 rows changed EXISTENCE.**

### 4. The 29-char trap the TO said length could not solve, measured on the served plane

The two 29-char values moved in **opposite and correct** directions:

| value | len | state | outcome |
|---|---|---|---|
| `Consumer Staples Distribution` | 29 | genuinely truncated | → `Consumer Staples Distribution & Retail`, 1 row, `inferred-from-truncation` |
| `Household & Personal Products` | 29 | the complete GICS name | untouched, 4 rows, still `observed` |

A length-keyed repair corrupts one or misses the other; the closed-list keying discriminated them.
This is also why **seven** labels decoded while only **six** sat at the 30-char cap — the seventh
was the 29-char one. That is the whole of the six-vs-seven gap, and `2.0.0_SA_COO~Z` identified
the same mechanism independently at `9048bf12d7`.

### 5. Surfaced a departure from the pre-registered prediction rather than absorbing it

`~Q` predicted `observed 173 | inferred-from-truncation 7`; measured `121 | 59`. They wrote the
**label** count (7) into a **row**-count slot whose denominator is 189. The correct row figure was
already in the estate, inside the very module under test: `_industry_group`'s docstring reads
*"radius 59 of 189 rows, 7 labels"*, and the TO's own §7 co-sign line carries the same figures.
Their other prediction, the one stated per-value, was exact — so the model was right and only the
unit slipped. It does not bear on AC4, whose three clauses are all met. Recorded because `~Q`
wrote *"A departure from that is the signal"*, and a departure quietly absorbed is how a
pre-registered prediction stops being a control.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Score on `platinum/…/positioning_data.json`, not the instructed gold path | The criterion text governs, and the decode is serving-tier at source. The instructed path returns a false negative. Issuer withdrew the path in msg 16760 before I scored. |
| Surface the grain question BEFORE measuring, not after | A clean no-change against the wrong plane is indistinguishable from a real failure, and reporting it would have put a false FAIL into the record. |
| Report BOTH planes in the AC4 row | AC4 holds on gold *and* platinum, so the plane choice does not change that verdict — unlike AC3, where it inverts it. Saying so prevents the next reader re-deriving it. |
| Leave AC1/AC2/AC5 byte-identical | Andrew closed the build 08-28 18:24Z; msg 13720 bars re-opening member/completions/radius/naming. Verified untouched by row-level compare against a pre-edit copy. |
| Do not edit the TO's `<status>` field | Issuer-owned and issuer-amended throughout this TO's life. Flagged its staleness instead. |
| Take the two-phase override with sub-token `proof-of-spec` | `safe-commit.sh:612` names this seat's `deliverables/` literally; the gate's own remedy is unsatisfiable when the named uncommitted source is your only file. Used the established sub-token (17 prior uses), minted nothing. |
| Do not push | Push is the integrator's act (LD-0367). Reported push state as measured instead. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ETFS_INGEST.TO-9-DS_PROOF_OF_SPEC.json` | AC3 + AC4 rescored UNCOMPUTABLE → PASS; assignee, 2 compiler_tools, 2 surprises appended | Yes — `a05957ab0b` |
| `infra/system/06_current_state.md` / `.json` | comp-system recompile discharging the override | Yes — `72b0adde46` |

**Push state, measured:** LOCAL @`a05957ab0b` and @`72b0adde46` (`git ls-remote origin SITEZ` read
— origin at `e998abbfa6`; 17 commits unpushed on SITEZ across 3 seats).

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| none | — | Scoring act over completed work; no new contract or deployment surface. |

---

## Blockers

None. Both criteria scored; nothing outstanding at this seat.

---

## Current State

`ETFS_INGEST.TO-9-DS` is COMPLETE at 5 of 5 PASS. The instance at
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ETFS_INGEST.TO-9-DS_PROOF_OF_SPEC.json`
validates `VALID`, violations=0, coverage checked against the TO's declared criterion set; AC3 and
AC4 are scored against `platinum/etfs/positioning_data.json` at VersionId
`bpgnYq4ir2yrM5cnWgJ35Dzm…` (148,372 B, 2026-08-29T13:01:25Z), written by the scheduled fire whose
manifests are `gold/_manifests/2026-08-28/0f277195f2d7.json` and
`platinum/etfs/_manifests/2026-08-28/027f2d7f9fc7.json`, both `run_class: scheduled`. Awaiting
certification by `3.0.0_SA_CVO~Z`; reported to `2.0.0_SA_COO~Z` + `3.0.0_SA_CVO~Z` as msg
16773/16774.

⚠ The TO's `<status>` field is STALE and `to-check` renders only its head: `9048bf12d7` landed the
plane correction entirely *after* `</status>` (43 insertions, all in the body — measured by
character offset against the status span). Inside `<status>`: `platinum` 0 hits, `publisher` 0
hits, `WITHDRAWN` 0 hits. It still leads with the MDPF `category-views` weekend-law paragraph,
still reads *"REMAINING: score AC3+AC4"*, and still asserts *"the etf-positioning producer's write
semantics have NOT been read"* — now false. **This face already documents this exact class about
itself**, and it has recurred in the same field on the same day.

---

## Next Steps

1. **[3.0.0_SA_CVO~Z] Certify the instance at `a05957ab0b`** — 5 of 5 PASS; the two rows added
   this session are AC3 and AC4 and every `0.4.0_DS_ClientPlatform~Q` row is byte-identical.
2. **[2.0.0_SA_COO~Z] Move the plane correction into `<status>`** — the head is what `to-check`
   renders, and it currently shows a different pipeline's weekend law plus an open REMAINING
   clause on completed work.
3. **[3.0.0_SA_CVO~Z] Hold the vocabulary observation** — the gold manifest's
   `industry_group_observed_members` still publishes 7 truncated names, and §5 of this TO names
   that list as the future adoption source. INERT (nothing consumes it today); not chased.
4. **[1.0.0_SA_CTO~Z] The reserved `STRUCTURAL-TWOPHASE/` sub-token has drifted to 10 values**
   across 119 uses — surfaced only; the reserved class is CTO-owned.
