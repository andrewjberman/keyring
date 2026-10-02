# ETFS_RIVALS task order -- `RIV-pv-1` -- ROUND 7 (ENRICHMENT): A RUN CARRIES ITS TRIGGER: run_path "scheduled" ONLY FROM THE SCHEDULE (CTO ruling 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-pv-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~21:3xZ, --drift) -- carrier C1 PARTIAL inside the 90 s budget (446 of 65,153 files scanned, 0 gates armed); C2-C6 not scanned (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes; the schedule INPUT changes (gen_policies.py -> generated.auto.tfvars.json), applied by the issuer's deploy
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 7** makes the 09:00 ET sweep run the AI step itself (round 6 left no scheduled path to it), makes every run carry its trigger, has the census read the rankings' classification and agree with the header, gives one deterministic name per security, asks Bloomberg for the CUSIP lines' names, and carries the page-walk remainder (PRD v0.13). Nothing in round 7 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-pv-1` -- a run carries its trigger: `run_path` "scheduled" only from the schedule (CTO ruling 3)
- The sweep schedule's input in `gen_policies.py` gains `"run_path": "scheduled"`, regenerated into
  `generated.auto.tfvars.json`.
- The sweep stamps "scheduled" only for an event carrying that value and no `only`. Every other event stamps "ad_hoc":
  an `only` fire, or a hand-made event.
- `run_path` goes into each account row's `input_manifest` and into `research_hypotheses_run`.
- A seat replaying the schedule payload verbatim still stamps "scheduled", and the docstring says so.
- **Organic trigger:** the same schedule. Its payload is the evidence.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff))

- The 09-30 manifest said run_path "scheduled" for an `only` fire; that is how ap-1's FAIL hid (CTO ruling 3: a value must carry its claim). The stored 09-30 object is NOT rewritten; the claim is corrected forward.
- Interface: the sweep schedule's input in gen_policies.py gains "run_path": "scheduled", regenerated into generated.auto.tfvars.json (`python infra/aws/terraform/etfs-rivalfunds/gen_policies.py --out infra/aws/terraform/etfs-rivalfunds`); the sweep stamps "scheduled" only for an event carrying that value and no `only`; every other event stamps "ad_hoc"; run_path goes into each row's input_manifest and into research_hypotheses_run. State in the docstring: a seat replaying the schedule payload verbatim still stamps "scheduled".
- Never run terraform; the issuer applies.
- Organic trigger: the same EventBridge schedule; its payload is the evidence.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/` and rounds 5-6's `.../round5/checks/`, `.../round6/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.13), the round-6 analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round6.md`, the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-7 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r7pv1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/ai_stage.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/tests/test_r7pv1_*.py
infra/aws/terraform/etfs-rivalfunds/gen_policies.py
infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- an only:[publish-page] fire stamps run_path ad_hoc on the rows and the manifest; the schedule's own payload stamps scheduled on both; a hand-made sweep event without run_path stamps ad_hoc (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/pv-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-pv-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round7/checks/pv-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-pv-1.run-path-carries-trigger.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-pv-1.run-path-carries-trigger`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-6 analysis @94f682c868 (CTO~Z msg 28735) section 3 + the RFW register
graded against rv-publish-1002r6; decomposition round 7 v1.0; Andrew-direct max parallelization (cooRV record 141xZ). Chain `~1`, slot `~1`, position 2 of 2 (sa-1 -> pv-1). Checks dry-run at base CLOUD 50761d39e9 (the package equals the deployed pin eb6e9f04ff):
pv-1.AC1 FAIL (4; arm 2's row limb PASSes) as expected; PASSES under the in-memory fix.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>7</round>
<slot>~1</slot>
<fabric>site-z</fabric>
