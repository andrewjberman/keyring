# AMGT_RESAPP task order -- `AMGT-rj-10` -- THE DEPLOY AND THE LIVE READ -- one terraform act carries the round's code and reads it back on the live plane

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~19</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~19`.** Same worktree (sparse cone incl. `infra`), same rules as `rj-4` and `rj-5`; this is the THIRD
and last order of chain B, handed to you only after `rj-1` and `rj-9` (chain A's adapter edits) are drained, with `rj-6`, `rj-7`
and `rj-8`'s pool objects landed. Your worktree branch is FAST-FORWARDED by the issuer to the drained tip before this order is handed
over, so `lib/research/` and the portal-independent code you deploy are the round's. Every Bash call begins `export
OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~19;`. **THIS CELL CHANGES THE WORLD (two functions' code, two policies, and a generation write).
It is ORDERED exactly as ri-2 and ri-4 were: the co-sign gate (AC1), the ledger entry with its sentinel COMMITTED, the act, the close,
the commit of the close, then the grading reads.** Write your serial into the halt gate's session file right before the apply
(`printf '%s' 0.9.0_WK_AMGT_RESAPP~19 > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"`) and run the apply with `HALT_ACK=1`.

## 1. THE CELL, inlined in full -- `AMGT-rj-10` (the consumer cell; C-ONE-STORE's package seam; C-RANKING-GENERATION on the live plane)

**WHAT MOVES, and only this (the COO half `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND11_ONE_STORE_COO_HALF.md` is the
whole permitted set; the CTO half `NEVER_WIDEN_ROUND11_ONE_STORE_CTO_HALF.md` must exist as a file in the MAIN tree, AC1):**
- `opal-amgt-scoped-api` (module.scoped_amgt_api): code -- the closure zip rebuilt by `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`
  (round 10's transitive-closure builder) and EXTENDED for C-ONE-STORE's package seam: the zip carries `lib/research/coverage/pool_reader.py`
  and its imports, the harvester's SCHEMA FILES (`lib/opal_data_harvest/article.schema.json`, `security-article.schema.json` -- non-`.py`
  members the closure walk does not see; add them explicitly), and a VENDORED `jsonschema` (pure-Python; pip-download into the build dir,
  never a layer), exercised in an ISOLATED runtime before upload (a fresh venv with no site-packages importing `lambda_function` and
  calling the coverage read against a local fixture).
- `amgt-resapp-chatter-axis`: code -- `infra/aws/terraform/harvest/lambda_src/build_zip.py` extended the same way (the pool reader, the
  crosswalk, the generation writer, the schema files, `jsonschema`), its own AST verify printing the closure.
- `aws_iam_role_policy.chatter_axis_lambda` and `aws_iam_role_policy.scoped_amgt_api_grants` (`scoped-amgt-api.tf`, `chatter-axis-schedule.tf`):
  `s3:GetObject` + `s3:ListBucket` on `opal-data-harvest` -- for the ADAPTER role the nine prefixes `publication-links/v1/`, `publications/v1/`,
  `universe/v1/`, `crosswalk/v1/`, `filings/v1/`, `drafting/v1/`, `peers/v1/`, `management/v1/`, `posture/v1/`; for the PRODUCER role only
  the FOUR it reads, `publication-links/v1/`, `publications/v1/`, `crosswalk/v1/`, `universe/v1/` (the CTO half's least-privilege REC
  @`e1c3cf0cb3`) -- resource ARNs by prefix, `ListBucket` with the `s3:prefix` condition; the DynamoDB `opal-harvest-articles` statements
  REMOVED from both (retired as a source); NO Scan, NO wildcard resource; the metrics table's grants unchanged.
- The producer's QA invoke (AC7): a COMPLETE generation for today on both chatter axes, with its pointer.
- NOTHING ELSE: no new function, no new schedule, no route change on `7k3ed8px20` (the 11 routes stand; new reads travel inside existing
  payloads per rj-9), no touch on the 16 pre-existing resources or the mount's other 17, no `opal-data-etfs` grant, no portal act.

**THE CTO HALF'S FIVE FINDINGS (@`e1c3cf0cb3` s.6), carried into your criteria:** (1) the metrics table has THREE writers at HEAD -- the
chatter Lambda (this act), the box-side price pull `integrations/bloomberg/research/price_axis_pull.py` (TRENDING_/BREAKOUT_PRICE#, no
pointer) and `lib/research/watchlist/store.py` (star markers) -- the act touches the first only; (2) no TRENDING_PRICE#/BREAKOUT_PRICE#
partition exists live, so a PRICE ranking already reads row_count 0 and the act cannot lower it; (3) the `_CURRENT` pointer sits inside
the legacy bare-date partition: AC7 prints its attribute names and `rank_sort` must be ABSENT (rj-5's writer guarantees it) or a
rolled-back adapter would serve it as an eleventh row; (4) the artifact key `research/opal-amgt-scoped-api.zip` is OVERWRITTEN this
time: AC2 prints the object's `VersionId` BEFORE the upload and records it as the rollback pointer; (5) the root's census is 32 state
ENTRIES / 42 INSTANCES (the 16 of round 10 + the 6 ri-2 moved in + the mount's 10 entries expanding to 19 instances), 4 to change,
28 entries unchanged -- AC4 prints entries and instances apart.

**DELIVER, in this order:**
1. **AC1** the co-sign gate. 2. The two zips rebuilt and verified in isolation (AC2, AC3); the scoped API artifact uploaded AFTER its
   current `VersionId` is printed (the producer's zip is read by `filebase64sha256()` at plan time). 3. **AC4** the whole-root plan: `Plan: 0 to add, N to change, 0 to
   destroy` with N the two functions (code hash) and the two policies -- FOUR addresses, enumerated APART from the data-source entries
   (W17-S5); any add, replace, destroy or a fifth address is a STOP. 4. The ledger entry (slug `amgt-round11-one-store-deploy`; legs
   L1 git, L2 s3 = the artifact upload with its head-object, L3 activation = the apply, L4 verify = the two functions' live config and
   policies, L5 verify = the generation write and the served reads), COMMITTED with its sentinel; `safe-apply` (AC5); close; commit the
   close. 5. **The live reads** (AC6-AC8) and the CAPTURES for rj-3: `rankings.trending.chatter.response.<day>.json` and
   `thesis.BA_US_Equity.response.<day>.json` from the deployed adapter, each with its sha256, in your deliverables.

**BOUND:** no edit to `lib/research/` (drained code only; a defect found here is a row, and the fix is a recut); no route change; no
new resource; the generation write is the producer's own invoke, never a hand-written item; the 10:00Z schedule unchanged.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4` (the one consumer cell), on C-ONE-STORE's package seam (the CRO's brief @`0e7de170e3`),
C-RANKING-GENERATION (@`5ae6dd04b5`), the round-10 co-sign shape (`NEVER_WIDEN_ROUND10_MOUNT_*` @`cf54bd03f3`), the slug's W17-S4/S5
criteria lessons, and Andrew's local-box word @`187f003998` (no new Lambda for any batch).

## 3. SURFACES -- what you may read and write

<paths>
infra/aws/terraform/harvest/
infra/aws/terraform/modules/yang-lambda/
infra/aws/lambda/research/scoped_amgt_api/
infra/aws/lambda/ci/lambda-source-map.json
lib/research/
lib/__init__.py
lib/opal_data_harvest/
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND11_ONE_STORE_COO_HALF.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND11_ONE_STORE_CTO_HALF.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/mcp/sessions/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-10.the-deploy-and-the-live-read.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/` is READ-ONLY input to the two zips; the two halves are READ-ONLY;
  your writes are the two build scripts, the two `.tf` policy edits, the ledger entry and sentinel, the session serial file, the
  instance and captures.
- **COMMITTING:** as in `rj-4`; several commits are expected (the builds and policies; the ledger open with its sentinel; the close).

## 4. BOUNDS

Egress @`dfa63b6d92` (Opal's own AWS). Secrets ONLY through `comp-secrets` (none needed). No non-ASCII in anything that reaches AWS. No
monitor or alarm. NEVER `terraform apply` bare (only `safe-apply`); NEVER `aws lambda update-function-code` (terraform only). **THE
REFUSAL CLAUSE** and **SURPRISE ROWS** as in `rj-4`; continue the `W19` sequence.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-10"><invocation>MAIN="$(dirname "$(git rev-parse --git-common-dir)")"; for h in COO CTO; do f="$MAIN/org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND11_ONE_STORE_${h}_HALF.md"; printf "%s_HALF %s\n" "$h" "$(test -f "$f" && echo PRESENT || echo ABSENT)"; test -f "$f" && sed -n '1,6p' "$f"; done; printf "NEG %s\n" "$(test -f "$MAIN/org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND11_ZZZ_NOPE.md" && echo PRESENT || echo ABSENT)"</invocation><expect>COO_HALF PRESENT and CTO_HALF PRESENT, each with its first lines printed and the CTO half carrying a Verdict line that reads SIGNED, and NEG ABSENT. STOP: CTO_HALF ABSENT means this order STOPS HERE -- a BLOCKING row, AC1 FAIL, the order OPEN, no build, no plan, no apply. Re-run only when the COO continues you</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-10"><invocation>.tools/aws s3api head-object --bucket opal-313476888478-lambda-artifacts --key research/opal-amgt-scoped-api.zip --query "[VersionId,ContentLength,Metadata.\"content-sha256\"]" --output text > .scratch/rj10.artifact-before.txt; printf "ARTIFACT-BEFORE %s\n" "$(cat .scratch/rj10.artifact-before.txt)"; timeout 115 bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh > .scratch/rj10.build-api.txt 2>&1; echo build-rc=$?; python -c "import re,io; t=io.open('.scratch/rj10.build-api.txt',encoding='utf-8',errors='replace').read(); print('closure-verify-missing', re.findall(r'missing \[[^\]]*\]', t)[-1:]); print('schema-members', t.count('article.schema.json') + t.count('security-article.schema.json'), 'jsonschema-vendored', t.count('jsonschema'), 'isolated-runtime', t.count('ISOLATED') + t.count('isolated'))"; tail -4 .scratch/rj10.build-api.txt</invocation><expect>an ARTIFACT-BEFORE line with the prior object's VersionId (or None when the bucket is unversioned -- recorded either way; it is the rollback pointer), size 75917 and the round-10 sha; build-rc=0; closure-verify-missing [] (the transitive closure holds after the reader joined it); schema-members at least 2 (both harvester schemas packaged); jsonschema-vendored at least 1; isolated-runtime at least 1 with an OK line from the fresh-venv import + coverage read against a fixture; the head-object JSON with Meta.content-sha256 EQUAL to the local sha256 line; OK: uploaded. A missing schema member, or an isolated-runtime failure, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-10"><invocation>python infra/aws/terraform/harvest/lambda_src/build_zip.py 2>&1 | tail -6; python -c "import zipfile; z=zipfile.ZipFile('infra/aws/terraform/harvest/.build/chatter-axis-producer.zip'); n=z.namelist(); print('entries', len(n), 'pool_reader', sum(1 for x in n if 'coverage/pool_reader.py' in x), 'crosswalk', sum(1 for x in n if 'identity/crosswalk.py' in x), 'schemas', sum(1 for x in n if x.endswith('.schema.json')), 'jsonschema', sum(1 for x in n if x.startswith('jsonschema/')))"</invocation><expect>OK lines from build_zip with its closure verify reporting missing []; entries above 20; pool_reader 1; crosswalk 1; schemas at least 2; jsonschema at least 1 (the vendored package). A zip without the reader, the crosswalk or the schemas is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-10"><invocation>cd infra/aws/terraform/harvest && timeout 60 terraform validate -no-color && timeout 115 terraform plan -input=false -no-color -detailed-exitcode -out=../../../../.scratch/rj10.tfplan > ../../../../.scratch/rj10.plan.txt 2>&1; echo plan-rc=$?; python -c "import re; t=open('../../../../.scratch/rj10.plan.txt',encoding='utf-8',errors='replace').read(); m=re.search(r'Plan: (\d+) to add, (\d+) to change, (\d+) to destroy',t); print('PLAN', m.group(0) if m else 'NO-PLAN-LINE'); ch=[l.strip()[:120] for l in t.splitlines() if l.strip().startswith('#') and 'will be updated in-place' in l]; print('managed-addresses-changing', len(ch)); [print(' ', l) for l in ch]; print('data-source-reads', sum(1 for l in t.splitlines() if l.strip().startswith('#') and ' data.' in l and 'Reading' in l)); print('replace-marks', t.count('must be replaced'), 'destroy-marks', t.count('will be destroyed'), 'create-marks', t.count('will be created'))"; timeout 60 terraform state list | python -c "import sys; t=[x for x in sys.stdin.read().split() if x]; import re; ents=set(re.sub(r'\\[.*?\\]$','',x) for x in t); print('state-instances', len(t), 'state-entries', len(ents), 'data-sources', sum(1 for x in t if '.data.' in x or x.startswith('data.')))"</invocation><expect>Success! The configuration is valid; PLAN Plan: 0 to add, 4 to change, 0 to destroy; managed-addresses-changing 4, EXACTLY module.scoped_amgt_api.aws_lambda_function (its address as the plan prints it), aws_lambda_function.chatter_axis_producer, aws_iam_role_policy.chatter_axis_lambda, aws_iam_role_policy.scoped_amgt_api_grants -- enumerated apart from data-source-reads (printed separately, never in the total); replace-marks 0, destroy-marks 0, create-marks 0, plan-rc=2; then state-entries 32 and state-instances 42 with the data-sources count printed apart (the CTO half's census: 28 entries unchanged). Any fifth address, any add, replace or destroy is OUTSIDE the co-sign and is NOT met: no apply runs</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-10"><invocation>printf '%s' 0.9.0_WK_AMGT_RESAPP~19 > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"; test -f org/critical_paths/.open_deploys/amgt-round11-one-store-deploy.json && git log -1 --format=%h -- org/critical_paths/.open_deploys/amgt-round11-one-store-deploy.json; HALT_ACK=1 timeout 115 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -no-color ../../../../.scratch/rj10.tfplan > .scratch/rj10.apply.txt 2>&1; echo apply-rc=$?; python -c "t=open('.scratch/rj10.apply.txt',encoding='utf-8',errors='replace').read(); import re; m=re.search(r'Apply complete! Resources: (\d+) added, (\d+) changed, (\d+) destroyed', t); print('APPLY', m.group(0) if m else 'NO-APPLY-LINE'); print('modifying', t.count('Modifying...'), 'modifications-complete', t.count('Modifications complete'), 'destroying', t.count('Destroying...'), 'creating', t.count('Creating...'), 'halt-block', t.count('BLOCK'))"</invocation><expect>a commit hash for the COMMITTED sentinel, then apply-rc=0 and APPLY Apply complete! Resources: 0 added, 4 changed, 0 destroyed (grepped over the saved output, never a tail window), modifications-complete 4, destroying 0, creating 0, halt-block 0. A halt-gate BLOCK is recorded verbatim and is NOT met until its cause is read; a non-zero destroyed or added count is a hard stop and a BLOCKING row</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-10"><invocation>for f in opal-amgt-scoped-api amgt-resapp-chatter-axis; do printf "%s " "$f"; .tools/aws lambda get-function-configuration --function-name $f --query "[State,CodeSha256,LastModified,CodeSize]" --output text; done; for r in "amgt-resapp-chatter-axis-lambda-role amgt-resapp-chatter-axis-lambda-policy" "opal-amgt-scoped-api-role opal-amgt-scoped-api-grants"; do set -- $r; .tools/aws iam get-role-policy --role-name $1 --policy-name $2 --query "PolicyDocument.Statement[].[Effect,Action,Resource]" --output json > .scratch/rj10.policy.$1.json; python -c "import json,io; t=io.open('.scratch/rj10.policy.$1.json',encoding='utf-8').read(); print('$1', 'articles-table', t.count('opal-harvest-articles'), 'pool-prefixes', sum(t.count(p) for p in ('publication-links/v1','publications/v1','universe/v1','crosswalk/v1','filings/v1','drafting/v1','peers/v1','management/v1','posture/v1')), 'scan', t.count('dynamodb:Scan'), 'wildcard', t.count('\"*\"'))"; done</invocation><expect>both functions Active with a CodeSha256 different from the pre-act values (round 10: sSanbq4vc+SDwxKfHplJr32E7hiPTYSJKm37hVMkPHA= for the API artifact; fj8wqp9jaZWfMaBrrAyUImGnt2c5Xeb7losUr+i65mM= for the producer) and LastModified today; both LIVE policies: articles-table 0, pool-prefixes at least 9, scan 0, wildcard 0 -- read from IAM, never from the .tf. A surviving articles-table grant is NOT met</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rj-10"><invocation>.tools/aws lambda invoke --function-name amgt-resapp-chatter-axis --cli-binary-format raw-in-base64-out --payload "{}" .scratch/rj10.invoke.json --query "[StatusCode,FunctionError]" --output text; python -c "import json,io; d=json.load(io.open('.scratch/rj10.invoke.json',encoding='utf-8')); print(json.dumps(d)[:400])"; TODAY=$(date -u +%F); for ax in TRENDING_CHATTER BREAKOUT_CHATTER; do printf "POINTER %s#%s: " "$ax" "$TODAY"; .tools/aws dynamodb get-item --table-name opal-harvest-security-metrics --key "{\"axis_date\":{\"S\":\"$ax#$TODAY\"},\"ticker\":{\"S\":\"_CURRENT\"}}" --query "Item.[generation_id.S,state.S,row_count.N,payload_hash.S,coverage_vintage.S]" --output text; printf "POINTER-ATTRS %s: " "$ax"; .tools/aws dynamodb get-item --table-name opal-harvest-security-metrics --key "{\"axis_date\":{\"S\":\"$ax#$TODAY\"},\"ticker\":{\"S\":\"_CURRENT\"}}" --query "keys(Item)" --output text | tr "\t" " "; echo; done</invocation><expect>200 None; a payload with rows_written per axis, generation ids and the pool denominators (names read, names with links); for each axis a POINTER line with a generation_id, state COMPLETE or EMPTY (BREAKOUT may be EMPTY on an all-zero day; TRENDING carries its tie-ranked rows), row_count, a 64-hex payload_hash and a coverage_vintage; a POINTER-ATTRS line per axis listing the item's attribute names with rank_sort ABSENT (the CTO half's finding 3: a pointer carrying rank_sort would be served as an eleventh row by a rolled-back reader). A missing pointer, a pointer with rank_sort, or rows written under a bare date partition, is NOT met</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-rj-10"><invocation>TODAY=$(date -u +%F); python -c "import json; ev={'version':'2.0','routeKey':'GET /api/scoped/amgt/lead-panel/rankings/{movement}/{subject}','rawPath':'/api/scoped/amgt/lead-panel/rankings/trending/chatter','rawQueryString':'','headers':{'x-firm-id':'opal-capital','x-user-role':'admin'},'queryStringParameters':{},'requestContext':{'http':{'method':'GET','path':'/api/scoped/amgt/lead-panel/rankings/trending/chatter'}},'pathParameters':{'movement':'trending','subject':'chatter'},'isBase64Encoded':False}; open('.scratch/rj10.ev.rank.json','w').write(json.dumps(ev)); ev2=dict(ev); ev2.update({'routeKey':'GET /api/scoped/amgt/security/{security_key}/thesis','rawPath':'/api/scoped/amgt/security/BA_US_Equity/thesis','pathParameters':{'security_key':'BA_US_Equity'}}); ev2['requestContext']={'http':{'method':'GET','path':'/api/scoped/amgt/security/BA_US_Equity/thesis'}}; open('.scratch/rj10.ev.thesis.json','w').write(json.dumps(ev2)); ev3=dict(ev2); ev3.update({'routeKey':'GET /api/scoped/amgt/security/{security_key}/coverage','rawPath':'/api/scoped/amgt/security/BA_US_Equity/coverage'}); ev3['requestContext']={'http':{'method':'GET','path':'/api/scoped/amgt/security/BA_US_Equity/coverage'}}; open('.scratch/rj10.ev.coverage.json','w').write(json.dumps(ev3))"; D="org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19"; mkdir -p "$D"; for e in rank thesis coverage; do printf "INVOKE %s: " "$e"; .tools/aws lambda invoke --function-name opal-amgt-scoped-api --cli-binary-format raw-in-base64-out --payload "file://.scratch/rj10.ev.$e.json" ".scratch/rj10.$e.out.json" --query "[StatusCode,FunctionError]" --output text; done; cp .scratch/rj10.rank.out.json "$D/rankings.trending.chatter.response.$TODAY.json"; cp .scratch/rj10.thesis.out.json "$D/thesis.BA_US_Equity.response.$TODAY.json"; python -c "import json,io,hashlib,glob; D='$D'; r=json.loads(json.load(io.open(D+'/rankings.trending.chatter.response.$TODAY.json',encoding='utf-8')).get('body') or '{}'); t=json.loads(json.load(io.open(D+'/thesis.BA_US_Equity.response.$TODAY.json',encoding='utf-8')).get('body') or '{}'); c=json.loads(json.load(io.open('.scratch/rj10.coverage.out.json',encoding='utf-8')).get('body') or '{}'); print('rank statusCode', json.load(io.open(D+'/rankings.trending.chatter.response.$TODAY.json',encoding='utf-8')).get('statusCode'), 'row_count', r.get('row_count'), 'generation_id', r.get('generation_id'), 'payload_hash', (r.get('payload_hash') or '')[:16], 'rows-with-key', sum(1 for x in (r.get('rows') or []) if x.get('security_key'))); print('thesis drafted sections', len(t.get('drafted_sections') or []), 'drafting_status', t.get('drafting_status'), 'identity', (t.get('identity') or {}).get('identity_status')); print('coverage items', len(c.get('items') or []), 'store_item_count', c.get('store_item_count')); [print('SAVED', f.split('/')[-1], hashlib.sha256(open(f,'rb').read()).hexdigest()[:16]) for f in sorted(glob.glob(D+'/*.response.*.json'))]"</invocation><expect>three invokes 200 None; rank statusCode 200 with row_count equal to the TRENDING pointer's row_count, a generation_id equal to the pointer's, a payload_hash, rows-with-key equal to row_count; thesis drafted sections 5 with drafting_status SERVED and identity MEASURED; coverage items at least 1 with store_item_count at least 1 and PRINTED (the pool's per-name link count; 2 for BA at row W19-S8); two SAVED lines with sha256 prefixes -- rj-3's exact inputs. A rankings response without generation_id, or a thesis with 0 drafted sections, is NOT met</expect></criterion>
  <criterion id="AC9" cell_refs="AMGT-rj-10"><invocation>python -c "import glob,os; fs=glob.glob('org/critical_paths/change_management/*amgt-round11-one-store-deploy*.md'); print('entries', len(fs)); [print(f, 'CLOSED-in-head', 'CLOSED' in open(f,encoding='utf-8').read()[:800]) for f in fs]; print('sentinel-present', os.path.exists('org/critical_paths/.open_deploys/amgt-round11-one-store-deploy.json'))"; git log -1 --format="%h %s" -- org/critical_paths/change_management/ | cut -c1-120</invocation><expect>entries 1, CLOSED-in-head True, sentinel-present False (ABSENT is the closed state), and the close COMMITTED. Run this LAST, after the close commit</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order. Every large
output is grepped for its tokens over the saved file (never a tail window); every state census enumerates managed addresses apart
from data-source entries.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/AMGT_RESAPP.TO-AMGT-rj-10.the-deploy-and-the-live-read.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8,AC9` (rc 0 is the verdict); keep the plan text,
the apply text, the two build logs, the policy reads and the captured payloads beside it; flip `<status>` to `complete`; commit with
`--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row -- and if it is AC4 or AC5, say
so as BLOCKING, because the world may be half-moved.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~19</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) C-ONE-STORE (the package seam; the CRO's brief @`0e7de170e3`) and C-RANKING-GENERATION (@`5ae6dd04b5`); NEVER-1 (CLAUDE.md) with the round-11 halves (COO half at the issuance; CTO half `1.0.0_SA_CTO~W`'s, requested in the issuance commit); the round-10 mount's halves @`cf54bd03f3`; Andrew's local-box word @`187f003998` (no new function); the slug's W17-S4/S5; decomposition v1.3 s.19 @`73938cdae4` (cell rj-10, chain B third, the one consumer cell, after the drains of rj-1/rj-9). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: RUN as the co-sign -- the blast is the two functions' code (opal-amgt-scoped-api, amgt-resapp-chatter-axis), the two role policies, and the served payloads of the coverage, thesis, peers, overlay-points, rankings, timeseries, management and posture reads; the whole permitted set is the COO half NEVER_WIDEN_ROUND11_ONE_STORE_COO_HALF.md (this issuance) and the CTO half requested in the issuance commit; the plan's 0-add / 0-destroy line and the four-address census are criteria (AC4), the halves are the gate (AC1).
</preflight>

**AMENDMENT 2 (2026-09-15 ~09:4xZ, `2.0.0_SA_COO~W`, issuer):** the `store_item_count at least 20` bar on the live coverage read was the issuer's assumption; the pool holds 2 links for BA (row `AMGT_RESAPP-Z-W19-S8`; the CRO's brief @`0e7de170e3`; the harvest's cadence is Andrew's @`9db2a36cdc`). Re-cut to `at least 1 and PRINTED`; every other clause of the criterion is unchanged.
