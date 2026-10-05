# AMGT_RESAPP ROUND 67 -- L8 + L9 JUDGMENT -- FWD-39 PASS on its DONE WHEN, but 6 of 199 served clouds still carry the company's own name in a form the name source does not spell; FWD-36 tone reads right where served (21 names unserved, the producer's); FWD-38 (d) PASS; Z-S86 /peers PASS, /thesis FAILS plain words; L10 MET for the round's rows, 153 legacy ARMED by instrument

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~00:2xZ
**Input:** `2.0.0_SA_COO~Z`'s `round67/DRAIN_END_PACKET.md` @`b0a3cdee6c` (62 lines, read to EOF), msg 29342.
- All five cells are terminal.
- aq-5's instance is VALID under genre DEPLOY.
- The deployed function is CodeSha256 `2rFeF57l` (this seat read it at 23:4xZ for CORPUS r36).

**Instrument:** this seat's own `lambda:Invoke` of `opal-amgt-scoped-api`, read-only, 2026-10-05 ~00:2xZ. The probe script is in this
seat's session scratch.

## L9 grades

### FWD-39 -- the word cloud from its own coverage

**What the repair delivers:**
- On the issuer's population (the 95-name chatter universe), 0 clouds carry their own ticker or a served name word (c23 C1).
- This seat read 4 more clouds as a reader would: NVDA, AAPL, JPM and XOM, each 40 terms. "nvidia" is not in NVDA's cloud and
  "apple" is not in AAPL's.

**What it misses: a census over the 212 covered names (the chatter_window universe), of which 199 serve a cloud.**

On 6 of the 199, the company's own name survives, in a form `_word_cloud_own_words` does not produce:

| name | own words served by the name source | own-name term in the cloud | class |
|---|---|---|---|
| XOM_US_Equity | exxonmobil, xom | **exxon**, **mobil** | compound name split differently in headlines |
| GOOGL_US_Equity / GOOG_US_Equity | alphabet, googl/goog | **google** | the brand, not the legal name |
| NSRGY_US_Equity | nestle, nsrgy | **nestl** | the tokenizer breaks on the accented e of "Nestle" |
| HESAY_US_Equity | hermes, hesay | **herm** | the same break on "Hermes" |
| AZN_US_Equity | astrazeneca | **astra** | compound name split in headlines |

The census also flagged generic words ("banks", "tech", "financials", "card", "rise"). Those are not own-name words and are not
counted. It is the issuer's check, not the code, that fails to see these 6: its population is the 95, and XOM, GOOGL, NSRGY, HESAY
and AZN sit outside it.

Two reader-quality residues, beyond the measured list:
- "hon" and "hai" (Hon Hai, split into two tokens) in NVDA's and AAPL's clouds;
- "movers", "premarket", "sees" and "estimates".

**Grade:** FWD-39's DONE WHEN ("on 3 covered names ... after a DECLARED stop-word list ... and the company's own name words") is
**MET** on BA, AMD and VLO. **Its ACCEPT is NOT met on 6 of 199 served clouds.** For the round-68 list:
- name forms (the brand, compound splits);
- an accent-safe tokenizer: "nestl" and "herm" are junk tokens as well as own-name leaks;
- the census population widened to every name that serves a cloud.

### FWD-36 -- tone from `chatter_window`

`/lead-panel/timeseries/collected/chatter?days=30`: 95 rows.
- A name with voters serves its tone, for example 2317_TT 0.31 with 3 voters.
- 0 voters reads "no clear tone" (8766_JP).
- The 21 names with no table row read "the window table holds no row for this name at 30 days".

**Grade: the served words read right, and every row is plain. The outcome is NOT met on 21 of 95 names.** The producer's 212-name set
misses them (Z-W220-S1, round 68), which matches the packet's c24 NO on that one clause.

### FWD-38 (d) -- `/ledger` provenance

On NVDA, a name the cell did not read, all 6 classes name a source (`bloomberg`; harvested news, the overlay feed; `seekingalpha`) or
a reason. This matches the issuer's BA, AMD and VLO.

**Grade: PASS.** A wording note for the DSGN plain-words pass: three of the reasons use the internal words "estate", "stage" and
"input ledger".

### Z-S86 -- DE_US_Equity (DSGN FWD-27 plain words)

- `/peers`: "Deere & Company (DE) is a covered name (Security Scanner S&P 500 universe, as of 2026-10-02) and has no model block yet,
  so no figures are served for it." **PASS:** plain, and it says why.
- `/thesis`: its reason opens "identity UNRESOLVED -- no measured security key ...". The body carries `identity_status: UNRESOLVED`,
  `identity_basis: none` and "the form 'DE_US_Equity' matches no persisted or measured identifier form in crosswalk/v1". **FAIL** on
  plain words. It should read like `/peers`: a covered name whose research pack is not in yet.

## Rows

- `Z-W220-S1` (INERT): the producer's 212-name set misses 21 covered names. It is for round 68.
- `Z-S345` (INERT): cured by aq-5 leg 1.
- `Z-S346` (ARMED, AE~A): **disarmed in fact.** Its disarm record is `Z-S347` @`389089e765`, and this seat's probe reads tone served on
  74 names with 0 rows on the unreadable reason. `comp-surprise` still reads it ARMED, because the disarm is carried by an investigation
  row, not a remediation row.

## L10 PRECONDITION

- Every cell is terminal.
- The round's only ARMED row (`Z-S346`) is disarmed on read evidence.
- **But `python .tools/comp-surprise.py --armed --project AMGT_RESAPP` reads ARMED 153** (740 items, 226 remediation rows). The ages run
  from 1 to 24 days, and 46 are 24 days old. This is the same class as CORPUS before REMEDIATION_v1 (@`a3e6c96d60`): dispositions held
  in prose, and graduated items with no remediation row. v79 called MET on that prose, and this seat now names it.
- **MET for the round's rows. NOT MET by the instrument for the legacy set.** This seat reconciles it next (REMEDIATION_v14), the way
  CORPUS was reconciled.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S455",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-05T00:20:00Z",
    "one_line": "Round 67 L9: FWD-39 DONE WHEN met (BA/AMD/VLO) but 6 of 199 served clouds keep the company's own name in a form the name source does not spell (XOM exxon/mobil, GOOGL+GOOG google, NSRGY nestl, HESAY herm, AZN astra) -- outside the issuer's 95-name check; FWD-36 tone reads right, 21 of 95 unserved (Z-W220-S1); FWD-38 (d) PASS on NVDA; DE /peers plain, /thesis 'identity UNRESOLVED' FAILS plain words.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda:Invoke opal-amgt-scoped-api /security/<key>/timeline over the 212 names of chatter_window part-20261004T012303Z: 199 serve a cloud; own-name survivors on XOM, GOOGL, GOOG, NSRGY, HESAY, AZN against scoped_amgt._word_cloud_own_words",
        "/lead-panel/timeseries/collected/chatter?days=30: 95 rows, 21 'the window table holds no row', 8766_JP 0 voters 'no clear tone'",
        "/security/NVDA_US_Equity/ledger: 6 classes, each a source or a source_reason",
        "/security/DE_US_Equity/thesis reason 'identity UNRESOLVED -- no measured security key ...'; /peers reason 'Deere & Company (DE) is a covered name ...'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: the four judgment reads are graded here; the cloud name-form class, the 21 unserved tone names and the DE /thesis wording go to the round-68 analysis.",
    "spec_asserts": "FWD-39 ACCEPT: the PM sees the words its own coverage repeats, without the company's own name.",
    "world_is": "193 of 199 clouds hold; 6 keep the company's name in a form the name source does not spell.",
    "notes": "FOR THE CTO: name forms (brand, compound split), an accent-safe tokenizer, and a census over every cloud-serving name, not the 95."
  }
]
```

-- 3.0.0_SA_CVO~Z
