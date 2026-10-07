# ETFS_RIVALS -- rounds 11 and 12 L8/L9 adjudication (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-06 ~18:30Z. Inputs:
- COO~RV handoff `org/tier1_exec/2.0.0_SA_COO~RV/handoffs/2026-10-06_1351Z.md` @77bf2076ba (round 11 drained 2/2);
- COO~RV msg 30154 (round 12 J1, seated on CTO~Z ruling msg 30153);
- the round-12 deploy record @8c40451259 and the browser record @6c489cc6de.

Round 11 is drained: RIV-gt-1 (merged 8fa75c6023) and RIV-dr-1 (merged b2b6876a19), both `complete`. Round 12 is graded for
RIV-au-1 only (closed ed529d33c9, deployed 8c40451259), the J1 the round-13 cut waits on. Round 12's BBGLEG workstream (RIV-eb-1,
RIV-pk-1; issued ce6c8e89ee 17:57Z, issuer-closed 0def541c91 18:38Z) and its rows (Z-S51, Z-W2-S14) are NOT compiled here; they
compile at BBGLEG's drain-end.

**The apply, this seat's reads:**
- The four mechanical checks re-run PASS 0 failures at CLOUD 7c328eb0df: gt-1.AC1, dr-1.AC1, au-1.AC1, au-1.AC2.
- All 5 rivalfunds Lambdas hold 39 of 39 package files equal by content to 50a2248fe9 (`lamcmp.py`). Negative control: 7 files
  differ from the prior pin ca39e20a20, so the read discriminates. This deploy ships gt-1, au-1 and ok-1; ok-1 is a no-op on
  live data (S43) and rides inside the CTO half @4a7b1cf411.
- The served replay (round-11 item 2): on 3 sampled dates of the 182 planned (2026-01-02, 2026-05-19, 2026-09-29), the newest
  `gold/trade_schedule` object is the `-v02` written 02:17-02:18Z on 10-06.
- The served 10-06 page: `platinum/page/date=2026-10-06/index.html`, 1,294,421 B, LastModified 17:33:01Z, beside `audit.html`
  (1,326,857 B) and `manifest.json`. The gateway answers 302 (login) to this seat, so the read is the S3 object the gateway
  serves, as in rounds 8-10.

**Judgment (round 12; round 11 carries none):** RIV-au-1 J1 is **PASS-in-part** (C-S46). The cell's outcome is MET: dialogs are
on, every button resolves, the page reads whole without the audit trail. Of 2,073 mentions, 15 (3 securities, 2 funds) open
a modal that carries no section for the fund whose text links it (C-S47, graduated).

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S45",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T18:30:00Z",
    "one_line": "Round 11 L8/L9: gt-1.AC1 and dr-1.AC1 re-run PASS at CLOUD 7c328eb0df; gt-1 is applied (5 Lambdas 39/39 at 50a2248fe9, control differs in 7); the served replay's -v02 is newest on 3 of 3 sampled dates. S48 and S49 are dispositioned; S43 joins C-S47.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S48",
      "ETFS_RIVALS-Z-S49"
    ],
    "spec_asserts": "Round-10 analysis @134485f75b section 4: cells gt-1 and dr-1; issuer acts 2 (served replay), 3 (ok-1 deploy, held by ruling (A) @982e914b1d) and 5 (the 10-06 proofs, graded @70eded3bb3 as C-S44).",
    "world_is": "- gt-1.AC1: PASS 0 failures (a same-input pass at a new code version writes a new -v<NN> revision; control: an object without producer_version reads as a different version).\n- dr-1.AC1: PASS 0 failures (data-arrival class 9,467 rows carries no commit; the other six classes are unchanged). This is C-S38's remedy.\n- Apply: etfs-rivalfunds-daily, etfs-rivalfunds-fetch-holdings, rivalfunds-build-silver, rivalfunds-build-canonical-shape and rivalfunds-publish-page each 39/39 equal to 50a2248fe9; 7 files differ from ca39e20a20.\n- Served replay: trades-...-v02.parquet newest on 2026-01-02, 2026-05-19 and 2026-09-29 (02:17:02Z, 02:17:43Z, 02:18:25Z).\n- S48 (enrichment hangs on an unreachable DAPI): CTO~Z addendum @b555e81836 places it as the RIV-e-1 retry-bound cell; not yet cut.\n- S49 (the stage Lambdas emit no application log lines): a property of the instrument, not a defect in a served value. It bounds every 'logs are clean' claim about these 5 functions; the sound oracle is the S3 artifact.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's re-runs of round11/checks/gt-1.AC1.py, round11/checks/dr-1.AC1.py at 7c328eb0df",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/lamcmp.py (lambda get-function zips vs git show by content)",
        "s3api list-objects-v2 gold/trade_schedule for 3 of 182 planned dates",
        "investigation rows ETFS_RIVALS-Z-S48, S49"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. S48 is placed by the CTO (RIV-e-1 bound cell, @b555e81836) and needs no second carrier. S49 is an instrument bound, recorded here, with no remedy owed. C-S38 moves to REMEDIATED in place (REMEDIATION_v9) on dr-1. S24, C-S36 and W6-S2 stay OPEN."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S46",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T18:30:00Z",
    "one_line": "RIV-au-1 J1 PASS-in-part on the served 10-06 page: 2,073 of 2,073 security buttons resolve in-document to 424 modals; 234 of 234 real clicks (13 funds x 3 periods x 6 spread buttons) open the right modal; a button inside an AI modal opens its security modal; no audit block, link or text; 13 of 13 panels whole. Residual: 15 mentions open a modal without the linking fund's section (C-S47). S47 is closed by this cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S47",
      "ETFS_RIVALS-Z-W1-S48",
      "ETFS_RIVALS-Z-S50"
    ],
    "spec_asserts": "RIV-au-1 J1: every ticker mention on the main page opens that security's modal for the fund's engagement with it, and the page reads whole without the audit trail (Andrew-direct ~16:3xZ; ADDENDUM 4 steps 1-2).",
    "world_is": "Measured by this seat with Playwright (chromium, headless) on the S3 bytes, sha256 in served_index_sha256.txt:\n- Static: 2,073 data-sec buttons, 0 unresolved, 0 outside a fund panel; 424 security modals + 26 AI modals = 450 popover ids, 0 dangling targets.\n- Real clicks: 234 of 234 open (:popover-open) the target modal; its h3 names the clicked security. In 132 of 234 the clicking fund's section is the modal's first section; this grade does not count section order.\n- Plain ticker mentions: a census of visible text outside buttons against the page's own 415 ticker tokens finds 106 hits, 0 of them prose ticker mentions: 'AI' and 'MTD' (words and period codes), 'MSCI EAFE Dec26' (a futures contract), and 148 machine keys in 89 citation lines inside the AI modals ('trade_schedule GQGU|30233Q108|...'). 0 '<id> XX Equity' forms in visible prose.\n- Whole: 13 of 13 panels carry the head, both AI faces and the rankings card; 0 details#audit, 0 audit hrefs, 0 'audit trail'/'audit.html' text. Trades surface through 43 trend blocks and 252 'buying this year' modal sections; the KPI '221 trades inferred' stays without its log on the main page.\n- S50's 5 shared-name AI mentions stay plain, by the ln-1 rule, as the CTO ruled for round 13 @4a7b1cf411.\n- nm-3 residue (C-S36): 4 securities still named in ticker form, 14 button mentions: 8053 JP x9, 9433 JP x2, RBLX US x2, 000270 KS x1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/j1_result.json (j1grade.py)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/census2.json (census2.py)",
        "j1_first_click.png, j1_nested_click.png, j1_idvz_top.png",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-06/index.html 1,294,421 B 17:33:01Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. S47 is closed by RIV-au-1 on the served page (holding dialogs on, 33.6% headroom under DIALOG_SOFT_CAP). W1-S48 (audit.html has no gateway-cap refusal; the data-status section is reachable only from the unlinked audit page) belongs to the audit-gateway round, step 3 of Andrew's order. S50 is ruled by the CTO for round 13. The residual graduates as C-S47."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S47",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T18:30:00Z",
    "one_line": "15 of 2,073 security mentions on the served 10-06 page open a modal that has no section for the fund whose text links it, so the reader sees no number for that fund's engagement: WCMG 'Nebius Group Nv' x8 -> N97284108 (GQGU only; NBIS_US_Equity carries WCMG), WCMG 'Alphabet Inc-Cl C' x2 -> GOOG_US_Equity (PFOE, GQGU, BASG, PCLG; WCMG is in GOOGL_US_Equity), GQGU 'Space Exploration Technologies Corp' x5 -> SPCX_US_Equity (TSEL, BASG; GQGU's 10-05 entry of $12.1m is cited in its own AI text).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S43"
    ],
    "spec_asserts": "RIV-au-1 J1 and Andrew-direct ~16:3xZ: a ticker mention opens the modal for THAT fund's engagement with that security.",
    "world_is": "Three causes, one symptom:\n- Nebius: the name resolves to the CUSIP-keyed listing GQGU reports, not the Bloomberg key WCMG holds (S43; ok-1's join cannot meet them; the pk-1 draft adds PARSEKYABLE_DES).\n- Alphabet: WCMG's AI text names the Class C listing; WCMG's contribution sits on the Class A key. Either the account names the wrong share class or the name map resolves a shared company name to the other listing.\n- SpaceX: GQGU's trade_schedule row for SPCX_US_Equity dated 2026-10-05 exists (cited in the AI modal), but the modal carries no GQGU section: an entry with no contribution row yet gets no 'buying this year' section either.\nNone is caused by RIV-au-1; each was invisible while the dialogs were off.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/census2.json key 'nfs' (15 rows) and 'goog_keys'",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/j1_result.json b_clicks.fails (3 WCMG Nebius clicks, one per period)",
        "investigation row ETFS_RIVALS-Z-S43"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
