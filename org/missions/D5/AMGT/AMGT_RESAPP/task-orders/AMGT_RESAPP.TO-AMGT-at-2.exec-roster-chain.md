# AMGT_RESAPP task order -- `AMGT-at-2` -- THE EXEC ROSTER: THE F3 CHAIN (FILING, DOSSIER, BLOOMBERG) OVER EVERY NAME WITH NO MANAGEMENT OBJECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-at-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~227</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only stores the function already reads; no write. A read of a NEW S3 path is named in your report (the redeploy cell simulates it).
comp-adversary: RUN by the issuer at the cut -- r70_served c31 FAILS at the base on deployed: 95 names, 11 SERVED, 84 failing (82 NO_OBJECT, 2 ZERO_OFFICERS), none naming a chain tried.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only. A figure or leg that needs a NEW vendor pull is served with a plain reason and filed as a row for Andrew's act, never pulled.
</preflight>

**Your worktree:** `C:/tmp/r70-227` (branch `wk-AMGT_RESAPP-227`, cut from the issuance commit with `--portal-ref 6936e92b`). Work
and commit only there. Start every shell call with `cd /c/tmp/r70-227`: a call that starts elsewhere resolves `git rev-parse
--show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-at-2` (round 70, decomposition s.78; CTO round-69 analysis item 2; DSGN FWD-7)

`/security/<key>/thesis` `management` serves officers only from an M-1 management object
(`s3://opal-data-harvest/management/v1/<key>/`). 84 of 95 covered names have none, or have zero officers. The F3 chain
(`lib/research/management/`; see `bloomberg_fallback.py`) is filing, then research dossier, then Bloomberg, tried in that order.

1. **When no M-1 object serves officers,** try the F3 legs at request time over STORED objects only: the filing text, the dossier
   and stored Bloomberg fields the estate already reads.
   - The first leg that yields officers serves them, each officer naming its `source`.
2. **When no leg yields officers,** serve `management_status` not SERVED, a non-empty `chain_tried` list naming each leg tried with
   its outcome, and a plain `reason`.
3. **A leg that would need a NEW vendor pull** (for example a live Bloomberg request) is NOT called. It appears in `chain_tried` as
   not tried and why, and you file ONE row listing those names for Andrew's act.
4. **The plant test** `lib/research/api/tests/test_exec_roster_chain.py` covers:
   - a name with an object is unchanged;
   - a name whose filing yields officers serves them with the source named;
   - a name with nothing serves `chain_tried` and a reason.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W227-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`. If one api test fails only because it
reads a portal function absent at this worktree's portal ref (`test_model_words.py`), name it in your report and file no row; the issuer
grades the suite on the shared tree.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. The 11 names served from an M-1 object keep exactly what they serve today. No store write.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block,
   estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~227/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-at-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_exec_roster_chain.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-at-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell c31 --where local; echo "exit=$?"</invocation><expect>population names 95 with 0 non-200; C1 PASS 0 names failing; R70 C31 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-at-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell c26 --where local; echo "exit=$?"</invocation><expect>R67 C26 SERVED: YES (DE 200 on thesis and peers; ZZZZ 404); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~227 <0.9.0_WK_AMGT_RESAPP~227@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~227/AMGT_RESAPP.TO-AMGT-at-2.exec-roster-chain.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the functions you changed;
- any new S3 read path;
- any row, including any vendor leg listed for Andrew.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-69 analysis @0bdf5b47ae item 2 and rulings 1-2; routed from DSGN_AMGTV1 FWD-7. Served by at-6.

<status>pending</status>
<round>70</round>
<slot>0.9.0_WK_AMGT_RESAPP~227</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
