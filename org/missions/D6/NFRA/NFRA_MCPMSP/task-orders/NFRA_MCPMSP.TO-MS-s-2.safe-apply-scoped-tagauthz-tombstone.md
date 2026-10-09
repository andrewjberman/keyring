# NFRA_MCPMSP task order -- `MS-s-2` -- ROUND 3, E1: safe-apply's tag-authz and tombstone stages grade the plan the apply runs

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-s-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPMSP.TO-MS-s-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPMSP~8</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a local gate script; the test uses a fake terraform and fake gates on a scratch root.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1's base-bytes run is the adversary read.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-s-2` (decomposition ROUND 3, R3.2; the CTO's round-2 analysis item E1, row NFRA_MCPMSP-Z-W7-S1)

`.tools/safe-apply.sh` (read it whole first; the last commit to touch it is `95d53e2068`) wraps `terraform apply` in
several gates. Round 2's cell MS-s-1 made the NAMING PLAN stage grade the plan the apply actually runs: the caller's
args are parsed once (`:200-229`, variables `SA_TARGETED`, `SA_PLANFILE`, `SA_PLAN_ARGS`, `SA_SCOPED`), and for a SCOPED
apply (any `-target`, or a positional planfile after `apply`) the naming plan stage (`:274-323`) runs
`plan -input=false -lock=false <caller's -target/-replace/-var/-var-file/-refresh/-destroy> -out=<tmp>` then `show -json`,
or `show -json <planfile>` with no re-plan.

The defect this cell fixes (measured): two LATER plan-reading stages still re-plan the WHOLE tree with none of the
caller's args, so for a scoped apply they grade a plan the apply does not run:
- the TAG-AUTHZ stage (`:326-465`; it runs only when the tree sets a provider `default_tags` block): `:426-427`
  `plan -input=false -lock=false -out="$TAG_TMP.bin"` then `show -json`, then `comp-tagauthz check --default-tags-tree
  <tree> --from-plan <json>`; a non-zero rc BLOCKS;
- the TOMBSTONE stage (`:468-507`): `:490-491` the same whole-tree plan, then `python tombstone-gate.py --plan-json <json>
  --register <tombstones.json>`; a non-zero rc BLOCKS (`exit "$TS_RC"`).

Build:
1. **`.tools/safe-apply.sh`:** for a SCOPED apply, the tag-authz and tombstone stages grade the SAME plan JSON the naming
   plan stage renders for that apply (render it once and hand it on, or render it the same way -- your choice; one
   render is preferred). Their verdict logic, messages, overrides (`TAGAUTHZ_OVERRIDE`, `TOMBSTONE_OVERRIDE`), audit
   lines and their existing behaviour when a plan cannot be produced stay as they are. An UNSCOPED apply (no `-target`,
   no planfile) is byte-for-byte today's behaviour in both stages. Touch no other stage.
2. **`.tools/tests/test_safe_apply_scoped_gates.sh` (new):** the self-test. It runs the script named by env
   `SAFE_APPLY_UNDER_TEST` (default `.tools/safe-apply.sh`) as a COPY placed in a SCRATCH ROOT (a temp dir laid out as
   `<root>/.tools/safe-apply.sh`, `<root>/.tools/comp-tagauthz` (a fake), `<root>/.tools/tombstone-gate.py` (a fake),
   `<root>/infra/aws/terraform/tombstones.json`, a temp tree with a provider `default_tags` block), with
   `SAFE_APPLY_TERRAFORM` pointed at a FAKE terraform that records its argv and, for `show -json`, writes a plan JSON
   whose resources depend on what was planned: a WHOLE-TREE plan (no `-target`) carries a marker resource `TRIP`, a
   targeted plan carries only the targeted addresses, and a planfile's JSON is whatever the arm wrote into it. The fake
   gates refuse (non-zero) exactly when the JSON they are handed contains `TRIP`. Isolate every other gate of the copied
   script (halt checkpoint, naming stages, seat/apply-who gates, and any `org/mcp/*.enforce` switch) by its own env
   switch or by the scratch root's own files -- never by editing the script under test, and never by reading the main
   tree's `org/mcp/` (a `naming-place.enforce` switch is announced to land on CLOUD during this round). It prints one
   line per arm -- `PASS: <arm>` or `FAIL: <arm>` -- then `RESULT: PASS` only when all six pass:
   - `tagauthz_targeted_grades_own_plan` -- `apply -target=A`, full-tree plan carries `TRIP`, the targeted plan does not:
     the tag-authz stage passes and the fake records `apply`;
   - `tagauthz_targeted_refuses_own_plan` -- `apply -target=TRIP`: the tag-authz stage blocks, NO `apply` recorded;
   - `tombstone_targeted_grades_own_plan` -- as the first arm, for the tombstone stage;
   - `tombstone_targeted_refuses_own_plan` -- as the second arm, for the tombstone stage;
   - `planfile_stages_read_given_planfile` -- `apply plan.bin` whose JSON has no `TRIP` while the full-tree plan does:
     both stages pass, the fake records `show -json plan.bin` and NO whole-tree `plan` for either stage;
   - `unscoped_apply_unchanged` -- an untargeted apply with `TRIP` in the full-tree plan: the tag-authz stage blocks (as
     today), NO `apply` recorded.
   Bound the whole test so it finishes inside 50 seconds.

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. `.tools/comp-tagauthz`, `.tools/tombstone-gate.py`,
   `.tools/naming-apply-gate.py`, `.tools/tests/test_safe_apply_targeted.sh` and `infra/aws/terraform/tombstones.json`
   are read-only (the test uses its own fakes and copies).
2. Never run safe-apply against a real tree or real terraform. No push, no vendor call, no AWS call. REFUSE a criterion
   you cannot meet as written.
3. After your change, `.tools/tests/test_safe_apply_targeted.sh` (MS-s-1's five arms) must still print `RESULT: PASS`;
   report its line.

## 3. SURFACES

<paths>
.tools/safe-apply.sh
.tools/tests/test_safe_apply_scoped_gates.sh
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~8/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: the read-only files in BOUNDS 1, `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round3/checks/`.
Rows: `INVESTIGATION_v1.Z.md`, id `NFRA_MCPMSP-Z-W8-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`; `surfaced_at` =
`date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-s-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round3/checks/s2.AC1.sh; echo "exit=$?"</invocation><expect>working safe-apply: arms PASS 6 of 6, final RESULT: PASS lines>=1; base safe-apply (95d53e2068): arms PASS fewer than 6 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~8/NFRA_MCPMSP.TO-MS-s-2.safe-apply-scoped-tagauthz-tombstone.proof_of_spec.json`.
Report once, with: which arms the base bytes fail; the AC1 line; MS-s-1's self-test line; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E1 of `ledger/ROUND_ANALYSIS.round2.md` @8a9def3720 (CTO ruling 2: Z-W7-S1 CUT; `1.0.0_SA_CTO~Z` stays
the row's owner until this cell lands). Sibling census at the cut: 6 orders name `.tools/safe-apply.sh`, all `complete`
(NFRA_CTLPLN CT-s-3, CT-d-3; LGIC_ENFORCE EN-t-2, EN-t-2-r2; LGIC_BLANKFIX BF-x-3; NFRA_MCPMSP MS-s-1). The analysis's
"both cases on a scratch root, with a negative control" = arms 1-4 plus the base-bytes difference control in AC1.
Check dry-run at base: AC1 FAIL as expected (self-test absent).

<status>complete</status>
<round>3</round>
<slot>~8</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
