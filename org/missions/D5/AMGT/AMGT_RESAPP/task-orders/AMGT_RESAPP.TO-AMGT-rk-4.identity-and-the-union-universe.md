# AMGT_RESAPP task order -- `AMGT-rk-4` -- IDENTITY AND THE UNION UNIVERSE -- resolve holdings WITHOUT converting unknown to false

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~25</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~25`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN C, a queue of FOUR orders (`AMGT-rk-4`, `AMGT-rk-5`, `AMGT-rk-13`, `AMGT-rk-14`). Chain C owns the identity set and everything that reads it, so the crosswalk and the peer rows have ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~25;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-4` (rows `W19-S6`, `W20-S13`, `W21-S3` (ARMED) and `W21-S4`; `FWD-13`; analysis s.5 C)

**THE MEASURED STATE.** The universe is **256 names: 33 MEASURED / 223 UNRESOLVED** (holding 167, coverage 86,
both 3). **167 of 170 holdings rows are unresolved** because the plane carries a **bare ticker** and the contract rightly forbids
guessing `US`. Separately, **23 of 33 peer sets are EMPTY** and the company-FIGI deduplication is broken.

⛔ **THE INPUT IS NAMED AND IT IS NOT A BARE-TICKER JOIN.** The Positioning chain **already resolves 164 of 164** holdings by
CUSIP / FIGI / SEDOL / Bloomberg security. **THAT CHAIN IS THE INPUT.** Resolving a population from a foreign key space when the
chain that feeds the consumer already carries the identity is the measured error this cell exists to avoid -- it is how 164
resolvable rows were once reported as 54 unresolvable.

⛔ **NEVER CONVERT UNKNOWN TO FALSE.** An unresolved vendor identifier stays **UNRESOLVED** and is never guessed. A holding that
cannot be resolved is carried as UNRESOLVED with its reason, never as "not held".

**DELIVER:** holdings resolved through the Positioning chain's identifiers; company-FIGI **deduplication** repaired; the **23
empty peer subjects** repaired (`4.0.0_SA_CRO~W` traced every one to a missing subject header / classification or an identity
join); every count **printed with its denominator**.

⚠ **TWO OF YOUR ROWS ARE ARMED.** `W21-S3` carries `hazard_standing: ARMED`. Read its `disarm_owner` and disarm it **in the same
turn** you satisfy it, by a NEW citing row -- never an in-place flip of the existing row.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. Analysis s.5 C names the Positioning chain as the INPUT; `4.0.0_SA_CRO~Z` measured the universe at 256 names, 33 MEASURED / 223 UNRESOLVED.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/
lib/research/peers/
lib/research/universe/
lib/research/scores/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-4.identity-and-the-union-universe.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant; this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~25 <0.9.0_WK_AMGT_RESAPP~25@opal.agent>" -F <msgfile> -- <paths>`
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
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W25-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it) and never
edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-4"><invocation>python -c "import json,boto3; s=boto3.client('s3'); import io; o=s.list_objects_v2(Bucket='opal-data-harvest', Prefix='universe/v1/').get('Contents',[]); k=sorted([x['Key'] for x in o])[-1]; d=json.loads(s.get_object(Bucket='opal-data-harvest',Key=k)['Body'].read()); rows=d if isinstance(d,list) else d.get('names') or d.get('rows') or []; import collections; c=collections.Counter((r or {}).get('resolution') for r in rows); print('universe_key', k); print('universe_rows', len(rows)); print('by_resolution', dict(c)); print('unresolved_holdings', sum(1 for r in rows if (r or {}).get('resolution')=='UNRESOLVED' and (r or {}).get('source')=='holdings'))"</invocation><expect>universe_rows printed as the denominator and by_resolution showing UNRESOLVED materially BELOW 59 and unresolved_holdings materially BELOW its value at this amendment. ISSUER AMENDMENT 2 re-cut this bar: the rows carry `resolution`, NOT `identity_status` (the original field read None on 250 of 250, so the bar could not be read at all), and the LIVE state at this amendment is already 250 rows / MEASURED 191 / UNRESOLVED 59 -- so the original bar ('MEASURED above 33') was ALREADY SATISFIED BEFORE THIS CELL DID ANYTHING and could not fail. The bar is read from the LIVE store AT THE CUT against the values printed here, and any row flipped from UNRESOLVED to a GUESSED identity is a hard fail, not a pass</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-4"><invocation>python -c "import io,glob; fs=sorted(glob.glob('lib/research/identity/*.py')); j=''.join(io.open(f,encoding='utf-8',errors='replace').read() for f in fs); print('identity-modules', len(fs)); print('positioning-input', j.lower().count('cusip') + j.lower().count('sedol') + j.lower().count('figi')); print('bare-ticker-join', j.count("guess") + j.count('+ \" US\"') + j.count("+ ' US'")); print('unresolved-preserved', j.count('UNRESOLVED'))"</invocation><expect>positioning-input NONZERO (CUSIP / SEDOL / FIGI are the identifiers the Positioning chain carries), bare-ticker-join 0, and unresolved-preserved NONZERO. Any surviving construction that appends a country code to a bare ticker is NOT met -- that is the guess the contract forbids</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-4"><invocation>python -c "import boto3,json; s=boto3.client('s3'); p=s.get_paginator('list_objects_v2'); ks=[o['Key'] for pg in p.paginate(Bucket='opal-data-harvest', Prefix='peers/v1/') for o in pg.get('Contents',[])]; import collections; n=0; empty=0; [ (lambda d: (globals().__setitem__('n',0)))(None) for _ in ()]; tot=0; emp=0; [ (lambda b: (tot.__class__, ))(None) for _ in ()]; res=[]; [res.append(json.loads(s.get_object(Bucket='opal-data-harvest',Key=k)['Body'].read())) for k in ks if k.endswith('.json')]; tot=len(res); emp=sum(1 for d in res if not (d.get('members') or [])); print('peer_objects', tot); print('empty_subjects', emp); print('populated', tot-emp)"</invocation><expect>peer_objects printed as the denominator (33 at the cut) and empty_subjects materially BELOW 23, with populated materially ABOVE 10. Read from the LIVE store AT THE CUT. An empty_subjects count still at 23 is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-4"><invocation>python -c "import io; t=io.open('org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md',encoding='utf-8').read(); print('W21-S3-mentions', t.count('W21-S3')); print('disarm-rows', t.count('DISARMED')); print('my-rows', t.count('AMGT_RESAPP-Z-W25-'))"</invocation><expect>W21-S3-mentions at least 2 -- the original ARMED row plus a NEW citing row that disarms it. A disarm is a NEW row citing the original, NEVER an in-place flip of the existing row, and the evidence names which row id carries the disarm</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/AMGT_RESAPP.TO-AMGT-rk-4.identity-and-the-union-universe.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>12</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- C-ONE-IDENTITY and C-UNION-UNIVERSE, FWD-13. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-4`, CHAIN C, a queue of FOUR orders (`AMGT-rk-4`, `AMGT-rk-5`, `AMGT-rk-13`, `AMGT-rk-14`). Chain C owns the identity set and everything that reads it, so the crosswalk and the peer rows have ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

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
