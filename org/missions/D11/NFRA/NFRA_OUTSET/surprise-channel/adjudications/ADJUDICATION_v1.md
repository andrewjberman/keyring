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
mechanical criteria are the proof instances' by output and are not re-graded. At C-S1 no investigation row was dispositioned; the
slug's dispositions are C-S3, C-S4 and C-S5 below, on the completion report.
**Denominator at this write:** 5 rows -- C-S1 (five grades on the first three terminal orders), C-S2 (the thirteen remaining
grades, on the issuer's completion report @a483609584 with 17 of 17 orders terminal), C-S3 (sixteen worker-form items graduated
and closed on in-round acts, W2-S20 by this seat's SPEC amendment), C-S4 (twenty-six items graduated and OPEN with owners
routed), C-S5 (thirty-one records dismissed). Investigation rows without a disposition after this write: 0 of 76.
Remediation rows minted: S1, S4, S8 closed; S2, S3, S6, S13, S14 OPEN.

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

## C-S2 -- the round-1 grade record, second tranche: the thirteen judgment criteria on the fourteen orders terminal since C-S1, each read against its bar with this seat's own instrument; thirteen PASS; the outcomes they serve are the CTO's to grade and several cannot be REALIZED while the served runner predates the round

```json
[
  {
    "id": "NFRA_OUTSET-C-S2",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T14:05Z",
    "one_line": "L9 on the issuer's completion report @a483609584 (17 of 17 orders terminal; 8 of 8 outcomes covered): the GRADE RECORD for the thirteen judgment criteria not graded at C-S1. THIS SEAT'S INSTRUMENTS, 13:3xZ-14:0xZ: the served estate-report runner (s3api head-object 125,857 B dated 2026-08-25T05:36:35Z; downloaded and grepped: 0 of _outset_read / OUTSET_ANSWER_STATE_TO_STATUS / tool_row_cited against 4 / 3 / 7 at HEAD, 159,687 B); the seam's row roster at org/modules/heatmap/outset_seam.py:153 reading paths, rows, uncommitted and nothing nested; `scheduler get-schedule estate-report-0900et` cron(0 9 * * ? *) America/New_York ENABLED targeting the orchestrator; `comp-pipescript --help` 0 hits for --budget against 4 on `deployed --help`; `glue get-tables globgrph` exactly code_heat, obs_findings, tool_activity; docs/architecture/NFRA_OUTSET_COMPOSITION_CONTRACT.md at HEAD with its owner DECLARED-NOT-ACCEPTED; the SPEC's stratum contract read for O11 and amended @ee82c4180d (W2-S20). Thirteen PASS; no FAIL; no NOT_EVALUATED. The record's own honesty is the reason: on eight of the thirteen the worker wrote the limit of its claim beside the pass, and this seat read the limit as part of the grade.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The served-versus-committed read at this seat is the discriminating instrument for O10-AC2, O14-AC2, O17-AC1 and O9-AC2's outcome standing: every cell that edits the runner passed its bar on committed bytes, and the bytes the host runs carry none of it. That is S14's item (REMEDIATION_v1.md), not a failure of any criterion below.",
        "The seam roster read at :153 is the instrument for W2-S21's finding under O14-AC2; the comp-pipescript help reads are the instrument for W3-S10's correction under O12-AC2; the schedule read is the instrument for O10-AC2's limb 2 and W1-S20; the Glue read is the instrument for O4-AC3's first resolution path.",
        "One of this seat's instruments returned a pattern-mismatch zero and is NOT cited: a comp-read enumerate for comp-heat's heatmap imports anchored on `^(from|import)` returned 0 hits; the worker's O15-AC1 import census (instrument B, 3 imports each of heat_map and object_freshness, 0 of the three legs) stands on its own denominator."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: this row adjudicates no item and opens nothing; its content is the thirteen grades below.",
    "grades": [
      {"criterion": "O10-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-10.the-consumption-seam-artifacts.proof_of_spec.json@fe0cee475e", "verdict": "PASS", "reason": "The bar: one real published artifact and the runner reading it, and the PRD s.3 falsifier measured. Limb 1 shows two producers publishing and the runner's own reader rendering an OK stratum with vintage, denominators and rows, beside an absent-artifact control that reads INSTRUMENT_FAILED. Limb 2 measures the falsifier and it does not fire as stated: the 09:00 window exists (read live here), the producers run nightly, the artifacts are fresh. The worker stated the limit plainly: the read is the reader CODE on real bytes, not the runner's ROLE from S3, and W1-S19 shows that role cannot read any seam location -- the publishing step has no owner (S14, W1-S20). PASS on the criterion; the unowned step is the round's central item."},
      {"criterion": "O16-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-16.the-archive-candidate-answer.proof_of_spec.json@b829b5a6ed", "verdict": "PASS", "reason": "The bar: gated on OS-s-15's decision, then one real ranked answer with reasons and denominator. The gate was read at HEAD (OS-s-15 complete: none of the legs a retire candidate; OS-s-16 a wire). The answer is real and bounded: 364 maximal cold subtrees across 4,165 directories rolled up from 30,702 scored paths, 5 assessed and 359 UNASSESSED at --top 5, 0 RECOMMEND_ARCHIVE and 5 HOLD_REFERENCED, each with a reason and a dispute-by line, and the mandatory graph gate named as not run by the tool. Advisory, nothing removed (R-5)."},
      {"criterion": "O17-AC1", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-17.the-sittings-evidence-citation.proof_of_spec.json@ae93134c26", "verdict": "PASS", "reason": "The bar: one day's proposals each citing the tool row behind it at path@vintage. Phase 1 measured the pre-build world (61 of 61 proposals across 7 days, 0 citing a tool row, with a live positive control) and stopped on the cut defect; phase 2 built it: the runner mints <stratum>@<vintage> from the OS-s-11 recipe, requires name AND vintage, runs the two gates in series with the anti-fabrication limb first and byte-unchanged, 10 of 10 arms with two red mutants firing. PASS on the build. The outcome is another matter and the worker said so (W1-S26): the served runner has 0 occurrences of tool_row_cited (read here), so no published day carries it -- FWD-4 stays NOT_EVALUATED until the deploy S14 names."},
      {"criterion": "O4-AC3", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-4.federated-vintage-and-catalog-disclosure.proof_of_spec.json@9ecf665da4", "verdict": "PASS", "reason": "The bar: whether any joined catalog cannot report a build time, and what prints then -- UNREAD with reason, never a default. iceberg.globgrph.graph_nodes cannot: the answer prints build_time=UNREAD claim=absent with the reason (a lexicographic S3 listing that did not complete within the probe ceiling claims no max), and five resolution paths were checked and closed -- the Glue catalog holds exactly code_heat, obs_findings, tool_activity (read here), no version-hint, no last_append pointer, the Nessie pointer in-VPC, the object plane affordable only out of band (183,447 objects, 36.6 s). The value exists once the listing completes; W1-S14 carries the growth condition."},
      {"criterion": "O8-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~1/NFRA_OUTSET.TO-OS-s-8.comp-similar-heat-weighting-consumes.proof_of_spec.json@67472e2975", "verdict": "PASS", "reason": "The bar: load_heat_live quoted before and after at file:line plus one real run with heat numbers, or the declaration. Both quotes are present with lines; the cause was on the exec plane (a Windows subprocess of the shim raised WinError 193, swallowed by _run_json into an empty dict) and the fix resolves the interpreter from the shebang and passes --budget; the real run banded 208 of 1,929 corpus resources from 51,861 heat keys with 6 of 6 candidates citing a comp-heat band. The exec cause is a CLASS (W2-S2), routed."},
      {"criterion": "O11-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/NFRA_OUTSET.TO-OS-s-11.traceability-on-deterministic-lines.proof_of_spec.json@ab481216d7", "verdict": "PASS", "reason": "The bar: take one deterministic row, re-run the tool it names at the vintage it names, show it reproduced; a row that cannot be reproduced IS the finding. One row of stratum C was taken at the pin, its recipe run as printed, and 17 of 17 rows re-derived by a fold written independently of the runner; a negative control (window 90 d to 2 d) produced 107 rows, so the comparison can fail. The reach is stated honestly (W2-S18): 4 of 4 strata carry a recipe, 1 of 4 demonstrated, two untested and two untestable until the seam publishes and the runner can read it. The shape the recipe lives in is now in the SPEC (5c @ee82c4180d)."},
      {"criterion": "O14-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/NFRA_OUTSET.TO-OS-s-14.fedobs-co-evolution-reaches-the-report.proof_of_spec.json@a4fbb68978", "verdict": "PASS", "reason": "The bar: show the signal in the report or state why it does not belong; silence is not acceptable. Both premise halves measured, the real producer run, published and rendered end to end -- and then the worker found and filed that the rows do not survive extraction (W2-S21: 35,752 rows nested at signals.coevolution.rows against a roster of paths/rows/uncommitted at :153, read here), so the report renders a confident zero wearing a healthy answer's clothes, and why three batteries missed it (W2-S22: every fixture is top-level shaped). The criterion is met as a reading act and its most valuable output is the defect; the outcome is not served until the roster is fixed."},
      {"criterion": "O9-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~2/NFRA_OUTSET.TO-OS-s-9.report-cochange-from-the-tool.proof_of_spec.json@848df59328", "verdict": "PASS", "reason": "The bar: :1308 and :1996 quoted before and after at file:line, and if the host copy stays, the declaration of which tool it stands in for. Both quoted, with the drift correction the record owed (W2-S16: :1996 is a filler line; the wiring moved to :2149 then :2221) rather than a silent substitution; the seam-read path added with prefix and loader parameters; COCHANGE_STANDS_IN_FOR declared in FWD-6's words. W2-S14's finding stands beside it: there is no tool to retire the host copy to, because comp-cochange answers agent co-movement, a different axis under the same word."},
      {"criterion": "O12-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~3/NFRA_OUTSET.TO-OS-s-12.working-order-census.proof_of_spec.json@74a16082ad", "verdict": "PASS", "reason": "The bar: run the census over the brief's tools and show the table with its denominator. 9 of 9 censused, one row each, column grains stated (a real answer probe, never --help; WORKING requires a non-trivial body; NO-ANSWER-DISCLOSED is the confident-zero shape). One row is KNOWN FALSE and the record says so twice (W3-S9 then W3-S10, the worker correcting itself): comp-pipescript read FAILED because the probe put --budget at the top level, where the tool does not accept it -- it accepts it on the deployed subcommand (0 against 4 hits at this seat) and answers there with a real MATCH row. The criterion is met; the census artifact carries a false row that its own author corrected on the record and that the delivered file still prints -- routed (W3-S10) rather than inherited."},
      {"criterion": "O13-AC1", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~3/NFRA_OUTSET.TO-OS-s-13.the-composition-contract.proof_of_spec.json@d3b1004fa2", "verdict": "PASS", "reason": "The bar: one home, one named owner, covering LOCAL->GIT, GIT->DEPLOY, co-evolution and the pairwise verdict, with comp-heat's header quoted. The document exists at HEAD (read here) with its owner recorded as 1.0.0_SA_CTO DECLARED-NOT-ACCEPTED and the basis for that claim status stated -- a worker cannot confer ownership; the header quoted at .tools/comp-heat:34-36; all four hops measured live at the pin with keys, domains and bounds, and the domain gap named (the GIT->DEPLOY hop covers 554 of 30,659 files; W3-S11)."},
      {"criterion": "O13-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~3/NFRA_OUTSET.TO-OS-s-13.the-composition-contract.proof_of_spec.json@d3b1004fa2", "verdict": "PASS", "reason": "The bar: express 'converging AND hot AND undeployed' from the contract without a new tool, or record that it cannot be. It can: comp-heat compare, comp-heat freshness and comp-pipescript deployed on one shared key, ~10.5 s, every call bounded, evaluating FALSE on the chosen path (DIVERGING, COLD, MATCH) -- a decidable answer on every limb, with the domain intersection (1.8%) and a domain-boundary negative control (rc=2 REFUSED) recorded."},
      {"criterion": "O15-AC1", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~3/NFRA_OUTSET.TO-OS-s-15.reachability-of-the-heat-engine-legs.proof_of_spec.json@afa659557d", "verdict": "PASS", "reason": "The bar: for each of the three legs, REACHABLE-FROM-CLI or RETIRE-CANDIDATE, with the line the CLI would call and the measured fact that the CLI reaches O1 only. The imports are measured on two instruments over 5,624 parsed .py files plus 42 shebang scripts (the CLI imports heat_map and object_freshness three times each and none of the legs); the decision per leg is reasoned with an exercised falsifier (O2's maximal-cold-subtree capability is not duplicated by the CLI's substitute: 1 root against 0 on the same synthetic scores). The worker also found the vocabulary not MECE over the world it measured (W3-S2) and answered outside it rather than forcing a wrong value -- the right act on a form defect."},
      {"criterion": "O15-AC2", "instance": "org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.9.0_WK_NFRA_OUTSET~3/NFRA_OUTSET.TO-OS-s-15.reachability-of-the-heat-engine-legs.proof_of_spec.json@afa659557d", "verdict": "PASS", "reason": "The bar: R-5 (never auto-delete) restated for any leg touching removal, and a leg that cannot honour it named a retire candidate. R-5 is quoted verbatim from the PRD at its line, all three legs and the caller are scanned, every `replace` hit is resolved individually to str.replace, and the count of filesystem-removal calls across the four files is zero -- the property is structural. No leg fails R-5."}
    ],
    "spec_asserts": "Spine v3 L9 / annex section 4a: a judgment criterion is graded by the CVO against the specification that issued it, with the CVO's own read beside the worker's record; L10 grades outcomes, and a cell's PASS does not make an outcome REALIZED (the CTO's ETFS_GUARDRAIL correction of this seat, applied here from the start).",
    "world_is": "All eighteen judgment criteria of round 1 are graded PASS (five at C-S1, thirteen here). The outcomes stand where the completion report placed them: FWD-6 (the composition contract) is APPLIED on a written artifact; FWD-1, FWD-5 and FWD-8 have live exercises the CTO can weigh; FWD-2, FWD-3, FWD-4 and FWD-7 cannot be REALIZED on a served day while the report host runs the 2026-08-25 runner, whatever the cells passed.",
    "notes": "Findings for the CTO's analysis, none a failure of a cell: the unowned deploy and publishing steps (S14, W1-S19, W1-S20, W2-S15); the seam's row roster (W2-S21, W2-S22); the census's false row (W3-S10); the exec class (W2-S2, W3-S7); the router running lexical-only on every call (W2-S11); the schema's missing deployed_state value (W1-S21); the SPEC caught up with the code (W2-S20 @ee82c4180d). Instrument notes for this seat's own reads: the published day's proposals live under the report JSON's `ai` object, not a top-level key, so this seat's first count of tool-row citations read 0 proposals and is not cited; the served runner lacking tool_row_cited is the load-bearing read instead."
  }
]
```

## C-S3 -- adjudicates the items graduated and CLOSED on in-round acts (the issuer's amendments, the workers' fixes, this seat's SPEC amendment): the seat-form S1, S4, S8 (clocks in ../remediations/REMEDIATION_v1.md), W1-S1, W1-S6, W1-S8, W1-S2 (limbs 1-2; limb 3 open at C-S4), W3-S4, W3-S1, W3-S5, W3-S6, W2-S3, W2-S4, W2-S6, W2-S7, W2-S8, W1-S24, W2-S12, W2-S20

```json
[
  {
    "id": "NFRA_OUTSET-C-S3",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T14:10Z",
    "one_line": "L9: ADJUDICATES nineteen items -- GRADUATED, remedied inside the round. The three seat-form items carry their clocks in ../remediations/REMEDIATION_v1.md: S1 (O6-AC1 amended @8d13fc6b80, the order complete), S4 (the proof stem on sixteen faces; 17 of 17 orders flipped through the gate), S8 (arm F's two flake mechanisms fixed by W1-S12 and W1-S18, S9's ACK corrected by S11). The sixteen worker-form items carry their clocks here (REMEDIATED, DISARMED, closed as of the commits named) because a W<n>-keyed remediation row is not one the CVO mints. W1-S1, W1-S6, W1-S8 (O1-AC2's cache-flaky expect): root cause fixed by the worker -- a path-scoped git call -- per its disarm record W1-S10, the issuer's --budget 60 amendment @ddff1d8eeb standing; the battery 21 of 21. W1-S2 (the federated budget race): limbs 1 and 2 closed on W1-S15's measurement (--budget 199.9 refuses and 200.1 dispatches, a nominal floor no elapsed clock could tell apart; the caller's wait bounded); limb 3, the remote task's own duration, stays open at C-S4. W3-S4 (the 'cold SUBTREES' label): both halves closed per the disarm record W1-S22. W3-S1, W3-S5, W3-S6 (OS-s-15's issued_to/paths mismatch and the lane gate's refusal): amended @b630052d6a, the order complete. W2-S3, W2-S4 (OS-s-8's issued_to/spawn-serial mismatch, the mechanical half BLOCKING): amended; the order complete and drained. W2-S6 (an unblock instruction that granted nothing until the amendment landed on the branch): measured 0 of 4 then 5 of 5; the amendment landed; the round is closed and the instruction is superseded by the measurement, carried to the analysis as the lesson. W2-S7, W2-S8 (O3-AC3's invocation could not produce its expect; two limbs): the order OS-s-3 complete under the issuer's amendment; W2-S13's evidence correction read. W1-S24 (BLOCKING on O17-AC1's build limb, no repo surface granted for a build verb): the issuer accepted its cut defect and amended <paths> @ed5c4e2b5b; phase 2 built and passed. W2-S12 (the comp-system gate fails open on a genuine source change): the worker regenerated 06_current_state worktree-locally within its grant and landed the pair; the tool hazard itself is W1-S11's at C-S4. W2-S20 (the SPEC's stratum shape one field behind the code, disarm_owner this seat): CLOSED @ee82c4180d (the commit before this one) -- SPEC_kimi_call_subdivision_and_insight_strata_20260805.md section 5c adds the optional additive `reproduce` key, its claim vocabulary and its vintage rule; code and specification agree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Each item's remedy is on the record in the row that closed it (W1-S10, W1-S15, W1-S22, S5, W2-S13) or in the order's completion through the gate (17 of 17 `<status>complete` at HEAD, read here); this seat re-read the artifact where one existed: the amended faces at HEAD, the SPEC at HEAD before and after this commit, the 06_current_state pair in the drained tree.",
        "W1-S2 is graduated on two limbs and left open on the third deliberately: the same row, two states, and the split is the record's own (W1-S15 'CLOSED BY LIMB, NOT WHOLESALE'); C-S4 carries limb 3 with its owner.",
        "W2-S20's closure is this seat's own act, committed @ee82c4180d: the SPEC's section 5c text and the runner's `_stratum` at :1248 and :1270 now describe one shape."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OUTSET-S1", "NFRA_OUTSET-S4", "NFRA_OUTSET-S8",
      "NFRA_OUTSET-W1-S1", "NFRA_OUTSET-W1-S6", "NFRA_OUTSET-W1-S8", "NFRA_OUTSET-W1-S2", "NFRA_OUTSET-W3-S4",
      "NFRA_OUTSET-W3-S1", "NFRA_OUTSET-W3-S5", "NFRA_OUTSET-W3-S6", "NFRA_OUTSET-W2-S3", "NFRA_OUTSET-W2-S4",
      "NFRA_OUTSET-W2-S6", "NFRA_OUTSET-W2-S7", "NFRA_OUTSET-W2-S8", "NFRA_OUTSET-W1-S24", "NFRA_OUTSET-W2-S12",
      "NFRA_OUTSET-W2-S20"
    ],
    "spec_asserts": "Annex sections 3 and 5: an ARMED hazard disarms via the row's disarm_owner; a graduated item remedied inside the round carries REMEDIATED and DISARMED with the exercised remedy cited.",
    "world_is": "Sixteen hazards this round surfaced were remedied before it closed; each is verified against the world or the record at this seat. None asks anything of the next round except the lessons the analysis carries.",
    "notes": "The four seat-form items closed in the same way (S1, S4, S8, and the ACK records) carry their clocks in ../remediations/REMEDIATION_v1.md."
  }
]
```

## C-S4 -- adjudicates the items graduated and OPEN, each outside the round's write surface, with owners named for the CTO's routing at L10: S14 with W1-S25 and W1-S26 (the unowned deploy), W1-S19, W1-S20 and W2-S15 (the unowned publishing step), W2-S21 and W2-S22 (the seam's roster), W1-S11 and W2-S5 (the comp-system gate), W2-S2 and W3-S7 (the Windows exec class), W2-S11 (the degraded router), W1-S21 (the schema), W1-S13, W1-S14, W1-S17, W1-S23, W2-S10, W2-S14, W2-S24, W3-S10, W1-S2 limb 3, and the seat-form S2, S3, S6, S13

```json
[
  {
    "id": "NFRA_OUTSET-C-S4",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T14:15Z",
    "one_line": "L9: ADJUDICATES twenty-six items -- GRADUATED, remedy OPEN, none within the round's write surface, routed by name in the slug. THE CENTRAL ONE, S14 with W1-S25 and W1-S26 (REMEDIATION_v1.md S14, owner 1.0.0_SA_CTO): the report host runs a 2026-08-25 runner that carries none of this round's runner edits, because the single S3 upload that deploys it belongs to no cell -- read at this seat on the served object and HEAD. THE SAME SHAPE ONE HOP IN, W1-S19, W1-S20, W2-S15 (owner 1.0.0_SA_CTO with S14): the runner's role holds no grant on any seam prefix, nothing publishes to the seam, and the PRD s.3 falsifier as stated does not fire -- the publishing step has no owner. THE SEAM'S ROSTER, W2-S21, W2-S22 (owner: the holder of org/modules/heatmap/outset_seam.py, routed by the CTO): rows=doc.get('paths') or doc.get('rows') or doc.get('uncommitted') at :153 (read here) drops 35,752 nested rows and every fixture is top-level shaped so no battery can see it. THE COMMIT GATE, W1-S11, W2-S5 (owner 1.0.0_SA_CTO): the comp-system stage refuses uncommitted source and resolves the main workspace's copy through PATH, so a linked-worktree worker cannot clear it. THE EXEC CLASS, W2-S2, W3-S7 (owner 0.8.0_AE_CloudComp with the CTO): a python subprocess of a shim or a bare `bash` on this host resolves to WinError 193 or the WSL stub, a false failure with a clean denominator. THE ROUTER, W2-S11 (owner 1.0.0_SA_CTO, comp-tool registry): comp-which falls back to lexical on every call on a fail-closed tokenizer hash mismatch, so every routing measurement on the fabric is on the lexical path. THE SCHEMA, W1-S21 (owner 1.0.0_SA_CTO): deployed_state has no value for a deploy-scope artifact committed and deliberately not deployed. AND: W1-S13 (a worker ran the main tree's code via the `&` backgrounding trap; owner 2.0.0_SA_COO, the worker harness), W1-S14 (graph_nodes' 20,374 unexpired metadata files make its build time unaffordable in-band; the globgrph lane via the CTO), W1-S17 (federated --sql unrestricted against a READ-ONLY docstring; 0.8.0_AE_CloudComp), W1-S23 (O3's substring match over-holds; 0.8.0_AE_CloudComp), W2-S10 (running a COPY of a comp-tool fail-softs on __file__; doctrine, 1.0.0_SA_CTO), W2-S14 (no tool to retire _stratum_cochange to; the runner's holder), W2-S24 (comp-fedobs takes no --budget; 0.5.0_AE_OpalETL via the CTO), W3-S10 (the delivered census prints a false FAILED for comp-pipescript; the census's holder via the CTO), W1-S2 limb 3 (the remote task's own duration needs .tools/_trino_fed.py; 0.8.0_AE_CloudComp); the seat-form S2, S6 (comp-find, 0.8.0_AE_CloudComp), S3 (the IAM trap for the doctrine, 1.0.0_SA_CTO), S13 (the decomposition's false manifest claim, 2.0.0_SA_COO at the recut) in REMEDIATION_v1.md.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO (routes at L10 to the lanes named per item; owns S3, S14, W1-S11/W2-S5, W2-S11, W1-S21, W2-S10 directly)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "This seat's reads behind the routing: the served runner's bytes and vocabulary against HEAD (S14 group); the seam roster line at HEAD (W2-S21); comp-pipescript's --budget placement (W3-S10); the schedule and the runner's role scope as W1-S19 recorded it (the IAM read is the worker's, resource-scoped to four keys on opal-estate-report and nothing on globgrph); the Glue catalog and the out-of-band listing sizes as recorded (W1-S14).",
        "Each remaining item's finding is the worker's or issuer's own measurement at HEAD, read here in full and not restated: the rows name their instrument, their denominator and what they deliberately did not do; every one is outside the order's <paths> that found it, which is why it is open and routed rather than fixed.",
        "Owners are named at the grain the estate can act on: a seat serial where the surface has one (comp-tools to 0.8.0_AE_CloudComp; comp-fedobs to 0.5.0_AE_OpalETL per its header; the gates, schema, doctrine and the deploy/publishing steps to 1.0.0_SA_CTO), and the CTO's L10 routing where the row could not establish one."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": [
      "NFRA_OUTSET-S14", "NFRA_OUTSET-W1-S25", "NFRA_OUTSET-W1-S26", "NFRA_OUTSET-W1-S19", "NFRA_OUTSET-W1-S20",
      "NFRA_OUTSET-W2-S15", "NFRA_OUTSET-W2-S21", "NFRA_OUTSET-W2-S22", "NFRA_OUTSET-W1-S11", "NFRA_OUTSET-W2-S5",
      "NFRA_OUTSET-W2-S2", "NFRA_OUTSET-W3-S7", "NFRA_OUTSET-W2-S11", "NFRA_OUTSET-W1-S21", "NFRA_OUTSET-W1-S13",
      "NFRA_OUTSET-W1-S14", "NFRA_OUTSET-W1-S17", "NFRA_OUTSET-W1-S23", "NFRA_OUTSET-W2-S10", "NFRA_OUTSET-W2-S14",
      "NFRA_OUTSET-W2-S24", "NFRA_OUTSET-W3-S10", "NFRA_OUTSET-S2", "NFRA_OUTSET-S3", "NFRA_OUTSET-S6", "NFRA_OUTSET-S13"
    ],
    "spec_asserts": "Annex section 5: a graduated item names its remedy and its owner; the CTO routes every round from the slug; spine v3 L10: an outcome no cell served is a PRD addendum -- the deploy and publishing steps are candidates for exactly that.",
    "world_is": "Twenty-six hazards this round found live outside its write surface, two of them the same uncovered-member shape one hop apart (the deploy nobody owns; the publish nobody owns), and the rest instrument, gate, schema and tooling defects the estate's other lanes hold. The seat-form five carry their clocks in REMEDIATION_v1.md; the worker-form twenty-one carry them here, OPEN, until the lanes act.",
    "notes": "For the CTO's L10 read, stated once: a PRD that costs a publishing step and a deploy step without placing them lets a project pass every criterion it was cut for while the thing the estate reads is unchanged; that is the addendum this round earns if the analysis agrees. The instrument traps among these (W2-S2, W3-S7, W2-S10, S2, S3, S6) are in this seat's memory where they fire unprompted; the doctrine entries are the CTO's."
  }
]
```

## C-S5 -- adjudicates the records DISMISSED_WITH_REASON: the ACKs, corrections, stops, disclosures and INERT observations already resolved on the record

```json
[
  {
    "id": "NFRA_OUTSET-C-S5",
    "project": "NFRA_OUTSET",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-05T14:20Z",
    "one_line": "L9: ADJUDICATES thirty-one rows -- DISMISSED_WITH_REASON, each a record rather than an item. The ACKs and corrections: S5 (S1/S4 disarmed), S9 with S11 (the arm F disarm acknowledged, then corrected as overclaimed -- S8's closure rests on both mechanisms, REMEDIATION_v1.md), S12, W1-S10 (the disarm record for W1-S1/S6/S8), W1-S12 with W1-S18 (the de-flake and its own correction), W1-S15 (W1-S2's limb record), W1-S22 (W3-S4's disarm record), W1-S27 (W1-S25's instrument correction), W2-S13 (W2-S7's evidence correction), W2-S16 (a line-citation drift, quoted correctly at O9-AC2), W2-S17 (a self-reported first attempt), W2-S19 with W2-S23 (cross-order coupling on the shared runner file, then the population corrected). The stops and disclosures: S7 (the half-provisioned worktree), W1-S4 (the instance filename), W1-S5 (the comp-system gate's first block, generalised by W1-S11), W1-S7 (the flip the worker declined), W1-S9 (its own correction), W1-S16 (a title asserting what the grant could not deliver, with the hazard carried on W1-S15), W2-S1 (three stacked causes under one named defect), W2-S9 (a cell whose premise and criteria measured different questions). The INERT observations: W1-S3 (10 of 30,276 paths omitted by the engine's git walk, advisory-only consequence), W3-S2 (a two-valued vocabulary not MECE over the measured world -- a form finding for the recut), W3-S3 (O3's hardcoded subprocess timeouts, named for the wire), W3-S8 (a per-call timeout does not bound a launcher grandchild -- in memory), W3-S9 (the census row W3-S10 corrects), W3-S11 (the header's domain gap, closed in the contract document), S10 (dependency width against contention width -- a method lesson for L5, not a decomposition defect), W2-S18 (the reach of the traceability claim -- carried in O11-AC2's grade so it cannot be over-read).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Each row read at HEAD in full at this seat; where a record's substance is a world state this seat re-read it (the served runner behind W1-S27; the comp-pipescript help behind W3-S9; the SPEC behind W2-S16's neighbour O9-AC2).",
        "The corrections are kept beside the rows they correct rather than folded into them: S9 and S11 together, W1-S12 and W1-S18 together, W3-S9 and W3-S10 across two rows -- a correction is a census too, and the census must show it."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Records of acts, corrections, stops, disclosures and INERT observations already resolved on the record or carried by an item elsewhere; none names a hazard that outlives the round on its own.",
    "adjudicates": [
      "NFRA_OUTSET-S5", "NFRA_OUTSET-S7", "NFRA_OUTSET-S9", "NFRA_OUTSET-S10", "NFRA_OUTSET-S11", "NFRA_OUTSET-S12",
      "NFRA_OUTSET-W1-S3", "NFRA_OUTSET-W1-S4", "NFRA_OUTSET-W1-S5", "NFRA_OUTSET-W1-S7", "NFRA_OUTSET-W1-S9",
      "NFRA_OUTSET-W1-S10", "NFRA_OUTSET-W1-S12", "NFRA_OUTSET-W1-S15", "NFRA_OUTSET-W1-S16", "NFRA_OUTSET-W1-S18",
      "NFRA_OUTSET-W1-S22", "NFRA_OUTSET-W1-S27", "NFRA_OUTSET-W2-S1", "NFRA_OUTSET-W2-S9", "NFRA_OUTSET-W2-S13",
      "NFRA_OUTSET-W2-S16", "NFRA_OUTSET-W2-S17", "NFRA_OUTSET-W2-S18", "NFRA_OUTSET-W2-S19", "NFRA_OUTSET-W2-S23",
      "NFRA_OUTSET-W3-S2", "NFRA_OUTSET-W3-S3", "NFRA_OUTSET-W3-S8", "NFRA_OUTSET-W3-S9", "NFRA_OUTSET-W3-S11"
    ],
    "spec_asserts": "Spine v3.2 L9: the census counts the investigation document's rows as items and reads the adjudication document for their dispositions, so every row needs one even when it names no hazard.",
    "world_is": "Thirty-one rows describe acts and states already resolved on the record; with C-S3 and C-S4 (and S1, S4, S8, S14 on the remediation plane), 76 of 76 rows are dispositioned and the L10 precondition is met on the investigation plane.",
    "notes": "For the analysis from these records: the round's corrections outnumber its defects in a good way -- five workers and the issuer corrected their own rows on the record eleven times, and every correction named what its falsifier could not have caught."
  }
]
```
