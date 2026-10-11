# NFRA_OPLGTW task order -- `OG-wr-1` -- prime the 13-month window once per master and measure the warm read on the served gateway (E5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-wr-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-wr-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~56</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- one SSM command on the gateway host (i-07dccb1615503ac99) outside any gateway release; the gateway queue's next release (CT-i-11, OG-ap-7) is not in flight at the cut. Run it between 11:00Z and 23:00Z and confirm no `.open_deploys/nfra-oplgtw-gateway-release-*` sentinel is open. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- the host's own role; no identity, role or policy changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's ruling (d) on row W43-S7, ROUND_ANALYSIS.round32.md ADDENDUM 1 @7b727bd74e (prime once, measure warm; fan-out only if the warm read is over 60 s).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-wr-1` (decomposition addendum R3-T.42, E5)

A COLD 13-month availability read costs about 221-235 s per master (row W43-S7: 0.8 s per first-seen date, 274 dates,
sequential). `infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py` `availability()` (`:872`) returns a stored
snapshot before any verification and persists a new one write-once (catalog.py:841-870). The cold cost is therefore paid
once per date. Alyssa's grant reads 13 months (`deliverables/0.9.0_WK_NFRA_OPLGTW~43/RL15_GRANTS.json`, 274 dates per
master and dataset).

1. Write one host-side program `W/wr1_ssm_prog.py`. It runs with the gateway's INSTALLED code and Python
   (`/opt/opal-gateway`), never repo code. For every master/dataset pair in the 13-month grant:
   - PRIME: one availability() pass over the window, timed (`cold_seconds`), through the installed catalog against the
     real state store. Snapshots are persisted write-once, exactly as a served read does. Write nothing else.
   - MEASURE: the same read again (`warm_seconds`).

   Record `window_dates` and `primed_dates` (stored snapshots present after the pass). Template: the r29 programs in
   `deliverables/0.9.0_WK_NFRA_OPLGTW~43/` (`r29_ssm_prog.py`). Print the body and `WR1_DIGEST <sha256 of json.dumps(body, sort_keys=True)>`.
2. Send it as ONE SSM RunShellScript to i-07dccb1615503ac99 (`bash .tools/aws ssm send-command ...`). Write
   `W/WR1_READ.json` = `{"body": {"pairs": [{"master","dataset","window_dates","primed_dates","cold_seconds","warm_seconds"}]}, "ssm_command_id", "instance_id"}`,
   with the body exactly as the host printed it.
3. If AC2 FAILs (warm read of 60 s or more on any pair), that is the ruling's trigger for the bounded fan-out (step 3).
   File a BLOCKING row with the measured figures. Do NOT build the fan-out here; the issuer cuts it.

## 2. BOUNDS

- One SSM command; the persistence is the service's own write-once snapshot store only. No restart, no deploy, no code
  change on the host, no principal impersonation, no grant written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~56/`. Rows: id `NFRA_OPLGTW-Z-W56-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-wr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/wr1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pairs not primed or unmeasured 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-wr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/wr1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)\(want . 60\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both masters primed, every pair measured. `AC2`: the warm read fits the 60 s ALB default (ruling (d) step 2).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-wr-1.warm-13-month-read.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once with the per-pair cold and warm figures.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, E5. Second on slot ~56 after OG-gw-1. The 13-month read is not advertised to Alyssa as interactive until AC2
  PASSES.
- Pre-cut: wr1.AC1 and wr1.AC2 base FAIL as expected (WR1_READ.json absent).

<status>complete</status>
<round>34</round>
<slot>~56</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
