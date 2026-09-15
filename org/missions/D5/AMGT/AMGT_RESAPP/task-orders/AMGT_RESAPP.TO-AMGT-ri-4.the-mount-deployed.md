# AMGT_RESAPP task order -- `AMGT-ri-4` -- THE MOUNT, DEPLOYED -- the scoped AMGT read API exists on the live plane

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ri-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~17</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~17`.** Same worktree, same branch, same rules as `ri-2`, which you have just
finished; this is the SECOND order in your queue. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~17;`. ⛔ **This cell changes the world (a new Lambda, its IAM, and
ELEVEN new routes on the SHARED portal HTTP API). It is ORDERED exactly as `ri-2` was: gate (AC1), ledger open
with its sentinel COMMITTED, act, close, commit the close, then the grading reads.** Re-write the halt-gate session
file before the apply as you did for `ri-2`, and run the apply with `HALT_ACK=1`.

## 1. THE CELL, inlined in full -- `AMGT-ri-4` (row `Z-W11-S2`; the DEPLOY act of `AMGT-rf-2`, carried since round 7)

**THE MOUNT WAS DECLARED AND NEVER APPLIED, AND THE PAGE HAS BEEN ERRORING AT THE EDGE EVER SINCE.** Measured by
the round-10 issuer on 2026-09-15 00:2xZ, which no round had done: `aws lambda get-function-configuration
--function-name opal-amgt-scoped-api` -> `ResourceNotFoundException`; `apigatewayv2 get-routes --api-id 7k3ed8px20`
-> **85 routes by auto-pagination (25 is ONE PAGE of the paginated list -- CLAUDE.md 22a), 0 naming amgt**; `harvest/tfstate` (serial 25) carries no `scoped_amgt_api` module. So every
`/api/scoped/amgt/*` call the served page makes returns an edge error, which the boundary defect (`ri-1`) rendered
as "the daily job has not written a row". Round 7 (`rf-2`) delivered the terraform mount, the handler package, the
source-map entry and the IAM; its issuer ruled AC1 a SOURCE-plane criterion and directed that no world act be
taken (`scoped-amgt-api.tf` header, "STILL NOT DONE, and deliberately so"). Row `Z-W11-S2`'s remedy: *"Finish the
existing packaging/artifact and served-route obligation under the applicable grants and deploy contract."*

**WHAT ALREADY EXISTS (READ, do not rewrite):**
- `infra/aws/terraform/harvest/scoped-amgt-api.tf`: the role `opal-amgt-scoped-api-role` and its policy (Query /
  GetItem / BatchGetItem on the metrics table + `/index/*`; Query on the article store + `/index/*`; PutItem /
  DeleteItem on the metrics table for star markers; NO Scan, NO wildcard resource), the Lambda on
  `../modules/yang-lambda` (`function_name opal-amgt-scoped-api`, `artifact_key research/opal-amgt-scoped-api.zip`,
  python3.11, `lambda_function.lambda_handler`, 29 s, 512 MB, env `HARVEST_METRICS_TABLE` / `HARVEST_ARTICLES_TABLE`
  from the resources), ONE AWS_PROXY integration, the ELEVEN routes as one `for_each` set with
  `authorization_type = "CUSTOM"` and `authorizer_id = local.portal_authorizer_id` (`naqxlm`), one Lambda permission,
  and `terraform_data.scoped_amgt_route_count_check` (the 11-route precondition).
- `infra/aws/lambda/research/scoped_amgt_api/lambda_function.py`: the thin entrypoint delegating to
  `lib/research/api/scoped_amgt.py`; its docstring states the package layout: *"lib/research/{api,metrics,checkface,
  rules,watchlist}/ are copied into the package root alongside this file, preserving the lib/ prefix so
  `from lib.research...` resolves unchanged. No sys.path surgery."*
- `infra/aws/lambda/ci/lambda-source-map.json` entry `opal-amgt-scoped-api` (`artifact_s3_key research/opal-amgt-scoped-api.zip`).
- `infra/aws/terraform/harvest/build-and-upload.sh`: the enqueue function's build+upload, byte-parallel to
  `portal-content/` and `ticket-center/` -- the SHAPE yours follows (python `zipfile`, `content-sha256` metadata,
  `head-object` verify).
- `modules/yang-lambda/main.tf` reads `data "aws_s3_object" "artifact"` at PLAN time and takes
  `metadata["content-sha256"]` as `source_code_hash`: **the artifact must be uploaded BEFORE the plan, or the plan
  fails.**

**AMENDED 2026-09-15 ~02:0xZ ON ROW `AMGT_RESAPP-Z-W17-S2`:** this root's `module.scoped_amgt_api` data source reads the
artifact key at EVALUATION time, so `ri-2` (the producer, same root, same worker, before this order) now carries the
co-sign gate and the artifact build+upload as its own AC11/AC12. When you reach this order the artifact is normally
ALREADY uploaded by you under ri-2: AC2 re-runs the same script and, being deterministic, reproduces the same bytes and
the same content-sha256 (the head-object equality is the bar either way). **AC3's whole-root plan runs only after ri-2
is TERMINAL** (its six resources imported and applied in place); the co-sign's `19 to add, 0 to change, 0 to destroy`
is derived from that state. If ri-2 is not terminal when you reach AC3, STOP on a BLOCKING row -- a whole-root plan
taken before ri-2's imports counts the six live producer resources as adds and an apply would collide with them.

**DELIVER:**
1. **THE CO-SIGN GATE (AC1).** This deploy sits under CLAUDE.md NEVER-1 as the round-8 cut read it. Both halves
   must exist as files: `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_MOUNT_COO_HALF.md` (the issuer's,
   in your worktree) and `.../NEVER_WIDEN_ROUND10_MOUNT_CTO_HALF.md` (`1.0.0_SA_CTO~W`'s, which lands in the MAIN tree
   after your branch was cut -- so AC1 reads BOTH from the main tree via `git rev-parse --git-common-dir`). If the
   CTO half is ABSENT, this order stays OPEN on a BLOCKING row and you STOP at AC1: no artifact upload, no plan, no
   apply. The COO hands you nothing else until it lands.
2. `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` (written under ri-2 AC12; re-run here): zip
   `lambda_function.py` at the root plus the TRANSITIVE IMPORT CLOSURE of `lib.research` modules reachable from it
   (seed: the five packages `api/`, `metrics/`, `checkface/`, `rules/`, `watchlist/`; walk every packaged `.py` by AST,
   module- AND function-scope imports; add what is named from `lib/research/`; repeat to a fixed point), the
   `__init__.py` of `lib/`, `lib/research/` and every packaged package, preserving the `lib/` prefix, EXCLUDING
   `tests/` and `__pycache__`; the VERIFY step prints the closure and refuses on a non-empty missing list (AMENDED on
   row W17-S3: the five-directory enumeration missed `lib.research.price.axis`, `lib.research.print.render_pack` and
   `lib.research.provenance.render_print`, all function-scope imports); then upload with
   `--metadata content-sha256=<base64 sha256>` and `head-object` the key back. Deterministic zip entries (fixed
   date_time) so a re-run on unchanged inputs does not perturb the hash.
3. Snapshot the api's route keys BEFORE anything (AC4), then plan (AC3): **`19 to add, 0 to change, 0 to destroy`**
   and every created address one of the mount's. Anything else is a STOP and a row -- the CO-SIGN COVERS EXACTLY
   THAT ADD-SET (read the COO half; its table is the whole permitted set).
4. Open the deploy-completion entry (slug `amgt-scoped-api-mount`; legs L1 git, L2 s3-prefix = the artifact upload
   with its head-object line, L3 activation = the apply, L4 verify = the live routes and function, L5 verify = the
   direct invoke), COMMIT the entry and sentinel, `safe-apply` (AC5), close, commit the close.
5. Verify live (AC6), exercise the deployed adapter DIRECTLY with a synthetic HTTP API v2 event (AC7): the crossed
   ranked read `trending/chatter` carrying `x-firm-id: opal-capital` returns 200 with `row_count` and a `resolution`
   record, and the same event WITHOUT the header returns 401 -- the firm boundary failing closed. Save both
   responses in your deliverables folder.

**BOUNDS:** no vendor call; no non-ASCII in anything that reaches AWS; no monitor or alarm (no log subscription, no
alarm on the function); `authorization_type` is never NONE; no Scan grant; nothing touches `portal/`; the portal
freeze (COMMIT YES / PROMOTE NO) is unaffected by a backend mount and you do not test it by promoting anything.

## 2. WHERE THIS CAME FROM

**ROUND 10**, decomposition s.18 (v1.1), cut by `2.0.0_SA_COO~W` on `1.0.0_SA_CTO~Z`'s L10 round-9 analysis
@`e9d1c6e6a5`. Row `Z-W11-S2` (round 7, `0.9.0_WK_AMGT_RESAPP~11`) named the artifact upload and the served route as
the two halves the grant then could not pay; round 8's cut (s.16a) carried it because *"NEVER-1's closers are
CTO+COO and no never-widen sign-off exists"*; round 9 carried it again. The issuer's live measurement at this cut
made it a precondition of the round's exercise cell and supplied the COO half of the sign-off.

## 3. SURFACES -- what you may read and write

<paths>
infra/aws/terraform/harvest/
infra/aws/terraform/modules/yang-lambda/
infra/aws/lambda/research/scoped_amgt_api/
infra/aws/lambda/ci/lambda-source-map.json
lib/research/
lib/__init__.py
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_MOUNT_COO_HALF.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_MOUNT_CTO_HALF.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/mcp/sessions/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-4.the-mount-deployed.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). Everything under `lib/`, `modules/yang-lambda/`, the
  `scoped_amgt_api/` package, the source map and the two ledger halves are READ-ONLY for you; your ONE new file is
  the build-and-upload script under `harvest/`. `deliverables/0.9.0_WK_AMGT_RESAPP~17/` needs no entry.
- **COMMITTING:** as in `ri-2`. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. THE REFUSAL CLAUSE AND THE ROWS

A criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired, widened or
satisfied by a route this order did not name. Surprise rows: *"a worker's row is `AMGT_RESAPP-Z-W<n>-S<k>` with
`<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every
new row."* Your coordinate is `W17`; continue its `<k>` sequence from where `ri-2` left it; append inside the one
fenced JSON array; never edit an existing row; keep working.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ri-4"><invocation>MAIN="$(dirname "$(git rev-parse --git-common-dir)")"; for h in COO CTO; do f="$MAIN/org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_MOUNT_${h}_HALF.md"; printf "%s_HALF %s\n" "$h" "$(test -f "$f" && echo PRESENT || echo ABSENT)"; test -f "$f" && sed -n '1,5p' "$f"; done; printf "NEG %s\n" "$(test -f "$MAIN/org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND10_ZZZ_NOPE.md" && echo PRESENT || echo ABSENT)"</invocation><expect>COO_HALF PRESENT and CTO_HALF PRESENT, each with its first lines printed and the CTO half carrying a Verdict line that reads SIGNED or a ruling that NEVER-1 does not bind this act, and NEG ABSENT. STOP: CTO_HALF ABSENT means this order STOPS HERE -- file a BLOCKING row, record AC1 as FAIL, leave the order OPEN, do not proceed to any later criterion. Re-run this criterion only when the COO continues you</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ri-4"><invocation>timeout 115 bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh > .scratch/ri4.build.txt 2>&1; echo build-rc=$?; tail -12 .scratch/ri4.build.txt</invocation><expect>(idempotent when ri-2 AC12 already ran it: same bytes, same content-sha256) build-rc=0; a zipped: line with a non-zero byte count and an entry count above 20; a VERIFY line reporting the transitive lib.research import closure it packaged (module- and function-scope, to a fixed point) with a missing list of []; a head-object JSON for research/opal-amgt-scoped-api.zip whose Meta.content-sha256 EQUALS the printed local sha256 (b64) line and whose Size is non-zero; and OK: uploaded s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip. A missing-module list that is not empty, or a head-object whose metadata lacks content-sha256, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ri-4"><invocation>cd infra/aws/terraform/harvest && timeout 115 terraform plan -input=false -no-color -detailed-exitcode -out=../../../../.scratch/ri4.tfplan > ../../../../.scratch/ri4.plan.txt 2>&1; echo plan-rc=$?; python -c "import re; t=open('../../../../.scratch/ri4.plan.txt',encoding='utf-8',errors='replace').read(); m=re.search(r'Plan: (\d+) to add, (\d+) to change, (\d+) to destroy',t); print('PLAN', m.group(0) if m else 'NO-PLAN-LINE'); print('update-marks', t.count('will be updated in-place'), 'replace-marks', t.count('must be replaced'), 'destroy-marks', t.count('will be destroyed')); [print(' ', l.strip()[:110]) for l in t.splitlines() if l.strip().startswith('#') and 'will be created' in l]"</invocation><expect>PLAN Plan: 19 to add, 0 to change, 0 to destroy, update-marks 0, replace-marks 0, destroy-marks 0, plan-rc=2, and the created list containing ONLY addresses that begin with module.scoped_amgt_api., aws_iam_role.scoped_amgt_api, aws_iam_role_policy_attachment.scoped_amgt_api_logs, aws_iam_role_policy.scoped_amgt_api_grants, aws_apigatewayv2_integration.scoped_amgt_api, aws_apigatewayv2_route.scoped_amgt_api[ (eleven), aws_lambda_permission.scoped_amgt_api_apigw, terraform_data.scoped_amgt_route_count_check. Any other address, any change, any destroy, or an add count other than 19 is OUTSIDE the co-sign and is NOT met: no apply runs</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ri-4"><invocation>.tools/aws apigatewayv2 get-routes --api-id 7k3ed8px20 --query "Items[].RouteKey" --output text | tr "\t" "\n" | sort > .scratch/ri4.routes.before.txt; python -c "t=[l for l in open('.scratch/ri4.routes.before.txt').read().splitlines() if l.strip()]; print('routes-before', len(t), 'amgt-before', sum(1 for r in t if '/api/scoped/amgt/' in r)); print(chr(10).join(sorted(t)))" # rail-checked: a LIVE route-set census before/after an apply; comp-routes reads the declared CF/API config from the repo and cannot read the live key set</invocation><expect>routes-before N -- the MEASURED count, printed, with every key listed (85 at 1.0.0_SA_CTO~W's auto-paginated read, 22951, 2026-09-15 ~01:0xZ; 25 is ONE PAGE of this paginated list and is never the expectation) -- and amgt-before 0. Run this BEFORE the apply; a snapshot taken after cannot discriminate. AMENDED on row Z-S92: the committed version hardcoded the page</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-ri-4"><invocation>printf '%s' 0.9.0_WK_AMGT_RESAPP~17 > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"; test -f org/critical_paths/.open_deploys/amgt-scoped-api-mount.json && git log -1 --format=%h -- org/critical_paths/.open_deploys/amgt-scoped-api-mount.json; HALT_ACK=1 timeout 115 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/harvest apply -input=false -no-color ../../../../.scratch/ri4.tfplan > .scratch/ri4.apply.txt 2>&1; echo apply-rc=$?; tail -6 .scratch/ri4.apply.txt</invocation><expect>a commit hash for the COMMITTED sentinel, then apply-rc=0 and the line Apply complete! Resources: 19 added, 0 changed, 0 destroyed. A halt-gate BLOCK is recorded verbatim and is NOT met until its cause is read; any changed or destroyed count above 0 is a hard stop and a BLOCKING row</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-ri-4"><invocation>.tools/aws apigatewayv2 get-routes --api-id 7k3ed8px20 --query "Items[].RouteKey" --output text | tr "\t" "\n" | sort > .scratch/ri4.routes.after.txt; python -c "b=set(l for l in open('.scratch/ri4.routes.before.txt').read().splitlines() if l.strip()); a=set(l for l in open('.scratch/ri4.routes.after.txt').read().splitlines() if l.strip()); print('before', len(b), 'after', len(a), 'amgt-after', sum(1 for r in a if '/api/scoped/amgt/' in r), 'before-subset-of-after', b <= a, 'lost', sorted(b-a))"; .tools/aws lambda get-function-configuration --function-name opal-amgt-scoped-api --query "[FunctionName,State,Runtime,Timeout,MemorySize,Environment.Variables.HARVEST_METRICS_TABLE]" --output text # rail-checked: a LIVE route-set census before/after an apply; comp-routes reads the declared CF/API config from the repo and cannot read the live key set</invocation><expect>after EQUAL to before plus 11, amgt-after 11, before-subset-of-after True, lost [], then opal-amgt-scoped-api Active python3.11 29 512 opal-harvest-security-metrics -- where before is the MEASURED count AC4 printed, never a literal. A lost key, an after count other than before plus 11, or a State other than Active is NOT met. AMENDED on row Z-S92: the committed version hardcoded 25 and 36</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-ri-4"><invocation>python -c "import json; ev={'version':'2.0','routeKey':'GET /api/scoped/amgt/lead-panel/rankings/{movement}/{subject}','rawPath':'/api/scoped/amgt/lead-panel/rankings/trending/chatter','rawQueryString':'','headers':{'x-firm-id':'opal-capital','x-user-role':'admin'},'queryStringParameters':{},'requestContext':{'http':{'method':'GET','path':'/api/scoped/amgt/lead-panel/rankings/trending/chatter'}},'pathParameters':{'movement':'trending','subject':'chatter'},'isBase64Encoded':False}; open('.scratch/ri4.ev.json','w').write(json.dumps(ev)); ev2=dict(ev); ev2['headers']={}; open('.scratch/ri4.ev-nofirm.json','w').write(json.dumps(ev2))"; for e in ri4.ev ri4.ev-nofirm; do printf "INVOKE %s: " "$e"; .tools/aws lambda invoke --function-name opal-amgt-scoped-api --cli-binary-format raw-in-base64-out --payload "file://.scratch/$e.json" ".scratch/$e.out.json" --query "[StatusCode,FunctionError]" --output text; python -c "import json; d=json.load(open('.scratch/$e.out.json')); b=d.get('body') or ''; print(' statusCode', d.get('statusCode'), 'body-head', b[:240])"; done</invocation><expect>ri4.ev -> 200 None then statusCode 200 with a body whose head shows axis TRENDING_CHATTER, a resolution record (requested_axis, served_axis, resolution CROSSED) and a row_count field (its value is at least 1 when ri-2's rows exist for today, and is recorded whatever it is); ri4.ev-nofirm -> 200 None then statusCode 401 with a body naming the missing edge-injected X-Firm-Id. A FunctionError on either, a 5xx statusCode, or a 200 on the no-firm event (the boundary failing OPEN) is NOT met. Copy both .out.json files into your deliverables folder</expect></criterion>
  <criterion id="AC8" cell_refs="AMGT-ri-4"><invocation>python -c "import glob,os; fs=glob.glob('org/critical_paths/change_management/*amgt-scoped-api-mount*.md'); print('entries', len(fs)); [print(f, 'CLOSED-in-head', 'CLOSED' in open(f,encoding='utf-8').read()[:800]) for f in fs]; print('sentinel-present', os.path.exists('org/critical_paths/.open_deploys/amgt-scoped-api-mount.json'))"; git log -1 --format="%h %s" -- org/critical_paths/change_management/</invocation><expect>entries 1, CLOSED-in-head True, sentinel-present False (ABSENT is the closed state), and the close COMMITTED. Run this LAST, after the close commit</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~17/AMGT_RESAPP.TO-AMGT-ri-4.the-mount-deployed.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7,AC8` (rc 0 is the verdict); save the
plan text, the apply text, both route snapshots and both invoke responses beside it; flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once in your final message. **If AC1 reads CTO_HALF ABSENT, that IS your
final report on this order: OPEN, BLOCKING row, nothing applied.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>10</round>
<slot>~17</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-9 analysis @`e9d1c6e6a5` (round 10 on the COO's recut, one issuance; the COO "adds or recuts task orders as its own judgment dictates", spine L10); row `AMGT_RESAPP-Z-W11-S2` (`0.9.0_WK_AMGT_RESAPP~11`, round 7) and its OPEN remedy in REMEDIATION_v7 ("Finish the existing packaging/artifact and served-route obligation under the applicable grants and deploy contract"), carried at s.16a and s.17a for want of a never-widen sign-off; the round-10 issuer's live measurement 2026-09-15 00:2xZ (function absent; 25 routes, 0 amgt; no module in harvest/tfstate) recorded at decomposition s.18a; the COO half `ledger/NEVER_WIDEN_ROUND10_MOUNT_COO_HALF.md` (this issuance) and the CTO half requested by message at the cut. CLAUDE.md NEVER-1 and NEVER-2. Cell set: s.18a; fan-out: s.18e.</authority>

<preflight>
ALL RUN 2026-09-15 00:3x-00:4xZ at this cut (decomposition s.18g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (15.2 s of 90); REACHED-DENOMINATORS C1=23, C2=9, C3=12, C4=21, C5=334; C2 = 9 OPEN deploy-ledger entries (this cell opens one and closes it inside the round); C3 = 12 standing NEVER clauses; BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s); it NAMES opal-amgt-scoped-api (role opal-amgt-scoped-api-role) at lib/research/api/scoped_amgt.py:312, :334 and :691 as UNRESOLVED-RESOURCE -- the three DynamoDB reads this mount serves, whose grants are the resource references in scoped-amgt-api.tf; the lens cannot resolve a table name read from an env var, stated not cleared. 629 UNRESOLVABLE-RESOURCE, 51 GRANTED-BROAD excluded not cleared; BLIND on 266 calls in 26 role-UNMAPPED services.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 32 commit pins, 9 repo paths, 6 file:line cites; 15 hex runs not parsed (named); T11 NOT RESOLVED (236 uncited siblings, CAP 25 declared); stage 4 disabled by the caller.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE with the reason: a PURE ADD on the shared portal API from the harvest root's own state; the 25 existing routes live in other roots' state and cannot be touched by this plan; the blast radius per key and the rollback per key are the never-widen halves, and the 0-change / 0-destroy plan line is a criterion.
</preflight>
