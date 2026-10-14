# TO MDPF_SECHIST.TO-SH-t25 -- round 6 SH-t-25: the Positioning page passes and shows a carried holding's frontier date (the adapter rung under C1)

<to_id>MDPF_SECHIST.TO-SH-t25</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~24</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>CLOSEDMKTPORTAL</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-25` (`decompositions/MDPF_SECHIST_DECOMP_R6.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none (the producer apply of SH-t-24 follows this feature's PROD promote, CTO half condition C1)

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-MDPF_SECHIST-24` (branch `wk-MDPF_SECHIST-24`, cut from the issuance commit); its nested portal worktree `C:/dev/wk-MDPF_SECHIST-24/portal` is at portal PROD `6a5926fc11`. Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-MDPF_SECHIST-24`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

### THE CELL -- `SH-t-25` (FWD-9, CTO message 5585, C1 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_SECHIST_CLOSED_MARKET_FRONTIER_DEPLOY_20261014.md`)

The Positioning page's producer is about to serve two NEW optional keys. When a holding has no vendor day on its book's date (SALXX in the books DIVZ and IDVZ on 2026-10-12, Columbus Day) the producer carries the last vendor day's returns and says which day:

- per holding, `returns_frontier`: an ISO date string, present ONLY on a carried holding (e.g. `"2026-10-09"` on a book whose `data_as_of` is `"2026-10-12"`);
- per book, `returns_frontier_holdings`: `[{"ticker": "SALXX", "frontier": "2026-10-09"}]`, present ONLY when at least one holding carried.

The page's adapter (`portal/src/pages/Positioning/shared/etfAdapter.ts`, `toCurrentHolding`) is an enumerated allowlist and DROPS both keys today. Build ONE portal feature, a branch `cand/dell1/sechist-frontier-label` cut from PROD `6a5926fc11`, that passes both keys through and shows them. Display only: no served value changes; with neither key present the page renders byte-equal to today.

1. **Types** (`portal/src/api/portal-proxy.ts`, types only): `EtfHolding` gains `returns_frontier?: string | null`; `EtfPositioningBook` gains `returns_frontier_holdings?: { ticker: string; frontier: string }[]`; `CurrentHolding` gains `returns_frontier?: string`; the per-book value of `PositioningDataResponse['current_holdings']` gains `returns_frontier_holdings?: { ticker: string; frontier: string }[]`. Find each declaration with Grep; do not add anything else to that file.
2. **Adapter** (`etfAdapter.ts`): `toCurrentHolding` adds `returns_frontier: h.returns_frontier ?? undefined`; in `etfToPositioningShape`, `current_holdings[code]` adds `returns_frontier_holdings: book.returns_frontier_holdings` ONLY when that array is non-empty (an absent or empty array adds NO key, so a book with none carried adapts to exactly the object it adapts to today).
3. **Two small presentational components** in a NEW file `portal/src/pages/Positioning/tabs/ReturnsFrontier.tsx` (named exports, no hooks, no queries, ASCII only, no tooltip-only text):
   - `ReturnsFrontierMark({ frontier })`: returns `null` when `frontier` is falsy; otherwise a `<span>` whose visible text is `as of ` followed by the month-day of the ISO date (`"2026-10-09"` -> `as of 10-09`), small and quiet (`text-[10px]`, the same secondary tone the table's dash cells use: `text-[hsl(var(--palette-mediumGray))]`), on its own line under the number (`block`).
   - `ReturnsFrontierNote({ holdings })`: returns `null` when `holdings` is undefined or empty; otherwise a one-line note under the table: `Returns for ` + the tickers (comma separated, in the given order) + ` are as of ` + the dates they carry (full ISO, `TICKER date` pairs separated by `; `) + ` (no vendor day on the book date).`
4. **HoldingsTab** (`portal/src/pages/Positioning/tabs/HoldingsTab.tsx`): in the Performance mode cells (the block that maps `performancePeriods`, around line 971, inside `getHoldingPerformance`'s neighbourhood) render `<ReturnsFrontierMark frontier={...}/>` after the formatted value, for BOTH the value branch and the dash branch, where the frontier comes from the same `currentHoldings.holdings.find(h => h.ticker === holding.ticker)?.returns_frontier` lookup `getHoldingPerformance` uses (add a sibling helper `getHoldingFrontier(ticker)`, same `selectedPortfolio === 'CSM'` handling). Render `<ReturnsFrontierNote holdings={...}/>` once under the holdings table, reading the selected book's `current_holdings[selectedPortfolio]?.returns_frontier_holdings` (the CSM compiled blend has none: pass undefined). Touch nothing else in this file.
5. **Harness first.** Write `portal/src/pages/Positioning/__harness__/frontierLabel.harness.cjs` BEFORE any product edit, in the style of `portal/src/pages/SecurityAnalysis/__harness__/currencyAndReasons.harness.cjs` (open it first: it transpiles the page's own files with the installed typescript, renders with `react-dom/server`, stubs only boundaries it does not own, writes no file). Fixtures in the same folder: `frontierFixture.json` (an `EtfPositioningResponse` with book DIVZ `data_as_of` `2026-10-12` holding SALXX with `returns_frontier` `2026-10-09` and `returns_frontier_holdings` `[{SALXX, 2026-10-09}]` plus one ordinary holding AAPL without either key, and book PFDE `data_as_of` `2026-10-13` with ordinary holdings and neither key) and `frontierNoCarry.golden.json` (the adapter's output for the PFDE book of that fixture, generated ONCE by running the UNCHANGED adapter at the base; record that run). Checks, each named and printed PASS or FAIL: F1 the adapted SALXX row carries `returns_frontier` `2026-10-09`; F2 the adapted DIVZ book carries `returns_frontier_holdings`; F3 the adapted PFDE book (no carry) is deep-equal to `frontierNoCarry.golden.json` and has neither key anywhere; F4 `ReturnsFrontierMark` renders text containing `as of 10-09` for `2026-10-09` and an empty string for undefined; F5 `ReturnsFrontierNote` renders text containing `SALXX` and `2026-10-09` for the DIVZ list and an empty string for undefined and for `[]`; F6 `HoldingsTab.tsx` source contains `ReturnsFrontierMark` and `ReturnsFrontierNote` once each as JSX. Print `FRONTIER LABEL HARNESS: YES (<n> of <n> checks)` or `NO`. Run it ONCE on the unchanged page: it must print `NO` (F1 and F2 failing); record that run.
6. **Then the product edits**, only in the paths below. Run AC1 to AC3.
7. **Receipt** `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~24/FEATURE_RECEIPT.md` with the sections `## What the branch carries` (branch, head commit, base `6a5926fc11`, every changed path), `## Pages changed` (a table page | route | class | gate: `Positioning | /positioning | client-facing | firm-gated (infra/logic/registry/firm_pages.json lists /positioning)`; any other page is a defect), `## Shared files` (`- portal/src/api/portal-proxy.ts (types only: four optional fields)`), `## Not carried` (package.json, bun.lock, src/lib/firmAccess.ts, src/App.tsx: each absent, with the `git diff 6a5926fc11 HEAD -- <path> | wc -l` count, 0), `## How to look` (the dev build `cd portal && bun run dev:live --port 5174`, the page `/positioning`; the label shows only against the NEW served keys, so state in one line that the fixture `frontierFixture.json` is the way to see it until the producer serves them).
8. **Commit** the branch in the nested worktree (`.tools/safe-commit.sh` of the OUTER checkout with the author line below, `-F` a message file written with the Write tool, `--` the changed paths relative to the portal root); do not stage `portal` in the outer worktree; NEVER push. Check the approval row would register: `python .tools/open-calls.py add --check-only --kind approval --project NFRA_DEVPLN --box dell1 --branch cand/dell1/sechist-frontier-label --purpose "MDPF_SECHIST SH-t-25: the Positioning page passes and shows a carried holding's frontier date (closed-market returns), display only" --pages "Positioning" --class client-facing --how "cd portal && bun run dev:live --port 5174; /positioning, Performance view, books DIVZ and IDVZ once the producer serves returns_frontier" --portal portal` and report its output verbatim. Do NOT run it without `--check-only`: the issuer registers the row in the shared tree, and you commit no file under `org/devices/`.

### ACCEPTANCE

<criterion id="SH6-t25-AC1" cell_refs="SH-t-25"><invocation>cd C:/dev/wk-MDPF_SECHIST-24/portal && node src/pages/Positioning/__harness__/frontierLabel.harness.cjs; echo "exit=$?"</invocation><expect>FRONTIER LABEL HARNESS: YES</expect></criterion>

<criterion id="SH6-t25-AC2" cell_refs="SH-t-25"><invocation>cd C:/dev/wk-MDPF_SECHIST-24 &amp;&amp; timeout 590 bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_feature_green_v2.sh" "C:/dev/wk-MDPF_SECHIST-24/portal" 6a5926fc11 | tail -2; echo "exit=${PIPESTATUS[0]}"</invocation><expect>R103 FEATURE GREEN: YES</expect></criterion>

<criterion id="SH6-t25-AC3" cell_refs="SH-t-25"><invocation>cd C:/dev/wk-MDPF_SECHIST-24 &amp;&amp; python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_CHECKS/r6_portal_surface.py C:/dev/wk-MDPF_SECHIST-24/portal 6a5926fc11 HEAD; echo "exit=$?"</invocation><expect>PORTAL-SURFACE-OK files=7</expect></criterion>

<criterion id="SH6-t25-AC4" cell_refs="SH-t-25" judgment="true"/>

<expected_criteria>SH6-t25-AC1,SH6-t25-AC2,SH6-t25-AC3,SH6-t25-AC4</expected_criteria>

AC1 FAILS at the base (the harness does not exist; once written it prints `NO`). AC2 is the AMGT_RESAPP feature check (it takes the base ref as an argument). AC3 was AMENDED by the issuer after the first pass (worker row MDPF_SECHIST-D1-W24-S1: the AMGT surface checker `r103_feature_surface_check.py` accepts Security Analysis files only, so it cannot pass a Positioning feature); it is now `R6_CHECKS/r6_portal_surface.py`, which names the exact seven allowed paths and the four never-carried files; it FAILS at the base (`PORTAL-SURFACE-BAD ... missing=[...]`, 7 files missing) and PASSES at the candidate head. AC4 is the CVO's: the reading of the labelled cells and the note on the screenshot, not yours. Each invocation is bounded by its own `timeout`; set your shell tool's timeout to 600000 ms. For AC4 evidence only, you may produce one screenshot of the page against `frontierFixture.json` through `scripts/ui-smoke.mjs` if it runs without credentials; if it does not, say so in your report and move on.

### BOUNDS

- Portal repository only: nested worktree `C:/dev/wk-MDPF_SECHIST-24/portal`, branch `cand/dell1/sechist-frontier-label` from PROD `6a5926fc11`; never push; never touch `DEV` or `PROD`; never `git merge` DEV; no `bun install` (`node_modules` is a link to the main checkout's).
- Product edits only in the files named in steps 1 to 4 and the harness folder `portal/src/pages/Positioning/__harness__/`; never `package.json`, `bun.lock`, `src/lib/firmAccess.ts`, `src/App.tsx`, or any file of another page. ASCII only in code and comments (CLAUDE.md).
- Design contract (portal `CLAUDE.md` and `DESIGN.md`): light canvas, navy ink on white panels; the new text is secondary ink on the existing cell, no colour block, no tooltip-only content, no new accent colour.
- Anything odd outside this cell: append ONE surprise row (dell1 id form `MDPF_SECHIST-D1-W<n>-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) to `INVESTIGATION_v1.md` and keep working. If a premise of this order does not reproduce (a file, line or helper named here is not where the order says), do not guess: file a BLOCKING row naming exactly what you found, finish what you can, and report.
- Client-data bounds (standing): never read, search, copy or `git show` any `org/**/W73_S*_EVIDENCE.json`, commits 1ba8eafcda / f5645bb6e9, the ADVI_COTBKF ~74 / ~66 / ~70 cottonwood manifests, the IRPT_DASHBD tie-out files, or anything under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`.

<paths>
portal/src/api/portal-proxy.ts
portal/src/pages/Positioning/shared/etfAdapter.ts
portal/src/pages/Positioning/tabs/HoldingsTab.tsx
portal/src/pages/Positioning/tabs/ReturnsFrontier.tsx
portal/src/pages/Positioning/__harness__/
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~24/
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R6.md</decomp_doc> (round 6), cell `SH-t-25`.
<owned_cells>SH-t-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH6-t25-AC1, SH6-t25-AC2, SH6-t25-AC3 (AC4 is a judgment criterion: record it as UNVERIFIABLE-BY-INSTRUMENT with `status_reason` naming 3.0.0_SA_CVO, no verdict). Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~24/MDPF_SECHIST.TO-SH-t25.positioning-frontier-label.proof_of_spec.json`, `to_id` equal to the `<to_id>` line above character for character, validated from INSIDE your worktree with `python .tools/proof-of-spec-check.py <instance> SH6-t25-AC1,SH6-t25-AC2,SH6-t25-AC3,SH6-t25-AC4` (the ids are ONE comma-separated argument) BEFORE the flip. Commit the PORTAL change inside the nested worktree first, then the deliverables in `C:/dev/wk-MDPF_SECHIST-24` with `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_SECHIST~24 <0.9.0_WK_MDPF_SECHIST~24@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool). When the instance is VALID, flip this order's `<status>` to complete in your worktree copy.
</proof_of_spec>

Report once: the branch name, its head commit and base; the harness run at the unchanged page (the `NO` line and the failing checks) and the run after; AC1, AC2 and AC3 output lines; the receipt's `## What the branch carries` and `## Pages changed` sections verbatim; the `--check-only` output verbatim; any row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a branch in the portal repository and a receipt; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; git, node and bun only.
comp-adversary: RUN -- the harness does not exist at PROD 6a5926fc11, so AC1 reads FAIL there as expected (read by the issuer: the path is absent at the ref). BLIND: the feature tools' behaviour on a Positioning page (they were written for Security Analysis; the worker reports their verdict lines as printed), and the live render.
EGRESS CLASS, declared: NONE beyond `git fetch origin` (read) in the nested portal repository; the harness reads committed fixture files and renders with react-dom/server.
risk: LOCAL (a portal branch; DEV landing by `portal-merge-forward.sh` on an approved row, PROD only by a chosen-set promote). The page is CLIENT-FACING (partner firm `cottonwood`, `firm_pages.json`): the approval row's class is client-facing and waits on Andrew's word.
</preflight>

Source: CTO msg 5585 (arms a to c: a carried holding shows its frontier date beside its windows; the book names its carried holdings; with no carried holding the page renders byte-equal to today) on the C1 condition of the SH-t-24 pair. The SH-t-24 producer apply follows this feature's PROD promote.
