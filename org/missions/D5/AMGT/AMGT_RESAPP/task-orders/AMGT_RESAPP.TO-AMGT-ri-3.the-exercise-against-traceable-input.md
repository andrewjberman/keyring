# AMGT_RESAPP task order -- `AMGT-ri-3` -- THE EXERCISE -- the assembled route against traceable actual input

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ri-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~16</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~16`.** Same worktree, same portal checkout (now carrying YOUR `ri-1` repair on
branch `wk-amgt_resapp-10-1-portal`), same rules as `ri-1`; this is the SECOND order in your queue, handed to you
only after the producer (`ri-2`) and the mount (`ri-4`) are terminal on the live plane. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~16;`. **NEVER RUN AN INSTALL.** The `portal` gitlink NEVER moves.

## 1. THE CELL, inlined in full -- `AMGT-ri-3` (row `Z-S72`, serving FWD-9 and FWD-15)

**THE ROUTE HAS NEVER BEEN SEEN POPULATED, AND NOW IT CAN BE.** Round 9 (`rh-1`) proved the assembled page
compiles, builds and serves; `2.0.0_SA_COO~ZZZ` drove a real browser and the page mounted -- and rendered EMPTY
(25,476 bytes, byte-identical on two runs, the text "the daily job has not written a row"). Row `Z-S72`'s remedy:
*"Exercise the assembled route with traceable actual input and record response state plus populated output,
navigation and marking at the relevant boundary. Prove FWD9 marking beside its source evidence, not merely fiscal
numbers. Keep absent/error controls."* At this cut the two upstream causes of that empty render are repaired by
other cells in this round: the scheduled producer writes today's rows again (`ri-2`), and the scoped API is
mounted (`ri-4`). Your `ri-1` made the boundary honest. This cell puts the pieces together and RECORDS what the
route serves, on the planes an instrument can reach.

**THIS CELL HAS TWO HALVES, AND YOU HOLD ONE.** The mechanical half is yours: the rows exist (AC1), the deployed
adapter serves them and the exact payload is SAVED as the traceable input (AC2), the served route discriminates on
the module plane with the repaired components (AC3), the three harnesses still hold in the assembled checkout
(AC4), the production build emits the route (AC5). The BROWSER half -- populated output on screen, navigation
(a ranked row to the Security overlay), FWD-9's drafting-face marker beside a figure, and the error arm rendered
DISTINCT on the served route -- needs a browser-driving instrument no worker holds; `2.0.0_SA_COO~W` drives it,
files it as a row and a deliverable under `org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/`, and the
CVO grades it as this cell's judgment criterion (AC6). **Say plainly in your instance which half you settled.**

**WHAT THIS CELL DOES NOT CLAIM:** that a person has used the page (that is REALIZED, and it is L9/L10's); that the
served route is promoted (it is not; the page lives on a drain ref); anything about the price axis (its producer
is box-side and out of this round).

## 2. WHERE THIS CAME FROM

**ROUND 10**, decomposition s.18 (v1.1), cut by `2.0.0_SA_COO~W` on `1.0.0_SA_CTO~Z`'s L10 round-9 analysis
@`e9d1c6e6a5` (s.6: *"Together they close exactly the gap AC6 opened: a served route nobody has yet seen
populated."*). Edges: `ri-1 -> ri-3` (same portal checkout), `ri-2 -> ri-4 -> ri-3` (the live plane).

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
lib/research/api/scoped_amgt.py
org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-ri-3.the-exercise-against-traceable-input.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). Everything here is READ-ONLY for you except your own
  order (the status flip), the investigation file (rows) and your `deliverables/0.9.0_WK_AMGT_RESAPP~16/` home, which
  needs no entry. You write NO source in this order; if a criterion needs a source change, that is a row.
- **COMMITTING:** superproject only, `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~16 <0.9.0_WK_AMGT_RESAPP~16@opal.agent>" -F <msgfile> -- <paths>`,
  never staging `portal`.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO; no push, no gitlink move, no DEV/PROD merge, no deployment
(a local dev server is not a publish). `C-SERVER-SIDE-RANKING`. No vendor call. No non-ASCII in anything you write.
No install. **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a
row. **SURPRISE ROWS**, quoted from the channel's own header: *"a worker's row is `AMGT_RESAPP-Z-W<n>-S<k>` with
`<n>` its slot; `<k>` restarts at 1 per coordinate. `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every
new row."* Your coordinate is `W16`; continue its `<k>` sequence from where `ri-1` left it.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ri-3"><invocation>TODAY=$(date -u +%F); for d in "$TODAY" 2026-09-13; do printf "COUNT TRENDING_CHATTER#%s: " "$d"; .tools/aws dynamodb query --table-name opal-harvest-security-metrics --key-condition-expression "axis_date = :ad" --expression-attribute-values "{\":ad\":{\"S\":\"TRENDING_CHATTER#$d\"}}" --select COUNT --query Count --output text; done</invocation><expect>COUNT for today at least 1 and at most 10, and COUNT for 2026-09-13 exactly 0 -- the day the deployed producer failed, so the query is shown to discriminate. A today count of 0 means ri-2's rows are not there and this order STOPS on a BLOCKING row; nothing downstream can populate</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ri-3"><invocation>TODAY=$(date -u +%F); python -c "import json; ev={'version':'2.0','routeKey':'GET /api/scoped/amgt/lead-panel/rankings/{movement}/{subject}','rawPath':'/api/scoped/amgt/lead-panel/rankings/trending/chatter','rawQueryString':'','headers':{'x-firm-id':'opal-capital','x-user-role':'admin'},'queryStringParameters':{},'requestContext':{'http':{'method':'GET','path':'/api/scoped/amgt/lead-panel/rankings/trending/chatter'}},'pathParameters':{'movement':'trending','subject':'chatter'},'isBase64Encoded':False}; open('.scratch/ri3.ev.json','w').write(json.dumps(ev)); ev2=json.loads(json.dumps(ev)); ev2['queryStringParameters']={'as_of':'2026-09-13'}; ev2['rawQueryString']='as_of=2026-09-13'; open('.scratch/ri3.ev-control.json','w').write(json.dumps(ev2))"; for e in ri3.ev ri3.ev-control; do printf "INVOKE %s: " "$e"; .tools/aws lambda invoke --function-name opal-amgt-scoped-api --cli-binary-format raw-in-base64-out --payload "file://.scratch/$e.json" ".scratch/$e.out.json" --query "[StatusCode,FunctionError]" --output text; python -c "import json; d=json.load(open('.scratch/$e.out.json')); b=json.loads(d.get('body') or '{}'); print(' statusCode', d.get('statusCode'), 'axis', b.get('axis'), 'as_of', b.get('as_of_date'), 'row_count', b.get('row_count'), 'resolution', (b.get('resolution') or {}).get('resolution'), 'first-ticker', (b.get('rows') or [{}])[0].get('ticker'))"; done; mkdir -p "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~16" && cp .scratch/ri3.ev.out.json "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~16/rankings.trending.chatter.response.$TODAY.json" && python -c "import hashlib,glob; f=glob.glob('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~16/rankings.trending.chatter.response.*.json')[0]; print('SAVED', f, hashlib.sha256(open(f,'rb').read()).hexdigest()[:16])"</invocation><expect>ri3.ev -> 200 None, statusCode 200, axis TRENDING_CHATTER, as_of today, row_count at least 1 and equal to AC1's today count, resolution CROSSED, a first-ticker that is a real universe ticker; ri3.ev-control -> statusCode 200 with row_count 0 and as_of 2026-09-13 (the adapter reads the requested day and finds nothing, which is the negative arm); then a SAVED line naming the payload file with its sha256 -- THAT FILE IS THE TRACEABLE ACTUAL INPUT the browser half renders. A 401, a 5xx, or a row_count that disagrees with AC1 is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ri-3"><invocation>cd portal && (timeout 100 ./node_modules/.bin/vite --port 5176 --strictPort > ../.scratch/ri3.vite.log 2>&1 &) ; sleep 12; for h in 127.0.0.1 [::1]; do printf "BIND %s %s\n" "$h" "$(curl -sS -m 5 -o /dev/null -w "%{http_code}/%{size_download}" http://$h:5176/ 2>/dev/null || echo CONNREFUSED)"; done; H=$(curl -sS -m 5 -o /dev/null -w "%{http_code}" http://127.0.0.1:5176/ 2>/dev/null); if [ "$H" != "200" ]; then B="[::1]"; else B="127.0.0.1"; fi; printf "USING %s\n" "$B"; for m in /src/pages/SecurityAnalysis/SecurityAnalysis.tsx /src/pages/SecurityAnalysis/components/LeadPanel.tsx /src/pages/SecurityAnalysis/components/RankedList.tsx /src/pages/SecurityAnalysis/components/StarredList.tsx /src/api/endpoints/amgt-lead-panel.ts /src/pages/SecurityAnalysis/zzz-no-such-module-ri3.tsx; do printf "MOD %s %s\n" "$m" "$(curl -sS -m 5 -o /dev/null -w "%{http_code}/%{size_download}" http://$B:5176$m 2>/dev/null)"; done; printf "ROOT %s\n" "$(curl -sS -m 5 -o /dev/null -w "%{http_code}/%{size_download}" http://$B:5176/ 2>/dev/null)"; curl -sS -m 5 "http://$B:5176/src/pages/SecurityAnalysis/components/RankedList.tsx" 2>/dev/null | python -c "import sys; t=sys.stdin.read(); print('served-RankedList-mentions-read-failure', ('read fail' in t.lower()), 'bytes', len(t))"; head -3 ../.scratch/ri3.vite.log</invocation><expect>the dev server REACHABLE on one loopback address (a CONNREFUSED on the other beside a 200 is the expected reading on this device); the FIVE real modules each 200 with a transformed body of thousands of bytes while zzz-no-such-module-ri3.tsx returns the SPA fallback at the same small size as ROOT; and served-RankedList-mentions-read-failure True -- the SERVED module is the repaired one. SPA fallback on an unmatched path is correct vite behaviour and is the control, never a defect. Port 5176 is used because 5175 is the issuer's view server; a port collision is a row, not a reason to pick another silently</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ri-3"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/join.harness.mjs 2>&1 | tail -6; timeout 110 node src/pages/SecurityAnalysis/__harness__/chart.harness.mjs 2>&1 | tail -6; timeout 110 node src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs 2>&1 | tail -12; echo rc=$?</invocation><expect>the round-8 numbers UNCHANGED in this assembled checkout -- PRE-REPAIR fiscal 0/183 against REPAIRED fiscal 183/183 with header 13/13 on both arms; the chart's three payloads 3 of 3 pairwise distinct -- and the errorEmpty checks all reading their met values (error_differs_from_empty true, error_claims_no_daily_row false) with rc=0. This is a REGRESSION check: a number that MOVES is the finding and is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-ri-3"><invocation>cd portal && timeout 110 ./node_modules/.bin/vite build --logLevel info > ../.scratch/ri3.build.txt 2>&1; echo rc=$?; python -c "import glob,os; t=open('../.scratch/ri3.build.txt',encoding='utf-8',errors='replace').read(); ls=[l for l in t.splitlines() if 'dist/' in l]; print('emitted-assets', len(ls)); js=sorted(glob.glob('dist/assets/*.js')); toks={'ranked-read-failure':b'the ranked names could not be read','empty-day':b'daily job has not written a row','control':b'zzz-no-such-string-ri3-control'}; hits={k:[os.path.basename(f) for f in js if v in open(f,'rb').read()] for k,v in toks.items()}; print('js-assets', len(js)); [print('TOKEN', k, len(v), v) for k,v in hits.items()]; print('same-chunk', hits['ranked-read-failure']==hits['empty-day'] and len(hits['empty-day'])==1)"</invocation><expect>rc=0, emitted-assets above 20, js-assets above 20, TOKEN ranked-read-failure 1 and TOKEN empty-day 1 -- each of the route's two rendered texts (RankedList.tsx:107 and :127 at this cut) found in EXACTLY ONE emitted JS asset -- with same-chunk True (both in the SAME asset: the route's lazy chunk, which rollup names after the barrel index.ts as index-<hash>.js, never after the directory), and TOKEN control 0. AMENDED on row W16-S2: the committed version filtered emitted asset NAMES for SecurityAnalysis, a name the chunk cannot carry, so its empty list could not tell a dropped route from the passing case. A token in 0 assets, the two tokens in different assets, or the control above 0, is NOT met</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-ri-3" judgment="true"/>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** `AC6` is a judgment criterion:
record it `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO~W` and pointing at the browser
half's deliverable path (`org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/ROUND10_BROWSER_EXERCISE.md`, read
it if it exists when you run; say ABSENT if it does not), and offer no verdict. It asks whether the assembled
route, populated from the payload AC2 saved, is the thing a person would call working -- figures on screen, a
ranked row that navigates, FWD-9's marker beside its evidence, an error arm a person can tell from an empty day.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~16/AMGT_RESAPP.TO-AMGT-ri-3.the-exercise-against-traceable-input.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); keep the saved
payload and the vite log beside it; stop the dev server you started; flip `<status>` to `complete`; commit with
`--only -- <paths>`. Report once in your final message. **If a criterion cannot be met, leave the order OPEN and
file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>10</round>
<slot>~16</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>`1.0.0_SA_CTO~Z`'s L10 round-9 analysis @`e9d1c6e6a5` s.6 ("Z-S72 ... exercise the assembled route with traceable actual input, recording response state, populated output, navigation and marking"), the slug REMEDIATION_v9 @`1ae76e9c83` row `AMGT_RESAPP-Z-S72` (OPEN, `2.0.0_SA_COO~ZZZ`, carried by the successor lane), the round-9 order `AMGT-rh-1` (the browser half is the issuer's, the module plane is the worker's), decomposition s.18 (v1.1): edges ri-1 -> ri-3 and ri-2 -> ri-4 -> ri-3; fan-out s.18e. Andrew-direct 03:21:46Z "no promote", carried verbatim.</authority>

<preflight>
ALL RUN 2026-09-15 00:3x-00:4xZ at this cut (decomposition s.18g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (15.2 s of 90); REACHED-DENOMINATORS C1=23, C2=9, C3=12, C4=21, C5=334; BLIND on C4 and C5 in the tool's own voice. This cell starts a LOCAL dev server and stops it; it publishes nothing and deploys nothing.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s); 629 UNRESOLVABLE-RESOURCE, 51 GRANTED-BROAD excluded not cleared; BLIND on 266 calls in 26 role-UNMAPPED services. This cell makes two READ calls (a DynamoDB COUNT query and a Lambda invoke of the deployed adapter) under the operator's own credentials and takes no AWS act.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 32 commit pins, 9 repo paths, 6 file:line cites; 15 hex runs not parsed (named); T11 NOT RESOLVED (236 uncited siblings, CAP 25 declared); stage 4 disabled by the caller.
comp-cache: RUN (collisions) -- 481 of 481 portal files, 119 of 119 useQuery sites; this cell changes no key and no source.
comp-blast: DECLARED-NOT-APPLICABLE -- a read-only exercise of a route on a drain ref; nothing served moves.
</preflight>
