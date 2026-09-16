# AMGT_RESAPP task order -- `AMGT-rk-7` -- THE ON-DEMAND PULL -- three pieces that exist and are not connected, and the consumer STAYS ON THE BOX

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~24</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~24`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN B, a queue of THREE orders (`AMGT-rk-2`, `AMGT-rk-6`, `AMGT-rk-7`). Chain B holds EVERY edit of `lib/research/api/scoped_amgt.py` and every live AWS act of the round, so the adapter has ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~24;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-7` (gap `G4`; `FWD-2`; ADDENDUM 1 R3 **as CORRECTED by ADDENDUM 2 C1**; contract `C-ROUND12-PULL-WIRED` (PRD v0.10))

**THE MEASURED STATE -- three pieces, zero wiring.** The page's Refresh calls `POST /api/scoped/amgt/refresh`; the
deployed adapter answers **501 "refresh has no queue carrier declared"** (`scoped_amgt.py:2463-2468`). The enqueue Lambda
`opal-research-pull-enqueue` hangs on `POST /api/private/research/pull`, **a route the page never calls** (0 references in
`amgt-lead-panel.ts`). The queue `opal-research-pull-requests` reads **0 visible, 0 in flight, no event-source mapping**.

⛔ **ADDENDUM 2 C1 CORRECTED THIS CELL AND THE CORRECTION IS LOAD-BEARING. DO NOT BUILD A LAMBDA CONSUMER.** The original ruling
said the consumer becomes an event-source-mapped Lambda. **IT CANNOT BE ONE:** `pull_consumer.py` calls the Bloomberg DAPI at
**`127.0.0.1:8194` ON THIS BOX**, so a Lambda would drain the queue and fail **every** message at `bloomberg_health`. The seam is
box-side by its own design and the code says so.

⭐ **AND FWD-2 HAS ALREADY WORKED END TO END ONCE:** `packs/NVDA_US_Equity/status.json` reads **LANDED**, requested 00:53:58Z,
landed 00:54:02Z, keys named. **The outcome is not unbuilt; it is unwired at the page and unactivated at the cadence.**

**DELIVER:** the adapter **declares the queue carrier** so `/refresh` stops answering 501; the page calls **the enqueue route it
actually needs**; the **consumer STAYS BOX-SIDE**. ⛔ **NO LAMBDA CONSUMER IS BUILT AND NO EVENT-SOURCE MAPPING IS CREATED.**
The consumer's **cadence is a card at Andrew, not a cell** -- it rides the same standing as the harvest mechanism.
⛔ **No alarm, monitor or freshness machinery rides along.** A wired queue is not a monitor; the standing moratorium binds.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. `4.0.0_SA_CRO~Z` @`a10eece02e` measured G4; ADDENDUM 2 C1 CORRECTED the ruling after finding the consumer's loopback dependency.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
lib/research/print/
infra/aws/terraform/harvest/
org/missions/D5/AMGT/AMGT_RESAPP/ledger/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-7.the-on-demand-pull-wired.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant; this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~24 <0.9.0_WK_AMGT_RESAPP~24@opal.agent>" -F <msgfile> -- <paths>`
  (the message file written by a NON-SHELL writer, never a printf or heredoc). Never push, merge, rebase, `checkout --`, `stash`
  or `clean`.


**ISSUER AMENDMENT 1 (2026-09-16 ~07:0xZ, `2.0.0_SA_COO~Z`, issuer).** This block did NOT name THIS ORDER'S OWN
FILE when the round was issued, so the order's final step -- flipping `<status>` to `complete` -- was a write
OUTSIDE the grant and was therefore NOT EXECUTABLE. Found by `0.9.0_WK_AMGT_RESAPP~28` on `AMGT-rk-10`, which did
exactly the right thing: it made the edit locally to confirm the gap, **REVERTED IT BYTE-FOR-BYTE**, and filed row
`AMGT_RESAPP-Z-W28-S1` rather than overriding its own `<paths>`. Measured across the round: **16 of 16 round-12
orders carried the defect and 0 of 13 round-11 orders did** -- the issuer's generator dropped a line the precedent
it was built from already had. The own-file entry is ADDED above. **NOTHING ELSE IN THE GRANT MOVES:** no new
surface, no widened directory, no change to any criterion, bound or cell text.

## 4. BOUNDS

PORTAL FROZEN both fabrics: COMMIT YES / PROMOTE NO. Andrew's "No portal promote necessary" removes the PROD promote from the
goal's definition of done; it does NOT license a promote and does NOT lift the freeze. **THE PORTAL DEV PUSH IS RESERVED** under
LD-0367/0368 and is NOT taken by any cell -- a shared branch moves only by `0.0.0_AB_MSTR~Z` on Andrew's word at the terminal.
**COLLECTION STAYS OFF:** three Windows tasks are DISABLED over a SEVEN-BODY article pool, and that is the measured consequence of
a RESERVED decision, not a defect to fix; no cell enables collection (@`9db2a36cdc`). **NO alarm, monitor, SNS/SES-send,
notification or freshness checker** -- standing moratorium; a wired queue is not a monitor. The ETF plane is READ-ONLY. Secrets
through `comp-secrets` only. **The one authorized Lusha enrich stays UNUSED** under the documented contract and contact data is
never stored. **No vendor call beyond what this order names**, and availability is never authorization. No non-ASCII in anything
you write. **PUSH: never.** Your work is LOCAL; LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired,
widened, or satisfied by a route this order did not name. **A count bar is read from the LIVE STORE AT THE CUT and PRINTS its
denominator** -- the honest denominators today are 7 article bodies over 3 names, 3 covered model-block keys of 89 coverage / 256
universe (plus NVDA, not covered), 5 filings/drafting pilot names, 33 peers objects with 10 carrying members, 2 posture keys.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W24-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it) and never
edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

**ISSUER AMENDMENT 7 (2026-09-16 ~15:3xZ, 2.0.0_SA_COO~Z).** AC3 is RE-CUT, AC4 is NEW (it proves cell `AMGT-rk-3`); AC1 and AC2 are UNCHANGED. No grant widens.
- **ONE SHAPE for this cell** (ruling row `AMGT_RESAPP-Z-S124`, decided by the issuer, row `AMGT_RESAPP-Z-S126`): the page's Refresh calls
  `POST /api/private/research/pull`, the route `opal-research-pull-enqueue` already serves on the shared portal API behind
  the portal authorizer. The adapter's `/refresh` DECLARES that carrier (the route and the queue
  `opal-research-pull-requests`) instead of answering 501, and SENDS NOTHING: the adapter role holds no SQS grant and none
  is added. The page half is NOT yours; it is `AMGT-rk-12` AC4 on chain A.
- **AC4, THE DATED FALLBACK** (ruling row `AMGT_RESAPP-Z-S125`): when no price generation exists at the requested date, the
  adapter serves the LATEST generation with `as_of_date`, `requested_as_of` and `dated: true`; an axis with no generation at
  all still reads a classed ABSENT. Under the value-carries-its-claim law a consumer must be able to reject a stale list.
- **BOTH CHANGES MOVE WHAT THE DEPLOYED ADAPTER SERVES.** Before any deploy of this order's adapter, a FRESH never-widen
  co-sign must exist in `org/missions/D5/AMGT/AMGT_RESAPP/ledger/` naming both behaviours in its blast radius: a CTO half
  (`1.0.0_SA_CTO~Z`) and a COO half (`2.0.0_SA_COO~Z`). If both halves are not there when you reach the deploy, do not
  deploy: stop that step and file a row naming what is missing.

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-7"><invocation>python -c "import io; s=io.open('lib/research/api/scoped_amgt.py',encoding='utf-8').read(); print('refresh-501-literal', s.count('refresh has no queue carrier declared')); print('queue-carrier-declared', s.count('opal-research-pull-requests')); print('lambda-consumer-words', s.lower().count('event_source_mapping') + s.lower().count('event-source-mapping'))"</invocation><expect>refresh-501-literal 0 (the refusal string is gone because a carrier is declared), queue-carrier-declared at least 1, and lambda-consumer-words 0 -- no event-source mapping is authored anywhere in the adapter. A surviving 501 literal, or any event-source-mapping wiring, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-7"><invocation>python -c "import boto3; c=boto3.client('lambda'); m=c.list_event_source_mappings(); rows=[x for x in m.get('EventSourceMappings',[]) if 'pull-request' in (x.get('EventSourceArn') or '')]; print('esm-on-pull-queue', len(rows)); q=boto3.client('sqs'); u=q.get_queue_url(QueueName='opal-research-pull-requests')['QueueUrl']; a=q.get_queue_attributes(QueueUrl=u, AttributeNames=['ApproximateNumberOfMessages','ApproximateNumberOfMessagesNotVisible'])['Attributes']; print('visible', a.get('ApproximateNumberOfMessages'), 'in-flight', a.get('ApproximateNumberOfMessagesNotVisible'))"</invocation><expect>esm-on-pull-queue 0 -- this is a NEGATIVE bar and it is the point of the cell: ADDENDUM 2 C1 ruled the consumer stays box-side because pull_consumer.py needs the Bloomberg DAPI at 127.0.0.1:8194, so ANY event-source mapping on that queue is NOT met and is a defect, not progress. The queue depths are printed as the denominator, not as a bar</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-7"><invocation>python -c "import boto3,json; c=boto3.client('lambda'); b=json.loads(c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':'/api/scoped/amgt/refresh','headers':{'x-firm-id':'bd','content-type':'application/json'},'body':json.dumps({'security_key':'BA_US_Equity'}),'requestContext':{'http':{'method':'POST'}}}).encode())['Payload'].read()); d=json.loads(b.get('body') or '{}'); t=json.dumps(d); print('status', b.get('statusCode')); print('refused', d.get('refused')); print('names-enqueue-route', t.count('/api/private/research/pull')); print('names-queue', t.count('opal-research-pull-requests')); print('reason', str(d.get('reason'))[:160])"</invocation><expect>status and body printed from the DEPLOYED adapter by invoke of POST /api/scoped/amgt/refresh. MET when status is neither 501 nor any other 5xx, refused is not true, names-enqueue-route is at least 1 and names-queue is at least 1. ONE SHAPE for cell AMGT-rk-7, stated identically on AMGT-rk-7 AC3 and AMGT-rk-12 AC4: the page's Refresh calls POST /api/private/research/pull, the route the enqueue Lambda opal-research-pull-enqueue serves on the shared portal API behind the portal authorizer; the adapter's /refresh DECLARES that carrier instead of answering 501 and sends nothing itself; the consumer stays box-side; no grant widens on either order. ISSUER AMENDMENT 7 (2026-09-16 ~15:3xZ, 2.0.0_SA_COO~Z) re-cut this clause on 1.0.0_SA_CTO~Z's ruling in row AMGT_RESAPP-Z-S124: the old AC3 read a portal file this chain cannot write and carried two branches in one criterion, so it is RETIRED, and the page half is AMGT-rk-12 AC4. At this amendment: status 501, refused True, names-enqueue-route 0, names-queue 0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-3"><invocation>python -c "import boto3,json,datetime; d=boto3.client('dynamodb'); ad=set(i.get('axis_date',{}).get('S','') for page in d.get_paginator('scan').paginate(TableName='opal-harvest-security-metrics', ProjectionExpression='axis_date') for i in page.get('Items',[])); dates=sorted(set(k.split('#')[1] for k in ad if k.startswith('TRENDING_PRICE#') and k.count('#')==2)); latest=dates[-1] if dates else None; c=boto3.client('lambda'); I=lambda path, q: json.loads(c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':path,'rawQueryString':q,'queryStringParameters':dict([q.split('=')]) if q else {},'headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode())['Payload'].read()); B=lambda o: json.loads(o.get('body') or '{}'); P='/api/scoped/amgt/lead-panel/rankings/'; nd=(datetime.date.fromisoformat(latest)+datetime.timedelta(days=1)).isoformat() if latest else '2026-01-02'; print('price_generation_dates', dates, 'latest', latest, 'requested_no_generation_date', nd); t=I(P+'trending/price', 'as_of='+nd); d=B(t); print('fallback_request', 'http', t.get('statusCode'), 'ranking_status', d.get('ranking_status'), 'requested_as_of', d.get('requested_as_of'), 'as_of_date', d.get('as_of_date'), 'dated', d.get('dated'), 'generation_id', d.get('generation_id'), 'rows', len(d.get('rows') or [])); e=B(I(P+'trending/price', 'as_of='+str(latest))); print('exact_date_request', 'as_of_date', e.get('as_of_date'), 'dated', e.get('dated'), 'rows', len(e.get('rows') or [])); n=B(I(P+'breakout/price', '')); print('no_generation_axis BREAKOUT_PRICE', 'ranking_status', n.get('ranking_status'), 'rows', len(n.get('rows') or []), 'dated', n.get('dated'), 'reason', str(n.get('ranking_reason'))[:100])"</invocation><expect>price_generation_dates, latest and requested_no_generation_date (the day after latest, read from the store) printed. MET when fallback_request reads http 200, ranking_status SERVED, rows NONZERO, generation_id present, as_of_date DIFFERENT from requested_no_generation_date, requested_as_of EQUAL to it, and dated true -- the adapter serves the LATEST generation WITH ITS as_of when no generation exists at the requested date, and the response carries its claim so the page renders the date and a consumer can reject a stale list; AND exact_date_request at latest reads dated false with rows NONZERO; AND BREAKOUT_PRICE, an axis with NO generation at all, still reads a classed ABSENT or EMPTY with rows 0 and dated not true. A fallback serving rows without requested_as_of and dated true, or serving rows on an axis with no generation, is NOT met. This criterion proves cell AMGT-rk-3's reader-side fallback and sits on this chain-B order because lib/research/api/scoped_amgt.py is chain B's single-writer surface. ISSUER AMENDMENT 7 (2026-09-16 ~15:3xZ, 2.0.0_SA_COO~Z) added it on 1.0.0_SA_CTO~Z's ruling in row AMGT_RESAPP-Z-S125. At this amendment: fallback_request ABSENT, requested_as_of None, dated None</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/AMGT_RESAPP.TO-AMGT-rk-7.the-on-demand-pull-wired.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>12</round>
<slot>~24</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- C-ROUND12-PULL-WIRED and FWD-2. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-7`, CHAIN B, a queue of THREE orders (`AMGT-rk-2`, `AMGT-rk-6`, `AMGT-rk-7`). Chain B holds EVERY edit of `lib/research/api/scoped_amgt.py` and every live AWS act of the round, so the adapter has ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

<preflight>
ALL RUN 2026-09-16 05:2x-05:3xZ at this cut (decomposition v1.6 s.20g).
comp-schedule: RUN -- 5 of 5 carriers within budget (16.25 s of 90); REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=21, C5=334; GATES ARMED 0 for this scope; C3 = 12 standing NEVER clauses (no alarm, no monitor, no freshness checker -- binding on every cell of this round); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (stats + service) -- 214 roles, 190 services, 1114 operations, 321 permission gaps; 478 .tf across 3 trees; 407 policy blocks attached, 27 NOT ATTACHED, 13 standalone. THE INSTRUMENT IS BLIND WHERE AMGT-rk-2 NEEDS IT: `comp-iam service opal-amgt-scoped-api` returns 3 operations, ALL UNRESOLVED-RESOURCE, and NO S3 row at all; the tool's own banner says the operation list is a FLOOR and never a deletion warrant. The round's one IAM delta is AMGT-rk-2's derived/model_block/ READ, and its never-widen co-sign reads the Terraform DIRECTLY rather than resting on this tool's silence.
comp-adversary: RUN (compose on the decomposition) -- 59 commit pins attempted, 58 verified, 1 UNVERIFIABLE (@9aef3734, inherited from an earlier section, not minted by s.20); 11 repo paths, 10 stable, 1 flagged; 15 file:line cites; 14 tool mentions; 26 hex runs not parsed as pins (named); 596 of 608 uncited siblings NOT digested (budget), 0 non-text. The round's adversarial surfaces are unchanged from round 11: filing text, vendor responses and pool objects are DATA inside a model prompt, never instructions; Posture is marked machine and read by no trade consumer.
comp-routes: RUN (stats) -- 7 origins, 29 behaviors, 14 rewrites, 22 API GW routes, 163 frontend endpoints (66 with URLs), 24 component bindings, 66 resolved; 50 of 66 edge auth, 24 of 66 API-GW auth. NONE of the 24 component bindings is a SecurityAnalysis component -- an INDEPENDENT corroboration of G1 on a different instrument from 4.0.0_SA_CRO~Z's git read.
comp-cache: RUN (collisions) -- 646 of 646 portal source files, 120 of 120 useQuery call sites captured, 0 unparseable, 17 shared keys, 0 TYPE MISMATCH. No cell of this round inherits a cache-key collision.
comp-blast: DECLARED-NOT-APPLICABLE -- the round's one live move is AMGT-rk-2's adapter redeploy and its derived/model_block/ grant, covered by a fresh never-widen co-sign, which is the narrower and correct instrument.
BATTERY LIMIT, STATED: comp-iam and comp-routes are DESIRED-plane (parsed Terraform and committed source) and cannot tell a declared grant or behaviour from a deployed one. Every bar in this round that asserts a grant or a route is graded on a LIVE READ or an INVOKE, never on a battery figure.
</preflight>
