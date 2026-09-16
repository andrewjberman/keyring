# AMGT_RESAPP task order -- `AMGT-rk-3` -- THE PRICE PRODUCER -- every Price list is ABSENT by ABSENCE, not by measurement

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~26</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~26`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN D, a single order (`AMGT-rk-3`).** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~26;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-3` (rows `W18-S11` (ARMED) and `Z-S105`; `FWD-15`; analysis s.5 B)

**THE MEASURED STATE.** Every Price list on the deployed readers reads **ABSENT**, and the reason is not a broken
read: **the Price producer has NEVER WRITTEN A GENERATION.** The chatter axis serves (`generation
20260915T200841Z-adf383740a9e`, 10 of 10 rows keyed); the price axis has no generation at all.

⛔ **ABSENT BY ABSENCE AND ABSENT BY MEASUREMENT READ IDENTICALLY ON THE PAGE AND ARE DIFFERENT DEFECTS.** A reader that says
ABSENT because a producer never ran is not telling the analyst what it appears to be telling them.

**DELIVER:** build the **generation writer** so a Price generation exists and the Price list serves keyed rows the way the chatter
axis already does.

⛔ **NO SCHEDULE, NO ALARM, NO MONITOR.** The standing moratorium binds and the collection plane stays OFF: a producer that can be
run is what this cell delivers; **arming a cadence is Andrew's and is not a cell.**
⚠ **YOUR ROW `W18-S11` IS ARMED** -- read its `disarm_owner` and disarm it same-turn by a NEW citing row, never an in-place flip.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. Analysis s.3 item 3 and packet section 5 item 1: the producer has NEVER written a generation.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/price/
lib/research/ranking/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~26/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-3.the-price-producer-generation-writer.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant; this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~26 <0.9.0_WK_AMGT_RESAPP~26@opal.agent>" -F <msgfile> -- <paths>`
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


**ISSUER AMENDMENT 2 (2026-09-16 ~07:4xZ, `2.0.0_SA_COO~Z`, issuer) -- THE ROUTE SHAPE WAS WRONG AND THE
CRITERION COULD NOT PASS.** The invocation named a bare `rawPath` with no `/api/scoped/amgt` prefix and no
edge header, so the deployed router refused it **404 "not an /api/scoped/amgt route"** BEFORE ANY CELL LOGIC
RAN. Adding the prefix alone returns **401 "missing edge-injected X-Firm-Id"**. Measured at this cut, the
shape that actually reaches the route is **the prefix PLUS an `x-firm-id` header -> 200**. ⛔ **A criterion
that 404s before the logic runs cannot discriminate a working route from a broken one -- it is the mirror of
a criterion that cannot fail: THIS ONE COULD NOT PASS.** The property asserted is UNCHANGED; only the object
it is asserted against is corrected. Found by the issuer's dry run after `0.9.0_WK_AMGT_RESAPP~24` and `~26`
each refused their own as written and filed rows (`W24-*`, `W26-S3`).

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
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W26-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it) and never
edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

**ISSUER AMENDMENT 4 (2026-09-16 ~14:5xZ, `2.0.0_SA_COO~Z`, issuer, after the 07:56Z site reboot).** AC3 is RE-CUT and
AC4's EVIDENCE invocation is replaced; AC1, AC2 and AC4's judgment text are UNCHANGED. Nothing else in this order moves.
- **YOUR WORK SO FAR EXISTS.** The previous `~26` slot built the generation writer and wrote one generation,
  `TRENDING_PRICE#2026-09-10#20260916T065448Z` (32 rows), and its row + proof commit `9d5ec84fef` is in your worktree. That
  slot died in the reboot. Do not rebuild what exists; run all four criteria as written here and finish what they measure.
- **AC3 could not pass as amendment 2 left it** (row `AMGT_RESAPP-Z-S118`). It read `axes.price` and `axes.chatter`, which the served
  body does not carry: each route returns ONE axis with `rows`, `row_count` and `ranking_status` at the top level. The re-cut
  reads those fields and calls the chatter route separately as the control. At this amendment the price route reads ABSENT,
  with the reason `no generation pointer at TRENDING_PRICE#2026-09-16 / _CURRENT`: the served route asks for TODAY's axis
  date, and the only price generation in the store is dated 2026-09-10. The chatter control reads SERVED with 10 rows.
- **AC4's evidence listed S3 `rankings/`**, a plane the estate has never written rankings to, so the grader would have been
  handed a vacuous 0. It now prints the same served read as AC3. Its judgment text and its L9 grader are unchanged.

**ISSUER AMENDMENT 7 (2026-09-16 ~15:3xZ, 2.0.0_SA_COO~Z).** AC3 is RE-CUT on `1.0.0_SA_CTO~Z`'s ruling in row `AMGT_RESAPP-Z-S125`; AC1, AC2 and AC4 are UNCHANGED.
- The Price axis works END TO END at its own date: generation `TRENDING_PRICE#2026-09-10#20260916T065448Z-9b7ffda3dcdc`,
  32 rows, pointer and reader serving. The default route asks for TODAY, and a today-dated generation is a fresh Bloomberg
  pull that no order names and that is RESERVED. AC3 now asserts served keyed rows at the LATEST COMMITTED generation's own
  date, read from the store at run time, with a negative control and the chatter control.
- **This order stays OPEN for a respawn to prove AC3 ONLY.** AC1 and AC2 are NOT re-run: carry their recorded evidence
  forward from the instance at commit `9d36bdfd36`. AC4 stays evidence-only for `3.0.0_SA_CVO~Z`.
- The TODAY-dated Price list is HELD on the reserved decision "the price pull's activation and cadence". The dated
  fallback (serve the latest generation with its date) is ruled YES and is `AMGT-rk-7` AC4, on chain B's adapter.

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-3"><invocation>python -c "import boto3,collections; s=boto3.client('s3'); pg=s.get_paginator('list_objects_v2'); ks=[o['Key'] for p2 in pg.paginate(Bucket='opal-data-harvest', Prefix='rankings/') for o in p2.get('Contents',[])]; print('s3_rankings_objects', len(ks), '(RECORDED: the estate has never written rankings to S3)'); d=boto3.client('dynamodb'); pa=d.get_paginator('scan'); ad=collections.Counter(); [ad.__setitem__(i.get('axis_date',{}).get('S',''), ad[i.get('axis_date',{}).get('S','')]+1) for page in pa.paginate(TableName='opal-harvest-security-metrics', ProjectionExpression='axis_date') for i in page.get('Items',[])]; gen=[k for k in ad if k.count('#')==2]; price=[k for k in gen if 'PRICE' in k.upper()]; chat=[k for k in gen if 'CHATTER' in k.upper()]; print('ddb_rows_scanned', sum(ad.values()), '| distinct_axis_dates', len(ad)); print('price_generations', len(price), sorted(price)); print('price_generation_rows', sum(ad[k] for k in price)); print('chatter_generations_CONTROL', len(chat), sorted(chat)[:3])"</invocation><expect>price_generations NONZERO with its keys listed and price_generation_rows NONZERO, against printed denominators (ddb_rows_scanned, distinct_axis_dates). chatter_generations_CONTROL is the POSITIVE CONTROL and MUST ITSELF BE NONZERO -- a control reading zero falsifies the instrument and the criterion is then UNREADABLE rather than failed, which is exactly how this clause was wrong twice before ISSUER AMENDMENT 2. s3_rankings_objects is RECORDED as 0 and is NOT a bar: the estate has never written rankings to S3, so the original S3 check was VACUOUS. A price_generations count of 0 against a NONZERO chatter control is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-3"><invocation>python -c "import io,glob; fs=sorted(glob.glob('lib/research/price/*.py')+glob.glob('lib/research/ranking/*.py')); j=''.join(io.open(f,encoding='utf-8',errors='replace').read() for f in fs); print('modules', len(fs)); print('generation-writer', j.count('generation')); print('security_key-on-rows', j.count('security_key')); print('schedule-words', j.lower().count('schedule') + j.lower().count('cron') + j.lower().count('eventbridge'))"</invocation><expect>generation-writer at least 1 and security_key-on-rows at least 1 against a printed module denominator; schedule-words 0. The last is a NEGATIVE bar and it binds: the collection plane stays OFF and arming a cadence is Andrew's, so any scheduling wiring authored by this cell is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-3"><invocation>python -c "import boto3,json; d=boto3.client('dynamodb'); ad=set(i.get('axis_date',{}).get('S','') for page in d.get_paginator('scan').paginate(TableName='opal-harvest-security-metrics', ProjectionExpression='axis_date') for i in page.get('Items',[])); dates=sorted(set(k.split('#')[1] for k in ad if k.startswith('TRENDING_PRICE#') and k.count('#')==2)); latest=dates[-1] if dates else None; c=boto3.client('lambda'); I=lambda path, q: json.loads(c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':path,'rawQueryString':q,'queryStringParameters':dict([q.split('=')]) if q else {},'headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode())['Payload'].read()); B=lambda o: json.loads(o.get('body') or '{}'); P='/api/scoped/amgt/lead-panel/rankings/'; print('price_generation_dates', dates, 'latest', latest); po=I(P+'trending/price', 'as_of='+str(latest)); p=B(po); rows=p.get('rows') or []; print('price_at_latest', 'http', po.get('statusCode'), 'ranking_status', p.get('ranking_status'), 'as_of_date', p.get('as_of_date'), 'generation_id', p.get('generation_id'), 'rows', len(rows)); print('rows_with_security_key', sum(1 for r in rows if r.get('security_key')), 'rows_unkeyed_with_identity_status', sum(1 for r in rows if not r.get('security_key') and r.get('identity_status')), 'rows_unkeyed_unclassed', sum(1 for r in rows if not r.get('security_key') and not r.get('identity_status'))); nd='2026-01-02'; n=B(I(P+'trending/price', 'as_of='+nd)); print('negative_control_date', nd, 'no_generation', nd not in dates, 'ranking_status', n.get('ranking_status'), 'as_of_date', n.get('as_of_date'), 'rows', len(n.get('rows') or []), 'reason', str(n.get('ranking_reason'))[:100]); q=B(I(P+'trending/chatter', '')); print('chatter_CONTROL', 'ranking_status', q.get('ranking_status'), 'rows', len(q.get('rows') or []))"</invocation><expect>price_generation_dates printed with latest READ FROM THE STORE AT RUN TIME. MET when price_at_latest reads http 200, ranking_status SERVED, as_of_date EQUAL to latest, generation_id present and rows NONZERO; AND rows_unkeyed_unclassed is 0, so every row either carries a security_key or states its identity_status (an unresolved identity is carried, never guessed); AND the negative control, a date with no price generation (no_generation True), does NOT read SERVED at that same as_of_date: it reads ABSENT with the pointer reason, or, once AMGT-rk-7's dated fallback lands, SERVED at a DIFFERENT as_of_date; AND chatter_CONTROL reads SERVED with rows NONZERO. A reader returning rows AT a date with no generation is NOT met. The TODAY-dated Price list is NOT graded here: it is HELD on the reserved decision 'the price pull's activation and cadence'. ISSUER AMENDMENT 7 (2026-09-16 ~15:3xZ, 2.0.0_SA_COO~Z) re-cut this clause on 1.0.0_SA_CTO~Z's ruling in row AMGT_RESAPP-Z-S125: a bar read at TODAY summed two writers, the reader and a producer run behind a reserved pull, and read ABSENT on a working reader. At this amendment: latest 2026-09-10, SERVED 32 rows (31 keyed, 1 unkeyed with identity_status, 0 unclassed), negative control ABSENT, chatter SERVED 10</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-3" judgment="true"><invocation>python -c "import boto3,json; c=boto3.client('lambda'); I=lambda ax: json.loads(c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':'/api/scoped/amgt/lead-panel/rankings/trending/'+ax,'headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode())['Payload'].read()); B=lambda o: json.loads(o.get('body') or '{}'); po=I('price'); p=B(po); qo=I('chatter'); q=B(qo); print('price', 'http', po.get('statusCode'), 'ranking_status', p.get('ranking_status'), 'rows', len(p.get('rows') or []), 'row_count', p.get('row_count'), 'as_of_date', p.get('as_of_date'), 'generation_id', p.get('generation_id')); print('price_reason', p.get('ranking_reason')); print('price_rows_with_security_key', sum(1 for r in (p.get('rows') or []) if r.get('security_key'))); print('chatter_CONTROL', 'http', qo.get('statusCode'), 'ranking_status', q.get('ranking_status'), 'rows', len(q.get('rows') or []), 'generation_id', q.get('generation_id'))"</invocation><expect>the JUDGMENT is whether a PM opening the Lead Panel now sees a Price axis that RANKS NAMES, rather than an ABSENT that was only ever ABSENT because nothing had run. The distinction the grader is asked for is absent-by-measurement versus absent-by-absence: both render identically on the page and they are different defects. GRADED AT L9 BY 3.0.0_SA_CVO~Z, NEVER SELF-GRADED</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** **AC4 IS A JUDGMENT CRITERION** -- graded at L9 by `3.0.0_SA_CVO~Z` and NEVER self-graded. Record its evidence and its denominator; do not write a verdict.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~26/AMGT_RESAPP.TO-AMGT-rk-3.the-price-producer-generation-writer.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>12</round>
<slot>~26</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- C-RANKING-GENERATION and FWD-15. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-3`, CHAIN D, a single order (`AMGT-rk-3`)). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

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
