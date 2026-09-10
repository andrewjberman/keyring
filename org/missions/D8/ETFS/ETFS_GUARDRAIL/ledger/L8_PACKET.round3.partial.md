# ETFS_GUARDRAIL round 3 -- L8 PACKET (PARTIAL: **6 of 7 orders terminal**; revised in place at each drain)

**Compiled by** `2.0.0_SA_COO` 2026-09-10 ~04:4xZ at the first compile of round 3 (v1 @`d30e3ca107`), revised ~05:3xZ at the second compile (v2 @`665bbd9b5c`), revised ~06:0xZ at the third (v3 @`8e6d41f50a`) -- `EG-s-24` TERMINAL and drained @`43ad639bac`, and its writer census FOUND A LIVE ARGUMENT INJECTION -- **revised ~06:2xZ at the fourth (this version, v4): `EG-s-25` TERMINAL and drained @`f17ea65a20`, leaving `EG-s-21` alone**; the v2 note read -- `EG-s-23` TERMINAL and drained @`24d7e8194a`, and the round grew from 5 cells to 7**, on the `/drive` obligation "terminal orders -> L8 compile NOW; the compile is an act, never a wait."
**For** `3.0.0_SA_CVO` at L9, as a FILE (the spine's three tracks share files, never messages; the one message names this path and its hash). **This is NOT the L10 slug** -- the slug is the CVO's, after L9, once every order of the round is terminal.

⛔ **A CORRECTION TO MY OWN LAST TICK, STATED BECAUSE IT WOULD OTHERWISE READ AS A CHOICE.** The tick-52 log said this packet was "owed at the round's close, not per-order." That was wrong on the obligation's own words and wrong against this project's round-2 practice, where the packet was compiled at the FIRST drain and revised in place five times. Three orders sat terminal and drained with no packet, which is precisely the hard gate's "uncompiled terminal order". Compiled now, one tick late, and the lateness is recorded rather than absorbed.

---

## 1. THE ROUND, AS IT STANDS AT L7

Round 3 is the round Andrew's ~03:0xZ law built -- **no FWD is a wait**. It opened as three cells on PRD v0.5 (`EG-s-19`, `EG-s-20`, `EG-s-21`, ONE issuance @`ea47e92a72`) and was widened TWICE BY AMENDMENT, both times on an artifact that arrived mid-round rather than on a schedule:

- **`EG-s-22`** @`eab3712b31` (decomp v0.4 s.13), on the CTO's placement of row `W1-S31` at 94947 -- PRD v0.6 row `S19`, the classifier half ruled INSIDE this project's surface while the producer half was placed OUT at row `S20`.
- **`EG-s-23`** @`5aeb940bd0` (decomp v0.5 s.14), on the ROUND-2 ANALYSIS at 94988, which graded FWD-8 NOT_REALIZED and listed three cells still to place. Two were already cut; this was the third.

`fanout: 3 of 3 chains, cap 8`. **SEVEN cells serving five outcomes**: FWD-1, FWD-4, FWD-8, FWD-9, FWD-10. It opened at three and grew to seven -- twice by amendment on an arriving artifact, and once because `EG-s-21` proved IMPOSSIBLE AS CUT and was re-decomposed into two enabling cells plus itself (v0.6 s.15, on row `W4-S2`).

| order | cell | outcome | slot | state |
|---|---|---|---|---|
| TO-EG-s-19 | EG-s-19 | FWD-1 | `~5` | **TERMINAL**, drained @`56cfbb2505` |
| TO-EG-s-20 | EG-s-20 | FWD-10 (precondition) | `~4` | **TERMINAL**, drained @`5d292ff11f` |
| TO-EG-s-22 | EG-s-22 | FWD-4 | `~1` | **TERMINAL**, drained @`ecd50f3096` |
| TO-EG-s-23 | EG-s-23 | FWD-8 | `~1` | **TERMINAL**, drained @`24d7e8194a` |
| TO-EG-s-21 | EG-s-21 | FWD-9, FWD-10 | `~4` | pending -- **BOTH DEPENDENCIES NOW SERVED**, dispatched this tick |
| TO-EG-s-24 | EG-s-24 | FWD-9 (enabling) | `~4` | **TERMINAL**, drained @`43ad639bac` |
| TO-EG-s-25 | EG-s-25 | FWD-9 (honesty) | `~5` | **TERMINAL**, drained @`f17ea65a20` |

---

## 2. THE TERMINAL ORDERS, re-validated AT THIS SEAT on the merged tree

Criterion ids taken from the ORDER at HEAD and passed as the checker's third argument -- never from the worker's report.

| order | instance (under `deliverables/`) | checker at this seat | drained at |
|---|---|---|---|
| TO-EG-s-19 | `0.9.0_WK_ETFS_GUARDRAIL~5/...TO-EG-s-19.the-catch-up-branch-driven.proof_of_spec.json` | **VALID rc 0**; 2/2 criteria carry a cell_ref, 1/1 resolves to the decomp, 1/1 cell reachable; 3 of 3 surprises resolve | `56cfbb2505` |
| TO-EG-s-20 | `0.9.0_WK_ETFS_GUARDRAIL~4/...TO-EG-s-20.the-send-path-correct-and-test-safe.proof_of_spec.json` | **VALID rc 0**; 3/3 criteria carry a cell_ref, 1/1 resolves, 1/1 reachable; 1 of 1 surprise resolves | `5d292ff11f` |
| TO-EG-s-22 | `0.9.0_WK_ETFS_GUARDRAIL~1/...TO-EG-s-22.the-classifier...proof_of_spec.json` | **VALID rc 0**; 2/2 criteria carry a cell_ref, 1/1 resolves, 1/1 reachable; 1 of 1 surprise resolves | `ecd50f3096` |
| TO-EG-s-23 | `0.9.0_WK_ETFS_GUARDRAIL~1/...TO-EG-s-23.the-ask-that-under-reports.proof_of_spec.json` | **VALID rc 0**; 2/2 criteria carry a cell_ref, 1/1 resolves, 1/1 reachable; 0 surprise entries (none filed) | `24d7e8194a` |
| TO-EG-s-24 | `0.9.0_WK_ETFS_GUARDRAIL~4/...TO-EG-s-24.thread-the-forcing-spec...proof_of_spec.json` | **VALID rc 0** (assignee, re-read at this seat on the merged tree); 10 of 10 arms; hermetic side 27 passed, was 20 | `43ad639bac` |
| TO-EG-s-25 | `0.9.0_WK_ETFS_GUARDRAIL~5/...TO-EG-s-25.the-verdict-discloses-its-own-forcing.proof_of_spec.json` | **VALID rc 0** re-read at this seat, ids from the ORDER at HEAD; 2/2 criteria carry a cell_ref, 1/1 resolves in a 29-cell index, 1/1 reachable; surprises **ENFORCE 4 of 4** | `f17ea65a20` |

---

## 3. WHAT THE OUTPUT SAYS -- SIX findings, and finding 5 found a live vulnerability

**1. `EG-s-19`: THE CATCH-UP BRANCH RAN FOR THE FIRST TIME IN THIS ESTATE, AND FOUND THE HOLE ITSELF.** 8 of 8 arms, `EGS19-CATCHUP-BRANCH-DRIVEN`. The discriminator that matters: `catchup_processed: ["2026-09-03"]` while the response's own `date` field reads `2026-09-08` -- **the catch-up path, not the main path**, which is exactly the dead end `EG-s-17` hit when `_latest_partition()` made the target its own `skip_date`. The restored slice is byte-identical to the deleted original: sha256 `060188a6e76b2275...` on original, archive AND restored. Andrew's ~02:5xZ constraint was proven on **three independently-failing planes** rather than asserted: the deployed bytes (1 of 1 file, 0 mailer tokens -- no send call exists), the role (0 `ses:` actions across 3 of 3 policies), and the window (`AWS/SES` Send/Delivery/BounceRate all 0 datapoints).

The date choice is worth the CVO's eye because the REJECTIONS carry the reasoning: `2026-09-08` is the newest priced partition and would have been skipped at `:268-269`; `2026-09-09` has `partition: false` so a hole there is damage rather than a test; `2026-09-05` is not a trading day so its absence is correct; `2026-09-04` was eligible on all four properties and was **deliberately held back as the 200 positive control**.

**2. `EG-s-20`: THE SEND PATH IS CORRECT AND TEST-SAFE, AND THE DISCRIMINATOR IS WHY THAT SENTENCE IS BELIEVABLE.** `S20-AC1` 15 of 15 in the named file (round-1 floor 7, +8), 20 of 20 across the directory; `S20-AC2` 20 of 20 arms, `EGS20-SEND-PATH-CORRECT-AND-TEST-SAFE`. **The same new arms run against the PRE-FIX blob fail 7, with the headline arm failing on `AssertionError: exactly ONE terminal send on the refusal branch` -- i.e. ZERO sends, which IS the defect.** An arm that passes against both the fixed and the broken code proves nothing, and this one was shown not to.

Measured on the DEPLOYED bytes: **aj@ in 0 of 24 test resolutions** (12 adversarial events x 2 carriers -- list, joined string, mixed, different case, padded, duplicated, empty, null, truthy-non-boolean marker, non-`run` mode); an all-forbidden override resolves to `[]` and makes **0** SES calls; a default test invocation resolves to `['andrew@opalinvest.com']` with a printed `MessageId`. **The scheduled direction is UNCHANGED at 5 of 5** marker-free payload shapes resolving to both recipients, identical to the module's own `EMAIL_RECIPIENTS`, with the live `EMAIL_RECIPIENT` env var untouched.

⭐ **THE ASSIGNEE REFUSED THE WEAKER SHAPE THE FACE PERMITTED, and its reason is better than my cut.** The face allowed "no send on a test invocation". It declined, because that would make **FWD-10 unprovable by construction** -- FWD-10's whole content is that the send FIRES and reaches andrew@. It built an unconditional forbidden-recipient FILTER that runs LAST instead, because a replacement is a default and a default is defeated by the next caller who passes an override. Taking a harder shape to keep a DOWNSTREAM outcome provable is judgment no criterion asked for.

**3. `EG-s-22`: THE CLASSIFIER NOW DISCRIMINATES, AND THE SHAPE WAS CHOSEN ON THE AXIS RATHER THAN ON THE PRICE.** 7 of 7 arms, `EGS22-CLASSIFIER-DISCRIMINATES`. Arm (a) reproduced the defect FIRST on the pre-change classifier pinned at `c866edd324` with the slice fetched live (1,209 B, 4 priced rows on a market holiday): both cases returned the byte-identical `{"class": "A", "probe": null, "reason": "market closed (not a trading day)"}`.

The assignee chose a **FIELD** (`slice_on_closed_day`), not a new class value, and its reason is the one to record: the class axis answers *"is this a hole, and why"*, while whether an artifact turned up is an orthogonal fact about a **different actor with a different remedy owner** (row `S20`). That is rule 24 (iii)/(iv) deciding the question mechanically rather than by taste. Consequence: `_CLASS_NAMES` is untouched, no four-postulate record or token census is owed, and **arm (e) PROVED the arithmetic did not move rather than asserting it** -- 27 partner-day records both sides, **0 counts moved**, `trading_days` and `holes` identical, all 9 changed records class A.

⭐ **It added TWO PERMANENT REGRESSION ARMS to the estate's own suite, unasked** (8 -> 10 passed, 0 failed both sides). The defect existed *because nothing covered it*, and a one-shot battery would have left that true. Both assert `with_slice != without`, which arm (a) measured byte-identical on the old code -- so both would FAIL against the world they were written to catch. They are controls, not constants.

**4. `EG-s-23`: THE ASK NOW NAMES EVERY PARTNER -- AND THE SUITE THAT LOOKED LIKE IT COVERED THIS PASSED AGAINST
THE DEFECT.** 7 of 7 arms, `EGS23-ASK-NAMES-EVERY-PARTNER`. Arm (a) reproduced it first: 2 of 2 `put_object` calls
on ONE key, the stored body carrying only the SECOND partner, top-level keys `['asks','authorization',
'generated_at','month']` -- nothing naming a partner it omits.

⭐ **THE FINDING THE CVO SHOULD CARRY BEYOND THIS CELL.** `test_rung3_two_d_days_two_partners_ask_names_all` ALREADY
EXISTED and PASSES AGAINST THE DEFECT, because it asserts the two RETURN VALUES and concatenates them IN THE TEST
(`all_asks = ask_cw["asks"] + ask_inf["asks"]`). **The completeness happened in the ASSERTION and never in the
ARTIFACT.** And `_StubS3` has no `get_object`, so nothing in that suite COULD read back a write. A harness that
cannot observe the stored object cannot score the property the stored object carries.

**The shape was chosen on the axis of who reads it, and the assignee argued against the obvious fix.** One merged
month document, not per-partner keys: per-partner keys make each FILE correct while a partner that never wrote stays
INVISIBLE to a reader who does not already know the partner set -- the same failure moved from an overwrite to an
absence. A manifest repeats it one level up. **And the merge has exactly ONE input -- the read of what is already at
the key -- so `_read_prior_asks` separates an absent CAPABILITY from an absent OBJECT:** no `get_object` yields
`ask_scope: "partner-only (prior asks UNREADABLE -- this file may omit other partners)"`, while a `get_object` that
merely raises is the ordinary first-partner absence. **The fix cannot quietly become the bug again**, which no arm
asked for.

3 of 3 partners reachable with the list taken FROM the served verdict artifact and printed as the denominator, never
by recall. FOUR permanent regression arms added to the estate's own suite (8 -> 12 passed), **all four FAILING
against the pre-change code**. Ladder untouched: `authorization` PER-USE verbatim, `dry_run` fires no rung 3, class B
stops with 0 re-runs. Consumer census 124 hits across 29,716 files, exactly 1 non-test consumer, its 3 access sites
read at `file:line` and NOT broken -- and that file is `~4`'s live surface, read and never touched.

**A CORRECTION THE ASSIGNEE MADE TO ITS OWN EARLIER ROW:** `W1-S27` reported this shortfall correctly but speculated
an unmapped provider for `49financial`. That was WRONG -- `_PROVIDER_BY_PARTNER` maps it to Schwab -- and the cause
is the partner-less key. The row hedged it as "likely", so it was a hypothesis rather than a finding, but anyone
chasing the provider map would have found nothing there.

⛔⛔ **5. `EG-s-24`: THE CTO'S WRITER CENSUS FOUND A LIVE ARGUMENT INJECTION IN THE SERVED FUNCTION, AND IT IS THE
STRONGEST ARGUMENT FOR THAT CONDITION ANYONE COULD HAVE MADE.** 10 of 10 arms, `EGS24-FORCING-THREADED-SCHEDULE-CLEAN`.

The condition (94999 (b)) required the writers of the forcing property counted BY SUBTRACTION, with N printed,
because the assignee's AST census over the handler's four event keys covered ONE writer. The command builder's own
source gives **denominator 6** -- 2 parameters and 4 Terraform-set globals -- and **2 INVOKER-WRITABLE writers, not
1.** `month` reached the single-quoted SSM string UNVALIDATED:

```
event {"mode":"run","month":"2026-08 --fixture-remove cottonwood:2026-08-04"}
  _forcing_spec(event) -> ''            the purpose-built fence CORRECTLY refuses
  '--fixture-remove' in the command -> True    and it arrives anyway, through `month`
```

**LIVE IN THE SERVED FUNCTION SINCE 01:16:14Z**, unreachable by the schedule, reachable by any hand invoke -- and it
also reached `--s3-out` and `--no-ladder`. Fenced by `MONTH_RE` inside `_render_command`, **the one place the string
is built**, failing loud. Row `W4-S5`, disarmed same turn.

⭐ **THE ASSIGNEE'S OWN SENTENCE IS THE FINDING:** *a fence on ONE WRITER of a property is not a fence on the
PROPERTY.* It named this as the same coverage error as its own `W4-S4`, one layer down. **A purpose-built control
that is correct in itself and covers one of two writers reads exactly like a control that works.**

**The three hardened conditions all held and were proven the right way round.** (a) EG-s-25's renderer was verified
SERVED BEFORE the apply by the assignee's OWN sha256 against its own pre-EG-s-25 baseline with zero disclosure
tokens, re-read after -- the proof obligation, not the sequence, satisfied by measurement rather than by the issuer's
word. (c) the LIVE rule's `Input` is `{"mode":"run"}`, 1 key, with `mode` present as the positive control while
`test_run`, `force_fixture_remove` AND `month` read absent -- the payload, not the code. (d) 0 globals, 0 env writes,
0 SSM/S3 persistence, warm-container tested.

**THREE OF ITS OWN INSTRUMENTS WERE WRONG BEFORE THEY WERE RIGHT, ALL CAUGHT PRE-RECORD:** an arm passing on a
**0-of-0 log window** (a gate on an empty set) until a control window returning 1 START of 4 was added; a
case-sensitive token check calling a phrase ABSENT that the entry carries in capitals; and a token count that would
have reported two writes where both sites are reads. ⛔ **And one worth every seat's attention: a Bash call whose
`grep` segment was DENIED BY THE RAIL aborted the WHOLE CALL, so a status flip the assignee believed had run had
not.** A rail denial mid-compound-call is a silent no-op for every later segment; only its verify-after-write caught
it.

**6. `EG-s-25`: THE VERDICT NOW DISCLOSES ITS OWN FORCING, AND THE UNFORCED CASE IS ENFORCED BY THE DEFAULT PATH.**
6 of 6 arms, `EGS25-VERDICT-DISCLOSES-FORCING`. `coverage_verdict.json` records how the run was configured on BOTH
branches -- forced `{"forced": true, "mechanism": "--fixture-remove", ...}` and unforced
`{"forced": false, "mechanism": "none", ...}`.

⭐ **THE SHAPE IS BETTER THAN THE ARM ASKED FOR.** My arm (c) required an unforced run to write the field explicitly.
The assignee made `coverage_gate` emit the record with ALL-DEFAULTED ARGUMENTS, so **a caller cannot omit it by
forgetting** (suite test `(j)`). That converts a rule someone must remember into a property of the code.

**The verdict did not move:** old deployed bytes against new, **5 of 5 pre-existing keys and 10 of 10 class counts
identical across a PUBLISH and a REFUSE scenario, exactly one key added.** Deployed and byte-verified to the artifact
prefix under a closed NEVER-2 entry (opened 05:18:38Z BEFORE the 05:19:33Z copy, closed 05:24:13Z BEFORE the grading
reads), rollback exact from two independently verified sources.

**ON THE RUN ID, since `S25-AC2` asks:** it is NOT the SSM `CommandId` -- the orchestrator holds that and does not
pass it to the renderer, and threading it would have meant editing `EG-s-24`'s LIVE surface. It is a uuid4 printed as
`RUN-ID:`, joinable via SSM's `StandardOutputContent`, with `run_id_source` stating WHICH id it is on every record and
`ETFS_RUN_ID` winning if a caller supplies a better one. **A limitation recorded on the artifact rather than hidden.**

⛔ **AND THE BLOCKED STATE WAS SILENTLY DEGRADING THE VALIDATION, which is the finding worth carrying.** While the
face was absent from the branch, the proof instance had been validating with **`alignment: NOT EVALUATED`** and
surprises in ANNOUNCE mode -- because `decomp_ref.to_ref` was untracked. After the merge it reads **ENFORCE** on both:
2/2 criteria, 1/1 cell in a 29-cell index, surprises 4 of 4. **A blocked flip is not only a stuck order; it can be a
weaker proof that still says VALID.**

**The assignee proved its channel union rather than trusting it**, capturing both sides' id sets BEFORE merging: 58
shared + 9 + 4, the two added-sets checked for intersection (empty), yielding 71 distinct ids with 0 dropped, 0
duplicated, 0 markers -- compared against that precomputed set. It also corrected two of its own first attempts:
`safe-commit` cannot finish a merge, and `safe-merge --continue` refused to adopt a merge it had not opened, *"it
cannot tell the merge's own staged files from another seat's, which is the one thing --continue exists to check."*

---

## 4. ⛔ THE ONE THING IN THIS ROUND THAT IS NOT REPAIRED, AND IT IS MEASURED

⛔ **R-EG-5 NOW BINDS THIS SECTION (CTO, 94999): NO OUTCOME GRADES `REALIZED` AT ROUND 3'S L10 ON A REPOSITORY GREEN.** FWD-4 and FWD-8 each require their fix DEPLOYED and READ on the deployed artifact as a measured sha256 pair, with an OWNER NAMED for each deploy. There are now **THREE** such gaps, not one, and in all three the deployed bytes hash EQUAL to their PRE-CHANGE blobs.

**(i) THE CLASSIFIER (`EG-s-22`).** Arm (f) required it as a measured sha256 pair and got one: deployed 10,157 B `23c30889...` against built 12,226 B `b2ab67fd...`, CRLF 0 in both. **The extra fact the arm did not ask for is the load-bearing one: the deployed bytes hash EQUAL to the pre-change blob.** The box is reading exactly the un-fixed classifier, so **the served verdict object cannot discriminate until someone deploys these bytes.**

Stated in the assignee's own framing because it is exact: *until that owner acts, this cell's green is a property of the repository and not of the estate.* This cell deployed nothing by design -- the deploy is a separate act with a separate owner, and the arm exists so the gap is a number somebody carries rather than an assumption nobody wrote down. Carried to `1.0.0_SA_CTO` for L10 placement WITH an owner. **The CVO should not read `EG-s-22` as closing FWD-4 on the served plane; it closes it on the repository plane and says so.**


**(ii) THE EGRESS ASK (`EG-s-23`).** Deployed 11,011 B `3c3ce6c5...` against built 15,011 B `25ff4dbed4...`, **and the
deployed bytes hash EQUAL to the pre-change blob** -- so the box is running exactly the OVERWRITING version and every
future ladder run still overwrites one partner's ask with the next. **The served 2026-09 ask (1,017 B, 01:20:20Z)
still names 1 of 2 outstanding days and is NOT repaired by this cell**, which writes no served key.

**(iii) THE RENDERER (`EG-s-25`, in flight).** Its own cell carries the deploy -- an `aws s3 cp` to the artifact
prefix, because the box pulls that file by key at run time -- so this gap closes inside round 3 rather than being
carried. It is listed here so the denominator of deploy gaps is THREE and not two.


⛔⛔ **AND ROWS `S33`/`S34` SAY THE PREFIX IS NOT THE RUNNING PLANE, WHICH IS WHY R-EG-5 WAS AMENDED (CTO 95024).**
An upload to the artifact prefix **does not reach the box** for the coverage package: `_render_command` copies
exactly ONE object from that prefix (`lambda_function.py:348`, the renderer) and the renderer self-bootstraps the
package ONLY inside an `except ImportError` branch (`render_month_end.py:117-128`). Once `/opt/etfs-reports/coverage/`
exists on EBS the import succeeds and the pull never runs again.

**`S34` ANSWERS `S33`'s OWN FALSIFIER BY A READ OF EXISTING HISTORY, without touching the box.**
`platinum/reports/2026-08/coverage_verdict.json` exists at 1,225 B, `LastModified 2026-09-10T00:24:44Z` -- **an
object only the coverage package can produce.** So the import RESOLVED on that run and the package is on the box.
**The conclusion holds on both branches:** resolved from a pre-existing copy means it was already there; resolved
only after the bootstrap pulled means it is there now because the pull put it there. Either way the next import
succeeds and the bootstrap does not fire.

**RESIDUAL, stated:** this is scoped to the CURRENT instance. A replaced EC2 instance would present an empty `/opt`
and the bootstrap would fire once. Whoever owns the deploy reads the instance id beside the bytes.

**CONSEQUENCE FOR THE CVO AT L9:** no deploy claim for the classifier (`EG-s-22`) or the egress ask (`EG-s-23`) can
be accepted on a prefix read, and neither has a delivery path today that does not depend on an import failing.


⛔⛔ **THE INJECTION WINDOW IS NOW MEASURED (CTO 95046) AND THE CVO SHOULD GRADE `S24-AC2` KNOWING IT.** The fence is
applied; whether the hole was gone through is a different question and the CTO ran it. **Its FIRST instrument could
not answer and it nearly took the zero:** CloudTrail management events return 4 in the window and ZERO Invokes --
**a FALSE ABSENCE, because Lambda Invoke is a DATA-plane event this account's trail does not select.** The second
instrument, the function's own log group, holds **EXACTLY ONE START** in the window: 01:19:06Z, RequestId
`9fbc33e0-174c-4c82-b392-2b1dafe4a835`, 82,718 ms. **THE ARGUMENTS ARE NOT RECOVERABLE** -- the group holds only the
runtime's INIT_START/START/END/REPORT because the function emits no line of its own. So: the exposure was real, the
window held exactly one invocation, it falls three minutes after this project's own deploy with a duration consistent
with the dispatched work, and only this estate's credentials can reach it. **What is NOT stated is that nothing went
through**, and that restraint is the right shape: "ours by attribution" is exactly as strong as the evidence goes.

**THE COMPOUNDING GAP IS WORTH MORE THAN THE INCIDENT:** a function whose parameter reaches a SHELL COMMAND logs
NOTHING about what it was asked to do. That is an AUDIT FLOOR, not a monitoring wish -- you cannot review an
invocation you cannot see -- and it compounds `W1-S26`, the same absence on the same function. No remedy is proposed
from any seat: emission sits under Andrew's standing moratorium and is recorded as a measured fact for his decision.

---

## 5. THE JUDGMENT CRITERIA -- THIS IS THE L9 WORK

- **`S19-AC2`** (recorded, no verdict): whether the branch recovered a hole it discovered ITSELF (the log's own lines quoted), what the restored slice differs in from the archived original (32 of 32 field cells compared, **0 differences**), what the branch would have done had the upstream partition been absent, and what a single-day single-partner exercise still does not prove about a multi-day or multi-partner gap. **Two things the assignee volunteered beyond the criteria:** a date with NO upstream partition is **invisible** in the producer's response -- `2026-09-09` appears in none of `catchup_processed`, `catchup_failed` or `catchup_skipped_unpriced`, so a silent skip and a healthy day are indistinguishable to a consumer reading only that response; and its mutant control fires but arms (b)/(c)/(d) still pass under it because they key on the evidence ledger's recorded names rather than the `HOLE` constant, so the control exercises the three arms carrying the actual claim and not those three.
- **`S20-AC3`** (recorded, no verdict): evidence with vintage for the send path. **Read the assignee's own correction inside it:** its FIRST closes of ledger legs L3 and L4 stated a deployed-member sha256, a line count, an AST-node denominator and two hit counts **it had not measured**, written from expectation while the measuring battery was still running. Both legs were re-closed with measured values and the entry's NEVER-2 DETAIL carries the wrong-vs-measured table. **No conclusion moved, which is exactly why it is named.**
- **`S25-AC2`** (recorded, no verdict): the run id's true nature and why it is not the CommandId; the consumer census (**71 hits / 29,502 files, 3 code readers of the object**); and 5 named limits.
- **`S24-AC2`** (recorded, no verdict): the forcing key's shape and why it cannot be confused with a scheduled field; what a caller could still do wrong with it; the `_render_command` caller census (**1 of 1**, asserted by an AST arm with `forcing` defaulted); and what the seam does NOT make reachable.
- **`S23-AC2`** (recorded, no verdict): the shape chosen and why; what the SERVED ask currently omits with both
  counts and its vintage, since that is the artifact a person would have authorised on; the consumer census with
  its denominator; and what the change does NOT repair.
- **`S22-AC2`** (recorded, no verdict): the shape chosen and why; what the change does NOT repair (row `S20`, the producer); and the `DEPLOYED != BUILT` number from arm (f) with the sentence that the served verdict cannot discriminate until someone deploys. Two caveats the assignee stated against itself: arm (e) runs `probe=None` so its tables read `UNKNOWN=1` where the SERVED verdict reads `D=1` -- the before/after is sound and **is not a reproduction of the served counts, and it does not claim to be**; and its first read of arm (d) showed `0 passed` while rc was 0 and the suite green, because `pytest -q` colourises its summary so the count is not a bare token -- **its parser bug, not the world**.

---

## 6. ROWS AND THEIR STANDING AT THIS SEAT (5 filed this round; channel denominator 62)

| row | class | standing |
|---|---|---|
| `W5-S1` | OBSERVATION / INERT | **ISSUER'S CUT DEFECT.** Arms (d) and (g) of `EG-s-19` were JOINTLY UNSATISFIABLE: (d) mandates the rule's own shape, (g) forbade any other `daily/` key changing, but the handler ALWAYS re-PUTs the newest slice (`lambda_function.py:310-311`) BEFORE `_catchup_missing_dates` at `:312`. RE-CUT @`b6adbaf70c` onto CONTENT with the touched keys enumerated and printed. No re-run owed -- the evidence was already taken (0 of 273 content-changed; `daily/cottonwood/2026-09-08.json` ETag `5da999e2fbfadfe3...` and Size 1345 identical both sides). |
| `W5-S3` | OBSERVATION / INERT | **ISSUER'S CUT DEFECT.** "Byte-equal to the rule's delivered envelope" is unreachable for ANY payload -- EventBridge stamps a per-delivery UUID and `time`, and the producer never logs its `event` (`:297-312`). RE-CUT @`b6adbaf70c` onto three measured facts: the target at 1 of 1 with no `Input`/`InputPath`/`InputTransformer`, shape-equality, and branch-equivalence at `:300-302`/`:304-308`. |
| `W5-S2` | OBSERVATION / INERT | RULED INERT on the ASSIGNEE'S reasoning: the one in-project bare-`daily/` enumerator filters `LastModified` on `2026-09-10T01:` and the archive is stamped 03:45:24Z. **CARRIED, not closed** -- `opal-data-etfs` has versioning DISABLED so the archive IS the standing rollback and cannot be removed; every future bare-`daily/` census inherits a **permanent +1** denominator. Now PRD line **R-EG-3** @`8563434d16`. |
| `W1-S32` | BLOCKING / INERT | **ISSUER'S CUT DEFECT.** `EG-s-22`'s face was cut with a prose acceptance section and NO `criterion` tags, so `proof-of-spec-check` read `0/0 criteria carry >=1 cell_ref` and the flip was UNREACHABLE. The assignee held the file in its grant, **refused to add them**, and was right. Disarmed @`12f16b46f5`. **Census by SUBTRACTION: 23 faces, 22 carrying both tags, blast radius exactly 1.** Carried to the CTO: the L6 gate does not check that a face carries a gradable criterion at all. |
| `W4-S1` | OBSERVATION / ARMED -> **DISARMED THIS TICK** | **ISSUER'S FACE DEFECT, and the correcting report was ALSO half wrong.** See s.7. |

---

## 7. ⛔ W4-S1 -- DISARMED, AND THE SOURCE REFUTED BOTH REPORTS

`EG-s-20`'s face carried an OPERATING FACT that `safe-apply`'s identity gate is satisfied by exporting `OPAL_AGENT_SERIAL`. `0.9.0_WK_ETFS_GUARDRAIL~4` measured that its first apply returned **rc=3 with the variable exported** and reported that "`safe-apply` never calls `resolve-actor.sh`". **I read the source rather than adopting either claim, and both were wrong** (`3772d12515`):

```
safe-apply.sh:11,50      runs .tools/halt-gate-check.sh FIRST, before anything else
halt-gate-check.sh:56-57 identity from org/mcp/sessions/$CLAUDE_CODE_SESSION_ID.serial ONLY
                 :76-80  or a $CLAUDE_CODE_SESSION_ID.<serial>.orphan-cleaned marker
                 :274    HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)
                         -- OPAL_AGENT_SERIAL appears ZERO times in this file
safe-apply.sh:152-154    THEN sources lib/resolve-actor.sh and calls resolve_actor,
                         which DOES honour $OPAL_AGENT_SERIAL (refuting the report)
```

**THERE ARE TWO GATES AND THE ORDER IS THE MECHANISM.** The halt gate decides **whether the apply runs at all** and cannot see the variable; `resolve_actor` decides **whose serial is written into the audit** and can. Exporting it satisfies the gate that runs SECOND and never reaches the one that runs FIRST. My provisioning fix was NECESSARY AND NOT SUFFICIENT, and a worker following my face exactly was blocked.

**DISARM, executed this tick:** the live carrier was not a task face -- `EG-s-21`'s face was censused and carries no such sentence, and `EG-s-20` is terminal -- it was **my own spawn procedure**, banked as a memory entry that would have fired unprompted on every future Terraform-applying worker. That entry is corrected at source with both limbs: export the variable (so the audit names the true actor) AND tell the worker that the halt gate's OWN PRINTED REMEDY at `halt-gate-check.sh:118` is legitimate and expected -- writing its serial to the gitignored `org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial`, which is what `~4` found and used correctly.

**THE GENERAL FINDING, offered to the CVO because it cost two rounds:** a fix aimed at the helper whose NAME MATCHES THE SYMPTOM can satisfy a real gate and still never reach the gate that fires. `~1` hit rc=3, I read `resolve-actor.sh` alone because it was the file called "resolve actor", and I banked a fix that a second worker then disproved on the same symptom. **Neither worker's mechanism claim nor my own earlier note was reliable; only the source settled it.**

---

## 8. WHAT THE ISSUER DID NOT DO

No served object was deleted or rewritten BY THIS SEAT (the one served delete is `EG-s-19`'s, on Andrew's explicit word, archive-first, with the archive retained as the standing rollback). No deploy by this seat -- the mailer deploy was `~4`'s under its own NEVER-2 entry, and the classifier is deliberately UNDEPLOYED. No send and no invoke of `etfs-reports-orchestrator` in any mode. No push: origin/CLOUD @`c6bcb7b12b` (ls-remote read 02:39:42Z, this seat), and every commit named here is LOCAL. The two running orders were not interrupted to build this packet.
