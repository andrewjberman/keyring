# AMGT_CORPUS task order -- `CRPS-am-3` -- ROUND 37: the Model sheet says why a gap inside a row is empty, and names each money row's currency

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-am-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check reads a fixture file.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV c66d08f346 -- am3_check.cjs build 0/2 control 2/2; modelPattern harness CHECKS-OK 12 of 12. Blind spot: the check grades the pure sheet builder on two captured names; the rendered page is the CVO's judgment (AC3).
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV push is Andrew's word after the CTO's review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 37.

**Your portal.** Your worktree's `portal/` is a nested git repository checked out at portal origin/DEV @`c66d08f346` on your own
portal branch. It already carries round 36's V3 lines (`75efe9d6`) and DSGN_AMGTV1's round-36 work. Portal files commit INSIDE
`portal/` on that branch first, then the outer commit for the outer files. Never commit the portal gitlink in the outer repository.

## 1. THE CELL -- `CRPS-am-3`

FWD-20 (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` about line 560) asks that "a row that still cannot show says
why in words a PM reads". Round 36 put the 49 V3 lines on the Model tab
(`portal/src/pages/SecurityAnalysis/modelSheet.ts`, `tabs/ModelTab.tsx`). The CVO and CTO found two limits on the running page:

1. **A gap INSIDE a showing row says nothing.** On 1299_HK_Equity (fiscal year not ending in December), the price-dated range rows
   read `--` in 2016, 2017 and 2022. The payload already serves why: `data.model.fiscal_unresolved` is a list of `{mnemonic,
   fiscal_year, reason}`, and for those cells it says `not dated at the fiscal period end (non-December FYE, fye_join)`.
   `buildModelSheet(figures, fiscalYears, servedLineNames, forecastFigures, fiscalUnresolved?, headerFigures?)` already receives
   that list; today it words a reason only for a row with NO figure at all.
2. **Money names no currency.** Each figure carries `currency` (a string, or null). A producer change in this same round
   (`CRPS-am-1`, then a re-derive) labels every money figure. The page today marks unlabelled money rows "currency not stated by
   the source" and never prints the currency it does have beside the amounts.

**Build, in `modelSheet.ts` and `tabs/ModelTab.tsx` only:**
1. Every `ModelSheetRow` gets `cellReasons: (string | null)[]`, aligned with `cells`. An entry is the reason in PM words where the
   cell is empty AND `fiscalUnresolved` names that row's mnemonic and that year. It is null otherwise (a cell with a figure, or an
   empty cell with no served reason). Word the served texts as round 36 does (`reasonInWords`): the fiscal-period-end text reads
   "The price-dated range is not reported at this company's fiscal year end, because its fiscal year does not end in December."
   Never invent a reason.
2. Every `ModelSheetRow` gets `currency: string | null`: the one currency every money figure of the row carries; null when none
   carries one. A money figure has a unit beginning `MILLIONS` but not `MILLIONS (share count)`, or `ABSOLUTE`, or `PER SHARE`.
   If the row's figures carry two different currencies, keep the existing per-row unit wording and name both; never pick one.
3. In `ModelTab.tsx`, show each gap reason at its cell (a hover title plus a small footnote mark per gap year, the reason itself
   listed once under the table), and print the row's currency beside its unit words. The page's "currency not stated by the
   source" mark stays for a row whose money figures really carry none.
4. Nothing else moves: the 17 rows of the first two groups, the V3 group's row list, DSGN's order ("What changed" leads, the
   presets), labels, types and values.
5. **Colour law** (`portal/CLAUDE.md`): on the light canvas and on white panels, ink is navy. Never use `text-white*`,
   `text-{color}-100..300` or `bg-white/N` here; reuse the existing classes.

## 2. BOUNDS

1. NO push of any branch, NO deploy, NO AWS call. Typecheck with `bun run typecheck` inside `portal/` (never bare `tsc
   --noEmit`, which checks nothing here).
2. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots, or any `__harness__/` file (they are
   the oracles).
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-am-3.model-sheet-gap-reasons-and-currency.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-am-3.model-sheet-gap-reasons-and-currency.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/types.ts`,
the existing `__harness__/` files, and the issuer's checks, fixtures and snapshots under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round36/` and `.../checks/round37/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-am-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round37/am3_check.cjs" portal</invocation><expect>(?m)^am3 build 2/2 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-am-3"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs</invocation><expect>(?m)^CHECKS-OK ([0-9]+) of \1$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-am-3" judgment="true"/>
</proof_of_spec>

- AC1 (the real `modelSheet.ts` on payloads captured from the real read path, TSM and 1299 HK):
  - build: on 1299 HK every gap cell with a served reason carries a reason in words (92 at the cut); on TSM every money row whose
    figures carry one currency exposes it, and one with none exposes null;
  - control: the 17 rows and the V3 row list are unchanged, and round 36's `al2_check` still reads 3/3 + 1/1.
- AC2: the existing Model-sheet harness still passes (`CHECKS-OK 12 of 12` at the base).
- AC3 (JUDGMENT, graded by the CVO at L9 on the running page): a PM sees why each gap is empty, and each money row's currency.
  Record it as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`; no verdict.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck`. It reads clean.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   outer commit as your proof instance.
4. Report ONCE: how a gap reason and a row's currency show on the page, every criterion's output line, the typecheck line, your
   portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-36 analysis @`4c3e3755a7` s.3 rulings 1 (the page half) and 2 + s.4 items 1-2. Base portal origin/DEV
c66d08f346: am3_check build 0/2 control 2/2; harness 12/12. portal_ref c66d08f346. A product-file candidate: `1.0.0_SA_CTO~Z`
reviews it; the DEV push is on Andrew's word.
<risk>LOCAL</risk>
<status>pending</status>
<round>37</round>
<slot>~2</slot>
<fabric>site-z</fabric>
