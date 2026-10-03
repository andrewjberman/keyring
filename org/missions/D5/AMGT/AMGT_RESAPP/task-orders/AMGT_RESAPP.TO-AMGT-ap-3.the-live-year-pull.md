# AMGT_RESAPP task order -- `AMGT-ap-3` -- THE LIVE ONE-TIME PX_LAST YEAR PULL (card 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ap-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one run by hand; nothing is scheduled and the daily job is not touched.
comp-iam: RUN by the issuer at the cut -- the act writes one new S3 object and new generation partitions through the paths AMGT-ap-2 declares; the plan run (ap-2 AC3) names both, and a denied write shows as a FAIL on AC1.
BLIND: no IAM simulation was run for this act; a denied write shows as a FAIL on AC1.
comp-adversary: RUN by the issuer at the cut -- r66_served c22 FAILS at the base, local and deployed (0 rows, "not produced yet").
EGRESS CLASS, declared: Bloomberg PX_LAST, ONE run, on Andrew's per-use word (card 4, ANDREW_DIRECT_20261003_20xxZ_YES_TO_ALL_SEVEN_OPEN_CALL_RECS.md @9fe6e6f111).
</preflight>

## 1. THE ACT -- `AMGT-ap-3` (round 66, decomposition s.74; ADDENDUM 1 @1162e9be0e item 1)

At the drained commit the GO names, run
`"C:/Users/Opal Bloomberg/AppData/Local/Programs/Python/Python311/python.exe" integrations/bloomberg/research/price_history_pull.py --live`
ONCE, from a checkout at that commit.

**Begin only when** the GO names the commit (AMGT-ap-2 drained). Before the run:
- Read `integrations/bloomberg/READ_HERE.md`.
- Confirm the terminal answers with a real data read. If it is signed out, STOP and report: a sign-in spends a budgeted attempt and
  is not in this order.
- Run `--plan` and keep its output.

**After the run:**
- Report the vendor request count, the S3 key and its size, the rows written per generation, and the excluded tickers with their
  reasons.
- Any write to a 30-day partition or pointer is a STOP.

## 2. BOUNDS

1. One `--live` run, and nothing else. No overwrite, no S3 delete, no deploy.
2. `price_axis_pull.py` and `scheduled_daily_pull.cmd` are untouched.
3. No push of shared branches.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ap-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round66/checks/r66_served.py --cell c22 --where local; echo "exit=$?"</invocation><expect>run from a checkout at the GO's commit: C1 PASS on trending and breakout x 90 and 365 (rows from the new generations, window_end, a window_note where it is earlier than the last trading day); R66 C22 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ap-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c10 --where deployed; echo "exit=$?"</invocation><expect>R64 C10 SERVED: YES on the deployed function, with every figure equal to the pre-run read (DELTA=0: the deployed code reads only the 30-day partitions); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ap-3.the-live-year-pull.proof_of_spec.json`.
Report once:
- the plan output
- the run's counts
- the S3 key
- every criterion's output lines

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.74 R4. Staged until ap-2 drains. DELTA=0 on served routes, so no never-widen hold (NEVER-1 non-application); the
NEVER-2 ledger entry is AE~A's as for any act.

<status>staged</status>
<round>66</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
