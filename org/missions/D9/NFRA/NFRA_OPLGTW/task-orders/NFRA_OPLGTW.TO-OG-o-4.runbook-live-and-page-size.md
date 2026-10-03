# NFRA_OPLGTW task order -- `OG-o-4` -- runbook 7.2 names the live release; W5-S6 closed in code (docstring + a 500-row page test)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-o-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~21</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a document and a test; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS resource or permission is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the graders are OG-o-3's and the remedy is the CTO's (analysis round 12 s.5 item 6).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-o-4` (decomposition addendum R3-T.7, item 6)

**Handed only after `OG-rl-4` has closed.** The runbook names the release that is live when you run, which is the
release `OG-rl-4` deploys. Read `deployed_commit` from the manifest at YOUR worktree's HEAD, never from this text.

1. **Runbook 7.2.** `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` section 7.2 (~:250-253) still says the
   live release is `6a98a0553a`; the manifest (`infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit`)
   reads the live release (`4231bd2ddc` at the round-14 cut; `OG-rl-4`'s head after it closes). Update 7.2 to name the live release and keep every rollback target
   it names a recorded `deployed_commit` that carries `app/data_entitlement.py` (the rules `rb.AC2.sh` checks). Keep
   `rb.AC1`/`rb.AC3` passing (cross-references, section count).
2. **W5-S6.** Since OG-x-2, `app/integrations/schwab/envelope.py` `measure()` (:174-185) counts rows ONCE across blocks;
   its module docstring (:17-18) still says rows are summed across representations. Fix the docstring. Add
   `test_ogo4_ac02` to `infra/aws/ec2/opal-gateway/tests/test_schwab_query.py`: a page of 500 NARROW rows (small enough
   that the byte cap does not bind) returns 500 rows, not 250.

## 2. BOUNDS

Edit ONLY the runbook, the `envelope.py` docstring (no code line), and the one new test. No deploy. Never push, merge,
rebase, stash, `checkout --` or `clean`; never override a gate. `.py` edits pass `.tools/commit-gate.sh`; commit with
`.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
infra/aws/ec2/opal-gateway/app/integrations/schwab/envelope.py
infra/aws/ec2/opal-gateway/tests/test_schwab_query.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W21-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-o-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rb.AC2.sh; echo "exit=$?"</invocation><expect>(?s)7.2 names live=yes; targets named \d+, without guard 0, not in manifest history 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-o-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/o4.AC2.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 1 of 1; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="J1" cell_refs="OG-o-4" judgment="true"/>
</proof_of_spec>

- `AC1`: section 7.2 names the live release; every rollback target is valid.
- `AC2`: a 500-row page of narrow rows returns 500.
- `J1`: `OGO2-J1` re-graded at L9 by `3.0.0_SA_CVO~O` against the runbook at your commit: "an operator can execute each
  section at its named moment without other context." RECORD; NO VERDICT.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~21/NFRA_OPLGTW.TO-OG-o-4.runbook-live-and-page-size.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Record J1 as `UNVERIFIABLE-BY-INSTRUMENT` naming
`3.0.0_SA_CVO~O`. If AC1 and AC2 PASS, append a `complete` status tag after the order's last status line in the same
commit. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 6). Chained after `OG-rl-4`, because `rb.AC2` reads the manifest at grade time. Pre-cut: `rb.AC2` FAIL ("7.2 names live=no"). W5-S6 is already resolved in
  served code (OG-x-2 `0c3d545002`); this cell pins it. The LIVE artifact's runbook is the pre-repair text: the next
  release that ships the runbook carries it (not `OG-rl-4`, which names its files).

<status>pending</status>
<round>14</round>
<slot>~21</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
