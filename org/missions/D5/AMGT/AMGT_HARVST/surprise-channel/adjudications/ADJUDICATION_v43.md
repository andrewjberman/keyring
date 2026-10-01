# AMGT_HARVST ROUND 33 -- L8 COMPILE (all criteria mechanical; two served gold rebuilds)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~13:3xZ
**Input:** `2.0.0_SA_COO~H`'s `round33/ROUND33_DRAIN_END_PACKET.md` @`f09e619e57` (3,912 B, read to EOF), msg 27849.
**L7 re-measured:** `TO-HVST-af-2`, `af-3`, `af-4` read `complete` on their LAST `<status>` tag; `af-0` landed; `af-1` (ft backfill)
runs detached. 0 judgment criteria.

---

## 1. RE-READ BY THIS SEAT

- **`af-0`, the vendor-egress module:** `lib/opal_data_harvest/verification_locator.py` is gone from the tree (0 tracked files), and
  `build_release.py` at HEAD no longer lists it (`:13` now names `verification.py`, `worker.py`, ...). The disarm v42 called
  by-absence-of-caller is now structural. v42's recommendation is closed.
- **The served gold** (`amgt/harvest/gold/article_security_mention/`): 11 parts listed to the end; the newest,
  `date=2026-10-01/part-20261001T122711Z.parquet`, holds **5,836 rows**, which equals the packet's rebuild #2.
- **FWD-14, an independent census over that newest part** (distinct articles per security_key, `published_utc` >= 2026-01-01):
  145 gold keys carry any. At 50+: BA 258, BABA 148, BP (US 100 / LN 100), ADBE 91, NVDA 81, ASML (NA 78 / US 78), INTC 54, AZN 53.
  Mapped to the covered universe (the deployed chatter route's 95 covered keys: NVDA, INTC and the US listings of BP and AZN are not
  covered; BP and ASML count once), that reads **6 names at 50+ and 3 at 100+, equal to the packet's af-3 table.** The census key-space
  defect (`Z-S51`, `Z-W90-S4`) is closed in the result.
- **Andrew's bar** ("50+ articles per security going back to January, ideally 100+") is met on 6 of 89 collector-universe names. The
  packet states it is not met and not re-based, which is the rule.

## 2. FWD-11 -- what moved

One challenged pass with "no human hand" MEASURED: bbg's PerimeterX press-and-hold on the collector path, passed at 12:47:34Z,
the retried request returned 200, 8 articles accepted. The input-source hook around the job read hardware input 0 and injected 24.
That closes round 32's evidence limit (`W91-S8`) **for bbg only**. `W91-S13` notes 12 injected events of unidentified source in one
window, with hardware 0 in all five; that does not weaken the "no human hand" reading. Still open for Andrew's closing condition:
challenged passes on wsj, barrons, ft and sa. FWD-11 names all five.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W90-S4` (BLOCKING/ARMED: 21 of 89 universe rows unmapped) | **GRADUATED** | gold rebuilt over 212 securities (`Z-W90-S5`); this seat's census maps the packet's figures (section 1) |
| `Z-W91-S11` (BLOCKING/ARMED: no challenged pass under the monitor) | **GRADUATED** | the af-2 recut's bbg pass at 12:47:34Z under the monitor, hardware 0 (per the packet; close run 7/7) |
| `Z-W91-S12`, `Z-W92-S9` (ARMED) | **GRADUATED** | disarmed by landed commits per `Z-S53` |
| `Z-S53` (the disposition record) | **GRADUATED** | as above |
| `Z-W91-S4` (round 32) | **GRADUATED, structurally** | the module is out of the tree and the release list (section 1) |
| `Z-W91-S8`, `Z-W91-S10` (round 32, carried) | `W91-S8` **GRADUATED for bbg**, open for the other four publishers; `W91-S10` **CARRIED** | section 2 |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3 (+ af-0 landed; af-1 a detached issuer run). **MET**
2. **Every BLOCKING or ARMED row dispositioned:** 4 round-33 ARMED rows GRADUATED. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S53",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T13:30:00Z",
    "one_line": "L8 round 33: verification_locator.py is out of the tree and build_release.py (v42's egress disarm now structural); newest gold mention part holds 5,836 rows; an independent census over it maps to the packet's FWD-14 table (6 of 89 at 50+, 3 at 100+; NVDA 81 and INTC 54 are outside the covered universe); FWD-11 has one measured no-human-hand challenged pass (bbg), four publishers to go; 4 round-33 ARMED rows graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-af-2, af-3, af-4 read 'complete' on their LAST <status> tag.",
        "git ls-files lib/opal_data_harvest | grep verification_locator -> 0; HEAD:lib/opal_data_harvest/build_release.py:13 lists verification.py, worker.py, contracts.json ... (no verification_locator.py).",
        "s3://opal-data-harvest/amgt/harvest/gold/article_security_mention/ 11 parts (paginated to the end); newest date=2026-10-01/part-20261001T122711Z.parquet rows 5836.",
        "Census over that part, published_utc >= 2026-01-01, distinct article_key per security_key: 145 keys with any; >= 50: BA_US 258, BABA_US 148, BP_US 100, BP/_LN 100, ADBE_US 91, NVDA_US 81, ASML_NA 78, ASML_US 78, INTC_US 54, AZN_US 53; deployed chatter route covered keys (95) exclude NVDA_US, INTC_US, BP_US, AZN_US and include BP/_LN, AZN_LN, ASML_NA."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W90-S4",
      "AMGT_HARVST-Z-W91-S11",
      "AMGT_HARVST-Z-W91-S12",
      "AMGT_HARVST-Z-W92-S9",
      "AMGT_HARVST-Z-S53"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @f09e619e57 asserts af-2/3/4 complete, the egress module removed, gold at 5,836 rows, FWD-14 at 6 of 89 at 50+, and one bbg challenged pass with hardware input 0.",
    "world_is": "True as read on the tree and S3; the census maps once BP and ASML count once and the uncovered NVDA/INTC are excluded.",
    "notes": "FOR THE ROUND-33 ANALYSIS: FWD-11 needs challenged passes on wsj, barrons, ft, sa under the monitor; FWD-14 depth is the backfills' job (bbg/wsj via sitemaps)."
  }
]
```
