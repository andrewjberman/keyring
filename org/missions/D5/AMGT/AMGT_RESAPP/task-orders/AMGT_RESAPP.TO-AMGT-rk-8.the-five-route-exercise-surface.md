# AMGT_RESAPP task order -- `AMGT-rk-8` -- THE EXERCISE SURFACE -- round 11 captured two routes, so three surfaces could not be exercised at all

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~23</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~23`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN A, a queue of FIVE orders (`AMGT-rk-1`, `AMGT-rk-8`, `AMGT-rk-12`, `AMGT-rk-15`, `AMGT-rk-16`). Chain A holds EVERY portal edit of the round, so the portal has ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~23;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-8` (rows `W18-S20` and `W18-S5`; analysis s.5 E)

**THE MEASURED STATE.** Round 11's exact-input exercise took **TWO** captured routes. The header's description, the
publisher feed and the **whole Peers panel** ride `/overlay` and `/peers`, so they were **outside what could be exercised at all**
-- not failing, unexercised, which reads identical in a passing record.

**DELIVER:** both the **mechanical** and the **browser** exercise take **THE SAME FIVE ROUTES** captured from the **DEPLOYED**
adapter: `/overlay`, `/peers`, the rankings route, `/thesis`, `/posture`.

⭐ **AND THIS CELL CHANGED MEANING BECAUSE OF `AMGT-rk-1`.** Round 11's browser half exercised a **LOCAL vite serve** of portal
`0e153399`. Once the page is on DEV, the exercise runs against the integrated branch -- **the first time the front-end and the
deployed adapter are read together on the plane a person would actually use.** Exercising a local serve against a deployed adapter
was never the product; it was two halves of it in the same room.

⛔ **CAPTURE FROM THE DEPLOYED PLANE, NEVER FROM SOURCE**, and name the exact capture filenames (round 11's `W20-S1` was a
grain mismatch between a pre-census and a post-census, and `AMGT-rk-9` repairs that class at the issuer).

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. ADDENDUM 1 A1.4 chained this cell after `AMGT-rk-1` because round 11's browser half exercised a LOCAL vite serve.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/App.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-8.the-five-route-exercise-surface.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant; this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~23 <0.9.0_WK_AMGT_RESAPP~23@opal.agent>" -F <msgfile> -- <paths>`
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
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W23-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it) and never
edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

**ISSUER AMENDMENT 11 (2026-09-16 ~18:0xZ, 2.0.0_SA_COO~Z, issuer) -- THE FIFTH ROUTE IS NOT A ROUTE.** The property this cell asserts is UNCHANGED; only the OBJECT it is
asserted against is corrected, exactly as AMENDMENT 2 did when the route shape 404'd before any cell logic ran.
- **MEASURED at HEAD `c0131af3fe`:** `lib/research/api/scoped_amgt.py:2615`, `scoped_amgt_route_table()`, serves
  **ELEVEN** entries, **EIGHT** of them GET, and **NOT ONE of them is a `/posture` leaf** (`/coverage` is, at `:2627`).
  A direct GET on `/api/scoped/amgt/security/BA_US_Equity/posture` returns **404 `refused: true`**, 111 bytes.
- **AND THE PAGE NEVER CALLS ONE.** The client this cell exercises, `portal/src/api/endpoints/amgt-lead-panel.ts` on
  `AMGT-rk-1`'s integrated branch, fetches exactly `overlay`, `peers`, `thesis`, `coverage`, `print` and the two
  `lead-panel` routes. Across the page's 68 files on that branch there is NO posture fetch.
- **THE POSTURE SURFACE IS REAL AND IT IS SERVED NESTED.** The `/overlay` body (45988 bytes, measured this cut)
  carries a `posture` object beside `description`, `header_figures`, `peers`, `chatter`, `feed` and `identity`. So
  posture is NOT unexercised once `/overlay` is captured; it has no route of its own to capture.
- **THE REPAIR.** AC1's fifth route becomes `/security/{key}/coverage`, and AC2 now bars `overlay-has-posture True`,
  which exercises the posture surface WHERE IT IS ACTUALLY SERVED. The cell's count of FIVE does not move, and
  neither does its intent: the same five routes for both halves, captured from the DEPLOYED plane, nothing the page
  reads left unexercised. The swap moves the criterion ONTO that intent -- `/coverage` is in the page's read set and
  `/posture` never was.
- **THE CELL TEXT IS FROZEN AND STILL READS `/posture` IN ITS DELIVER LINE. DO NOT EDIT IT.** That line is the record
  of what was asked at the cut; this note is the correction of the object, and L9 grades the cell whole with both.
- **WHY THIS WAS NOT LEFT ALONE, THOUGH BOTH CRITERIA PASSED AS WRITTEN.** A 404 body is non-empty JSON, so
  `captured 5` and `nonempty-bodies 5` were BOTH MET ON A ROUTE THAT DOES NOT EXIST. The defect was SILENT, and it
  pointed straight at **AC4, the JUDGMENT criterion graded at L9**, whose evidence would have shown a REFUSED surface
  on a page that serves it. A grader reading that refusal grades the page unusable on a route the product does not
  have. An unpassable bar argues with you; this one would not have.
- **DRY RUN AT THE AMENDMENT, both criteria end to end, against the deployed adapter:** overlay 200 50197, peers 200
  19603, rankings 200 7319, thesis 200 221015, coverage 200 1696; `captured 5`; `files 5`; `nonempty-bodies 5`;
  `overlay-has-description True`; `overlay-has-posture True`; `peers-has-members True`.
- **NOTHING ELSE MOVES:** no grant path, no bound, no cell text, and AC3 and AC4 are byte-identical.

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-8"><invocation>python -c "import boto3,json,os; c=boto3.client('lambda'); routes=['/api/scoped/amgt/security/BA_US_Equity/overlay','/api/scoped/amgt/security/BA_US_Equity/peers','/api/scoped/amgt/lead-panel/rankings/trending/chatter','/api/scoped/amgt/security/BA_US_Equity/thesis','/api/scoped/amgt/security/BA_US_Equity/coverage']; os.makedirs('.scratch/rk8',exist_ok=True); n=0; [ (lambda p: (open('.scratch/rk8/'+p['f'],'wb').write(json.dumps(p['b']).encode()), print(p['r'], p['b'].get('statusCode'), len(json.dumps(p['b'])))))({'r':r,'f':r.strip(chr(47)).replace(chr(47),'_')+'.json','b':json.loads(c.invoke(FunctionName='opal-amgt-scoped-api',Payload=json.dumps({'rawPath':r,'headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode())['Payload'].read())}) for r in routes]; print('captured', len(os.listdir('.scratch/rk8')))"</invocation><expect>captured 5 -- all FIVE routes captured from the DEPLOYED adapter in one act, each with its printed statusCode and byte length, and each written to a named file under .scratch/rk8/. Round 11 captured 2, so any count below 5 is NOT met; the exact capture filenames are recorded in the evidence, never paraphrased. AMENDMENT 11: the fifth route is /coverage, which the adapter's own route table serves and the page's own client calls. Measured at the amendment, all five served 200 -- that is CONTEXT, NOT A BAR. The bar is CAPTURE: a route that refuses is still captured and still counted</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-8"><invocation>python -c "import json,glob,os; fs=sorted(glob.glob('.scratch/rk8/*.json')); print('files', len(fs)); tot=0; [print(os.path.basename(f), len(open(f,'rb').read())) for f in fs]; import io; bods=[json.loads(json.loads(io.open(f,encoding='utf-8').read()).get('body') or '{}') for f in fs]; print('nonempty-bodies', sum(1 for b in bods if b)); print('overlay-has-description', any('description' in (b or {}) for b in bods)); print('overlay-has-posture', any('posture' in (b or {}) for b in bods)); print('peers-has-members', any((b or {}).get('members') for b in bods))"</invocation><expect>files 5, nonempty-bodies 5, overlay-has-description True, overlay-has-posture True -- the header's description and the Peers panel are now INSIDE the exercised set, which is the whole point of widening from two routes to five. peers-has-members is PRINTED not barred, because 10 of 33 peer sets carried members at the cut and that population is AMGT-rk-4's to move, not this cell's. overlay-has-posture IS barred: the posture surface has NO route of its own and rides the /overlay body, so this is where it is exercised</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-8"><invocation>cd portal && timeout 110 node src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs 2>&1 | tail -16; echo rc=$?</invocation><expect>rc=0 with every prior check still at its met value -- a harness that drops a prior check to add a new one is NOT met. The browser half now runs against the DEV-integrated branch from AMGT-rk-1 rather than a local vite serve of a drain ref, and the evidence states which branch it ran on</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-8" judgment="true"><invocation>python -c "import json,glob,os; fs=sorted(glob.glob('.scratch/rk8/*.json')); print('routes_captured', len(fs), 'of 5'); [print('  ', os.path.basename(f), len(open(f,'rb').read()), 'bytes') for f in fs]; print('branch_under_judgment', open('portal/.git/HEAD').read().strip() if os.path.exists('portal/.git/HEAD') else 'see AC3 evidence')"</invocation><expect>the JUDGMENT is whether the Security Analysis page, on the DEV-INTEGRATED branch and against the DEPLOYED adapter, is a page a person could actually use today -- header and five tabs, each serving its figures or stating a CLASSED absent. This invocation prints the captured-route denominator (5) and the branch so the grader has the evidence; the verdict is not written here. GRADED AT L9 BY 3.0.0_SA_CVO~Z, NEVER SELF-GRADED</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** **AC4 IS A JUDGMENT CRITERION** -- graded at L9 by `3.0.0_SA_CVO~Z` and NEVER self-graded. Record its evidence and its denominator; do not write a verdict.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/AMGT_RESAPP.TO-AMGT-rk-8.the-five-route-exercise-surface.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>12</round>
<slot>~23</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- the FWD-15..FWD-19 page carrier and the exercise discipline in s.20b. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-8`, CHAIN A, a queue of FIVE orders (`AMGT-rk-1`, `AMGT-rk-8`, `AMGT-rk-12`, `AMGT-rk-15`, `AMGT-rk-16`). Chain A holds EVERY portal edit of the round, so the portal has ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

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
