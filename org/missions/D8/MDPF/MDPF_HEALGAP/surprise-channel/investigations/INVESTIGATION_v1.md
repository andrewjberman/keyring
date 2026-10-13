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
    "id": "MDPF_HEALGAP-S11",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~F",
    "surfaced_at": "2026-10-08T13:05Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "Condition 4 of the FWD-1 exercise half sets its service line at 13:30Z, but gold dim_model_portfolio -- the gold layer built from the Cottonwood model silver tables -- lands at 13:30:39Z-13:30:42Z on 9 of the last 10 days, so a condition-4 read widened to gold returns MISSED on a normal day with nothing wrong.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3api list of blackdiamond/cottonwood/gold/dim_model_portfolio/ at 2026-10-08T13:0xZ: 60 partitions; the newest 10 LastModified in UTC are 2026-10-07 13:30:40Z, 10-06 13:30:40Z, 10-05 13:30:40Z, 10-04 13:30:40Z, 10-03 13:30:39Z, 10-02 13:30:40Z, 10-01 22:08:16Z, 09-30 13:30:42Z, 09-29 13:30:40Z, 09-28 13:30:40Z -- 9 of 10 inside 13:30:39Z-13:30:42Z, the tenth later still",
        "the writer is data/assets/scripts/gold/build_dim_model_portfolio.py invoked by the EC2 mdpf-daily-runner at infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:554, NOT by the runner's on_success destination opal-assets-silver-blackdiamond, so gold is not on the chain condition 4 names",
        "129 scheduled EventBridge rules enumerated with aws events list-rules: none carries a 13:30 cron (nearest are opal-assets-silver-blackdiamond-sweep-daily and etf-positioning-producer-daily at cron(0 13 * * ? *)), which corroborates that the 13:30:40Z arrival is the EC2 runner's own cadence and not an Events schedule",
        "leg L5 of org/critical_paths/.open_deploys/mdpf-healgap-hg-d3-fwd1-exercise-20261008.json: condition 4 graded MET at 13:01:58Z on the instrument the condition names, the on_success chain's newest write for D=2026-10-08 at 11:46:08Z, with the four model silver tables at 11:32:29Z-11:32:33Z"
      ]
    },
    "spec_asserts": "CTO half condition 4, carried as TO-HG-d3 act 4b: whether the date's served Cottonwood figures were in place by 13:30Z is a discriminating read of whether the heal delivered in time.",
    "world_is": "On the instrument the condition names -- the on_success chain -- D=2026-10-08 read MET by 1h43m, so the heal itself is not in question and this row does not reopen it. But the 13:30Z line sits 39 to 42 seconds INSIDE gold's own daily arrival, so widening 'served' to gold makes the same read return MISSED on nine of the last ten days with no failure present: at that width the line discriminates nothing. FWD-1's own wording is 'by the end of the same day', which both widths satisfy. Owner: 2.0.0_SA_COO~G1, to decide whether condition 4's successor reads silver and keeps 13:30Z, or reads gold and moves the line past the mdpf-daily-runner's arrival.",
    "notes": "Not fixed here: the half's text and the gold producer's cadence are both outside this order's write grant, and no remedy is proposed as executed. Distinct from MDPF_HEALGAP-D1-S3, which is about the unattributed 06:08:46Z restore, not the 13:30Z line."
  },
  {
    "id": "MDPF_HEALGAP-S12",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~F",
    "surfaced_at": "2026-10-08T14:25Z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The actor of the 06:08:46Z HG-d3 restore is this seat's OWN fail-safe background task, which outlived a harness-reported kill AND the seat's close and made a production AWS write about 10 hours later with no live seat: a harness kill notice is not evidence the process died, and an unregistered armed actuator can act for a seat that no longer exists.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Read directly by this seat at 2026-10-08T14:2xZ, not taken from a report: C:/Users/AndrewBerman/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/393fd2b5-feaa-49dd-81e2-9376e8701755/tasks/bv5miebw8.output, 414 bytes, mtime 2026-10-08 02:08 local (06:08Z). Verbatim: FAILSAFE-WOKE 2026-10-08T06:08:40Z current_input={\"mode\":\"pull\",\"induce\":\"auth-lapse\"} / FAILSAFE-ACTING the induce input is still live -- performing the order's second put-targets / FailedEntryCount 0 / FAILSAFE-PUT_UTC=2026-10-08T06:08:45Z / FAILSAFE-READBACK {\"mode\":\"pull\"} / FAILSAFE-RESTORED-BY-SCRIPT -- the seat still owes HG1-d3-AC3, the no-change plan and the ledger record",
        "The sibling 06:03Z wake task's output file in the same directory reads [killed], 10 bytes, mtime 2026-10-07 16:26 local (20:26Z) -- so of the two timers the prior session reported killed at 20:2xZ, ONE really died and the other did not, and both were reported the same way",
        "FAILSAFE-PUT_UTC 06:08:45Z matches the CloudTrail PutTargets at 2026-10-08T06:08:46Z to the second, and the user agent aws-cli/1.44.44 Python 3.12.10 Windows 10.0.26100 matches this laptop's own shim exactly",
        "HAZARD SPENT, measured: a Win32_Process census over every process on this box for the prior session id 393fd2b5-feaa-49dd-81e2-9376e8701755 and separately for put-targets|hg_d3|FAILSAFE|cot-rebalancer-runner-daily returns ZERO rows, so no such actuator is running now",
        "0.0.0_AB_MSTR msg 106939 to 1.0.0_SA_CTO (13:25:26Z) reports the same file and quotes Andrew at dell1 ~13:1xZ: \"i did not do it by hand ... look into it regardless\""
      ]
    },
    "spec_asserts": "CTO ruling 106485 names owner (1) of the restore as 0.7.0_AE_CloudOps~F \"at its 06:03Z wake\", and the prior session's own log states that the 06:03Z wake and the idempotent fail-safe were armed in-session and that \"neither survives this session ending\" -- which is why the four-deep fallback chain was ruled at all.",
    "world_is": "One of the two DID survive, and it acted correctly at 06:08:45Z with no live seat, so owner (1) in effect performed step 2 after all. Three consequences, none of which the order or the ruling anticipated. (1) A harness-reported kill is not evidence a process died: the prior session reported both timers killed at 20:2xZ and one of them was still running ten hours later. (2) An armed actuator that can make a PRODUCTION AWS write is invisible once its seat is gone: nothing in org/ref/LIVE_ARMS.md, the broker, the task orders or the halves named it, so the fabric spent about seven hours attributing the write to an unknown actor and reached \"operator's own terminal, inferred\" -- while the answer sat in a 414-byte file on this box the whole time. (3) The ledger entry that should carry the correction cannot: once deploy_ledger.py close removes the sentinel, close-leg refuses the slug outright (measured), and a hand-edit of the entry .md is outside that tool's world, so leg L2's text stands as written at close and this row plus the proof instance carry the correction instead. DISARM (1.0.0_SA_CTO): rule whether a seat may arm an actuator that can outlive its session and make a production write, and if so require the arm to be registered where the next reader can attribute it in ONE read -- an org/ref/LIVE_ARMS.md row naming the task id, the exact write and the condition. Until that exists the next such put-targets is mis-attributed exactly the same way.",
    "notes": "The specific process is gone, so nothing needs killing; the ARMED standing is about the PRACTICE, which recurs on the next seat that arms a fail-safe. Answers the open question in MDPF_HEALGAP-D1-S3 (2.0.0_SA_COO~G1) rather than re-filing it; D1-S3's own disposition stays its owner's. Distinct from MDPF_HEALGAP-S11, which is about condition 4's 13:30Z line."
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
  },
  {
    "id": "MDPF_HEALGAP-D1-W3-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~3",
    "surfaced_at": "2026-10-08T15:02:00Z",
    "one_line": "HG-t-3 reads the earlier run result with s3:GetObject to set healed_at, but the runner role is granted PutObject and ListBucket only, so in production the read fails soft and healed_at is never recorded on a re-attempt.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf:73-112 @f0da37597a: statements WriteOwnCottonwoodBronzeMeta (s3:PutObject on bronze/* and meta/*), ListCottonwoodForLandingGuard (s3:ListBucket), DenyBlackdiamond49fFirmSep; a scan of the file for 'GetObject' / 's3:Get' finds none (the only s3:* is the :103 Deny on the 49f tree)",
        "infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py _already_landed docstring: 'the role holds s3:ListBucket, not s3:GetObject'",
        "task order HG-t-3 build item 1 asks healed_at to be set 'when an earlier result marked a feed missing', which needs a read of the earlier result; _read_earlier_result in the worker's change attempts get_object and returns {} on any failure, so the run never fails on it",
        "test_healgap_result.py::test_reattempt_records_healed_at_for_the_filled_feed passes against an in-memory S3 that serves get_object; nothing in this order exercises the real role"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "HG-t-3 item 1: when an earlier result marked a feed missing and this run lands it, healed_at is set; and the preflight says the result key sits inside the runner's existing PutObject grant with no role change.",
    "world_is": "PutObject on meta/* covers writing the result, and the per-feed arrived/missing status and the PARTIAL raise never need a read (they come from listing). Only the healed_at carry-over needs GetObject on meta/<date>-result.json, which the role does not hold, so on the live role a re-attempt that fills the feed still reads COMPLETE with healed_at null. Owner: 2.0.0_SA_COO~G1 to decide whether the role gains s3:GetObject on blackdiamond/cottonwood/meta/*-result.json (a terraform change outside this order's grant) or healed_at is read as best-effort. Not fixed here; no check weakened."
  },
  {
    "id": "MDPF_HEALGAP-D1-W6-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~6",
    "surfaced_at": "2026-10-08T15:22:25Z",
    "one_line": "FWD-6 asks each session-dependent pull to be marked RECOVERS or NOT-EXPOSED, but four pulls (five schedules) are exposed to a lapsed login and have neither answer: asset-dim, two Schwab SDD pulls, and the ASTN FT leg.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bd-asset-dim-pipeline-trigger cron(10 22 ? * MON-FRI *) fires SSM opal-bd-asset-dim-download, which mints a bearer from blackdiamond/49f/session (infra/aws/ssm/opal-bd-asset-dim-download.json line 23); the 49F fees mint bd-49f-fees-session-daily is cron(20 22 ? * MON-FRI *), ten minutes later (live list-rules read 2026-10-08); no re-attempt target exists on the rule",
        "canonical-schwab-si2-08242234-daily-pull and canonical-schwab-si2-08335338-daily-pull run sdd-daily-pull.ps1, whose own text says a dead standing SI2 session needs a human to re-establish it (infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1:271-272); the 30-day lookback (:33) refills the days only after that",
        "astn-wsjft-3am-run rides the parked astn/ft/session cookie (tools/astn_wsjft/scripts/run.py:53-59); on failure it records the warning 'session expired? -> run harvest_ft_session' (run.py:133), a manual step",
        "the census with all 23 answered rows and the section 'Exposed, neither answer is true': org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-HG-t7 and PRD FWD-6: every scheduled pull whose success depends on a vendor login kept alive by something else is marked either 'recovers the same way' or 'not exposed, because ...'; a pull left without an answer fails the outcome. AC1 accepts only RECOVERS or NOT-EXPOSED because <reason> in the answer column.",
    "world_is": "Four pulls on five schedules depend on a login that lapses and is not re-minted before they run, and neither answer is true of them (asset-dim: no re-attempt and the missed as-of is not re-pulled; Schwab SDD: next-fire catch-up but only after a person restores the session; ASTN FT: manual cookie harvest, no re-attempt). They are listed outside the table, each with the recovery that exists today, so the table carries no false answer and AC1 still reads CENSUS-OK on the 23 true ones. Whether FWD-6 is met for these four is the CVO's grade, and whether they become round-3 enrichment is the COO's and CTO's.",
    "notes": "No remedy attempted; the order is read-only and these are outside its write grant. ARMED because a lapse on any of the four in normal operation leaves a day unfilled with nobody acting; disarm owner is the round issuer, who recuts."
  },
  {
    "id": "MDPF_HEALGAP-D1-W6-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~6",
    "surfaced_at": "2026-10-08T15:22:25Z",
    "one_line": "The native Grep tool fails in this worker environment with ENOENT on ripgrep, and the comp-find census verb ran past the 120s Bash bound on a two-token query.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Grep(pattern='recover_or_exit|check_jwt_freshness|assert_fresh_or_exit', path='C:/tmp/wk-healgap-6/infra/aws/lambda/inf-pipeline') returned 'ENOENT: no such file or directory, uv_spawn rg' at the worker's first search, 2026-10-08 ~15:1xZ",
        "comp-find 'wsd-49f-partner-held-etf-daily|wsb-49f-model-aua-daily' --files --all --limit 30 was moved to the background after the 120s timeout (task b56zda7kh) and completed with exit 0 later; the worker did not wait on it and read the same answer with git ls-files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worker brief: code search by comp-find / comp-which, and the Grep tool is fine.",
    "world_is": "The Grep tool cannot run (no ripgrep binary found by the harness in this session), and comp-find with --all on the whole worktree is slow enough to exceed the bound, so the census reads were done by git ls-files plus Python line scans and direct file reads. Results are the same file:line facts; only the instrument differed."
  },
  {
    "id": "MDPF_HEALGAP-D1-W6-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~6",
    "surfaced_at": "2026-10-08T15:23:25Z",
    "one_line": "The order says worker rows are MDPF_HEALGAP-W6-S<k>, but the row gate refuses that id on fabric dell1 and requires MDPF_HEALGAP-D1-W6-S<k>.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-HG-t7 BOUNDS refusal clause: 'a surprise row (id MDPF_HEALGAP-W6-S<k>, fabric dell1, ...)'",
        ".tools/surprise-row-gate.py at the commit of this row: \"MDPF_HEALGAP-W6-S1: fabric='dell1' but the id carries no coordinate ... dell1 = id <CODE>-D1-S<n> (worker: <CODE>-D1-W<n>-S<k>)\""
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-HG-t7 BOUNDS: worker surprise rows are minted MDPF_HEALGAP-W6-S<k> with fabric dell1.",
    "world_is": "On fabric dell1 the gate accepts only MDPF_HEALGAP-D1-W6-S<k>. This worker's rows are therefore MDPF_HEALGAP-D1-W6-S1, -S2 and this one (-S3); the proof instance cites the D1 form."
  },
  {
    "id": "MDPF_HEALGAP-D1-S6",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-08T15:30:00Z",
    "one_line": "Disarms MDPF_HEALGAP-D1-W6-S1 (disarm owner 2.0.0_SA_COO~G1): the four exposed session-dependent pulls (bd-asset-dim-trigger, two Schwab SDD masters, the ASTN FT leg) pre-date this project and change nothing it builds; they are routed by name to the round-2 drain-end read as FWD-6 residuals for the CTO's round-2 analysis, never left as a silent census footnote.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md section 'Exposed, neither answer is true' (drained @a0ee7928f1); CENSUS-OK rows=23 denominator=162 re-run by the issuer.",
        "PRD v0.2 FWD-6 ACCEPT: each pull marked RECOVERS or NOT-EXPOSED because ...; a pull left without an answer fails the outcome. C-FIX-NOT-NOTIFY: no outcome becomes a monitor or alert.",
        "None of the four is touched by any round-2 write set (decomposition ROUND 2, write sets)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D1-W6-S1: ARMED -- four pulls depend on a login that lapses and is not re-minted before they run, with neither answer true.",
    "world_is": "The exposure is real and pre-existing (not caused or widened by MDPF_HEALGAP). Disarmed for this project by routing: the round-2 drain-end read carries the four by name as FWD-6 NOT YET REALIZED residuals, each with its recovery today, so the CTO's round-2 analysis decides whether each becomes a round-3 cell (heal it the way FWD-1 did) or a ruled NOT-EXPOSED with a new reason. No monitor or notification is built (C-FIX-NOT-NOTIFY). Owner of the routing: 2.0.0_SA_COO~G1; owner of the decision: 1.0.0_SA_CTO~DELL1 at L10."
  },
  {
    "id": "MDPF_HEALGAP-D1-S7",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-08T16:05:00Z",
    "one_line": "A second reader of the runner's same-day bronze was missed by every half of this project: cot-satellites-registry-producer-daily cron(0 7 * * ? *) is DERIVED from the runner's 06:00Z landing. Today's induced failure (HG-d3) starved it: 07:00Z and 07:01Z both BLOCKED, so the served platinum/satellites/registry.json and holdings.json still read as_of 2026-10-07. The HG-t-5 move to 12:45Z would starve it every day.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~DELL1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf:286 description 'Fires 1h after the measured 06:00:43Z upstream landing'; the same file's schedule comment: if cot-rebalancer-runner-daily is ever re-anchored, this cron must move with it.",
        "CloudWatch /aws/lambda/cot-satellites-registry-producer 2026-10-08: 07:00Z and 07:01Z 'RegistryProducerError: BLOCKED: no roster partition at s3://opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_models/2026-10-08/page_000.json'; no event after 07:04Z. Paginated read 09-28..10-07: 'OK: wrote' on each of 10 of 10 days.",
        "s3 head opal-data-cot platinum/satellites/registry.json LastModified 2026-10-07T07:00:19Z, body as_of 2026-10-07; holdings.json 2026-10-07T07:00:20Z.",
        "Round-1 never-widen halves and the R2 act-2 half draft counted N=1 reader (the 13:30Z silver/gold floor); comp-find over infra/ for cot-rebalancer-runner-daily hits the runner's own .tf and this file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD/decomp ROUND 2 HG-t-5: moving the daily fire to cron(45 12 * * ? *) changes one schedule under its own pair with served delta 0; round-1 exercise halves: an induced 06:00Z failure healed by 11:32Z reaches every served reader by its floor.",
    "world_is": "The satellites producer reads same-day bronze at 07:00Z with no re-attempt, so any day the runner lands after 07:00Z serves a one-day-stale registry. Today is such a day (stale now). Held by 2.0.0_SA_COO~G1: HG-t-5 is NOT applied (act 2 split; the age change HG-t-4 alone may proceed). Disarm owner 1.0.0_SA_CTO~DELL1 rules (a) the same-day re-run of the producer (a served write off its clock; never-widen pair, owner 0.6.2_AE_PartnerETL) and (b) the FWD-5 design: move the satellites trigger with the runner, chain it to the stamp, or withdraw HG-t-5."
  },
  {
    "id": "MDPF_HEALGAP-D1-S8",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-08T16:08:00Z",
    "one_line": "D1-S7 ruling (a) executed, branch A: the same-day re-run at 16:07:33Z rewrote registry.json and holdings.json as_of 2026-10-08; the served gap is closed. D1-S7 stays ARMED until ruling (b), the stamp chain, is cut as a PRD addendum at L10 (CTO 51c9c0e64a section 3).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Ledger org/critical_paths/change_management/20261008T1607Z_healgap-satellites-rerun-20261008_deploy_completion.md CLOSED, 2 of 2 legs proven.",
        "head_object 16:08Z: registry.json 16:07:36Z version vXnGqZ.W7ab8xIhkZT5ZKttXNHMQS.bS as_of 2026-10-08 books 9; holdings.json 16:07:37Z version 3QEozK4gibtzby_gvIuHUz9uqWNxAMOx.",
        "A correction to D1-S7: its surfaced_at reads 16:05Z; the actual time was ~15:43Z (broker send 20261008T154308Z). The row is append-only and left as written."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D1-S7: the served satellites registry reads as_of 2026-10-07 on 2026-10-08.",
    "world_is": "Served keys read as_of 2026-10-08 from 16:07:36Z. The structural cause (a 07:00Z cron coupled to the runner's fire time) remains until the stamp chain lands."
  },
  {
    "id": "MDPF_HEALGAP-D1-S9",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
    "surfaced_at": "2026-10-09T07:21:10Z",
    "one_line": "R2-1 / HG-t-8 cannot be committed as written: the naming commit limb REFUSES the order's own verbatim statement text. naming-gate.py grades the added Resource literal a NEW hand-kept carrier of the firm token 'cottonwood' and demands it be read through lookup('cottonwood') -- a form a .tf file cannot express. The three identical literals already in the same resource are graded EXISTING and only WARN, so the refusal turns on the line being new, not on the name being wrong.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit 2026-10-09 ~07:13Z: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.' NAMING REFUSE infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf:94 arn:aws:s3:::{x}/blackdiamond/cottonwood/meta/*-result.json -> lookup('cottonwood'); why: NEW hand-kept carrier (context rule). NAMING-GATE: REFUSE 1 graded, denominator 1 of 1 seen.",
        "naming-gate.py:1737 returns REFUSE for a NEW hand-kept carrier and :1738 returns WARN for an EXISTING one, so newness alone is the discriminator. The same file already carries the literal at :85, :86 and :102 (grep over the one named file, 7 'cottonwood' hits).",
        "The gate's only sanctioned admission for this shape is the R20 DECLARED EXCEPTION at naming-gate.py:1721-1731, 'THE ONE CONSUMPTION POINT', which needs a waiver entry whose read_context.kind is r20_exception with a register_ref row id, an occurrence count, a cutoff, an owner, and an authority{record,pin} that authority_ok() (:1295) verifies by resolving a full 40-hex pin and finding the ruling id as a whole token in the blob at that pin. CLAUDE.md rule 30: 'a deliberate departure is an R20 register entry Andrew acknowledges.'",
        "CLAUDE.md rule 30 non-application reads 'existing pipelines -- each reaches conformance through its own migration project (R19), never as a rider', and opal-assets/cot_rebalancer_runner is an existing pipeline: the doctrine exempts this edit while the mechanical gate still refuses it.",
        "No declared carrier exists to reference instead: monolith.tf:58-59 declares only locals.monolith_bucket = 'opal-data-assets', and :89 a firms-per-tree map blackdiamond = ['cottonwood']; there is no local holding the cottonwood key prefix.",
        "THE WORLD IS UNTOUCHED AND THE SHARED TREE IS CLEAN. No ledger was opened (nothing began, so an OPEN entry with stranded legs would itself be the drift class). Live get-role-policy cot-rebalancer-runner-write-cot reads 3 statements, no GetObject. The edit was reverted and the revert proven: git diff 0 bytes, 0 occurrences of ReadOwnRunResult in the worktree, and C1 back to its base reading 'IAM-BAD statements granting s3:GetObject: 0 (want 1)'. The refused patch is kept at org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/healgap_r2_1_ReadOwnRunResult_REFUSED_BY_NAMING_GATE.patch (925 B) so the act is one apply away once the call clears.",
        "The apply side would have refused too (safe-apply.sh:183 the naming limb, :262 and :321 BLOCKED), so no bypass of the commit limb would have landed this either."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's own conditions: 'Naming gate REFUSES hand-typed names (rule 30, msg 1355): no new name or address here; a refusal is a missing registry row to report, never a workaround.' Scope 2 gives the statement text verbatim and says 'Touch nothing else. Commit via safe-commit.'",
    "world_is": "There is no missing registry row to add: 'cottonwood' is already a known firm segment, which is exactly why carrier() flags it. The gate wants the literal read through the builder, and Terraform has no such call, so the order as written cannot pass its own stated commit path. Nothing this seat may do clears it: safe-commit --force covers contamination only, never a lane or limb refusal, and an R20 entry needs an authority record Andrew acknowledges. CALL, routed to 2.0.0_SA_COO~G1 and 1.0.0_SA_CTO~DELL1: either (a) land an R20 declared-exception entry for this literal under Andrew's word, (b) rule that rule 30's existing-pipeline non-application admits it and have an authorised seat carry the waiver, or (c) re-cut the act so no new firm-token literal is typed. The order is P1 and must land before ~20:00Z, so the call is time-boxed.",
    "notes": "Reported, not worked around. Distinct from MDPF_HEALGAP-D1-S7/S8, which concern the satellites producer's clock coupling, not the naming limb. The same class will refuse any future new firm-token literal in an existing pipeline's .tf, so the disposition is worth more than this one order."
  },
  {
    "id": "MDPF_HEALGAP-D1-S10",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
    "surfaced_at": "2026-10-09T07:51:06Z",
    "one_line": "R2-1's criterion C5 cannot be exercised from dell1: this box's agent principal holds iam:SimulatePrincipalPolicy only for its OWN ARN, not for cot-rebalancer-runner-role, and iam:SimulateCustomPolicy is absent, so there is no substitute instrument. The IAM change itself LANDED and is verified by C4 on the live principal; only the live-evaluation arm is unrunnable, so the ledger is HELD rather than closed and the order is not flipped complete.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C5 arm 1: 'An error occurred (AccessDenied) when calling the SimulatePrincipalPolicy operation: User: arn:aws:iam::313476888478:user/cloudops-dell1-agent-user is not authorized to perform: iam:SimulatePrincipalPolicy on resource: arn:aws:iam::313476888478:role/cot-rebalancer-runner-role because no identity-based policy allows the iam:SimulatePrincipalPolicy action'.",
        "POSITIVE CONTROL, which is what makes this the instrument and not the world: the SAME action with --policy-source-arn arn:aws:iam::313476888478:user/cloudops-dell1-agent-user returns 'allowed'. The API call works; the grant is RESOURCE-SCOPED to the caller's own principal. An uncontrolled reading of arm 1 would have been indistinguishable from a real deny about the target.",
        "NO SUBSTITUTE INSTRUMENT: iam:SimulateCustomPolicy is also denied ('not authorized to perform: iam:SimulateCustomPolicy on resource: *'), so the policy document cannot be evaluated locally either. sts get-caller-identity confirms the caller is arn:aws:iam::313476888478:user/cloudops-dell1-agent-user.",
        "THE CHANGE IS NOT IN DOUBT. C4 on the live principal reads 4 statements with ReadOwnRunResult = Allow s3:GetObject on arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/meta/*-result.json, DenyBlackdiamond49fFirmSep byte-identical, and a re-plan at the same target reads 'No changes' with -detailed-exitcode rc=0. C1, C2, C3, C4, C7 and C8 all PASS; the proof-of-spec instance grades VALID (rc=0, controls 4 of 4 discriminate).",
        "Ledger 20261009T0732Z_healgap-r2-1-runner-reads-own-result-dell1-20261009 is HELD-SOVEREIGN-GATED with the gate naming the exact action and resource, rendered by deploy_ledger as 'apply legs proven, only verify open; tracked-not-stranded'. L1 and L2 carry proof; only L3 is open. Closing it would be the DRIFT-DANGEROUS shape this seat surfaced on two laptop entries earlier in the same session.",
        "NOT SELF-REMEDIED, deliberately: granting this seat's own principal the action it needs to verify its own work is outside the order's <paths> (which names only cot_rebalancer_runner.tf plus ledger and deliverable surfaces) and is the wrong shape regardless. Recorded as a declared exclusion in the instance."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order ADHOC.healgap-r2-1-runner-reads-own-result C5: '.tools/aws iam simulate-principal-policy --policy-source-arn <role arn> --action-names s3:GetObject --resource-arns <three keys>' expecting 'allowed / implicitDeny / explicitDeny, in that order'. C6 then requires the ledger CLOSED, every leg proven. Both presume the applier's principal can simulate the TARGET role.",
    "world_is": "It cannot, from this box. The dell1 IAM parity grant (ANDREW_DIRECT_20261009_035xZ, ADDENDUM 3 @947dd446e5) gave dell1 its own deploys but not iam:SimulatePrincipalPolicy on other principals, so every WORLD-risk IAM order assigned here will hit the same wall at its verification step, not at its apply step. TWO WAYS TO CLEAR IT, either acceptable: extend the dell1 agent principal with iam:SimulatePrincipalPolicy on arn:aws:iam::313476888478:role/cot-rebalancer-runner-role (or the roles dell1 is given to deploy), or have 2.0.0_SA_COO~G1 grade C5's three arms from a box that holds the action -- the arms must be THREE SEPARATE invocations, because two or more --resource-arns in one call flip the held ones to implicitDeny. Owner of the choice: 1.0.0_SA_CTO~DELL1 with the issuer. The ledger's re-read is the event, not a date.",
    "notes": "Distinct from MDPF_HEALGAP-D1-S9, which was the naming limb refusing the statement's source text and is RESOLVED by ruling H and amendment A1 -- this row is about verifying the grant, not writing it. Worth more than this one order: it is a standing hole in dell1's ability to close the verify leg of any IAM deploy it is given."
  },
  {
    "id": "MDPF_HEALGAP-D1-S11",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
    "surfaced_at": "2026-10-09T08:07:27Z",
    "one_line": "Disposition of MDPF_HEALGAP-D1-S10: amendment A2 @37ce04cf93 SPLIT C5 rather than waiting on the grant -- C5a (the deny arms, read from the live policy documents) graded here PASS 4 of 4, C5b (the allow arm) EXERCISED by the issuer at act 3 on 2026-10-10. R2-1's ledger is CLOSED, 3 of 3 legs proven, and the order is flipped complete. THE UNDERLYING GAP IS NOT CLOSED BY THIS and stays owned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Amendment A2 @37ce04cf93 read VERBATIM at its own pin (9,895 B as the positive control that the pin-and-path read resolves), which is also where the issuer records re-measuring the AccessDenied against the same principal at 08:0xZ -- so the gap in D1-S10 is corroborated by a second seat, not just this one.",
        "C5a: 4 of 4 arms match over ALL FIVE identity-based carriers on cot-rebalancer-runner-role (3 inline + 2 attached managed at their default versions) and 10 statements -- deliberately not scoped to the single policy this order edited, since an Allow in another carrier would falsify an implicit-deny claim. result key -> allowed (only write-cot/ReadOwnRunResult matches); bronze/* key -> implicitDeny (zero matches); complete-stamp -> implicitDeny; 49f key -> explicitDeny (only DenyBlackdiamond49fFirmSep matches). 3 distinct verdicts, so the evaluator discriminates. Reproducible at org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/healgap_r2_1_c5a_identity_policy_eval.py with its captured output.",
        "Ledger healgap-r2-1-runner-reads-own-result-dell1-20261009 CLOSED, all 3 legs proven; verified by three agreeing reads rather than the tool's word -- deploy_ledger check no longer lists the slug (0 occurrences), the sentinel is unlinked, and the entry's tail reads 'CLOSED -- all 3 legs proven'. The entry retains its HELD-SOVEREIGN-GATED interval and its release, so the hold is in the record rather than erased.",
        "WHAT IS STILL TRUE AFTER THIS ROW: iam:SimulatePrincipalPolicy on another principal remains denied to cloudops-dell1-agent-user, and iam:SimulateCustomPolicy is absent. A2 routed around the gap for THIS order; it did not grant anything."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D1-S10 asserted that C5 and C6 could not close from dell1 and that the order could not be flipped. Amendment A2 then re-scoped what this seat owes: 'C5a (closable now, by this seat): the two DENY arms from the LIVE policy document, not a simulation' and 'C6 then closes on C5a'.",
    "world_is": "R2-1 is complete: the grant is live (4 statements, ReadOwnRunResult, 49f Deny byte-identical, re-plan 0-diff), C5a is graded, the ledger is CLOSED and the order reads complete. D1-S10 is therefore RESOLVED as a blocker on this order. It is NOT resolved as a capability gap: the next WORLD-risk IAM order assigned to dell1 will meet the same wall at its VERIFY step, not its apply step, and will need the same split or the grant. TWO REMEDIES, either acceptable, owner 1.0.0_SA_CTO~DELL1 with the issuer: extend the dell1 agent principal with iam:SimulatePrincipalPolicy on the roles dell1 is given to deploy, or make the split standard practice and say so in the order template. Whoever takes the first route: the arms must be THREE SEPARATE invocations, because two or more --resource-arns in one call flip the held ones to implicitDeny.",
    "notes": "DISPOSITION ENUM: UNDER_INVESTIGATION, deliberately, not GRADUATED -- GRADUATED is the CVO's L9 adjudication field (surprise-row-gate.py:119-120, :522-524) and an AE seat setting it would self-grade a judgment that is not its to make; every other row in this channel sits at UNDER_INVESTIGATION for the same reason, including D1-S8 which reported D1-S7's served gap closed. The row text, not the enum, carries the disposition. Resolves D1-S10 rather than re-filing it, the same shape D1-S8 used for D1-S7. D1-S9 (the naming limb) was resolved earlier by CTO ruling H @1af255b7da and amendment A1 @83028dca8a. Both of this order's surprises are now dispositioned."
  },
  {
    "id": "MDPF_HEALGAP-D1-S12",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-11T02:40Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "Act 3's restore chain named two actors and both lived on the box that went down: the induce sat on the production daily target 14h23m past the 06:05Z first-owner moment and 8h28m past the 12:00Z backup deadline, until the laptop CTO restored it at 20:28:38Z under NEVER-2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Ledger healgap-r2-act3-induced-partial-repair-20261010 (opened 2026-10-09T20:14:25Z) names the rollback and the chain: 'MSTR~DELL1 told 20:14Z, owns restore by 12:00Z if this seat is down at 06:05Z'; leg L1 read-back 20:15:19Z shows Input {mode:pull, induce:drop-feed:rebalancer_accounts} on the single target of rule cot-rebalancer-runner-daily.",
        "Ledger leg L3 and commit 5404f51097 (1.0.0_SA_CTO, laptop): live Input read BEFORE the restore still carried the induce; put-targets FailedEntryCount 0 at 2026-10-10T20:28:38Z; read-back Input {mode:pull}. The commit states dell1 seats and MSTR~DELL1 were down since ~23:02Z 2026-10-09 and the 12:00Z deadline was missed.",
        "Andrew-direct record ANDREW_DIRECT_20261010_201xZ_RESTART_COMPILE_STATE_DEPLOYS_THEN_RESIDUE_THEN_INFORM.md quotes that the sitez, dell1 and dell2 boxes hit usage limits 12-24 hours before ~20:1xZ 2026-10-10.",
        "Measured exposure, read 2026-10-11 ~02:2xZ: the daily rule is cron(0 6 * * ? *), so the window held ONE daily fire (06:00Z 2026-10-10); CloudWatch AWS/Lambda cot-rebalancer-runner read for 05Z-15Z only: 06Z 3 invocations 3 errors (induced first attempt + 2 async retries), 11Z 1 invocation 0 errors (the re-attempt target, which carries no induce). 15Z to 20:28Z was not read. The 2026-10-11 06:00Z fire had not yet occurred at the restore, so no second induced fire ran."
      ]
    },
    "spec_asserts": "The act 3 half and ledger assume that at least one of two dell1 actors (2.0.0_SA_COO~G1 at 06:05Z, 0.0.0_AB_MSTR~DELL1 by 12:00Z) is live to restore the daily target input, so an induce on a production target is bounded to hours.",
    "world_is": "Both actors depend on one box and one usage budget; when the box stopped, nothing on dell1 could restore, and the bound became whenever a seat on ANOTHER device read the ledger (14h23m past the first owner moment). The loss was nil here only because the daily rule has one fire per day and the next fire (06:00Z 2026-10-11) came after the laptop restore; a rule with a shorter period, or a restore that landed after the next fire, would have run a second induced day. REMEDY (one, owner 1.0.0_SA_CTO~DELL1 at the next induce): the half of any later induced act names a restore actor on a DIFFERENT device than the seat that sets the induce, with the ledger path it reads, and says so in the ledger's rollback line. Distinct from MDPF_HEALGAP-S12, which is a fail-safe that outlived its kill; this is a fail-safe chain with no member off the failing box.",
    "notes": "No build asked for: this is a wording rule for the half, not a monitor or alert (standing moratorium). UNDER_INVESTIGATION is deliberate, as in D1-S10/D1-S11: GRADUATED is the CVO's L9 field. Act 3's own outcome (PARTIAL read, heal, C5b) is in the R2 drain-end read."
  },
  {
    "id": "MDPF_HEALGAP-D1-W10-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~10",
    "surfaced_at": "2026-10-11T04:03:48Z",
    "one_line": "On the EC2 path the 6d block rewrites one cottonwood gold partition before the slice: dispatch line 554 runs build_dim_model_portfolio.py --upload for the newest silver assignment date. The slice itself writes no gold partition, but the EC2 path is a second writer of the day partition, which the MDPF_HEALGAP-S1 world_is does not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:549-556 at HEAD d08867926c: cot_date is the newest blackdiamond/cottonwood/silver/fact_model_assignment partition; line 554 runs build_dim_model_portfolio.py --date cot_date --upload before the slice at line 556",
        "data/assets/scripts/gold/build_dim_model_portfolio.py:538-542: key = GOLD_PREFIX + dim_model_portfolio/date=<date>/data.parquet, GOLD_PREFIX = blackdiamond/cottonwood/gold/ (line 72), then put_object and head_object",
        "list read 2026-10-11T04:0xZ on opal-data-assets prefix blackdiamond/cottonwood/gold/dim_model_portfolio/: date=2026-10-10 LastModified 2026-10-10T13:30:39Z; the only EC2 launch read is 2026-09-30T13:30:35Z (MDPF_HEALGAP-S1), so the 10-10 launch is UNREAD"
      ]
    },
    "spec_asserts": "MDPF_HEALGAP-S1: which one writes the day's partition is read here. Its world_is says the EC2 slice would re-publish on the newest assignment date only and cannot rewrite a caught-up partition.",
    "world_is": "When the 6d condition holds, the EC2 path re-uploads gold/dim_model_portfolio/date=<newest silver assignment date> before the slice step, so the EC2 path can rewrite a gold partition on the day. Whether that rewrite is byte-identical to the served partition is UNREAD (the builder re-derives from silver on each run). The slice step (line 556) writes only the revamp object and no gold partition.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "MDPF_HEALGAP-D1-W10-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~10",
    "surfaced_at": "2026-10-11T04:03:48Z",
    "one_line": "NOOP for the EC2 slice re-publish is UNKNOWN: the slice writes one fixed key unconditionally, and its body carries a date-derived trading-days field, so a same-day re-run is a no-op only if that field and the staged axis match what is served. No served-bytes comparison was read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:1501: put_object to SLICE_KEY with no skip-if-exists; :1353-1366: trading_days_behind_settled_frontier computed from dt.date.today()",
        "head-object 2026-10-11T04:0xZ on opal-data-assets gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json: LastModified 2026-10-10T13:31:08Z, ETag 50425224d45dc36f6588544bb0525d4d, 162895 bytes; no later write recorded",
        "infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:504-516 and :556: the slice runs after the 6a axis stage of the same run, so its axis input is the EC2 run's own staged copy"
      ]
    },
    "spec_asserts": "TO HG-t-13 NOOP field: YES, NO, or UNKNOWN because a reason, read for whether the EC2 re-publish has the same bytes or keys as what is served.",
    "world_is": "The key is the same on every run, so the key level is a no-op. The bytes are unread: a same-day re-run matches the served object only if the dim partition, the staged axis and the trading-days value all match, and a later run can change the trading-days field. The read that answers it is a GET of the served key diffed against a rebuild with dt.date.today() held fixed, or the ETag of the served key across two consecutive days.",
    "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~7",
    "surfaced_at": "2026-10-11T04:05:10Z",
    "one_line": "HG-t-9's premise says the Cottonwood runner lands bronze after 07:00Z on some days (preflight: after a 12:45Z landing), but the tree's own measured record says it lands 06:00:43-44Z every day.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf @c8f7662637 :269 -- 'landing 06:00:43-44Z EVERY day, from cot-rebalancer-runner-daily cron(0 6 * * ? *)'",
        "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf @c8f7662637 :286 -- the existing rule description: 'Fires 1h after the measured 06:00:43Z upstream landing.'",
        "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf @c8f7662637 :34 -- 'cot-rebalancer-runner-daily cron(0 6 * * ? *) UTC, no timezone'",
        "infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py @c8f7662637 :99 -- 'landing 06:00:43-44Z daily'",
        "Not found in the worktree read for this order: any 12:45Z landing measurement (the TO RECORD FACE preflight cites one). The rule cron(0 6 * * ? *) was not read live (read-only AWS not run for this criterion set)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "HG-t-9 cell: 'On a day the Cottonwood runner lands bronze AFTER 07:00Z the registry serves the previous day'; RECORD FACE preflight: the 13:15Z fire is 'placed after a 12:45Z landing'.",
    "world_is": "The in-tree measured record places the runner's landing at 06:00:43-44Z every day, before the existing 07:00Z fire. The stamp gate is correct as built (it rebuilds only when the stamp exists), but the stated reason for the 13:15Z slot is not supported by any measurement in this tree. The cell's conditional ('on a day ... after 07:00Z') is not contradicted; the 12:45Z figure is unsourced here.",
    "notes": "No build asked for and none changed: the handler and the rule are built to the order's text. Disposition is for the CVO's L9 read of the premise, not this worker's."
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~7",
    "surfaced_at": "2026-10-11T04:05:10Z",
    "one_line": "The completion stamp this cell grants read on, blackdiamond/cottonwood/meta/<date>-complete.json, is the key the runner writes and the silver reader reads, but the key-rulings registry records meta/ as a non-canonical prefix whose canonical form is state/pull_complete/.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/registry/key_rulings.json @c8f7662637 :172-174 -- key 'blackdiamond/cottonwood/meta/' (bucket opal-data-assets, shape prefix), canonical 'blackdiamond/cottonwood/state/pull_complete/', owner 'The opal-assets Cottonwood pull and silver functions (directive D8)'",
        "infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py @c8f7662637 :70 META_PREFIX = SCOPE_PREFIX + 'meta/'; :207-208 _stamp_key -> META_PREFIX + date + '-complete.json' (the writer)",
        "infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/rebalancer_conversion.py @c8f7662637 :417 STAMP_PREFIX = 'blackdiamond/cottonwood/meta/' (the reader)",
        "The HG-t-9 patch (uncommitted in this worktree) adds the grant Resource arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/meta/*-complete.json and the s3:prefix condition blackdiamond/cottonwood/meta/ in the producer role policy"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "HG-t-9 build: the stamp is read at 'meta/<today UTC>-complete.json' under the runner's meta prefix, and the handler derives its prefix from producer.ROSTER_KEY.",
    "world_is": "The grant and the handler encode the live key, which matches writer and reader. The key-rulings registry nonetheless names a different canonical location for it. Any future move of the stamp key must move this grant and the handler's derivation in the same commit; the registry's disposition for the existing key was not read by this worker.",
    "notes": "Observation only. No change to the key is made by this cell."
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~7",
    "surfaced_at": "2026-10-11T04:05:10Z",
    "one_line": "The HG3-t9-AC2 checker (hg_r3_rules.py --t9-iam) passes a ListBucket statement whose Resource is widened to opal-data-assets/*, so the check does not hold the 'nothing wider' clause on the ListBucket resource.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Control run, this worktree: copy of satellites-registry-producer.tf with the ListBucket Resource changed from arn:aws:s3:::opal-data-assets to arn:aws:s3:::opal-data-assets/* (scratch copy .scratch/mut/m4_tf_bare_bucket_star.tf, uncommitted) -> 'T9IAM-OK stamp GetObject + prefix-conditioned ListBucket, nothing wider' rc=0",
        "Control run, same checker, a copy with the s3:prefix condition removed -> 'T9IAM-BAD s3:ListBucket carries no s3:prefix condition' rc=1 (the prefix arm does fire)",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_r3_rules.py t9_iam(): the ListBucket arm tests presence of 'ListBucket' and of the prefix condition only; it does not read the statement's Resource"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "HG3-t9-AC2: 'the role gains GetObject on the stamp pattern and one prefix-conditioned ListBucket and nothing wider'.",
    "world_is": "The checker does not bind the ListBucket statement to the bucket ARN. The applied patch carries the correct bucket ARN, so this worker's tree is right; the gap is in the checker, which is outside this worker's grant and was not edited.",
    "notes": "Not fixed here: the checker belongs to the issuer's R3_CHECKS and the criterion text is unchanged. Recorded so the CVO's L9 read sees that AC2 PASS does not cover the ListBucket Resource."
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~7",
    "surfaced_at": "2026-10-11T04:12:00Z",
    "one_line": "The TO says the naming gate refuses a new hand-kept cottonwood literal; at commit d90794efd4 the gate WARNs on the stamp prefix literal the patch types in satellites-registry-producer.tf:46 and does not refuse it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh output at commit d90794efd4: '[naming-gate] NAMING RAISE-EXISTING infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf:46 blackdiamond/cottonwood/meta/ -> (pre-LGIC key; conformance via its migration project, Rule 30)' and '[naming-gate] NAMING-GATE: WARN 2 graded'",
        "The same gate's stated reason: 'the same literal is already carried at HEAD in data/assets/scripts/silver/rebalancer_conversion.py, so this copy mints nothing: WARN; hand-kept carrier of cottonwood outside every permitted context: read it through lookup(cottonwood)'",
        "infra/aws/terraform/modules/opal_name/generated_locals.tf @c8f7662637 :8 and :31 carry the scope registry as generated data; no generated local for the stamp prefix exists in the module"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "HG-t-9 build text: 'the naming gate refuses a new hand-kept cottonwood literal', so the handler derives the bucket and prefix from producer constants and the rule name is built by opal_name.",
    "world_is": "The handler carries no typed key (it derives the prefix from producer.ROSTER_KEY). The Terraform does carry the literal in locals cot_meta_prefix, because HCL cannot import the Python constant. The gate grades that line as a WARN on a pre-LGIC key, not a refusal. The rule-name line is CONFORMANT as built by name().",
    "notes": "Recorded only: the patch is the issuer's, the refusal clause is not triggered (no refusal), and no name was changed by this worker. Whether the literal should come from a generated local is for the CVO's L9 read."
  },
  {
    "id": "MDPF_HEALGAP-D1-W9-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~9",
    "surfaced_at": "2026-10-11T04:09:27Z",
    "one_line": "HG-t-12 grades the outlook transcripts pull EXPOSED-MANUAL, where round 2 graded it RECOVERS: it and the Teams pull share one gateway Microsoft sign-in, which only a person renews when it lapses. The PRD v0.3 addendum's list of person-renewed pulls names neither.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/NFRA/NFRA_TRNSPT/STATUS.md:82 read at d08867926c: 'gateway sign-in (the laptop's has lapsed; renewing it is a person act)'",
        "infra/aws/lambda/transcripts-pull/mail_handler.py:3-5, :9-10 and infra/aws/terraform/transcripts/pull.tf:27-30 read at d08867926c: the mail and transcript routes both read the gateway bearer and sit on the gateway's sign-in",
        "live list-rules outlook-global-transcripts-pull-daily cron(30 23) and teams-global-transcripts-pull-hourly cron(0 13-22 ? * MON-FRI *) read 2026-10-11T03:59Z-04:09Z; PRD v0.3 addendum (prd/MDPF_HEALGAP_PRD.md:201-203) names four person-renewed pulls and neither"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-6 round 2 graded the outlook pull RECOVERS (its 7-day window refills missed days with nobody acting). The PRD v0.3 addendum names the two canonical-schwab SI2 pulls, schwab-canonical-si2-08403355-pull-daily and astn-wsjft-3am-run as the pulls whose login no machine renews.",
    "world_is": "A missed day on the outlook pull refills with nobody acting only after a person renews the gateway's Microsoft sign-in. The RECOVERS answer and the EXPOSED-MANUAL answer describe the same login at two points in its life. This census grades both outlook and teams EXPOSED-MANUAL for consistency. The CVO rules which answer stands for outlook. Teams is also unbuilt upstream (the gateway transcript tools are not landed; handler.py:9-10 raises GatewayToolsAbsent by design), so its answer rests on source and STATUS, not on a run."
  },
  {
    "id": "MDPF_HEALGAP-D1-W9-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~9",
    "surfaced_at": "2026-10-11T04:09:27Z",
    "one_line": "bd-asset-dim-pipeline-trigger is graded EXPOSED-MANUAL today, but its 49F login is machine-minted at 00:00Z, 04:35Z and 22:20Z. The v0.3 third answer says only a person can renew the login, so the answer grammar does not describe this row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ssm/opal-bd-asset-dim-download.json:3 and :20-24 read at d08867926c: the REST module mints a bearer from the session secret blackdiamond/49f/session that bd-49f-auto-login already maintains",
        "infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py:274-299 read at d08867926c: the full re-mint runs the auto-login OTP when the cookie is not positive-live",
        "bd-49f-keepalive lambda_function.py:12 and :17-18 read at d08867926c: the keepalive extends the session in place and mints no cookie; live list-rules bd-asset-dim-pipeline-trigger cron(10 22 ? * MON-FRI *) read 2026-10-11"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.3 FWD-6: the third answer, EXPOSED-MANUAL, is for a pull whose login only a person can renew. The answer set is RECOVERS, NOT-EXPOSED because <reason>, or EXPOSED-MANUAL because <reason>.",
    "world_is": "A machine renews this login at 00:00Z, 04:35Z and 22:20Z. The keepalive extends it between mints without minting. Nothing machine-side renews between the 04:35Z mint and the 22:10Z fire; the fire has no re-attempt, and its as-of is computed at run time. Read today the row is EXPOSED. The census types it EXPOSED-MANUAL because the grammar has no third exposed value, and it names the person's act (re-capture the cookie if the keepalive reports it dead, then re-run the missed as-of). The CVO rules whether 'only a person can renew' should read 'no machine renews before the pull'. RECOVERS is claimed only by the HG-t-11 re-attempt once applied, and is not claimed here."
  },
  {
    "id": "MDPF_HEALGAP-D1-W9-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~9",
    "surfaced_at": "2026-10-11T04:09:27Z",
    "one_line": "The 49F keepalive's dead-cookie alert tells a person to re-capture the .bd.identity cookie, while the session trigger's full mint re-issues the cookie automatically. The two sources disagree on whether a person renews the 49F login.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/bd-pipeline/bd-49f-keepalive/lambda_function.py:12, :17-18, :22-26 and :128-146 read at d08867926c: the keepalive extends in place and mints no cookie; on 401/403 it publishes 'ACTION (D, ~30s): capture a fresh .bd.identity'",
        "infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py:274-299 read at d08867926c: the full mint with auto-login OTP runs when the cookie is not positive-live"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The 49F rows of the census assume a machine renews the 49F login at 00:00Z, 04:35Z and 22:20Z. The keepalive alert assumes a dead cookie needs a person.",
    "world_is": "Both can hold only if a mint can fail to re-issue a dead cookie. The census grades the 04:35Z-anchored 49F rows NOT-EXPOSED on the mint, and bd-asset-dim EXPOSED-MANUAL on the gap between mints. If the keepalive alert is current, a dead cookie before 06:30Z needs a person and residual R1 is a person's act, not a machine's. The CVO rules which text describes current behaviour."
  },
  {
    "id": "MDPF_HEALGAP-D1-W9-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~9",
    "surfaced_at": "2026-10-11T04:09:27Z",
    "one_line": "The open-calls list that PRD v0.3 names as the place an EXPOSED-MANUAL act is listed when owed has no file path located in this worktree. The census names 1.0.0_SA_CTO's open calls as the place, unverified.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/MDPF/MDPF_HEALGAP/prd/MDPF_HEALGAP_PRD.md:207-208 read at d08867926c: 'where that act is listed when owed (the open-calls list)'",
        "Grep 'open.?call|OPEN_CALLS' under org/missions/D8/MDPF/MDPF_HEALGAP returns the task order and the PRD only; Glob **/*open*call* under org/tier1_exec/1.0.0_SA_CTO returns one logs file (logs/2026-08-24/session_1510-1800Z_open_calls_rulings_49f_program_registered.md), not a standing list"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-6 v0.3: an EXPOSED-MANUAL row names where the person's act is listed when owed (the open-calls list).",
    "world_is": "No standing open-calls file was located, so the 'listed on' cell for the seven EXPOSED-MANUAL rows names a queue this worker could not read. The CVO or 1.0.0_SA_CTO names the file the list lives in. This worker wrote to no list."
  },
  {
    "id": "MDPF_HEALGAP-D1-W8-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~8",
    "surfaced_at": "2026-10-11T04:04:00Z",
    "one_line": "HG3-t11-AC2's checker cannot fail its failed-read arm: a mutant whose guard skips the pull on rc 1 and 2 still prints SSMGUARD-OK, so AC2 is not evidence for the negative arm.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Checker org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t11_assetdim.py@287ef0d2ee lines 107-110 test only 'pull_bd_asset_dim_rest.py' in run['calls'] for rc 1 and 2. Document line 41 (infra/aws/ssm/opal-bd-asset-dim-download.json, staging 'aws s3 cp .../code/bronze/pull_bd_asset_dim_rest.py') writes that substring to the calls log before any guard line runs, so the test is always true.",
        "Mutant .scratch/mutant_always_skip.json (line 80-87 guard test changed from -eq 0 to -ge 0) through the checker's own harness: guard_rc=1 script_rc=0 pull_ran=False; guard_rc=2 script_rc=0 pull_ran=False. Run 'HG_T11_DOC=.scratch/mutant_always_skip.json python hg_t11_assetdim.py --ssm' printed 'SSMGUARD-OK ... rc=0'. The negative arm did NOT fire.",
        "Control .scratch/mutant_noshutdown.json (skip-path 'shutdown -h +2 &' removed) printed 'SSMGUARD-BAD guard read OK but the shutdown was not armed', rc=1: the skip arm discriminates, so the defect is confined to the failed-read arm.",
        "The patched real document through the same harness: guard_rc=0 gives no RUNUSER pull line, SHUTDOWN armed, script rc 0; guard_rc=1 and guard_rc=2 each give 'RUNUSER -l ec2-user -c cd ... python3 data/black_diamond/scripts/bronze/pull_bd_asset_dim_rest.py pull'. The document meets the bar; the invocation does not evidence it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "HG3-t11-AC2 (order MDPF_HEALGAP.TO-HG-t11): the document's own shell, run with the instance's tools stubbed: 'guard read failed (rc 1 and 2) -> the pull runs'. Invocation 'hg_t11_assetdim.py --ssm', expect SSMGUARD-OK. The refusal clause: a criterion that cannot be met as written is a stop and a row, and no check is weakened.",
    "world_is": "The invocation's failed-read arm is satisfied by the staging line, so a regression that makes a failed guard read skip the download still prints SSMGUARD-OK and AC2 cannot gate it. The patched document itself runs the pull on rc 1 and 2 (measured by the same harness). The defect is in the check, not the guard. The checker is outside this order's <paths> grant and was not edited.",
    "notes": "Owner of the fix is the issuer, 2.0.0_SA_COO~G1: a failed-read arm that reads the RUNUSER pull line, as the skip arm reads its SHUTDOWN line. Nothing was sent; no AWS act; the two patches are committed LOCAL on branch wk-MDPF_HEALGAP-8 for the drain, with no apply."
  },
  {
    "id": "MDPF_HEALGAP-D1-W7-S5",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~7",
    "surfaced_at": "2026-10-11T04:59:55Z",
    "one_line": "HG3-t9-AC1 does not fail on the tree the order starts from: hg_r3_rules.py --t9 prints T9-OK rc=0 on the v1 satellites tf, so the order's sentence 'All three FAIL at the base' is not true of AC1 at the start tree; AC1 does not discriminate the v2 patch.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Control run, this worktree: git show 85fe77beb7:infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf saved to .scratch/ctl/base.tf (uncommitted); 'python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_r3_rules.py --t9 .scratch/ctl/base.tf' -> 'T9-OK new_rule=cot_satellites_registry_producer_stamp_gated schedule=cron(15 13 * * ? *) existing=cot_satellites_registry_producer_daily cron(0 7 * * ? *)' rc=0",
        "git diff --stat 85fe77beb7 9ab36371f1 lists no satellites-registry-producer file, so the blob above is the start tree's pre-patch Terraform at commit 9ab36371f1",
        "The same start-tree controls: --t9-iam on that blob -> T9IAM-BAD rc=1; hg_t9_stamp_gate.py with HG_T9_HANDLER on the 85fe77beb7 handler blob -> GATE-BAD rc=1. AC1 is the only one of the three criteria that passes on the start tree",
        "org/missions/D8/MDPF/MDPF_HEALGAP/task-orders/MDPF_HEALGAP.TO-HG-t9.satellites-second-fire-stamp-gated.md@9ab36371f1 line 78: 'All three FAIL at the base'; lines 44-46 state the tree already carries the round-3 v1 change merged at 85fe77beb7"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "HG-t9 TO line 78: 'All three FAIL at the base (T9-BAD ..., T9IAM-BAD ..., GATE-BAD ...)'; HG3-t9-AC1 expects T9-OK on the rule's presence and schedule.",
    "world_is": "At the start tree the T9 rule check already passes without the v2 patch (the rule was merged at v1). AC1 therefore gives no signal on the v2 change; AC2 and AC3 do fail on the start tree as the order states.",
    "notes": "Recorded only: the order's sentence is quoted, not corrected. The AC1 PASS on the patched tree is correct for the rule but is not evidence that this cell's v2 patch changed the rule. For the CVO's L9 read."
  },
  {
    "id": "MDPF_HEALGAP-D1-W11-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~11",
    "surfaced_at": "2026-10-11T13:25:59Z",
    "one_line": "The top-of-file WHY block of satellites-characteristics-producer.tf (lines 34-35) names the registry producer's cron(0 7 * * ? *) rule as this trigger's anchor. The file's finality input, holdings.json, is final only at the stamp-gated cron(15 13 * * ? *) fire, which that block does not mention. Outside the three edits HG-t-14 names; not edited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf lines 34-35 at 60ee1f8f3d: the anchor is 'cot-satellites-registry-producer-daily   cron(0 7 * * ? *)   UTC'",
        "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf lines 304-307 (cot_satellites_registry_producer_daily, cron(0 7 * * ? *)) and lines 334-337 (cot_satellites_registry_producer_stamp_gated, cron(15 13 * * ? *)) at 60ee1f8f3d; hg_t14_schedule.py printed stamp_gated=cron(15 13 * * ? *)",
        "Worktree edit for HG-t-14: schedule_expression changed to cron(25 13 * * ? *); the top-of-file block was left as found"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The file's top-of-file WHY block: this trigger's anchor is the registry producer's daily UTC cron at 07:00Z, so a constant UTC margin holds to a UTC-cron upstream.",
    "world_is": "The registry producer still carries the 07:00Z daily rule, and holdings.json is final only at the stamp-gated 13:15Z fire. The block names only the 07:00Z rule, so it does not describe the input this trigger now clears. The UTC-cron reasoning itself still holds.",
    "notes": "Recorded only; no edit made. The CVO or the issuer decides whether the top-of-file block is re-worded in a later cell."
  },
  {
    "id": "MDPF_HEALGAP-D1-S13",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-11T13:42Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "safe-apply's seat gates ran in WARN mode on this seat's round-3 applies and printed APPLY-WHO verdict=REFUSED ('a COO does not apply') and CROSSBOX-DEPLOY verdict=STOP; both would stop the act under ENFORCE, and the signed halves name this COO as the acting seat.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-apply output of the HG-t-14 apply (cot-pipeline, 2026-10-11 ~13:3xZ), lines 1-4: '[seat-gates] mode=WARN APPLY-WHO serial=2.0.0_SA_COO~G1 kind=COO root=cot-pipeline verdict=REFUSED reason=a COO does not apply; it cuts or spawns, a CLOUDOPS or TIER2 seat applies'; 'OPEN-DEPLOY: open deploy secclass-cot-repoint-m-20261002 (author 2.0.0_SA_COO~M, status OPEN, opened 2026-10-02T05:40:50Z) names the root (token cot-pipeline)'; 'would stop under ENFORCE ( apply-who crossbox-deploy ); WARN mode proceeds.'",
        "safe-apply output of the HG-t-5 apply (opal-assets, 2026-10-11 13:41Z), lines 1-4: the same APPLY-WHO REFUSED line with root=opal-assets and 'OPEN-DEPLOY: open deploy adhoc-partner-roster-t1 (author 0.7.0_AE_CloudOps~DELL1, status OPEN, opened 2026-10-09T02:21:29Z) names the root'.",
        "Each plan was a saved one-target plan reading only the rule named by the signed half (HG-t-14: 0 add 1 change; HG-t-5: 0 add 1 change); neither open deploy's resources were in either plan.",
        "The two earlier applies of this round (bd-pipeline act 3, cot-pipeline act 1) went through the same wrapper; this seat's reading of their output was filtered and tailed, the seat-gate lines were not read, and the same gate is presumed to have printed the same WARN (NOT verified)."
      ]
    },
    "spec_asserts": "The never-widen halves for round 3 name 2.0.0_SA_COO~G1 on dell1 as the acting seat for each apply (R2 act 1's pattern) and the CTO signed them; the apply step of each half reads 'the targeted plan reads exactly ...' as the only condition at apply time.",
    "world_is": "The wrapper's APPLY-WHO gate holds a rule that a COO does not apply and a CloudOps or Tier-2 seat does; it is in WARN, so four applies landed. Under ENFORCE they would each stop at APPLY-WHO and at CROSSBOX-DEPLOY (an open deploy by another seat naming the same root). No harm is measured: every plan was one rule. What is open is which seat applies a signed half's act, and whether an open deploy by another seat that names the root should hold a targeted one-rule apply. REMEDY (owner 1.0.0_SA_CTO~DELL1): rule which seat applies in the halves that follow (the retirement pair for the 07:00Z rule and HG-t-10), and either seat a CloudOps lane for the apply or have the half name the COO as acting seat with the gate's mode ruled; this seat does not choose.",
    "notes": "Recorded and disclosed, no edit to the gate. The gate lines were in the output of every apply; this seat should have read them at the first apply, not the fourth. UNDER_INVESTIGATION is deliberate: GRADUATED is the CVO's L9 field."
  },
  {
    "id": "MDPF_HEALGAP-D1-W12-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~12",
    "surfaced_at": "2026-10-12T13:33:31Z",
    "one_line": "The LGIC root map still registers cot-satellites-registry-producer-daily as an EVENT_RULE name (system posn, root_map.json line 264). After HG-t-15 no tf resource declares that rule, so the registry row names a rule the tree no longer carries. Recorded only; the registry is outside this cell's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/registry/root_map.json lines 263-268 at 0d488da900: the row name cot-satellites-registry-producer-daily, type EVENT_RULE, system posn, evidence 'the rule fires that producer. Decided by 4.0.0_SA_CRO 2026-10-07; no row existed.'",
        "Grep of infra/ in the worktree after the HG-t-15 edit: the name occurs only at infra/logic/registry/root_map.json:264 and as a comment at infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf:35 (the anchor block already filed as MDPF_HEALGAP-D1-W11-S1); no aws_cloudwatch_event_rule declares it after the edit",
        "infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf after the HG-t-15 edit: the daily rule, target and permission are removed; module stamp_gated_rule_name and the stamp-gated resources are unchanged"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The LGIC root map row at line 264 records cot-satellites-registry-producer-daily as a decided EVENT_RULE name for the posn system, the rule that fires the registry producer.",
    "world_is": "The rule is retired by MDPF_HEALGAP.TO-HG-t15 and no tf declares it, but the root map row remains. The registry does not state whether a retired rule keeps its row.",
    "notes": "Recorded only; no edit to the registry. The CVO decides at L9 whether the row is retired with the rule."
  },
  {
    "id": "MDPF_HEALGAP-D1-S14",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-13T11:42:13Z",
    "one_line": "The HG-t-10 half's acceptance text and its healed check predicted accounts healed_at null after the repair; the live result reads a timestamp, which is what the producer's own rule writes. The expectation was mine and was wrong; the check printed HEALED-BAD on that one condition and no other.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T10_FWD3_EXERCISE_20261012.md section 5 item 3: 'healed_at on accounts reads null live (the R2-1 rule)'; hg_t10_exercise.py cmd_healed flags any non-null healed_at",
        "infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py lines 276-278: healed_at = prev healed_at, and 'if prev.get(status) == missing and feed in landed_now: healed_at = now_iso'",
        "live read 2026-10-13T11:42:13Z: meta/2026-10-13-result.json verdict COMPLETE, rebalancer_accounts status arrived, healed_at 2026-10-13T11:41:17Z; hg_t10_exercise.py healed printed 'HEALED-BAD accounts healed_at is 2026-10-13T11:41:17Z' with no other condition listed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The half (CTO ADDENDUM 7 signed it) says the healed feed's healed_at reads null live after the repair.",
    "world_is": "healed_at carries the repair's invoke time, as lambda_function.py lines 276-278 write it for a feed an earlier result marked missing that lands in a later run. The served outcome (COMPLETE, stamp, accounts keys, the two present feeds' key sets equal to the pre-repair snapshot) is as the half intended; only the predicted field value was wrong.",
    "notes": "The check script is left as run (not edited to pass). L6 is graded at 12:45Z by the producer's rule with this deviation stated; the CVO decides at L9 whether the half's text is corrected."
  },
  {
    "id": "MDPF_HEALGAP-D1-S15",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-13T11:42:13Z",
    "one_line": "During the HG-t-10 exercise the Black Diamond API answered HTTP 401 to the runner four times between 11:35:58Z and 11:39:29Z (one GET of a model, two POSTs to strategies/search on the repair); the repair's third attempt at 11:41:17Z succeeded. The half expected the repair to land on its first invoke.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cot-rebalancer-runner log 2026-10-13: 11:35:58Z RuntimeError 'BD GET /api/models/<id> -> HTTP 401' (induced retry 3); 11:38:29Z and 11:39:29Z RuntimeError 'BD POST /api/models/strategies/search -> HTTP 401' (repair invoke and its first async retry); 11:41:17Z START then 11:41:34Z verdict BRONZE-COMPLETE models 71 accounts 993 model_details 93",
        "the 11:32:36Z and 11:33:51Z attempts of the same day reached the vendor and raised PartialDay as designed, so the session was valid at 11:32Z and again at 11:41Z"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The half says the vendor session is valid at 11:32Z and the repair closes the hole before 11:45Z.",
    "world_is": "The session answered 401 for roughly 11:35Z-11:40Z and was valid again at 11:41Z; the repair closed the hole at 11:41:34Z, inside the 11:45Z bound, by its second async retry. The cause (token expiry window, vendor rotation or another puller) is not read.",
    "notes": "Not chased. The 12:45Z fire is the safety if a later run meets the same window. No code or config touched."
  },
  {
    "id": "MDPF_HEALGAP-D1-S16",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~G1",
    "surfaced_at": "2026-10-13T13:33:21Z",
    "one_line": "The 13:25Z characteristics producer fire failed three times on 2026-10-13 with NoSuchKey on bbg/2026-10-12/characteristics.parquet in opal-data-etfs; the Bloomberg T-1 partition is absent at 13:33Z. The served characteristics.json stays the 2026-10-12 version. The cause is upstream of this project and not the HG-t-10 exercise.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cot-satellites-characteristics-producer log 2026-10-13: START 13:25:14Z, 13:26:29Z, 13:28:23Z each ending '[ERROR] NoSuchKey: ... GetObject' from producer.main (lambda_function.py line 87)",
        "data/assets/scripts/gold/build_satellites_characteristics.py lines 144-146 and 246-250: the T-1 read is s3://opal-data-etfs/bbg/<T-1>/characteristics.parquet then run_manifest.json; lib.trading_calendar.prev_trading_day(2026-10-13) = 2026-10-12",
        "head-object 2026-10-13T13:33:21Z: bbg/2026-10-12/characteristics.parquet 404; bbg partitions present through 2026-10-09 (list with delimiter); bbg/2026-10-09/characteristics.parquet LastModified 2026-10-12T11:03:03Z (positive control)",
        "inputs that exist: opal-data-cot/platinum/satellites/holdings.json LastModified 2026-10-13T13:15:49Z (as_of 2026-10-13); opal-data-portal-v2/json/positioning/positioning_data.json LastModified 2026-10-10T11:06:06Z; served characteristics.json LastModified 2026-10-12T13:26:03Z"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The HG-t-10 half step 6 and the HG-t-14 retime say the 13:25Z fire runs after its inputs land and serves holdings_as_of == as_of for the day.",
    "world_is": "Today's Bloomberg T-1 partition had not landed by 13:33Z, so the scheduled fire failed three times and the day serves the prior day's characteristics, as any failed day did. Whether the Bloomberg pull for 2026-10-12 failed, is queued or runs later is not read; Bloomberg pulls go only through their queue and are not this seat's.",
    "notes": "No manual re-invoke: a run off the producer's own clock needs a never-widen half. Not caused by the exercise (it touched rebalancer bronze, silver and the sentinel target only). The CVO takes it at L9 with D1-S14 and D1-S15; a re-run on the partition's arrival is the CTO's call."
  },
  {
    "id": "MDPF_HEALGAP-D1-W14-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~14",
    "surfaced_at": "2026-10-13T14:30:00Z",
    "one_line": "The round-3 census says the deployed Teams transport is a stub that raises GatewayToolsAbsent by design, so no run has completed. At HEAD the deployed Lambda passes a bearer and makes a live GET; GatewayToolsAbsent is raised only when no bearer is passed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/transcripts-pull/handler.py:41-42 read at HEAD: the gateway arm reads the bearer from Secrets Manager and returns GatewayTransport(base_url, bearer=bearer)",
        "data/transcripts/scripts/teams/gateway_client.py:221 read at HEAD: _token raises GatewayToolsAbsent only when no bearer is held; :224-228 the _get performs the live GET with the bearer",
        "infra/aws/lambda/transcripts-pull/handler.py:9-10 read at HEAD: the docstring still says the gateway transport is the stub that raises GatewayToolsAbsent (stale wording)",
        "data/transcripts/scripts/teams/pull.py:318-321 read at HEAD: the stub message is the CLI no-bearer path (GatewayTransport() with no bearer)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round-3 census teams row: as deployed the transport raises GatewayToolsAbsent by design, so no run has completed and the answer rests on source and STATUS, not on a run (cites handler.py:9-10).",
    "world_is": "The deployed handler builds a live transport with a bearer, so the stub is the no-bearer CLI path and the docstring is stale. Whether the gateway route answers 200 or 503 needs_login was not read (no vendor call). The teams disposition in FWD6_SEVEN_DISPOSITIONS_R4.md is NAMED-REASON on the needs_login path, not on the stub.",
    "notes": "Not chased. Read-only grading only; no code touched. The docstring fix is the owner's, not this worker's."
  },
  {
    "id": "MDPF_HEALGAP-D1-W14-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~14",
    "surfaced_at": "2026-10-13T14:30:00Z",
    "one_line": "The census names the act that refills the SI2 standing session for the three SDD pulls as the run-capture.ps1 task SchwabSddCapture. That task writes Secrets Manager schwab/sdd/session; the puller reads Credential Manager SDDSecure, and no in-repo code writes SDDSecure.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1:229 read at HEAD: CredReadW('SDDSecure') is the credential the puller reads; :270-272 says a human must re-establish the session on the box",
        "infra/aws/ec2/canonical-schwab-si2/schwab_sdd_session_capture.py:8 and :10 read at HEAD: the capture writes a session blob to Secrets Manager (schwab/sdd/session) and never drives a login",
        "infra/aws/ec2/canonical-schwab-si2/run-capture.ps1:29 read at HEAD: schtasks /Create /TN SchwabSddCapture runs the capture as the Administrator console user",
        "Grep of infra/aws/ec2/canonical-schwab-si2 at HEAD for CredWrite, cmdkey and SDDSecure returns only reads of SDDSecure (sdd-daily-pull.ps1, sdd-backfill-08335338.ps1); no writer"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round-3 census rows for schwab-canonical-si2-08403355, 08242234 and 08335338 name the act as re-establishing the SI2 standing session via run-capture.ps1 task SchwabSddCapture.",
    "world_is": "In repo code the capture task refreshes Secrets Manager, not the SDDSecure credential the puller reads. The act that writes SDDSecure is not in the repo. The SI2 desktop sign-in is the person's act the capture reads; whether the named task refreshes SDDSecure is not read here. The three rows stay NAMED-REASON on sdd-daily-pull.ps1:272, with the named act corrected in their because-cells.",
    "notes": "No AWS act. The CVO or the owner of the SI2 box names the act that writes SDDSecure."
  },
  {
    "id": "MDPF_HEALGAP-D1-W14-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~14",
    "surfaced_at": "2026-10-13T14:30:00Z",
    "one_line": "The task order's example row for astn-wsjft-3am-run grades NAMED-REASON on the premise that the next 3 AM run reads the new cookie. The code gives no catch-up for a missed day, so the pull does not refill and the disposition is RE-ATTEMPT-DESIGNED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tools/astn_wsjft/scripts/run.py:88 and :144 read at HEAD: _fresh keeps articles published within 12 hours of now, and the run applies it to the raw set",
        "tools/astn_wsjft/scripts/run.py:133 read at HEAD: a failed FT fetch is a warning, and no retry is scheduled",
        "tools/astn_wsjft/ARCHITECTURE.md:58 read at HEAD: the session is harvested out-of-band by harvest_ft_session.js when it expires"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's example row: a failed FT fetch is a warning and the next 3 AM run reads the new cookie (tools/astn_wsjft/scripts/run.py:53), which the order presents as a NAMED-REASON shape.",
    "world_is": "The next run reads the new cookie going forward, but a missed day is not refilled: the 12-hour window and the absence of any lookback drop the missed window's articles. A pull that does not refill is RE-ATTEMPT-DESIGNED under the order's own rule.",
    "notes": "The example row was a shape, not an answer, as the order says. The disposition in FWD6_SEVEN_DISPOSITIONS_R4.md is RE-ATTEMPT-DESIGNED with the design written in the row."
  },
  {
    "id": "MDPF_HEALGAP-D1-W14-S4",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~14",
    "surfaced_at": "2026-10-13T14:30:00Z",
    "one_line": "infra/aws/terraform/transcripts/pull.tf says it is DESIRED ONLY and never applied, but the teams-global-transcripts-pull-hourly rule is live and ENABLED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/transcripts/pull.tf:1-3 read at HEAD: this file is planned, never applied by the order that wrote it",
        "aws events describe-rule --name teams-global-transcripts-pull-hourly read 2026-10-13 (read-only): State ENABLED, cron(0 13-22 ? * MON-FRI *); outlook-global-transcripts-pull-daily also ENABLED, cron(30 23 * * ? *)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "pull.tf header: the clock and writer are planned and not applied; the apply is a later release act with a change-management entry.",
    "world_is": "The live rule exists and is ENABLED. Either the apply happened outside this file's history or the header is stale. Which is true was not read further.",
    "notes": "Not chased. The disposition of the teams row does not depend on the header."
  },
  {
    "id": "MDPF_HEALGAP-D1-W13-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~13",
    "surfaced_at": "2026-10-13T14:26:31Z",
    "one_line": "HG-t-16's code commit is refused by the naming limb (LGIC_ENFORCE, ENFORCE mode): the reattempt rule's printed name etfs-cot-satellites-characteristics-producer-reattempt-hourly is a HOLE because its cadence cannot be read from cron(25 14-23 * * ? *), so the hole-count ratchet for infra/aws/terraform/cot-pipeline grows 0 -> 1.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "base 011fd686a8: satellites-characteristics-producer.tf has one rule (cron(25 13 * * ? *)); worktree C:/dev/wk_healgap_r4_13 carries org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R4_PATCHES/t16_characteristics_tf.patch and t16_handler.patch applied, UNCOMMITTED, both files passed git apply --check first",
        "safe-commit.sh on the two code files (lambda_function.py, satellites-characteristics-producer.tf) ABORTED at the naming limb: 'NAMING REFUSE infra/aws/terraform/cot-pipeline:0 <hole-count-ratchet> -> -'; 'New: HOLE EVENT_RULE etfs-cot-satellites-characteristics-producer-reattempt-hourly -> partial form etfs-cot-satellites-characteristics-producer-reattempt-{cadence}; could not fill {cadence}: hour field 14-23: more than once a day, not a list of single hours: not a fixed interval [infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf:434]'; 'NAMING-GATE: REFUSE 3 graded'; 'Commit aborted; files unstaged.'",
        "same gate run: 'NAMING CONFORMANT infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf:425 etfs-cot-satellites-characteristics-producer-reattempt-hourly ... built by name() at the call site: CONFORMANT as SCHEDULE'; the S3Key WARN at tf:178 (platinum/satellites/characteristics.json) is on an EXISTING line and is not a refusal",
        "after the abort: git rev-parse HEAD = 011fd686a8, git diff --cached empty, both code files show as modified in the worktree only"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order names the rule's printed name as opal_name builder output (rule 30): etfs-cot-satellites-characteristics-producer-reattempt-hourly; its refusal clause says a gate refusing a name is a stop, written as a surprise row, with no check weakened.",
    "world_is": "The naming limb cannot decide the cadence of a multi-hour window (14-23) and refuses the new name as a hole; the ratchet refuses growth. The HCL the criteria grade (AC1-AC3: T16-OK, T16IAM-OK, GATE-OK on the worktree; T16-BAD, T16IAM-BAD, GATE-BAD on base copies) lands through no commit, so the reattempt cannot reach the drain from this branch as written.",
    "notes": "Not worked around: no --force, no GIT_COMMIT_AUTHOR_OVERRIDE, no edit to the schedule expression or the name (AC1 names cron(25 14-23 * * ? *) and the printed name), no edit to any check. The uncommitted diff stays in the worktree for the COO. Owed from the naming-rule owner: a schedule the cadence reader decides (the gate prints 'not a list of single hours'), or a name that ends in the cadence word. Disposition for the COO and the CVO at L9; the two files are the only code change."
  },
  {
    "id": "MDPF_HEALGAP-D1-W15-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_MDPF_HEALGAP~15",
    "surfaced_at": "2026-10-13T17:36:07Z",
    "one_line": "tools/astn_wsjft/scripts/store.py at base carries an unused 'import re' that ruff F401 refuses, so the universal commit gate blocked the issuer's reference patch from being committed as delivered; the one-line import removal is in commit 1eaea051c4.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tools/astn_wsjft/scripts/store.py:9 read at fe216d8d06 (git show HEAD:path): 'import re' and no 're.' use anywhere in the file",
        "ruff check --select F401 on git show fe216d8d06:tools/astn_wsjft/scripts/store.py (scratch copy): Found 1 error, re imported but unused",
        "safe-commit of 3 code files before the fix: commit-gate BLOCKED ruff check failed on tools/astn_wsjft/scripts/store.py; after the fix: commit-gate clean for 3 of 3 file(s), commit 1eaea051c4 LOCAL on wk-MDPF_HEALGAP-15"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's build step applies the issuer's t18_tools.patch unchanged and runs the two criteria; a patch that does not apply or a criterion that reads BAD is a stop, written as a surprise row, with no check weakened.",
    "world_is": "Both patches applied cleanly and both criteria read GATE-OK on the patched tree. The commit gate (universal, fail-closed, --force does not bypass) then refused store.py on a lint defect that predates the patch. The fix is one unused import line in a file the grant names; no behaviour changed, and the gates were re-run GATE-OK (rc=0) after it. Owed to the issuer: the patch set as delivered does not pass the commit gate at base, so the drain should expect this one-line delta.",
    "notes": "Not worked around by --force or GIT_COMMIT_AUTHOR_OVERRIDE. No check edited. A mutant control (dedupe removed in a scratch copy via HG_T18_RUN) fired GATE-BAD F and rc=1, so arm F is live."
  }
]
```
