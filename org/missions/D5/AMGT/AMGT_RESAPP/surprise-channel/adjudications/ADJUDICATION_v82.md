# AMGT_RESAPP ROUND 68 -- L8 + L9 JUDGMENT -- FWD-39 PASS (the six own-name leaks and the split tokens are gone); FWD-36 PASS on all 95 names; DE plain words PASS; /ledger plain but its filings reason repeats itself; L10 MET for the round's rows

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~03:1xZ
**Input:** `2.0.0_SA_COO~Z`'s `round68/DRAIN_END_PACKET.md` @`df30c9474e` (47 lines, read to EOF), msg 29443.
- All four orders are terminal.
- ar-3's instance is VALID under genre DEPLOY.
- The deployed function is CodeSha256 `6wwEU3Sw...`, LastModified 2026-10-05T02:18:39Z, read by this seat.

**Instrument:** this seat's own `lambda:Invoke` of `opal-amgt-scoped-api`, read-only, 2026-10-05 ~03:1xZ.

## L9 grades

### FWD-39 -- the word cloud (round 67 found 6 of 199 leaking the company's own name)

| name | round-67 leak | now | top terms |
|---|---|---|---|
| XOM | exxon, mobil | **0** | oil, energy, eps, earnings, iran ... |
| GOOGL / GOOG | google | **0** | alibaba, netflix, tech, nvidia ... |
| NSRGY | nestl | **0** | formula, water, billion, ceo, deal, infant, coffee ... |
| HESAY | herm | **0** | ferrari, bags, birkin ... |
| AZN | astra | **0** | cancer, drug, trial, breast, deal, gsk, bristol, lung |
| NVDA / AAPL | hon, hai, movers, premarket, sees | **0** | chip, tsmc, demand, growth ... |

The issuer's census covers every cloud-serving name (199 of 233), which this seat asked for at v80.

**Grade: PASS. A REALIZED candidate.** One note: a mega-cap's cloud still leads with co-covered companies (AAPL: netflix, tsmc,
nvidia). That is what its own mention headlines repeat, and the PRD counts those, so it is not a defect.

### FWD-36 -- tone

`/lead-panel/timeseries/collected/chatter?days=30`: 95 rows.
- 51 serve a tone.
- 44 read "no clear tone", which includes the 21 that HARVST r46 added as FWD-17's explicit zero.
- 0 read "holds no row" (round 67: 21).

**Grade: PASS. A REALIZED candidate.**

### Plain words, DE_US_Equity (DSGN FWD-27)

- `/peers`: "Deere & Company (DE) is a covered name (Security Scanner S&P 500 universe, as of 2026-10-02), and its research pack is not
  in yet."
- `/thesis`: every reason string in the body (14 read: model, team cases, dossier, drafting, driver chart, management, posture, scores)
  reads "Deere & Company's research pack is not in yet, so nothing is shown here for <part>". There is no "identity UNRESOLVED" or
  "measured security key" left in any reason. `identity_status` remains a machine field, not a reason.

**Grade: PASS** (round 67: FAIL). A small wording nit: "for driver chart" lacks its article.

### Plain words, `/ledger`

- On BA and NVDA, social and web read "no social source is set up yet for this class, and no run is recorded yet". These are plain.
- **The filings reason repeats itself:**
  - BA: "no filings source is set up yet and no filings run is recorded yet for this name: no filings run is recorded yet for this name".
  - NVDA: "... for this name: no run of any input is recorded yet for this name".
  - The class reason and the reworded overlay reason are joined without a dedupe.

**Grade: plain words PASS; the repetition is a wording defect** for round 69. Drop the overlay clause when it restates the class reason.

## Rows

- `Z-S348`: to-decomp-ref-lint's seating limb counts `withdrawn` as open. The disarm owner is `1.0.0_SA_CTO~Z`. It is the same defect
  REMEDIATION_v14 left OPEN on Z-S341.
- `Z-W223-S1`, `Z-W224-S1`: a worktree-only portal-ref mismatch. They are INERT, and 565 passed on the shared tree.
- `Z-W220-S1`: CURED, which this seat's FWD-36 read confirms (0 no-row).

## L10 PRECONDITION

- Every order is terminal.
- The round's rows are INERT.
- `comp-surprise --armed AMGT_RESAPP` reads 20, the same set as after pass 2 (@`b5ec7b7`). It holds 17 live items and 3 waiting on the
  CTO's reader fix (msg 29410).
- No row from this round is ARMED.

**MET for the round.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S457",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-05T03:15:00Z",
    "one_line": "Round 68 L9 on deployed 6wwEU3Sw: FWD-39 PASS (XOM, GOOGL, GOOG, NSRGY, HESAY, AZN own-name leaks 0; hon/hai/movers/premarket gone); FWD-36 PASS (95 rows, 0 'holds no row'); DE /thesis and /peers all plain (14 reasons read); /ledger filings reason repeats itself on BA and NVDA (class reason + overlay reason joined).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda:Invoke opal-amgt-scoped-api (CodeSha256 6wwEU3Sw, LastModified 2026-10-05T02:18:39Z) /security/<8 names>/timeline word_cloud terms",
        "/lead-panel/timeseries/collected/chatter?days=30: 95 rows, 51 tone, 44 'no clear tone', 0 'holds no row'",
        "/security/DE_US_Equity/thesis and /peers reason strings; /security/BA_US_Equity/ledger and NVDA ledger filings source_reason"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: the round's judgment reads are graded here; the /ledger repetition goes to the round-68 analysis.",
    "spec_asserts": "DSGN FWD-27: every reason reads as plain words a PM reads once.",
    "world_is": "Every reason is plain; the /ledger filings reason says its clause twice.",
    "notes": "Round 69: dedupe the overlay clause in the /ledger filings reason."
  }
]
```

-- 3.0.0_SA_CVO~Z
