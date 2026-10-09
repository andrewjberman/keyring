# NFRA_IAMROLES202609.TO-IAM-v-3 -- PREDICT one narrowing before it is made: the candidate, the prediction, the patch, the rollback

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R5.md</decomp_doc>
<owned_cells>IAM-v-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~13</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-5; the round-4 analysis calls this E3, and this is its first half)

```
IAM-v-3. ACT: choose ONE never-used permission on ONE role, find out with the existing instrument what
removing it would break, and put that prediction ON RECORD, committed, together with the exact change and its
rollback. You change NOTHING in AWS and NOTHING under infra/. A separate order (IAM-v-4, the CloudOps lane,
under a signed never-widen pair) makes the change later and reads the outcome against YOUR prediction.

FWD-5, verbatim:
  "An engineer can narrow a permission and know beforehand what it would break"
  DONE WHEN  EXERCISED -- a real narrowing has been checked in advance and the check was believed
  ACCEPT     Before anyone takes a permission away, they can find out what would stop working -- and be
             right. Nothing breaks because we tidied up.
  C-NO-ACCESSDENIED: the project must not cause the outage it exists to prevent.

THE POPULATION: org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/permission-cold-raw-bundle.round4.json
  run 2026-10-09, lookback 90, 280 roles, 1486 rows with status "never-used".
  shape: results[role_name] = {role, role_arn, rows: [{permission, status, last_used?, age_days?, reason?}]}

THE INSTRUMENT (run it, never edit it):
  org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/preflight-blast-radius.py
  (blob bd7620790c; read its header for arguments; it composes `.tools/comp-iam-usage permission-cold` and
  `reach-check`, i.e. live policy reads plus simulate-principal-policy, all READ-ONLY). Its round-2 report:
  deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/BLAST_RADIUS.md.

CHOOSING THE CANDIDATE -- every rule must hold, and PREDICTION.md says how each was checked:
  1. status "never-used" in the round-4 bundle (observable AND unused for 90 days -- never "unobservable").
  2. the role's policy is DECLARED in Terraform under infra/aws/terraform/ (find the exact file and line), so
     the change is a code edit with a revert as its rollback.
  3. NOT rows 8 or 10 of the governance disposition (opal-data-refresh-lambda-role, portal-auth-lambda-role),
     and not a role any portal or client login path assumes.
  4. ONE action, removed from ONE statement; no wildcard expansion, no other line moved.
  5. prefer a role whose consumers run at least daily, so the outcome can be read within a day.

WHAT TO PRODUCE, in deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/:
  (a) PREDICTION.json -- keys: role, role_arn, action, terraform_file, terraform_line, round4_status (copied
      from the bundle), consumers (every compute identity that assumes the role, with how you found it),
      predicted_breaks (a list; [] means "nothing will break"), observation_window (when v-4 can read the
      outcome, and which consumer run it waits for), rollback (the exact revert), instrument_blob.
  (b) PREDICTION.md -- the same in prose, the instrument's full output quoted, the comp-blast output on the
      module (`comp-blast` on the terraform file), and the reasoning from evidence to predicted_breaks.
  (c) narrowing.patch -- a git diff, against the base, of the ONE terraform file, removing the ONE action.
      It must apply cleanly with `git apply --check`. Do not apply it.
```

## DEPENDENCIES

None. `IAM-v-4` waits on this order and on a signed never-widen pair.

## BOUNDS

```
NOTHING CHANGES: no AWS write of any kind; no file under infra/ is edited (the patch lives in your
  deliverables directory only); no terraform plan or apply (v-4 plans it).
C-ANALYZER-PRICED-FIRST + G-25: no Access Analyzer.  G-21: no alert, alarm, monitor or schedule.
INSTRUMENTS ARE RUN, NOT REWRITTEN: .tools/ and every other worker directory are read surfaces.
BOUND EVERY AWS READ: each call under `timeout 120`; a timeout is recorded as the output.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
instrument pin   preflight-blast-radius.py blob bd7620790c6884d55969779812bebe9ba7565355 at the base e9bda7b982.
bundle pin       permission-cold-raw-bundle.round4.json blob 3ac4deb7f663065bbdc32b3efb76d251c4cfab7b.
aws shim         `.tools/aws`; `MSYS_NO_PATHCONV=1` only on calls carrying ARN arguments.
comp-* tools     invoke as `bash .tools/<tool>` from YOUR worktree: a bare name resolves through a ~/bin
                 forwarder to the MAIN checkout (row Z-S14).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-v-3.predict-one-narrowing-before-it-is-made.md
</paths>

Your surprise row id is `NFRA_IAMROLES202609-Z-W13-S<k>`, `"fabric": "site-z"`; `surfaced_at` = `date -u +%FT%TZ`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-v-3"><invocation>python -c "import json;d=json.load(open('org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/PREDICTION.json',encoding='utf-8'));print(d['round4_status'],d['role'],d['action'],d['terraform_file'],len(d['predicted_breaks']),bool(d['rollback']),bool(d['observation_window']))"</invocation><expect>one line beginning `never-used`, then the role, the action and a terraform_file under infra/aws/terraform/, then the predicted-break count, then `True True`; a FileNotFoundError or KeyError means the prediction is not on record</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-v-3"><invocation>bash -c "git apply --check org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/narrowing.patch && git apply --numstat org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/narrowing.patch"</invocation><expect>rc=0 and exactly ONE numstat line, whose path is the same terraform_file PREDICTION.json names -- one file, applicable, not applied</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-v-3"><invocation>git hash-object org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/preflight-blast-radius.py</invocation><expect>exactly bd7620790c6884d55969779812bebe9ba7565355 -- the round-2 instrument was run, not rewritten</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-v-3" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming
  3.0.0_SA_CVO~Z): is the prediction specific enough that the outcome could prove it wrong, and does the evidence in
  PREDICTION.md support it rather than assume it?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>5</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-v-3</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 5) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-4 slug @3f69d8a895 -> `ROUND_ANALYSIS.round4.md` @20c2fcabe8 E3 -> L5 round-5 decomp (E3 split, issuer ruling 1) -> this issuance.
**Chain:** head of chain v-3 -> v-4. **Risk LOCAL:** AWS reads only; the write surface is one deliverables directory.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 220`, BUDGET REACHED, 1 of 6 carriers, C1=23, C2=22 PARTIAL (0 of 22 scanned), rc=3; PARTIAL_OR_BLIND, not read as clean. G-21 binds as CLAUDE.md law.
comp-iam: RUN -- `bash .tools/comp-iam stats` from the main checkout: 214 IAM roles parsed / 196 services / 1154 operations; the cell uses it to confirm its candidate is declared.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (bundle 280 roles / 1486 never-used rows, blob 3ac4deb7f6; instrument blob bd7620790c).
</preflight>

**Preflight disposition:** checks dry-run at the base `e9bda7b982`: AC1 base: FAIL as expected (file absent); AC2 base: FAIL as expected (patch absent); AC3 base: PASS as expected (pin equals the base blob).
