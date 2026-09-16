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
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). A READ needs no grant; this block governs WRITES. Scratch is
  `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~24 <0.9.0_WK_AMGT_RESAPP~24@opal.agent>" -F <msgfile> -- <paths>`
  (the message file written by a NON-SHELL writer, never a printf or heredoc). Never push, merge, rebase, `checkout --`, `stash`
  or `clean`.

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

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-6"><invocation>python -c "import io; s=io.open('lib/research/print/render_pack.py',encoding='utf-8').read(); head=s[:s.find(chr(10)+'def ') if chr(10)+'def ' in s else 2000]; print('module-level-matplotlib', head.count('import matplotlib')); print('onedrive-path', s.lower().count('onedrive')); print('worker-deliverables', s.count('0.9.0_WK_AMGT_RESAPP~'))"</invocation><expect>module-level-matplotlib 0, onedrive-path 0, worker-deliverables 0. All three were nonzero at the cut (render_pack.py:40-44 and :53-57); any surviving nonzero is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-6"><invocation>python -c "import boto3,zipfile,io as _i; s=boto3.client('s3'); import json,subprocess; c=boto3.client('lambda'); f=c.get_function(FunctionName='opal-amgt-scoped-api'); import urllib.request; d=urllib.request.urlopen(f['Code']['Location']).read(); z=zipfile.ZipFile(_i.BytesIO(d)); names=z.namelist(); print('zip-bytes', len(d), 'entries', len(names)); [print('PKG', p, sum(1 for n in names if n.startswith(p))) for p in ('matplotlib','pypdf','numpy')]"</invocation><expect>each of PKG matplotlib, PKG pypdf and PKG numpy is NONZERO in the DEPLOYED archive (or, if a layer is used, the layer is listed and its contents printed by the same invocation). At the cut all three read 0 against 183 entries / 747,396 B, so a 0 on any of the three is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-6"><invocation>python -c "import boto3,json,base64; c=boto3.client('lambda'); r=c.invoke(FunctionName='opal-amgt-scoped-api', Payload=json.dumps({'rawPath':'/security/BA_US_Equity/print','requestContext':{'http':{'method':'GET'}}}).encode()); b=json.loads(r['Payload'].read()); print('status', b.get('statusCode')); body=b.get('body') or ''; print('isBase64', b.get('isBase64Encoded')); raw=base64.b64decode(body) if b.get('isBase64Encoded') else body.encode(); print('body-bytes', len(raw)); print('pdf-magic', raw[:5])"</invocation><expect>status 200 and body-bytes NONZERO, with pdf-magic reading the PDF header bytes. At the cut this route returned 500, so any 5xx is NOT met -- and a 200 carrying zero bytes is NOT met either, because a route that answers with nothing has not produced a pack</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/AMGT_RESAPP.TO-AMGT-rk-6.the-print-pack-packaged-server-side.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
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
