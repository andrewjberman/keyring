# Round 73 AMGT-aw-7: the bottleneck moved rather than vanished, and the route that clears the DEV push takes 11 seconds -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

## Objective

Execute `AMGT_RESAPP.TO-AMGT-aw-7` on the GO at `c84776a617`. Two legs, in order, under ONE NEVER-2 entry:
(1) CODE at `9d2b7b3d7c` carrying aw-1/aw-2/aw-3/aw-5, one code-only `safe-apply`, then
`leadpanel_cold_warm.py --label after` plus the cold invokes' `AMGT_PHASE` lines; (2) POOL WRITE,
`build_universe --as-of 2026-10-06 --write-pool` from CLOUD at or after `1aa1d8f2df`, to the NEW key
`universe/v1/2026-10-06.json`, on stored objects only with no sec.gov call. `memory_size` stays 1769.
Six CTO conditions. AMENDMENT 1 removed the grant leg.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `content_diff.py` (in the build) | `--build-only`, then the real run | PASS. CHANGED 4 and nothing else, read at the four lines. Size `253,976,309 B` = the COO half's figure **to the byte**. |
| `r73_served.py` | c48/c49/c50 deployed; c52 local, before AND after the write | PASS. Base arm first, then post-code. c52 read identically before and after the write, which is what established the dry-run was clean before anything landed. |
| `build_universe` | `--dry-run`, then `--write-pool` | PASS. Dry-run rc 0, union 302. The write's own `SEC CACHE:` line names the **stored** bronze object, which is condition 2's evidence rather than my inference. |
| `comp-find` | egress pattern over `lib/research/identity/`, then over `lib/research/` as a control | PASS, **and the control is the point.** 0 hits / 28 files in the write path; 20 hits / 418 files in the parent including the egress definition at `filings/fetch.py`. Without it the zero was indistinguishable from a broken pattern. |
| `comp-read` | `--for` on `r73_served.py`; `--enumerate` imports on `build_universe.py` | MIXED. The first found the `boto3 lambda.invoke` helper the /freshness probe reuses. The second read **0 imports in a 1104-line Python file** -- implausible on its face, so treated as a pattern bug, not a finding; the import block was read at the bytes. |
| `deploy_ledger.py` | `open` / `close-leg` x7 / `close` | PASS. 7 legs, one per act plus the gating read, committed `@e035d9653e` before the first apply. |
| `commit-gate.sh` | on the new /freshness probe | PASS, run **before the probe was used**, not just before the commit. |
| `proof-of-spec-check.py` | pre-commit, then committed bytes | **VALID first pass**, 12 of 12 controls discriminating. Rounds 71 and 72 cost 14 and 2 first-pass violations; those lessons carried. |

## Deployment Sequence

| # | Step | Evidence |
|---|---|---|
| 1 | Authorization checked, not assumed | The order's last `<status>` reads `go`, flipped by the ISSUER `@c84776a617` with an ISSUER GO block. The CTO's half-signature notice arrived first and was **not** treated as a GO. |
| 2 | Base re-read live | `2lUlZomo...`, 1769. Equals both halves. |
| 3 | Condition 6 union | **52 worktrees, 52/52 resolved, 0 unresolved, 1,186 entry-rows**, per-tree denominator printed |
| 4 | Pool key BEFORE state, with a control | prefix listed the two real September keys; `2026-10-06.json` ABSENT, so the write is a first mint |
| 5 | Pin resolved **by content** | `build_universe.py` sha `612529db0d59ce02` at HEAD **and** at `1aa1d8f2df`, so the CTO's static reading transfers to the executed bytes |
| 6 | NEVER-2 opened + committed | `@e035d9653e`, before any apply |
| 7 | Build + CONTENT-DIFF | CHANGED 4, ADDED 0, REMOVED 0; 96.9% of ceiling |
| 8 | Upload | VersionId `KIDdM0A1Ts_.ImnC0GCw_su8ZKmG3cK9` |
| 9 | Code apply (saved plan) + leadpanel | 49 rows -> 1 update; all four prohibited classes 0; measurement 9 s after the apply, same tool call |
| 10 | Live verify + 0-diff | `satkY3HX...`, 1769; re-plan `No changes` |
| 11 | Pool write | first mint, `fPJ4F12cXpgvHd576hcEPVAOfMKMsmcj`, 311,901 B |
| 12 | AC1 / AC2 / AC3 | all PASS |

## Verification

**AC1** c48/c49/c50 YES. **AC2** c52 YES (covered 95 of 95, 13 prior forms, 302 rows, 0 regressions), run
`--where local` after the write as written. **AC3** r72 c39-c45 and r71 c38 YES, no regression, c38 worst
read 725 ms against a 2,000 ms bar. Every criterion run literally and **unpiped**.

**Attribution is measured.** The base arm on the deployed base read c48 at 86 long-decimals / 3 reprs / 742
clipped spans, c49 at `NEVER 95`, c50 at 131 of 383 failing -- all to **0** after. And `c39`'s population
**grew 138 -> 147** because the pool write enlarged the universe, so that regression pass holds over a
*larger* population than round 72's, not a smaller one. A pass whose denominator quietly shrank would have
been the thing to catch.

**The pool write is a first mint and provably nothing more.** Before: the prefix held two September keys.
After: exactly three, with both September keys **unchanged at their original sizes and timestamps**. The
readback was done on the **written object**, not the dry-run: 13 prior decided `form_expected` values all
kept, 0 regressed; of 51 new names, 51 carry the absent shape and 51 carry a provenance note -- the CTO's
ruling-7 boundary respected, `none` only where the stored filer list cannot decide.

**No SEC egress, bounded by mechanism rather than by a census alone.** A directory census bounds the
sample; the import surface bounds the inference. `build_universe` imports stdlib plus `openpyxl`, `boto3`,
`pyarrow`, and first-party only `opal_naming`, `crosswalk`, `resolver`, `positioning_chain` -- none of
`filings`, `social` or `management`, the three packages that carry HTTP. boto3/AWS is the only network
client reachable. Then the run itself said so: `SEC CACHE: ... sec/harvest/bronze/company_tickers/`.

## The two findings, and why neither is a rollback

**1. /freshness serves warm in 10.3-11.8 s.** Row `AMGT_RESAPP-Z-S356`. About **5x** the COO half's own
2,000 ms row-bar. Two agreeing planes: client-side 10622/11013/10997 ms at 292 rows, server-side
10274-11825 ms with 0 of 17 REPORT events carrying Init Duration -- so warm, not scaled-out cold
containers. aw-3 bought a correct pack clock (c49: `NEVER` 95 -> 0) and the price is an 11-second route.

**This is not merely a latency note.** CTO condition 4 makes a live read of this exact route the thing that
clears the portal condition for asking Andrew's DEV push. The condition **is** met -- on correctness. And a
portal page calling it will sit for eleven seconds. Those two facts belong to the same decision, which is
why the ask went up with the report rather than after it.

**And it changed the decision.** Issuer ruling msg 29890, minutes later: the DEV push is **held** and the
ask to MSTR~Z **withdrawn**, with a precomputed or cached pack clock becoming a round-74 item and the push
re-asked once the route reads under 2 s. Worth recording as a method note rather than a victory lap: the
number existed either way, and what made it actionable was being raised against the decision it bore on
instead of filed only in the proof instance. A latency line buried under "AC1-AC3 all PASS" would have
been true, complete, and useless -- the push would have gone out on a correct page that takes eleven
seconds to load.

**2. The cold bottleneck moved rather than vanished.** Cold chatter 6381-7786 ms, both ends down against
round 72's 6998-8638. The phase table over 459 emitted `AMGT_PHASE` lines (459 parsed) shows the **names**
phase aw-1 targeted down to **1175 ms** from the 2.5-3.0 s the half measured locally -- but **mentions
decode at up to 3720 ms** is now the largest cold phase, about half the read. That is why total cold fell
only ~0.6-0.9 s while one phase improved ~1.5 s. Further cold work should target mentions decode. Per
condition 5 the cold read stays above 2 s, so provisioned concurrency **stays** on Andrew's list.

## Three instrument failures caught, all the same class

A zero that cannot tell absence from a broken reader.

1. **The cold/warm split for /freshness.** First read `aws logs --output text` plus a tab-split and got
   "0 cold". A REPORT message carries **native tabs**, so the split shredded each message and `Init
   Duration` could only ever have been absent from the kept fragment -- the count was structurally
   incapable of being non-zero. Re-read with `--output json`: same answer, sound instrument. The answer
   being right is exactly why this one was worth redoing; a broken instrument that agrees with you is the
   one you never check.
2. **`comp-read --enumerate` on imports.** 0 hits in a 1104-line Python file. Implausible on its face, so
   treated as a pattern bug rather than a finding.
3. **The surprise-row append.** Its literal tail anchor `"}]\n```"` no longer matched because a peer had
   re-laid the array out as `}` / `]` on separate lines. The assert **failed closed** and refused to write,
   which is why a 2.8 MB shared channel was not corrupted; redone anchored on the array's closing bracket,
   with the parse proven before the write. A shared append-only file has concurrent writers, so its exact
   whitespace is never a stable anchor.

## Decisions Made

| Decision | Why |
|---|---|
| Treat the CTO half-signature notice as **not** a GO | A half-signature is not authorization. I checked the order for an issuer-committed `go` flip, found it `@c84776a617` with an ISSUER GO block, and the issuer's broker GO then arrived and was acked. |
| Re-verify the no-sec.gov claim on the bytes I run | The CTO read it at `1aa1d8f2df`; I would run from HEAD. Resolved by **content** -- the file is byte-identical -- so the reading transfers rather than being assumed to. |
| Run the pool dry-run before the code leg | Read-only, and it operates on S3 objects the code leg does not touch, so it was free early warning on the leg furthest away. |
| Read back the **written object**, not the dry-run | Condition 2 says "read back the written object". The dry-run and the write produce the same document, but only one of them is what readers will take. |
| File the /freshness latency as a row and raise it as the ask | The half makes a warm read over 2,000 ms a row. Reporting it only in the proof instance would have buried a fact that bears on the DEV-push decision. |
| Report the cold read as a modest improvement, not a win | Both ends moved down, which is more than round 72 managed -- but it is two single runs of n 6, and the phase table shows why the headline barely moved. |
| Not flip the order's `<status>` | The order's `<paths>` does not grant `task-orders/`, and git log shows every flip committed by the issuer. Measured across three orders now. |
| Give the /freshness probe no gate-shaped exit code | The halves make it report-only. An exit code would invite a later reader to mistake a report for a criterion. |

## Files Modified

| Path | Commit |
|---|---|
| `.open_deploys/amgt-resapp-r73-aw7.json` | opened `e035d9653e`, removed at close `c85341be0d` |
| `change_management/20261006T0337Z_..._deploy_completion.md` | `e035d9653e` -> CLOSED 7/7 `c85341be0d` |
| `deliverables/0.7.0_AE_CloudOps~A/...aw-7...proof_of_spec.json` | `c85341be0d`, VALID on committed bytes |
| `deliverables/0.7.0_AE_CloudOps~A/LEADPANEL_AFTER_aw7.txt` | `c85341be0d` -- carries the phase table and the min-is-warm caveat |
| `deliverables/0.7.0_AE_CloudOps~A/aw7_freshness_latency.py` | `c85341be0d` |
| `surprise-channel/investigations/INVESTIGATION_v1.md` | `c85341be0d`, row `Z-S356`; 778 rows, 0 duplicate ids |

No grant, no IAM change, no memory change, no S3 delete, no vendor or SEC call, no shared-branch push, no
portal promote. `ad2-pre-bytes/` remains untracked in my deliverables from an earlier act and was again
deliberately **not** committed.

## Blockers

**None.** Nothing is owed by this seat on aw-7.

## Current State

`opal-amgt-scoped-api` runs `satkY3HXAhzfU7zYZ5fk+EmNHaqIRfj7bBtVlG4XfIY=` at memory 1769, carrying
aw-1/aw-2/aw-3/aw-5. `universe/v1/2026-10-06.json` is now the newest dated key, so every reader that takes
the newest key -- crosswalk build, peers, posture, filings, management, chatter, /freshness -- is reading
it from this point. All three criteria pass; the NEVER-2 entry is CLOSED 7/7; all rollbacks named and
intact.

**Push state: LOCAL @c85341be0d**; `origin/CLOUD` reads `e82f508eef` (`git ls-remote`). Pushing is
`0.0.0_AB_MSTR`'s on Andrew's word.

## Next Steps

1. ~~Row `Z-S356`: does the DEV push proceed with an 11-second /freshness?~~ **RULED, msg 29890: the DEV
   push is HELD.** "Correctness is met (pack dated 95 of 95), but at 10.3-11.8 s warm the /freshness page
   is not pushed. I withdrew the DEV push ask to MSTR~Z. A precomputed or cached pack clock is a round-74
   item, and the push is re-asked once the route reads under 2 s." Nothing owed by this seat;
   `2.0.0_SA_COO~Z` closes aw-7 on the report.
2. **[`2.0.0_SA_COO~Z`]** Further cold-path work targets **mentions decode** (up to 3720 ms), not names
   (now 1175 ms). The phase table is in `LEADPANEL_AFTER_aw7.txt`.
3. **[`2.0.0_SA_COO~Z`]** Provisioned concurrency stays on Andrew's list per condition 5; the cold read is
   6.4-7.8 s.
4. **[`2.0.0_SA_COO~X`]** Close `amgt-corpus-r36-al5` SUPERSEDED. Measured dead in rounds 71, 72 **and**
   73, each time costing a 50-plus-worktree union read to rediscover.
5. **[`0.7.0_AE_CloudOps`]** The 51 new pool names carry `form_expected` "none" by the absent-shape rule;
   `filings/batch.py` ignores them because it acts only on `source == edgar` with a cik. Worth knowing
   before anyone reads "none" as a filing claim.
