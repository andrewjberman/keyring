# AMGT_RESAPP task order -- `AMGT-rk-14` -- THE FIT -- it needs a CODE to read AND a VALUE to read for it, and repairing one end moves nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-14</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~25</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~25`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN C, a queue of FOUR orders (`AMGT-rk-4`, `AMGT-rk-5`, `AMGT-rk-13`, `AMGT-rk-14`). Chain C owns the identity set and everything that reads it, so the crosswalk and the peer rows have ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~25;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-14` (rows `W20-S9`, `W20-S10`, and (ADDENDUM 4 s.4) `W18-S13`, `W21-S5`, `W21-S6`; ADDENDUM 3 s.2)

**THE MEASURED STATE -- one defect in two places.** The presets carry **counts and weights instead of factor-code
lists**: DIVZ names **7 of its 13** codes, PFOE **0 of its 16**, so **22 of the 29 preset slots have NO CODE TO READ**. And R-1's
rows carry **NO scanner factor values at all**, because the ranker's loader keeps the 284-code set and **DROPS THE NUMBERS BY
DESIGN**.

⛔ **THE FIT NEEDS A CODE TO READ AND A VALUE TO READ FOR IT, AND BOTH ENDS ARE MISSING. THIS IS ONE CELL FOR THAT REASON.**
Name the 22 codes against rows carrying no values and the score is still ABSENT; retain values for codes the preset never names
and the score is still ABSENT. **A cell that fixes one end and passes its criterion is the failure mode here.**

**DELIVER, ALL FOUR (the last two folded in by ADDENDUM 4 s.4 on this cell's own logic -- same rows, same loader, same property:
a value that is present AND comparable):**
1. the presets name **EVERY** factor code they score under -- **13 of 13 DIVZ, 16 of 16 PFOE**, printed denominator beside each;
2. the loader **RETAINS** the factor values for exactly those codes on the R-1 rows -- **bounded by the presets**, not by the
   scanner's 284-code width;
3. the **CSC columns carry values WITH THEIR HORIZON LABELLED** -- trailing versus NTM, **never a fiscal-year label over an NTM
   figure** (5 of 17 columns marked present, ONE with values on the member rows, two of them trailing/NTM under fiscal-year
   labels);
4. the **size band comparable across currencies and vintages**, with the **FX basis and vintage NAMED**, or ABSENT with that
   reason.
**ABSENT carries a CLASSED reason** where a named code has no value for a name.

⛔ **THE CRITERION PRINTS FOUR DENOMINATORS PER NAME -- codes named, values present, horizons labelled, FX basis stated -- AND IS
NOT A BOOLEAN.** A fit that renders ABSENT everywhere satisfies "the tab renders" and proves nothing.
⛔ **RETIRING THE FIT IS NOT AVAILABLE TO YOU.** It is part of the surface Andrew approved (PRD s.3b), so retirement is an
ENDPOINT change and a card at Andrew. If it proves uncomputable on measured grounds, that is a ROW with the measurement attached.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. Found by `1.0.0_SA_CTO~Z` at self-drive tick 1 (ADDENDUM 3) and independently by `2.0.0_SA_COO~Z`'s L5 subtraction as open call U3; ADDENDUM 4 s.4 FOLDED the CSC and comparability rows in rather than giving them a cell.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/identity/
lib/research/peers/
lib/research/universe/
lib/research/scores/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-14.the-fit-both-ends.md
lib/research/posture/fit.py
lib/research/posture/tests/
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

**ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z).** The grant WIDENS by two entries, AC2 is RE-CUT, AC1 and AC3 read wider or fresher objects; AC4 is UNCHANGED.
- **THE PRESETS ARE THE `PRESETS` OBJECT IN `lib/research/posture/fit.py`**, which this order did not grant, so naming
  13 of 13 DIVZ and 16 of 16 PFOE codes was a write OUTSIDE the grant and not executable. The grant now names
  `lib/research/posture/fit.py` and `lib/research/posture/tests/`, and no other round-12 order names `lib/research/posture/`.
  The codes are READ from `portal/src/pages/SecurityScanner/constants.ts` (a read needs no grant); `fit.py`'s own
  docstring records which codes card 3 left unnamed.
- **AC2** globbed for preset files and found 0. It now reads `PRESETS` itself: DIVZ 7 of 13 named, PFOE 0 of 16.
- **AC3** read the first 40 sorted peer keys; it now reads one latest object per subject.
Found by running the queued orders' criteria before any worker reached them (row `AMGT_RESAPP-Z-S121`).

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-14"><invocation>python -c "import io,glob,json; fs=sorted(glob.glob('lib/research/scores/*.py')+glob.glob('lib/research/peers/*.py')+['lib/research/posture/fit.py']); j=''.join(io.open(f,encoding='utf-8',errors='replace').read() for f in fs); pj=''.join(io.open(f,encoding='utf-8',errors='replace').read() for f in sorted(glob.glob('lib/research/peers/*.py'))); print('modules', len(fs)); print('divz-codes-listed', j.count('DIVZ')); print('pfoe-codes-listed', j.count('PFOE')); print('preset-bounded-retention', pj.count('PRESETS') + pj.count('preset')); print('horizon-label', j.lower().count('trailing') + j.upper().count('NTM')); print('fx-basis', j.lower().count('fx') + j.lower().count('currency'))"</invocation><expect>divz-codes-listed and pfoe-codes-listed both nonzero, preset-bounded-retention at least 1, horizon-label nonzero and fx-basis nonzero, against a printed module denominator. All FOUR ends must appear -- this cell exists because repairing one end passes a criterion while the score stays ABSENT. ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z) widened this invocation's module set to include lib/research/posture/fit.py, where the presets live, and counts preset-bounded-retention in the peers modules only, where the loader is</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-14"><invocation>python -c "import sys; sys.path.insert(0,'.'); from lib.research.posture import fit as f; print('preset-home', f.__file__.replace(chr(92),'/').split('ajb_workspace/')[-1]); print('preset-source', f.PRESET_SOURCE[:120]); [print('preset', k, 'declared', v.get('declared'), 'codes_named', len(v.get('named') or []), 'unnamed_slots', len(v.get('unnamed') or []), 'codes', [x.get('code') for x in (v.get('named') or [])]) for k,v in sorted(f.PRESETS.items())]"</invocation><expect>preset-home and preset-source printed, and PER PRESET the count of factor codes NAMED against the count DECLARED, with the codes listed. MET when DIVZ reads codes_named 13 against declared 13 and PFOE reads codes_named 16 against declared 16, each with unnamed_slots 0. A preset naming fewer codes than it scores under is NOT met, and the two numbers are printed, never asserted. ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z) re-cut this clause to the presets' real home: the old invocation globbed presets*.json and *preset*.py under lib/research and found 0 files, because the presets are the PRESETS object in lib/research/posture/fit.py, which this order's grant did not name; the grant now names that file. At this amendment: DIVZ 7 of 13 with 6 unnamed, PFOE 0 of 16 with 16 unnamed</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-14"><invocation>python -c "import boto3,json; s=boto3.client('s3'); B='opal-data-harvest'; ks=sorted(o['Key'] for pg in s.get_paginator('list_objects_v2').paginate(Bucket=B,Prefix='peers/v1/') for o in pg.get('Contents',[]) if o['Key'].endswith('.json')); last={k.rsplit('/',1)[0]: k for k in ks}; res=[json.loads(s.get_object(Bucket=B,Key=k)['Body'].read()) for k in sorted(last.values())]; ms=[m for d in res for m in (d.get('members') or [])]; F=lambda m: m.get('factors') or {}; print('peer_objects', len(res), 'of', len(ks), 'dated objects'); print('member_rows', len(ms)); print('codes_named', sum(1 for m in ms if F(m))); print('values_present', sum(1 for m in ms if isinstance(F(m),dict) and any(v is not None for v in F(m).values()))); print('horizons_labelled', sum(1 for m in ms if m.get('horizon') or m.get('horizon_label'))); print('fx_basis_stated', sum(1 for m in ms if m.get('fx_basis')))"</invocation><expect>FOUR DENOMINATORS PRINTED against member_rows: codes_named, values_present, horizons_labelled and fx_basis_stated, each NONZERO. This is the cell's whole point and it is deliberately not a boolean -- at the cut values_present was effectively 0 because the loader dropped the numbers by design, so a nonzero codes_named with values_present 0 is NOT met and is exactly the one-end repair the cell forbids. ISSUER AMENDMENT 6 (2026-09-16 ~15:2xZ, 2.0.0_SA_COO~Z) made this invocation read ONE latest object per subject instead of the first 40 sorted keys, which after AMGT-rk-13's re-run would have been stale dated objects rather than the fit's output</expect></criterion>
for d in res:
  for m in (d.get('members') or []):
    n+=1
    f=(m.get('factors') or {})
    codes+= 1 if f else 0
    vals += 1 if any(v is not None for v in (f.values() if isinstance(f,dict) else [])) else 0
    hor  += 1 if m.get('horizon') or m.get('horizon_label') else 0
    fx   += 1 if m.get('fx_basis') or m.get('currency') else 0
print('member_rows', n); print('codes_named', codes); print('values_present', vals); print('horizons_labelled', hor); print('fx_basis_stated', fx)"</invocation><expect>FOUR DENOMINATORS PRINTED against member_rows: codes_named, values_present, horizons_labelled and fx_basis_stated, each NONZERO. This is the cell's whole point and it is deliberately not a boolean -- at the cut values_present was effectively 0 because the loader dropped the numbers by design, so a nonzero codes_named with values_present 0 is NOT met and is exactly the one-end repair the cell forbids</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-14" judgment="true"><invocation>python -c "import boto3,json; s=boto3.client('s3'); p=s.get_paginator('list_objects_v2'); ks=[o['Key'] for pg in p.paginate(Bucket='opal-data-harvest', Prefix='peers/v1/') for o in pg.get('Contents',[]) if o['Key'].endswith('.json')]; print('peer_objects_at_the_cut', len(ks)); print('presets_under_judgment DIVZ(13) PFOE(16)')"</invocation><expect>the JUDGMENT is whether the fit is COMPUTABLE for a real name -- a nonzero factor count on a real subject -- or is honestly ABSENT with a CLASSED reason for every name. A fit that renders ABSENT everywhere satisfies "the tab renders" and proves nothing, and a fit computed from codes with no values is worse than an honest absence. The denominators are printed by AC3; this clause names the verdict question. GRADED AT L9 BY 3.0.0_SA_CVO~Z, NEVER SELF-GRADED</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** **AC4 IS A JUDGMENT CRITERION** -- graded at L9 by `3.0.0_SA_CVO~Z` and NEVER self-graded. Record its evidence and its denominator; do not write a verdict.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~25/AMGT_RESAPP.TO-AMGT-rk-14.the-fit-both-ends.proof_of_spec.json`
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
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- the approved surface at PRD s.3b and the fit's own contract. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-14`, CHAIN C, a queue of FOUR orders (`AMGT-rk-4`, `AMGT-rk-5`, `AMGT-rk-13`, `AMGT-rk-14`). Chain C owns the identity set and everything that reads it, so the crosswalk and the peer rows have ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

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
