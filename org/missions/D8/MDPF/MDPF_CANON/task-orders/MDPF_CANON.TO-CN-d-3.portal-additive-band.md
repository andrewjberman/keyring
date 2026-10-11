# MDPF_CANON task order -- `CN-d-3` -- THE GLOBAL TREND STACK MEETS THE LINE: THE TWO ADDITIVE SERIES RENDER AS THEIR OWN BANDS (W8-S3, FWD-3; PORTAL DEV CANDIDATE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-d-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~12</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; one reader and one page.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS; the portal reads fields the served global object already carries.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at portal DEV c96efe1714 -- `r4_cn_d_3.py reader` reads 1 of 4 and `page` 1 of 5 at base (the controls pass, the builds fail); `selftest` proves a reference patch reads 4 of 4 and 5 of 5 and two mutants (a null coalesced to 0; a client sum of the two fields) fail.
EGRESS CLASS, declared: NONE (the worker reads no AWS and writes none).
</preflight>

**Your worktree:** the spawn names it (outer branch `wk-MDPF_CANON-12`, cut from the issuance commit). The portal is a NESTED repository at
`<worktree>/portal`, already provisioned on its own branch `wk-MDPF_CANON-12-portal` cut from portal `DEV` c96efe1714 with `node_modules` linked.
Start every shell call with `cd` into the outer worktree path: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base
checkout. Edit the two portal files by their path under `<worktree>/portal/`.

## 1. THE ACT -- `CN-d-3` (round 4, decomposition v4)

THE DEFECT. The Global AUA trend (Model Portfolios page, Global view) stacks the model bars and the Non-Model band, and anchors its tooltip Total on
the producer's `opal_aggregate_aua`. The served global object also carries two additive series, `sma_additive_aua` (non-null on 24 of 493 dates) and
`tax_additive_aua` (non-null on 7), and on every date where either is non-null the producer's identity is

```
opal_aggregate_aua = model_aua + non_model_aua + sma_additive_aua + tax_additive_aua     (a None additive term counts as absent)
```

The page never reads the two additive series, so on those dates the stack sits BELOW the line by their sum and the tooltip rows do not add to the Total
(about 1.4 percent on 2026-10-08). The sleeves are `cohort_class: 'sma'` entries in `by_model` (display names `PFDE` and `Tax-Managed SMA`), which the page
deliberately keeps out of the model bars (the Global branch builds `nonSmaKeys` at `src/pages/ModelPortfolios.tsx:775`). Do not change that.

THE FIX. Read each additive series as a FIELD READ and render each as its own stacked band above Non-Model, for the Global view only. Both files use
CRLF line endings (0 LF-only lines at c96efe1714): keep them, and confirm with `git -C portal diff --stat` that the diff is a few dozen lines, not the
whole file.

### 1a. `portal/src/lib/pairedProvenanceRead.ts` (this module is the ONLY legal reader of the raw value arrays; it imports nothing)

1. Interface `ProvenancedFirmSeries` (line 156): after `non_model_aua?: Array<number | null>` (line 159) add
   `sma_additive_aua?: Array<number | null>` and `tax_additive_aua?: Array<number | null>`.
2. Interface `GlobalEnterprisePoint` (line 767): add `smaAdditiveAua: number | null` and `taxAdditiveAua: number | null`.
3. `readGlobalEnterpriseSeries` (line 774): in the returned object add `smaAdditiveAua: series.sma_additive_aua?.[i] ?? null` and
   `taxAdditiveAua: series.tax_additive_aua?.[i] ?? null`. A missing array or a null cell reads `null`, never `0`: absent is not zero.
4. Extend the doc comment above it (line 756): the Global identity is `oaa == model + non_model + sma_additive + tax_additive`, the two additive
   terms are None where no sleeve is counted, and consumers still read, never compose.

### 1b. `portal/src/pages/ModelPortfolios.tsx` (anchors at c96efe1714)

1. `STACK_SERIES` (line 146): append, AFTER the `non_model` entry (line 154), `{ key: 'sma_additive', label: 'Additive SMA sleeves' }` and
   `{ key: 'tax_additive', label: 'Tax-Managed SMA' }`. The array is a closed literal mounted in registration order: do not mount conditionally.
2. The `globalEnterpriseByPeriod` map value type (line 462): add the two new fields to its type literal.
3. After `hasGlobalEnterprise` (line 468) add two memos in the same style, `hasGlobalSmaAdditive` and `hasGlobalTaxAdditive`: true when any point of
   `globalEnterprise` has the respective field non-null.
4. Period-end bar rows, the block that ends with the `nmKey` branch (lines 1874-1883): immediately after `const nmKey = keyForModel('Non-Model')` and
   its if/else chain, set `dataPoint['sma_additive']` and `dataPoint['tax_additive']` to
   `globalEnterpriseByPeriod.get(aggregateItem.period)?.smaAdditiveAua ?? null` and `...?.taxAdditiveAua ?? null`, ONLY when
   `!timeSeriesData.isPerFirm` (otherwise `null`). Both fields must be read within 30 lines after the `const nmKey` line.
5. Daily area rows, the second `const nmKey = keyForModel('Non-Model')` (line 2066): the same two assignments with `period` in place of
   `aggregateItem.period`, within 30 lines after that line.
6. Both stack mounts, the `const show =` expressions (lines 1969-1971 for the Bars and 2197-2199 for the Areas): keep the existing `non_model` and
   model branches unchanged and add `s.key === 'sma_additive'` -> `!timeSeriesData.isPerFirm && hasGlobalSmaAdditive`, and `s.key === 'tax_additive'`
   -> `!timeSeriesData.isPerFirm && hasGlobalTaxAdditive`. Everything else in the mounts stays as it is.
7. `renderTrendLegend` (line 1128): after the Non-Model entry (line 1139-1141) add one entry per band, shown only when `effectiveFirmId === 'global'`
   and the respective `has...Additive` is true, labelled with the band's label, coloured `getModelColor(label)?.primary || PALETTE.gray300`.
8. Leave alone: the tooltip (it derives rows from the payload and anchors on `total_aua`, which is already `opal_aggregate_aua` for Global; an
   unlisted name sorts last), the `plottedKeys` whole-day-gap filter (additive must never keep a row alive on its own), the donut, every per-firm
   path, and `src/lib/modelPortfolioColors.ts`.

LAWS THAT BIND THIS EDIT. (i) FIELD READ: no arithmetic between an artifact field and the pixel (the page's own 0340Z ruling): do not sum the two
additive fields into one value anywhere. (ii) Absent is not zero: a null additive renders as no band on that date. (iii) Global only: a per-firm view
shows no additive band and no additive legend entry. (iv) The provenance read guard stays green (`node scripts/provenance-read-guard.mjs` in the
portal prints `OK:`).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Row id form `MDPF_CANON-D1-W12-S<k>` (dell1's registered coordinate is D1),
`disarm_owner` `2.0.0_SA_COO~D1`. If a band's resolved colour equals another series' colour, file an OBSERVATION row naming both hex values: do not edit the
colour registry.

## 2. BOUNDS

1. Portal repository only, on branch `wk-MDPF_CANON-12-portal`; never push; never touch `DEV` or `PROD`; no merge.
2. Edit only the two files in section 3 (plus your deliverables and the surprise channel). No new component, no token change, no new dependency.
3. No AWS call of any kind, no deploy, no store write. No `bun install` (the modules are linked). No browser launch.
4. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file. The check uses synthetic numbers; keep to that.
5. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF.
6. If an item cannot be met inside your paths, file a row and stop on that criterion: the issuer rules it, you do not route around it.

## 3. SURFACES

<paths>
portal/src/lib/pairedProvenanceRead.ts
portal/src/pages/ModelPortfolios.tsx
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~12/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/scripts/provenance-read-guard.mjs` and
`portal/src/lib/modelPortfolioColors.ts`. The issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_3.py` is read-only (never edit it); read its two
subcommands to see exactly what each arm asserts.

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-d-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_3.py" reader; echo "exit=$?"</invocation><expect>ROUND 4 BAND-READER: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-d-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_3.py" page; echo "exit=$?"</invocation><expect>ROUND 4 BAND-PAGE: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-d-3" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-4 close (never self-graded): the issuer renders the Global trend headless against a fixture shaped like the served
global object (the `/frontend-dev` method, `scripts/ui-smoke.mjs --fixtures`) and the CVO reads the screenshot -- the bands sit above Other AUA on the
additive dates only, the legend names them, and on a sampled additive date the tooltip rows add to the Total. You do not render; the issuer does.

## 5. WHEN YOU ARE DONE

1. Commit the two portal files INSIDE the nested repo: `git -C "<worktree>/portal" add -- src/lib/pairedProvenanceRead.ts src/pages/ModelPortfolios.tsx`
   then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~12 <0.9.0_WK_MDPF_CANON~12@opal.agent>" -F <msgfile>` (message file written with
   the Write tool; confirm with `git -C "<worktree>/portal" log -1`). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at
   `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~12/MDPF_CANON.TO-CN-d-3.portal-additive-band.proof_of_spec.json`, with AC3
   UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-4 close". **Flip this order's `<status>` to `complete` in the SAME commit as your
   proof instance**, and only when AC1 and AC2 both pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~12 <0.9.0_WK_MDPF_CANON~12@opal.agent>" -F <msgfile> -- <paths>`
   (naming the outer paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its
   verdict line.

Report once: the portal branch and commit hash, the diff (one line per file: lines added and removed), the output line of AC1 and AC2, the outer commit
hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round3.md` @ae094ea51d section 3 item 3 (the Global stack meets the
line, W8-S3). A portal candidate touching a product file: it comes to `1.0.0_SA_CTO~DELL1` for review BEFORE any DEV landing, with the issuer's render
beside it; a PROD promotion is a separate pair under the push law (this page can be opened by a partner-firm login for its own scope, so the receipt
names the page and its class, and unsure is client-facing). Independent of the fold cell: it reads fields the served global object already carries
(measured 2026-10-11 on `portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-08.json`: `sma_additive_aua` non-null 24, `tax_additive_aua` 7,
`opal_aggregate_aua` equals the four-term identity on 484 of 484 valued dates, the two-term identity fails on 24), so it is its own chain and runs in
parallel in slot ~12. DRAIN CHECKS (the issuer's, not criteria): `bun run typecheck` and `node scripts/provenance-read-guard.mjs` in the portal worktree,
once, after the commit; the `ui-smoke` render for AC3.

**RISK CLASS:** `LOCAL`. The paths imply no more: `portal/src/` is the LOCAL floor in `.tools/to-pipeline-gate.py` GATE (xii) (its self-test admits a
`<risk>LOCAL</risk>` order on `portal/src/a.tsx`), the order writes no AWS and the candidate lands on portal DEV only. `worker-light`: about 40 product
lines over two files, every anchor inlined.

**FORKS FOR THE ISSUER:** (1) one cell with two bands, not one summed band: the CTO's item reads "as their own band" and the 0340Z ruling forbids client
arithmetic, so each additive series is its own key; a single summed band would need a producer field. (2) The label for the SMA sleeves is generic
('Additive SMA sleeves') because `sma_additive_aua` is the sum of every additive sleeve (today PFDE only); a pinned colour for that label is a
`modelPortfolioColors.ts` edit and is the CTO's, not this cell's. (3) The `ui-smoke` fixture for AC3 needs the served global timeseries as a body for the
page's global fetch URL substring: build it from a read-only get of the served object and keep it out of the repo.

<status>pending</status>
<round>4</round>
<to_id>MDPF_CANON.TO-CN-d-3</to_id>
<slot>~12</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
