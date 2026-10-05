# AMGT_RESAPP task order -- `AMGT-at-4` -- EVERY DAY-ROUTE ROW SERVES ITS ORIGIN (OWN OR EXTERNAL), OWN PUBLICATIONS FIRST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-at-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~229</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only stores the function already reads; no write. A read of a NEW S3 path is named in your report (the redeploy cell simulates it).
comp-adversary: RUN by the issuer at the cut -- r70_served c33 FAILS at the base on deployed: 5 day probes, 8 rows, 8 with no origin.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only. A figure or leg that needs a NEW vendor pull is served with a plain reason and filed as a row for Andrew's act, never pulled.
</preflight>

**Your worktree:** `C:/tmp/r70-229` (branch `wk-AMGT_RESAPP-229`, cut from the issuance commit with `--portal-ref 6936e92b`). Work
and commit only there. Start every shell call with `cd /c/tmp/r70-229`: a call that starts elsewhere resolves `git rev-parse
--show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-at-4` (round 70, decomposition s.78; CTO round-69 analysis item 4; DSGN FWD-5)

`/security/<key>/timeline/day/<date>` serves `articles` rows with `publisher` (for example barrons, sa, bbg) and no origin.
The page rule is that "the firm's own publications come first", and today it can only be graded vacuously.

1. **Serve `origin` on every row:** `"own"` for the firm's own publications and `"external"` for every other publisher.
   - Declare the own-publisher list in code, with a `_SOURCE` string naming where it comes from.
   - If the estate has no own publisher today, the list is empty and every row is external. Say so in the source string.
2. **Order:** own rows first, then external rows, each group in the route's existing order.
3. **The plant test** `lib/research/api/tests/test_day_origin.py` covers:
   - a planted own row is served first with `origin: own`;
   - external rows serve `origin: external`.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W229-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`. If one api test fails only because it
reads a portal function absent at this worktree's portal ref (`test_model_words.py`), name it in your report and file no row; the issuer
grades the suite on the shared tree.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Add `origin` and the own-first order only. No row is dropped or added, and no other field moves.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block,
   estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~229/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-at-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_day_origin.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-at-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell c33 --where local; echo "exit=$?"</invocation><expect>C1 PASS 0 rows failing and C2 PASS 0 out of order; R70 C33 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~229 <0.9.0_WK_AMGT_RESAPP~229@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~229/AMGT_RESAPP.TO-AMGT-at-4.day-route-origin.proof_of_spec.json`.
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

**ISSUER NOTES:** CTO round-69 analysis @0bdf5b47ae item 4 and rulings 1-2; routed from DSGN_AMGTV1 FWD-5. Served by at-6.

<status>pending</status>
<round>70</round>
<slot>0.9.0_WK_AMGT_RESAPP~229</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~07:1xZ):** CLOSED.
- Worker ~229: code `507af39d49`, instance at `2b8f4c3557`, proof-of-spec-check VALID (rc=0) on the committed bytes.
- AC1 PASS 3 of 3; the mutant fails 2 of 3. AC2 PASS c33 local: 8 rows over 5 probes, 0 failing, 0 out of order.
- `DAY_OWN_PUBLISHERS` is empty, and its source string says the estate holds no own publisher today, so every row is external.
  0 new S3 read paths. Served by at-6.

<status>complete</status>
