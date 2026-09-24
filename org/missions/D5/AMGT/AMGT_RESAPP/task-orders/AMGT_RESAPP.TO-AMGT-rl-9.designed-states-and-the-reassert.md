# AMGT_RESAPP task order -- `AMGT-rl-9` -- THE FOUR DESIGNED STATES EVERYWHERE, AND THE CONTRACT CHECK RE-ASSERTED OVER THE MERGED PAGE: six states PASS, six PNGs for a person to read

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rl-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~138</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the L1 brief at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. Renders against a LOCAL vite dev server with the stubbed session and fixtures; no fetch to any origin but localhost.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~138`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`test -f portal/scripts/ui-contract-check.mjs && echo INSTRUMENT-OK`, and print
`node portal/scripts/ui-class-census.mjs portal/src/pages/SecurityAnalysis | tail -1` -- the page-wide census over the
MERGED page you are handed (record the number; it is your starting state). Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~138;`. **NEVER RUN AN INSTALL.** Never push, merge, rebase, `checkout --` or
`clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are committed inside it
(`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~138 <0.9.0_WK_AMGT_RESAPP~138@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts, logs and
captures under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~138/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rl-9` (round 37, decomposition s.45) -- WAVE 2, over the MERGED page

Every surface cell of this round has merged before you were spawned. Two outcomes close here:

- **`FWD-28`:** *"PanelEmpty, PanelLoading, PanelError and PanelNoPermission from src/ui/components/states each captured at
  least once across the six states. ACCEPT: An empty panel looks designed, as /market's already does."*
- **`FWD-29`:** *"for each of the six states the JSON reads bandContainersTopLevel == 1, fonts == {Lato}, weights within
  {400,700}, no size below 11, radii within {2,3,4,pill}, shadows == 0 outside the focus ring, lowContrastChars == 0,
  purpleFills per FWD-27, the four states present; the drafting, tabs and posture harnesses green; AND THE SIX PNGs READ BY A
  PERSON, a rejection citing its clause."* At the cut the SAME instrument read today's page as FAILING each predicate --
  that is what makes this a control and not a checklist.

**WHAT YOU BUILD.** (1) Extend `scripts/ui-contract-check.mjs` with a `--states-sweep` mode that renders each of the six
states FOUR more times with fixtures that force EMPTY (an empty rows/members/sections body), LOADING (a fixture route that
never resolves for the panel's own read, captured within 2 s), ERROR (a 500 body) and NO-PERMISSION (a 403 body), captures a
PNG and a JSON per (state, designed-state), and asserts a DOM marker the designed-state components carry (read
`src/ui/components/states/PanelStates.tsx` for the marker each emits; if none carries a marker, assert on the component's
own distinctive markup and say which). It prints a matrix state x designed-state -> PASS/FAIL with the marker found, and a
final line `DESIGNED-STATES <k> of 4 captured at least once`. (2) Where the sweep finds a panel rendering something other
than one of the four (a bare sentence, a blank, a spinner over nothing), FIX THAT BRANCH in the page file that owns it --
this is the ONE cell this round admitted to every `src/pages/SecurityAnalysis/**` file, because it runs after the others
have merged -- using the four components, never a new state. (3) Run the six-state check to PASS.

## 2. BOUNDS

1. **The dev server:** from `portal/`, the bun binary at
   `C:/Users/Opal Bloomberg/AppData/Local/Microsoft/WinGet/Packages/Oven-sh.Bun_Microsoft.Winget.Source_8wekyb3d8bbwe/bun-windows-x64/bun`
   (`"<bun>" run dev --port 5182 > ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~138/dev.log 2>&1 &`),
   wait for `Local:` (up to 90 s), run, then stop it by the PID you recorded (or leave it and say so). Port **5182**.
2. **A predicate that FAILS on the merged page is a FINDING, not something to tune away:** never weaken a predicate,
   never widen a set, never special-case a state in the check. Fix the page (bound 3) or REFUSE the criterion with the
   measured value and the file the failure lives in. `ui-measure.mjs` is not edited by this cell.
3. **Fixes are PRESENTATION ONLY** (`C-PRESENTATION-ONLY`), under `portal/DESIGN.md` C1-C12, and touch the smallest branch
   that owns the defect. No route, DTO, query key or figure moves; no `src/ui/**`, `src/components/**`, `src/api/**`; no
   harness ARM is weakened (the drafting, tabs and posture harnesses are run, not edited, unless a state fix changes a
   markup string an arm names -- then the arm's expectation moves with the markup and you say so).
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/scripts/ui-smoke.mjs
portal/scripts/ui-class-census.mjs
portal/src/pages/SecurityAnalysis/**
portal/src/ui/components/states/PanelStates.tsx
portal/src/ui/components/states/index.ts
portal/src/ui/components/panels/Panel.tsx
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~138/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE `scripts/ui-contract-check.mjs` and, for a designed-state fix only, files under `src/pages/SecurityAnalysis/**`;
everything else is read-only.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rl-9"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5182 --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~138/contract-check-final; echo "exit=$?"</invocation><expect>THE CHECK PASSES ON THE MERGED PAGE: six states run of six asked, a PNG larger than 20 KB and a JSON per state under contract-check-final/, the state-by-predicate table reading PASS in EVERY cell -- bandContainersTopLevel 1, fonts {Lato}, weights within {400,700}, no size below 11, radii within {2px,3px,4px,pill}, shadows 0, lowContrastChars 0, purpleFills 0 on list and 1 on every Security-mode state -- and exit 0. Print the table. A FAIL cell is reported with its measured value and the owning file; it is never tuned away</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rl-9"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5182 --states-sweep --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~138/designed-states; echo "exit=$?"</invocation><expect>EVERY DESIGNED STATE CAPTURED: the state x designed-state matrix printed with the DOM marker found in each cell; DESIGNED-STATES 4 of 4 captured at least once (PanelEmpty, PanelLoading, PanelError, PanelNoPermission), a PNG per captured cell under designed-states/, and no cell reading a bare sentence, a blank panel or a spinner over nothing; exit 0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rl-9"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs &amp;&amp; node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs &amp;&amp; node src/pages/SecurityAnalysis/__harness__/posture.harness.cjs &amp;&amp; node scripts/ui-class-census.mjs src/pages/SecurityAnalysis</invocation><expect>THE THREE HARNESSES GREEN AND THE PAGE-WIDE CENSUS: drafting CHECKS-OK 8 of 8, tabs CHECKS-OK n of n with NO WRONG-WAY line (exec_officers_rendered now true), posture CHECKS-OK n of n and exit 0; then the census over the whole page directory printing FILES at least 18 and TOTAL equal to the band-ink classes the Lead Panel cell admitted (its AC2 list) and nothing else -- print the per-file lines; any translucent, opacity-slash, sub-11px, off-weight, off-radius or shadow hit outside that admitted list FAILS</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rl-9" judgment="true"/>
</proof_of_spec>

AC4 is JUDGMENT and is not yours to grade: **the six PNGs under contract-check-final/ are read by a person** (`3.0.0_SA_CVO~Z`
at L9) against `portal/DESIGN.md`, and a rejection cites a clause number (`C-CLAUSE-CITED-REJECTION`,
`C-RENDER-IS-THE-ORACLE`: a JSON pass without the PNG read is care, not a control). Record AC4 in your instance as
UNVERIFIABLE-BY-INSTRUMENT with `status_reason` naming the CVO; never PASS or FAIL. A fourth criterion sits on this face
because the cell's whole subject is the CONTROL (the diet's stated non-application).

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~138/AMGT_RESAPP.TO-AMGT-rl-9.designed-states-and-the-reassert.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` from
the worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:**
the starting page-wide census number and the final one, every designed-state branch you fixed (file and state), every
predicate that FAILED on the merged page before your fixes with its file, the two commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

# pipeline-override: LIMB 6 only -- the BRIEF half reads STALE at 8da812bf80 (owed by 4.0.0_SA_CRO~Z, asked 05:59Z); R-10 (Andrew-direct 2026-09-23 ~21:2xZ, 'agreed with your rec': the L4-R signature is not a BAR for AMGT, the review is kept) + ADDENDUM B B.6 + 1.0.0_SA_CTO~Z msg 25282 (3) 'no round is held on it'; the review stays owed and is not skipped. The PRD_HEADER key refusal is CLEARED at 8da812bf80; coverage is NOTED at EXECUTING (enrichment recut).

**ISSUER NOTES:** wave 2, spawned after every wave-1 branch has merged; the only cell this round admitted to every page
file, because it is the only one that runs when no other cell is writing. AC4 is the round's ONE judgment criterion, graded
by the CVO on the PNGs at L9.

<status>pending</status>
<round>37</round>
<slot>~138</slot>
<fabric>site-z</fabric>
