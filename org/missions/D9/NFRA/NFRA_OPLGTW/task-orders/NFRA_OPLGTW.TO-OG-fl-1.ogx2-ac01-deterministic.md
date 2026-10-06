# NFRA_OPLGTW task order -- `OG-fl-1` -- make test_ogx2_ac01 deterministic

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-fl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~26</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test fix; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local tests; no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's (round-19 analysis s.4 item 3; row Z-W15-S58).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-fl-1` (decomposition addendum R3-T.13, item 3; row Z-W15-S58)

`infra/aws/ec2/opal-gateway/tests/test_schwab_export_stream.py::test_ogx2_ac01` fails intermittently on both CLOUD and
live, with an export-stream `job_failed`.
1. **Find the cause.** Candidates are timing, a shared path or the engine deadline. Reproduce it: run the test
   repeatedly and capture the `job_failed` detail.
2. **Make the test deterministic.** Fix the test or its fixture, and touch product code ONLY if the cause is a real
   product defect. In that case file a row naming it and keep the product change minimal and separately committed.
   Never loosen the assertion's meaning, never skip, never retry-to-green.
3. **Write `FL1_CAUSE.md`.** It holds a line `cause: <timing|shared path|engine deadline|other: ...>`, the evidence,
   and `commit <sha>` of the fix.
4. **Baseline.** The issuer's baseline file names this id FLAKY. Do not edit it; the issuer removes the id at your
   drain.

## 2. BOUNDS

- Tests (and, only as named above, product code with a row). No deploy.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/
infra/aws/ec2/opal-gateway/app/integrations/schwab/export.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/engine.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W26-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-fl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r20/checks/fl1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)test_ogx2_ac01 passed 20 of 20 own-process runs; FL1_CAUSE.md names the cause and the fix commit: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~26/NFRA_OPLGTW.TO-OG-fl-1.ogx2-ac01-deterministic.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`, and on PASS edit this order's ONE `<status>` tag IN
PLACE to `complete`. Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 20 (R3-T.13, item 3). Alone.
- If its fix touches `export.py` or `engine.py`, it rides the next release.
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>20</round>
<slot>~26</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
