# AMGT_RESAPP.TO-AMGT-ae-1 -- the posture batch over the 12 held names: 12 keys re-judged, AC1 failed on a route that was never deployed

**archetype:** DEPLOY

**Seat:** `0.7.0_AE_CloudOps~A` | **Session:** `a769140b` | **Fabric:** site-z | **Round:** 55
**Order:** `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ae-1.posture-batch-over-the-held-names.md`
**Risk class:** WORLD | **Commits:** `f3ea4d2556` (ledger OPEN), `0ecb5292c5` (proof)
**Push state:** LOCAL @`0ecb5292c5`; `origin/CLOUD` at `0abf99fcd4` (ls-remote read 05:4xZ). This seat does not push shared branches.

## What was asked

Re-run the posture judgment over exactly the 12 targets whose own name or comparable holds D-1 sentences
after round 54's `ad-2` held 179 no-span sentences, each at its PRIOR `as_of` so the only input that moves
is the D-1 pack, and read the diff from the batch's own output. One Anthropic message per target, on
Andrew's per-use word. 12 same-key overwrites of `posture/v1/<K>/<A>.json` in a versioned bucket.

## Authorization chain, each verified by content

- Andrew's per-use word `2026-10-01T00:41:29Z` ("go"), scope exactly the 12 calls -- record @`17f29440e8`,
  3,034 B at the pin == 3,034 B in the worktree.
- GO msg 27510 from `2.0.0_SA_COO~Z`, READ-acked. The prior hold (msg 27456) confirmed holding was correct
  until the word arrived, so the chain is coherent end to end.
- COO never-widen half @`53a6ad274e` (4,850 B), CTO half @`312405a2f4` (2,105 B); both ancestors of
  `origin/CLOUD 0abf99fcd4`.
- Pin `51df60aa1a`: the act's whole import closure is byte-equal between the pin, the GO run commit
  `0abf99fcd4` and this worktree. Denominator printed: 1 of `lib/`'s files differs from the pin
  (`lib/opal_data_harvest/test_o1_run_record_reach.py`, a test outside the closure). Negative control: the
  same three-surface diff against `HEAD~400` is non-empty.

## Deployment sequence

1. NEVER-2 ledger entry `20261001T0500Z_amgt-resapp-r55-ae1-posture-batch` OPENED with 3 legs and
   **committed before the act** at `f3ea4d2556`, as the order's stated order of work requires.
2. `ae_1_posture.py --what pre` -- 12 names holding 179 sentences, **targets 12** (stop limb 3), verdicts
   equal to the half's table on all 12.
3. Act-start gate: the half's 12 VersionIds re-read live -- **UNMOVED 12 of 12**, with a mutated-expectation
   negative control that reads MOVED on the same comparison. D-1 provenance captured as VersionId AND
   content sha256 for all 12 drafting objects.
4. Pin worktree built at `51df60aa1a` (sparse cone), HEAD read back, clean.
5. Two dry-runs (no model call, no write) per branch, compared worktree-vs-main-tree until byte-identical.
6. The 12 judge runs, in the half's table order, halting on the first non-zero exit. 12 of 12 rc=0 in 3m01s.
7. AC1 at the order's literal invocation. **FAILED, exit=1.**
8. Legs L1 and L3 CLOSED with proof; **L2 left OPEN**; the disposition refused upward to the issuer.

## Verification (actual output)

- **12 of 12 moved** off their prior VersionIds, 0 unmoved, read back live from S3.
- **Packs now count the live (held) D-1 sections** on every target: BABA 38->34, HD 38->20, BA 38->17,
  COST 39->15, HD 36->20, INTU 40->26, KMB 39->18, NU 27->8, SAP 38->30, VLO 39->13. Each equals `ad-2`'s
  post-hold pack count, and BABA 34 / HD 20 were predicted by the pre-act dry-run before any call was made.
  That is the whole point of the act, and it holds.
- **Cites** validated == total on all 12. **Every verdict in the enum.**
- **One verdict moved: `KMB_US_Equity` hold -> better.** The RESULT, read from the batch's own output,
  graded by nobody here.
- **9 model calls of the 12 authorized.** The 3 classed-ABSENT targets (ASML, HAL, PBR) make none by the
  producer's own rule (`judge.py:394` region). Fewer than 12 is strictly inside the word; a 13th would have
  been a REFUSAL. Model `claude-opus-5`, 158,142 in / 7,137 out.
- **Cost $0.9692**, summed from the producer's own `usage.usd` field, under the half's ~$1.3 estimate.

## The finding of this session

**AC1's served limb tests a route that is not deployed, and the check cannot say so.**

All 24 BAD lines are ONE signature -- `served /as_of None != stored ...` and `served /verdict None != stored
...` -- on 12 of 12 targets and on both branches. Measured, not inferred:

- `GET /api/scoped/amgt/security/<K>/posture` returns **404 `no /api/scoped/amgt route for GET ...`** on
  3 of 3 keys this act overwrote **and on 3 of 3 keys it never touched**. The control was drawn from a
  printed denominator: 33 posture subjects, 12 touched, 21 untouched.
- `/thesis` on the **same function and the same prefix** returns **200 at 658,610 B** for a touched name and
  481,945 B for an untouched one. The function is up; only `/posture` is missing from its route table.

So the act cannot be the cause. Two instrument defects kept it hidden until now:

1. The check's `serve()` is `body, _m = cl._invoke(...); return body or {}` -- `_invoke` returns
   `(None, meta)` on any non-200, so a 404 becomes an empty dict and prints as a **content mismatch** rather
   than a missing route. The meta that names the 404 is discarded.
2. `pre`'s volatile set is the paths that DIFFER between two serves 3 s apart. **Two empty serves differ on
   0 paths**, so `volatile []` on 12 of 12 reads identically for a stable route and a dead one. The pre
   capture was never evidence that `/posture` served, though it looked like it.

The issuer's `comp-adversary` note says AC1 "PASSES on a simulated post-state" -- and a simulated post-state
cannot see an absent route. That is the instrument's blind spot, not a defect of the arm.

**Not rolled back and not self-adjudicated.** Stop limb 6 names a failing AC1 as the rollback trigger; the
rollback stayed armed throughout (all 12 prior VersionIds live in `ae1-pre/pre.json`; the half's rollback is
a VersionId copy-back, a write, not a delete). Reported upward the same turn -- the discipline the issuer
itself ruled correct for `ad-2` L3 (msg 27355, AMENDMENT 2 @`9d5bd13f74`).

## Instrument traps hit and recorded

- **A sparse worktree silently changes code paths.** The cone initially excluded
  `infra/logic/registry/systems.json`, and the candidate universe fell back to a worker folder with a WARN.
  Widening revealed a SECOND missing file, `org/standards/NAMING_SCHEMA.json` -- the fallback chain reveals
  one at a time, so the first fix looked complete and was not. Settled only by comparing dry-run output
  between the worktree and the main tree until the diff was empty with 0 WARN **on both branches**, two
  different targets still differing as the control. A pin worktree is not automatically an equivalent
  environment; it has to be proven to be one.
- **`volatile []` is not evidence of a live route** -- see the finding above. A zero-difference between two
  reads is produced equally by stability and by both reads being empty.
- **A wrong-object cost figure.** My first cost number ($0.5815) applied sonnet list prices to an `opus-5`
  run. Withdrawn in favour of the producer's own `usage.usd` field ($0.9692). The producer's own field beat
  my arithmetic because it knows which model it called.
- **`deploy_ledger.py open` stages on the caller's behalf**, and `git` index-lock contention from a live peer
  aborted the first commit (rc=128) after every gate had already passed. Asked the repository rather than
  grepping the tool's stdout, confirmed nothing had landed, retried clean. Same class as the already-filed
  `Z-S322`.
- **`close-leg --proof` text goes through a python argv list**, never a double-quoted bash string -- `ad-2`'s
  L3 proof was corrupted by command substitution on a backticked word.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-secrets` | `comp-secrets get anthropic-api-key --reveal` | PASS. Shape probed WITHOUT printing the value: 4 lines, the `value:` line 108 chars starting `sk-ant-`. The driver refuses to make any call unless the fetched value matches `sk-ant-*`, so an empty or malformed secret is a loud stop, never a silent 0-call run. |
| `comp-which` | `comp-which "how do I grep the repo"` | PASS, forwarder RAN (startup A.3 exercise). PATH: 104 of 104 comp-tools resolve bare. |
| `comp-schedule` | not run | The order's preflight declares it NOT-APPLICABLE (no cron, alarm, monitor or cadence; the batch runs once, by hand). Not re-derived here. |
| `comp-iam` | not re-run | RUN BY THE ISSUER at the cut; same executor identity already reads `opal-data-harvest` and wrote `posture/v1` under rk-22. Corroborated by the act: 12 of 12 PutObject succeeded and were read back, 0 writes outside the 12 keys. |
| `comp-adversary` | not re-run | RUN BY THE ISSUER at the cut. Its positive arm was a SIMULATED post-state, which is exactly why it could not see the absent route. |
| `comp-pipescript deployed` / `postdeps` | not run | Not applicable: this act is not a gold run and triggers no pipeline. The AE minimum in `org/XXX.md` binds on gold-run triggers and ad-hoc gold runs, neither of which this is. |

**Gap:** there is no comp-tool that answers "is this HTTP route deployed on this function?" The one that
comes closest, `comp-routes behaviors`, reads CloudFront behaviors, not a handler's own route table -- which
is the layer that 404'd here. That gap is why a missing route reached an acceptance criterion.

## Files modified

- `org/critical_paths/change_management/20261001T0500Z_amgt-resapp-r55-ae1-posture-batch_deploy_completion.md`
  + its `.open_deploys/` sentinel -- OPENED at `f3ea4d2556`, L1/L3 closed at `0ecb5292c5`, L2 open.
- `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` -- rows
  `AMGT_RESAPP-Z-S324`, `AMGT_RESAPP-Z-S325`. Verified no peer row was clobbered: 692 rows in HEAD, 694 in
  the worktree, 0 lost, exactly my 2 added.
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/` -- the proof_of_spec instance, the 12
  run logs, `ae1-pre/` (pre.json, D-1 census, post receipts), `evidence/` (7 ae1_* files).
- NOT touched: the order's `<status>` line. The flip is the issuer's.

## MCP traffic

- IN msg 27510 (`2.0.0_SA_COO~Z`, the GO) -- READ-acked. Delivery ledger since 2026-09-30: 9 of 9 ACKABLE
  rows READ, denominator printed.
- OUT msg 27550 to `2.0.0_SA_COO~Z` -- one ask, the disposition on AC1's served limb. Delivered, 1,120 B
  verified on the recipient's file.

## Blockers

**One, and it is the issuer's to clear:** AC1 is ae-1's single criterion and its served limb cannot pass
against an undeployed route. Row `Z-S325` is ARMED with `disarm_owner 2.0.0_SA_COO~Z`. The two dispositions
open to the issuer: amend the served limb to grade the route's REACHABILITY explicitly, so an absent route
reads as a route defect and never as a content mismatch; or rule the served limb out of ae-1's scope and
route `/posture`'s absence to the seat that owns the scoped API.

## Current state

The store plane is exactly what the round wanted: the 12 posture objects are re-judged against the held
D-1 packs, and the one verdict that moved is recorded. The served plane has no reader to move, and never did.
The pin worktree `/c/tmp/ae1-pin-r55` (16 MB) is kept deliberately in case the disposition calls for a re-run
under an amended AC1; it is removable the moment that is settled.

## Next steps

1. **[`2.0.0_SA_COO~Z`]** The disposition on AC1's served limb (msg 27550), and the `<status>` flip. Nothing
   else is owed by this lane on this order.
2. **[whoever owns the scoped API]** `/posture` is absent from `opal-amgt-scoped-api`'s route table for all
   33 subjects, so the page's posture card has no served source. Surfaced in `Z-S325`, not adjudicated here.
3. **[this seat]** On the disposition: either close L2 and the ledger entry, or execute the rollback from
   `ae1-pre/pre.json` and close it SUPERSEDED. Both are one act; neither is started without the ruling.

---

## CLOSE-OUT (ruling msg 27564, 06:20Z) -- ACCEPTED, and the finding survived the fix

The issuer ruled the served limb **its check's defect, not the act's**: posture is not served by a
`/posture` route at all, it rides `/security/{key}/overlay` as that payload's `posture` field
(`read_security_overlay -> read_posture`). The amendment re-points `serve()` at that carrier and **raises on a
non-200** instead of returning an empty dict for the next comparison to misread. Order flipped `complete`;
no rollback wanted; the 12 prior VersionIds stay in `ae1-pre/pre.json` as the record.

**AC1 re-run BY THIS SEAT, not cited from the issuer's run:** `targets 12; verdicts moved 1`, **no BAD line**,
label YES, **exit=0** (`evidence/ae1_ac1_amended.txt`).

**And not closed on the producer's self-report.** The served plane was re-read independently of the check, by
invoking the deployed function directly and comparing to the stored object per key: overlay **status 200 on
12 of 12** (70,657-99,606 B), posture field **PRESENT on 12 of 12**, served `as_of` + `verdict` **EQUAL to
stored on 12 of 12** -- AGREE 12, disagree 0, refused 0 (`evidence/ae1_overlay_verify.txt`).

**Two controls, because an amendment that re-points a limb is exactly where a loosening would hide:**

1. A planted mismatch on VLO (`verdict 'steer_clear'` against the stored `'better'`) reads **DISAGREE** -- the
   comparison still discriminates.
2. `/api/scoped/amgt/security/VLO_US_Equity/posture` **still returns 404** after the amendment. So this is a
   CHECK fix, not a route deployment, and row `Z-S325`'s finding remains a true fact about the estate rather
   than something the fix absorbed. `Z-S325` is disarmed by the issuer's carrier row `Z-S326`.

**One citation inconsistency, recorded and not reconciled:** the check file labels the change `AMENDMENT 1`
at line 79; the ruling message calls it `AMENDMENT 2`. Noted in the proof instance so a later reader chasing
either label finds the other.

**One trap worth carrying:** the order's `<status>` now holds TWO tags -- `pending` at :70 and `complete`
at :84, because flips APPEND. A first-match parse reads the stale one and would call this order open.

**NEVER-2 entry `20261001T0500Z`: CLOSED**, all 3 legs proven, sentinel removed. Nothing is owed by this lane
on `AMGT_RESAPP.TO-AMGT-ae-1`.
