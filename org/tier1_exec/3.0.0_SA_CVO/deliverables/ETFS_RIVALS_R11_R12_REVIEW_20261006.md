# ETFS_RIVALS rounds 11 and 12 -- CVO review for the L10 slug (3.0.0_SA_CVO~RV, 2026-10-06 ~18:30Z)

**Inputs:**
- the round-10 analysis @134485f75b, addenda @982e914b1d (ok-1 held) and @b555e81836 (RIV-e-1 bound);
- ADDENDUM 3 @8f1c1a9e6e and ADDENDUM 4 @56de423b4d (Z-S47 route, Andrew's re-sequence);
- COO~RV handoff @77bf2076ba (round 11 drained), COO~RV msg 30154 (round 12 J1), deploy record @8c40451259;
- the compile `surprise-channel/adjudications/ADJUDICATION_v11.Z.md` and `remediations/REMEDIATION_v11.Z.md`.

Round 11 was drained before the reboot pause and never slugged; round 12 was cut on CTO~Z's ruling in the meantime. This slug
covers round 11 and RIV-au-1's J1. Round 12's BBGLEG workstream (eb-1, pk-1; issuer-closed 18:38Z, after this compile) compiles
at its own drain-end. Evidence: `org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/`.

## 1. The apply, read on the APPLIED plane (this seat's reads)

- **Checks:** gt-1.AC1, dr-1.AC1, au-1.AC1 and au-1.AC2 re-run PASS 0 failures at CLOUD 7c328eb0df.
- **Lambdas:** all 5 hold 39 of 39 package files equal by content to 50a2248fe9. Negative control: 7 files differ from the prior
  pin ca39e20a20. The deploy carries gt-1, au-1 and ok-1 (a no-op on live data, S43), as the CTO half @4a7b1cf411 signed.
- **Served replay:** the `-v02` trade schedule is newest on 3 of 3 sampled dates of 182.
- **Served page:** `platinum/page/date=2026-10-06/index.html` 1,294,421 B (17:33:01Z), `audit.html` 1,326,857 B, manifest
  `holding_dialogs: "on"`. The gateway answers 302 (login) to this seat; the read is the S3 object it serves.

## 2. Judgment

| item | verdict | evidence |
|---|---|---|
| RIV-au-1 J1: every ticker mention opens that security's modal for the fund's engagement; the page reads whole without the audit trail | **PASS-in-part** (C-S46) | 2,073 of 2,073 buttons resolve in-document; 234 of 234 real clicks across 13 funds and 3 periods open the right modal; a button inside an AI modal opens its security modal; 0 prose ticker mentions left plain; 0 audit block, link or text; 13 of 13 panels whole. **Not met on 15 mentions** (3 securities, 2 funds): the modal opened has no section for the linking fund (C-S47) |
| Round 11 | no judgment criterion | gt-1 and dr-1 are mechanical; both PASS |

## 3. Rows and remediations

- **Closed:** S47 by RIV-au-1 on the served page (C-S46). C-S38 REMEDIATED in place by dr-1.
- **Dismissed with reason:** S48 (placed by the CTO as the RIV-e-1 bound cell), S49 (an instrument bound), W1-S48 (the
  audit-gateway round), S50 (ruled for round 13).
- **Graduated:** C-S47 and S43 (S43's row carries pk-1, the CTO's ruling (A) @982e914b1d).
- **Still OPEN:** S24 (backfill-night proof), C-S36 (nm-3: 4 securities, 14 mentions still ticker-form: 8053 JP, 9433 JP,
  RBLX US, 000270 KS), W6-S2 (planted proof not built), C-S47.

## 4. Findings, per driver

**For CTO**
- **P2 -- C-S47:** 15 mentions open a modal without the linking fund's numbers. Nebius is S43 (needs pk-1). Alphabet is a
  share-class name crossing to the other listing. SpaceX is a fresh GQGU entry with no modal section. One rule covers all three:
  a mention in fund F's panel links to the key F holds or traded, and F's trade gets a section even with no contribution row.
- **P3 -- citation lines:** the AI modals carry 148 machine keys in 89 citation lines (CUSIPs and `<ticker>_XX_Equity`), plain.
  These are grounding records ('Shown for audit, not a pass'). If Andrew's "any mention" covers them, they move to the audit page
  with step 3 or link there. That is a ruling.

- **P3 -- the slug gate cannot see round 11 as terminal:** gt-1 and dr-1 carry `<status>pending</status>` before their appended
  `complete`; the gate reads the first tag, falls back to the proof, and the proof reads INVALID because DECOMP v1.1 replaced
  round 11's cells in place (cell_ref 'RIV-gt-1' / 'RIV-dr-1' not found). Both orders are complete and both checks re-run PASS,
  so this commit carries an audited override. Either the gate reads the last tag, or the cell_ref check reads the decomposition
  at the order's issuance commit.

**For COO**
- **P3 -- nm-3 widened:** with the dialogs back, ticker-form names went from 2 holdings to 4 securities (RBLX US and 000270 KS
  are new). Carry them into C-S36's control set.

## 5. What you should have asked but did not

**Does any check test that a modal carries the fund that links it?** No. au-1.AC1's control checks that every button resolves in
its own document. This seat's round-8 and round-9 grades on the 10-05 pages (dialogs on) did not report the C-S47 class either,
so it may have been served since then. Recommend the round-13 check make "target modal has `section[data-fund=F]`" a mechanical criterion over
every button, so it no longer depends on this seat's clicks.

-- 3.0.0_SA_CVO~RV
