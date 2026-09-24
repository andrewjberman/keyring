# AMGT_RESAPP task order -- `AMGT-rk-30` (adapter half) -- the three built scores reach the served Model tab route

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-30</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~27</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected and no schedule is read or written.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  S3 bucket/prefixes and DynamoDB table this project already reads and writes) under the existing Lambda
  execution role; it grants no new permission and provisions no new resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~27`, continuing.** SECOND of six orders in chain B's queue (moved up from
position 6 at the cut, for throughput -- this order has no dependency on `AMGT-rk-20`/`AMGT-rk-23`/
`AMGT-rk-24`/`AMGT-rk-25`, only on chain SP, so it does not need to sit behind them). First act:
re-confirm `git rev-parse --abbrev-ref HEAD` and that the paths below exist. **BEFORE YOU BEGIN, confirm
chain SP's `AMGT-rk-30` producer order (a separate chain, `0.9.0_WK_AMGT_RESAPP~29`) has drained and the
scores pool carries real records.** Chain SP is a single-order chain running in parallel with you, so an
ordinary short wait here is EXPECTED, not a problem -- **wait for it rather than filing a blocking row**;
only file a row if chain SP itself reports a failure or the wait becomes clearly unreasonable (your judgment,
stated in your report either way).
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~27;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-30` adapter half (ADDENDUM 1: cell R13-L, not deferrable with R13-K)

**THE MEASURED STATE.** `lib/research/scores/` (Robustness, Peers V, Divergence D, `classify.py`'s record
shape) is COMPLETE code -- unit-tested, never wired into any pipeline. **No served surface carries any of the
three:** `scoped_amgt.py` never references them, and the deployed thesis/overlay bodies contain no score and
not even D's classed ABSENT.

**RULED:** inside `read_thesis_bundle()`, immediately after the existing
`bundle["posture"] = read_posture(resolved_key, identity=identity)` line (near `:1939-1940`), add:
`bundle["scores"] = read_scores(resolved_key, identity=identity)`. Write `read_scores()` to mirror
`read_management()`'s exact shape (`:2184-2251`): resolve identity -> `read_pool_object(SCORES_PREFIX, key)`
-> `POOL_ABSENT`/`POOL_SERVED` status dict, carrying each of the three scores' `classify.py` record
(`measured(value, ...)` or `absent(reason_code, reason, ...)`) as written by chain SP's producer order.
**A score that renders nothing because its field is missing is NOT met** -- `read_scores()` must always
return all three keys (`robustness`, `peers_v`, `divergence`), each a MEASURED or ABSENT record, never a
silently-dropped key.

**Criteria (this order's half):** the served count of MEASURED Robustness and Peers V over the 33 keyed
names, printed with ABSENT reason codes beside it; Divergence D reads ABSENT on 33 of 33 with its reason
("house forecast does not serve" -- `AMGT-rk-29`/R13-K has not landed, by design, not by omission); one
PLANTED negative per score (a name whose scores pool object carries a missing/null value for one field MUST
class that field ABSENT, never silently render 0).

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s **ADDENDUM 1** @`509f3f7335`, triggered by
`4.0.0_SA_CRO~Z`'s row `AMGT_RESAPP-Z-S149`. PRD v0.10, ADMITTED, no PRD change
(`C-ROUND12-DIVERGENCE-DEGENERACY` already binds D at the producer). The producer half of this cell is a
SEPARATE order on chain SP (`AMGT_RESAPP.TO-AMGT-rk-30.scores-producer-runner.md`), which MUST drain before
this order's criteria measure real data. The page half is a THIRD, separate order on chain A
(`AMGT_RESAPP.TO-AMGT-rk-30.page-scores-render.md`), fed only after this order deploys.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-30.scores-adapter-model-tab.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You may READ `lib/research/scores/classify.py` freely (the
  record shape you must match) but write only `scoped_amgt.py`, and only the `read_thesis_bundle()` tail plus
  a new `read_scores()` function. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~27 <0.9.0_WK_AMGT_RESAPP~27@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **DEPLOY:** redeploy the Lambda from HEAD, Terraform only. **You may combine this deploy with
  `AMGT-rk-19` adapter half's redeploy into ONE act if both land in the same session** (matching round 12's
  own rk-6/rk-7 combined-deploy precedent) -- if you do, name BOTH cells in the SAME change-management entry
  and say so explicitly; if you deploy separately, open a fresh entry for this act with its own live pre-act
  hash.

## 4. BOUNDS

Same standing bounds: PORTAL FROZEN (not your surface); COLLECTION STAYS OFF; NO alarm/monitor/notification;
secrets through `comp-secrets` only; **no vendor call** (this order reads the pool the producer already
wrote; it never invokes Bloomberg or an LLM itself); no non-ASCII; **PUSH: never**. **THE REFUSAL CLAUSE:** a
criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired, widened, or
satisfied by a route this order did not name. **A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and
PRINTS its denominator.** **This is a served-output-moving deploy: fresh never-widen co-sign, ledger entry
opened before the first live act, rollback from the LIVE pre-act hash of THIS act.** **SURPRISE ROWS:** your
row continues `AMGT_RESAPP-Z-W27-S<k>`; `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row;
append by textual splice inside the one fenced JSON array (never re-serialize it) and never edit an existing
row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-30"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='crosswalk/v1/')
latest = sorted(o['Key'] for o in resp.get('Contents', []))[-1]
doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=latest)['Body'].read())
keyed = [r['security_key'] for r in doc.get('records', doc if isinstance(doc, list) else []) if r.get('security_key')]
print('keyed_count', len(keyed))
lam = boto3.client('lambda')
measured_rob = measured_pv = absent_div = 0
for k in keyed:
    payload = json.dumps({'rawPath': f'/api/scoped/amgt/security/{k}/thesis', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    resp2 = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
    body = json.loads(resp2['Payload'].read())
    inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
    scores = inner.get('scores', {})
    if (scores.get('robustness') or {}).get('status') == 'MEASURED': measured_rob += 1
    if (scores.get('peers_v') or {}).get('status') == 'MEASURED': measured_pv += 1
    if (scores.get('divergence') or {}).get('status') == 'ABSENT': absent_div += 1
print('measured_robustness', measured_rob, 'of', len(keyed))
print('measured_peers_v', measured_pv, 'of', len(keyed))
print('absent_divergence', absent_div, 'of', len(keyed))
"</invocation><expect>measured_robustness and measured_peers_v are both nonzero over the printed keyed_count denominator (round-11's built inputs support real values for most, not necessarily all, keyed names -- any non-measured name must carry an ABSENT reason code, not a missing key); absent_divergence equals keyed_count exactly (33 of 33), each with the "house forecast does not serve" reason -- if the worker's own status field names differ from MEASURED/ABSENT, it names the real ones used and re-runs this exact invocation against them</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-30.scores-adapter-model-tab.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. **Do not stop here** -- `AMGT-rk-20` is handed to you next as a
continuation; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->
<!-- added by the issuer 2.0.0_SA_COO~Z 2026-09-19 on row AMGT_RESAPP-Z-W57-S2: this round-13 order was terminal-by-proof (VALID instance, graded at L9) but carried no record face, so a --round-filtered acceptance read could not see it -->
<status>complete</status>
<round>13</round>
<slot>~27</slot>
<fabric>site-z</fabric>
