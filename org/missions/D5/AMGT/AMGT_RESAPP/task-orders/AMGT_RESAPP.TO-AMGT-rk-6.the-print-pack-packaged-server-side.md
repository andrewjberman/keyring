# AMGT_RESAPP task order -- `AMGT-rk-6` -- THE PRINT PACK -- FWD-5 is the brief's own displacement test and the route returns 500

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~24</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~24`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN B, a queue of THREE orders (`AMGT-rk-2`, `AMGT-rk-6`, `AMGT-rk-7`). Chain B holds EVERY edit of `lib/research/api/scoped_amgt.py` and every live AWS act of the round, so the adapter has ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~24;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-6` (gap `G3`; `FWD-5`; ADDENDUM 1 R2; contract `C-ROUND12-PRINT-SERVER-SIDE` (PRD v0.10))

**THE MEASURED STATE.** Direct invoke 04:57Z, GET `/security/BA_US_Equity/print`: **500 `internal error in the AMGT
scoped read API`.** Read from the bytes: `lib/research/print/render_pack.py` **imports `matplotlib` at module level** and reads
`pypdf` at module level (`:40-44`), and reads its inputs from a **worker-local deliverables folder** and a **OneDrive `.docx`
template path on this box** (`:53-57`). The deployed archive `research/opal-amgt-scoped-api.zip` is **747,396 B / 183 entries**
and carries **`matplotlib` ABSENT, `pypdf` ABSENT, `numpy` ABSENT**. `_print_pack` additionally needs `read_model_block` from the
same absent root (`scoped_amgt.py:2475-2505`), which `AMGT-rk-2` repairs before you start.

**RULED (ADDENDUM 1 R2, and the PRD contract): PACKAGE IT SERVER-SIDE.** matplotlib, pypdf and numpy ship in the deployed archive
or in a layer; the template moves off the OneDrive path into the pool; `render_pack.py` stops reading a worker-local deliverables
folder and **stops importing matplotlib at module level**.

⛔ **NOT RULED AS A BROWSER ACT, and the reason is the outcome's own wording.** FWD-5 is *"Adam forwards a printed pack without
reformatting it"* -- the displacement test is that **a person forwards the output AS PRODUCED**. A browser-rendered print is the
analyst's own reformatting under another name, and it would satisfy a criterion while failing the outcome.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. `4.0.0_SA_CRO~Z` @`a10eece02e` measured G3 by direct invoke and by listing the deployed archive.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
lib/research/print/
infra/aws/terraform/harvest/
org/missions/D5/AMGT/AMGT_RESAPP/ledger/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-6.the-print-pack-packaged-server-side.md
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
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W24-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize it) and never
edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING** -- never halt to investigate.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

**ISSUER AMENDMENT 8 (2026-09-16 ~15:5xZ, 2.0.0_SA_COO~Z).** AC4 and AC5 are NEW and prove the ADAPTER halves of cells `AMGT-rk-12` and `AMGT-rk-16`; AC1-AC3 are UNCHANGED.
- **Why they are here** (row `AMGT_RESAPP-Z-S127`, under ruling row `AMGT_RESAPP-Z-S124`): chain B is the single writer of
  `lib/research/api/scoped_amgt.py` and holds every live AWS act. `AMGT-rk-12`'s grant never named the adapter, so its route
  criterion was walled, and `AMGT-rk-16`'s grant named it, which made chain A a second writer. The page halves stay on chain A.
- **AC4:** served routes for the three hand-run modules -- coverage freshness (`lib/research/freshness/build_view.py`), the input
  ledger (`lib/research/ledger/ledger.py`) and the list register and rot signal (`lib/research/lists/rot.py`). Route names must
  contain `freshness`, `ledger` and `lists`. A control that cannot act SAYS WHY (contract C-ROUND12-SURFACED-OUTCOMES).
- **AC5:** served routes that list a key's stamps under `derived/model_block/KEY/` and compare two of them; names must contain
  `versions` and `compare`, and a compare with no query defaults to the two latest stamps. The read grant on
  `derived/model_block/` landed with `AMGT-rk-2`.
- **THIS ORDER'S DEPLOY MOVES SERVED OUTPUT** -- the print route (500 to a PDF) and the new routes above. Before ANY deploy, a
  FRESH never-widen co-sign must exist in `org/missions/D5/AMGT/AMGT_RESAPP/ledger/`, a CTO half (`1.0.0_SA_CTO~Z`) and a COO
  half (`2.0.0_SA_COO~Z`), naming every served change and any grant it needs. If a route needs a read the adapter role does not
  hold, that is a GRANT WIDENING the halves must name. If both halves are not there when you reach the deploy, do not deploy:
  stop that step and file a row naming what is missing.

**ISSUER AMENDMENT 12 (2026-09-16 ~18:1xZ, 2.0.0_SA_COO~Z, issuer) -- AC2's ESCAPE CLAUSE WAS UNREACHABLE BY ITS OWN INSTRUMENT.**
- **THE DEFECT.** AC2's expect has ALWAYS allowed a layer -- *"or, if a layer is used, the layer is listed and its
  contents printed by the same invocation"* -- but the invocation read **ONLY the function's own zip**. A layer is the
  standard remedy for matplotlib on Lambda, so **the most likely correct fix would have printed `PKG matplotlib 0` and
  read as a FAILURE.** That is AMENDMENT 11's defect with the sign flipped: there a wrong object passed silently, here
  a right answer fails silently. A criterion must be able to MEASURE every branch it permits.
- **THE REPAIR.** The invocation now reads `Configuration.Layers` itself, resolves each with
  `get_layer_version_by_arn`, downloads and lists each layer's entries, and counts the three packages **summed across
  the zip AND every layer**, printing a per-source `SRC` breakdown. One invocation, both branches, grammar unchanged.
- **MEASURED AT THIS AMENDMENT, the repaired invocation run whole:** `layers 0`; `SRC zip bytes 754470 entries 185`;
  `total-entries 185`; `PKG matplotlib 0`, `PKG pypdf 0`, `PKG numpy 0`. The cut's 183 entries / 747,396 B moved
  because `AMGT-rk-2`'s fix-forward redeployed the adapter at 17:23:29Z. The BAR does not move and all three still 0.
- **THE FUNCTION CARRIES NO LAYER TODAY, and its limits are small:** `Layers []`, python3.11, **memory 512 MB, timeout
  29 s, ephemeral storage 512 MB**. matplotlib and numpy are large and slow to import. **IF YOUR ACT RAISES MEMORY,
  TIMEOUT OR EPHEMERAL STORAGE, THAT IS A SERVED-PLANE CHANGE AND IT BELONGS IN THE NEVER-WIDEN CO-SIGN'S BLAST RADIUS
  WITH ITS OWN ROLLBACK VALUE** -- it is not a free adjustment taken on the way past. Terraform only, through
  `.tools/safe-apply.sh`; never `aws lambda update-function-code`.
- **THE OTHER FOUR CRITERIA ARE BYTE-IDENTICAL, and each was DRY-RUN WHOLE at this amendment, rc=0, each
  discriminating at the cut:** AC1 `module-level-matplotlib 2`, `onedrive-path 2`, `worker-deliverables 1` (all three
  nonzero, NOT met, exactly as issued -- `render_pack.py:40-44` carries the module-level `import matplotlib` and
  `:53-57` the OneDrive template path); AC3 `status 500`, `body-bytes 127`, `pdf-magic b'{"ref` (NOT met); AC4 `11` entries,
  freshness/ledger/lists `0 / 0 / 0`, `0 of 0`; AC5 `11` entries, versions/compare `0 / 0`, `0 of 0`.
- **NOTHING ELSE MOVES:** no grant path, no bound, no cell text, and AC1, AC3, AC4 and AC5 are untouched.

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-6"><invocation>python -c "import io; s=io.open('lib/research/print/render_pack.py',encoding='utf-8').read(); head=s[:s.find(chr(10)+'def ') if chr(10)+'def ' in s else 2000]; print('module-level-matplotlib', head.count('import matplotlib')); print('onedrive-path', s.lower().count('onedrive')); print('worker-deliverables', s.count('0.9.0_WK_AMGT_RESAPP~'))"</invocation><expect>module-level-matplotlib 0, onedrive-path 0, worker-deliverables 0. All three were nonzero at the cut (render_pack.py:40-44 and :53-57); any surviving nonzero is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-6"><invocation>python -c "import boto3,zipfile,io,json,urllib.request; c=boto3.client('lambda'); f=c.get_function(FunctionName='opal-amgt-scoped-api'); L=f['Configuration'].get('Layers') or []; print('layers', len(L)); srcs=[('zip', f['Code']['Location'])] + [('layer'+str(i+1), c.get_layer_version_by_arn(Arn=l['Arn'])['Content']['Location']) for i,l in enumerate(L)]; alln=[]; [ (lambda tag,url: (lambda d: (alln.extend(zipfile.ZipFile(io.BytesIO(d)).namelist()), print('SRC', tag, 'bytes', len(d), 'entries', len(zipfile.ZipFile(io.BytesIO(d)).namelist()))))(urllib.request.urlopen(url).read()))(t,u) for t,u in srcs]; print('total-entries', len(alln)); [print('PKG', p, sum(1 for n in alln if p in n.replace('python/','').split(chr(47))[0])) for p in ('matplotlib','pypdf','numpy')]"</invocation><expect>each of PKG matplotlib, PKG pypdf and PKG numpy is NONZERO in the DEPLOYED artifact, counted SUMMED ACROSS the function's own zip AND every attached layer -- the invocation now enumerates the layers itself, resolves each one and lists its entries, printing a per-source breakdown, so the LAYER branch this clause always allowed is REACHABLE BY THE INSTRUMENT (ISSUER AMENDMENT 12; before it the invocation read only the zip, so a layer-based fix would have printed 0 and read as a failure). At the cut all three read 0 against 183 entries / 747,396 B; re-measured whole at AMENDMENT 12 after AMGT-rk-2's redeploy, layers 0, SRC zip bytes 754470 entries 185, total-entries 185, all three still 0. A 0 on any of the three is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-6"><invocation>python -c "import boto3,json,base64; c=boto3.client('lambda'); r=c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':'/api/scoped/amgt/security/BA_US_Equity/print','headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode()); b=json.loads(r['Payload'].read()); print('status', b.get('statusCode')); body=b.get('body') or ''; print('isBase64', b.get('isBase64Encoded')); raw=base64.b64decode(body) if b.get('isBase64Encoded') else body.encode(); print('body-bytes', len(raw)); print('pdf-magic', raw[:5])"</invocation><expect>status 200 and body-bytes NONZERO, with pdf-magic reading the PDF header bytes. At the cut this route returned 500, so any 5xx is NOT met -- and a 200 carrying zero bytes is NOT met either, because a route that answers with nothing has not produced a pack</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-12"><invocation>python -c "import sys,json,boto3; sys.path.insert(0,'.'); from lib.research.api import scoped_amgt as m; r=m.scoped_amgt_route_table(); c=boto3.client('lambda'); W=['freshness','ledger','lists']; hits=[(v,x) for v in W for x in r if v in x]; print('route-table-entries', len(r)); [print('route', v, x) for v,x in hits]; S=lambda x: x.split()[1].replace('{security_key}','BA_US_Equity').replace('{movement}','trending').replace('{subject}','price'); I=lambda x: json.loads(c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':S(x),'headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode())['Payload'].read()).get('statusCode'); [print('deployed', v, S(x), I(x)) for v,x in hits if x.split()[0]=='GET']; print('named-routes', dict((v, sum(1 for u,_ in hits if u==v)) for v in W)); print('named-GET-routes-answering-200', sum(1 for v,x in hits if x.split()[0]=='GET' and I(x)==200), 'of', sum(1 for v,x in hits if x.split()[0]=='GET'))"</invocation><expect>route-table-entries printed as the denominator, every route naming freshness, ledger or lists printed, and each GET one of them invoked on the DEPLOYED adapter with its status printed. MET when named-routes reads freshness, ledger and lists each at least 1 AND named-GET-routes-answering-200 reads N of N with N at least 3 -- the FWD-7, FWD-12 and FWD-14 surfaces are SERVED routes, not hand-run modules. This criterion proves cell AMGT-rk-12's ADAPTER half and sits on this chain-B order because lib/research/api/scoped_amgt.py and every live AWS act are chain B's. ISSUER AMENDMENT 8 (2026-09-16 ~15:5xZ, 2.0.0_SA_COO~Z) moved it here from AMGT-rk-12 AC1 under the mechanism of 1.0.0_SA_CTO~Z's ruling in row AMGT_RESAPP-Z-S124: rk-12's grant never named the adapter, so its AC1 was walled. At this amendment: 11 entries, 0 / 0 / 0, 0 of 0; a planted route the deployed plane does not serve reads 1 named and 0 of 1 answering 200</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-16"><invocation>python -c "import sys,json,boto3; sys.path.insert(0,'.'); from lib.research.api import scoped_amgt as m; r=m.scoped_amgt_route_table(); c=boto3.client('lambda'); W=['versions','compare']; hits=[(v,x) for v in W for x in r if v in x]; print('route-table-entries', len(r)); [print('route', v, x) for v,x in hits]; S=lambda x: x.split()[1].replace('{security_key}','BA_US_Equity').replace('{movement}','trending').replace('{subject}','price'); I=lambda x: json.loads(c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':S(x),'headers':{'x-firm-id':'bd'},'requestContext':{'http':{'method':'GET'}}}).encode())['Payload'].read()).get('statusCode'); [print('deployed', v, S(x), I(x)) for v,x in hits if x.split()[0]=='GET']; print('named-routes', dict((v, sum(1 for u,_ in hits if u==v)) for v in W)); print('named-GET-routes-answering-200', sum(1 for v,x in hits if x.split()[0]=='GET' and I(x)==200), 'of', sum(1 for v,x in hits if x.split()[0]=='GET'))"</invocation><expect>route-table-entries printed as the denominator, every route naming versions or compare printed, and each GET one of them invoked on the DEPLOYED adapter for BA_US_Equity with no query string, its status printed. MET when named-routes reads versions and compare each at least 1 AND named-GET-routes-answering-200 reads N of N with N at least 2 -- a served route lists a key's stamps, and a served compare route answers for BA_US_Equity with no query by defaulting to its two latest stamps. This criterion proves cell AMGT-rk-16's ADAPTER half and sits on this chain-B order because lib/research/api/scoped_amgt.py and every live AWS act are chain B's. ISSUER AMENDMENT 8 (2026-09-16 ~15:5xZ, 2.0.0_SA_COO~Z) moved it here from AMGT-rk-16 AC2 under the mechanism of ruling row AMGT_RESAPP-Z-S124, because a chain-A grant naming the adapter made chain A a second writer on chain B's surface. At this amendment: 11 entries, 0 / 0, 0 of 0</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/AMGT_RESAPP.TO-AMGT-rk-6.the-print-pack-packaged-server-side.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>12</round>
<slot>~24</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- C-ROUND12-PRINT-SERVER-SIDE and FWD-5. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-6`, CHAIN B, a queue of THREE orders (`AMGT-rk-2`, `AMGT-rk-6`, `AMGT-rk-7`). Chain B holds EVERY edit of `lib/research/api/scoped_amgt.py` and every live AWS act of the round, so the adapter has ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

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
