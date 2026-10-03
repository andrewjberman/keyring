# ETFS_RIVALS round 6 -- CVO review for the L10 slug (3.0.0_SA_CVO~RV, 2026-10-02 ~20:30Z)

**Inputs:**
- the round-5 analysis `ledger/ROUND_ANALYSIS.round5.md` @a059825ea9;
- the round-6 drain (59 of 59 terminal);
- the apply at pin eb6e9f04ff (COO~RV msg 28718; ledger 20261002T1942Z CLOSED; pair: CTO 15f3366309 19:35Z, COO 03036ef58b
  19:36Z);
- the compile `surprise-channel/adjudications/ADJUDICATION_v6.Z.md` (part A @692477fa57, part B with this slug);
- `remediations/REMEDIATION_v6.Z.md`.

## 1. The apply, read on the APPLIED plane (this seat's reads)

- **Deployed bytes equal the pin.** `etfs-rivalfunds-daily-lambda` and `rivalfunds-publish-page-lambda` each hold 36 of 36
  `rivalfunds/*.py|*.json` files byte-equal to eb6e9f04ff. Positive control: the deployed `render.py` differs from its
  722f0db291 version.
- **The secret came before the apply:** created 19:44:32Z; the apply LastModified is 19:46:29Z.
- **The daily environment is applied:** RIVALFUNDS_AI_ENABLE=1 and RIVALFUNDS_OPENAI_SECRET=rivalfunds/openai-api-key. The
  publish-page Lambda has no environment.
- **The grants are scoped as signed** (simulate-principal-policy on the daily role):

  | action | target | decision |
  |---|---|---|
  | s3:PutObject | gold/research_hypotheses/... | allowed |
  | s3:DeleteObject | gold/research_hypotheses/... | implicitDeny |
  | GetSecretValue | rivalfunds/openai-api-key-* | allowed |
  | GetSecretValue | opal/openai/news-trending-* | implicitDeny |

- **Served pages:**
  - 2026-10-02 `rv-publish-1002r6`: published, 13 of 13, readback true, 1,833,385 B, 0 `<script>`;
  - 2026-09-30 `rv-ai-0930r6`: published, 12 of 13 (GQGU is one trading day behind, W5-S28).
  - The CTO half names the "09-30 AI fire" in its blast radius.

## 2. The six judgment criteria (L9)

| order | J1 | verdict | evidence |
|---|---|---|---|
| RIV-ui-2 | one count chip per block; the method text once per page behind an info element; an empty period shows its state | **PASS** | 39 ranking blocks with one `rf-chip` each (6 sampled). "Priced from" occurs once, inside `details.rf-method`. IDVZ MTD/QTD read "Nothing ranked for IDVZ, month to date. None of its 40 holding(s) has a price on file", with 0 empty table shells (1002g rendered four) |
| RIV-ui-3 | month ticks read without overlap at 1280-1920 px; names wrap to at most two lines | **PASS** | The month record moved into the holding popover (fixed 1080 px at both widths). Jan-Oct read cleanly, with "no data" before history and "no trade" after: looked at in the 1280 screenshot. The probe's own overlap count found only 7 leaf labels, so the screenshot is the evidence. The visible trend card's 16 names render on 1 line each at 1280 and 1920. Figures now read "+$2.2m" (1002g showed dollar precision) |
| RIV-ui-4 | each account opens to its first two sentences; the vintage line where tables differ | **PASS** | A grounded account's face is its first two sentences plus "Read the full analysis and its citations". A FAIL account's face is the FAIL and "Open the account for audit", never prose presented as analysis. "Written against earlier tables: buying_trend 2026-10-02 11:04Z (this page serves 2026-10-02 19:49Z); holding_contribution ... 11:03Z ... shown as written and is not rewritten" |
| RIV-ui-5 | one display name per security across the page | **NOT_EVALUATED** | The order says the Bloomberg-sourced names arrive with the 2026-10-05 vehicle run. Graded on that page |
| RIV-r-6 | the next AI run names securities by name and writes figures in display form | **PASS on the prompt; names residue to ui-5** | Run 20261002T195217Z-ai (a1-chain/5, 24 accounts), against the 10-02 seat run (a1-chain/3): source ids `fear_greed/...` 106 -> 0; 6+-decimal floats 0 -> 0; underscore keys 23 -> 0; ticker forms 268 -> 129. Both positive controls flip: TXUE now writes "Orange" and "Enel" (was "ORA FP Equity"), and IDVZ now PASSes grounding. All 129 remaining ticker forms sit in 4 funds (ETFT, PCLG, TSEL, WCMG), whose served holding names ARE the ticker strings (grades 2-3 showed "TXN US Equity", "VEEV US Equity" as names). 4 raw CUSIPs remain, among them BASG's "entered 02043Q107 at $5.2 million", where no name exists. A per-token test against the cited rows had no denominator (the rows carry no name field) and was discarded |
| RIV-ap-1 | the first SCHEDULED account reads as well as a seat run's | **FAIL** | The accounts are good: 24/24 PASS, 0 web reads, median 179 words against 164, coherent and in display form (BASG and TXUE read in full). But no scheduled path produces them on a normal day; they came from a deliberate `only:[publish-page]` fire. See C-S24, graduated |

## 3. Findings, per driver

**For CTO**
- **P1 -- C-S24 (graduated): the AI accounts are still not a production act.**
  - On 2026-10-05 the morning page publishes through the publish-page Lambda without the gate, and the 09:00 sweep then sees the
    marker and does nothing, so the page carries no accounts with no seat awake.
  - Recommended shape: the sweep runs the AI stage as its own step, then republishes.
  - Not recommended: the AI gate on the publish-page Lambda. That would put up to 48 vendor calls with 120 s timeouts in front
    of the morning page write.
- **P2 -- provenance:** the 09-30 run's manifest says run_path "scheduled" for an `only` fire. A value must carry its claim, and
  "scheduled" should be reserved for the schedule.

**For COO**
- **P2 -- W4-S9 is still ARMED.** Round 6's issuer act I-1 (one marker batch above 45 dates, carried by the first backfill) has
  not run.

## 4. The FAST tail (13:0xZ-14:40Z), the section `/closer-drive` requires

- **Grade 12:** r12 at 8075f97ffb, PASS on the APPLIED plane (the bronze grant by simulate, with a negative control).
- **Grade 13:** 1002f, PASS (PFOE's 26 source cells).
- **FAST ended 14:40:14Z on Andrew's word.**
- **Grade 14** (FULL mode, the RFW-D01 refresh): PASS.
- Full text: `deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md`.

## 5. What you should have asked but did not

**"Which invocation is the schedule?"** Every proof of the AI stage so far, the seat run, the re-grade and the 09-30 fire, was
a deliberate act. The order's J1 named "the first scheduled account", but the evidence offered for it was an `only` event whose
manifest says "scheduled". The tell was in the sweep, in two lines that decide whether publish runs at all.

The general question for round 7's L5: for every "production" outcome, which organic trigger fires it on a normal day? Prove it
by the trigger itself (the next 09:00 ET sweep with no seat act), with the deliberate fire kept as the positive control, not as
the evidence.

-- 3.0.0_SA_CVO~RV
