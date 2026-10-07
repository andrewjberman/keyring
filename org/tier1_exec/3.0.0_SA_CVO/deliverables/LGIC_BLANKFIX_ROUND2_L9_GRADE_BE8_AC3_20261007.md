# LGIC_BLANKFIX round 2 -- L9 grade of BE8-AC3 and the L8 compile (answer to 1.0.0_SA_CTO msg 106364)

**archetype:** VALIDATE

## BE8-AC3: NOT MET

The criterion: a seat that built none of the check reads the thread's run to the end and can act on every line without
asking a question, and tells a name that is wrong apart from a name that is not asked for a system. Read against
FWD-1's ACCEPT (three kinds of line only; no hole; a line from a saved example fails).

**Result: 122 of 140 lines can be acted on from the line alone. 18 cannot.** `hole=0` is true and measures blanks; it
does not measure whether a reader can act.

## What was read, and how

- The run was made LIVE by this seat, not read from the saved file:
  `python lib/opal_naming_rootcheck.py infra/aws/terraform/bd-pipeline --map infra/logic/registry/root_map.json --report-only`
  at HEAD (`lib/opal_naming_rootcheck.py` @4d5f31dad0), rc 0, 141 lines, last line
  `ROOTCHECK ok=True root=infra/aws/terraform/bd-pipeline items=140 right=9 fix=113 not_asked=9 pattern=1 carded=6 refused=2 hole=0`.
- `diff` of the live output against the saved trace
  `org/missions/D14/LGIC/LGIC_BLANKFIX/deliverables/2.0.0_SA_COO~G/THREAD_TRACE_round2_bd-pipeline.txt` @7145fcd3eb:
  0 lines differ.
- All 140 lines parsed (0 unparsed) and every one read. This seat built none of the check.

## The 122 that pass

- RIGHT, 9 of 9: the line gives the name back unchanged.
- FIX, 111 of 113: a whole target name, no brace, no blank, never equal to the old name, and no old name given two
  targets.
- PATTERN, 1 of 1: "a code pattern, not a name; variable '%s'". Nothing to do, and it says so.
- NOT-ASKED, 1 of 9: `openpyxl-layer`, whose printed name equals its current name.
- Wrong and not-asked are told apart on sight: the line's first word is FIX or NOT-ASKED.

## The 18 that do not

1. **NOT-ASKED, 8 of 9 (the inline policies).** Each line says "this kind of name is not asked to carry a system" and
   then prints a DIFFERENT name (`s3-access` -> `s3-access-policy`, `AdditionalPermissions` ->
   `additional-permissions-policy`). The reader cannot tell whether to rename or leave it: the line says the name is
   not wrong and hands over another one. FWD-1's ACCEPT also asks the line to say WHY the part is not asked; no line
   does.
2. **CARDED, 6 of 6.** "skipped by a card: K1: segment 1 'config' is neither a source nor a tier (this cell's own
   re-measurement, registry@HEAD)". This is not one of FWD-1's three kinds of line. It gives no correct name and no
   statement that none is owed, in words ("card", "K1", "V7") a reader who did not build the check cannot act on.
   Row W2-S5 measured the cause: no card carries a correct name.
3. **REFUSED, 2 of 2.** "this key belongs to another firm's store; conflict: path token 'cot' names firm 'cottonwood'
   ...; the key's bucket: opal-data-bd". The line states a problem and no act. Row S4 already reads it as
   misleading: the bucket is 49 Financial's own and only the file's name says Cottonwood.
4. **FIX, 2 of 113: one target for two machines.** EC2 instances `bd-49f-fees-runner` and `bd-fees` are both sent to
   `blackdiamond-49f-fees-runner`. Two resources cannot take one name; the reader has to ask which keeps it.

## Seen, not counted against the criterion

- 14 `FIX S3_BUCKET opal-data-bd -> opal-data-49financial` lines give a whole name, but the act is a data migration,
  not a rename a person types. The lines are complete; whether a root's engineer should act on them at all is
  1.0.0_SA_CTO's.
- The root's alarms resolve to three systems (`globgrph-`, `advi-`, and `blackdiamond-` for its other resources).
  Each line is complete; the mix was not checked against the registry here.

## The L8 compile

`org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/adjudications/ADJUDICATION_v1.md` dispositions all 22 rows of
the channel (0 ARMED): 5 GRADUATED, each with a remediation row; 17 DISMISSED (8 resolved inside rounds 1 and 2 and
re-read at HEAD, 6 carried by the remediation rows, 3 records). Five remediation rows in
`.../remediations/REMEDIATION_v1.md`: the thread's 18 lines (S4, owner 2.0.0_SA_COO~G); the folder map (W7-S1) and
the two match keys (W3-S2), owner 4.0.0_SA_CRO; and two calls owned by 1.0.0_SA_CTO: which wins for an inline policy,
its role or a ruled exception (W2-S4), and who corrects the stale worked case in GRADING_RULE.md (W2-S2).

-- 3.0.0_SA_CVO
