# TO IRPT_BCKEND.TO-IB-rtj-2 -- THE L4 BOUNDED TEST PRINCIPAL: CREATED, EXERCISED, DESTROYED: round 9's `IB-rti-3` found neither `opal-data-inflection` nor `opal-data-cottonwood` has an existing, non-exempt, assumable principal whose IAM already grants `s3:ListBucket` reaching the bucket -- "cannot discriminate without a new grant" (row `IRPT_BCKEND-W11-S1`). The CTO ruled (msg 99312, CALL 1) that this test is drivable on demand and must not sit UNEXERCISED (Rule 27); it is APPROVED as a bounded, self-deleting round-10 cell, never a standing grant.

<to_id>IRPT_BCKEND.TO-IB-rtj-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-22 (round 10, chain B, decomp v0.14 s.R10.1) in the ONE round-10 issuance</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 10 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 (no addendum) | **Decomp cell:** `IB-rtj-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.14, s.R10.1) | **outcome_ref:** FWD-11 | **Row:** `IRPT_BCKEND-W11-S1` | **Ruling (READ IN FULL, this face restates its shape but is not a substitute):** `1.0.0_SA_CTO` msg 99312 CALL 1, 2026-09-21 ~23:03Z

---

## IDENTITY

- **Serial:** `0.7.0_AE_CloudOps~V` (existing live Tier-2 seat; this order does NOT seat a new lane, per LD-0529 -- a Tier-2 seat hears an act only as a task order). Work in your own home tree; per Rule 14b, isolate anything bigger than a one-file edit in your own linked worktree (`git worktree add ../<slot> -b <branch>`) while other seats are live, and merge back with `.tools/safe-merge.sh` when done.
- **Commit:** `bash .tools/safe-commit.sh --author "0.7.0_AE_CloudOps~V <0.7.0_AE_CloudOps~V@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by a non-shell writer. Capture output to a file; never `| tail`; verify by `git log`.
- Python `py -3.12`; Terraform via `bash .tools/safe-apply.sh` (never bare `terraform apply`); AWS via `.tools/aws`.

## THE CELL

- **(a) THE ROLE.** One IAM role, minted through Terraform (`safe-apply`) -- never hand-created in the console. Its name must NOT match `role/*-inf-*` or `role/*-cot-*` (the two fence exemption patterns); print the chosen name beside BOTH live `ArnNotLike` lists (`opal-data-inflection`'s and `opal-data-cottonwood`'s policies, read fresh) to prove it is genuinely non-exempt. Its ONLY grant, its entire inline/attached policy: `s3:ListBucket` on `opal-data-inflection`, `opal-data-cottonwood`, and ONE unfenced control bucket you choose and name (any bucket this role can legitimately read that carries no per-firm Deny fence). No other action, no other resource, no wildcard beyond what `ListBucket` requires.
- **(b) LEDGER FIRST.** Open the change-management ledger entry BEFORE the Terraform apply (per NEVER-2); this is an S1-stakes act (spawn/apply class). State the role's exact name, its exact policy JSON, and the destroy-and-verify step it will end with, in the entry, before you apply anything.
- **(c) SIGN-OFF BEFORE THE APPLY -- two halves, CTO + CRO** (the CloudOps~V precedent: "~V does work, CRO and CTO sign off"). Write the packet: the role's name, its exact policy, the two target buckets + the one control, the destroy-and-verify step. Send it to `1.0.0_SA_CTO` and `4.0.0_SA_CRO` (or a live COO holding CRO's round per standing doctrine, if CRO is not online). **STOP here until BOTH halves are at HEAD naming this packet.** This is the ONE exception to "no grant is widened" this round (CTO msg 99299/99312); it does not authorize any other principal, ever.
- **(d) APPLY, THEN THE POSITIVE ARM.** With both halves at HEAD: `safe-apply.sh` the role. Assume it (or otherwise exercise its exact grant). POSITIVE ARM: `s3:ListBucket` on the control bucket succeeds -- print the wire result. This proves the role, its assumption and the instrument all work before the negative arms are read as meaningful.
- **(e) THE NEGATIVE ARMS, ATTRIBUTED.** `s3:ListBucket` on `opal-data-inflection` and on `opal-data-cottonwood`, each under the SAME role. Both must be DENIED, and the denial must be ATTRIBUTED to the bucket's resource policy explicit Deny -- read the CloudTrail event or the S3 API's own error context (never just the bare error code, which cannot distinguish "denied by this policy" from "denied because nothing grants it"). Print the attribution evidence for each bucket, denominator = 2 of 2 buckets.
- **(f) DESTROY, THEN VERIFY.** In the SAME session, `safe-apply.sh` DESTROY the role. Verify with `aws iam get-role --role-name <name>`: the call must return `NoSuchEntity`. Print the exact CLI output. Close the ledger entry only after this verification prints.

## DELIVERABLE
The ledger entry (opened before, closed after); the signed packet + both halves' file paths; the Terraform plan/apply/destroy output; the positive-arm and negative-arm wire evidence (2 of 2 buckets, attributed); the `NoSuchEntity` verification; the result.md; the proof instance.

## BOUNDS
- **No grant beyond exactly `s3:ListBucket` on the three named buckets. No other principal touched. No standing role -- it is destroyed in this same session, verified, before this order can flip `complete`.**
- No new bucket, no bucket-policy edit, no exemption-list edit. This cell reads the fence; it does not change it.
- The forward-looking-criterion bar; R-40 (content hash per artifact read AT the event); the LEDGER opened before the act; the identity bar (the negative arms run under the DEPLOYED role, not a simulated stub).
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md` (tree project path: `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`), id `IRPT_BCKEND-W15-S<k>` starting at 1 (or continuing above the highest at your HEAD), append INSIDE the fence, PREVAILING EOL, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED; then keep working.

<expected_criteria>R102-AC1, R102-AC2</expected_criteria>
<criterion id="R102-AC1" cell_refs="IB-rtj-2"><invocation>see result.md: role name, policy, CloudTrail-attributed negative arms on 2 of 2 buckets, positive arm on the control, NoSuchEntity verification</invocation><expect>IBR102-BOUNDED-PRINCIPAL-DISCRIMINATES-AND-IS-DESTROYED</expect></criterion>
**`R102-AC1` -- PASSES BY OUTPUT:** the role's exact policy is printed and is ListBucket-only on exactly 3 buckets; the role's name is printed beside both live `ArnNotLike` lists and does not match either; the positive arm on the control bucket succeeds; BOTH fenced buckets deny, each attributed to the resource-policy explicit Deny with cited evidence (CloudTrail event id or the S3 error context, not the bare code); the role is destroyed and `get-role` returns `NoSuchEntity`, printed verbatim. The token prints only when every element holds.

<criterion id="IRPT_BCKEND-L4-SIGNOFF" cell_refs="IB-rtj-2" judgment="true"/>
**Never-widen sign-off gate (not a graded criterion, a hard STOP):** arm (d) does not run until BOTH the CTO's and the CRO's (or a live-COO-in-CRO's-stead) halves are committed at HEAD naming this packet's exact role name and policy.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtj-2.the-l4-bounded-test-principal-created-exercised-destroyed.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/investor-reporting/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.14, cell `IB-rtj-2` (s.R10.1).
<owned_cells>IB-rtj-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- this cell's WHOLE PURPOSE is to mint and exercise a new, bounded, self-deleting principal under the sign-off gate in arm (c); no grant is assumed or read at cut time.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R102-AC1. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/IRPT_BCKEND.TO-IB-rtj-2.the-l4-bounded-test-principal-created-exercised-destroyed.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator`, `expect` from this face, R-40 content hashes pinned to the commit carrying each artifact. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R102-AC1 PASS-by-output AND the destroy-verify printed, then flip `<status>` to `complete`. A STOP (either half missing, or B1/B2 cannot discriminate for a reason not anticipated here) leaves the order `pending` with the BLOCKING row and is the final report.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, naming the criterion's deciding output, the destroy-verification line verbatim, proof-of-spec-check rc, every row id filed with its class, and the L4 ledger leg's final state (this closes leg L4 of `20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md` if the discrimination succeeds -- say so explicitly, or say why not).
</content>
