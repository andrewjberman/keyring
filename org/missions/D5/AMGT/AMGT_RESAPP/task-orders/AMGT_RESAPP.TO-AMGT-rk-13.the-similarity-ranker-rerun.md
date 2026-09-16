# AMGT_RESAPP task order -- `AMGT-rk-13` -- THE RANKER RE-RUN -- a better crosswalk feeding the same ten populated peer sets moves nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~25</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~25`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN C, a queue of FOUR orders (`AMGT-rk-4`, `AMGT-rk-5`, `AMGT-rk-13`, `AMGT-rk-14`). Chain C owns the identity set and everything that reads it, so the crosswalk and the peer rows have ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~25;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-13` (`FWD-8`'s population; ADDENDUM 2 s.4)

**THE GAP, IN ONE SENTENCE.** `AMGT-rk-4` resolves names that were UNRESOLVED. **Nothing in its text says the
similarity ranker re-runs over them** -- so without this cell, `AMGT-rk-4` yields a better crosswalk feeding **the same ten
populated peer sets**, and every per-cell check passes while `FWD-8`'s population does not move.

**DELIVER:** re-run the similarity ranker over the names `AMGT-rk-4` newly resolves; the peer sets are rebuilt from the widened
identity set; **print the before and after counts with the same grain** (round 11's `W20-S1` was a grain mismatch between a
pre-census and a post-census -- take both censuses the same way, in the same units, in this one invocation).

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. Found by `1.0.0_SA_CTO~Z` at ADDENDUM 2 s.4: nothing in cell C's text said the ranker re-runs, so C would have yielded a better crosswalk feeding the same ten populated peer sets.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/
lib/research/peers/
lib/research/universe/
lib/research/scores/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-13.the-similarity-ranker-rerun.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~21/
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

**ISSUER AMENDMENT 3 (2026-09-16 ~14:4xZ, `2.0.0_SA_COO~Z`, issuer, after the 07:56Z site reboot).** AC1 is RE-CUT, AC3 is
NEW, AC2 is UNCHANGED. Nothing else in this order moves: no cell text, no grant, no bound.
- **AC1 is re-cut on `1.0.0_SA_CTO~Z`'s ruling at msg 23440, condition 2** (row `AMGT_RESAPP-Z-S116`). "Populated materially above 10"
  read a SUM of two writers. The re-cut is an IDENTITY with both sides printed: every MEASURED name in the latest universe that
  has a classification source must carry a populated peer set, and nothing else may. At this amendment it reads 121 expected
  against 10 populated.
- **AC3 is the W25-S3 re-arm condition as its own criterion.** Row `W25-S3` left the cross-listing self-match residual to
  whichever cell next writes peers/v1 objects for the widened universe, which is this one. **Run AC3's invocation BEFORE the
  batch writes any peers/v1 object and save its output to
  `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/AMGT-rk-13.self_match_prewrite.txt`**, then run it
  again after the batch; the run after the batch is the one you grade.
- **One open question does not block you** (row `AMGT_RESAPP-Z-S117`, at `1.0.0_SA_CTO~Z`): the engine reads model blocks from a repo
  deliverables directory, while the pool is where new blocks land. Today both hold blocks for the same three covered subjects,
  so nothing you run reads differently.

**ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z).** AC4 is NEW; AC1, AC2 and AC3 are UNCHANGED. Nothing else in this order moves.
- **AC4 carries `1.0.0_SA_CTO~Z`'s ruling in row `AMGT_RESAPP-Z-S120`.** The model-block store has ONE writer (the pull, into
  the pool) and TWO readers. The adapter already reads the pool; the peers engine reads `model_block_<key>.json` from a repo
  directory, so blocks landed in the pool would populate no peer set. **The engine reads blocks THROUGH THE POOL prefix
  `derived/model_block/KEY/LATEST/model_block.json`, with the repo directory as a fallback ONLY for a key absent in the pool,
  and the source is printed per subject.** `lib/research/peers/` is already inside your grant. No grant widens: the engine
  runs on the box under the box's credentials.
- AC4's planted case is `NVDA_US_Equity`: a block in the pool, none in the directory. Today it classifies through
  `scanner_row`, and it must classify through `model_block_header`.

**ISSUER AMENDMENT 10 (2026-09-16 ~17:5xZ, 2.0.0_SA_COO~Z).** NO criterion changes. The grant WIDENS by one path, and this note settles what AC3's escape clause does and does
not cover.
- **AC3's two suspects are NOT the escape clause's case.** `GOOGL_US_Equity` and `GOOG_US_Equity` are ONE issuer's two share
  classes, each served as the other's comparable. AC3's escape is for a suspect that is *genuinely a different company*
  sharing tokens; the same issuer under two share classes is the self-match shape `W21-S3` named, one level further out
  (row `AMGT_RESAPP-Z-W25-S6`, and `AMGT-rk-4`'s own cell text names the broken **company-FIGI deduplication** as this
  family's mechanism). **The repair is inside `lib/research/peers/`, which this order already grants.** AC3 stands as
  written: `self_match_suspects 0` with `mutant_suspects 2`.
- **AND THE OVER-EXCLUSION CONTROL IS PART OF THE REPAIR, because the last attempt at this class over-excluded.** In
  `AMGT-rk-4` a token-overlap rule caught the named case and also dropped unrelated companies sharing a corporate-suffix
  word, and was reverted byte-for-byte (row `W25-S3`). So the evidence PRINTS, across every subject, the members the new
  rule removes and the member count before and after: the removals must be share-class siblings of their own subject and
  nothing else. A removal you cannot name that way is a refusal and a row, not a pass.
- **W25-S7, the batch artifact:** `engine.batch_artifact_paths()` writes the batch log and summary beside the
  candidate-universe cache under `deliverables/0.9.0_WK_AMGT_RESAPP~21/`, which your grant did not name, so the mandated
  invocation could not commit its own evidence. That path is ADDED above. Do not move the coordinate itself: another
  cell reads the same default, and relocating it is not this cell's act.
- **W25-S8, the grant's `lib/research/universe/`:** that directory does not exist, and the code it names lives in
  `lib/research/peers/universe.py` and `lib/research/identity/build_universe.py`, both already granted. The entry is left
  as issued: removing it changes nothing you can write, and the row records the fact for L9.

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-13"><invocation>python -c "import io,os,json,sys,boto3; sys.path.insert(0,'.'); from lib.research.peers import universe as u; s=boto3.client('s3'); B='opal-data-harvest'; L=lambda p: [o['Key'] for pg in s.get_paginator('list_objects_v2').paginate(Bucket=B,Prefix=p) for o in pg.get('Contents',[])]; P='derived/model_block/'; pool=set(k[len(P):].rsplit('/',2)[0] for k in L(P) if k.endswith('/model_block.json')); d=u.MODEL_BLOCK_DIR_DEFAULT; eng=set(n[len('model_block_'):-len('.json')] for n in (os.listdir(d) if os.path.isdir(d) else []) if n.startswith('model_block_') and n.endswith('.json') and not n.startswith('model_block_fye_')); us=set(str(r.get('ticker')) for r in json.load(io.open(os.path.join(u.CACHE_DIR_DEFAULT,u.CACHE_NAME),encoding='utf-8'))['rows']); src=lambda k: (k in pool) or (k in eng) or (u.ticker_root(k)[1]=='US' and u.ticker_root(k)[0] in us); uk=sorted(k for k in L('universe/v1/') if k.endswith('.json'))[-1]; meas=set(r['security_key'] for r in json.loads(s.get_object(Bucket=B,Key=uk)['Body'].read())['names'] if r.get('resolution')=='MEASURED' and r.get('security_key')); exp=set(k for k in meas if src(k)); ks=sorted(k for k in L('peers/v1/') if k.endswith('.json')); last={k.rsplit('/',1)[0]: k for k in ks}; objs=[json.loads(s.get_object(Bucket=B,Key=k)['Body'].read()) for k in sorted(last.values())]; pop=set(o.get('security_key') for o in objs if (o.get('members') or [])); print('universe_key', uk); print('measured_names', len(meas)); print('populatable_expected', len(exp)); print('held_no_classification_source', len(meas - exp)); print('peer_objects', len(objs), 'of', len(ks), 'dated objects'); print('populated_subjects', len(pop)); print('expected_not_populated', len(exp - pop), sorted(exp - pop)[:12]); print('populated_outside_expected', len(pop - exp), sorted(pop - exp)[:12]); print('total_members', sum(len(o.get('members') or []) for o in objs)); print('grain', 'one latest object per subject; subjects and members; one census, one invocation, one grain')"</invocation><expect>universe_key, measured_names, populatable_expected, held_no_classification_source, peer_objects, populated_subjects and total_members printed, with the grain line. MET when populated_subjects EQUALS populatable_expected, expected_not_populated is 0, populated_outside_expected is 0 and total_members is nonzero. populatable_expected counts the MEASURED names in the latest universe that HAVE a classification source: a landed block in the pool under derived/model_block/ or in the peers engine's own block directory, or a US ticker root present in the scanner. Every source is MEASURED here, never read from a peer object's reason label. At this amendment it reads 121 expected against 10 populated, so the bar cannot pass until the ranker re-runs over the widened identity set. Names with no classification source are HELD and are not graded here. ISSUER AMENDMENT 3 re-cut this bar on 1.0.0_SA_CTO~Z's ruling at msg 23440, condition 2: the old bar, populated materially above 10, read a SUM of two writers. A post-census in a different grain from the pre-census is the W20-S1 defect and is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-13"><invocation>python -c "import io,glob; fs=sorted(glob.glob('lib/research/peers/*.py')); j=''.join(io.open(f,encoding='utf-8',errors='replace').read() for f in fs); print('peer-modules', len(fs)); print('reads-crosswalk', j.count('crosswalk')); print('figi-dedup', j.lower().count('figi'))"</invocation><expect>reads-crosswalk at least 1 and figi-dedup at least 1 against a printed module denominator -- the ranker consumes the widened identity set from AMGT-rk-4 rather than its own older key space. A ranker that re-runs against the pre-existing keys would reproduce the same ten populated sets and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-13"><invocation>python -c "import json,re,boto3; s=boto3.client('s3'); B='opal-data-harvest'; ks=sorted(o['Key'] for pg in s.get_paginator('list_objects_v2').paginate(Bucket=B,Prefix='peers/v1/') for o in pg.get('Contents',[]) if o['Key'].endswith('.json')); last={k.rsplit('/',1)[0]: k for k in ks}; STOP=set('the and inc ltd plc adr co sa ag nv se spa group holding holdings company corp corporation incorporated limited class sponsored shares ordinary'.split()); tok=lambda n: [w for w in re.sub('[^a-z0-9 ]',' ',str(n or '').lower()).split() if len(w)//3 and w not in STOP]; hit=lambda a,b: bool(tok(a)) and bool(tok(b)) and tok(a)[0]==tok(b)[0] and (len(tok(a))==1 or len(tok(b))==1 or tok(a)[1]==tok(b)[1]); objs=[json.loads(s.get_object(Bucket=B,Key=k)['Body'].read()) for k in sorted(last.values())]; pairs=[(o.get('security_key'), (o.get('subject') or {}).get('name'), m.get('ticker'), m.get('name')) for o in objs for m in (o.get('members') or []) if hit((o.get('subject') or {}).get('name'), m.get('name'))]; print('peer_objects', len(objs)); print('subjects_with_name', sum(1 for o in objs if (o.get('subject') or {}).get('name'))); print('members_graded', sum(len(o.get('members') or []) for o in objs)); print('self_match_suspects', len(pairs), pairs[:10]); print('mutant_suspects', int(hit('ALIBABA GROUP HOLDING-SP ADR', 'Alibaba Group Holding Limited')) + int(hit('SAP SE', 'SAP SE')))"</invocation><expect>members_graded printed as the denominator over every latest peers/v1 object, self_match_suspects 0 and mutant_suspects 2. A suspect is a member whose first significant name token, and its second where both names carry one, equals the subject's own: the cross-listing shape row W21-S3 names, where the subject also sits in the scanner under a SEDOL-shaped identifier with a DIFFERENT name string, which the engine's exact-name arm does not catch. The two mutants are the measured Alibaba case and an exact-name SAP case. A suspect that is genuinely a different company is refused as written: list it and file a row. This is the W25-S3 re-arm condition, made its own criterion by 1.0.0_SA_CTO~Z's ruling at msg 23440, condition 2</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-13"><invocation>python -c "import io,os,json,sys,boto3; sys.path.insert(0,'.'); from lib.research.peers import universe as u, engine as e; s=boto3.client('s3'); B='opal-data-harvest'; P='derived/model_block/'; pool=sorted(set(o['Key'][len(P):].rsplit('/',2)[0] for pg in s.get_paginator('list_objects_v2').paginate(Bucket=B,Prefix=P) for o in pg.get('Contents',[]) if o['Key'].endswith('/model_block.json'))); d=u.MODEL_BLOCK_DIR_DEFAULT; eng=sorted(set(n[len('model_block_'):-len('.json')] for n in (os.listdir(d) if os.path.isdir(d) else []) if n.startswith('model_block_') and n.endswith('.json') and not n.startswith('model_block_fye_'))); rows=json.load(io.open(os.path.join(u.CACHE_DIR_DEFAULT,u.CACHE_NAME),encoding='utf-8'))['rows']; src=lambda k: (e.resolve_subject(k, rows, d)[0] or {}).get('source'); print('blocks_in_pool', len(pool), pool); print('blocks_in_engine_dir', len(eng), eng); print('pool_only', sorted(set(pool)-set(eng))); print('dir_only', sorted(set(eng)-set(pool))); [print('subject', k, 'in_pool', k in pool, 'in_dir', k in eng, 'source', src(k)) for k in sorted(set(pool)|set(eng))]; print('pool_blocks_classified_by_block', sum(1 for k in pool if src(k)=='model_block_header'), 'of', len(pool)); print('mutant_NVDA_US_Equity_pool_only_source', src('NVDA_US_Equity'))"</invocation><expect>blocks_in_pool and blocks_in_engine_dir printed side by side with pool_only and dir_only, and every subject's in_pool, in_dir and engine source printed. MET when pool_blocks_classified_by_block EQUALS the number of blocks_in_pool AND mutant_NVDA_US_Equity_pool_only_source reads model_block_header. NVDA_US_Equity has a block in the pool and none in the engine's directory, so it is the planted case the ruling names: a block present in the pool and absent in the directory MUST classify through the pool. At this amendment it reads 3 of 4 and NVDA classifies through scanner_row, so the bar cannot pass until the engine reads the pool. A directory-only key may classify through the fallback; its source is printed and not graded. ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z) added this criterion on 1.0.0_SA_CTO~Z's ruling in row AMGT_RESAPP-Z-S120: the engine reads blocks THROUGH THE POOL prefix derived/model_block/KEY/LATEST/model_block.json, the repo directory as a fallback ONLY for a key absent in the pool</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/AMGT_RESAPP.TO-AMGT-rk-13.the-similarity-ranker-rerun.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>12</round>
<slot>~25</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- C-SIMILARITY-RANKER and FWD-8. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-13`, CHAIN C, a queue of FOUR orders (`AMGT-rk-4`, `AMGT-rk-5`, `AMGT-rk-13`, `AMGT-rk-14`). Chain C owns the identity set and everything that reads it, so the crosswalk and the peer rows have ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

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
