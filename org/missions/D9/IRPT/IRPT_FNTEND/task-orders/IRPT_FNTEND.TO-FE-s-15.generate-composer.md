# TO IRPT_FNTEND.TO-FE-s-15 -- the Generate composer (F5 at v0.6, S10)

<to_id>IRPT_FNTEND.TO-FE-s-15</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-11</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F5 v0.5/v0.6, S10 `docs/research/investor_reporting_ycharts_variants_20260911/UI_CONTRACT.md` @72acd16e66; CONTRACTS `AnalysisRequest` request half) | **Decomp cell:** `FE-s-15` (round 2, v0.2) | **outcome_ref:** FWD-4 | **depends_on:** `FE-s-13`, `FE-s-14` (R1: the v1 client) | **slot:** ~1, queue position 3 | **slug rows:** W3-S2, C-S43 (clean/correction)

---

## WORKER FACE

### THE CELL

`FE-s-15` -- the Analysis tab (`tabs/analysis/`, built by FE-s-6 on v0.4's shape) gains the Generate composer the PRD's F5 row specifies at v0.6, and reads revision identity and section support from the wire fields FE-s-13 adapted. The composer PRODUCES the browser request half of `AnalysisRequest` and nothing else from the browser, in this order:

1. **Client** -- the header's current selection (never re-entered in the tab).
2. **Account(s)** -- the permitted accounts of that selection with a confirmable default; an account NUMBER is a display label and is never treated as a vendor identity.
3. **Holdings snapshot** -- preselected from the wire `HoldingsSnapshot` the tab already holds, shown WITH its as-of; an immutable `snapshot_id`; the tab never fetches a different "latest" while a job is open.
4. **Comparisons** -- zero to five ORDERED selections by OPAQUE catalog keys (the catalogue the wire scope carries; vendor ids never shown).
5. **Title** -- optional; otherwise derived for display from the client/account label and comparison names (the request sends `null` when not overridden).
6. **Prepared-for / prepared-by / contacts** -- prefilled from the profile fields the wire scope carries; overrides only where the wire policy allows; nothing invented.
7. **Variant** -- resolved by comparison count and DISPLAYED: 0 = Overview, 1 = Comparison, 2-5 = Multi-Comp; `variant: 'auto'` is sent unless the advisor picks; an explicit pick inconsistent with the count is refused client-side before submit; a sixth comparison is refused.
8. **request_id** -- a stable idempotency key minted per click, preserved across transport retries; any changed input mints a new one.

The request body is exactly `{ request_id, client_id, account_ids, snapshot_id, variant, comparison_keys, report_title }` and never carries a `resolved` key or any server-only field; it is submitted through the typed client's `analysis-requests` operation (`POST .../analysis`, the contract's producer name -- AMENDED on `docs/contracts/investor-reporting/v1/` @7ce4761a2f: the response envelope's `data` is the issued `identity` and `stage`, its `status` is REQUIRED). Job states `queued / preparing / generating / ready / needs attention` render from the `status` the `analysis-report` envelope carries (`GET .../analysis/{jobId}/sections`, polled through the typed client -- the contract names NO consumer operation for `status/{jobId}`; the tab polls through `analysis-report`) -- never vendor background polling; a WAF-refresh or reconciliation state renders as needs attention WITH the request preserved (the composer's inputs unchanged, resubmittable), never as a failed request. A correction is NOT a route (`submit-correction` is NOT-A-ROUTE under v1): it is a NEW `analysis-requests` submission whose `AnalysisRequest.corrections` field carries the correction, minting a new `request_id`.

**W3-S2.** Revision identity and section support come from the wire fields the schemas name: `AnalysisRequest.identity` / `corrections` / `stage` / `release` and `AnalysisReport.extraction_validation` / `release` through the FE-s-13 adapters; `parity.ts`'s local derivation and any `inputRevision` fallback are removed; a clean request and its correction preserve the identity the wire carries.

Everything FE-s-6 built (request list under the no-route bound, input review and correction as a NEW revision, stage display without percentages, native sections, vendor PDF preview labelled as such, MODELED never actual) stays; the composer is added above it.

### ACCEPTANCE

<criterion id="F15-AC1" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F15-AC1` -- the whole portal typechecks.

<criterion id="F15-AC2" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-15/composer.test.ts</invocation><expect>REQUEST KEYS: 7 of 7</expect></criterion>
`F15-AC2` -- composing from the header selection, two accounts, the held snapshot and two comparison keys yields a body whose key set is exactly the seven S10 keys, `snapshot_id` equal to the held snapshot's id, `comparison_keys` in the selected order.

<criterion id="F15-AC3" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-15/composer.test.ts</invocation><expect>RESOLVED-KEY LEAKS: 0</expect></criterion>
`F15-AC3` -- the body and the adapter's request output carry no `resolved` key and none of the ResolvedScope schema's server-only keys (the test prints the keys it scans for).

<criterion id="F15-AC4" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-15/variant.test.ts</invocation><expect>VARIANT BY COUNT: 4 of 4</expect></criterion>
`F15-AC4` -- 0, 1, 2 and 5 comparisons display Overview, Comparison, Multi-Comp, Multi-Comp and send `variant: 'auto'`.

<criterion id="F15-AC5" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-15/variant.test.ts</invocation><expect>REFUSED: 2 of 2</expect></criterion>
`F15-AC5` -- an explicit `comparison` pick with 3 comparisons and a sixth comparison are each refused client-side (no submit reaches the adapter's call log).

<criterion id="F15-AC6" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-15/request-id.test.ts</invocation><expect>REQUEST ID: stable-on-retry, new-on-change</expect></criterion>
`F15-AC6` -- a transport retry sends the same `request_id` (call log: 2 sends, 1 distinct id); changing one comparison mints a new id.

<criterion id="F15-AC7" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-15/job-states.test.ts</invocation><expect>JOB STATES: 5 of 5</expect></criterion>
`F15-AC7` -- queued, preparing, generating, ready and needs-attention each render one distinct label from an `analysis-report` envelope fixture whose `status` carries the state (AMENDED: the envelope's status, not a status-job call); the WAF-refresh fixture renders needs attention and the composer's inputs deep-equal their pre-submit values.

<criterion id="F15-AC8" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-15/identity.test.ts</invocation><expect>REVISION IDENTITY: preserved</expect></criterion>
`F15-AC8` -- a clean wire request and its correction render the identity fields the schema names unchanged, and a source grep of `tabs/analysis/` for `inputRevision` returns 0 hits (printed).

<criterion id="F15-AC9" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-15_analysis_clean_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-15-clean.json --click Analysis --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Analysis</expect></criterion>
`F15-AC9` -- the Analysis tab with the composer and a clean request at 390.

<criterion id="F15-AC10" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-15_analysis_needs_correction_390.png --port <PORT> --width 390 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-15-needs-correction.json --click Analysis --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Analysis</expect></criterion>
`F15-AC10` -- the tab in needs-correction at 390.

<criterion id="F15-AC11" cell_refs="FE-s-15"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F15-AC11` -- the whole Investor Reporting set is green.

<criterion id="F15-AC12" cell_refs="FE-s-15" judgment="true"/>
`F15-AC12` -- graded at L9 from the two PNGs: the composer reads in the S10 order, the variant is displayed, and the clean and correction states are distinguishable. RECORD; NO VERDICT.

<expected_criteria>F15-AC1, F15-AC2, F15-AC3, F15-AC4, F15-AC5, F15-AC6, F15-AC7, F15-AC8, F15-AC9, F15-AC10, F15-AC11, F15-AC12</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. The typed client and the adapters are FE-s-13's and are READ only; a wire field the composer needs that the adapter does not expose is a surprise row, never an edit there. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Numbers.** The 0.30% fee stays a displayed setting from the contract; no fee, count or width constant in `tabs/analysis/`. 390 is a test setup.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: `src/pages/InvestorReporting/tabs/analysis/ src/pages/InvestorReporting/fixtures/smoke/ src/pages/InvestorReporting/__tests__/fe-s-15/`. Workspace records under org/ only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints; kill it before your final report. Routes without a leading slash.
- **Fixture maps name the whole page's needs** (resolve-scope, the default Reporting tab's performance report, holdings, the analysis fixtures under test, status).
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W1-S<k>` continuing the W1 sequence (read the file for the last W1 id); never edit an existing row; keep working.
- Report push state as LOCAL.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-15/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.2 @430c5fcb4a, cell `FE-s-15`.
<owned_cells>FE-s-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F15-AC1` .. `F15-AC12`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-15.generate-composer.proof_of_spec.json`
(phase `BUILD-GENERAL` -- AMENDED BY THE ISSUER at the FE-s-12 drain on row IRPT_FNTEND-W1-S15: the schema's phase enum has no BUILD member, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F15-AC1,F15-AC2,F15-AC3,F15-AC4,F15-AC5,F15-AC6,F15-AC7,F15-AC8,F15-AC9,F15-AC10,F15-AC11,F15-AC12` BEFORE the `complete` flip. `F15-AC12` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `generate-composer.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written; the Generate route and the job record are the counterpart's.
comp-adversary: RUN at L4 on PRD v0.6 (ADMITTED) -- carried; S10 consumed by F5 at v0.5/v0.6.
lane: the <paths> block IS the grant; portal paths bind by reading; workspace paths bind mechanically. tabs/analysis/ was FE-s-6's; that cell is terminal.
</preflight>

Seating: slot ~1, queue position 3; seated when `FE-s-13` is terminal and drained, fresh worktree pair from HEAD.
