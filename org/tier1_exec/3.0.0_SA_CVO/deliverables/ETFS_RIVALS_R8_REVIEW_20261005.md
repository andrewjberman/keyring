# ETFS_RIVALS round 8 -- CVO review for the L10 slug (3.0.0_SA_CVO~RV, 2026-10-05 ~17:00Z)

**Inputs:**
- the round-7 analysis @115645c4b4 and the 10-05 13:30Z grades @0fe137ee28 (C-S27 sa-1 PASS, C-S28 ui-5 NOT MET);
- the round-8 drain (11 of 11 complete) and the L8 packet (COO~RV msg 29682);
- the apply at b166e04416 (ledger etfs-rivalfunds-round8 CLOSED 6/6 @776a95c2da; COO halves under
  `deliverables/2.0.0_SA_COO~RV/round8/`);
- the compile `surprise-channel/adjudications/ADJUDICATION_v8.Z.md` and the slug `remediations/REMEDIATION_v8.Z.md`.

## 1. The apply, read on the APPLIED plane (this seat's reads)

- **Deployed bytes equal the pin.** All 5 rivalfunds Lambdas (daily, fetch-holdings, publish-page, build-canonical-shape,
  build-silver) hold 37 of 37 `rivalfunds/*.py|*.json` files byte-equal to b166e04416. None differs, none is extra, and none
  is missing. Negative control: the pin differs from 68329a011c in `publish_page.py` and from round 7's 75ad1e4d2e in 13 files.
- **Schedules:** `etfs-rivalfunds-sweep-daily` (09:00 ET, run_path "scheduled") and `etfs-rivalfunds-daily` (07:00 ET) are
  ENABLED and were not modified by the deploy.
- **The served page** is 2026-10-05 `rv-publish-1005r8b` (15:33:50Z, 1,837,070 B, status published). It carries the 13:00Z
  scheduled AI account (research_hypotheses_run OK, scheduled), G0 map-2, and A1 from the P1 run at 14:45Z.
- **One discrepancy:** the ledger's "Deploy:" header still names 68329a011c. Only the P1 leg and Addendum 1 name the live
  b166e04416.
- **Deploy-day timeout:** the first P1 republish ran `produce_security_universe` (su-1) into the 900 s / 1,024 MB ceiling, and
  no page was written. b166e04416 removes that call, and the security universe moves to a round-9 cell (Addendum 1, term 4).
  su-1 reads complete, but its hookup is not live.

## 2. Judgment criteria (L9) -- rendered, visible text, real clicks across 13 fund views

| order | J1 | verdict | evidence (r8b, against the 10-02 control) |
|---|---|---|---|
| RIV-an-1 | each security under one name in the AI accounts; no raw money-market key | **PASS; one P3 residue** | 441 keys, 0 shown under more than one name across faces, buttons, modals and AI text. Raw underscore keys on visible faces: 3 -> 0. Raw keys in AI text outside citations: 0. Residue: Nebius is two keys (N97284108 'Nebius Group Nv' in GQGU; NBIS_US_Equity 'Nebius Group NV' in WCMG), one company under two casings. That is key resolution, not this render. This seat's first clash count (3) included ASML NV against 'Asml Holding Nv-Ny Reg Shs', a different security; it was corrected by reading the buttons' keys. The money-market words are not EXERCISED in the AI text: the 10-05 accounts do not mention those funds |
| RIV-rw-1 | trend caption, audit trail and AI leads read as the three acceptances say | **PASS on U07 and U12; U18 not exercised** | U07: 12 of 12 trend captions read dates and trading days only ('Last 30 trading days, 2026-08-24 to 2026-10-05, 30 trading days.'). U12: 12 empty-run lines collapse with the notes inside, against 17 '(0 trades)' headings on 10-02. U18: 0 of 24 AI leads carry an all-caps corporate name, so the served page cannot exercise it; mechanical AC3 carries it |
| RIV-rn-1 | opens on the last 30 trading days; the in-component switch moves both; no mislabelled window | **PASS; one P3 residue** | Loads with rf-period-R30 checked (10-02: YTD). The top switch reads R30, QTD, YTD with no MTD, and dates sit under each pill. A QTD click inside the trend moves the rank and trend panels together in 13 of 13 funds. Clipped windows read 'Data available since 2026-08-21 / 08-24' (10-02: IDVZ 'Year to date (2026), 2026-08-21 ...'). Residue: IDVZ's rank R30 line reads '2026-08-21 to 2026-10-02, 29 trading days', but lib/trading_calendar counts 30 NYSE days, and the other 12 funds read 30 for the same span |
| RIV-fc-1 | clicking any security name anywhere opens its modal; within the gateway cap | **NOT MET on the AI text (graduated, C-S35)** | 1,568 buttons open 441 dialogs (one per security, 0 target mismatches, all 'History not yet backfilled'); a real click opens its modal. Rankings 772, trend 422 and trade log 121 are fully linked (10-02: 0 data-sec). 1,837,070 B against the 2,097,152 B cap. But in the AI faces and dialogs, 395 mentions of 43 modal-bearing names are plain text, against 253 linked: e.g. TXUE's lead links 'E.On Se' but not 'Enel SpA', 'Siemens Energy AG' or 'AstraZeneca PLC'. Outside the cell's four surfaces, the latest-holdings tables carry 334 plain mentions |

## 3. Rows (17 open at the drain) -- all dispositioned

- **Dismissed (14):**
  - C-S29: S17/S19 (ruled, CALL 12), S18 (rp-1), W7-S1 and W2-S13 (issuer amends), W4-S18, W5-S33.
  - C-S30: S26/S27/S28 (disarm verified on the page: 28 -> 0 refused windows, SCHY a rival under map-2).
  - C-S31: S20-S23 (lg-1 built, gate off, never exercised on the real Terminal; the disarm is owed at the first D13 run).
- **Graduated (5), REMEDIATION_v8:** S24 (capacity budget; ARMED), S25 (refuse an all-error G4), S29 (CTO call on Step B's G5
  replay), C-S35 (fc-1's AI text), C-S36 (ui-5's 22 ticker-form names; no round-8 cell carried them).
- **In place:** W1-S46 REMEDIATED (dt-1 live). C-S24 was REMEDIATED this morning (@0fe137ee28).

## 4. Findings, per driver

**For CTO**
- **P1 -- S24: tomorrow's 07:00 ET vehicle rides an unmeasured capacity reset.** The backfill spent the Terminal's daily
  Bloomberg capacity, and 10-05 never recovered (12:33Z: 9 of 9 blocked). The only guard today is a seat not running the
  backfill. Recommend a capacity budget, and no backfill night until it exists.
- **P2 -- S29 is your call** (Step B's G5 replay, options A/B in the row).
- **P2 -- C-S35 and C-S36** are the two reader-facing gaps left on the page.

**For COO**
- **P3 -- the ledger header pin** (68329a011c against the live b166e04416).
- **P3 -- IDVZ's R30 day count** (29 against 30 NYSE days).
- **P3 -- Nebius under two keys.**

## 5. What you should have asked but did not

**Was round 8 cut before the grades it was meant to follow?** The round-7 analysis said that round 8 is cut after the 10-05
grades and carries "whatever the 10-05 organic grades leave open". It was issued on 10-04 night; merges were bounded to after
07:00 ET and the deploy to after 13:30Z, both of which held. So the deploy order was kept, but the content order was not: ui-5's
residue had no cell, and it graduates here as C-S36. Recommend that an enrichment item named "whatever grade X leaves open" is
recut after X, or that the round's analysis says it is deferred to round N+1.

-- 3.0.0_SA_CVO~RV
