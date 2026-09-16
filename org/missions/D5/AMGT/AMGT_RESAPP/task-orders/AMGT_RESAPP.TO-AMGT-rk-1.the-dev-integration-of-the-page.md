# AMGT_RESAPP task order -- `AMGT-rk-1` -- THE DEV INTEGRATION -- the page exists only on a drain ref, and a page nobody is served is not a front-end

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~23</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~23`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt. Your first act prints
`git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a
BLOCKING row. **YOU HOLD CHAIN A, a queue of FIVE orders (`AMGT-rk-1`, `AMGT-rk-8`, `AMGT-rk-12`, `AMGT-rk-15`, `AMGT-rk-16`). Chain A holds EVERY portal edit of the round, so the portal has ONE writer.** Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~23;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-1` (gap `G1`; `FWD-15`..`FWD-19` carrier; ADDENDUM 1 R1)

**THE MEASURED STATE (`4.0.0_SA_CRO~Z` @`a10eece02e`, an independent seat on its own instruments):** the 48
`SecurityAnalysis` files and the `/security-analysis` route exist **ONLY** at portal `refs/drains/rj-portal` @`b616b759`.
Portal **DEV @`be8cf218` carries 0 of 48 and no route line**. PROD `portal-v2.1.179` has no such page. It is viewable only in a
developer worktree. `git merge-tree --write-tree DEV b616b759` returns **rc 0, 0 conflicts** -- it is ONE CLEAN MERGE from DEV,
and that merge has not been made.

⛔ **THIS IS ANDREW'S OWN NAMED FAILURE MODE:** *"have seen scenarios in building where the agents have a great PRD and forget to
actually produce some material part of the end product ... frontend doesnt exist"*. A page on a drain ref is a page nobody opens.

**RULED (ADDENDUM 1 R1):** *"No portal promote necessary"* removes the **PROD promote** from done. It does **NOT** remove the
**DEV integration**. The merge into portal DEV is a **COMMIT-class act** and the portal freeze reads **COMMIT YES / PROMOTE NO**,
so it is permitted.

**DELIVER, in this order:**
1. **The merge.** On a branch cut from portal `DEV`, merge `b616b759`. Merge, do not cherry-pick; do not rebase.
2. **TYPESCRIPT, WHICH `merge-tree` CANNOT SEE.** ⛔ **`merge-tree` MEASURES CONFLICTS, NOT TYPESCRIPT.** DEV is **212 commits
   past the merge-base**, so `tsc -b` is run **on the merged tree** and must come back clean. **Zero conflicts is not zero
   breakage** and a green merge-tree is not evidence about compilation.
3. **A render.** Build the merged tree and read that the route resolves and the page's header and five tab shells mount.
4. **The gitlink NEVER moves** and the superproject never stages `portal`.

⛔ **THE PUSH OF PORTAL DEV IS RESERVED AND IS NOT YOURS.** LD-0367/0368 put a shared-branch push with `0.0.0_AB_MSTR~Z` on
Andrew's word at the terminal. **You commit LOCALLY and state your push state as LOCAL.** A push is a hard stop and a BLOCKING row.

## 2. WHERE THIS CAME FROM

**ROUND 12**, decomposition **v1.6 s.20 @`8ac5ff6a57`** (cut and amended by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-11
analysis @`c708914c50` and its ADDENDUM 1 @`1db70c8e87`, ADDENDUM 2 @`06378dd3bd` and ADDENDUM 4 @`4055200e2f`; the round-11 slug
`REMEDIATION_v11.md` (drained into the tree by `3.0.0_SA_CVO~Z` @`d87181423c`); PRD **v0.10 @`49aedcf88b`, ADMITTED** -- both L4-R
halves SIGNED and current, measured at the cut. `4.0.0_SA_CRO~Z`'s product-existence audit @`a10eece02e` measured G1 on the served plane; ADDENDUM 1 R1 ruled it IN SCOPE and the round's FIRST cell.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/App.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-1.the-dev-integration-of-the-page.md
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

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-1"><invocation>cd portal && git log --oneline -1 --format="%h %s" | cat; git merge-base --is-ancestor b616b759 HEAD && echo CONTAINS_DRAIN=yes || echo CONTAINS_DRAIN=no; git ls-tree -r --name-only HEAD -- src/pages/SecurityAnalysis | wc -l; python -c "import io; a=io.open('src/App.tsx',encoding='utf-8').read(); print('route-lines', a.count('/security-analysis'))"</invocation><expect>CONTAINS_DRAIN=yes; the SecurityAnalysis file count is 48 or more (it was 0 on DEV at the cut -- print the number, never a boolean); route-lines at least 1. CONTAINS_DRAIN=no, a file count of 0, or route-lines 0 is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-1"><invocation>cd portal && timeout 110 ./node_modules/.bin/tsc -b > ../.scratch/rk1.tsc.txt 2>&1; echo rc=$?; python -c "import io; t=io.open('../.scratch/rk1.tsc.txt',encoding='utf-8',errors='replace').read(); print('bytes', len(t)); print('error-lines', t.count('error TS'))"</invocation><expect>rc=0 and error-lines 0 on the MERGED tree. This is the criterion merge-tree could not answer: DEV is 212 commits past the merge-base, so any nonzero error-lines count is NOT met and is the real finding</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-1"><invocation>cd portal && timeout 110 ./node_modules/.bin/vite build --logLevel info > ../.scratch/rk1.build.txt 2>&1; echo rc=$?; python -c "import glob,os; js=sorted(glob.glob('dist/assets/*.js')); tok={'page':b'SecurityAnalysis','control':b'zzz-no-such-token-rk1-control'}; print('js-assets', len(js)); [print('TOKEN', k, sum(1 for f in js if v in open(f,'rb').read())) for k,v in tok.items()]"</invocation><expect>rc=0, js-assets above 20, TOKEN page at least 1, TOKEN control 0. The control MUST read 0 -- a nonzero control means the probe matches anything and the page token proves nothing</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-1"><invocation>echo "gitlink: $(git ls-tree HEAD portal | cut -c13-22)"; git status --porcelain | cat; cd portal && git status --porcelain | cat; git rev-parse --abbrev-ref HEAD; git ls-remote origin DEV 2>&1 | cut -f1</invocation><expect>the superproject gitlink is UNCHANGED FROM ITS PRE-ACT VALUE, which is `be8cf218` measured live at this amendment (NOT `e85f6eb8`, which this criterion named until ISSUER AMENDMENT 2 -- a real commit, 217 behind DEV, correct one ROUND earlier), and the superproject status stages NO portal entry; the portal working tree is clean and HEAD is your own branch, never DEV; the ls-remote line is printed so your push state is MEASURED and reported as LOCAL. A moved gitlink is a hard stop and a BLOCKING row</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~23/AMGT_RESAPP.TO-AMGT-rk-1.the-dev-integration-of-the-page.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR
WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip `<status>` to `complete`;
commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order OPEN and file a row.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`, never `git stash`,
never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>12</round>
<slot>~23</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.10 @`49aedcf88b` (ADMITTED; ratified-text SIGNED `3.0.0_SA_CVO~Z`, brief SIGNED `4.0.0_SA_CRO~W`, both current at the cut) -- C-PAGE-LAYOUT and the FWD-15..FWD-19 page carrier. `1.0.0_SA_CTO~Z`'s L10 round-11 analysis @`c708914c50` + ADDENDA 1/2/4; decomposition v1.6 s.20 @`8ac5ff6a57` (cell `AMGT-rk-1`, CHAIN A, a queue of FIVE orders (`AMGT-rk-1`, `AMGT-rk-8`, `AMGT-rk-12`, `AMGT-rk-15`, `AMGT-rk-16`). Chain A holds EVERY portal edit of the round, so the portal has ONE writer). Cell set: s.20c + s.20h + s.20i; fan-out: s.20i.</authority>

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
