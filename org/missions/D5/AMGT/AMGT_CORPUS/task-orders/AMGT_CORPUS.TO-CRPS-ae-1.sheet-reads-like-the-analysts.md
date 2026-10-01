# AMGT_CORPUS task order -- `CRPS-ae-1` -- ROUND 29: the Model sheet reads like the analyst's

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ae-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures.
comp-adversary: RUN by the issuer at the cut on portal DEV e8a20ba9 -- face29.cjs 2 of 6 (FAIL as designed; arms 3 and 6 are controls); bound 4 of 4; tsc -b rc 0. Blind spots: one name (BA); the fixture predates the ad-4 re-derive, so BA's DPS and some P/E years read refused there and are skipped by the decimals arm; "currency once" is counted on the face text before the sheet.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 29. Serves FWD-12, FWD-20 and FWD-21: the Model tab reads like the
analyst's SharePoint sheet. By CONTRACT amendment 1, AMGT_CORPUS is the one writer of `ModelTab.tsx` through the Friday freeze.

## 1. THE CELL -- `CRPS-ae-1` (three rulings of the CTO, all display-only; every served value stays as served)

In `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` and `portal/src/pages/SecurityAnalysis/modelSheet.ts`:

1. **Consensus, labelled.**
   - Replace the subtitle "Adam's Model sheet, served from the model block -- nothing estimated in its place" with exactly
     "Reported figures and Bloomberg consensus estimates, from the model block".
   - Label the 2026E-2028E columns "Consensus (Bloomberg)" in the sheet's header (`<thead>`), e.g. as a spanning label above
     the E years.
2. **Decimals per row type.** Each sheet row has one type, declared where the rows are declared (`modelSheet.ts`), and every
   figure cell of that row (history and E columns) prints at that type's precision:
   - amounts in millions (Diluted shares `IS_SH_FOR_DILUTED_EPS`, EBITDA `EBITDA`, EBITDA (adjusted) `EBITDA_ADJUSTED`): 0 dp with
     thousands separators (e.g. `12,391`, `-10,232`);
   - per-share (Revenue/Sh `REVENUE_PER_SH`, EPS `IS_EPS`, BVPS `BOOK_VAL_PER_SH`, DPS `IS_DIV_PER_SHR`): 2 dp (e.g. `147.12`,
     `-0.83`);
   - multiples (P/E `PE_RATIO`, P/B `PX_TO_BOOK_RATIO`): 1 dp followed by `x` (e.g. `14.7x`);
   - percent and margins (Dividend yield, FCF yield, FCF margin, ROA, ROE, RoTA, EBITDA margin, Earnings margin): 1 dp followed by
     `%` (e.g. `3.6%`);
   - a row whose type the sheet does not name: 2 dp.
   The FULL served value stays exactly where it is today: `data-model-cell` and the tooltip's `data-full-value` keep
   `String(figure.value)`. A refused row keeps its refusal sentence unchanged.
3. **The currency, once per name.**
   - State the name's currency ONCE in the Model face above the sheet (e.g. "Figures in USD").
   - Take it from the block's MEASURED reporting currency: the served header figure the page already reads as `crncy`
     (`IDENTITY_CURRENCY_MNEMONIC`), or a measured reporting-currency header figure if one is served.
   - Row labels drop currency words: today's unit words "(USD per share)", "(millions, currency not stated)" and the like
     become "(per share)", "(millions)", "(%)", "(multiple)".
   - A row whose figures carry no measured currency (the cases that today print "currency not stated") gets a `*` at the end
     of its label.
   - Exactly ONE footnote line below the sheet reads "* currency not stated by the source for marked rows". It appears only
     when at least one row is marked.
   - Never repeat "currency not stated" per row.

**Harness re-anchor, NECESSARY only, granted.** If a check in `__harness__/modelPattern.harness.cjs` or `__harness__/tabs.harness.cjs`
anchors on the raw text this cell changes (a value's printed digits, the subtitle, unit words), re-anchor that ONE check onto the
same fact, keep its claim, and keep each harness at its floor (modelPattern 12, tabs 20). Never drop a check. Edit no other
harness.

**The rules every cell keeps:** C-PRESENTATION-ONLY -- formatting a served value for display is allowed; deriving a new figure is
not. **Design law (portal `DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; a heredoc on this machine turns `\b` into a
   0x08 byte.
5. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with `disarm_owner 2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/modelSheet.ts
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-ae-1.sheet-reads-like-the-analysts.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ae-1.sheet-reads-like-the-analysts.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/types.ts`, the issuer's
checks under `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round28/` and `.../round29/`, and DSGN's loader
and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ae-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round29/face29.cjs"; echo "exit=$?"</invocation><expect>THE SHEET READS LIKE THE ANALYST'S: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ae-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" AE1 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>AE1 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-ae-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node_modules/.bin/tsc -b --noEmit; echo "exit=$?"</invocation><expect>(?m)^exit=0$</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-ae-1" judgment="true"/>
</proof_of_spec>

- AC1 (`face29.cjs`, six arms on BA's served `/thesis` capture):
  1. the consensus label and the new subtitle;
  2. each printed figure matches its row type's precision;
  3. the full served values are still in `data-model-cell`;
  4. no visible "currency not stated", no USD in a row label, and USD exactly once on the face before the sheet;
  5. at least one `*`-marked row and exactly one footnote line;
  6. round 28's `face.cjs` (9/9) and `sheet.cjs` (6/6) still pass.
- AC2: the page's harnesses that load the Model tab stay green at their floors.
- AC3: the portal typechecks.
- AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's real run, never self-graded: the sheet reads like the analyst's.

## 5. WHEN YOU ARE DONE

1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit. Pin
   portal artifacts to portal commits and check each pin by content (`git -C portal show <pin>:<path>`). It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   commit as your proof instance.
4. Report ONCE: what changed (the row-type table, the visible header, currency and footnote wording), each harness re-anchor (old
   check -> new), every criterion's output line, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-28 analysis @`bd50135e57` s.2-3 (CVO v33 ad-3 AC4 PARTIAL). Base CLOUD `463e30ded8`, portal DEV `e8a20ba9`:
face29.cjs 2 of 6; bound 4 of 4; tsc rc 0. Deadline: on portal DEV before 22:00Z (placement freeze).
<risk>LOCAL</risk>
<status>pending</status>
<round>29</round>
<slot>~1</slot>
<fabric>site-z</fabric>
