# /self-drive NFRA_OPSEC202609 -- ticks 8-10 (2026-09-03 ~13:1xZ-13:4xZ), 1.0.0_SA_CTO~Z

state: ARMED | cron 30635e1e (:13/:43) | carrier org/XXX.md CTO row @f41a37322e | paired: solo | last log: tick 7 @bd311c0e29 (+ amendment @81d0a9fc8d)
scope: NFRA_OPSEC202609 (D12, site-z) -> 1 project (denominator: 1 of 13 live directives) | device SITEZ | completion test: NOT DONE

## The tick that mattered: tick 8, one call, one verdict, one PRD version

**The call.** `opal-data-security` was one bucket doing two jobs. C-8 required the project customer-managed key on it;
C-13 scoped that key to three IAM roles; and the bucket is written by TWO AWS service principals delivering
CloudFront and ALB access logs, landed by the COMPLETE cell OP-s-5. Both constraints were correct and could not hold
in one bucket, because S3 default encryption is per-BUCKET and not per-prefix. So the key flip C-13 required was
predicted to stop both live delivery legs SILENTLY. `0.7.0_AE_CloudOps~S` surfaced it before any write (Z-S37) and
`2.0.0_SA_COO~Z` routed it to L4 rather than ruling at L6, correctly: the gap was in a constraint this seat ratified.

**The measurement that decided it.** `list-objects-v2` on the bucket: 36 objects, EVERY one under `waf-logs/`, newest
13:10:11Z, and `cases/`, `reports/`, `allowlists/` EMPTY. The issuer had framed the split as "move the logs out, if
those services can even use a customer key" -- a question nobody can answer safely, since every candidate to test on
is another live log destination. The census inverted it: **move the EMPTY surface instead.** Nothing live moves, the
COMPLETE cell is not reopened, and the answer holds whether or not the unmeasurable variable resolves yes. A ruling
that does not depend on an unmeasured fact beats one that does, even when the fact would probably go our way.

**The verdict (19801) improved the reasoning, not just the outcome.** The pitch defended the split as correcting an
authoring conflation of this seat's own -- available, but weak, because "the author conflated two things" invites a
later reader to reopen it. `3.0.0_SA_CVO~Z` found the stronger ground in the RATIFIED TEXT: 7.3 already read
"(Firehose raw, if S3 delivery is chosen over CloudWatch Logs)" and row S5 already read "CloudWatch Logs
`aws-waf-logs-opal-{scope}`, or Firehose into S17 `waf-logs/`". The split SELECTS a branch the design names. It also
attached the one caution that keeps the amendment honest: FWD-18's ACCEPT names "every case, LOG EXTRACT and
allowlist", so the new store must HOLD the log extracts a case cites; only the RAW DELIVERY STREAM moves. An
amendment reading "logs leave the evidence store" would have left FWD-18's own acceptance unsatisfiable by the thing
it builds -- one word too wide, the same shape this project has been catching all day.

**What landed** -- PRD v0.9 @001709c96e: C-8 amended to `opal-security-evidence` under the project CMK; NEW C-16
keeping `opal-data-security` at SSE-S3 as FWD-5's log destination; C-15's target following the store; 7.3 split into
two path lists with the `waf-logs/{scope}/` grammar corrected to name the three kinds that actually deliver (the
FIFTH referent in C-8's family); manifest S17 re-pointed, NEW row S28 for the log destination. **C-13 and C-14 stand
UNAMENDED and become exactly right**: under the split the CMK bucket has no service-principal writer, so the
three-role key policy is correct as written. What was wrong was never the key policy. FWD-18 unchanged.
Ledger row 4 carries the operative sentence verbatim; the L4 handoff went to the issuer (19808).

**The precedent was this seat's own**, and the issuer found it: C-15 ruled the sibling access-logs target SSE-S3
rather than the project key at ~08:3xZ, for exactly this reason, with the reason written down at the time. The same
question had already been asked and answered four and a half hours earlier on a bucket of the same shape.

## The gate investigation, and why nothing was filed

Grading the amendment, the first conformance run returned an empty verdict -- which I nearly recorded as a pass. It
was not: an ABSENT file returned the identical empty result, so the harness was a NO-OP and the reading meant
nothing. Corrected, the limb has its own ran-discriminator and returned "step-4 conformance graded 1 PRD(s) with an
ENDPOINT section -- OK", which is a real pass.

Then three mutants all passed, which looked like a broken gate on this seat's own surface. **Before filing a defect
row I checked whether the limb had RUN on the mutants -- it had not** (graded 0, notes empty). Called directly, the
core catches the exact mutation with the exact right message: "PRD_HEADER.fabric='laptop' but the register row says
'site-z' -- two carriers of one quantity must agree." So the gate discriminates, the wrapper skip is an artifact of
staging a blob by `update-index --cacheinfo` rather than a finding, and **no defect was filed.** The residual -- why
that staging path makes the wrapper skip -- is unexplained and recorded here rather than as a row, because the
instrument was non-standard and a defect claim I cannot support is worse than no claim. If it recurs under a normal
`git add`, it becomes a row.

Worth keeping: the FIRST run and the MUTANT runs both returned "no violations", and they meant opposite things --
one because the file was clean, one because the check never ran. **The discriminator was never the verdict; it was
the note saying how many PRDs got graded.**

## Ticks 9 and 10

Quiet on calls. Tick 9 confirmed the verdict landed and the handoff fired. Tick 10: zero open calls, zero verdicts
pending, no new commits since the PRD, inbox empty. Three foreign rows are sitting UNCOMMITTED in the channel file
(worktree 40 rows, HEAD 37) belonging to other seats, so this log commits the log alone and does not touch that file
-- the discipline that came out of this morning's sweep class.

## Scope state (denominators printed)

| project | status | dep_stage | task orders | rows | ledger |
|---|---|---|---|---|---|
| NFRA_OPSEC202609 | active | EXECUTING (round 2) | 8 cut, 5 carrying a valid proof instance | 40 in the worktree (15 ARMED), 37 at HEAD | 4 rows |

Completion test: **NOT DONE** -- 1 of 1 members REACHABLE, 0 complete, 0 UNREACHABLE. The decomposition is not spent.
RESERVED cards at Andrew on this scope: **none**. The two Andrew-gated items on this device sit on a SIBLING D12
project (the carrier-verification text and the toll-free number), not on this one.

## CORRECTION (13:4xZ, one minute after this log was committed): the "three uncommitted foreign rows" claim was FALSE

This log said, in Ticks 9 and 10: "Three foreign rows are sitting UNCOMMITTED in the channel file (worktree 40 rows,
HEAD 37) belonging to other seats." **Measured immediately after the commit: HEAD 40 rows, worktree 40 rows, `git
status` on the file EMPTY. Zero uncommitted rows.** Z-S38, Z-S39 and Z-S40 were committed by their own authors
(the last at dd977d7f31, 3.0.0_SA_CVO~Z). Nothing was uncommitted and no seat had work at risk.

HOW THE CLAIM WAS MANUFACTURED, because the shape is the same one this log spends a section on: this seat read the
WORKTREE row count at tick 8 (37), read the WORKTREE row count again at tick 10 (40), then ran `git log
001709c96e..HEAD` which returned empty and concluded the three new rows must therefore be uncommitted. **That range
was empty for a trivial reason -- 001709c96e WAS HEAD at that moment -- so it proved nothing whatever about when
those rows landed. The one number that would have settled it, HEAD's own row count, was never read.** A difference
between two readings on ONE plane got attributed to the OTHER plane, on the strength of a range query that could not
have returned anything else.

WHAT CAUGHT IT: the foreign-row check run one second after the commit, as pre-commit discipline on a file this seat
was not even committing. Its first line reads "40 row(s) at base -> 40 in tree", and "at base" IS HEAD. The
instrument printed the disconfirming number in its ordinary output; it only needed reading.

WHAT IS UNAFFECTED: the decision not to touch the channel file was correct anyway and cost nothing -- this log had no
business in that file. Everything about tick 8, the verdict, PRD v0.9 and the gate investigation stands; the false
sentence is confined to the Ticks 9 and 10 paragraph and is withdrawn here rather than edited above, since the log is
a committed record.

THE COUNT, since this seat has now made the same class of error three times today (the 31-routes subtraction, the
"no fourth instance" scope, and this): every one printed a denominator faithfully and every one attached it to a
question the instrument could not answer. The recurring defect is not missing evidence. It is evidence measured on
one plane and spent on a claim about another.

## Compiler Tools

- the deciding read: `aws s3api list-objects-v2 --bucket opal-data-security` (36 objects, prefix census, newest stamp)
- the DECLARED read: `infra/aws/terraform/opsec/kms.tf` -- three statements, the two delivery service principals 0 times
- grounding validation of the verdict: all three citations resolved at PRD v0.8 @36786251af, file byte-identical at HEAD
- conformance: `check_prd_conformance(root, <task-order rel>)` reading the STAGED index, ran-discriminator in its notes; `_prd_conformance` called directly for the falsifier arm
- ledger: `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/NFRA_OPSEC202609/VERDICTS.jsonl` (4 rows)
- foreign-row discipline: scratchpad `foreign_row_check.py`, identity from the seat serial, fails closed
- push state: LOCAL (0.0.0_AB_MSTR~Z integrates SITEZ; LD-0367)
