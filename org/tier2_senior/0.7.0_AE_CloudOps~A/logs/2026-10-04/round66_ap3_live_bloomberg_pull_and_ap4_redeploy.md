# AMGT_RESAPP round 66 -- ap-3's live Bloomberg pull and ap-4's redeploy -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-10-04 (acts ran 2026-10-03 22:4xZ - 2026-10-04 00:4xZ)
**Task Orders:** AMGT_RESAPP.TO-AMGT-ap-3 (section 1) and AMGT_RESAPP.TO-AMGT-ap-4 (sections 1 and 6 AMENDMENT 1)
**Status:** BOTH COMPLETE. ap-3 AC1 + AC2 PASS; ap-4 AC1 + AC2 + AC3 PASS. Neither rollback taken.

Delta since `56b3a4597c`, which covered ao-2.

## Objective

Two acts that together finish FWD-36's price 90/365 thread:
1. **ap-3** -- ONE live Bloomberg `PX_LAST` year pull on Andrew's per-use word, landing a write-once
   bronze object and the four 90D/365D generation partitions.
2. **ap-4** -- the code redeploy that makes the deployed function READ those generations, carrying the
   `tone_reason` deletion and the FWD-39 word cloud as well.

## Compiler Tools

| Tool | Result |
|------|--------|
| `bloomberg_health` + `bloomberg_reference_data` | PASS. The order's precondition is a REAL DATA READ, and `READ_HERE` s.2 warns the port is necessary-not-sufficient, so health alone would not discharge it. SPY 769.64 and AAPL 333.69 with NAME and CRNCY. |
| `price_history_pull.py --plan` then `--live` | PASS. The plan equalled the issuer's read line for line and declared 0 vendor calls / 0 writes; the live run went ONCE, exit=0, 95 of 95 usable. |
| `aws s3api head-object` x2 | PASS. Both artifacts re-read independently of the producer's own report: ap-3's bronze object (562,248 B, sha equal to the run's) and ap-4's zip (41,153,619 B, VersionId `Pj6GLEdK`). |
| `aws dynamodb describe-table` + `query --select COUNT` | PASS, and `describe-table` was load-bearing: my first query assumed a `pk` hash key and was refused with `Query condition missed key schema element: axis_date`. Reading the schema turned a guess into a measurement. |
| `build-and-upload-scoped-amgt.sh --build-only` then real | PASS. 355/350/5 file for file, size equal to the half to the byte, and the `gen_harvest_prefixes --check` that `opal_naming.py` could have broken. |
| `terraform plan` / `show -json` / `safe-apply` / `-detailed-exitcode` | PASS. 49 changes, 1 non-no-op, 3 attributes, `memory_size` 1769 -> 1769, no delete or replace; apply 0/1/0; re-plan 0. |
| `.tools/deploy_ledger.py` x2 | PASS. Both entries opened AND COMMITTED before their irreversible act (`012e5c2466`, `c381a73995`); both CLOSED 3 of 3. |
| `r66_served.py` c22/c19/c18, `r64_served.py` c9-c15, `r65_served.py` c17 | PASS. Base arms on the deployed function before each act, then again after. |
| `ap4_range_cold.py` (this seat's own, committed) | PASS after a method change. Mirrors c15's instrument exactly; its body-key print caught MY OWN probe error. |
| `.tools/commit-gate.sh` | PASS on the one `.py` this seat authored. |
| `comp-read --for` / `--enumerate` | PASS. Gave c15's exact cold oracle to mirror, and `rolling_windows.py:100`'s declaration of which keys the 30-day partitions use -- which told me what to measure. |

**What worked:** measuring the thing the condition names instead of the thing that was easy to get.
Three times this session that mattered -- the vendor word read from committed bytes, the 30-day
partitions read off the live table with a positive control, and the range cold read re-run twice
because the first two samples were warm.

**What failed:** my own range probe, twice, both caught before anything was reported (below).

**Gap found:** `r64_served` c10 now contradicts `r66_served` c22 on identical bytes (row Z-S344).

## Deployment Sequence

| Step | Act | Result |
|------|-----|--------|
| 1 | ap-3 vendor word verified in COMMITTED bytes | card 4 @`9fe6e6f111`, "one-time PX_LAST year pull | yes" |
| 2 | `READ_HERE.md` read; terminal gate on a real data read | PASS; no sign-in, no budgeted attempt spent |
| 3 | `--plan`, then entry opened + COMMITTED | `012e5c2466` |
| 4 | ONE `--live` run | 95 of 95 usable, 4 generations COMPLETE, `failed axes=[]` |
| 5 | 30-day STOP measured with a positive control | DID NOT FIRE -- 30-day pointers still at 11:06Z |
| 6 | ap-3 AC1 c22 local YES, AC2 c10 deployed DELTA=0 exact | entry CLOSED `444ad788f4` |
| 7 | ap-4 base re-read, halves read at their pins | base UNMOVED `lPTMo20T`/1769 |
| 8 | `--build-only` at the detached pin | 355/350/5, the amendment's five files |
| 9 | base arms c19/c18/c22 all NO | the negative control for the three graded cells |
| 10 | entry opened + COMMITTED, then build + upload | `c381a73995`, VersionId `Pj6GLEdK` |
| 11 | code-only `safe-apply`, re-plan 0-diff | `FcVBPafw`, memory 1769 |
| 12 | AC1/AC2/AC3 + regressions | all three PASS; c10's carve-out documented |
| 13 | ~830 s idle, then c15 cold | 3 of 3 COLD, 2.03-2.33 s |
| 14 | range cold read, third attempt | 9 of 12 COLD, 2.03-2.55 s; entry CLOSED `abb9bd85de` |

## Verification

ap-3's 30-day STOP, which needed measuring rather than parsing because all four generations
reported `pointer_written=True`:

```
30-day axes (DIFFERENT partition keys from the ones written):
  TRENDING_PRICE#2026-10-02   1 item, _CURRENT, gen 20261003T110628Z, written 11:06Z
  BREAKOUT_PRICE#2026-10-02   1 item, _CURRENT, gen 20261003T110629Z, written 11:06Z
positive control, same query shape, the four axes the run DID write:
  TRENDING_PRICE_90D#2026-10-02   gen 20261003T224449Z, written 22:44Z
  ...and three more, all 22:44Z
```

The run started 22:44:21Z, so the 30-day pointers predate it by 11h38m, and the control proves the
instrument discriminates rather than reading blind.

ap-4's three graded cells, each against the base arm I measured first:

```
c19  base: 'window tone is held: ... publisher-terms card' x4   after: 'window tone is not served on this route yet' x4
c18  base: 0 terms, word_cloud None                             after: BA/AMD/VLO 40 terms each, empty window serves its reason
c22  base: 0 rows, window_end None, 'not produced yet' x4       after: 94/95/94/95 rows, window_end 2026-10-02
```

c15 cold, with the word cloud now on the path: 3 of 3 COLD at 2328.76 / 2036.49 / 2067.04 ms,
every headline 6 of 6 -- unchanged from round 64's 1.9-2.3 s band.

## Decisions Made

1. **Verified the vendor word in the committed bytes before calling Bloomberg.** The GO cited card 4
   by path and hash; I printed `git show 9fe6e6f111:<path>` rather than reading the worktree file or
   grepping for the quote. A per-use word is the one thing in this act that cannot be re-derived at
   the call site, and a citation ages separately from the text it quotes.
2. **Discharged the terminal gate on DATA, not the port.** `READ_HERE` s.2 says a listener on 8194 is
   necessary and not sufficient, so `bloomberg_health` alone would have been the wrong oracle. Ran a
   real `reference_data` call. Had it been signed out the act was to STOP and report -- a sign-in
   spends one of a 2-attempt budget and was not in the order.
3. **Ran `--live` exactly once and did not retry.** The bound is one run and the word is per-use, so a
   retry on a stumble would have been a second vendor call outside the authorisation.
4. **Measured the 30-day STOP instead of parsing it.** "Any write to a 30-day partition or pointer"
   is ambiguous, and all four generations reported `pointer_written=True`. The source's own comment
   said the 30-day keys differ, but a comment is a claim; I read the live table and ran the positive
   control beside the negative.
5. **Re-ran the range cold read twice rather than report a warm number.** Two ~800 s idles both read
   COLD 0 of 3 -- Lambda held the environments longer than the idle, with `identity=0 import=0`
   confirming reuse. Reporting the warm 344 ms would have substituted a different measurement for the
   one condition 3 asked for. Forced coldness by raising concurrency above the warm pool.
6. **Corrected my own probe before it reached a report.** It read `body['articles']` and printed 0 on
   every run while the day route serves 6. The range route has NO `articles` key -- it serves
   `series` 33, `events` 6, `markers` 6. That zero was my PATTERN, not the world, which is
   `READ_HERE` s.5's own lesson one layer deeper. I added a body-key print rather than file a finding.
7. **Did not treat c10's SERVED NO as a rollback.** The half's failure branch makes "any other check
   moves" a rollback, so this needed care. All four FAIL lines are its 90/365 clauses, and the
   carve-out is declared in three places; its 30-day clauses pass at 94, identical to baseline.
8. **Named two figures in the halves that do not hold** rather than letting them pass: the ap-4 half
   predicts "VLO 22 terms" where VLO serves 40, and it expects the range route ~1.5 s above the
   headline read where the deployed cold read sits inside c15's band.

## Files Modified

See `012e5c2466`, `444ad788f4`, `c381a73995`, `77c1dea4ec`, `abb9bd85de`. No terraform file changed --
ap-4 is code-only and `memory_size = 1769` stands.

## Blockers

**None owed by this seat.**

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 FcVBPafwzuPI0RMFjOJJfYN/KeZe3YYns9uqTSOlalU=` at
`MemorySize 1769`, artifact VersionId `Pj6GLEdKjRnDFwBjZzOSR2gYAsQPHilG`. The 90/365 price generations
are live and served: `s3://opal-data-harvest/.../price_history_px_last/date=2026-10-02/year_pull.json`
plus four generations at `#2026-10-02` (94/94/95/95 rows). Package headroom 8,407,040 B at 96.8%.

Round 66 served state: c18, c19 and c22 YES for the first time; c9, c11-c15, c17 unchanged and YES;
c10's 30-day clauses YES with its 90/365 clauses superseded by c22.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The `<status>` flips on ap-3 and ap-4 -- `task-orders/` is not in either
   order's `<paths>`.
2. **[`2.0.0_SA_COO~Z`]** Row Z-S344: amend or retire `r64_served` c10's C2 clauses, or every later
   round reads SERVED NO on a healthy function.
3. **[`2.0.0_SA_COO~Z`]** The round-67 word-cloud cost cell the CTO half anticipated: the deployed
   cold range read is 2.03-2.55 s, inside c15's band, so the performance basis is weaker than assumed.
4. **[`2.0.0_SA_COO~Z`]** The 90-day axes rank 94 of 95 tickers where 365-day rank 95, on a 95-of-95
   usable pull. Same shape as the 30-day axes, so likely structural -- one read if FWD-36 needs the
   95th name at 90 days.
5. **[`0.0.0_AB_MSTR~Z`]** The push. All nine commits from this seat this session are LOCAL on this
   device.
