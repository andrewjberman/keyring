# TO POSN_ASTTAX.TO-V5-1 -- THE COLOUR REGISTRY: `structured` (pink) and `commodities` (a NEW yellow token, never amber) in `ASSET_CLASS`; `Metals` and `Hedge` sub-asset colours; `Commodities` leaves the equity-blue family. Committed inside the portal submodule on the round's ONE drain ref (AT5-s-5, F1; FWD-3/FWD-4)

<to_id>POSN_ASTTAX.TO-V5-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~22</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-COLOURS; s.3 order + colour) - **Decomp cell:** `AT5-s-5` - **Issuance:** round 5, wave 1. **GATES `AT5-s-6` (F2).**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~22`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~22;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Workspace commits via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~22 <0.9.0_WK_POSN_ASTTAX~22@opal.agent>" -F <msgfile> -- <paths>`.
Never push, merge, rebase, `checkout --`, `clean` -- in the workspace OR the portal.

## THE PORTAL, AND THE ONLY WAY YOU MAY WRITE INTO IT

The freeze never barred SOURCE writes (round-3 analysis s.7; Andrew 2026-09-14 05:31Z: *"the frontend being done is defined as built
and committed behind the freeze"*). What it bars: **the gitlink move, any promote, any DEV/PROD push.** So:
1. Your worktree's `portal/` is a SEPARATE clone. Before writing, verify it sits EXACTLY at the pin: `git -C portal rev-parse HEAD`
   == `e85f6eb84f` and `git -C portal merge-base --is-ancestor` TRUE in BOTH directions (a one-direction read cannot tell behind
   from ahead -- round-3 analysis s.7c). If it is not at the pin, `git -C portal checkout --detach e85f6eb84f` (a detached checkout,
   never a branch move of DEV) and re-verify.
2. Your worktree's `portal/` is a LINKED WORKTREE of the portal repo, PRE-CUT by the COO on branch `wk-posn-5-22-portal` at the pin `e85f6eb84f` (`cat portal/.git` names the portal repo's gitdir). Verify it (`git -C portal rev-parse --abbrev-ref HEAD` reads that branch); do NOT re-create it.
3. Commit inside `portal/` with `git -C portal commit --author="0.9.0_WK_POSN_ASTTAX~22 <0.9.0_WK_POSN_ASTTAX~22@opal.agent>"
   -F <msgfile>` (the submodule has its own history; safe-commit.sh is the workspace's).
4. **The superproject gitlink does NOT move**: `git -C <worktree> diff --submodule=log -- portal` must show NO gitlink change
   staged or committed by you. Do not `git add portal`.
5. Record the ref: the round's ONE drain ref is `refs/drains/posn-5-portal`; the COO drains your branch onto it. You append ONE
   line to `org/missions/D4/POSN/POSN_ASTTAX/ledger/PORTAL_REFS.md` (create it if absent) naming your branch, its head hash, and the
   pin it was cut from -- at your FIRST portal commit (round-3 analysis s.7b).

## THE CELL

Measured at the pin: `portal/src/lib/chartColors.ts:113-120`
```
export const ASSET_CLASS = { fixedIncome: PALETTE.green500, equity: PALETTE.blue500, cash: PALETTE.amber500,
                             alternatives: PALETTE.orange500, realEstate: PALETTE.orange500, other: PALETTE.gray500 }
```
-- no `structured`, no `commodities`. `:308` `'Commodities': PALETTE.blue950` (a shade of equity blue -- round 4 U2's finding).
`PALETTE` already carries `pink500 '#ec4899'` (`:61`) and `yellow500 '#eab308'` (`:78`, "electric yellow (not amber)").

**Your edit, in that one file:**
- `ASSET_CLASS` gains `structured: PALETTE.pink500` and `commodities: PALETTE.yellow500` -- **never amber** (amber is Cash on six
  readers; Andrew: *"mint some yellow color, yes"*).
- The sub-asset map (`:283-309`) gains `'Metals'` (yellow family) and `'Commodities'` leaves the blue family for the yellow one.
- **AMENDED ~19:0xZ by the issuer (rows W22-S1, W22-S4):** `'Hedge'` ALREADY EXISTS at `:294`, bound to `PALETTE.green900` inside
  the Fixed Income gradient. C-SUB-ASSET encodes `Hedge` under STRUCTURED. The issuer measured the binding DEAD: a filtered scan of
  the served table (285 rows, no LastEvaluatedKey) found **0 rows** with `sub_asset_class = Hedge` (the four volatility tickers
  carry `Volatility` until R1 moves them to `Hedge`). So RE-BIND `'Hedge'` to a PINK-family token (`PALETTE.pink600` exists at
  `:62`; a shade distinct from the class base `pink500` where one exists). Leave `'Volatility'` as it is (it goes dead at R1;
  not this cell's).
- **AMENDED ~19:0xZ (row W22-S4):** `getSubAssetTextColor` (`:314-320` at the pin) branches on the background VALUE; moving
  `'Commodities'`/`'Metals'` to `yellow500` flips their chip text to white-on-yellow (measured 1.92:1). ADD `PALETTE.yellow500` to
  its `lightBackgrounds` set so those chips read dark-on-yellow (measured 9.25:1). The pink family stays white-on-pink only if it
  measures >= 4.5:1; else add it to the light set too, and print the reading.
- Nothing else in the file moves. The token NAMES `ASSET_CLASS.structured`, `ASSET_CLASS.commodities` are the CONTRACT F2 binds:
  print them in your report exactly.

Round 4 U2 measured the ratified five in canonical order: Fixed Income / Cash (green), Equity (blue), Structured (pink),
Commodities (yellow, ruled), Alternatives (orange). Read them from the PRD at `99cc431075` s.3, do not retype them from here.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W22-S<k>`, appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working. The Attribution page's
`holdings-shared.tsx` binding colours of its own is KNOWN (W18-S2) and OUT by Andrew's word -- do not file it again.

## CRITERIA -- structured, one clause each

<criterion id="V5-AC1" cell_refs="AT5-s-5"><invocation>timeout 60 git -C portal rev-parse HEAD</invocation><expect>e85f6eb84f3a1771a37011a7e77e372570bad02a, and `git -C portal merge-base --is-ancestor HEAD e85f6eb84f` AND the reverse both exit 0 (both directions printed). Otherwise detach to the pin and re-run; if it still fails, STOP with a row.</expect></criterion> `V5-AC1` -- YOUR OWN CLONE, AT THE PIN, PROVED BOTH WAYS. (A PRE-WRITE precondition, recorded ONCE before the first edit; never re-run after your commit -- its detach branch would abandon your work. Row W22-S5.)

<criterion id="V5-AC2" cell_refs="AT5-s-5"><invocation>timeout 60 git -C portal diff --stat e85f6eb84f -- src/lib/chartColors.ts</invocation><expect>exactly one file changed; the diff (printed) adds `structured: PALETTE.pink500` and `commodities: PALETTE.yellow500` to ASSET_CLASS, adds 'Metals' to the sub-asset map, RE-BINDS the existing 'Hedge' from PALETTE.green900 to a pink-family token, moves 'Commodities' off PALETTE.blue950 to a yellow-family value, adds PALETTE.yellow500 to getSubAssetTextColor's lightBackgrounds set (and the pink token only if the contrast reading requires it), and touches nothing else.</expect></criterion> `V5-AC2` -- THE EDIT, NO WIDER THAN THE CELL.

<criterion id="V5-AC3" cell_refs="AT5-s-5"><invocation>timeout 120 node -e "<LOAD_ASSET_CLASS_MAP>"</invocation><expect>ZERO ratified classes share a value (fixedIncome, equity, structured, commodities, alternatives are five DISTINCT values, printed); the pre-existing alternatives/realEstate pair is printed and disclosed as a class and its own sub-asset, unchanged by you.</expect></criterion> `V5-AC3` -- EXCLUSIVITY: ONE COLOUR PER CLASS, THE SAME EVERYWHERE THIS REGISTRY REACHES.

<criterion id="V5-AC4" cell_refs="AT5-s-5"><invocation>timeout 600 bash -c "cd portal && bun run tsc -b"</invocation><expect>exit 0 with the file count it checked printed (tsc -b, NEVER tsc --noEmit against the root tsconfig, which typechecks ZERO files -- AMGT rd-8 AC2's measured vacuity). POSITIVE CONTROL, REQUIRED: inject a one-line type error into chartColors.ts, re-run, observe the failure (error TS printed), revert -- an instrument that cannot fail proves nothing.</expect></criterion> `V5-AC4` -- THE BUILD, WITH AN INSTRUMENT THAT CAN FAIL.

<criterion id="V5-AC5" cell_refs="AT5-s-5"><invocation>timeout 60 git -C portal log -1 --format='%H %an %s' wk-posn-5-22-portal</invocation><expect>one commit on wk-posn-5-22-portal authored 0.9.0_WK_POSN_ASTTAX~22, parent e85f6eb84f; and the superproject gitlink UNMOVED, read two ways at the worktree root: `git ls-tree HEAD -- portal` prints `160000 commit e85f6eb84f3a1771a37011a7e77e372570bad02a portal`, and `git diff --cached -- portal` is EMPTY (nothing staged). (Amended ~19:0xZ, row W22-S2: the first cut's `git diff --submodule=log -- portal` compares the index to the submodule's working-tree HEAD and is non-empty BY CONSTRUCTION once the mandated commit exists -- it failed exactly the compliant worker.)</expect></criterion> `V5-AC5` -- COMMITTED INSIDE THE SUBMODULE; THE GITLINK UNMOVED.

<criterion id="V5-AC6" cell_refs="AT5-s-5"><invocation>timeout 60 cat org/missions/D4/POSN/POSN_ASTTAX/ledger/PORTAL_REFS.md</invocation><expect>one line naming wk-posn-5-22-portal, its head hash from V5-AC5, and the pin e85f6eb84f, with the drain ref refs/drains/posn-5-portal named as the destination -- written at your first portal commit and committed in the workspace under your serial.</expect></criterion> `V5-AC6` -- THE REF IS WRITTEN DOWN WHERE THE PROMOTE WILL READ IT.

<criterion id="V5-AC8" cell_refs="AT5-s-5"><invocation>timeout 120 node -e "<CONTRAST_CHECK>"</invocation><expect>for EACH sub-asset background this cell added or moved ('Metals', 'Commodities', 'Hedge') the text colour getSubAssetTextColor returns for it, and the WCAG contrast ratio of that text on that background, printed as a (key, background, text, ratio) table with every ratio >= 4.5; the pre-amendment white-on-yellow reading (1.92) printed as the negative control the amendment fixed.</expect></criterion> `V5-AC8` -- THE CHIP TEXT READS ON EVERY COLOUR THIS CELL TOUCHED (added ~19:0xZ, row W22-S4).

<criterion id="V5-AC7" cell_refs="AT5-s-5" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether yellow500 beside amber500 is distinguishable on the silver canvas (the design law in portal/CLAUDE.md), read from a rendered swatch if one is available, else stated as unread. Record the readings and offer NO verdict.</expect></criterion> `V5-AC7` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V5-AC1, V5-AC2, V5-AC3, V5-AC4, V5-AC5, V5-AC6, V5-AC7, V5-AC8</expected_criteria>

<placeholders>CONTRAST_CHECK, LOAD_ASSET_CLASS_MAP</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V5-1.the-colour-registry.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~22/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D4/POSN/POSN_ASTTAX/ledger/PORTAL_REFS.md
portal/src/lib/chartColors.ts
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-5`.
<owned_cells>AT5-s-5</owned_cells>
Read-dependencies, NOT claimed: round 4's `AT4-s-2` (TO-U2-1, `~18`) measured the colour failures and the missing tokens -- READ its
result, do not re-census. DOWNSTREAM: `AT5-s-6` (F2, your next order on this slot) binds the token NAMES you print.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a source edit inside a frozen submodule; no job, deploy or monitor; the promote is Andrew's.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not rendered yellow500 against the silver canvas
-- V5-AC7 is the first look; (2) the issuer read PALETTE at the pin and found pink500/yellow500 present -- if the sub-asset map's
grammar needs a different key shape, that is a row, not a redesign; (3) whether `bun run tsc -b` is the project's build entry is
asserted from AMGT rd-8's lesson, not exercised by the issuer on this clone.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~22/POSN_ASTTAX.TO-V5-1.the-colour-registry.proof_of_spec.json
</proof_of_spec>
