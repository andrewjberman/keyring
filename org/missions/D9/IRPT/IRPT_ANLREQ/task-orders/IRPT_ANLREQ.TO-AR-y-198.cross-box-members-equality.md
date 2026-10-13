# TO IRPT_ANLREQ.TO-AR-y-198.cross-box-members-equality -- the cross-box resident members compared to their owners' released versions

<to_id>IRPT_ANLREQ.TO-AR-y-198</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-198` (`decompositions/IRPT_ANLREQ_DECOMP_R19R2_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-198`, inlined) -- READ. Nothing is changed or called.

*The cross-box members of the resident delta: EQUAL to a version their owner already released, or not.* The CTO (section 4 point 2): ADVI_FIRMBKTS's three and NFRA_CTLPLN's one (other boxes): each member's bytes at the release pin must EQUAL a version its owner already released (the Lambda artifacts their own pairs shipped: act 4's eight, the CTLPLN release). Equal: the pair cites that release and no read is asked. Not equal: that member goes to its owner through `0.0.0_AB_MSTR~DELL2` before the pair is signed.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_PACKAGE_DELTA.json` (`other_differing_by_owner`, `only_in_new`), `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 4, the act-4 ledger entry `org/critical_paths/change_management/20261012T1340Z_advi-firmbkts-fb-f-11-act4-irpt-leg-20261012_deploy_completion.md` and its records (`ACT4_EXPECT.json`, `act4_irpt/builds_and_priors.json` under the dell1 applier's deliverables: find them from the entry), the source map `infra/aws/lambda/ci/lambda-source-map.json` (each function's `staged_from` rows carry the member's `pin` and `sha256`), and the CTLPLN release records for `lib/opal_naming.py` and `infra/logic/registry/firm_pages.json` (find the NFRA_CTLPLN project's release/deploy entries; say what you read).
The five members: `_authz/loaders.py`, `infra/logic/registry/exemptions.json`, `infra/logic/registry/scopes.json` (ADVI_FIRMBKTS); `lib/opal_naming.py` and `infra/logic/registry/firm_pages.json` (NFRA_CTLPLN; the latter is NEW in the release build).

For EACH, an object in `members` with: `member`, `owner`, `release_pin_blob` (the blob hash at `069b8f797e`) and its sha256, `owner_released_version` (what the owner released: the commit or pin, the blob hash and sha256, and WHERE that is recorded: file and line), `verdict` (`EQUAL` if the blobs are byte-identical, `NOT_EQUAL` with the two hashes and the commits between them, or `CANNOT_TELL` with the reason), and `evidence`. Note the source map row for `irpt-ycharts-generate`'s `_authz/loaders.py` moved from `69679b90e3` to `0642c9d004` between the round-19 base and the head (row W51-S20): say which of the two the owner RELEASED and which the release pin carries.
**Write `r19/CROSS_BOX_MEMBERS_EQUALITY.json`** with `members`, `claim`, `not_read`. **In your report:** the five verdicts first; for any NOT_EQUAL, the owner, the member and the commits that differ.

### ACCEPTANCE

<criterion id="AR198-y-AC1" cell_refs="AR-y-198"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y198-equal --root C:/dev/wk-irpt-anlreq-51</invocation><expect>Y198-EQUAL-OK</expect></criterion>
`AR198-y-AC1`: the record has the five members, each with the release-pin blob, the owner's released version, a verdict (EQUAL, NOT_EQUAL or CANNOT_TELL) and its evidence.

<criterion id="AR198-y-AC2J" cell_refs="AR-y-198" judgment="true"/>
`AR198-y-AC2J` (judgment, graded at L9, never by you): each owner-released version is read from a record that names it, EQUAL means byte-identical blobs rather than similar, and a CANNOT_TELL says what is missing.

<expected_criteria>AR198-y-AC1 AR198-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R2_Y.md</decomp_doc>
<owned_cells>AR-y-198</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-198.cross-box-members-equality.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-198`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of the repository and recorded releases; nothing is changed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (section 4 point 2: equal to an owner-released version, or back to the owner) against the cell; the lens: 'equal' decided by similarity or by a pin rather than by the blob. The order requires byte-identical blobs and the recorded source of each owner-released version. NOT seen: the live Lambda artifacts in S3 (0 S3 objects read; only recorded hashes).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 analysis section 4 point 2. Base: `AR198-y-AC1` FAIL as expected (no record).
