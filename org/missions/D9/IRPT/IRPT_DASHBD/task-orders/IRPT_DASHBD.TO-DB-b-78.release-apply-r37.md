# TO IRPT_DASHBD.TO-DB-b-78 -- E1: the R37 activity-and-lot release APPLY under both halves -- 18 pins and the root restored, plan exactly 0/3/0, one targeted safe-apply, a population dry_run under the 85% line gating the first fire, A1 to A7

<to_id>IRPT_DASHBD.TO-DB-b-78</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~55</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>38</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's round-37 ADDENDUM 6 @fb5579ddfc (on ADJUDICATION_v22 @153e101791), enrichment item E1 | **Decomp cell:** `DB-b-78` (decomposition section 40) | **outcome_ref:** FWD-4 | **depends_on:** both halves (given); DB-b-73/74 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-55`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~55/`.

**The cell (`DB-b-78`).** The release is signed on both halves:
- the packet, sha256 `848dd8640688c28cb62ffab109c4d55ea4e5348bc5286400a824d8e1405fd40b`, at `C:/dev/wk-irpt-dashbd-55/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~51/NEVER_WIDEN_PACKET_ACTIVITY_LOT_RELEASE_R37.md`;
- the COO half, `C:/dev/wk-irpt-dashbd-55/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_ACTIVITY_LOT_RELEASE_R37_COO_HALF.md`;
- the CTO half, `C:/dev/wk-irpt-dashbd-55/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_ACTIVITY_LOT_RELEASE_R37_CTO_HALF.md`.

Read all three whole: the halves' conditions bind you. The packet's "Preconditions", "The act", "Rollback, per key", "BRANCH A", "BRANCH B" and
"After-read" are your procedure. Round 36's attempt (DB-b-70) was rolled back for stale pins and an unsized lots stage, and both are repaired.
Record everything in `R37_APPLY_RECORD.json` in your folder.

1. **Ledger first, pinned.** Open a ledger with `python .tools/deploy_ledger.py` (read its `--help`), with legs P1 (pins, root, plan), D1 (apply),
   V1 (readback and dry_run) and A1 (the first fire). Its text states the pin of what it signed: the packet sha256 `848dd864...fd40b` and the
   artifact sha256 you build (MSTR msg 2680). Record `ledger_entry`.
2. **Re-read the anchor.** Live CodeSha256 must be `Mex71Y5gk9RYE9q885knj3Ph12xV2Y9eVqMl3uJ1Z44=` (the rollback state). Otherwise STOP and
   file a row.
3. **Precondition 1: the 18 pins.** Set the source-map entry `irpt-49f-reporting-gold-lambda` to the packet's pins table, with each
   `git show <pin>:<path> | sha256sum` re-read now. If `account_activity_lots.py`'s pin `c0afa6f55e` is not on `origin/CLOUD` by that commit
   id, re-pin it to the commit that carries those bytes there. Rebuild and upload with `infra/aws/lambda/ci/build-and-upload.sh`, then commit
   the source map.
4. **Precondition 2: the root.** Restore `iam.tf`, `locals.tf` and `lambda.tf` under `infra/aws/terraform/investor-reporting/reporting-gold/`
   to their `efeb21df71` bytes. Verify each sha256 against the packet's table, then commit.
5. **Precondition 3: the plan.** Run the packet's targeted plan. It must read exactly `0 to add, 3 to change, 0 to destroy`; anything else is a
   STOP and a row. Use the main checkout's `terraform.exe` and the local provider mirror, with no download (row D2-W47-S3).
6. **The act.** Run one `.tools/safe-apply.sh` apply of the saved plan. Read back CodeSha256 and record it in the source map with
   `infra/aws/lambda/ci/record-deploy-scope.py`. Record `plan`, `apply` and `readback`.
7. **Precondition 4: sizing on the Lambda.** Invoke `{"dry_run": true, "accounts": "population", "backfill": {"start": D, "end": D}}`,
   where D is the newest LANDED `account_return_daily` day. `accounts` is an event-level key, not inside `backfill` (round 36's refusal).
   - Record `dry_run` {accounts, lots_rows, objects_written, duration_ms, max_memory_mb}, taking the duration and memory from the REPORT line.
   - **CTO condition:** above 1,740.8 MB or 765 s, roll back by the packet's route BEFORE 11:41Z, file a row and stop. A SOURCE_LAG day with
     0 lots rows sizes nothing: pick a landed day.
8. **The first fire.** Use the 07:41 ET (11:41Z) scheduled fire, or an ad-hoc `{}` invoke if that comes first; record `how`. Read A1 to A7 as
   the packet defines them, with A4 DELTA=0 on returns before any second fire and A7 printing the 18 member hashes. Record `first_fire`
   {request_id, how, a1..a7 each {pass, value}}, `a4.delta` and `a7.members`. Then close the ledger.
9. **Report the IAM write** in your final message; the issuer relays it to `0.0.0_AB_MSTR~DELL2`. Any delete under a new prefix waits on
   Andrew.

<criterion id="DB38-1-AC1" cell_refs="DB-b-78"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-1-AC1</invocation><expect>DB38-1-AC1 PASS</expect></criterion>
`DB38-1-AC1` -- plan exactly 0/3/0, apply complete, live CodeSha256 equal to the source map and not the anchor, the ledger pinned to the packet. Base: FAIL.

<criterion id="DB38-1-AC2" cell_refs="DB-b-78"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-1-AC2</invocation><expect>DB38-1-AC2 PASS</expect></criterion>
`DB38-1-AC2` -- the population dry_run on a landed day sizes the lots stage under 1,740.8 MB and 765 s, writing nothing. Base: FAIL.

<criterion id="DB38-1-AC3" cell_refs="DB-b-78"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r38/p38_round38.py" . DB38-1-AC3</invocation><expect>DB38-1-AC3 PASS</expect></criterion>
`DB38-1-AC3` -- the first fire's A1 to A7 pass, A4 DELTA=0, A7 printing 18 member hashes. Base: FAIL.

<expected_criteria>DB38-1-AC1,DB38-1-AC2,DB38-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception, under both signed halves:**
  - edit the source map and the three Terraform root files named in `<paths>`, and write the ledger;
  - upload ONE artifact;
  - run ONE targeted `safe-apply` from a saved plan;
  - invoke the function: ONE population `dry_run`, and at most one ad-hoc first fire;
  - roll back by the packet's route only if a stop condition fires.
- No other function, role, bucket or key. No S3 delete.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~55/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/reporting-gold/iam.tf
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-78.release-apply-r37.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 40 (round 38), cell `DB-b-78`.
<owned_cells>DB-b-78</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB38-1-AC1, DB38-1-AC2, DB38-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~55/IRPT_DASHBD.TO-DB-b-78.release-apply-r37.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB38-1-AC1,DB38-1-AC2,DB38-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the plan counts, live CodeSha256 and artifact version before and after, the dry_run REPORT line, A1 to A7, the IAM write, and the ledger, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the signed R37 packet IS the blast-radius read (five gold write prefixes, three silver read prefixes, one DynamoDB GetItem); plan must read 0/3/0.
comp-iam: RUN -- 214 IAM roles parsed, 196 services; BLIND on irpt-49f-reporting-gold-role (no service row); the packet's policy delta and A5 are the read.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: RUN -- the schedule cron(41 7 ? * MON-FRI *) America/New_York is unchanged by the plan; A1 reads the first fire.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB38-1-AC1/AC2/AC3 FAIL at base (no record). Both halves GIVEN (COO @9395a9c1bc, CTO @e64eb96736); live at the anchor since the 04:31Z rollback.
lane: the <paths> block IS the grant.
</preflight>
