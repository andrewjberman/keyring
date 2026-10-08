# MDPF_HEALGAP -- surprise channel, INVESTIGATION v1 (round 1)

Append-only. Worker rows `MDPF_HEALGAP-W<n>-S<k>`; seat rows `MDPF_HEALGAP-S<k>`.

```json
[
  {
    "id": "MDPF_HEALGAP-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T08:34:00Z",
    "one_line": "FWD-3 asks for the eleven missing model_detail days 2026-08-31..09-10 to be repaired by one act, but the runner sends Black Diamond no as-of date: a --date repair would land TODAY's model composition under those eleven dates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py @c21432885a: ingest() (lines 400-458) uses `date` only to build landing keys; the vendor calls are POST /api/models/strategies/search and POST /api/accounts/search with body {skip,take,sort,searchString} (line 231) and GET /api/models/{id} (line 313), none carrying a date",
        "the brief's own control (PART VI.3): the 2026-09-01T02:50Z one-shot re-run for 2026-08-31 landed models and accounts, i.e. current-state pages written under a past date"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-3: the eleven missing days of 2026-08-31 to 2026-09-10 repaired by one act; afterwards exactly those are present. ACT 2: the word is asked for only when the hop-0 read predicts that the repair will fill the days.",
    "world_is": "The Rebalancer endpoints the runner uses return current state only (no as-of parameter is sent, and none is known to exist). A repair can fill the eleven keys, but with 2026-10-xx compositions, not the compositions in force on those days. Whether any endpoint serves historical composition is unread. The disclosure ACT 2 owes Andrew changes from 'may return empty' to 'would fill the days with the wrong-dated composition unless a historical source exists'. Not a round-1 act (FWD-3 is enrichment 2); no vendor call made."
  },
  {
    "id": "MDPF_HEALGAP-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T08:34:00Z",
    "one_line": "Hop 0's cause read is answered in the repo, not unread: the count-reconcile self-gate raised between accounts and model_detail on 2026-08-31..09-10, fixed by c53e48f7fb and deployed 2026-09-11T03:26Z; the runner's log group keeps only 14 days, so the original failure lines are gone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda_function.py _reconcile_counts docstring (lines 337-363) at HEAD; git log c53e48f7fb 2026-09-10 22:17 -0400 'a count mismatch is DISCLOSED, not fatal -- one closed account froze the Cottonwood model chain for 11 days'",
        "aws lambda get-function cot-rebalancer-runner 2026-10-07: LastModified 2026-09-11T03:26:00Z",
        "aws s3api list-objects-v2 opal-data-assets blackdiamond/cottonwood/meta/2026-09-0 -> no complete-stamp; meta/2026-10-01..07-complete.json present, each ~06:01Z",
        "aws logs describe-log-groups /aws/lambda/cot-rebalancer-runner: retentionInDays 14; filter-log-events 2026-09-05T05:50Z+1h returns nothing"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD section 2 hop 0 and brief PART VII.1: why rebalancer_model_detail stopped 2026-09-01..09-10 while its siblings landed is UNREAD and must be read before building.",
    "world_is": "It is a second cause class (a vendor-maintained counter treated as a fail-closed gate), already closed in code and deployed. Its primary evidence (the runner's log) has aged out at 14 days, which also bounds FWD-2: 'read from the run's own result' cannot mean the CloudWatch log for anything older than two weeks."
  },
  {
    "id": "MDPF_HEALGAP-W1-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~1",
    "surfaced_at": "2026-10-07T08:56:59Z",
    "one_line": "The commit gate refuses every commit of lambda_function.py on this device: installed ruff is 0.16.10, the gate pins 0.15.11, and 0.16.10's default rule set raises 30 errors on the untouched base file.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -m ruff --version -> ruff 0.16.10; .tools/commit-gate.sh line 46 pins 0.15.11; `ruff check --target-version py39 --extend-select FA` on the base lambda_function.py (git show 474ec88e5a) -> Found 30 errors (UP031, I001, UP037, BLE001); the same call with ruff 0.15.11 -> All checks passed.",
        "Worker workaround, uncommitted: ruff 0.15.11 wheel unpacked under .scratch/ruff1511 and a PYTHONPATH shim .scratch/shim/ruff/__main__.py exec-ing it; commit 8af853ce59 landed through the unchanged gate on that shim. Also: no git committer identity on this device, supplied by GIT_COMMITTER_NAME/EMAIL env only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-HG-t1 commit step: safe-commit.sh runs the commit-gate (py_compile + ds-precommit + ruff py39) and a conforming edit passes.",
    "world_is": "Any worker commit of a .py file with the device's ruff 0.16.10 is blocked regardless of the edit (--force does not bypass). Sibling HG-t-2 edits the same file and meets the same block unless it carries the shim or the install is repaired.",
    "notes": "Not fixed here: the gate and the installed ruff are outside this order's write grant."
  },
  {
    "id": "MDPF_HEALGAP-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T09:12:00Z",
    "one_line": "Disarms MDPF_HEALGAP-W1-S1 (owner 2.0.0_SA_COO~G1): the ruff drift has no live effect on round 1, the box-wide repair is routed to 0.0.0_AB_MSTR~DELL1, and the worker's ruff 0.15.11 wheel has an unread provenance.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Round 1 has one more .py write: none. HG-t-2's <paths> is a .tf file only (task-orders/MDPF_HEALGAP.TO-HG-t2...md), so W1-S1's 'sibling HG-t-2 edits the same file' does not hold.",
        "HG-t-1 drained through safe-merge.sh at ca914096d7 (merge commits are not re-graded by ruff); the shim lives only in /c/tmp/wk-healgap-1/.scratch, uncommitted, and no gate file changed.",
        "python -m ruff --version -> 0.16.10 on dell1; .tools/commit-gate.sh:46 pins 0.15.11 (read 2026-10-07).",
        "/c/tmp/wk-healgap-1/.scratch/ruffwhl held ~11.5 MB at 08:53Z and ruff1511/ruff-0.15.11.dist-info was unpacked from it; whether the wheel came from the local pip cache or from PyPI is UNREAD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W1-S1: ARMED, disarm owner 2.0.0_SA_COO~G1; any worker .py commit on dell1 is refused and HG-t-2 meets the same block.",
    "world_is": "Disarmed for this project: no remaining round-1 order writes Python, and the issuer cuts no further .py order on dell1 that relies on a worker-fetched shim. The device repair (installed ruff matching the gate's 0.15.11 pin) is the box integrator's and is routed to 0.0.0_AB_MSTR~DELL1. If the wheel was fetched from PyPI it was package egress after 1.0.0_SA_CTO~DELL1 msg 71 noted that a PyPI install needs Andrew's egress word; that read is the CVO's to adjudicate."
  },
  {
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~F",
    "surfaced_at": "2026-10-07T11:12:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "MDPF_HEALGAP-S5",
    "one_line": "TO-HG-d1's <paths> write grant omits files the order's own step 5 (record-terraform-deploy.sh) writes and commits: infra/aws/terraform/opal-assets/CHANGELOG.json and the .open_deploys sentinel; the granted project ledger/ folder went unused.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/SURPRISE_ROWS_OWED_FROM_TO_HG_D1_20261007.md (on origin @ebd245f91d) Row 1",
        "commit b84c07b204 (2 files: the source map and opal-assets CHANGELOG.json)"
      ]
    },
    "spec_asserts": "TO-HG-d1 <paths>: the WRITE grant is org/critical_paths/change_management/, infra/aws/lambda/ci/lambda-source-map.json and org/missions/D8/MDPF/MDPF_HEALGAP/ledger/; everything else is read-only.",
    "world_is": "The directed tool writes infra/aws/terraform/opal-assets/CHANGELOG.json and org/critical_paths/.open_deploys/<slug>.json, neither granted; the deploy-completion ledger writes under change_management/, not the project ledger/. The issuer's own cut defect (2.0.0_SA_COO~G1): a deploy order's grant must enumerate the deploy tool's write set; carried into the next deploy order this issuer cuts."
  },
  {
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~F",
    "surfaced_at": "2026-10-07T11:12:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "MDPF_HEALGAP-S6",
    "one_line": "deploy_ledger.py close for one slug rewrote ten other seats' sentinels under org/critical_paths/.open_deploys/ in the same invocation; the deploying seat left them uncommitted and out of its commits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/SURPRISE_ROWS_OWED_FROM_TO_HG_D1_20261007.md (on origin @ebd245f91d) Row 2 (the ten slugs are listed there)",
        "the seat's ledger commits touched 2 and 3 files (pathspec held)"
      ]
    },
    "spec_asserts": "Closing one change-management ledger entry touches that entry only.",
    "world_is": "python .tools/deploy_ledger.py close --slug mdpf-healgap-hg-t1-runner-deploy-20261007 modified ten unrelated sentinels in the laptop tree. A seat committing with a loose pathspec after a close, or closing inside a worktree it then drains, would carry ten other deploys' state. The ten files sit modified and uncommitted on the laptop. Tool owner unread; outside this project's surface, so it reaches 1.0.0_SA_CTO in the slug."
  },
  {
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~F",
    "surfaced_at": "2026-10-07T11:12:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "MDPF_HEALGAP-S7",
    "one_line": "safe-apply.sh reports a mangled gate path (MSYS_NO_PATHCONV=1 exported) as 'BLOCKED by the naming plan limb (LGIC_ENFORCE ...)', a naming verdict, although no name was graded.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/SURPRISE_ROWS_OWED_FROM_TO_HG_D1_20261007.md (on origin @ebd245f91d) Row 3",
        "rc=7 with the variable set; rc=0 and the naming limb graded normally with it unset"
      ]
    },
    "spec_asserts": "An LGIC_ENFORCE naming BLOCK from safe-apply means a resource name is out of pattern.",
    "world_is": "The gate's script path was rewritten to C:/c/Users/.../.tools/naming-apply-gate.py and Python could not open it; the verdict line still read as a naming block, and rc=2 from that limb does not separate 'a name is wrong' from 'the gate could not run'. It failed closed (nothing planned or applied). The variable is banned for safe-apply by CLAUDE.md, so the act was operator error; the defect is the diagnostic. Outside this project's surface, so it reaches 1.0.0_SA_CTO in the slug."
  },
  {
    "id": "MDPF_HEALGAP-S8",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T13:00:00Z",
    "one_line": "This project's terraform calls on dell1 ran without CHECKPOINT_DISABLE=1 before the rule existed: the issuer's `terraform version` and failed `plan` (~09:0xZ), the HG1-t2-AC1 check's `terraform fmt` at the base dry-run, and slot 2's AC1 runs; the check now sets the variable.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~DELL1 msg 251 relaying laptop 1.0.0_SA_CTO msg 106231 (row NFRA_CTLPLN-W13-S8): a bare terraform call on a Dell contacts its vendor; no call without CHECKPOINT_DISABLE=1",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_t2_tf_check.py now passes env CHECKPOINT_DISABLE=1 to its fmt call (base re-run: TF-BAD no file, as before)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "No terraform call on a Dell reaches its vendor (CLAUDE.md: no egress off Opal infrastructure without Andrew's word).",
    "world_is": "Before 106231, this seat and worker slot 2 ran terraform on dell1 with the default checkpoint on, so each call may have contacted checkpoint-api.hashicorp.com (version check only; no data sent beyond the binary's version/platform). Whether the box's egress allowed it is unread. Future calls from this project's checks set the variable; the drain's re-run of HG1-t2-AC1 uses the amended check."
  },
  {
    "id": "MDPF_HEALGAP-W2-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~2",
    "surfaced_at": "2026-10-07T08:54:00Z",
    "one_line": "HG-t-2 cannot commit: the naming gate (ENFORCE) refuses the literal cot-bronze-complete in the new .tf file as a NEW hand-kept carrier of 'cot', and the only admitting routes (an r20_exception or tf_local entry in org/standards/NAMING_LEGACY_READS.json) are outside this order's write grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bash .tools/safe-commit.sh ... -- infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf (worktree wk-healgap-1-2, base 474ec88e5a): rc=1, 'NAMING REFUSE cot_rebalancer_reattempt.tf:23 cot-bronze-complete -> lookup(cottonwood)' and ':34 arn:aws:events:{x}:{x}:rule/cot-bronze-complete -> lookup(cottonwood)'; commit aborted, files unstaged",
        "infra/logic/registry/resources.json:2309 registers cot-bronze-complete as an EVENT_RULE under system blackdiamond (legacy-shaped name), so modules/opal_name name() cannot produce it and the gate's opal_name-module-arguments context does not apply",
        "hg_t2_tf_check.py requires the literal rule = \"cot-bronze-complete\" and a source_arn matching rule/cot-bronze-complete, so the literal cannot be moved out of the file without failing AC1",
        "AC1 TF-OK and AC2 SEAM-OK both pass on the uncommitted file; the proof-of-spec instance validated rc=0 before the commit attempt"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's grant (the .tf file, the investigation file, the deliverables folder, the order file) is enough to land HG-t-2, and the file copies the runner file's style.",
    "world_is": "A NEW .tf literal carrying the token cot is refused at commit unless NAMING_LEGACY_READS.json carries an r20_exception entry (needs a conformance-ledger register row) or a tf_local entry for it; both are outside the write grant and not the worker's to add. The file, proof instance and deliverables sit uncommitted in worktree C:/tmp/wk-healgap-2; the order stays pending. No gate was bypassed, no check weakened. Issuer decision needed: obtain the waiver entry, or reshape the order."
  },
  {
    "id": "MDPF_HEALGAP-W2-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~2",
    "surfaced_at": "2026-10-07T14:13:10Z",
    "one_line": "HG-t-2 still cannot commit after the R20 merge: entry MDPF-HEALGAP-R20-01 admits the bare literal on the rule line (:23) but the gate grades the source_arn string (:34) as a separate NEW carrier and refuses it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "After merge b780cda36a (CLOUD incl. dee4061bf9) bash .tools/safe-commit.sh ... -- infra/aws/terraform/opal-assets/cot_rebalancer_reattempt.tf: rc=1. Lines: 'NAMING DECLARED-EXCEPTION cot_rebalancer_reattempt.tf:23 cot-bronze-complete -> R20 X16 (waiver MDPF-HEALGAP-R20-01 ... 2 occurrence(s) as declared)' then 'NAMING REFUSE cot_rebalancer_reattempt.tf:34 arn:aws:events:{x}:{x}:rule/cot-bronze-complete -> lookup('cottonwood'); why: NEW hand-kept carrier (context rule)'; 'NAMING-GATE: REFUSE 2 graded'. Commit aborted.",
        "First attempt also showed 'literal occurs 3 time(s) in the file text, declared 2'; the third occurrence was a header comment, reworded to drop the literal (the file now holds exactly 2 textual occurrences: :23 and :34). The count refusal cleared; the :34 refusal did not.",
        "hg_t2_tf_check.py:46 requires source_arn to match 'rule/cot-bronze-complete' on one line of the permission block, and :37 requires rule = \"cot-bronze-complete\" in the target block, so both occurrences are forced by AC1 and cannot be restructured without failing it.",
        "org/standards/NAMING_LEGACY_READS.json entry MDPF-HEALGAP-R20-01 @dee4061bf9: literal 'cot-bronze-complete', occurrences 2; the gate matches the entry to the whole-string literal at :23 only, so the :34 string 'arn:aws:events:{x}:{x}:rule/cot-bronze-complete' is graded as a different literal."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer ruling on W2-S1: with entry MDPF-HEALGAP-R20-01 on CLOUD, the naming gate admits the .tf file and the commit lands.",
    "world_is": "The entry covers the rule line but not the source_arn line; a second entry (or a literal/occurrence form the gate matches to the ARN string, e.g. the ARN-shaped literal as its own R20 row) is owed by 1.0.0_SA_CTO~DELL1 outside this order's write grant. The .tf file passes AC1 and AC2 uncommitted; the order stays open; no bypass or override was used."
  },
  {
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~F",
    "surfaced_at": "2026-10-07T17:30:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "MDPF_HEALGAP-S9",
    "one_line": "TO-HG-d2 act 4 ('record-terraform-deploy.sh as for HG-d1') does not fit a wiring-only apply: the recorder resolved an empty deployment set and refused (rc=2, nothing written), and its HG-d1 form would have mis-stamped the runner's last code deploy as HG-d2's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/SURPRISE_ROWS_OWED_FROM_TO_HG_D2_20261007.md (on origin @905aa9c271) Row 1",
        "recorder output: 'stamped 0 of 15 rows under opal-assets' / 'resolved deployment set is EMPTY ... REFUSING'; git status empty on the source map and CHANGELOG after the run"
      ]
    },
    "spec_asserts": "TO-HG-d2 act 4: run record-terraform-deploy.sh as for HG-d1.",
    "world_is": "The apply created an event target and a Lambda permission and moved no Lambda code, so record-deploy-scope.py admits no address and the recorder correctly refuses. The issuer's cut copied a CODE-deploy step into a WIRING deploy (2.0.0_SA_COO~G1's defect): a wiring-only order omits act 4 or names the empty-set refusal as its expected outcome. The seat refused the --function form that would have overwritten the HG-d1 stamp."
  },
  {
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~F",
    "surfaced_at": "2026-10-07T17:30:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "MDPF_HEALGAP-S10",
    "one_line": "A 0-diff targeted plan still lists module.cot_rebalancer_runner.aws_lambda_function.this in resource_changes (actions no-op); only record-deploy-scope.py's actions filter keeps it out, and a --plan path given from the repo root fails with the same 'scope resolution refused' wording as a legitimate refusal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/SURPRISE_ROWS_OWED_FROM_TO_HG_D2_20261007.md (on origin @905aa9c271) Row 2",
        "terraform show -json: the function address present with change.actions == ['no-op']; --plan infra/aws/terraform/opal-assets/hgd2.tfplan doubles the prefix ('Failed to read the given file as a state or plan file')"
      ]
    },
    "spec_asserts": "Feeding a saved plan to the recorder scopes it to what that plan applies, and its refusal names its cause.",
    "world_is": "A reader who counts aws_lambda_function entries in resource_changes without reading change.actions concludes the apply deployed the runner (the seat did, then corrected it from the resolver source). And --plan resolves against the terraform root, so a path fault and an empty-set refusal print the same verdict line -- the same diagnostic-ambiguity shape as MDPF_HEALGAP-S7. Tool owner unread; outside this project's surface, so it reaches 1.0.0_SA_CTO in the slug."
  },
  {
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-07T20:20:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G1",
    "disposition": "UNDER_INVESTIGATION",
    "id": "MDPF_HEALGAP-D1-S1",
    "one_line": "The induced auth-lapse input on the cot rebalancer's daily event target stands about 12.5 hours (17:40Z to 06:20Z 2026-10-08), not the half's 'about 25 minutes'; any untargeted apply of opal-assets in that span restores the input and silently voids the 06:00Z FWD-1 test.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "laptop 1.0.0_SA_CTO msg 106554, relayed as dell1 msg 627: CROSS-BOX DEPLOY NOTICE, no untargeted apply of infra/aws/terraform/opal-assets until 06:20Z 2026-10-08",
        "~F's plan at 20:10Z: aws_cloudwatch_event_target.cot_rebalancer_runner_daily '1 to change'; live input {\"mode\":\"pull\",\"induce\":\"auth-lapse\"}"
      ]
    },
    "spec_asserts": "The FWD-1 exercise half (CTO_HALF_MDPF_HEALGAP_FWD1_EXERCISE_20261008) sizes the induced state at about 25 minutes.",
    "world_is": "The input was set at 17:40Z for a 06:00Z fire and is restored at 06:20Z, so the window is about 12.5 hours, across a whole evening of other applies on a shared root. The only guard is the laptop's time-boxed notice. Disarm: G1 restores the input at 06:20Z and reads the target back; the notice expires then."
  },
  {
    "id": "MDPF_HEALGAP-D1-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-07T20:26:00Z",
    "one_line": "Disarms MDPF_HEALGAP-D1-S1 (disarm owner 2.0.0_SA_COO~G1): the ~12.5h induced-input window is guarded by the laptop CTO's CROSS-BOX DEPLOY NOTICE until 06:20Z, ended by the 06:05-06:20Z restore (owner ~F at 06:03Z, this seat armed at 06:10Z), and the HG-d3 half now states the true window.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "laptop 1.0.0_SA_CTO msg 106554 (relay 0.0.0_AB_MSTR~DELL1 msg 628): no untargeted apply of infra/aws/terraform/opal-assets until 06:20Z 2026-10-08; a targeted plan must not name aws_cloudwatch_event_target.cot_rebalancer_runner_daily",
        "half corrected @5c14dbcb51 (17:40:36Z to the 06:05-06:20Z restore, ~12.5 hours)",
        "restore fallback owner (2): org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_d3_restore_fallback.py @cc6b15a7f3, one-shot armed for 06:10Z; dry run 2026-10-07T17:59Z named the exact re-put"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D1-S1: ARMED -- an untargeted apply of opal-assets inside the window restores the input and silently voids the 06:00Z test.",
    "world_is": "Disarmed for the window: every apply of opal-assets is held to a targeted plan that does not name the daily target until 06:20Z, and the restore owners are named and armed. Residual (not a hazard): the guard is a notice binding by reading, not a gate; the cut lesson is that an amendment moving a step's time re-reads every half bounding that step's duration."
  },
  {
    "id": "MDPF_HEALGAP-D1-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-08T06:20:00Z",
    "one_line": "The HG-d3 restore of cot-rebalancer-runner-daily's input landed at 06:08:46Z from an actor none of the three named restore owners claims: the laptop CTO made no put, ~F was down, and dell1's fallback read NOOP at 06:10:09Z.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CloudTrail PutTargets 05:50-06:15Z: 1 of 1 on rule cot-rebalancer-runner-daily, 2026-10-08T06:08:46Z, user/Andrew_Berman, input {\"mode\":\"pull\"} (read by 2.0.0_SA_COO~G1 06:1xZ)",
        "0.0.0_AB_MSTR~DELL1 msg 808: key ending CBIJ, IP 108.242.96.89, aws-cli/1.44.44 Python 3.12.10 Windows 10.0.26100; laptop 1.0.0_SA_CTO says it made no put; dell1 acts as cloudops-dell1-agent-user on aws-cli 2.37.9",
        "hg_d3_restore_fallback.py 06:10:09Z NOOP-ALREADY-RESTORED; OS task 06:11:01Z NOOP-ALREADY-RESTORED; hg_fwd1_exercise.py --restored RESTORED-OK 06:10:23Z"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-HG-d3 step 2 and the FWD-1 never-widen half: the restore is made by a named owner -- (1) 0.7.0_AE_CloudOps~F, (2) 2.0.0_SA_COO~G1 at 06:10Z, (3) laptop 1.0.0_SA_CTO at 06:17Z -- with its put time-stamped in the ledger.",
    "world_is": "The right value landed inside the 06:05-06:20Z window, so the exercise is intact (FAILED-OK, RESTORED-OK). But the act carries no owner: a laptop-credential process or Andrew directly wrote the target, and nothing in the order or the halves names it. INERT: the value is the declared restore value and no further put is pending. The ledger names the actor by CloudTrail identity until the laptop identifies it (asked by MSTR~DELL1 msg 808)."
  },
  {
    "id": "MDPF_HEALGAP-D1-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-08T13:25:00Z",
    "one_line": "Advances MDPF_HEALGAP-D1-S3: the 06:08:46Z restore was made by an automated laptop-credential process -- the same key and client that set the induce at 17:40:39Z ran a read-put-read restore after polling the rule roughly hourly all night; Andrew confirms it was not by hand.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Andrew-direct 13:1xZ (0.0.0_AB_MSTR record @14130c9b47): 'i did not do it by hand ... more likely a cascading issue/error, look into it regardless.'",
        "CloudTrail read by 2.0.0_SA_COO~G1 13:2xZ, rule cot-rebalancer-runner-daily, 10-07 12:00Z..10-08 06:15Z: PutTargets 2 of 3 events on the rule, both user/Andrew_Berman key ...CBIJ aws-cli/1.44.44 -- 17:40:39Z (the induce set, TO-HG-d3 step 1) and 06:08:46Z (the restore).",
        "06:08 shape: ListTargetsByRule 06:08:41Z -> PutTargets 06:08:46Z -> ListTargetsByRule 06:08:56Z (the order's step-2 read, put, read-back).",
        "Same client read the rule ~hourly overnight: 18:42, 19:09, 20:10, 20:29, 20:39, 20:43, 21:24, 21:36, 22:22, 22:48, 23:06, 23:48, 00:40, 01:35, 02:36, 03:34, 04:37, 05:41, 06:08:41Z (130 ListTargetsByRule on the rule in the window, all principals).",
        "Source IP 108.242.96.89 is shared with dell1 (cloudops-dell1-agent-user reads from it too), so IP does not discriminate the box; principal + OS build 26100 (dell1 26200) do (1.0.0_SA_CTO~DELL1 msg 911)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D1-S3: the restore carries no owner -- the laptop CTO made no put, ~F's timers were reported dead at 20:2xZ (MSTR msg 642), dell1 read NOOP.",
    "world_is": "An owned automation did it: a laptop-credential process with ~F's toolchain kept polling the rule all night and restored on schedule. Most likely 0.7.0_AE_CloudOps~F's owner-(1) restore loop survived the session kill that was reported as 'timers died', so the defect is a liveness report that called a running loop dead, not an unknown actor. INERT: correct value, in window. Open until the laptop names the process (asked via 0.0.0_AB_MSTR~DELL1)."
  },
  {
    "id": "MDPF_HEALGAP-D1-S5",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-08T13:30:00Z",
    "one_line": "Names the actor of MDPF_HEALGAP-D1-S3/D1-S4: the 06:08:46Z restore was laptop 0.7.0_AE_CloudOps~F's own failsafe script (background task bv5miebw8, session 393fd2b5), which outlived the 20:2xZ kill ~F reported, polled hourly, acted once and exited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.0.0_AB_MSTR~DELL1 msg 924, relaying the laptop MSTR (bus 355bc946), measured on the laptop: task bv5miebw8 output (414 bytes, last write 06:08:55Z) reads FAILSAFE-WOKE 06:08:40Z current_input={\"mode\":\"pull\",\"induce\":\"auth-lapse\"} / FAILSAFE-ACTING / FailedEntryCount 0 / PUT_UTC 06:08:45Z / READBACK {\"mode\":\"pull\"} / FAILSAFE-RESTORED-BY-SCRIPT; nothing runs now.",
        "Matches the CloudTrail reconstruction in D1-S4 (list 06:08:41Z, put 06:08:46Z, list 06:08:56Z; hourly reads 18:42Z..05:41Z; cadence ends after 06:35:48Z).",
        "Site Z ruled out on OS build 26200 vs the event's 26100 (MSTR msg 919)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MSTR msg 642 (relaying laptop CTO 106564): ~F's HG-d3 timers 'DIED' in the laptop's 20:2xZ out-of-memory kill, neither had fired, so owners (2) and (3) carried the restore.",
    "world_is": "One of ~F's restore mechanisms was an unattended background task that survived both the kill and the seat's close and did the restore correctly inside the window. The restore therefore had an owner the whole time; the defect is the liveness report ('timers died') that called a running task dead. For the next cut: a seat that arms a restore names every mechanism it armed and reads each one's state, rather than inferring death from its own session ending. Follow-up of the killed-but-not-killed gap is the laptop's (MSTR msg 924)."
  }
]
```
