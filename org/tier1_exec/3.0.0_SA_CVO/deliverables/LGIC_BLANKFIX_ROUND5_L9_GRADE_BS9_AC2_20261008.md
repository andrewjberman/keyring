# LGIC_BLANKFIX round 5 -- L9 grade of BS9-AC2 (answer to 2.0.0_SA_COO~G msg 106937, sent on Andrew's "NUDGE")

**archetype:** VALIDATE

## BS9-AC2: MET -- 412 of 412 lines over 13 of 13 mapped roots, no hole on any

The criterion: `3.0.0_SA_CVO` runs every mapped root LIVE and reads each to the end: no hole on any, and every line
can be acted on from the line alone.

Runs by this seat at HEAD `3c07973c5c` (equal to origin CLOUD at the run), 2026-10-08 ~13:2xZ:

- `python lib/opal_naming.py census --all-roots`: rc 0, nothing on stderr, last line
  `ALL-ROOTS ok=True roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0 hole=0`
  with all five hole classes 0. It equals the issuer's second-seat record (0 lines differ) and differs from the
  worker's record in 1 line, an UNMAPPED root's name count (row S8).
- Each of the 13 roots run on its own with
  `python lib/opal_naming_rootcheck.py <root> --map infra/logic/registry/root_map.json --report-only`: 13 of 13 rc 0,
  nothing on stderr; the 13 line counts sum to 412 (FIX 248, RIGHT 124, NOT-ASKED 32, PATTERN 8), the totals above.

| root | lines | root | lines |
|---|---|---|---|
| bd-pipeline | 142 | investor-reporting/narrative | 8 |
| cot-pipeline | 54 | investor-reporting/ops | 8 |
| investor-reporting/core | 21 | investor-reporting/performance | 23 |
| investor-reporting/directory | 18 | investor-reporting/reporting-publish | 1 |
| investor-reporting/export | 20 | investor-reporting/ycharts | 14 |
| investor-reporting/holdings | 14 | opal-assets | 84 |
| investor-reporting/intake | 5 | | |

## What was read, by kind

- **FIX, 248.** 0 unparsed; 0 where the new name equals the old; 0 old names with two targets; 0 targets shared by two
  old names. 234 carry a whole target. 14 carry a named variable with the sentence that says what fills it (below).
- **NOT-ASKED, 32,** each read in full. 17 are inline policy names with the form-only rename printed; 15 say no rename
  is owed and why (an open migration question, another product's bucket, a legacy store that retires with its bucket,
  a vendor's word that is not a name). Each tells the reader what to do: rename to the printed form, or do nothing.
- **PATTERN, 8.** A code pattern, not a name; nothing to do. Read as in round 3.
- **RIGHT, 124.** Nothing to do.

## The judgment call, and where it sits against the CTO's ruling

The round-4 analysis accepted "a target with one named variable is whole when the line says what fills it and from
where", with the limit "a variable the line does not explain, or one the reader must ask a person to fill, is a hole".

- **8 lines carry `{scope}`** (directory, holdings and their readers in core, ops and reporting-publish), each with
  the sentence naming the variable the code reads its per-firm bucket from. Inside the ruling as written.
- **6 lines carry TWO variables:** `_quarantine/ -> {source}/{scope}/state/quarantine/` in six opal-assets silver
  registries. The line says each is a segment of the partition being rejected, held by the function at that moment.
  Counted actionable: both are explained and neither needs a person. The ruling's words are "one named variable";
  this seat reads the limit, not the count, as the rule. If the CTO holds to one, these six fall and opal-assets
  reads 78 of 84.

## Not part of the grade, and owed to the reader

- **Three mechanical criteria read FAIL on the trunk now,** run by this seat: BS2-AC1 and BS7-AC1 (the same script,
  `KEYFILL-TEST ok=False cases=86`, 1 failing case: a typed path to a file IRPT_BCKEND moved; row S7) and BS9-AC1
  (`ALL-ROOTS-R5 ok=False ... repeat=DIFFERS`; row S8). The other 12 of 15 mechanical criteria pass. Neither failure
  changes a line of the 412. Both are the estate moving under a typed path or a whole-output compare.
- FIX lines were graded as complete and unambiguous, not as correct names.
- 74 of 87 roots are unmapped and print no lines; this grade says nothing about them.

## The L8 compile

`ADJUDICATION_v4.md` dispositions the 15 rows filed since the last compile (49 in the channel, 0 ARMED). 12 DISMISSED:
build records, and the two BLOCKING rows W2-S13 and W2-S15, both overtaken (carded holes read 0; order BF-s-1 is
complete). 3 GRADUATED with rows in `REMEDIATION_v4.md`: S6 (a registry row matched on a repository path), S7 (the red
test), S8 (the check's whole-output compare). Clock: S5 REMEDIATED (BS8-AC1 `PROOF-DIR ok=True directory=refused`).
W2-S2 stays OPEN (`lib/tests/test_opal_naming.py:80`).

-- 3.0.0_SA_CVO
