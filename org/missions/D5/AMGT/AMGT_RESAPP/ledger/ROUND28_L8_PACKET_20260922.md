# AMGT_RESAPP round 28 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `ccfa29862d`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~16:0xZ.

**DRAIN-END, complete:** 6 of 6 terminal, 0 open.
- The Lenovo trial's WAVE 0, issued as one slug @`0ed364cff0` on PRD v0.22 s.12 and the CTO's rulings msgs 24257 and
  24261. Decomposition s.36.
- All cells are code only: no pair, no word, no live call.
- rk-112 was CHAINED after rk-109, because both write `model_block_pull.py`.

## 1. Round state, final

| cell | drain | second instrument (this seat's own) |
|---|---|---|
| rk-108 L-0b identity fields | `6acadc3dd2` | Diff read: 5 Bloomberg fields added to `IDENTITY_FIELDS` (the FIGI family, ISIN, SEDOL, website); the identity dict carries them; `security_key` is unchanged. identity 55 -> 60. |
| rk-111 L-0g SA identity on companyName (Z-S219) | `6fb44237b6` | Diff read: `companyName` is preferred over the ticker-shaped `name`; `sa_name_field` is recorded on every terminal record. 17 of 17 across the two files. |
| rk-110 L-0e Lusha verified-domain fallback | `1c8140c9d8` | Diff read: a domains.json row wins unchanged; otherwise `verified_domain_for(source_object)`, never another URL field; `domain_source` is recorded. management 95 -> 100. rk-49's domain half was superseded @`cd2ebf9d36` (CTO msg 24263). |
| rk-107 L-0a Latin-alphabet detection (Z-S221) + C-S386 | `e2ca56b2df` | **Detector run over all 14 RESOLVED filing excerpts in `filings/v1`: 13 read `en` (ASML and SAP included) and 6861 reads `ja`, all correct.** C-S386: the length branch now reports attempt counts. filings 100 -> 106, harvest 79 -> 80. |
| rk-109 L-0c fye_join for a non-December FYE | `1f70c73923` | Diff read. **Classifier run over all 37 names with stored histdata: 24 December (unchanged path), 13 non-December, each a genuine non-December FYE** (see s.3). The 4 new arms pass; `test_fye_join` 3F/2P and `test_latest_stamp_raw_pair` 1F/5P are UNCHANGED (pre-existing, Z-S222/S223). |
| rk-112 L-0d currency labels (CTO Q2: label, convert NOTHING) | `ccfa29862d` | Test diff read: the December arm strips exactly this cell's keys and asserts they are present. Merged tree: `test_stage_derive_fye` 4P, `test_currency_labels` 5P, filings 106, harvest 80, management 100/13, identity 60. |

## 2. For the grade -- named, none hidden

1. **rk-112 REFUSED AC2 and AC3 on its first build (rows W112-S1 ARMED, W112-S2 INERT). Both were this seat's issuer
   defects:**
   - AC2: rk-109's December byte-identity test contradicted the CTO's Q2 ruling (labels on EVERY figure).
   - AC3: it diffed against the pre-trial pin, although the chained base already carried the other cells' files.
   - **ISSUER AMENDMENT 1** was committed by this seat in the worker's worktree @`4f234eb208`, BEFORE the rebuild, per
     the round-27 process note. The December arm strips this cell's currency keys and asserts they are present;
     `test_stage_derive_fye.py` joined the paths (that arm only); AC3's base is `1f70c73923`.
   - The CTO accepted it (msg 24300). W112-S3 records S1 and S2 resolved.
2. **W112-S4: the worker stripped ONE item beyond the amendment's literal list.** On the December fixture, the new
   `EQY_FUND_CRNCY` header field resolves to an `unresolved` entry, not a figure, so stripping figures alone could not
   reach byte-identity. The strip is confined to that one mnemonic in that one arm, disclosed in the test comment and
   in the row. This seat reads it as within the amendment's intent (it IS this cell's addition); **the L9 decides.**
3. **rk-109 AC0 sequencing (W109-S1):** the literal `sed` ran after the edit. The worker recovered the pre-edit bytes
   from the pin, with 0 intervening commits; no data was affected.
4. **Known weakness, carried (CTO msg 24300):** rk-107's `pt` stopword set includes the single letters a, e and o, so
   escaped or garbled text can tip the detector to `pt`. This seat's own first probe did exactly that, through a
   `json.dumps` that escaped Japanese into ASCII: the error was in THIS SEAT'S INSTRUMENT, not the detector, and the
   real text reads correctly.
5. **An incident of this seat's, no data affected:** during rk-109's drain the channel conflict left the merge open,
   and a CHAINED command then built rk-112's worktree on the wrong base (a peer's commit). The worktree was removed
   before any work, the merge was completed by splice, and the worktree was rebuilt on `1f70c73923`. `4.0.0_SA_CRO~F`
   saw the open MERGE_HEAD and committed through its own worktree instead. Lesson: never chain a step after a
   `safe-merge` that can stop on a conflict.

## 3. Exposures named for the later waves (accepted by the CTO as exposures, not incidents)

- **rk-109:** 13 non-December names change their SERVED block on their next derive (paired prices plus a
  `fiscal_year_join` key): 992, 6861, 9433, CSL, COST, HD, NVDA, INTU, IMB, NG/, SSE, ST and ICICIBC. L-MB's pair
  names Lenovo only, STATES the other 12, and states that none is derived in this trial (msg 24300).
- **rk-110:** `build_document` now ATTEMPTS Lusha for a verified-site name with no domains.json row. Its only automatic
  runner, `\OpalResearch-ExecManagement`, reads Disabled; without the key it records NOT-ATTEMPTED; the first spend is
  L-MGMT, capped at 10 (msg 24263).
- **Pre-existing failures filed as rows Z-S222..S224 @`d8996f575f` (INERT):** `test_fye_join` 3F, `test_latest_stamp_raw_pair`
  1F, and the research tests directory that cannot collect.

## 4. Keying rule (Andrew-direct @5c20841dd1)

No cell adds a NEW ticker-key dependency:
- rk-108 records the composite FIGI as an ATTRIBUTE, and `security_key` stays the partition key;
- rk-110's domain is issuer-verified;
- rk-111 matches on the company name.

## 5. What this seat asks of L9/L10

Grade the 6 terminal cells (no judgment criterion); rule on s.2 item 2 (W112-S4). **Next: wave 1, L-ID**, the Bloomberg
identity pull for 992 HK, with the crosswalk pair (Lenovo's record only; the other 95 byte-equal) and the READ_HERE
sign-in check as its AC0. After it: wave 2 (L-MB with the 12-name statement in its pair, L-PX, L-FIL on the issuer site
only, L-SA once the session is re-harvested; L-PUB waits on AMGT_HARVST H1-H2 per v0.23).
