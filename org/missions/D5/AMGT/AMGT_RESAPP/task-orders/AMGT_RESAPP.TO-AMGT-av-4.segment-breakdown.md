# AMGT_RESAPP task order -- `AMGT-av-4` -- THE SEGMENT BREAKDOWN SERVED FROM STORED FILING ANALYSES, OR A PLAIN REASON (FWD-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-av-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~240</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: RUN by the issuer at the cut -- the route will read `filings/v1/<key>/*.analysis.json`, a prefix REMOVED from the Lambda grant (`infra/aws/terraform/harvest/scoped-amgt-api.tf:123`). The grant is av-8's leg, with a simulate arm. A local run uses the operator's credentials.
comp-adversary: RUN by the issuer at the cut -- r72 c43 FAILS on deployed: 0 of 95 names serve `segment_breakdown`.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only. A numeric segment table for the other names needs a Bloomberg segment pull: list it for Andrew, never pull.
</preflight>

**Your worktree:** `C:/tmp/r72-240` (branch `wk-AMGT_RESAPP-240`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r72-240`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-av-4` (round 72, decomposition s.80)

PRD v0.39 FWD-1 DONE WHEN (PRD `:487`).

No stored numeric segment data exists: 0 of 95 model blocks, and 0 of 117 Bloomberg bronze fields. Segment PROSE (5-12 cited items
each) exists in the filing analyses at `filings/v1/<key>/*.analysis.json` for 12 of 95 names.
1. **Serve `segment_breakdown` on `/security/<key>/thesis`:** `{"rows": [{"segment", "text", "cite"}], "reason", "source"}`.
   - Rows come from the newest stored filing analysis that carries segment items.
   - A name with none serves `rows: []` and a plain `reason`.
2. **The census** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~240/SEGMENT_CENSUS.md`: per covered name, rows served or the reason. File ONE row listing the names
   without segments, for Andrew's Bloomberg segment pull (a vendor use).
3. **The plant test** `lib/research/api/tests/test_segment_breakdown.py`.
4. **Name the new S3 read path** (`filings/v1/`) in your report, for av-8's grant leg.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W240-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Add the block only. No other served field changes.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~240/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-av-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_segment_breakdown.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-av-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round72/checks/r72_served.py" --cell c43 --where local; echo "exit=$?"</invocation><expect>population names 95 with non-200 0; C1 PASS failing 0; C2 PASS with rows 12 or more; R72 C43 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~240 <0.9.0_WK_AMGT_RESAPP~240@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~240/AMGT_RESAPP.TO-AMGT-av-4.segment-breakdown.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the new S3 read path;
- the census totals;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-71 analysis item 4. The premise is corrected in s.80a. The grant leg is av-8's.

<status>pending</status>
<round>72</round>
<slot>0.9.0_WK_AMGT_RESAPP~240</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
