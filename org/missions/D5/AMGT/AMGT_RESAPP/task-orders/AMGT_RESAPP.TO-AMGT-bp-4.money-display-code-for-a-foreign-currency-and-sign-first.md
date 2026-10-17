# AMGT_RESAPP task order -- `AMGT-bp-4` -- A MONEY FIGURE IN A CURRENCY THAT IS NOT THE PRICE CURRENCY PRINTS ITS CODE, AND A NEGATIVE ONE PRINTS ITS SIGN FIRST (ONE PORTAL FEATURE CUT FROM PROD `15bc21b3`, WITH ITS RECEIPT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bp-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~490</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bp-4.money-display-code-for-a-foreign-currency-and-sign-first</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN at the cut -- AC1's harness `src/pages/SecurityAnalysis/__harness__/moneyDisplay.harness.cjs` does not exist at PROD `15bc21b3`: `node` exits 1 with MODULE_NOT_FOUND (read here), so AC1 reads FAIL there as expected; AC2 run on a detached worktree at PROD `15bc21b3` itself (since removed) reads `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 21 of 27 pass, base 21 of 27, ...)`, so its expectation of 28 harness files and 22 passing is unmet there as expected; AC3 with the receipt absent ends in a FileNotFoundError traceback (rc 1). The worker runs AC1 against the unchanged page before any product edit (step 3).
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server; no browser, no HTTP.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-490` (branch `wk-AMGT_RESAPP-490`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-490`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bp-4` (round 109, decomposition s.118)

Two display faults on the Security Analysis page, both in how a money amount is printed. This ONE portal feature (Opal-internal, cut from PROD `15bc21b3`) fixes both. Page side only: no served value moves, no figure is changed, no existing sentence is reworded.

**What the page does today (read at PROD `15bc21b3`).** `src/pages/SecurityAnalysis/components/StatTile.tsx`: `currencyPrefix(code)` returns `$` for the served code `USD` and `<code> ` for every other code (`PHP `, `EUR `, `GBp `); `formatStatValue(value, format, currency, unit, currencyBasis)` builds a money string as `${currencyPrefix(currency)}${amount}` where `amount` already carries the number's minus sign. So (1) a negative amount prints `$-63.90B` (GOOGL US's net debt, served `NET_DEBT` -63902.0 in `MILLIONS`, USD); and (2) a USD figure prints a bare `$` even beside tiles in another currency: on ICT PM (price `PHP 860.00`, market cap in PHP) the enterprise value `CURR_ENTP_VAL` 33107.07 `MILLIONS` with served currency `USD` prints `$33.11B`, so one header row mixes PHP tiles and a `$` tile with nothing saying the `$` is a different currency.

**The change.**
1. **The sign leads the whole figure.** In `formatStatValue` (and anywhere else in `src/pages/SecurityAnalysis/` that builds a signed money string from `currencyPrefix`), a negative amount prints its minus sign BEFORE the currency prefix: `-$63.90B`, `-EUR 4.20M`, `-PHP 3.65B`; never `$-63.90B`. A positive amount, zero and every non-money format (`ratio`, `percent`, `shares-abs`) print exactly as today.
2. **A foreign-currency money figure prints its code.** `$` is printed only when the figure's currency is USD AND the name's price currency (the served `CRNCY`/`PX_LAST` currency of the same header, the one the price tile prints) is USD, or when no price currency is served for the name. A figure whose served currency is USD on a name whose price currency is NOT USD prints `USD ` and the amount (`USD 33.11B` on ICT PM, beside `PHP 860.00`). Every other code keeps printing as today (`PHP `, `EUR `, `GBp `). Implement it with ONE new optional last parameter of `formatStatValue`, `priceCurrency?: string | null`, which only `HeaderCards.tsx` passes (the header tiles are where the mix is visible); every other caller omits it and so prints exactly as today (apart from item 1's sign). Do NOT edit `WhatChangedPanel.tsx` (another cell of this round owns it), `ModelTab.tsx` or `PeersTab.tsx`: the sign fix lives in `formatStatValue`, so their callers get it with no edit.
3. **A census of every caller.** `formatStatValue` and `currencyPrefix` are called from five files (`components/HeaderCards.tsx`, `tabs/ModelTab.tsx`, `tabs/PeersTab.tsx`, `components/model/WhatChangedPanel.tsx`, `components/StatTile.tsx`; 24 occurrences at PROD). The harness reads those source files, lists every call site (file, line, which function) and asserts the set of files equals these five, so a sixth caller added later fails the harness.

**Fixtures (copy them into `src/pages/SecurityAnalysis/__harness__/`; all are committed in this repository, unedited live bodies read 2026-10-17).** From `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round109_prep/fixtures/`: `GOOGL_US_header_slice_live.json` to `moneyFixture.GOOGL_US.json` and `ICT_PM_header_slice_live.json` to `moneyFixture.ICT_PM.json` (each `{security_key, identity, header_figures, source}`; `header_figures` is the served list the header cards read: `PX_LAST`, `CUR_MKT_CAP`, `NET_DEBT`, `CURR_ENTP_VAL`, each with `value`, `unit`, `currency`). Read an existing harness in `__harness__/` that renders the header cards or the Model tab as your model (`ls __harness__/`; transpile the page's own files with the installed typescript, render with react-dom/server, stub only the boundaries you do not own, write no file); if none renders `HeaderCards`, render it directly with the fixture's `identity` and `header_figures` as its props.

**Do this in order.** (1) `cd C:/dev/wk-resapp-490/portal && git switch -c cand/dell1/amgt-sa-money-display` (from PROD `15bc21b3`, which your nested worktree is at). (2) Write the harness `src/pages/SecurityAnalysis/__harness__/moneyDisplay.harness.cjs` FIRST. It must check at least these 9, each named in the output: S1 `formatStatValue(-63902, 'currency-millions', 'USD')` is `-$63.90B`; S2 the same with `'EUR'` is `-EUR 63.90B` and with `'PHP'` is `-PHP 63.90B`; S3 the same three with a positive value print as before (`$63.90B`, `EUR 63.90B`, `PHP 63.90B`); S4 a negative `price` format (`-12.5`, `'USD'`) is `-$12.50`; S5 `ratio`, `percent` and `shares-abs` with a negative value print exactly what the PROD file printed (record the PROD outputs at step 3 into `moneyFixture.base_outputs.json` and compare to it); H1 the rendered GOOGL US header's NET DEBT tile reads `-$63.90B`; H2 the rendered ICT PM header's ENTERPRISE VALUE tile reads `USD 33.11B` and its PRICE tile still reads `PHP 860.00`; H3 the rendered GOOGL US header's market-cap and enterprise-value tiles still print a bare `$` (a USD name keeps `$`); C1 the caller census (above); D1 the difference control: every header tile text of both fixtures after the edit equals the text recorded at step 3 (`moneyFixture.base_tiles.json`, written from the UNEDITED page), except exactly two tiles that may differ (GOOGL US NET DEBT, ICT PM ENTERPRISE VALUE), named in the output with their before and after text. Print `MONEY DISPLAY HARNESS: YES (<n> of <n> checks)` or `NO`. If a premise above does not reproduce on a fixture (a field or a tile is not where this order says), file a BLOCKING row naming exactly what you found, finish what you can, and report; do not patch around it. (3) Create the two base files from the UNEDITED page (a small one-off node step or a record-base mode of the harness; commit them) and run the harness ONCE: it must print `NO` (or exit 1 on a failing check) with S1, S2, H1 and H2 failing; record that run. (4) Then make the product edits, only in `src/pages/SecurityAnalysis/` (expected: `components/StatTile.tsx` and `components/HeaderCards.tsx`, plus the harness folder). (5) Run AC1 to AC3. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~490/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, head commit, base `15bc21b3`, every changed path), `## Pages changed` (a table page | route | class | gate: Security Analysis | /security-analysis | Opal-internal | internal; any other page is a defect), `## Shared files` (`- none`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent with the `git diff 15bc21b3 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/security-analysis`, names `ICT PM` and `GOOGL US`, the header tiles). (7) Commit the branch in the nested worktree (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root). Do not stage `portal` in the outer worktree. NEVER push. (8) Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/amgt-sa-money-display --purpose "AMGT_RESAPP bp-4: a money figure in a currency other than the price currency prints its code, and a negative one prints its sign first" --pages "Security Analysis" --class opal-internal --how "cd portal && bun run dev:live --port 5174; /security-analysis, ICT PM and GOOGL US, the header tiles" --portal portal` and report its output verbatim. Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Portal repository only: nested worktree `C:/dev/wk-resapp-490/portal`, branch `cand/dell1/amgt-sa-money-display` from PROD `15bc21b3`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
2. Product edits only under `src/pages/SecurityAnalysis/` (the page's own files, its harness folder and its fixtures), and in the page only `components/StatTile.tsx` and `components/HeaderCards.tsx`; never `components/model/WhatChangedPanel.tsx`, `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx` or any file of another page. The saved value of every figure never changes: display only. Do not reword any existing sentence.
3. Do not register the approval row yourself (step 8 is `--check-only`) and commit nothing under `org/devices/`.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~490/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bp-4"><invocation>cd C:/dev/wk-resapp-490/portal &amp;&amp; timeout 300 node src/pages/SecurityAnalysis/__harness__/moneyDisplay.harness.cjs; echo "exit=$?"</invocation><expect>the line `MONEY DISPLAY HARNESS: YES (<n> of <n> checks)` with n at least 9 and every check named PASS; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bp-4"><invocation>cd C:/dev/wk-resapp-490 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round107_prep/checks/r107_feature_green_v3.sh" "C:/dev/wk-resapp-490/portal" 15bc21b3 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the line `R103 FEATURE GREEN: YES (typecheck rc 0, lint rc 0, harness 22 of 28 pass, base 21 of 27, regressions 0, pre-existing: assembled.harness.cjs exportCompare.harness.cjs posture.harness.cjs posturePattern.harness.cjs tabs.harness.cjs timelineFourStates.harness.cjs)` (the base's 27 harness files plus the new one is 28; the six names fail at PROD itself and read pre-existing) and `lint rc 0` read on `src/pages/SecurityAnalysis`; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-bp-4"><invocation>cd C:/dev/wk-resapp-490/portal &amp;&amp; python "C:/dev/wk-resapp-490/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_surface_check.py" --portal . --base 15bc21b3 --head HEAD --receipt "C:/dev/wk-resapp-490/org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~490/FEATURE_RECEIPT.md"; echo "exit=$?"</invocation><expect>every changed file listed as page, none forbidden or unnamed, and the line `R103 FEATURE SURFACE: YES (<n> files: <n> page, 0 shared named, 0 forbidden, 0 unnamed)`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~490 <0.9.0_WK_AMGT_RESAPP~490@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~490/AMGT_RESAPP.TO-AMGT-bp-4.money-display-code-for-a-foreign-currency-and-sign-first.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-490` on the committed bytes and report its verdict line. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-resapp-490`.

Report once:
- the branch name, its head commit and base;
- the harness run at the unchanged page (the NO line and the failing checks) and the run after;
- AC1's, AC2's and AC3's output lines;
- the receipt's `## What the branch carries` and `## Pages changed` sections, verbatim;
- the `--check-only` output verbatim;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 7490 and `ROUND_ANALYSIS.round108.md` items 3 and 4 (the CVO's slug, `REMEDIATION_v48`): ICT PM's overlay EV `$33.11B` beside PHP tiles, and GOOGL US's NET DEBT `$-63.90B` where the display rule is `-$63.90B`. Both live in `StatTile.tsx`'s money formatter (`currencyPrefix`, `formatStatValue`) and the header cards, so they are one cell and one candidate (the round-106 `bm-1`, round-107 `bn-1`, round-108 `bo-1` precedent). Premises measured at the cut (2026-10-17 ~12:0xZ): the served ICT PM header (`CURR_ENTP_VAL` 33107.07 MILLIONS, currency USD; `PX_LAST` 860.0 PHP; `CUR_MKT_CAP` PHP; `EQY_FUND_CRNCY` USD) and GOOGL US (`NET_DEBT` -63902.0 MILLIONS), `StatTile.tsx` at `origin/PROD` `15bc21b3` (read). The rule `$` only for a USD figure on a USD-priced name is the issuer's decision (s.118 (c)): the CTO said "every figure on a page carries one stated currency, or the conversion is shown"; a code beside a foreign figure states its currency and invents no conversion. The new parameter is optional and only `HeaderCards.tsx` passes it, so `WhatChangedPanel.tsx` (owned by `AMGT-bp-1` this round) is not touched. AC2's totals (28 files, 22 passing, base 21 of 27, six pre-existing names) were measured at the cut on a detached worktree at PROD `15bc21b3`.

<status>pending</status>
<round>109</round>
<slot>0.9.0_WK_AMGT_RESAPP~490</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
