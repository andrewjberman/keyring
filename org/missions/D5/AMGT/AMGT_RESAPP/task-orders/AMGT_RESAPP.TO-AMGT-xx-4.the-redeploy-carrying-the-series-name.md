# AMGT_RESAPP task order -- `AMGT-xx-4` -- THE REDEPLOY CARRYING THE SERIES NAME

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-xx-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN by the issuer at the cut -- xx-2's join calls only `dynamodb:GetItem` on `etf-classifications`, granted at round 48 (@26113dbc97); the plan must show NO IAM change.
comp-adversary: RUN by the issuer at the cut -- AC2 reads the deployed series' names against a held and an unheld ticker; AC3 holds round 48's served names and words.
EGRESS CLASS, declared: the artifact build pip-downloads its pinned wheels; otherwise Opal's own AWS only.
</preflight>

## 1. THE ACT -- `AMGT-xx-4` (round 49, decomposition s.57)

Redeploy `opal-amgt-scoped-api` so the served `/lead-panel/timeseries/<movement>/<subject>` series carry `name`, `classification`
and `name_state` (xx-2's join in `lib/research/api/scoped_amgt.py` `read_rank_series`).

**Begin only when all three hold:** `AMGT-xx-2` is `complete` and merged on the working branch (the issuer's GO names the build
commit), and both never-widen halves are committed:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/NEVER_WIDEN_HALF_COO_XX4.md` and
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND49_XX4_CTO_HALF.md`. **The acts, in order, under ONE NEVER-2 entry
opened AND COMMITTED before the build** (sentinel + entry): (1) capture the halves' pre-apply outputs; (2) build and upload the
ONE artifact `research/opal-amgt-scoped-api.zip` (record the prior VersionId), then ONE `safe-apply` on
`infra/aws/terraform/harvest/` -- print the plan first; it must move the function's code and NOTHING else (no IAM, no prefix);
(3) verify with the three criteria; close the entry. A criterion that fails after the apply is the ROLLBACK trigger named in the
halves.

## 2. BOUNDS

1. The one act and nothing else, under ONE NEVER-2 entry committed before the build and closed in the same session.
2. A plan that moves anything beyond the function's code, a closure diff that hits a stop limb of the halves, or a gate refusal is
   a REFUSAL: print it, stop, report.
3. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-xx-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-4.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-xx-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-4.AC2.py; echo "exit=$?"</invocation><expect>tickers asked N, series N, name SERVED M (M &gt; 0), THE DEPLOYED RANK-HISTORY SERIES CARRY THE SERVED NAME: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-xx-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/ww-1.AC3.py; echo "exit=$?"</invocation><expect>THE DEPLOYED FUNCTION SERVES THE NAMES AND THE WORDS: YES -- and exit=0 (round 48's served outcome holds)</expect></criterion>
</proof_of_spec>

AC1 the act landed; AC2 this round's served series names; AC3 round 48's served names and words hold.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-xx-4.the-redeploy-carrying-the-series-name.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-48 analysis s.4 row 2. Waits on xx-2. The COO half is written after xx-2 lands, against its landed code,
reading the expected outcome from the join rule (the round-48 method). Base: AC1 FAIL (CodeSha256 = lg6NJ2JL...), AC2 FAIL (name
SERVED 0), AC3 PASS (round 48's outcome, rc 0).

<status>pending</status>
<round>49</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
