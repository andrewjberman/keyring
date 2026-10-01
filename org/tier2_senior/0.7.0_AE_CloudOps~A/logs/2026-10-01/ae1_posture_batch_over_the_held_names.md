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

---

# SECOND ORDER OF THIS SESSION -- AMGT_RESAPP.TO-AMGT-ag-1, the one scoped-API redeploy

**archetype:** DEPLOY

**Order:** `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ag-1.the-one-redeploy.md`
**Risk:** WORLD | **Round:** 57 | **GO:** msg 27624, READ-acked (it states ag-2 RIDES, so AC2 was GRADED)
**Commits:** `957a020416` (item 0 / the build commit), `47ee1cbee2` (ledger OPEN), `cffc66ed7e` (proof)
**Push state:** LOCAL @`cffc66ed7e`; `origin/CLOUD` at `0abf99fcd4` (ls-remote read 08:5xZ).

## What landed

One of each, as the halves bound it: item 0 (CLOSURE_ROOTS gains `lib.trading_calendar`), ONE artifact
upload, ONE code-only `safe-apply`.

- Base re-read LIVE and **UNMOVED** before the build: CodeSha256 `/QP4upEV...`, LastModified
  2026-09-30T15:22:01Z, artifact VersionId `C9brZ5Qd6_.iSbxw3NKZOxHuDByQScll` -- all equal to both halves.
- Artifact -> `RhEQ661Bi9gnVKhBphUCMtjH_rrsscPS`, content-sha256
  `/HInwjrnGBzDLzV2EnYyGFseCcXIuWC/ddnyYUpUEX8=`, 41,115,264 B, read back by the script.
- Plan: **0 to add, 1 to change, 0 to destroy** -- one resource, three attribute lines, no
  destroy/IAM/route/gateway/alias. The **saved** plan was applied, so only reviewed actions could land.
- Live after: CodeSha256 **equals the uploaded artifact's sha**, so the deployed bytes are the BUILT bytes
  rather than merely different ones. CodeSize equals the uploaded ContentLength.
- **AC1 PASS** exit=0; **AC2 PASS** exit=0. NEVER-2 entry CLOSED, all 5 legs proven.

## The two things worth keeping

**1. Item 0's real risk was not the line -- it was whether anything imports the module.** A closure root only
packages what the import walk SEES. Had nothing imported `lib.trading_calendar`, adding the root would have
changed nothing and `--build-only` would still have exited 0 with the file absent. `comp-find` settled it
before the build: 7 hits across 346 files scanned, 5 SURFACED all in `scoped_amgt.py`, and `:745` does a
request-time `import lib.trading_calendar as trading_calendar` -- with the author's own comment at `:743`
naming the CLOSURE_ROOT requirement and why the DOTTED form is used (`from lib import trading_calendar`
reads as module `lib` to the walk). AC1's FWD-33 then proved it LIVE: `stale_trading_days=1` is served, a
clause that could only have raised ImportError without it.

**2. A pass that is narrower than its own sentence (row Z-S330).** AC2 printed three `REFUSED: deployed read
failed` lines and then passed. Two of the three were **status 200 with `application/pdf`** -- successful
responses misclassed as refusals, because `capture_lib._invoke` cannot json-parse a PDF and returns
`(None, meta)`. So the print route contributed **0 of the 1,114** reason strings for all 3 names, while the
printed sentence still reads "3 names x 4 routes" -- because that factor is `len(NAMES) x len(LEAVES)` at
`af_7_text.py:83`, computed from the CONSTANTS, never from what was walked. Two numbers in one sentence with
different provenance, and only the structural one can lie. `af_7_text.py:36` shows the LOCAL check
deliberately graded that non-JSON body "by its text"; the deployed swap lost the capability rather than
never having it. AC2 is **met as written** and L5 closed on that basis -- the census's adequacy is the
issuer's call, not mine.

## Instrument traps hit

- **The shared tree moved mid-act.** Peers advanced CLOUD HEAD from my build commit `957a020416` to
  `5429f9284b` between `--build-only` and the upload. So I graded the CONTENT-DIFF **twice** -- on each
  build's own output -- rather than carrying the first grade forward. Both CLEAR, which made "nothing moved
  underneath me" a measurement instead of an assumption.
- **A peer's merge blocked the commit, and nothing was staged.** safe-commit refused on an in-progress merge
  in the shared index. I did not touch it (a merge I did not create is a peer's work-in-progress); by the
  time I read `MERGE_HEAD` it had already cleared, and the retry landed.
- **The surprise-channel append anchor broke on a peer's indentation.** My appender anchored on
  `\n}\n]\n` and the array now closes with a two-space indent, so it refused and wrote nothing -- failing
  closed, correctly. Fixed by making the anchor tolerate leading whitespace. Worth keeping: the appender
  should match on SHAPE, not on one peer's formatting.
- **Native Python read an MSYS `/c/...` path as ZERO files, silently** -- twice this session. A failed
  retrieval returning a VALUE. `C:/...` works. The count is the only tell.
- **Heredoc escaping mangled a regex twice**; the fix was to stop patching through a heredoc and write the
  script with a file writer instead.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find 'trading_calendar' lib/research --files` | PASS and load-bearing -- see finding 1. 7 hits / 346 files scanned, SURFACED=5 TEST=2. |
| `comp-schedule` | not run | Preflight declares NOT-APPLICABLE (one redeploy by hand). Not re-derived. |
| `comp-iam` | not re-run (issuer ran it with a PutObject negative control) | The clause this seat graded is the one the order names: the PLAN shows no IAM change. Corroborated live by AC1 exercising the riders' reads end to end. |
| `comp-adversary` | not re-run | Base arm recorded under controls.mutant; each base symptom answered specifically post-act. |
| `comp-routes behaviors` | not run | GAP, named: the plan held no CloudFront/gateway change. It is also the nearest tool to "is this route deployed" and reads CloudFront behaviors, not a handler's route table -- the same distinction as this session's earlier `Z-S325`. |

## Files modified

- `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` (item 0, one line + comment).
- `org/critical_paths/change_management/20261001T0759Z_...ag1...md` + its sentinel -- OPENED at `47ee1cbee2`,
  CLOSED 08:30:21Z with 5 legs proven.
- `.../surprise-channel/investigations/INVESTIGATION_v1.md` -- row `AMGT_RESAPP-Z-S330` (702 -> 703 rows, 0 lost).
- `.../deliverables/0.7.0_AE_CloudOps~A/` -- the proof instance, `ag1-pre.json`, `ag1-evidence/` (9 files).
- NOT touched: the order's `<status>` (the issuer's), and `infra/aws/terraform/harvest/ag1.tfplan` was left in
  place -- outside this order's `<paths>`, and the dir already carries `i4.tfplan` / `ww1.tfplan` from prior rounds.

## MCP traffic

- IN 27624 (the GO) -- READ-acked. OUT 27646 to `2.0.0_SA_COO~Z` -- the completion report, no ask.

## Blockers

None. Nothing is owed by this lane on ag-1; the `<status>` flip is the issuer's.

---

# THIRD ORDER OF THIS SESSION -- AMGT_RESAPP.TO-AMGT-ah-2, the name-fix redeploy

**archetype:** DEPLOY

**Order:** `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ah-2.the-name-fix-redeploy.md`
**Risk:** WORLD | **Round:** 58 | **GO:** msg 27703, READ-acked
**Commits:** `e85243de69` (ledger OPEN), `174cf144e9` (proof)
**Push state:** LOCAL @`174cf144e9`; `origin/CLOUD` at `0abf99fcd4` (ls-remote read 09:5xZ).

## What landed

One artifact upload, one code-only `safe-apply`. Base re-read live and **unmoved** at
`/HInwjrnGBzDLzV2EnYyGFseCcXIuWC/ddnyYUpUEX8=` with artifact `RhEQ661Bi9gnVKhBphUCMtjH_rrsscPS` -- both
exactly what `ag-1` produced an hour earlier, so the chain across rounds 57 and 58 is continuous and that
continuity is itself evidence nothing else redeployed this function in between.

- Artifact -> `hj5ITKr5Ct9Mn3ySEvztrK9eG.bnsHho`, sha `g9H0TW2garLGS0zMoLmJgFQU8a/6ZJUGMwJaYFSkc/c=`, 41,115,765 B.
- CONTENT-DIFF **exactly one file** -- `lib/research/api/monthly_chatter.py` -- 350 / 349 / 1 / 0 / 0.
- Plan: **0 add, 1 change, 0 destroy**, three attribute lines, no destroy/IAM/route/gateway/alias. Saved plan applied.
- Live after: CodeSha256 **equals the uploaded sha**; CodeSize equals the uploaded ContentLength.
- **AC1 PASS** exit=0; **AC2 PASS** exit=0 (no regression). Entry CLOSED, 4 legs proven. No row this round.

## The one that mattered: a branch no criterion could see

The preflight declared the classifications-table GetItem **BLIND** -- one action, one table, no IAM
simulation -- and said plainly that a DENIED read would leave those names on the ticker fallback, which C2
still passes. So **AC1 is structurally unable to distinguish granted from denied.** Worse, `bg_names.py`
never prints `name_source` at all, so the pass carries no trace of which branch ran.

I read the distribution off the deployed body myself: **classification 7, crosswalk 63, ticker 25, 95 of 95
rows**, every count equal to the halves' expected branch. `classification = 7` and not `0` means the GetItem
was **ALLOWED**. That is the allowed branch *measured on the live plane*, not inferred from a green criterion
-- and it is the whole reason the preflight assigned the count-read to the executor rather than to the check.

Worth keeping: an IAM *simulate* would have been the weaker instrument here. `/cloud-ops` lists four
independent false-deny modes for `simulate-principal-policy`, and it fails in the under-granted direction
precisely against a narrowly scoped principal -- which is what this role is. The served count is the thing
the page actually depends on, so exercising it beat simulating it.

## Measured rather than inherited

Going in, the worktree differed from the build commit in four peer-landed `lib/opal_data_harvest` files
(`contracts.json`, `publishers.py`, `tab_transport.py`, `test_ae2_hookup.py`). The CTO half reasons they sit
outside the function's closure. I tested each against the packaged set instead of trusting it -- **all four
read NOT PACKAGED** -- so the one-file diff is a property of the import closure rather than luck. The
fabricated-path control confirms the membership test discriminates.

## One self-correction

My first `name_source` read hit `/api/scoped/amgt/timeseries/collected/chatter` and got a 404. The real route
is `/api/scoped/amgt/lead-panel/timeseries/collected/chatter` (`af_1_route.py:23`) -- I had dropped
`lead-panel/`. A wrong-object error of mine, caught by the 404 rather than by producing a plausible wrong
number, and fixed by reading the path out of the grader instead of guessing a second time.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-schedule` | not run | Preflight declares NOT-APPLICABLE (one redeploy by hand). |
| `comp-iam` | not re-run; issuer ran it and declared the classifications GetItem BLIND | The gating clause is the PLAN's no-IAM change, and it holds. The blind read was then settled by live exercise, not simulation -- see above on why that is the stronger instrument here. |
| `comp-adversary` | not re-run | Base arm (C2: 32 of 95 serving the raw key) answered specifically post-act: 0 of 95. |
| `comp-pipescript` | not run -- not applicable | A Lambda artifact redeploy, not a gold/silver/bronze script; triggers no pipeline. |

## Files modified

- `org/critical_paths/change_management/20261001T0938Z_...ah2...md` + sentinel -- OPENED `e85243de69`,
  CLOSED 09:54:15Z, 4 legs proven.
- `.../deliverables/0.7.0_AE_CloudOps~A/` -- the proof instance, `ah2-pre.json`, `ah2-evidence/` (7 files).
- NOT touched: the order's `<status>` (the issuer's); `infra/aws/terraform/harvest/ah2.tfplan` left in place,
  outside this order's `<paths>`.

## MCP traffic

- IN 27703 (the GO) -- READ-acked. OUT to `2.0.0_SA_COO~Z` -- the completion report, no ask.

## Blockers

None. Three orders complete this session (`ae-1`, `ag-1`, `ah-2`); nothing owed by this lane. All `<status>`
flips are the issuer's.

---

# FOURTH ORDER OF THIS SESSION -- AMGT_RESAPP.TO-AMGT-ai-2, the price identity join redeploy (DEMO-BLOCKING)

**archetype:** DEPLOY

**Order:** `org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ai-2.the-price-identity-redeploy.md`
**Risk:** WORLD | **Round:** 59 | **GO:** msg 27804, READ-acked | **Deadline:** 22:00Z, landed **12:34Z**
**Commits:** `01e5b6fbfc` (ledger OPEN), `a30a3443fc` (proof)
**Push state:** LOCAL @`a30a3443fc`; `origin/CLOUD` at `0abf99fcd4` (ls-remote read 12:4xZ).

## What landed

One artifact upload, one code-only `safe-apply`. Base re-read live and **unmoved** at `g9H0TW2g...` with
artifact `hj5ITKr5...` -- exactly what `ah-2` produced, so the chain across rounds 57/58/59 is continuous and
that continuity is itself evidence nothing else redeployed this function between them.

- Artifact -> `q0Vf.FzuGpVovbH.xb2dumggs4k5kMKB`, sha `E6PdHVFB9z1xUcvCRtNIALjgAaCzNtolAdzaKmCssvM=`, 41,116,522 B.
- CONTENT-DIFF **exactly one file** -- `lib/research/api/scoped_amgt.py` -- 350 / 349 / 1 / 0 / 0. The two
  peer-drifted `lib/opal_data_harvest` files were **measured** not-packaged, not assumed.
- Plan `0 add, 1 change, 0 destroy`; saved plan applied; live CodeSha256 equals the uploaded sha.
- **AC1 PASS**, **AC2 PASS**, both exit=0. Entry CLOSED, 4 legs proven.
- Both axes: 94 rows SERVED, **unkeyed 0 of 94** (base 62), display_name 94 of 94, company name 70 of 94 --
  the 70 matching the COO half's local figure exactly. `score_pct` survived the join (0 missing), so FWD-34
  is intact.

## The one worth keeping: my own control broke, and the fix was already in the spec

The CTO's condition 3 asks for "a 200 on `/security/<key>/overlay`" as proof that AMD's and TSM's bars
**open** their security. I got those 200s. Then I probed a fabricated key, `ZZZZ_XX_Equity`, expecting it not
to open -- **it returned 200 as well.** So the status code cannot distinguish a covered key from an
impossible one, and my AMD/TSM 200s were weak evidence standing alone.

Rather than report the green and move on, I went looking for a test that *could* fail. It was one document
away: the COO half describes the join as setting `identity_status MEASURED`. On the live bodies —
**AMD MEASURED, TSM MEASURED, fabricated key UNRESOLVED**, with 73,327 / 32,242 / **3,427** B and 12 / 12 /
**6** populated top-level keys of 13. So "the bar opens" *is* soundly established — as a populated overlay
with `identity_status MEASURED`, never as a status code. Condition 3 is met as written **and** on the
stronger reading. Filed as `Z-S332` (INERT; the wording is the issuer's to change).

This is the fourth instance this session of the same shape: a check that passes for a reason other than the
one it names (`Z-S324` AC1 silent on `generated_at`; `Z-S325` a limb testing an undeployed route; `Z-S330` a
census whose "4 routes" came from a constant; now `Z-S332` a 200 that any key earns). The common tell is a
clause whose oracle is cheaper than the claim it supports.

## Figures that moved, named so they are not read as regressions

Since my `ag-1`/`ah-2` runs: the month range now reaches **2026-10** with `as_of 2026-10-01`;
`stale_trading_days` fell **1 -> 0** because the served day is now T-1 itself; BA's 2026-09 count rose
**20 -> 43**; per-axis rows rose **32 -> 94**. All world changes from a new gold day landing, not effects of
this act. Every clause passes on the new values because the graders recompute their oracle each run -- which
is exactly why they track the world instead of breaking against it.

## One record correction

My content-diff grader was derived from `ah-2`'s and two of its **static headings** were not re-worded: it
prints "must equal exactly monthly_chatter.py" and "the 4 peer-touched files" where this round's values are
`scoped_amgt.py` and 2 files. The measured lines beneath are correct and are what L1 rests on. Recorded in
the proof instance so the committed artifact is not misread.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-schedule` | not run | Preflight declares NOT-APPLICABLE (one redeploy by hand). |
| `comp-iam` | not re-run; issuer ran it, 0 new actions, declared BLIND | Gating clause is the PLAN's no-IAM change, and it holds. The reads this act needs were already exercised live in earlier rounds -- the `research_dossier` listing by `ag-1`'s monthly route, the classifications GetItem measured ALLOWED by me at `ah-2` -- so "0 new actions" is corroborated, not assumed. A denied listing would have left 62 rows unkeyed and failed C2; C2 reads 0 of 94. |
| `comp-adversary` | not re-run | Base arm (62 of 94 unkeyed, no `display_name`) answered specifically: 0 of 94 and 94 of 94, both axes. |
| `comp-pipescript` | not run -- not applicable | A Lambda redeploy, not a data script; BOUNDS 1 also forbids rewriting the 09-30 generation. |

## Files modified

- `org/critical_paths/change_management/20261001T1225Z_...ai2...md` + sentinel -- OPENED `01e5b6fbfc`,
  CLOSED 12:42:26Z, 4 legs proven.
- `.../surprise-channel/investigations/INVESTIGATION_v1.md` -- row `Z-S332` (704 -> 705 rows, 0 lost).
- `.../deliverables/0.7.0_AE_CloudOps~A/` -- the proof instance, `ai2-pre.json`, `ai2-evidence/` (7 files).
- NOT touched: the order's `<status>` (the issuer's); `ai2.tfplan` left in place, outside this order's `<paths>`.

## Blockers

None. Four orders complete this session (`ae-1`, `ag-1`, `ah-2`, `ai-2`); nothing owed by this lane.

---

# FIFTH ORDER OF THIS SESSION -- AMGT_RESAPP.TO-AMGT-aj-2, the overlay-name redeploy

**archetype:** DEPLOY

**Order:** `.../task-orders/AMGT_RESAPP.TO-AMGT-aj-2.the-overlay-name-redeploy.md`
**Risk:** WORLD | **Round:** 60 | **GO:** msg 27858, READ-acked | **Deadline:** 22:00Z, landed **13:59Z**
**Commits:** `a2e64034c9` (ledger OPEN), `1ccf6a59db` (proof)
**Push state:** LOCAL @`1ccf6a59db`; `origin/CLOUD` at `0abf99fcd4`.

## What landed

One upload, one code-only `safe-apply`. Base unmoved at `E6PdHVFB...` with artifact `q0Vf...` -- what `ai-2`
produced, so the chain across rounds 57-60 is unbroken.

- Artifact -> `1DFcRU3xDzUsi84yZnWv985DDF1MymMn`, sha `UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo=`.
- CONTENT-DIFF exactly `lib/research/api/scoped_amgt.py`, 350/349/1/0/0, **zero peer drift** this round.
- Plan `0 add, 1 change, 0 destroy`; saved plan applied; live CodeSha256 equals the uploaded sha.
- **AC1 PASS**, **AC2 PASS**. Entry CLOSED, 4 legs proven. No row.
- AC1's core claim graded across the FULL population: **0 of 94** overlay/row `display_name` mismatches.

## The loop closing on my own earlier finding

Round 59's `Z-S332` said the condition's oracle -- a 200 on overlay -- was non-discriminating, and named
`identity_status` as the field that works. This round the CTO's condition 3 reads "**not the HTTP status**"
and AC1's C4 names `identity_status`. The weak oracle is excluded by the criterion's own wording now, so the
strong form is graded by construction rather than by a side read. A row became a spec change in one round.

## What I still had to read myself

C4's **detail string is empty** -- it passes "the identity block unchanged, AMD/TSM MEASURED" without showing
any values. So I read them: **AMD MEASURED, TSM MEASURED, fabricated key UNRESOLVED**, all three returning
HTTP 200, which is exactly why the status cannot be the oracle.

And one property **no clause asserts**, measured because it is the thing that would quietly go wrong: the
fabricated key's new top-level `name` is **None**, not a ticker fallback. The name path does not invent a
label for a key that cannot resolve.

I did **not** file a fifth row for C4. It is reporting thinness, not a bad oracle, and after `Z-S324`,
`Z-S325`, `Z-S330` and `Z-S332` another row in that family is noise rather than signal -- recorded in the
proof and leg L3 instead.

## Fixed rather than re-noted

`ai-2`'s proof recorded that two static headings in my content-diff grader had been carried over from the
`ah-2` variant and named the wrong file. This round's grader derives every heading from its `EXPECT_CHANGED`
constant, so that class of error cannot recur.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-schedule` | not run | Preflight declares NOT-APPLICABLE. |
| `comp-iam` | not re-run; issuer ran it, 0 new actions, BLIND | Gating clause is the plan's no-IAM change, and it holds. The reads were already exercised live by this seat in rounds 58-59, so "0 new actions" is corroborated, not assumed. A denied read would show as an overlay/row mismatch; C2 reads 0 of 94. |
| `comp-adversary` | not re-run | Base arm (94 of 94 overlays without `display_name`) answered specifically: 0 of 94 mismatches. |
| `comp-pipescript` | not applicable | A Lambda redeploy; BOUNDS 1 forbids any store write. |

## Blockers

None. Five orders complete this session (`ae-1`, `ag-1`, `ah-2`, `ai-2`, `aj-2`); nothing owed by this lane.
