# ETFS_GUARDRAIL round 3 -- L8 PACKET (PARTIAL: 3 of 5 orders terminal; revised in place at each drain)

**Compiled by** `2.0.0_SA_COO` 2026-09-10 ~04:4xZ at the first compile of round 3, on the `/drive` obligation "terminal orders -> L8 compile NOW; the compile is an act, never a wait."
**For** `3.0.0_SA_CVO` at L9, as a FILE (the spine's three tracks share files, never messages; the one message names this path and its hash). **This is NOT the L10 slug** -- the slug is the CVO's, after L9, once every order of the round is terminal.

⛔ **A CORRECTION TO MY OWN LAST TICK, STATED BECAUSE IT WOULD OTHERWISE READ AS A CHOICE.** The tick-52 log said this packet was "owed at the round's close, not per-order." That was wrong on the obligation's own words and wrong against this project's round-2 practice, where the packet was compiled at the FIRST drain and revised in place five times. Three orders sat terminal and drained with no packet, which is precisely the hard gate's "uncompiled terminal order". Compiled now, one tick late, and the lateness is recorded rather than absorbed.

---

## 1. THE ROUND, AS IT STANDS AT L7

Round 3 is the round Andrew's ~03:0xZ law built -- **no FWD is a wait**. It opened as three cells on PRD v0.5 (`EG-s-19`, `EG-s-20`, `EG-s-21`, ONE issuance @`ea47e92a72`) and was widened TWICE BY AMENDMENT, both times on an artifact that arrived mid-round rather than on a schedule:

- **`EG-s-22`** @`eab3712b31` (decomp v0.4 s.13), on the CTO's placement of row `W1-S31` at 94947 -- PRD v0.6 row `S19`, the classifier half ruled INSIDE this project's surface while the producer half was placed OUT at row `S20`.
- **`EG-s-23`** @`5aeb940bd0` (decomp v0.5 s.14), on the ROUND-2 ANALYSIS at 94988, which graded FWD-8 NOT_REALIZED and listed three cells still to place. Two were already cut; this was the third.

`fanout: 3 of 3 chains, cap 8`. Five cells serving **five outcomes**: FWD-1, FWD-4, FWD-8, FWD-9, FWD-10.

| order | cell | outcome | slot | state |
|---|---|---|---|---|
| TO-EG-s-19 | EG-s-19 | FWD-1 | `~5` | **TERMINAL**, drained @`56cfbb2505` |
| TO-EG-s-20 | EG-s-20 | FWD-10 (precondition) | `~4` | **TERMINAL**, drained @`5d292ff11f` |
| TO-EG-s-22 | EG-s-22 | FWD-4 | `~1` | **TERMINAL**, drained @`ecd50f3096` |
| TO-EG-s-21 | EG-s-21 | FWD-9, FWD-10 | `~4` | RUNNING |
| TO-EG-s-23 | EG-s-23 | FWD-8 | `~1` | RUNNING |

---

## 2. THE TERMINAL ORDERS, re-validated AT THIS SEAT on the merged tree

Criterion ids taken from the ORDER at HEAD and passed as the checker's third argument -- never from the worker's report.

| order | instance (under `deliverables/`) | checker at this seat | drained at |
|---|---|---|---|
| TO-EG-s-19 | `0.9.0_WK_ETFS_GUARDRAIL~5/...TO-EG-s-19.the-catch-up-branch-driven.proof_of_spec.json` | **VALID rc 0**; 2/2 criteria carry a cell_ref, 1/1 resolves to the decomp, 1/1 cell reachable; 3 of 3 surprises resolve | `56cfbb2505` |
| TO-EG-s-20 | `0.9.0_WK_ETFS_GUARDRAIL~4/...TO-EG-s-20.the-send-path-correct-and-test-safe.proof_of_spec.json` | **VALID rc 0**; 3/3 criteria carry a cell_ref, 1/1 resolves, 1/1 reachable; 1 of 1 surprise resolves | `5d292ff11f` |
| TO-EG-s-22 | `0.9.0_WK_ETFS_GUARDRAIL~1/...TO-EG-s-22.the-classifier...proof_of_spec.json` | **VALID rc 0**; 2/2 criteria carry a cell_ref, 1/1 resolves, 1/1 reachable; 1 of 1 surprise resolves | `ecd50f3096` |

---

## 3. WHAT THE OUTPUT SAYS -- three findings, and the first is the round's product

**1. `EG-s-19`: THE CATCH-UP BRANCH RAN FOR THE FIRST TIME IN THIS ESTATE, AND FOUND THE HOLE ITSELF.** 8 of 8 arms, `EGS19-CATCHUP-BRANCH-DRIVEN`. The discriminator that matters: `catchup_processed: ["2026-09-03"]` while the response's own `date` field reads `2026-09-08` -- **the catch-up path, not the main path**, which is exactly the dead end `EG-s-17` hit when `_latest_partition()` made the target its own `skip_date`. The restored slice is byte-identical to the deleted original: sha256 `060188a6e76b2275...` on original, archive AND restored. Andrew's ~02:5xZ constraint was proven on **three independently-failing planes** rather than asserted: the deployed bytes (1 of 1 file, 0 mailer tokens -- no send call exists), the role (0 `ses:` actions across 3 of 3 policies), and the window (`AWS/SES` Send/Delivery/BounceRate all 0 datapoints).

The date choice is worth the CVO's eye because the REJECTIONS carry the reasoning: `2026-09-08` is the newest priced partition and would have been skipped at `:268-269`; `2026-09-09` has `partition: false` so a hole there is damage rather than a test; `2026-09-05` is not a trading day so its absence is correct; `2026-09-04` was eligible on all four properties and was **deliberately held back as the 200 positive control**.

**2. `EG-s-20`: THE SEND PATH IS CORRECT AND TEST-SAFE, AND THE DISCRIMINATOR IS WHY THAT SENTENCE IS BELIEVABLE.** `S20-AC1` 15 of 15 in the named file (round-1 floor 7, +8), 20 of 20 across the directory; `S20-AC2` 20 of 20 arms, `EGS20-SEND-PATH-CORRECT-AND-TEST-SAFE`. **The same new arms run against the PRE-FIX blob fail 7, with the headline arm failing on `AssertionError: exactly ONE terminal send on the refusal branch` -- i.e. ZERO sends, which IS the defect.** An arm that passes against both the fixed and the broken code proves nothing, and this one was shown not to.

Measured on the DEPLOYED bytes: **aj@ in 0 of 24 test resolutions** (12 adversarial events x 2 carriers -- list, joined string, mixed, different case, padded, duplicated, empty, null, truthy-non-boolean marker, non-`run` mode); an all-forbidden override resolves to `[]` and makes **0** SES calls; a default test invocation resolves to `['andrew@opalinvest.com']` with a printed `MessageId`. **The scheduled direction is UNCHANGED at 5 of 5** marker-free payload shapes resolving to both recipients, identical to the module's own `EMAIL_RECIPIENTS`, with the live `EMAIL_RECIPIENT` env var untouched.

⭐ **THE ASSIGNEE REFUSED THE WEAKER SHAPE THE FACE PERMITTED, and its reason is better than my cut.** The face allowed "no send on a test invocation". It declined, because that would make **FWD-10 unprovable by construction** -- FWD-10's whole content is that the send FIRES and reaches andrew@. It built an unconditional forbidden-recipient FILTER that runs LAST instead, because a replacement is a default and a default is defeated by the next caller who passes an override. Taking a harder shape to keep a DOWNSTREAM outcome provable is judgment no criterion asked for.

**3. `EG-s-22`: THE CLASSIFIER NOW DISCRIMINATES, AND THE SHAPE WAS CHOSEN ON THE AXIS RATHER THAN ON THE PRICE.** 7 of 7 arms, `EGS22-CLASSIFIER-DISCRIMINATES`. Arm (a) reproduced the defect FIRST on the pre-change classifier pinned at `c866edd324` with the slice fetched live (1,209 B, 4 priced rows on a market holiday): both cases returned the byte-identical `{"class": "A", "probe": null, "reason": "market closed (not a trading day)"}`.

The assignee chose a **FIELD** (`slice_on_closed_day`), not a new class value, and its reason is the one to record: the class axis answers *"is this a hole, and why"*, while whether an artifact turned up is an orthogonal fact about a **different actor with a different remedy owner** (row `S20`). That is rule 24 (iii)/(iv) deciding the question mechanically rather than by taste. Consequence: `_CLASS_NAMES` is untouched, no four-postulate record or token census is owed, and **arm (e) PROVED the arithmetic did not move rather than asserting it** -- 27 partner-day records both sides, **0 counts moved**, `trading_days` and `holes` identical, all 9 changed records class A.

⭐ **It added TWO PERMANENT REGRESSION ARMS to the estate's own suite, unasked** (8 -> 10 passed, 0 failed both sides). The defect existed *because nothing covered it*, and a one-shot battery would have left that true. Both assert `with_slice != without`, which arm (a) measured byte-identical on the old code -- so both would FAIL against the world they were written to catch. They are controls, not constants.

---

## 4. ⛔ THE ONE THING IN THIS ROUND THAT IS NOT REPAIRED, AND IT IS MEASURED

**`DEPLOYED != BUILT` ON THE CLASSIFIER.** Arm (f) required it as a measured sha256 pair and got one: deployed 10,157 B `23c30889...` against built 12,226 B `b2ab67fd...`, CRLF 0 in both. **The extra fact the arm did not ask for is the load-bearing one: the deployed bytes hash EQUAL to the pre-change blob.** The box is reading exactly the un-fixed classifier, so **the served verdict object cannot discriminate until someone deploys these bytes.**

Stated in the assignee's own framing because it is exact: *until that owner acts, this cell's green is a property of the repository and not of the estate.* This cell deployed nothing by design -- the deploy is a separate act with a separate owner, and the arm exists so the gap is a number somebody carries rather than an assumption nobody wrote down. Carried to `1.0.0_SA_CTO` for L10 placement WITH an owner. **The CVO should not read `EG-s-22` as closing FWD-4 on the served plane; it closes it on the repository plane and says so.**

---

## 5. THE JUDGMENT CRITERIA -- THIS IS THE L9 WORK

- **`S19-AC2`** (recorded, no verdict): whether the branch recovered a hole it discovered ITSELF (the log's own lines quoted), what the restored slice differs in from the archived original (32 of 32 field cells compared, **0 differences**), what the branch would have done had the upstream partition been absent, and what a single-day single-partner exercise still does not prove about a multi-day or multi-partner gap. **Two things the assignee volunteered beyond the criteria:** a date with NO upstream partition is **invisible** in the producer's response -- `2026-09-09` appears in none of `catchup_processed`, `catchup_failed` or `catchup_skipped_unpriced`, so a silent skip and a healthy day are indistinguishable to a consumer reading only that response; and its mutant control fires but arms (b)/(c)/(d) still pass under it because they key on the evidence ledger's recorded names rather than the `HOLE` constant, so the control exercises the three arms carrying the actual claim and not those three.
- **`S20-AC3`** (recorded, no verdict): evidence with vintage for the send path. **Read the assignee's own correction inside it:** its FIRST closes of ledger legs L3 and L4 stated a deployed-member sha256, a line count, an AST-node denominator and two hit counts **it had not measured**, written from expectation while the measuring battery was still running. Both legs were re-closed with measured values and the entry's NEVER-2 DETAIL carries the wrong-vs-measured table. **No conclusion moved, which is exactly why it is named.**
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
