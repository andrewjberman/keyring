# AMGT_CORPUS ROUND 19 -- L8 COMPILE (no judgment criterion; the issuer's one call weighed)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~02:5xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND19_DRAIN_END_PACKET.md` @`2`, msg 26856. The packet was read to EOF (4,668 B).
**L7 re-measured, not adopted:** `u-1`, `u-2` read `complete` on their LAST `<status>` tag. `u-3` is held on AMGT_RESAPP r51 cell 1,
and nothing is registered.

---

## 1. RE-RUNS BY THIS SEAT

- **The round-18 replay after u-2 and the hookup** (`round18/t2_AC1.sh`): "t2 replay rc 0 shared_changed 0 shared_removed 0
  type_changed 0 **hitachi_reproduced 214 of 214** non6501_added 0".
  - This is 209 of 214 at round 18 (ADJUDICATION_v21). The 5 this seat listed there (the BEST_ and CIE_DES_BULK `measured_on`
    appends) now reproduce, which confirms `Z-W2-S14`'s header-path cause.
- **u-1 AC1:** "u1 reader best_sales_6501 unit UNRESOLVED sign UNRESOLVED control_8035 unit MILLIONS sign POSITIVE
  module_in_toplevel yes".
- **u-1 AC2:** "u1 served best_sales_6501 FY1 value 11962163.4 served_unit_class UNRESOLVED reader_unit_class UNRESOLVED agree yes".
- So the served Hitachi block and the fixed reader agree. The control is unmoved, so the widened reader does not over-fire on a
  measured name.

## 2. THE ISSUER'S CALL -- the reader also honours a non-MEASURED per-security status without an `exception` key

**AGREED.** The committed map's 6501 entry predates the exception shape. An `exception`-only reader would have kept serving the
shared `MILLIONS`, the exact hazard `Z-W2-S13` named. The control 8035 reading MILLIONS/POSITIVE (section 1) shows the wider test
does not catch a measured name. Ruling 1's branch holds: the served block stands, and the fix protects the next derive.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W2-S13` (ARMED: an exception under a scalar shared field is invisible to the unit/sign readers) | **GRADUATED** | section 1, u-1 re-run |
| `Z-W2-S14` (the CLI and the producer feed different headers) | **GRADUATED** | 214 of 214 on this seat's replay |
| `Z-W1-S18` (ARMED: the import-time `sys.path` injection) | **CARRIED** -> AMGT_RESAPP (ruling 3) | u-1's probe guards it (`module_in_toplevel yes`) |
| `Z-S63`, `Z-S66` (ARMED) | **CARRIED** | u-3 waits on AMGT_RESAPP r51 cell 1 |
| `Z-S64` | **CARRIED** | the migration item |
| `Z-W2-S11` (BLOCKING/ARMED), `Z-S3`, `Z-S6`..`Z-S9` | **CARRIED**, unchanged | |

**For the analysis (packet section 6 item 2):** `_ensure_unit_map` writes with `Path.write_text(..., newline="\n")`, a keyword
Python 3.9 does not accept. The code's stated floor is 3.9, and the commit gate's ruff py39 target does not catch a keyword a
stdlib call gained later. It is INERT on today's runtime, but it is a floor the code claims and does not meet.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 2 of 2 cut. u-3 was held on a named external block. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W2-S13` GRADUATED; the rest CARRIED with owners. **MET**
3. **Every judgment item graded:** 0 criteria; the issuer's one call was AGREED. **MET**

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S22",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T02:55:00Z",
    "one_line": "L8 round 19: the Hitachi replay now reproduces 214 of 214 (209 at round 18; the 5 BEST_/CIE_DES_BULK appends this seat listed now land); u-1 re-run: 6501 BEST_SALES reads UNRESOLVED and agrees with the served block, the control 8035 stays MILLIONS/POSITIVE; the issuer's wider-reader call agreed; Z-W2-S13 and Z-W2-S14 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-CRPS-u-1 and u-2 read 'complete' on their LAST <status> tag.",
        "round18/t2_AC1.sh re-run: 't2 replay rc 0 shared_changed 0 shared_removed 0 type_changed 0 hitachi_reproduced 214 of 214 non6501_added 0'.",
        "u-1 AC1 re-run: 'u1 reader best_sales_6501 unit UNRESOLVED sign UNRESOLVED control_8035 unit MILLIONS sign POSITIVE module_in_toplevel yes'; AC2: 'u1 served best_sales_6501 FY1 value 11962163.4 served_unit_class UNRESOLVED reader_unit_class UNRESOLVED agree yes'."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W2-S13",
      "AMGT_CORPUS-Z-W2-S14"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet asserts u-1 and u-2 VALID and merged, the hookup landed, the real run agreeing served and reader, and u-3 blocked on AMGT_RESAPP r51 cell 1.",
    "world_is": "True as read on this seat's re-runs. Both round-18 ARMED/INERT unit rows are closed by measurement.",
    "notes": "FOR THE ROUND-19 ANALYSIS: Path.write_text(newline=...) in _ensure_unit_map breaks the code's stated Python 3.9 floor (ruff py39 cannot see it); u-3 carries on AMGT_RESAPP r51 cell 1."
  }
]
```
