# AMGT_RESAPP task order -- `AMGT-rk-19` (adapter half) -- the SECOND join: filing-verified points, only on the exact-mnemonic join's miss

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-19</owned_cells>
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

**You are `0.9.0_WK_AMGT_RESAPP~27`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the
paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN B, a queue of SIX
orders, in this order: `AMGT-rk-19` (this one, adapter half), `AMGT-rk-20`, `AMGT-rk-23`, `AMGT-rk-24`
(adapter half), `AMGT-rk-25`, `AMGT-rk-30` (adapter half). Chain B holds `lib/research/api/scoped_amgt.py`
WHOLE-FILE plus every live AWS act that moves served output this round, so that surface has ONE writer, and
EACH deploy in your queue is sequenced strictly after the one before it.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~27;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-19` adapter half (FWD-18; ADDENDUM 2's A2.3 item 3, unchanged from s.3.1 items 2-3)

**RULED.** `thesis_driver_chart()` (`scoped_amgt.py`, currently `:1953-2013`) keeps its exact-mnemonic join at
FULL PRECEDENCE, unedited -- a keyword or fuzzy match is still refused by design (row `W18-S12`). **Add a
SECOND branch that runs ONLY when the exact join misses:** serve the driver's VERIFIED filing points (written
by the sibling producer order, `AMGT-rk-19`'s producer half -- `thesis_driver.points`, each carrying a
character span and, where matched, a `passage_id`) with `source: "filing"` on the served object, needing at
least 2 verified points; otherwise the chart stays ABSENT, with the emitted-vs-verified counts printed
(`held_uncited` count vs `points` count). **The route never re-serves an unverified point** -- if
`thesis_driver.points` is empty or `resolution` is not the corrected verified state, the second branch does
not fire.

This function is called from `read_thesis_bundle()` (`:1897-1949`) at
`bundle["thesis_driver_chart"] = thesis_driver_chart(bundle.get("thesis_driver"), fiscal_year_figures)` --
that call site does not move; only `thesis_driver_chart()`'s own body gains the second branch.

**This is a served-output-moving deploy. It needs a FRESH never-widen co-sign (CTO half + your COO's half),
each naming blast radius and per-key rollback FROM THE LIVE PRE-ACT HASH OF THIS ACT** (never a prior act's --
the banked lesson: a co-sign rollback goes stale the moment a second act hits the same address). **Open your
change-management ledger entry BEFORE your first live act on this order**, close it on completion, per
NEVER-2.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.3.1 @`9419550eb1` and its
**ADDENDUM 2** (same commit, appended) s.A2.3 item 3 (explicitly UNCHANGED from s.3.1's original items 2-3).
PRD v0.10, ADMITTED, no PRD change.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant (you may read
  `filings/v1/BA_US_Equity/000162828026004357.analysis.json` from the pool to confirm the producer's fix
  landed before you deploy); this block governs WRITES. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~27 <0.9.0_WK_AMGT_RESAPP~27@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **DEPLOY:** redeploy the Lambda from HEAD per this project's established deploy mechanism (the same one
  round 12's `AMGT-rk-2`/`AMGT-rk-6` combined redeploy used -- read that order's own record for the exact
  invocation if you need the precedent). Never bare `aws lambda update-function-code`; Terraform only, per
  the standing hard-stop.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO -- not your surface. **THE PORTAL DEV PUSH IS RESERVED**
under LD-0367/0368. **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness
checker.** Secrets through `comp-secrets` only. **No vendor call beyond what this order names** (none is
named -- this order calls no vendor). No non-ASCII in anything you write. **PUSH: never.** Your work is
LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator.**
**BEFORE YOU DEPLOY:** confirm chain FP's `AMGT-rk-19` producer order has drained and BA's stored analysis
object carries the corrected, verified `thesis_driver.points` -- if it has not, STOP and file a row rather
than deploying against unverified upstream data.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W27-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-19"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
payload = json.dumps({'httpMethod': 'GET', 'path': '/api/scoped/amgt/security/HOLLOW_NONEXISTENT_KEY_Equity/thesis', 'headers': {}, 'queryStringParameters': None}).encode()
resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
body = json.loads(resp['Payload'].read())
print('statusCode', body.get('statusCode'))
inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
tdc = inner.get('thesis_driver_chart', inner)
print('points_count', tdc.get('points_count'))
"</invocation><expect>a nonexistent security key's second branch never fires and the chart reads ABSENT / points_count 0 -- the PLANTED negative control confirming the second branch only fires on real, verified data, never on a miss</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-19"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
lam = boto3.client('lambda')
payload = json.dumps({'httpMethod': 'GET', 'path': '/api/scoped/amgt/security/BA_US_Equity/thesis', 'headers': {}, 'queryStringParameters': None}).encode()
resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
body = json.loads(resp['Payload'].read())
inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
tdc = inner.get('thesis_driver_chart', {})
print('points_count', tdc.get('points_count'))
print('source', tdc.get('source'))
print('points', tdc.get('points'))
"</invocation><expect>a DIRECT invocation of the deployed adapter (post-redeploy) for BA_US_Equity reads points_count 3, source "filing", and three points each carrying provenance -- this is the served plane, not a source read; ADDENDUM 2 reverses the ORIGINAL expectation of ABSENT for this exact name</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order. **Both criteria run AFTER your redeploy, against the LIVE deployed plane, never a local import.**

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-19.adapter-second-join.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. **Do not stop here** -- `AMGT-rk-20` is handed to you next as a
continuation; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
