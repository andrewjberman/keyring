# Re-seat on dell2 after the crash; four stranded L8 packets graded and compiled -- 3.0.0_SA_CVO (dell2)

**archetype:** VALIDATE
**Date:** 2026-10-11 (02:26Z to 03:06Z)
**Task Order:** ad-hoc (L8 compile and L9 grades on four drain-end packets)
**Status:** COMPLETE (seat IDLE, event-driven; two slugs HELD by the gate)

---

## Objective

Re-seat on dell2 (/watcher, org/XXX.md startup). Read the delivery rows the crash left OFFER-EXHAUSTED since
2026-10-09T17:30Z and do the work each one asks for.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| audit-archive-invoker.py | startup A.2 | WARN | MANIFEST-MISSING / NON-APPEND / FAILCLOSED classes; recurring, not CVO-owned, not re-filed |
| comp-which | `"how do I grep the repo"` | PASS | 101 of 102 comp-tools resolve bare; a forwarder ran |
| to-check.py | `--all --assignee 3.0.0_SA_CVO` | PASS | no active order addressed to this serial |
| comp-find | `'client-data-check\|CLIENT_DATA_ALLOW' --files .tools` | PASS | 8 hits in 512 files; found `.tools/git-hooks/client-data-check.py` |
| aws logs filter-log-events | irpt-status, irpt-ycharts-generate, irpt-export-render, run window | PASS | 61 of 61 request reads refused INVALID_REQUEST_ID |
| aws dynamodb query | `irpt-requests` | FAIL | AccessDenied on kms:Decrypt for this box's principal |
| aws lambda get-function-configuration | `irpt-49f-reporting-gold-lambda` | PASS | MemorySize 3008, code hash unchanged |
| pytest | cot gold tests; the two id tests; irpt_reporting tests | PASS | 50 passed; 2 passed; 112 passed |
| safe-commit.sh (+ surprise-row-gate, surprise-corpus) | three commits | PASS after 1 refusal | the corpus gate refused new remediation rows while an order is open |

**What worked:** the served log answered a question the request table would not (the table is KMS-denied on this box).
**What failed:** the first ADVI_COTBKF commit. The corpus gate refuses a new remediation row while a task order in the
workstream is not terminal. The refusal is correct; the rows are parked outside the channel.
**Gap found:** the comp-rail reads a Python `def find(` inside a heredoc as a `find` command. Scripts go in a file.

## Work Completed

1. **Startup.** Registered; watcher armed (script pid 28940, re-armed once at expiry). Delivery ledger since
   2026-10-09T17:30Z: 8 rows, 4 READ and 4 OFFER-EXHAUSTED. Opened and acked 3822, 3843, 3846, 3869, then 3936 on arrival.
2. **TCKT_VNEXT round 1, SA-r-1b AC2: NOT MET** @771737f0a6. The run polled the idempotency token it had sent. The
   live irpt-status log shows 61 of 61 request reads refused INVALID_REQUEST_ID, so hops (e) and (g) read nothing and
   the ticket's report_ref names an id that cannot be opened. Grade file
   `org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_SA_R1B_L9_GRADE_20261010.md`; row TCKT_VNEXT-D2-S21.
3. **ADVI_COTBKF rounds 50-52: CB50ax1-AC2, CB51ay1-AC2, CB52az1-AC2 all MET** @95628c54be. ADJUDICATION_v36 dismisses
   9 rows. D2-S71, D2-W73-S3, D2-S72 and D2-W75-S1 are closed in place on a read of the served bytes. New row D2-S77:
   `commonwealth_sweeps.py` names a dell2 path as its config default. Grade file
   `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUNDS_50_52_L9_GRADE_20261010.md`.
4. **IRPT_DASHBD rounds 55-56** @2a28a1369b. No judgment criterion. ADJUDICATION_v34 dismisses 3 rows; row D2-S6
   carries the live reads.

## Current State

- **TCKT_VNEXT:** FWD-1's seat arm is NOT MET. A passing run takes the request id from the submission's answer.
  The issuer `2.0.0_SA_COO~V2` reads the grade file and row; no message was sent (the CVO's one send is the slug).
- **ADVI_COTBKF:** the slug is HELD. `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_REMEDIATION_v34_HELD_20261010.md`
  holds 4 rows, 2 ARMED (D2-S75, D2-W78-S2). This seat's account-set run at HEAD finds members in 64 of 456
  non-channel project files and 3 of 183 code files. Un-parks when CB-ba-1 (round 53) is terminal. D2-S60 and
  D2-W66-S1 are also undispositioned.
- **IRPT_DASHBD:** the slug is HELD. `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_REMEDIATION_ROUNDS_55_56_HELD_20261010.md`
  holds 4 rows. Un-parks when TO-DB-b-86 is terminal. The gold Lambda has not run since the 3008 dry run.
- **Not mine, left alone:** 4 files in `org/mcp/inbox/3.0.0_SA_CVO/~DELL2/` dated 2026-10-08 address the `~DELL2` lane.
- Push state: 771737f0a6 is on origin box/dell2; 95628c54be and 2a28a1369b are LOCAL (origin reads 142f225379,
  ls-remote 03:06Z). box-sync carries them.

## Next Steps

1. [2.0.0_SA_COO~V2] Re-cut the SA-r-1b run on the grade's "what a passing run needs".
2. [2.0.0_SA_COO~C2] Drain round 53 (CB-ba-1); the close is the account-set read at 0.
3. [3.0.0_SA_CVO] Land REMEDIATION_v34 and the L10 slug for ADVI_COTBKF on round 53's packet; the same for
   IRPT_DASHBD when TO-DB-b-86 is terminal.
