# AMGT_CORPUS task order -- `CRPS-ao-3` -- ROUND 39: the Model page names the header facts' currency, marks every "--", and says each unmeasured reason in a PM's words

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ao-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the checks read a fixture file.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV e2130d42 -- ao3_check currency build 0/1 control 1/1; marks build 0/1 control 1/1; words build 0/1 control 1/1; modelPattern harness CHECKS-OK 12 of 12. Blind spot: the checks grade the pure builder and formatter on three captured names; the rendered page is the CVO's judgment (AC4).
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's render review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 39. After this order the issuer hands you `CRPS-ao-4` (the same files).

**Your portal.** Your worktree's `portal/` is a nested git repository checked out at portal origin/DEV @`e2130d42` on your own
portal branch. Portal files commit INSIDE `portal/` on that branch first, then the outer commit for the outer files. Never commit
the portal gitlink in the outer repository.

## 1. THE CELL -- `CRPS-ao-3`

The Security Analysis page's Model tab (`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx`) renders the sheet that
`buildModelSheet` (`modelSheet.ts`) builds from the served payload. The CVO's read of the TSM page (round 38) found three defects
in outcome FWD-20 ("every money figure names its currency, and every gap gives a reason in a PM's words"). Build all three.

**(a) Currency on the header-fact line.** `buildModelSheet` fills `v3Facts` (about `modelSheet.ts:428-432`) with `{mnemonic,
label, value, unit}` from the served header figures and drops the figure's served `currency` (the type does not declare it; read it
as round 37's `figureCurrency` does, about line 281). So the line under the V3 group (`V3GroupNotes`, `ModelTab.tsx` about
390-421, value text from `v3FactValue` about 379) reads "Market capitalisation: 2,452,061 million" with no currency.
- Add `currency: string | null` to `V3Fact` and carry the served figure's currency (null when it carries none).
- Render it the way the sheet's money rows show theirs: the code with the figure (e.g. "USD 2,519,589 million"). A money fact with
  no served currency says so in words ("currency not stated"), never a guessed code.

**(b) A mark on every in-row "--".** A row that shows at least one figure renders "--" for each empty year (`ModelTab.tsx` about
536-548). A "--" carries a superscript mark only when `row.cellReasons[index]` is set, and `cellReasons` is set only from the
served `fiscal_unresolved` (`modelSheet.ts` about 397). TSM's `fiscal_unresolved` is empty, so its 99 in-row "--" carry nothing:
- EPS, DPS and P/E across 2016-2025 (30 cells; the block serves no history for these lines, only 2026E-2028E forecasts);
- 23 lines across 2026E-2028E (69 cells; no consensus estimate is served for these lines).
In `buildModelSheet`, give every empty cell in a row that shows a figure a reason in words. Precedence:
1. the served `fiscal_unresolved` reason for that (mnemonic, year) when there is one -- unchanged from round 37;
2. else, a history year in a line the block carries no history for at all: "Bloomberg reports no history for this line";
3. else, an estimate year (`<year>E`): "No consensus estimate is served for this line";
4. else (a history year in a line that has other history years): "Bloomberg returned no figure for this year".
The page's existing mark and the reason list under the table (`gapReasons`, about 457-462 and 567-575) then carry them.

**(c) Unmeasured reasons in a PM's words; no bare raw figure.** `formatStatValue` in `components/StatTile.tsx` (about 51-80)
renders an UNRESOLVED-unit money figure as "unit not resolved -- raw figure 77,689,148.37" (TSM enterprise value), and a money
figure with no currency as "-2.00T currency not stated" (TSM net debt). Both served figures carry a `currency_basis` beginning
`UNMEASURED: ...` (e.g. "UNMEASURED: no read isolates this figure's own currency (CRPS-aa-1 round-25 census)"). The header tiles
(`components/HeaderCards.tsx`) and the "What changed" rows (`components/model/WhatChangedPanel.tsx`) both call `formatStatValue`.
- Add a fifth, optional parameter: `formatStatValue(value, format, currency, unit, currencyBasis?)`, and pass the figure's served
  `currency_basis` from both callers.
- An UNRESOLVED-unit money figure renders NO number at all: a short reason in a PM's words (e.g. "Not shown: Bloomberg's figure
  does not say whether it is in units or millions"). The full served value stays in the tooltip, as now.
- A figure whose basis begins `UNMEASURED:` maps to a PM sentence about its currency (e.g. "currency not confirmed by
  Bloomberg"). Never print the basis text, a cell id (`CRPS-...`), "census", or an UPPER_SNAKE token.
- A resolved figure with a currency renders exactly as now ("USD 184B").

Nothing else moves: row lists, labels, figure values, the history columns, the consensus band, DSGN's "What changed leads the
Model tab" order. **Colour law** (`portal/CLAUDE.md`): on the light canvas and white panels, ink is navy; never `text-white*`,
`text-{color}-100..300` or `bg-white/N`. Reuse the existing classes.

## 2. BOUNDS

1. NO push of any branch, NO deploy, NO AWS call. Typecheck with `bun run typecheck` inside `portal/` (never bare `tsc
   --noEmit`, which checks nothing here).
2. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots, or any `__harness__/` file.
3. Write code with the Edit/Write tools, never a shell heredoc. ASCII only.
4. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-ao-3.model-page-currency-marks-words.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ao-3.model-page-currency-marks-words.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/types.ts`,
the `__harness__/` files, and the issuer's checks, fixture and snapshots under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ao-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/ao3_check.cjs" currency portal</invocation><expect>(?m)^ao3 currency build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ao-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/ao3_check.cjs" marks portal</invocation><expect>(?m)^ao3 marks build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ao-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round39/ao3_check.cjs" words portal</invocation><expect>(?m)^ao3 words build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-ao-3" judgment="true"/>
</proof_of_spec>

- AC1 (the real `modelSheet.ts` on TSM, BA and ASML captured from the real read path): build -- every header fact whose served
  figure carries a currency exposes it (6 at the cut); control -- the fact list is unchanged.
- AC2: build -- every TSM in-row empty cell carries a reason in words (99 at the cut); control -- no figure cell moves on any of
  the three names.
- AC3 (the real `formatStatValue`, called with the served basis): build -- TSM EV shows no raw figure and TSM net debt and EV
  carry no machine token; control -- BA's EV and net debt format exactly as before ("USD 184B", "USD 26.96B").
- AC4 (JUDGMENT, graded by the CVO at L9 on the issuer's real run of the page): a PM reads each header fact's currency, why each
  "--" is empty, and each unmeasured reason, in plain words. Record it as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason`
  naming `3.0.0_SA_CVO~Z`; no verdict.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck` (clean) and `node src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs`
   (`CHECKS-OK 12 of 12` at the base).
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2,AC3,AC4 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   outer commit as your proof instance.
4. Report ONCE: the words you chose for each reason, every criterion's output line, the typecheck and harness lines, your portal
   and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-38 analysis @`9619211bcf` rulings 2-4 + s.4 item 2; CVO `ADJUDICATION_v44.md` FWD-20 defects 1-3. Base
portal origin/DEV e2130d42: ao3 currency/marks/words each build 0/1 control 1/1; harness 12/12; round-37 am3_check 2/2 + 2/2.
portal_ref e2130d42. A product-file candidate: `1.0.0_SA_CTO~Z` reviews the render before DEV.
<risk>LOCAL</risk>
<status>pending</status>
<round>39</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
