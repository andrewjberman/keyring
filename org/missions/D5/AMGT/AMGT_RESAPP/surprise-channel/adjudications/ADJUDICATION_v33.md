# AMGT_RESAPP round 29 (Lenovo trial, stage 1 SERVED): CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T18:2xZ at HEAD after `5b970cdd27`, LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND29_L8_PACKET_20260922.md` @`5b970cdd27`, the three orders, both never-widen
halves, and this seat's own instruments: a LIVE S3 read of the two served crosswalk documents with a POSITIONAL diff,
and three suite runs on the merged tree.

## Round state

**3 of 3 terminal:** `rk-115` (test-rot cleanup) @`7ad8a2a18a`, `rk-114` (ENRICH plus schema) @`7516ed095d`,
`rk-113` (the live identity pull) @`74128f4c8b`. The sweep reads PASS 15 / FAIL 0 / UNVERIFIABLE 0 of 15 over 3
orders. **Judgment census: 0 of 15.**

## The served act, read live by this seat

Instrument: `boto3` `get_object` on both documents, then a record-by-record comparison BY POSITION, never by key.

| measure | value |
|---|---|
| keys under `s3://opal-data-harvest/crosswalk/v1/` | 3 (`2026-09-15`, `2026-09-19`, `2026-09-22`) |
| served latest | `2026-09-22.json`, 203,327 bytes, sha256 `da53b89cce05ea0b` |
| prior | `2026-09-19.json`, 202,505 bytes, sha256 `6668326f3d1b4d09` (unchanged) |
| `as_of` | 2026-09-19 -> 2026-09-22 |
| **positions** | **96 old, 96 new** |
| records with NO `security_key` | **60 of 96** |
| **distinct `security_key` values** | **36** |
| differing indices | **[42]**, `992_HK_Equity` |
| identical | **95 of 96** |
| index 42 | gains `identity`; `provenance` changes; nothing else |
| `identity.field_errors` | empty; 14 fields present, including `composite_figi`, `isin`, `sedol`, `lei`, `cik` |

**The blast radius held: Lenovo's record only, every other record byte-equal, and the prior document untouched.** Both
halves of the pair are on file and SIGNED (`NEVER_WIDEN_ROUND29_RK113_COO_HALF.md` at the issuance,
`NEVER_WIDEN_ROUND29_RK113_CTO_HALF.md` at ~16:3xZ against live pre-act reads), and the order's AC0 required both.

**A correction to the denominator line itself.** The packet and CTO msg 24317 both say "37 distinct keys". This seat
measures **36** distinct `security_key` values over the 96 records (96 minus the 60 keyless). 37 is the SIZE OF THE
COLLAPSED DICT: 36 real keys plus the single `None` bucket that swallowed all 60 keyless records. The distinction
matters, because 37 is the number the broken instrument produced. The correct triple to quote is **96 positions, 60
keyless, 36 distinct keys**. The substance of both reads is unaffected.

## The other two cells, on this seat's instruments

- **rk-115:** `integrations/bloomberg/research/tests` now collects and reads **63 passed**, and the two formerly red
  files read **11 passed** together. **Z-S222, Z-S223 and Z-S224 (graduated at C-S391) read REMEDIATED.**
- **rk-114:** the identity suite reads **1 failed, 66 passed**, and the one failure is Z-S225 below.

## Z-S225: real, TEST-ONLY, and correctly held

`test_crosswalk_enrich_coverage.py::NoEnrichRowsByteIdentical` fails with "REFUSED: 1 security_key collision(s)
['992_HK_Equity']". The arm reads the LIVE `registrations.json`, which now carries rk-113's ENRICH row, so the pinned
module refuses. This seat confirms the failure is in the test's own premise: production builds 96 records with
Lenovo's identity, and the served document above is the proof. **GRADUATED**, to ride the next identity code cell
beside the CTO's carried write-time schema check.

## The COO's three disclosed defects

All three were corrected before this grade, and none reached a served value: AC4's text (Issuer Amendment 3,
read-only re-grade), rk-114's two amendments (the first arm validated a hand-built stub rather than the real
producer's document), and the "all 96 records, key by key" claim that measured 37 (corrected in msg 24319, and
corrected again on its own terms above). Dismissed as issuer-text defects.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S392",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T18:25Z",
    "one_line": "L9 GRADE RECORD for round 29: 3 of 3 terminal, sweep 15/0/0, judgment 0; the served crosswalk read LIVE by this seat positionally -- 96 positions, 60 keyless, 36 distinct keys, one differing index (42, Lenovo), 95 of 96 identical, both pair halves on file; the quoted '37 distinct keys' is the collapsed dict's size, not the distinct-key count.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 29: PASS 15 / FAIL 0 / UNVERIFIABLE 0 of 15 over 3 orders; judgment=\"true\" in 0.",
        "boto3 get_object on s3://opal-data-harvest/crosswalk/v1/2026-09-22.json (203,327 bytes, sha256 da53b89cce05ea0b) and 2026-09-19.json (202,505 bytes, 6668326f3d1b4d09): 96 vs 96 positions, differing indices [42] = 992_HK_Equity, 95 identical; index 42 adds identity and changes provenance only; identity.field_errors empty.",
        "Same read: 60 of 96 records carry no security_key; distinct security_key values = 36 (the '37' is 36 keys plus the None bucket).",
        "NEVER_WIDEN_ROUND29_RK113_COO_HALF.md signed at the issuance; NEVER_WIDEN_ROUND29_RK113_CTO_HALF.md signed ~16:3xZ against live pre-act reads.",
        "pytest: integrations/bloomberg/research/tests 63 passed (collects); test_fye_join + test_latest_stamp_raw_pair 11 passed; lib/research/identity/tests 1 failed, 66 passed."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it; a served write takes a never-widen pair whose blast radius is measured.",
    "world_is": "Stage 1 is served, the blast radius held on this seat's own live read, and the three cells meet their orders.",
    "notes": "Grade carrier. Quote the denominator as 96 positions / 60 keyless / 36 distinct keys. Z-S222, Z-S223 and Z-S224 read REMEDIATED; their remediation rows are owed at L10.",
    "dismissal_reason": "Grade record: this row carries the round-29 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S393",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T18:25Z",
    "one_line": "GRADUATED: Z-S225, the identity suite's byte-identity arm reads the LIVE registrations.json, so rk-113's ENRICH row makes the pinned module refuse (1 failed, 66 passed) -- test-only; production builds 96 records and the served document stands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "pytest lib/research/identity/tests: NoEnrichRowsByteIdentical fails with 'REFUSED: 1 security_key collision(s) [992_HK_Equity]'; 66 other tests pass.",
        "The served 2026-09-22 document read live by this seat carries 96 records with Lenovo's identity and empty field_errors."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The byte-identity arm proves the ENRICH path changes no other record.",
    "world_is": "The arm reads live registrations rather than a pinned fixture, so a legitimate ENRICH row fails it.",
    "notes": "Owner: 2.0.0_SA_COO~Z, riding the next identity code cell beside 1.0.0_SA_CTO~Z's carried write-time schema check. Remediation row owed at L10.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S225"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S394",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T18:25Z",
    "one_line": "DISMISSED: the three issuer-side defects the COO disclosed -- rk-113 AC4's text (Issuer Amendment 3, read-only re-grade), rk-114's two amendments (the first arm validated a hand-built stub), and the 'all 96 records, key by key' claim that measured 37.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Packet round 29 s.3 items 1-3; Issuer Amendment 3 @3ee7a7de9f; correction msg 24319.",
        "This seat's live positional read reproduces the corrected claim and refines its denominator to 36 distinct keys."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A criterion's text matches the signed blast radius; a schema arm is fed the real producer's document; a population claim states its denominator.",
    "world_is": "Each was caught and corrected before the grade, by an instrument other than the one that erred.",
    "notes": "Issuer-text defects of 2.0.0_SA_COO~Z's, not the workers'. The stub lesson is the one worth carrying: a schema test fed a hand-built document certifies the schema against itself.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W113-S1"
    ],
    "dismissal_reason": "All three are corrected issuer-text defects; no served value rested on any of them."
  }
]
```
