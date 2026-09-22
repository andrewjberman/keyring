# AMGT_RESAPP round 28 (Lenovo trial, wave 0): CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T15:5xZ at HEAD after `0972b8631c`, LOCAL on SITEZ.
**Inputs:**
- The COO's packet `ledger/ROUND28_L8_PACKET_20260922.md` @`0972b8631c`, and the six orders.
- The five worker rows.
- This seat's own instruments, all local: in-process probes of `detect_language`, `_first_differing_outcome_field`
  and the SA name read, and a read of the December-arm strip in `test_stage_derive_fye.py`.

## Round state

**6 of 6 terminal:**

| order | criteria | drained @ |
|---|---|---|
| rk-107, Latin detection plus C-S386 | 5 | `e2ca56b2df` |
| rk-108, identity fields | 4 | `6acadc3dd2` |
| rk-109, fye_join | 4 | `1f70c73923` |
| rk-110, Lusha verified domain | 4 | `1c8140c9d8` |
| rk-111, SA companyName | 4 | `6fb44237b6` |
| rk-112, currency labels | 4 | `ccfa29862d` |

The sweep reads PASS 25 / FAIL 0 / UNVERIFIABLE 0 of 25 over 6 orders. The order files carry 5+4+4+4+4+4 = 25
criterion ids, and **0 of 25 are judgment criteria**.

**The mid-flight amendment followed the process note of round 27:** rk-112's ISSUER AMENDMENT 1 is @`4f234eb208`,
authored by `2.0.0_SA_COO~Z` and committed before the rebuild.

## Three graduated rows now read remedied, on this seat's own instruments

- **Z-S221, Latin languages.** In-process `detect_language`:

  | input | result |
  |---|---|
  | German | `de` |
  | French | `fr` |
  | Italian | `it` |
  | English control | `en` |

  A two-word German fragment ("Die Gesellschaft") still reads `en`. That is below any useful sample size, and filing
  excerpts are long, so it is noted, not faulted. **Remedied.** It was the precondition for any non-US filing
  analysis (C-S388), and that precondition is now met.
- **C-S386, the CHANGED-HELD length text.** One attempt against two now prints `battery.attempts length: 1 -> 2`; it
  was `14 -> 21`. **Remedied.**
- **Z-S219, SA identity.** `sa_forecast_fallback.py:240` now reads
  `sa_attrs.get("companyName") or sa_attrs.get("name")`, and records which field it used. **Remedied.**

Their remediation rows read REMEDIATED at the true L10 close.

## W112-S4, the ruling asked of this seat: WITHIN INTENT

On the December fixture, the walled byte-identity arm strips from `unresolved` the one entry for mnemonic
`EQY_FUND_CRNCY`. That is one item beyond the amendment's literal three-item list. Read at
`test_stage_derive_fye.py:236-266`:
- the strip is confined to that one mnemonic;
- it removes an entry the pinned module could never have produced, because rk-112 appends `EQY_FUND_CRNCY` to
  `HEADER_FIELDS` itself;
- every other `unresolved` entry, and every figure, is still compared byte for byte.

The walled property ("a December name derives exactly as before, apart from this cell's additive currency labelling")
is therefore still what the test proves. **Ruled within intent.**

**One asymmetry, for the next code cell (not a fault):** the comment at `:240` says the strip first ASSERTS the
stripped keys were present, "so the strip can never hide an absence". The currency-key strip does assert that
(`:244-245`). The new `unresolved` strip does not. Add
`assert sum(u.get("mnemonic") == "EQY_FUND_CRNCY" for u in unresolved) == 1` so both strips carry the same guard.

## Row dispositions

- **W112-S1 (ARMED):** the ruled currency keys broke rk-109's walled test as the order stood. ISSUER AMENDMENT 1
  resolves it, and the rebuilt arms all PASS. Disarmed by amendment: DISMISSED_WITH_REASON, following the disarm
  contract (a pure disarm is never GRADUATED).
- **W112-S2:** AC3's premise undercounted the base (11 unrelated files differ at `1f70c73923`). An issuer-text defect,
  fixed by the same amendment. DISMISSED.
- **W112-S3:** the record of the amendment itself. DISMISSED.
- **W112-S4:** ruled above. DISMISSED.
- **W109-S1:** AC0's literal sed could not be re-run before the edit, so it was reconstructed from the pin. INERT: the
  pin is immutable and the baseline is the same object. DISMISSED.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S389",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T15:55Z",
    "one_line": "L9 GRADE RECORD for round 28 (Lenovo wave 0): 6 of 6 terminal, sweep 25/0/0, judgment 0; Z-S221, C-S386 and Z-S219 read remedied on this seat's own probes; W112-S4 ruled within intent; the amendment is issuer-committed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 28: PASS 25 / FAIL 0 / UNVERIFIABLE 0 of 25 over 6 orders; criterion ids 5+4+4+4+4+4, judgment=\"true\" in 0.",
        "git log 4f234eb208: author 2.0.0_SA_COO~Z, 'ISSUER AMENDMENT 1, committed by the issuer before the rebuild'.",
        "In-process detect_language: German -> de, French -> fr, Italian -> it, English -> en; 'Die Gesellschaft' -> en (two words).",
        "In-process _first_differing_outcome_field: 1 vs 2 attempts -> 'battery.attempts length: 1 -> 2'.",
        "sa_forecast_fallback.py:240: sa_name = sa_attrs.get('companyName') or sa_attrs.get('name') or ''.",
        "test_stage_derive_fye.py:236-266: currency keys asserted present then stripped; the EQY_FUND_CRNCY unresolved strip is confined to that mnemonic and carries no presence assert."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "All six cells meet their orders; three graduated defects are remedied; the walled property holds.",
    "notes": "Grade carrier. Z-S221, C-S386 and Z-S219 remediation rows read REMEDIATED at L10. Next code cell: add a presence assert to the EQY_FUND_CRNCY unresolved strip.",
    "dismissal_reason": "Grade record: this row carries the round-28 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S390",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T15:55Z",
    "one_line": "DISMISSED: W112-S1 (ARMED, disarmed by ISSUER AMENDMENT 1 @4f234eb208), W112-S2 (AC3 base undercount, issuer text), W112-S3 (the amendment's record), W112-S4 (ruled within intent), W109-S1 (baseline reconstructed from the immutable pin).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W112-S3 and the packet s.2: the amendment put test_stage_derive_fye.py into <paths> and re-based the December arm; AC0-AC3 PASS on the rebuild; the sweep reads 25/0/0.",
        "W112-S4 read at test_stage_derive_fye.py:236-266 by this seat: the strip is confined to mnemonic EQY_FUND_CRNCY.",
        "W109-S1: the reconstruction reads from the immutable pin, the same object the literal command would have printed."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each order's criteria as issued, then as amended by the issuer.",
    "world_is": "The one armed conflict was an issuer-text defect removed by an issuer-authored amendment before the rebuild; the rest are disclosures.",
    "notes": "Issuer-text defects of 2.0.0_SA_COO~Z's, not the workers'.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W112-S1",
      "AMGT_RESAPP-Z-W112-S2",
      "AMGT_RESAPP-Z-W112-S3",
      "AMGT_RESAPP-Z-W112-S4",
      "AMGT_RESAPP-Z-W109-S1"
    ],
    "dismissal_reason": "A pure disarm is DISMISSED, never GRADUATED; the other four are disclosures or issuer-text defects already corrected in the rebuilt, passing orders."
  }
]
```
