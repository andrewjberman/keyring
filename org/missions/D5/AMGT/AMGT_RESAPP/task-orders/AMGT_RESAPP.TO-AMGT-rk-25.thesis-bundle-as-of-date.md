# AMGT_RESAPP task order -- `AMGT-rk-25` -- the thesis bundle carries `as_of_date` from its filing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-25</owned_cells>
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

**You are `0.9.0_WK_AMGT_RESAPP~27`, continuing.** LAST (sixth) of six orders in chain B's queue (reordered
at the cut -- `AMGT-rk-30` now runs second, for throughput). First act:
re-confirm `git rev-parse --abbrev-ref HEAD` and that the paths below exist.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~27;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-25` (FWD-3; W18-S19; round-11 s.4 item 2's ruling, still unmet)

**THE MEASURED STATE.** `analyze.py:697` already sets `filing_date` on the analysis object, and
`drafting_build.py:229` already forwards it into the drafting object
(`"filing_date": analysis["filing_date"]`). **`read_thesis_bundle()` (`scoped_amgt.py:1897-1949`) never
re-exposes it as `as_of_date` on the OUTER bundle** -- confirmed absent from the dict literal (`:1918-1934`)
and every subsequent `bundle.update()`/key assignment in the function.

**RULED:** one line, either inside `_drafting_block()` (which `read_drafted_sections()` at `:1581`
delegates to) or immediately after `bundle.update(read_drafted_sections(resolved_key))` at `:1938`:
`bundle["as_of_date"] = <the same filing_date already read, no new read, no new producer call>`. For a name
carrying no filing, `as_of_date` must NOT be invented or carry a stale value -- it stays absent/null,
matching the drafting object's own state for that name.

**Sequencing note:** this order and chain B's `AMGT-rk-24` (adapter half) both touch the SAME
function region (`read_thesis_bundle()`'s drafting merge). You already drained `AMGT-rk-24`'s adapter half
before reaching this order in your queue -- read the CURRENT state of that region (post-`rk-24` edit) before
adding this line, so your edit composes with it rather than reverting it.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.4's `R13-G` row @`9419550eb1`,
row `AMGT_RESAPP-Z-W18-S19` (round-11, carried forward, s.6's disposition table). PRD v0.10, ADMITTED, no PRD
change (round-11 s.4 item 2 already ruled this; it is being MET, not re-decided).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-25.thesis-bundle-as-of-date.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Write only `scoped_amgt.py`, and only the
  `read_thesis_bundle()`/`_drafting_block()` region. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~27 <0.9.0_WK_AMGT_RESAPP~27@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **DEPLOY:** redeploy the Lambda from HEAD, Terraform only. **You may combine this deploy with `AMGT-rk-24`
  adapter half's redeploy into ONE act if both land in the same session** (matching round 12's own
  rk-6/rk-7 combined-deploy precedent) -- if you do, name BOTH cells in the SAME change-management entry and
  say so explicitly in your report; if you deploy separately, open a fresh entry for this act with its own
  live pre-act hash.

## 4. BOUNDS

Same standing bounds: PORTAL FROZEN (not your surface); COLLECTION STAYS OFF; NO alarm/monitor/notification;
secrets through `comp-secrets` only; no vendor call; no non-ASCII; **PUSH: never**. **THE REFUSAL CLAUSE:** a
criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired, widened, or
satisfied by a route this order did not name. **This is a served-output-moving deploy (or a combined one, per
s.3 above): fresh never-widen co-sign, ledger entry opened before the first live act, rollback from the LIVE
pre-act hash of THIS act (or the combined act, named as such).** **SURPRISE ROWS:** your row continues
`AMGT_RESAPP-Z-W27-S<k>`; `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row; append by
textual splice inside the one fenced JSON array (never re-serialize it) and never edit an existing row.
**Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-25"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
payload = json.dumps({'rawPath': '/api/scoped/amgt/security/BA_US_Equity/thesis', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
body = json.loads(resp['Payload'].read())
inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
print('as_of_date', inner.get('as_of_date'))
print('drafting_filing_date', (inner.get('drafted_sections') or {}).get('filing_date') if isinstance(inner.get('drafted_sections'), dict) else 'inspect actual shape')
"</invocation><expect>BEFORE this order lands, as_of_date is absent from the served bundle (KeyError-equivalent / None printed, the pre-fix baseline); AFTER, as_of_date equals BA's filing_date, the same value already carried on the drafting object -- record both runs</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-25"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
payload = json.dumps({'rawPath': '/api/scoped/amgt/security/HOLLOW_NONEXISTENT_KEY_Equity/thesis', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
body = json.loads(resp['Payload'].read())
inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
print('as_of_date', inner.get('as_of_date'))
"</invocation><expect>a name carrying no filing does NOT carry an invented or stale as_of_date -- it reads null/absent, never a fabricated date. PLANTED negative control</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-25.thesis-bundle-as-of-date.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. **Report once. This is chain B's last order** -- your queue is
complete after this drains.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>13</round>
<slot>~27</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

