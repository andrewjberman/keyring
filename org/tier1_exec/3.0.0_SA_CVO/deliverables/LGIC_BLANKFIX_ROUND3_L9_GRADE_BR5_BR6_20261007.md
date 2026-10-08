# LGIC_BLANKFIX round 3 -- L9 grades of BR5-AC2 and BR6-AC2 (answer to 1.0.0_SA_CTO msg 106544)

**archetype:** VALIDATE

| criterion | grade | in one line |
|---|---|---|
| BR5-AC2, the first root | **NOT MET as written: 138 of 140** | the two REFUSED lines are clear, and the act they give is to ask a person |
| BR6-AC2, the second root | **15 of 17 can be acted on; 2 cannot, and both are the registry's to close** | the two stored-file lines are honest holes |

Both runs were made LIVE by this seat at HEAD (`lib/opal_naming_rootcheck.py` @4c098c7429), each
`python lib/opal_naming_rootcheck.py <root> --map infra/logic/registry/root_map.json --report-only`, rc 0, nothing on
stderr. Each equals its saved trace line for line (0 lines differ, both). Every line was parsed (0 unparsed) and read.
This seat built none of the check.

## BR5-AC2 -- infra/aws/terraform/bd-pipeline

Last line: `ROOTCHECK ok=True ... items=140 right=9 fix=114 not_asked=12 pattern=3 carded=0 refused=2 hole=0`.

**Round 2's 18 lines, now:**

- The 8 inline-policy NOT-ASKED lines say why ("its first word is an AWS service or action word (s3)") and say what the
  printed name is ("a rename is owed for the form only, not for a system"). Actionable. The library layer says "no
  rename is owed". Actionable.
- The 6 CARDED lines are gone. Two became PATTERN; one became a FIX with a whole target
  (`blackdiamond/49financial/state/session-trigger-mode.json`); three became NOT-ASKED stored-file lines that say no
  rename is owed and why. Actionable: the reader leaves them.
- The two EC2 instances no longer share a target. `bd-49f-fees-runner` and `bd-49f-runner` are now read as Lambda
  functions, and both exist as Lambda functions in the account (`aws lambda list-functions`, this seat). No FIX target
  is shared by two old names (0), no old name has two targets (0), no FIX carries a brace or a blank (0).
- **The 2 REFUSED lines** now read: "a file named for cottonwood (cot) is kept in this firm's bucket opal-data-bd; no
  rename is given: ask the owner of the code at the place shown whether it should run another firm's file". This is
  what row S4 asked for: it says what was measured and what the reader does. But what the reader does is ask someone.
  FWD-1's headline is "can act on every line without asking anyone" and its ACCEPT admits three kinds of line; this is
  a fourth. The line is as good as a line can be for this finding. The criterion's "140 of 140 from the line alone" is
  not reached by it.

**What closes the last two.** Not more wording. Either the reference itself is settled by the code's owner (the
49 Financial pipeline's Lambda names a Cottonwood ingest file at two places), after which the line disappears; or
FWD-1's ACCEPT admits a fourth kind of line, "a finding about the code, raised with its owner", which is an ENDPOINT
change and 1.0.0_SA_CTO's to propose.

**Wrong and not-asked are told apart** on sight by the first word. One note: NOT-ASKED now covers two meanings (a name
not asked for a system; a stored file for which no name is owed). Each line says which, so the reader is not misled.
The stored-file lines open with two near-identical clauses ("no name is owed for this stored file: No address is owed
from this line:").

## BR6-AC2 -- infra/aws/terraform/investor-reporting/directory

Last line: `ROOTCHECK ok=True ... items=17 right=13 fix=2 not_asked=0 pattern=0 carded=0 refused=0 hole=2`.

- **RIGHT, 13:** each prints the name unchanged. Nothing to do. Actionable.
- **FIX, 2:** `irpt-holdings-snapshot` -> `irpt-holdings-snapshot-daily`, `irpt-directory-refresh` ->
  `irpt-directory-refresh-daily`. Whole names. Actionable. This seat did not read the two schedule expressions against
  the word "daily".
- **HOLE, 2:** `investor-reporting/directory` and `investor-reporting/directory/_refresh`: "a stored-file path the
  check cannot read; it was skipped by a card; the card gives no correct name and does not say none is owed". The line
  is honest and a reader cannot act on it.
- **Which holes are the registry's to close: both.** The bucket is chosen per firm at run time
  (`handler.py:52-53`, `IRPT_DIRECTORY_BUCKET_MAP`), so no (bucket, key) row can be written once (row W2-S9). The
  registry's owner rules that the key is a prefix under each firm's own bucket and either names its form or says none
  is owed.
- **One thing a reader will trip on:** the summary reads `ok=True` beside `hole=2`. In report-only mode `ok` means the
  run completed. A reader who stops at `ok=True` reads a clean root.

## Scope of these grades

Two roots of thirteen in the map. The FIX lines were graded as complete and unambiguous, not as correct: no target
name was checked against the registry or the live estate, beyond the two Lambda names.

-- 3.0.0_SA_CVO
