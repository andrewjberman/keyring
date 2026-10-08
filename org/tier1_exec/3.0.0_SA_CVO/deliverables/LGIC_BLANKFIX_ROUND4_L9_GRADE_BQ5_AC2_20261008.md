# LGIC_BLANKFIX round 4 -- L9 grade of BQ5-AC2 (answer to 2.0.0_SA_COO~G msg 106667, sent on Andrew's "nudge cvo")

**archetype:** VALIDATE

## BQ5-AC2: MET -- 142 of 142 and 18 of 18

The criterion: a seat that built none of the check runs both roots LIVE, reads each to the end, and can act on every
line from the line alone, without asking anyone.

Both runs were made by this seat at HEAD `20e21c5078` (`lib/opal_naming_rootcheck.py` @57aefecc94), each
`python lib/opal_naming_rootcheck.py <root> --map infra/logic/registry/root_map.json --report-only`, rc 0, nothing on
stderr. Each equals its saved trace (0 lines differ, both). Every line parsed (0 unparsed) and read.

| root | last line | lines acted on |
|---|---|---|
| `infra/aws/terraform/bd-pipeline` | items=142 right=9 fix=118 not_asked=12 pattern=3 carded=0 refused=0 hole=0 | 142 of 142 |
| `infra/aws/terraform/investor-reporting/directory` | items=18 right=13 fix=5 not_asked=0 pattern=0 carded=0 refused=0 hole=0 | 18 of 18 |

## First root: what changed since round 3 (138 of 140)

- **The two REFUSED lines are now FIX lines** with a whole target:
  `code/bronze/cot_bronze_ingest.py -> blackdiamond/49financial/code/bronze/bronze_ingest.py`. The reader renames; no
  one has to be asked. The basis is a registry ruling (`infra/logic/registry/key_rulings.json`) on the CTO seat's
  measurement that the file is one script copied into each firm's bucket. Re-measured by this seat: `head-object` on
  that key reads 80,599 bytes and ETag `a1d81b96e8b679142176ad827af2c00d` in BOTH `opal-data-bd` and `opal-data-cot`.
  The target key does not exist in `opal-data-bd` today (one object under `code/bronze/` carries "bronze_ingest"), so
  the rename collides with nothing there.
- **Two new lines**, both FIX with whole targets: Lambda names held as literals
  (`opal-assets-bd49f-reporting-pull`, `bd-price-update`) are now judged.
- The 12 NOT-ASKED and 3 PATTERN lines are word for word what round 3 graded as actionable (15 of 15 unchanged).
- Across the 118 FIX lines: 0 with a brace, a blank or a question mark; 0 equal to the old name; 0 targets shared by
  two old names; 0 old names with two targets.

## Second root: what changed since round 3 (15 of 17)

- **The two HOLE lines are now FIX lines:**
  `investor-reporting/directory -> irpt/{scope}/platinum/directory/` and
  `investor-reporting/directory/_refresh -> irpt/{scope}/state/directory_refresh/`, each followed by "(the firm's place
  {scope} is filled per firm: the code reads its bucket from IRPT_DIRECTORY_BUCKET_MAP, one bucket per firm, so the
  firm is the one whose bucket is being served)".
- One new line: `irpt-directory-search -> irpt-directory-search-lambda`.

**The one judgment call in this grade.** Those two targets carry a brace. FWD-1's ACCEPT says "the whole correct name"
and "no line has a hole in it". This seat counts both lines as actionable, for this reason: the stored-file name in
the code is itself per firm (the bucket comes from an environment map at run time), so the correct form IS a form with
one variable, and the line says what fills it and from where. An engineer can write the key from the line without
asking anyone. What the line does not give is the list of the firms' words; that is a look-up in the registry, not a
question. If 1.0.0_SA_CTO reads "no hole" as "no brace, ever", these two lines are the only two that would fall, and
the grade would read 16 of 18.

## Scope of this grade

- Two roots of the thirteen in the map. The round's own cross-firm sweep over all thirteen reads `refused=3` and
  `unchecked=48` of 79 keys (BQ3-AC2, run by this seat): lines outside these two roots that this grade did not read.
- FIX lines were graded as complete and unambiguous, not as correct, apart from the one ruling re-measured above.

## The L8 compile

`ADJUDICATION_v3.md` dispositions the 4 rows filed since the last compile (34 in the channel, 0 ARMED): 1 GRADUATED
(S5, the proof checker's crash on a directory path, owner 1.0.0_SA_CTO), 3 DISMISSED as records. Clocks advanced on
this round's runs: S4, W2-S9, W1-S10 and W1-S8 REMEDIATED. W2-S2 stays OPEN: `lib/tests/test_opal_naming.py` line 80
still overrides the one worked case at load time.

-- 3.0.0_SA_CVO
