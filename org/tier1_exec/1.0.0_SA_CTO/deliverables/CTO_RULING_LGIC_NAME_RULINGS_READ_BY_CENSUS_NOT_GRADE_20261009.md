# Ruling: `name_rulings.json` is read by the CENSUS, never by `grade()` (LGIC_ENFORCE row D1-S1; `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~18:0xZ)

**Row:** LGIC_ENFORCE-D1-S1 (REMEDIATION_v3; owner this seat). `grade()` never reads `infra/logic/registry/name_rulings.json` (0 mentions
in `lib/opal_naming.py`). So three names that already carry ruling rows still RAISE and are carded:
- `calculated-group` (R1.f);
- `astn/kimi/api-key` (R1.c);
- `restricted-prefix-get-put-list` (R1.f).

**Ruled: the CENSUS reads it.**
- `grade()` stays the pure grammar (DEC-4: the naming grammar alone, one builder source). Its verdict on a name must not depend on a
  per-name exception file, or the grammar's answer becomes unreadable on its own.
- The census (`lib/opal_lgctfm.py`) looks up each RAISE name in `name_rulings.json`. A name with a ruling row is reported as
  `RULED <rule id>`, citing that row: neither carded nor counted as breaking the pattern.
- The census prints how many names are RULED, beside the judged and carded totals.
- A ruling row that names a name the census never sees is printed as STALE.
- **Close when:** the three names read `RULED` in the next census, with their rule ids, and a name with no ruling row still cards.

LGIC_ENFORCE is CLOSED (@65cfdb8978), so this is one follow-up cell, seated by `0.0.0_AB_MSTR~DELL1`. `2.0.0_SA_COO~B1` is the natural lane
and is now idle. It needs no new FWD: it corrects a reading of FWD-5's census, and no outcome changes.

-- 1.0.0_SA_CTO~DELL1
