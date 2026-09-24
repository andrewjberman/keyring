# AMGT_RESAPP task order -- `AMGT-rm-2` -- THE FREE CHROME: C1 and C11 on the panel strips and the page title, with the sidebar left where Andrew holds it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rm-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~141</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-37 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. Renders against a LOCAL vite dev server with the stubbed session and fixtures; no fetch to any origin but localhost.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~141`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. First act:
print `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, `test -d org && test -d .tools && echo TREE-OK`,
`grep -c 'scope' portal/scripts/ui-contract-check.mjs` (the re-keyed instrument, rm-1, has merged before you; 0 = BLOCKING
row, stop), and `node portal/scripts/ui-class-census.mjs portal/src/components/PageHeaderVariants.tsx portal/src/ui/components/panels/PanelHeader.tsx portal/src/ui/components/panels/PanelFooter.tsx | tail -1`
(your starting census; it read FILES 3 TOTAL 11 at the cut). Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~141;`. **NEVER RUN AN INSTALL.** Never push, merge, rebase, `checkout --` or
`clean`. **Portal is a NESTED repository at `<worktree>/portal`:** portal files are committed inside it
(`cd portal && bash ../.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~141 <0.9.0_WK_AMGT_RESAPP~141@opal.agent>" -F <msgfile> -- <paths>`),
then the outer commit carries `portal` and your deliverables. Messages PURE ASCII via the Write tool. Scripts, logs and
captures under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~141/`, never `.scratch/`.

## 1. THE CELL -- `AMGT-rm-2` (round 38, decomposition s.46) -- WAVE 1, after rm-1

**`FWD-29`'s C1 and C11 limbs, on the chrome the page renders but does not own.** `3.0.0_SA_CVO~Z` REJECTED rl-9's AC4 on
**C1** (*"Lato at two weights only: 400 and 700"* -- weight 300 at 8 chars and weight 500 at 226 on every state) and **C11**
(*"Radii are 2, 3 and 4px -- or a pill ... No 6px, 8px, 12px or 16px radius anywhere"* -- 8px radii at 17-18 per state), and
left the C11 shadow limb INDETERMINATE (shadows 1 on all six; C11 permits exactly one `box-shadow`, the focus ring).
`4.0.0_SA_CRO~Z` then measured chrome BY SUBTRACTION (whole minus main): weight 500, the shadow, 17 of the 18 radii and
list's size-10 are the sidebar `<aside>` -- ⛔ **which is Andrew's reserved card and is NOT yours** (s.46b.2) -- while
**weight 300 is `PageHeaderVariants.tsx:46` `font-light`** (invariant because the header renders once per page) and the
remaining strip radii are **`PanelHeader.tsx:62` `rounded-t-lg`** and **`PanelFooter.tsx:92` `rounded-b-lg`** (every panel
title strip in the product, the Dashboard's included).

**WHAT YOU BUILD**, presentation only, under `portal/DESIGN.md` C1/C11: (1) `PageHeaderVariants.tsx`: the last word of the
title at weight 400 (drop `font-light`); keep the 3px identity rule (C8-legal, `:40`) exactly as it is. (2) `PanelHeader.tsx`
and `PanelFooter.tsx`: strip radii to `rounded-t-[4px]` / `rounded-b-[4px]` (C11 `rounded.md` 4px for panels); the title
`font-semibold` to `font-bold` (700) with its uppercase tracking kept; the `text-white` / `border-white/10` idioms inside the
strip are LEGAL on a `--bg-header` strip (it is an inverted surface) -- the census counts them, so record them as DECLARED
EXCLUSIONS with the clause (C5 inversion on a dark strip) rather than inventing a light strip; the strips' shadow, if any of
the three files carries one, removed. (3) Determine the C11 shadow limb for the STRIPS: print `getComputedStyle(strip).boxShadow`
for one PanelHeader and one PanelFooter on the merged page (a node one-liner through the instrument's playwright, or a
line in your harness) -- if a drop shadow lives in your three files, remove it; if the single shadow is the sidebar's
`shadow-lg` (`App.tsx:271`), REPORT it as the sidebar's and touch nothing. **You do not touch `App.tsx`, `index.css`,
`Panel.tsx` or any page file.**

⚠ **BLAST RADIUS, named because it is real:** `PanelHeader` and `PanelFooter` are every panel's strip across the portal.
The change is radius and weight only; AC3 proves the Dashboard (`/market`) still renders with its strips in place.

## 2. BOUNDS

1. **The dev server:** from `portal/`, the bun binary at
   `C:/Users/Opal Bloomberg/AppData/Local/Microsoft/WinGet/Packages/Oven-sh.Bun_Microsoft.Winget.Source_8wekyb3d8bbwe/bun-windows-x64/bun`
   (`"<bun>" run dev --port 5183 > ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~141/dev.log 2>&1 &`),
   wait for `Local:` (up to 90 s), run, then stop it by the PID you recorded. Port **5183**.
2. **Presentation only** (`C-PRESENTATION-ONLY`): no prop, no behaviour, no layout split moves; `flex-wrap` on the header
   (Andrew-direct 2026-09-14 ~19:0xZ, the zoom rule) stays exactly as written.
3. **A predicate that still FAILS after your three files are clean is a FINDING with its owning file**, never tuned: the
   sidebar's weight 500 / shadow / radii / size-10 are EXPECTED to remain in the scope=body table and are reported as the
   sidebar's (s.46b.2); inside scope=main, weight 300 must read 0 on all six and the strip radii must be gone.
4. **Standing:** no install, no vendor or Bloomberg call, no S3 delete, no key hunting, no push, no promote. **REFUSE, do
   not rescue.**

## 3. SURFACES

<paths>
portal/src/components/PageHeaderVariants.tsx
portal/src/ui/components/panels/PanelHeader.tsx
portal/src/ui/components/panels/PanelFooter.tsx
portal/scripts/ui-contract-check.mjs
portal/scripts/ui-measure.mjs
portal/scripts/ui-smoke.mjs
portal/scripts/ui-class-census.mjs
portal/src/ui/components/panels/Panel.tsx
portal/src/App.tsx
portal/src/index.css
portal/DESIGN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~141/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

You WRITE the first three entries (and your deliverables); every other path is a read-only input.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rm-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-class-census.mjs src/components/PageHeaderVariants.tsx src/ui/components/panels/PanelHeader.tsx src/ui/components/panels/PanelFooter.tsx</invocation><expect>THE THREE FILES CLEAN AT THE SOURCE: weight, radius and shadow categories read 0 on all three (was weight 2, radius 0 by the census's rounded-lg pattern -- print what rounded-t-lg/rounded-b-lg read as, and if the census does not count the -t-/-b- forms say so and count them by grep beside it); the idiom category's remaining hits are each named with the clause that makes them legal on a --bg-header strip (C5 inversion), printed per line with its denominator; FILES 3 and the TOTAL after exclusions 0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rm-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-contract-check.mjs --port 5183 --scope main --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~141/contract-check-chrome; echo "exit=$?"</invocation><expect>INSIDE MAIN, ON ALL SIX STATES: weight 300 reads 0 (was 8 on every state) and no 8px radius attributable to a strip remains (print the radii map per state; the residue, if any, is named by element and is another cell's -- rm-3's attribution); the scope=body table printed beneath still shows the sidebar's weight 500 / shadow / radii and they are REPORTED as the sidebar's, not touched; the C11 shadow limb DETERMINED in words -- the single shadow is named as the sidebar's shadow-lg or as one of your files' and, in the second case, gone; six PNGs larger than 20 KB</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rm-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node scripts/ui-smoke.mjs --port 5183 --route /market --out ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~141/market-after.png &amp;&amp; node scripts/ui-measure.mjs --port 5183 --route /market --scope main &amp;&amp; npx tsc -b --noEmit; echo "tsc=$?"</invocation><expect>THE DASHBOARD STILL RENDERS WITH ITS STRIPS: a /market PNG larger than 20 KB, its stripContainers count printed and equal to the count measured BEFORE your edit (print both -- the strips moved in radius and weight, not in number), tsc clean (tsc=0). If ui-smoke.mjs takes no --route flag, add the smallest one to it (it is in your paths) and say so</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~141/AMGT_RESAPP.TO-AMGT-rm-2.the-free-chrome.proof_of_spec.json`,
graded by **YOUR WORKTREE'S OWN** `PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` from the
worktree root. **The status flip is the ISSUER'S**; leave the record face alone and say so. **Report once, naming:** the
three files' before/after census lines, weight 300 per state before/after, the strip radii before/after, the shadow limb's
determination in one sentence, the /market strip count before/after, the two commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** wave 1, after rm-1 merges. The round-37 analysis (item 1) admitted `App.tsx` and `index.css` as well; the
CRO's research @`88f08c0c7a` measured the sidebar as Andrew's reserved card (DSGN_REBRND round-2 decisions :11-12) and the
`--bg-band` repoint as his ~19:5xZ word, so this cell admits only the three FREE files; the CTO was told at the issuance.

<status>pending</status>
<round>38</round>
<slot>~141</slot>
<fabric>site-z</fabric>
