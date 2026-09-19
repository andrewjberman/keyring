# AMGT_RESAPP task order -- `AMGT-rk-23` -- every artifact name built from a raw security key is path-safe; print serves 33 of 33

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-23</owned_cells>
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

**You are `0.9.0_WK_AMGT_RESAPP~27`, continuing.** Fourth of six orders in chain B's queue (reordered at the
cut -- `AMGT-rk-30` now runs second, for throughput). First act:
re-confirm `git rev-parse --abbrev-ref HEAD` and that the paths below exist.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~27;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-23` (FWD-5; S141; W19-S5)

**THE MEASURED STATE, row `AMGT_RESAPP-Z-S141`:** the print pack serves a valid PDF for 31 of 33 keyed
covered names; the two that 500 are exactly the two keys containing a slash (`BP/_LN_Equity`,
`NG/_LN_Equity`): the renderer writes the raw security key into a local file path, and `NG/_LN_Equity`
resolves to `pack_NG/_LN_Equity.pdf`, a path with a directory (`pack_NG`) that does not exist ->
`FileNotFoundError`.

**Two sites CENSUSED at this cut, both local-filesystem joins (S3 keys already tolerate `/` fine -- this is
never an S3 problem):**
1. `lib/research/print/render_pack.py:243-244` -- `pdf_path`/`txt_path` built as
   `base / "pack_{0}.pdf".format(sec_key)` / `"pack_{0}.txt"`, where `sec_key = security_key(security)`
   (`:147-148`), which only replaces spaces, never slashes.
2. `lib/research/api/scoped_amgt.py:1403` -- the offline/test drafting-document reader
   (`AMGT_DRAFTING_ROOT`), `filename = "{0}.json".format(security_key)`, same shape, same hazard (lower risk
   today since only exercised on the offline/test fixture path, but the census is "every artifact name",
   not "every LIVE one").

**RULED:** a one-line path-safe encode at BOTH sites (e.g. `sec_key.replace("/", "-")`, or
`urllib.parse.quote(sec_key, safe="")` if a reversible/URL-safe form is preferred -- your choice, stated in
your report, applied IDENTICALLY at both sites so a name's on-disk artifact name is the same string
everywhere). **No new module** -- `lib/opal_naming.py`'s `address()`/`name()` mint S3/resource addresses,
not sanitize an already-existing key for filesystem use; this is a two-line fix, not infrastructure (YAGNI).

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.4's `R13-E` row @`9419550eb1`,
grounded in row `AMGT_RESAPP-Z-S141` (`4.0.0_SA_CRO~Z`, corroborating round-11's `W19-S5`). PRD v0.10,
ADMITTED, no PRD change (a bug fix, not a new outcome).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/print/render_pack.py
lib/research/api/scoped_amgt.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-23.artifact-name-encoding.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `scoped_amgt.py` is named here (chain B's own surface,
  which you already hold this queue) -- edit ONLY line `:1403`'s filename construction, nothing else in the
  file, from this order. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~27 <0.9.0_WK_AMGT_RESAPP~27@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.
- **DEPLOY:** this touches `scoped_amgt.py` -- redeploy the Lambda from HEAD, Terraform only, never bare
  `aws lambda update-function-code`.

## 4. BOUNDS

Same standing bounds: PORTAL FROZEN (not your surface); COLLECTION STAYS OFF; NO alarm/monitor/notification;
secrets through `comp-secrets` only; no vendor call; no non-ASCII; **PUSH: never**. **THE REFUSAL CLAUSE:** a
criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired, widened, or
satisfied by a route this order did not name. **A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and
PRINTS its denominator** -- re-read the 33 keyed names from `crosswalk/v1/<latest date>.json` yourself, never
cite 33 as a constant. **This is a served-output-moving deploy: fresh never-widen co-sign, ledger entry opened
before the first live act, rollback from the LIVE pre-act hash of THIS act.** **SURPRISE ROWS:** your row
continues `AMGT_RESAPP-Z-W27-S<k>`; `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row;
append by textual splice inside the one fenced JSON array (never re-serialize it) and never edit an existing
row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-23"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='crosswalk/v1/')
latest = sorted(o['Key'] for o in resp.get('Contents', []))[-1]
doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=latest)['Body'].read())
keyed = [r['security_key'] for r in doc.get('records', doc if isinstance(doc, list) else []) if r.get('security_key')]
print('keyed_count', len(keyed))
print('slash_bearing', [k for k in keyed if '/' in k])
lam = boto3.client('lambda')
results = {}
for k in keyed:
    payload = json.dumps({'rawPath': f'/api/scoped/amgt/security/{k}/print', 'headers': {'x-firm-id': 'bd'}, 'requestContext': {'http': {'method': 'GET'}}}).encode()
    resp2 = lam.invoke(FunctionName='opal-amgt-scoped-api', Payload=payload)
    body = json.loads(resp2['Payload'].read())
    results[k] = body.get('statusCode')
ok = sum(1 for v in results.values() if v == 200)
print('served_ok', ok, 'of', len(keyed))
print('failures', {k: v for k, v in results.items() if v != 200})
"</invocation><expect>served_ok equals the printed keyed_count (33 at this cut, re-measured live) -- both previously-failing slash-bearing keys now read statusCode 200, and failures is empty. Before the fix, failures names exactly the two slash-bearing keys and served_ok reads keyed_count minus 2 -- record both the before and after run</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-23.artifact-name-encoding.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. **Do not stop here** -- `AMGT-rk-24` (adapter half) is handed to you next as
a continuation; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->
<!-- added by the issuer 2.0.0_SA_COO~Z 2026-09-19 on row AMGT_RESAPP-Z-W57-S2: this round-13 order was terminal-by-proof (VALID instance, graded at L9) but carried no record face, so a --round-filtered acceptance read could not see it -->
<status>complete</status>
<round>13</round>
<slot>~27</slot>
<fabric>site-z</fabric>
