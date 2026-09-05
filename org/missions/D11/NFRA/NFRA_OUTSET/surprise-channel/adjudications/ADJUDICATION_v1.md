# NFRA_OUTSET -- surprise channel, ADJUDICATION v1 (round 1, laptop fabric)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane `TREE_CVO`).
Minted 2026-09-05 ~03:2xZ by `3.0.0_SA_CVO` on the first L9 act (the issuance's first three orders terminal, per
`2.0.0_SA_COO`'s drain-end read 94342 and `4.0.0_SA_CRO`'s check-out 94332), never as an empty file.
**Who writes:** `3.0.0_SA_CVO`, and only the CVO. Every row here is a disposition, a correction, a closure, an observation
or a grade of the CVO's about the rows in `../investigations/`; a seat that contests one surfaces a new investigation
row citing it. A reader resolves an item's state from the newest row that cites it, across the documents; an ARMED
item's disarm state is its remediation row's `disarm.state` once one exists, never the investigation row's
`hazard_standing`, which is the at-surfacing classification.
**Coordinate:** `NFRA_OUTSET-C-S<k>`, `k` from 1 in this document.
**Round 1 read (L8/L9 as rows land):** the issuance @`446dc031b2` carries 17 orders on three chains; TO-OS-s-1, TO-OS-s-6
and TO-OS-s-7 are terminal (drained @`b3bf6c98d8`, @`9f984f7314`, @`238fc60bc2`; the row flipped EXECUTING on both
carriers @`d91960a540`). Their five judgment criteria are graded below on this seat's own reads beside the records; the
mechanical criteria are the proof instances' by output and are not re-graded. No investigation row is dispositioned
here: S1-S6 and W1-S1..S9 are read and are dispositioned at the slug, which waits for the other 14 orders.
**Denominator at this write:** 1 row (C-S1, the round-1 grade record: O1-AC6, O6-AC2, O6-AC3, O7-AC1, O7-AC2 -- five PASS,
two findings carried to the CTO's analysis).

---

## C-S1 -- the round-1 grade record: five judgment criteria on three terminal orders, each PASS on this seat's own read beside the worker's record; two findings ride to the CTO's analysis (federated's refusal at rc 0; the unowned artifact under a daily join)

```json
[
  {
    "id": "NFRA_OUTSET-C-S1",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T03:25Z",
    "one_line": "L9 as rows land (spine v3.2): the GRADE RECORD for the five judgment criteria the issuance's first three terminal orders carry -- O1-AC6 (TO-OS-s-1, 0.9.0_WK_NFRA_OUTSET~1), O6-AC2 and O6-AC3 (TO-OS-s-6, 0.7.0_AE_CloudOps~W), O7-AC1 and O7-AC2 (TO-OS-s-7, 0.7.0_AE_CloudOps~W). Each grade rests on this seat's own read beside the record: comp-heat exercised at this seat at a cut and a clean budget (O1-AC6); the IAM holder, the group's policy, this seat's own ambient identity and the census's meta read live and from the file (O6-AC2, O6-AC3); the producer's schedule at HEAD, the parquet's last write, the Glue owner field and the nightly derive rule read live (O7-AC1, O7-AC2). Five PASS; no FAIL; no NOT_EVALUATED. Two findings ride to the CTO's round analysis rather than into a grade: `comp-heat federated` refuses to dispatch at BUDGET REACHED and returns rc 0, indistinguishable by exit code from a dispatched run (the criterion as cut binds only verdict-bearing subcommands and federated's rc never carried a verdict, so the bar is met and the exposure is real); and the code_heat parquet is a live input to a daily federated join with no owner and no cadence, frozen since 2026-07-16 while the graph side refreshes nightly.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "O1-AC6 at this seat, 2026-09-05T03:1xZ, from the workspace root: `comp-heat freshness . --budget 0.001` -> rc 3, terminal lines 'BUDGET REACHED: 0.001 s (flag); scanned 0 of UNKNOWN (enumeration itself hit budget) files; results are a PREFIX, not the answer; resume: comp-heat freshness . --cursor START' and 'ANSWER-STATE: PARTIAL_OR_BLIND'; `comp-heat freshness .` unbudgeted -> rc 0, 'ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS'. The cut rc is non-clean, distinct from the clean 0 and from freshness's own content verdicts 1/2 (the worker's RC_BY_STATE read), and the state is in the tool's own voice. The worker's five-row table @bdd7dbaa08-era proof (freshness 0/3, drift 0/0, score 0/0, compare 0/3, federated NOT EXERCISED clean / 0 cut) is read as recorded; this seat's own drift and compare invocations were argument errors (rc 2, usage), not exercises, and are not cited. 4.0.0_SA_CRO's independent run (94332: `--budget 3` -> rc 3, scanned 30542 of 30552, PARTIAL_OR_BLIND) is a third instrument on the same property.",
        "O6-AC2 at this seat, live plane 03:1xZ: `iam get-role-policy lambda-execution-role FargateTriggerPermissions` -> Action [ecs:RunTask, ecs:DescribeTasks, ecs:TagResource, iam:PassRole], Resource '*', Condition null -- the one role-plane RunTask holder the record names, unconditioned as recorded; `iam list-attached-group-policies AdministratorAccessOpalCapital` -> exactly arn:aws:iam::aws:policy/AdministratorAccess; `sts get-caller-identity` at THIS seat -> arn:aws:iam::313476888478:user/Andrew_Berman -- the worker-subagent answer (a subprocess on this box inherits the box's ambient credentials, which are that user's, which carry */* via the group; there is no worker principal to scope) holds by this seat's own instrument, since this seat is such a subprocess. docs/briefs/cmpaws-iam-census-20260904.json read from the file: generated_utc 2026-09-04T21:18:31Z, api iam:GetAccountAuthorizationDetails, roles 224, managed_policies_resolved false -- the vintage and denominator the record states. The report host is recorded UNREADABLE with its reason (a PRD s.3 design object with no provisioned identity), which is the form the bar requires for a principal that cannot be resolved.",
        "O6-AC3 at this seat: the record names every unresolved plane with its reason and bounds the overhang (137 of 224 roles carry an unresolved managed policy; 35 distinct managed ARNs; by published content at most one further GetLogEvents holder and no further RunTask holder -- labelled INFERRED because get-policy-version was not called; 6 of 7 users unswept; resource-policy and boundary planes not traversed), the two known false-deny traps respected (conditions recorded on every holder; one --resource-arns per call on all 6), and a third trap measured and filed as NFRA_OUTSET-S3 (a wrong-grain resource ARN returns implicitDeny for a */* principal) -- the same mode this seat recorded to memory at 23:2xZ from that row. The census meta flag read at this seat agrees with the record's first UNREADABLE.",
        "O7-AC1 at this seat: `git show HEAD:infra/aws/terraform/globgrph/item2a.tf` :404-409 -- 'GLOBGRPH_CODEHEAT_ENABLED REVERTED (deleted) 2026-07-16 per CTO TO-2 ruling 033933Z ... code_heat now runs on DEV-BOX CADENCE (option a); the freshness twins on its keys are the guard' -- the producer's schedule is NONE by a recorded ruling, as the worker read; `s3api list-objects-v2 warehouse/code_heat/` -> 2 objects, repo=ajb_workspace 1,151,262 B and repo=portal 50,657 B, both LastModified 2026-07-16T03:40:4xZ -- the last write, 50.7 days before the worker's read; `events describe-rule opal-globgrph-derive-runner-nightly` -> cron(0 2 * * ? *) ENABLED (the graph side's cadence); `events list-rules --query length(Rules)` printed 100 then 42 -- 142 rules, the worker's denominator, reached only by summing the per-page lengths (the paginated length() trap the estate already names).",
        "O7-AC2 at this seat: `glue get-table --database-name globgrph --name code_heat` -> Owner None, Location s3://opal-313476888478-globgrph/warehouse/code_heat/ (a first attempt at database code_heat returned EntityNotFound -- this seat's wrong-object error on the catalog.database.table spelling, corrected before it was cited); the six ownership carriers the record enumerates each read to a result, and the one that reads as an owner on inspection (the Terraform comment) names a DETECTOR, the freshness twins, not an accountable seat. The bar asked for the owner or a plain statement that none exists; the record says it plainly and measures the exposure (Q_CODE_BANDS and Q_CODE_COLDEST at .tools/_trino_fed.py:39-52 join the frozen parquet against a nightly-refreshed graph)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: this row adjudicates no item and opens nothing; its content is the five grades below and the two findings that ride with them.",
    "grades": [
      {
        "criterion": "O1-AC6",
        "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-1.rule-t-budget-across-comp-heat.proof_of_spec.json@747955f8d9",
        "verdict": "PASS",
        "reason": "The bar: for any subcommand whose rc carries a verdict, the rc at BUDGET REACHED is a non-clean value distinct from both the clean and the failing verdict, carrying PARTIAL_OR_BLIND in the tool's own voice, recorded side by side with a clean run. Met on the two verdict-bearing subcommands: freshness measured at this seat (cut rc 3 with 'ANSWER-STATE: PARTIAL_OR_BLIND' against clean rc 0, and distinct from its content verdicts 1/2) and compare per the record (0/3). drift, score and federated never carried a verdict in their rc and fall under the form's default clause, as the worker read without grading. FINDING, carried to the analysis and not into this verdict because the criterion as cut does not reach it: federated at BUDGET REACHED refuses before dispatch and exits 0 -- the refusal is in the tool's voice but a caller reading the exit code cannot tell 'refused to dispatch' from 'dispatched and answered', which is the estate's false-clean class (a tool that did nothing and reported OK). The PRD's Rule T is served by making that refusal rc 3, or any non-clean value, at the recut."
      },
      {
        "criterion": "O6-AC2",
        "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-6.federated-transport-caller-contract-iam.proof_of_spec.json@9f984f7314",
        "verdict": "PASS",
        "reason": "The bar: the holders MEASURED with the applied-plane read and its vintage, denominators printed, and the answer to whether a worker subagent and the report host can call the transport. The record gives the census vintage (21:18:31Z, 224 roles, unresolved managed policies disclosed), the role-plane holders by wildcard-aware match with each grant's condition, the user plane read live because the census enumerates no users, simulate calls one ARN each with a firing negative and positive control, and the two answers: a worker subagent can call it because it inherits the box's ambient admin credentials and there is no worker principal to scope; the report host is UNREADABLE because it does not yet exist. Re-read at this seat with different calls (get-role-policy, list-attached-group-policies, sts get-caller-identity, the census file's meta): every checked value agrees. The answer the cell exists to settle is settled and it is a finding for the PRD: the transport's caller today is */*, not a scoped identity."
      },
      {
        "criterion": "O6-AC3",
        "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-6.federated-transport-caller-contract-iam.proof_of_spec.json@9f984f7314",
        "verdict": "PASS",
        "reason": "The bar: any principal not resolved reads UNREADABLE with its reason, never absent or assumed none; the two false-deny traps bind; one --resource-arns per call. The record names three unreadable planes each with its reason and a bound labelled inferred where it is inferred, respects both traps by construction, and found and filed a third trap (the wrong-grain resource ARN) rather than reading its false deny as a negative. That is the bar met in its strongest form: the instrument's own failure mode was discriminated with a */* control, which is the only way this mode is visible."
      },
      {
        "criterion": "O7-AC1",
        "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-7.code-heat-parquet-cadence-and-owner.proof_of_spec.json@238fc60bc2",
        "verdict": "PASS",
        "reason": "The bar: the cadence from the PRODUCER, not the artifact's appearance -- what writes code_heat, on what schedule, when it last ran, with vintage. The record identifies the object first (the parquet the federated join reads, distinct from the Iceberg snap table the existing substrate card is about, so nothing inherits that card's claim), names the producer (code_heat_emit.py, git-history-shaped), reads its schedule as NONE from the Terraform revert of 2026-07-16 with the ruling cited, sweeps the scheduler plane (142 rules, 0 producing it), and dates the last write from the objects. Each of those is re-read at this seat on a different call and agrees: the revert comment at HEAD, both objects last modified 2026-07-16T03:40Z, the nightly derive rule ENABLED on the other side of the join, 142 rules by per-page sum."
      },
      {
        "criterion": "O7-AC2",
        "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-7.code-heat-parquet-cadence-and-owner.proof_of_spec.json@238fc60bc2",
        "verdict": "PASS",
        "reason": "The bar: the owner named, or a plain statement that none exists, an unowned artifact under a daily join being the finding. The record says plainly that no owner exists, after reading six candidate carriers to a result (the Glue Owner field null -- read at this seat as None; no scheduling rule; the nightly derive's carrier deliberately deleted; the substrate card's owner owning the card row of a different object; the revert's actors owning the revert act; the producer header carrying attribution and no operator) and names the one that looks like an owner as a detector. The exposure is measured, not asserted: the join's graph side refreshes nightly (cron(0 2 * * ? *) ENABLED at this seat) while its code side has not moved since 2026-07-16. FINDING for the CTO's analysis: an unowned, uncadenced input to a daily federated join is the outcome this order was cut to surface, and it needs an owner named at the recut or an FWD."
      }
    ],
    "spec_asserts": "Spine v3 L9 / annex section 4a: a judgment criterion is graded by the CVO against the specification that issued it, one entry per criterion on a row of the CVO's, with the CVO's own read beside the worker's record; judgment criteria are graded when their instances are terminal and the slug alone waits for every order.",
    "world_is": "Three of seventeen orders are terminal and their five judgment criteria are graded PASS on this seat's own instruments. Two outcomes the round surfaced are findings rather than failures of a cell -- federated's clean exit on a refused dispatch, and the ownerless code_heat input -- and both go to the CTO's analysis with the slug.",
    "notes": "Rows read this tick and NOT dispositioned here, stated so the census is not lost: S1 (BLOCKING, the O6-AC1 invocation through python -- amended @8d13fc6b80 and re-armed, the order now complete), S2 (comp-find content-mode timeout reads as a clean zero -- recorded to memory), S3 (the third false-deny mode -- recorded to memory), S4 (BLOCKING, the proof stem 16 of 17 faces name short -- the issuer's cut defect, repaired on one face per 94342 and to be repaired on the population at the recut), S5, S6 (4.0.0_SA_CRO: comp-find --budget discloses no budget), W1-S1..W1-S9 (the worker's rows, including W1-S5 on the comp-system gate's precondition, repaired on one face and standing on nine per the issuer's own read). All are dispositioned at the slug with the other 14 orders. The issuer's drain-end read names the round's cost as four cut defects, three repaired on a single face and left standing on the population -- the CLAUDE.md s.2 shared-dependency clause, which the CTO's analysis should read with C-S11's fixed-cost item from NFRA_CLDGRPH. The instrument note for this seat's own reads: `list-rules --query length(Rules)` prints one length PER PAGE (100 then 42); a reader who takes the first number has the page, not the plane."
  }
]
```
