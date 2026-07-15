# ~A lane -- directives #7-#8: UIUX_DESIGN built; /tax-pt1 LIVE + backfilled + guardrailed + verified SOUND (15:45Z -> 19:05Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE

Lane: 0.5.0_AE_OpalETL~A (Andrew sovereign-delegate lane). Window since laneA log @ efae9b327.
12 commits (11 workspace + 1 portal DEV), 2 gateway deploys (both SSM-verified), 4 Andrew rulings.

## Window summary

1. **Andrew-direct #7 (UIUX):** UIUX macro + UIUX_DESIGN registered + P0 built same-session --
   workspace-root `design/` = canonical design repository (anti-sprawl law; DESIGN_SYSTEM +
   PANEL_PRIMITIVES moved canonical w/ tombstone stubs; COLOR_ARCHETYPES = color-law home;
   LIVING_SOURCES pointer register; UI_VERIFICATION process law). Part B: all 15 tier-3 RD agents
   repointed via their ONE choke point (org/ref/prompts/react_designer.md; per-agent prompts embed
   nothing -- verified 0 matches). ws 210f70a9a + portal 3df9231e. COO fleet-relayed (DT covered);
   CTO filed both comp-tool notes durably @ c9cbeb3cb (incl. closing his own filed-vs-said gap).

2. **/tax-pt1 FIRST LIVE RUN (Andrew observing, step-by-step):** Yang's spec email re-read fresh
   ("Tax SMA Automation" 06-26); S0.3 byte-CONFIRMED w/ correction (pair = SSAVAIL/SSAVAIL2, not
   SSAVAIL1/2); PRELIM+FINAL landed + listing-verified; SCOPE PROOF exercised (Files.ReadWrite.All
   alone suffices -- NO IT ask; the 06-24 Sites.ReadWrite gap does not touch the drive endpoint).
   MCP-reconnect mechanism established: gateway tools deployed mid-session need /mcp reconnect.
   71b0fcde8.

3. **BACKFILL (Andrew GO):** 27 files, all trading days 06-29 -> 07-14 (07-03 holiday absent),
   35/35 listing-verified. DISCOVERY: FIS recurring bad-send mode -- 404-byte stubs + corrected
   re-sends hours later; re-sends are UPDATED SNAPSHOTS (07-10: +809 rows). 822474a03.

4. **Andrew-direct #8 (guardrails, "overengineer this"):** corpus profiled 35/35 server-side ->
   Content Contract v1.0 (eeddba83a; FIS 0164 fixed-width 200-char; trailer==linecount 35/35;
   as-of==prior trading day, holiday-proven; envelope 53,484-77,045 lines). EN-ROUTE FIND (fleet
   relevant): gateway read_site_file/read_file returned EMPTY-SUCCESS since inception (httpx
   follow_redirects=False swallowed Graph 302s) -- fixed c0cd853c1; CTO banked as instrument-class
   reference w/ 3 generalized lessons. Validator built (ssavail_contract.py C1-C7+C9, 8/8 battery
   incl. lying-checksum case) + validate_ssavail_attachment (SAFE, pre-save) + upload_text_to_site
   (write_files) -- a89bb53e6, deployed AFTER DT's BBGTML flip per explicit deconflict (COO
   sequenced, DT signaled directly, their ENABLED_INTEGRATIONS preserved + grep-verified).
   EXERCISED both rails: today's pair PASS w/ sha256 tie; 07-10 stub FLAG-STUB discriminating on
   C7 ONLY (C4/C5 pass on it -- right-axis proof). Flagged Files (w/ operator README) + Intake
   Logs LIVE in SharePoint. 07-01 TRUNCATED-VALID adjudication -> Yang (EXTRA-1 is complete file).

5. **Rulings:** schedule = "Yes B now, we will do A later" (operator-cadence LIVE, autonomous
   deferred; 099b1162c). Trigger = the /tax-pt1 SKILL INVOCATION, not a phrase (7305595ee).

6. **/verify (formal):** /tax-pt1 = SOUND (verifier==builder caveat held; all evidence exercised:
   collision path FIRED live for the first time -- Graph 409, zero overwrite; Alyssa standard
   write_files SSM-read on-box; sha256 chains tie; names match Yang's kept pattern).
   tax-pt2/pt3 = DOES-NOT-EXIST by design, records consistent. Primer /draw delivered in-chat.

## Deployment Sequence + Verification (AE)

Two gateway deploys via deploy-to-ec2.sh (i-07dccb1615503ac99), both APPLIED-truth verified:
```
c0cd853c1 @ 18:00:05Z -- redirect fix + profile_site_file; SSM md5: tools cf1b969b, graph 739a3dcb == local
a89bb53e6 @ 18:29:20Z -- validator + upload tool; SSM md5 x3 == local; ENABLED_INTEGRATIONS grep=1 (DT's enable preserved)
```
Manifest records: b42fbb32a, 9bfcb8c25. Deconflict: held on COO heads-up 181657Z -> DT DONE signal
182744Z -> deployed -> closed both ways.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pulse (auto) | ~8x via safe-commit | PASS | EC2_MANIFEST hot-node HOLDs read each time (bd-gold-trigger memory; unrelated); SKILL.md basename FPs persistent |
| surface-check (auto) | ~8x | PASS | 0 critical surfaces |
| owned-paths gate | 1 BLOCK | WORKED | docs/architecture/ = CTO lane -- contract moved to docs/briefs (right outcome, no override needed) |
| SSM (operational aws) | 4x | PASS | on-box md5s, entitlements cat, service state -- APPLIED-truth primitives |

What worked: the owned-paths block routed the contract doc to its honest home. What failed: my
first typecheck-style trap avoided this window, but the FIRST profile attempt returned 4x empty --
caught only because a 404-byte KNOWN-CONTENT file returned empty (the accidental positive control
CTO's banking now makes deliberate). Gap: none new filed (color-lint + design-scan-root items
already on comp-learns backlog).

## MCP traffic

~14 in / ~10 out. Significant: #7 broadcasts->ACKs (COO fleet relay; CTO c9cbeb3cb durable filing);
COO m365-restart heads-up -> my deconflict disclosure -> COO confirm -> DT direct DONE signal ->
closure both ways (a clean shared-box sequencing pattern worth reusing); #8 close broadcasts
(COO + CTO; CTO banked the false-green as memory reference_gateway_302_empty_body_false_green_httpx_redirects).

## Blockers

None open.

## Current State (zero-context handoff)

- **OPAL_TAXSMA:** /tax-pt1 SOUND + LIVE, operator-cadence (Option B). TAX/Short Sale continuous
  06-29->07-15 (35 files + 2 SharePoint aux folders: Flagged Files w/ README, Intake Logs w/
  commissioning log). Gateway (i-07dccb1615503ac99, manifest entry m365-mcp-gateway) @ a89bb53e6:
  tools list_email_attachments, save_email_attachment_to_site, profile_site_file,
  validate_ssavail_attachment, upload_text_to_site; contract module app/ssavail_contract.py;
  8/8 unit battery at tests/test_ssavail_contract.py. Contract doc:
  docs/briefs/OPAL_TAXSMA_SSAVAIL_CONTENT_CONTRACT.md (v1.0, 35/35 denominator).
- **UIUX_DESIGN:** P0 complete; design/ canonical; DECK DESIGN_BIBLE move-vs-pointer = open
  Andrew ruling.
- **OPAL_TICKET:** P0 on PROD (unfixed visual rode as passenger); contrast fix on DEV rides next
  promote; P1 awaits Andrew GO (Teams-sender design decision to bring first).
- **Gateway session mechanics:** new gateway tools REQUIRE an Andrew-side /mcp reconnect to
  surface; the tool list is a connect-time snapshot.

## Next Steps -- HANDOFF TO FUTURE SELF (Andrew-ordered; read this list before acting on anything)

1. **[self, TOMORROW ~7:00 ET + every trading morning until Option A]** The /tax-pt1 daily run --
   FIRST single-invocation exercise of the composed v2 flow (validate BEFORE save). Expect: 2
   emails, 2 PASS, 2 canonical saves, run-log to Intake Logs. If ANY FLAG or incomplete pair:
   re-run after ~9:00 ET (FIS corrections 8:10-8:20 ET; collisions on re-run = already-filed
   signal). The as-of recipe is PINNED in the skill (expected_last_trading_day(D-1) -- the fn
   INCLUDES D; do not "fix" it back). If the run surfaces a defect in the composed order, that
   is the named residual from the /verify -- fix in the skill, cite the verify record 7305595ee.
2. **[self, on Andrew/Yang word -- ASK if a week passes]** 07-01 swap: SSAVAIL2 20260701.ASC is
   TRUNCATED-VALID (14,152 lines); EXTRA-1 (67,236) is the complete same-as-of file. Swap =
   rename both in SharePoint (EXTRA-1 -> canonical, old -> ' SUPERSEDED'). NEVER silent-swap.
   Also pending from Yang: backfill acknowledgment + whether both-files-daily stays (his practice
   was FINALs-only sparse).
3. **[self, ~2026-07-22+ or Andrew word]** Option A (scheduled-autonomous): port the /tax-pt1
   flow verbatim to a server-side runner (EventBridge -> gateway-side job or Lambda). Precondition
   Andrew set: a week-ish of live Option-B mileage. The orchestration IS the skill's 7 steps; the
   validator + calendar recipe already separate cleanly (calendar stays estate-side -- decide the
   boundary consciously when porting).
4. **[self, gated on a FRESH manual Tax Lot export (Yang runs step-2 on a rebalance day)]**
   /tax-pt3 build: convert_cost_basis.py VERBATIM ({BASE},{date} injected only), inputs from
   Tax Lot/{YYYYMMDD}, outputs to Initial Holdings/{YYYYMMDD}. upload_text_to_site seeded the
   write path; large-binary writes may need an upload_file_to_site (base64) -- decide at build.
   /tax-pt2 remains a RESERVED name (step-2 manual-assist: validate+file Alyssa's downloads;
   commission only on Andrew's word).
5. **[self, on Andrew GO]** OPAL_TICKET P1 (cutoff sweep vs CUTOFF_ET=14:00, Teams-only claim
   links, requester asap-ack + claimed-by notify). BRING FIRST: the Teams-sender design decision
   (gateway holds Graph auth, so the sender runs gateway-side, not Lambda -- confirm w/ Andrew).
   Bobby@ re-adds to ROUTING_MATRIX when hired (~2026-08).
6. **[self, on Andrew ruling]** DECK DESIGN_BIBLE move-vs-pointer into design/systems/decks/
   (deck_generation/ is a working system -- do not move without the word). Also watch: next
   portal promote carries the ticket-center contrast fix to PROD (0.2.0_DT's lane; no action,
   just verify it rode).
7. **[standing]** New gateway tools need Andrew's /mcp reconnect; two-lane gateway deploys need
   explicit sequencing (the COO-brokered DT pattern from this window is the template). The
   drive-read false-green lesson: every NEW read instrument gets a DELIBERATE known-content
   positive control before trusting its output.
