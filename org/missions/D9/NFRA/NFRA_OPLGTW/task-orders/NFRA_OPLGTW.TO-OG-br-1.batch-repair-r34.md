# NFRA_OPLGTW task order -- `OG-br-1` -- round-34 batch repair: gateway records and the SI2 puller (E4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-br-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-br-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~54</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repo records and puller source only; the installed puller on SI2 is NOT redeployed by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no identity, role or policy is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's analyses: round 32 @3566a85699 section 2 (W39-S1/S2, S69, S70) and round 33 @2672b8d28a section 2 (Z-S84, W45-S4, W47-S2, Z-S88).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-br-1` (decomposition addendum R3-T.42, E4: one batch, repairs only)

`G` = `infra/aws/ec2/opal-gateway/`. The live gateway release is `c3af8687e4` (`infra/aws/ec2/EC2_MANIFEST.json`
`services.opal-gateway.deployed_commit`).

1. **Runbook 7.2 (row Z-S88).** `G/runbooks/SCHWAB_PILOT_RUNBOOK.md` section 7.2 lists rollback targets and does not name
   the live release. Update it to name `c3af8687e4` as the live release, with its rollback anchor in the same form as
   the targets already listed. Grade: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rb.AC2.sh`
   must PASS, and rb.AC1 and rb.AC3 (same folder) must still PASS.
2. **Manifest checksums (row Z-S84).** In `infra/aws/ec2/EC2_MANIFEST.json`, `services.opal-gateway.file_checksums` holds
   10 entries (paths relative to `G`); 6 differ from the deployed bytes. Re-derive EVERY entry as the md5 of that path's
   blob at `deployed_commit` (`git show <deployed_commit>:infra/aws/ec2/opal-gateway/<path> | md5`). Change no other
   manifest field.
3. **Source-map build note (row S70).** In `infra/aws/lambda/ci/lambda-source-map.json`, the `advi-49f-gold-dispatch`
   entry's `_build_note` says "Zip carries BUILD_MANIFEST.json". The builder ships no manifest for this function. Correct
   the sentence to say the zip carries `lambda_function.py` and `trading_calendar.py` only, and that the source map is
   the build record. Edit only that note.
4. **The SI2 puller (rows W39-S1, W39-S2)**, `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, in the
   `if ($Mode -eq 'enumerate') { ... }` block (about lines 362-370):
   - call `Release-SessionLock` before its `exit 0`;
   - force the per-type date list to an array (`$ds = @( ... )`), so a one-file type prints its own date and not
     `2..0`.

   Change nothing else, and do not touch the census copy under `infra/system/`.
5. **Failing-test baseline (rows W45-S4, W47-S2).** `G/tests/baseline/failing_ids_full.txt` already lists the 4 named
   failing ids. Confirm they are there and add nothing. This item is a read: say so in your report.

## 2. BOUNDS

- Records and the one puller file only. No deploy, no SSM, no AWS call, no change to the installed puller.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W54-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-br-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/br1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)rb\.AC2 PASS; file_checksums \d+ entries at deployed_commit \w+, 0 differ \[\]; _build_note claims a BUILD_MANIFEST member: False.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-br-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/br1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)releases the lock before exit: yes; date list forced to array: 1 \(want 1\); parse errors: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three records match the served release. `AC2`: the puller's two defects are fixed and the script parses.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-br-1.batch-repair-r34.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag
to `complete` only if both PASS, and report once. Name in the report what reinstalling the puller on SI2 would take; do
not do it.
`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~54/`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, E4. Second on slot ~54 after OG-db-1.
- Row S69 (silver-schwab source-map fields) was settled by OG-ap-5 @68c493e37c and is not re-cut.
- Z-S84's ruling supersedes OG-mf-1's R26 empty-map convention, which re-derives from the served release.
- Pre-cut: br1.AC1 base FAIL as expected (rb.AC2 FAIL; 6 of 10 checksums differ; note claims the member).
  br1.AC2 base FAIL as expected (no release before exit; 0 array wraps; parse errors 0).

<status>complete</status>
<round>34</round>
<slot>~54</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
