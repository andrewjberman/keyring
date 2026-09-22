# TO IRPT_FNTEND.TO-FE-s-91 -- F49-AC8's comparator: exact match on the sanctioned hunk, honest labels, false-value controls

<to_id>IRPT_FNTEND.TO-FE-s-91</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~41</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2 | **Decomp cell:** `FE-s-91` (round 15, v0.15) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~3 | **rows:** C-S190 | **base:** workspace = the round-15 issuance commit on CLOUD (your worktree branches from it), portal DEV `7dd3d067` (round 14's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE
### THE CELL

`FE-s-91` -- round 14's `F49-AC8` carve-out (`__tests__/fe-s-49/admin-gate.test.ts`, the "SANCTIONED REWRITE"
branch this project's own round-14 amendment added) checks the print route's gate hunk by testing whether every
PRE-EXISTING TOKEN is present as a SUBSTRING of the current line, plus the one new token. The CVO's own negative
control found this too loose: setting `requireAdmin={{false}}` or `requireInternal={{false}}` on that line STILL
reads as a substring match (`"requireAdmin"` is a substring of `"requireAdmin={{false}}"`), so the comparator
reports the hunk as matching when the actual BOOLEAN VALUE of a required prop has been flipped to false -- a
real admission-gate weakening the current substring check cannot detect. Its final summary line also then
claims "THREE ... BYTE-IDENTICAL" even for the sanctioned hunk, which is not literally true (only two hunks are
literally byte-identical; the third is a substring-sanctioned match) -- an honesty-of-label defect, separate
from the detection gap.

**Fix, in `__tests__/fe-s-49/admin-gate.test.ts`'s existing `SANCTIONED_ADDITIONS` carve-out logic
(introduced this round in the F49-AC8 sanctioned-rewrite branch -- read it in full before changing it):**
1. Replace the substring check with an EXACT comparison: parse the print-route JSX line's actual PROP LIST
   (the file already has TypeScript's own compiler available -- `import ts from 'typescript'` -- prefer walking
   the real AST attribute list over another regex/substring scheme) and require it to equal EXACTLY the old
   hunk's prop set plus the one sanctioned addition -- no fewer, no more, and each BOOLEAN-VALUED prop must
   still evaluate true (a JSX shorthand `requireAdmin` is true; an explicit `requireAdmin={{false}}` must be
   read as false and REFUSED).
2. Fix the summary line to report the true shape: e.g. `"TWO HUNKS BYTE-IDENTICAL, ONE SANCTIONED ADDITIVE
   MATCH"` -- never a single claimed "N of N byte-identical" number that conflates two different kinds of
   match.
3. **Preserve `F49-AC7`'s own independent Boolean-true checks completely unchanged** -- this fix narrows
   `F49-AC8`'s carve-out; it must not touch or duplicate F49-AC7's own logic.

**Required controls, in addition to the existing ones this file already has (do not remove any):**
- Positive: the real, current print-route line (unchanged) still matches the sanctioned carve-out.
- Negative (already exists, keep it): `requireInternal` entirely REMOVED from the print-route line -> refuses.
- **New negative:** `requireAdmin={{false}}` on the print-route line (present but false-valued) -> refuses.
- **New negative:** `requireInternal={{false}}` on the print-route line -> refuses.
- **New negative:** an UNRELATED extra prop added alongside the sanctioned one (e.g. `data-extra="x"`) on the
  print-route line -> refuses (the carve-out permits EXACTLY the one named addition, nothing else).
Each negative control is exercised the same way the existing one is: a temporarily-committed mutation, the test
run against it, then a clean `git revert` back to net-zero -- never a history rewrite, never left uncommitted-back.

**Your surface.** `src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts` (the `SANCTIONED_ADDITIONS`
carve-out logic and its summary-line text ONLY -- every other test in this file, including `F49-AC7`, is
read-only to you), and your own `__tests__/fe-s-91/` if you need a separate scratch space (prefer keeping your
new controls inside the existing `fe-s-49` file beside the logic they test, matching this project's own
established idiom of co-locating a fix with its test).

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md`, `<WS>/portal/CLAUDE.md`; the PRD's ENDPOINT/CONTRACTS text
   (`../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2); the CTO's round-14 analysis (`org/missions/D9/IRPT/IRPT_FNTEND/ledger/ROUND_ANALYSIS.round14.md`
   @8b1b0d6832); the CVO's round-14 slug (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v11.md`)
   and its full review (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND14_L8_L9_20260922.md`) -- your
   cell's remedy is quoted from these; read the SURROUNDING text too, not just your own paragraph.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 6020-6024 (outside every prior round's
   range): `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal`, background, INLINE PREFIX, NEVER
   exported. Test with `curl` first; that number is `<PORT>`.
3. **A control is a claim.** Before trusting a passing assertion, run its wrong-state / negative arm and confirm
   it fails or reads UNMEASURABLE as required.
4. **Regression is the safety net.** This round FIXES instruments and fixtures that other cells' criteria already
   depend on -- the whole-suite criterion is not a formality, it is the proof you did not silently break a
   currently-passing test while fixing your own defect.
5. **Stop your dev server before the whole-suite criterion, verify the port closed** (`curl` returns `000`).
6. **Fixes.** A defect on YOUR write surface may be fixed with a BEFORE capture kept and an AFTER beside it. A
   defect needing another cell's file is ONE surprise row, never a wider grant.
7. **Result file** (`<slug>.result.md` in your deliverables folder), disclosure paragraph first.
8. **Keep your context small:** write long outputs to files and read their tails.

### ACCEPTANCE

<criterion id="F91-AC1" cell_refs="FE-s-91" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F91-AC1` -- the whole portal typechecks.

<criterion id="F91-AC2" cell_refs="FE-s-91" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F91-AC2` -- the whole fe-s-49 file passes with the new exact-match comparator and honest summary label, including F49-AC7's own unchanged checks.

**Run the three new negative controls as temporarily-committed mutations** (mirroring this
round's own established pattern for exercising this exact test file), recording each result in your result file:
`requireAdmin={{false}}`, `requireInternal={{false}}`, and an unrelated extra prop -- each must show the
comparator REFUSING (the carve-out no longer matches), then `git revert` each cleanly back to net-zero before
moving to the next.

<criterion id="F91-AC3" cell_refs="FE-s-91" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F91-AC3` -- post-revert: the file is back to a genuinely clean, unmutated state and passes exactly as F91-AC2 already proved -- confirming every temporary control was fully and cleanly reverted.

<criterion id="F91-AC4" cell_refs="FE-s-91" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F91-AC4` -- the whole IRPT_FNTEND suite is green.

<criterion id="F91-AC5" cell_refs="FE-s-91" judgment="true" drives="none"/>
`F91-AC5` -- graded at L9 by the CVO: the comparator now genuinely refuses a false-valued required prop and an unrelated extra prop (not merely a substring match that happens to pass), the summary label is honest about which hunks are literally byte-identical versus sanctioned-additive, and F49-AC7's own independent Boolean checks are unchanged. RECORD; NO VERDICT.

<expected_criteria>F91-AC1, F91-AC2, F91-AC3, F91-AC4, F91-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W41-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **Every temporary mutation commit MUST be reverted via `git revert` before your final report** -- an
  uncommitted or unreverted mutation left on your portal branch is an order defect, not a passing result.
- **F49-AC7 and every other test in this file besides the `SANCTIONED_ADDITIONS` carve-out is READ-ONLY to
  you.** Do not restructure the file beyond your narrow fix.
- **C-S176 declared N/A, with reason, at cut time:** this cell's criteria are AST/string-comparison logic
  checks and their controls, not rendered visual assertions -- the five-part visual control rule does not
  apply. The five controls named above (one positive, four negative) ARE this cell's control set.
<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-91/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.15, cell `FE-s-91`.
<owned_cells>FE-s-91</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F91-AC1`, `F91-AC2`, `F91-AC3`, `F91-AC4`, `F91-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-91.gate-hunk-comparator-exact-match-and-honest-labels.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F91-AC1,F91-AC2,F91-AC3,F91-AC4,F91-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-91.gate-hunk-comparator-exact-match-and-honest-labels.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `gate-hunk-comparator-exact-match-and-honest-labels.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.10 (both L4-R halves SIGNED, prd-signoff.py status ADMITTED).
the design: RUN by the issuer -- REMEDIATION_v11.md @f7546b6aec, the CVO's round-14 review, and ROUND_ANALYSIS.round14.md @8b1b0d6832, all read at HEAD.
the spec: RUN -- PRD FWD-12 ENDPOINT row and the CTO's round-14 analysis, both read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 15, wave 1, slot ~FE-s-91.
