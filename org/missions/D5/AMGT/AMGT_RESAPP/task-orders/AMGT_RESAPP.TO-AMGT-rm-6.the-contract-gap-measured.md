# AMGT_RESAPP task order -- `AMGT-rm-6` -- THE CONTRACT GAP, MEASURED AND DRAFTED: every clipped text block on the six states, and a C13 overflow/wrap clause drafted for the CTO's ratification

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rm-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~145</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-37 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. Renders against a LOCAL vite dev server with the stubbed session and fixtures; no fetch to any origin but localhost.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~145`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`grep -c 'clippedTextBlocks' portal/scripts/ui-measure.mjs` (rm-1's detector has merged before you; 0 = BLOCKING row,
stop), and `grep -ci 'overflow\|truncat\|clip\|ellipsis\|wrap' portal/DESIGN.md` (expected 0 at the cut -- the gap). Every
Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~145;`. **NEVER RUN AN INSTALL.** Never push, merge, rebase,
`checkout --` or `clean`. Messages PURE ASCII via the Write tool. Scripts, logs and captures under
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/`, never `.scratch/`. **This cell commits NO portal
file**: its output is a deliverable.

## 1. THE CELL -- `AMGT-rm-6` (round 38, decomposition s.46) -- WAVE 1, after rm-1; MEASURE AND DRAFT, DO NOT EDIT THE CONTRACT

ADJUDICATION_v47 s.2.4: a provenance caption clipped mid-word could not be REJECTED because *"`DESIGN.md` has NO clause on
overflow, truncation, clipping, ellipsis or wrap -- measured, 0 hits"*, and *"a rejection on taste is not a rejection"*. The
round-37 analysis (item 6, amended @`18d29a99c7`): the amendment's CONTENT is `1.0.0_SA_CTO~Z`'s to specify and its EDIT
belongs to a named writer -- so this cell produces the INPUT to both: the measured cases and a draft clause.

**WHAT YOU BUILD, as `PROPOSAL_C13_overflow_and_wrap.md` in your deliverables:** (1) run rm-1's instrument on the six
states with `--scope main` and `--scope body` and collect every `clippedTextBlocks` sample (tag, text head, the clipped
tail, the owning container's overflow/text-overflow/white-space computed values, and the state); attribute each to a
file by its class string (the census patterns) or mark it UNATTRIBUTED with the reason; print the denominators (blocks
found vs attributed, per state, both scopes). (2) Read the estate's existing practice: census `truncate`, `text-ellipsis`,
`whitespace-nowrap`, `overflow-hidden`, `break-words`, `line-clamp-*` over `portal/src/**` (counts per class, files),
so the draft says what the portal DOES today, not only what it should. (3) DRAFT the clause as `C13` in DESIGN.md's own
voice and shape (read C11 and C12 for the register: a bold title, rules as bullets, each with its rationale, the
exception named): when text may be cut and how it must SAY so (an ellipsis at a word boundary with the full text reachable
on hover/focus or in the panel's disclosure), when it must WRAP (a provenance or disclosure line -- anything that carries a
fact -- NEVER clips), what a table cell does, and what the instrument grades (`clippedTextBlocks` == 0 inside main, or a
list of permitted ellipsis classes). (4) A CLOSING table: each measured case -> what the draft clause says about it.

## 2. BOUNDS

1. **The dev server:** from `portal/`, the bun binary at
   `C:/Users/Opal Bloomberg/AppData/Local/Microsoft/WinGet/Packages/Oven-sh.Bun_Microsoft.Winget.Source_8wekyb3d8bbwe/bun-windows-x64/bun`
   (`"<bun>" run dev --port 5185 > ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/dev.log 2>&1 &`),
   wait for `Local:` (up to 90 s), run, then stop it by the PID you recorded. Port **5185**.
2. **`portal/DESIGN.md` is READ-ONLY for this cell.** The clause is a DRAFT for `1.0.0_SA_CTO~Z`'s L4-R; the edit lands by
   the named writer once ratified. You write nothing under `portal/`.
3. **Measure, never fix**: no source file moves.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/scripts/ui-smoke.mjs
portal/scripts/ui-class-census.mjs
portal/src/**
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE only your deliverables; every other path is a read-only input.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rm-6"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5185 --scope main --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/clipped-main; echo "exit-main=$?"; node scripts/ui-contract-check.mjs --port 5185 --scope body --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/clipped-body; echo "exit-body=$?"</invocation><expect>THE CLIPPED BLOCKS MEASURED ON ALL SIX STATES IN BOTH SCOPES: the clippedTextBlocks column printed per state in each table with its samples in the JSONs (the list state's provenance caption expected among them unless rm-5 has merged first -- say which), six PNGs per scope; the graded columns are NOT this cell's and their FAIL cells are left standing; both exit codes printed (a graded FAIL exits 1 and does not fail this criterion)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rm-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; test -s org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/PROPOSAL_C13_overflow_and_wrap.md &amp;&amp; grep -c "^C13\|^## C13\|C13\." org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/PROPOSAL_C13_overflow_and_wrap.md &amp;&amp; head -80 org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/PROPOSAL_C13_overflow_and_wrap.md</invocation><expect>THE PROPOSAL, WITH ITS CASES AND DENOMINATORS: every measured clipped block listed with state, scope, owning file or UNATTRIBUTED-with-reason, and the container's computed overflow values; the estate census of truncate / text-ellipsis / whitespace-nowrap / overflow-hidden / break-words / line-clamp with counts and file totals; the C13 draft in DESIGN.md's register naming when text may be cut and how it must say so, when it must wrap (a fact-bearing line never clips), the table-cell rule, and what the instrument grades; the closing case-to-clause table</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rm-6"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; git status --porcelain | grep -v "^??" | wc -l &amp;&amp; git diff --name-only $(git merge-base HEAD DEV) | wc -l</invocation><expect>NO PORTAL FILE MOVED: 0 tracked changes in the nested repository and 0 files differing from its base -- this cell's output is the deliverable alone</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~145/AMGT_RESAPP.TO-AMGT-rm-6.the-contract-gap-measured.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
clipped-block counts per state and scope, the attributed/unattributed split, the estate census totals, the draft's rule
headings in one line each, the outer commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 1 (14:2xZ, before spawn, on row W140-S2):** AC1's two check runs were chained with `&&`; a graded FAIL
exits 1 and the second run would never start (the defect rm-1's AC3 carried). They are now separated with `;` and each exit
code is printed. Nothing else on the face moves.

**ISSUER NOTES:** wave 1, after rm-1 merges (its `clippedTextBlocks` detector is this cell's instrument). Item 6 of the
round-37 analysis as amended @`18d29a99c7`: content the CTO's, edit the named writer's; this cell supplies the measured
cases and the draft so neither is cut blind. The `DESIGN.md` edit is carried (s.46g), not cut.

**ISSUER CLOSE-OUT, 2.0.0_SA_COO~Z, 2026-09-24 ~14:5xZ.** Flipped by the ISSUER; the worker left the record face alone.
3 of 3 criteria PASS, proof-of-spec rc=0 VALID (re-run by this seat inside the worker's worktree C:/tmp/wk-amgt-38-145).
AC1: clippedTextBlocks 0 on all six states in BOTH scopes (24 of 24 measurement JSONs, samples empty; exit-main=1 / exit-body=1 on
the other cells' graded FAILs, printed) -- rm-5 had already fixed the one case the CVO saw. The historical case reproduced BY
READING portal 1f1555d2 (git show, never a checkout): the pre-rm-5 clip was UNSIGNALLED -- no overflow-hidden / clip / ellipsis on
the leaf, parent or grandparent; the mechanism was flex-shrink-0 plus flexbox's implicit min-width:auto with the cut at an ancestor
frame -- so rm-1's leaf-only clippedTextBlocks detector has a stated gap (C13 draft bullet 5), carried to the analysis. AC2: the
proposal with the live and historical denominators, the estate census (truncate 97/59, text-ellipsis 0/0, whitespace-nowrap 64/35,
overflow-hidden 121/69, break-words 4/2, line-clamp 4/3) and a five-bullet C13 draft in DESIGN.md's register for the CTO's L4-R;
DESIGN.md untouched. AC3: 0 tracked changes in the portal, 0 files off its base. No rows. Drained @7e26b17aec (deliverables only; the
gitlink did not move). The DESIGN.md edit stays carried (s.46g) until the CTO ratifies the text.

<status>complete</status>
<round>38</round>
<slot>~145</slot>
<fabric>site-z</fabric>
