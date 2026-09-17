# AMGT_RESAPP task order -- `AMGT-rk-24` (adapter half) -- the thesis route surfaces the store's own no-CIK reason, not a generic NoSuchKey

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-24</owned_cells>
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

**You are `0.9.0_WK_AMGT_RESAPP~27`, continuing.** Fifth of six orders in chain B's queue (reordered at the
cut -- `AMGT-rk-30` now runs second, for throughput). First act:
re-confirm `git rev-parse --abbrev-ref HEAD` and that the paths below exist.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~27;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-24` adapter half (FWD-18; S139 corrected by S146)

**THE MEASURED STATE.** The thesis route currently surfaces NONE of the filings store's own classification:
zero occurrences of `UNRESOLVED-SOURCE` or `filing_identity` anywhere in `scoped_amgt.py`.
`read_thesis_bundle()` (`:1897-1949`) never reads the security's `filings/v1/<key>/` source object at all --
it only reads the model block, drafting sections, management and posture. For a name with no CIK, the page's
`drafting_reason` reads the generic S3 `NoSuchKey`, even though the store (per this cell's sibling producer
order, chain FP-B's `AMGT-rk-24`) now carries an explicit, named no-CIK reason for every one of the 21 unfiled
names.

**RULED:** inside `read_thesis_bundle()`, where the drafting merge happens
(`bundle.update(read_drafted_sections(resolved_key))`, around `:1938`), also read the security's
`filings/v1/<key>/` source object (reuse whatever read helper `read_drafted_sections()`/`_drafting_block()`
already uses for the analysis object, or add one call alongside it). When that object's `status` reads
`UNRESOLVED-SOURCE`, merge its `reason` through as the bundle's `drafting_reason`, replacing the generic
`NoSuchKey` string. **Do not change `fetch.build_source_object()`'s classification logic** -- it is already
correct; this order only makes its result visible on the served route.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.4's `R13-F` row @`9419550eb1`,
rows `AMGT_RESAPP-Z-S139`/`S146` (`4.0.0_SA_CRO~Z`). The producer half of this same cell (writing the
`UNRESOLVED-SOURCE.source.json` objects this order reads) is a SEPARATE order on chain FP-B,
`AMGT_RESAPP.TO-AMGT-rk-24.batch-unresolved-objects.md`, and must drain BEFORE this order's criteria can pass
for the 21-name population (do not spawn/run this order's criteria before confirming chain FP-B's order has
reached that order).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-24.thesis-route-no-cik-reason.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You may READ `lib/research/filings/fetch.py` freely (its
  `unresolved_source_object()` shape is what you are matching) but write only `scoped_amgt.py` among repo
  files, and only inside `read_thesis_bundle()`/`_drafting_block()`'s drafting-merge region. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~27 <0.9.0_WK_AMGT_RESAPP~27@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **DEPLOY:** redeploy the Lambda from HEAD, Terraform only.

## 4. BOUNDS

Same standing bounds: PORTAL FROZEN (not your surface); COLLECTION STAYS OFF; NO alarm/monitor/notification;
secrets through `comp-secrets` only; no vendor call; no non-ASCII; **PUSH: never**. **THE REFUSAL CLAUSE:** a
criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired, widened, or
satisfied by a route this order did not name. **A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and
PRINTS its denominator** -- re-count the 21 yourself. **This is a served-output-moving deploy: fresh
never-widen co-sign, ledger entry opened before the first live act, rollback from the LIVE pre-act hash of
THIS act.** **SURPRISE ROWS:** your row continues `AMGT_RESAPP-Z-W27-S<k>`; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-24"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json, boto3
s3 = boto3.client('s3')
doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key='universe/v1/2026-09-16.json')['Body'].read())
unresolved = [r['security_key'] for r in doc.get('names', []) if not (r.get('filing_identity') or {}).get('cik')]
print('unresolved_count', len(unresolved))
lam = boto3.client('lambda')
name = unresolved[0]
payload = json.dumps({'httpMethod': 'GET', 'path': f'/api/scoped/amgt/security/{name}/thesis', 'headers': {}, 'queryStringParameters': None}).encode()
resp = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
body = json.loads(resp['Payload'].read())
inner = json.loads(body.get('body', '{}')) if isinstance(body.get('body'), str) else body.get('body', {})
print('drafting_reason', inner.get('drafting_reason'))
"</invocation><expect>BEFORE this order lands, drafting_reason reads a generic NoSuchKey-shaped string; AFTER (and after chain FP-B's order has written the pool objects), drafting_reason for the sampled unfiled name reads the store's own no-CIK reason text (matching `filing_identity.source is None: no cik and expected form to fetch by`, or the equivalent corrected wording) -- the worker records both runs and names which unresolved name it sampled</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-24.thesis-route-no-cik-reason.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. **Do not stop here** -- `AMGT-rk-25` is handed to you next as a
continuation; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
