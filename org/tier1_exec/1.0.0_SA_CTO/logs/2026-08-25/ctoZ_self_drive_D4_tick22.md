# /self-drive D4 -- ticks 21-22 log (2026-08-25 02:08Z - 02:45Z) -- state: ARMED

**archetype:** COORDINATE · **secondary:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick20.md`.
**37 minutes: an Andrew hypothesis confirmed, a TRUE finding of mine retracted and un-retracted, an undeployed fix caught with four seats already reporting it verified, a gate I manufactured and dissolved, and a phantom defect killed by a timezone offset.**

## SCOPE + COMPLETION

```
D4 -> ETFS_CANON(scoping) · ETFS_POSITIONING(active) · +ETFS_INGEST(claimed, active)
  COMPLETION TEST: NOT DONE -- 0 of 2.  REACHABLE 2 / UNREACHABLE 0.  open TOs 6
  1 of 9 live directives · device SITEZ · 1 RESERVED card at Andrew (the Pathfinder weekend stamp)
```

## ANDREW-DIRECT ~02:10Z -- HIS HYPOTHESIS, MEASURED, CONFIRMED

VERBATIM: *"the websites that post these csvs, actually do not have reliable date logic"*

**PATHFINDER FORWARD-DATES ON WEEKENDS** -- Sat 08-15 capture carries `08/17`; Sat 08-22 carries `08/24`.
Three instruments, two tiers, zero counterexamples (`3.0.0_SA_CVO~Z` Z-S33, 41 files · `2.0.0_SA_COO~Z`
14/14 · this seat, 12 days). **The Saturday file DIFFERS IN BYTES from Friday's** -- a genuine
forward-dated basket, not a re-stamp; that check is what separates "effective-for" from "lazy".
**IT REACHES OUR STORE:** `silver/holdings/2026-08-22` and `-23` carry a `data_as_of` **that had not
happened when we wrote it.** Recorded `ETFS_INGEST_PRD.md` §14 **@a24f7f98d7**.

## AND I RETRACTED A TRUE FINDING OF MY OWN, AT FULL REACH, THEN UN-RETRACTED IT

```
PROVIDERS, both holdings sheets, same Monday capture:  pathfinder 08/24/2026 · trueshares 8/24/2026
OUR STORE:  filepoint -> 2026-08-24 (114 rows)  |  trueshares -> 2026-08-21 (73 rows)
```
**The TrueShares sheet asserts 8/24 and we store 08-21** -- the NET-ASSETS PAGE as-of substituted onto
HOLDINGS rows. **Z-S16, live, backdating the provider by three calendar days.** My 00:5xZ finding
(*"no provider divergence -- we manufactured it at silver"*) **was correct.**

**MECHANISM OF THE RETRACTION:** `3.0.0_SA_CVO~Z` correctly falsified a **different limb** -- my
"TrueShares clean T-1, 12/12" is the NET-ASSETS page, and there is exactly ONE TrueShares holdings
capture in existence. **I let that valid correction propagate into an INDEPENDENT limb that shared
none of its evidence.**
>> **Two limbs, one message, one banner -- and the banner carried the falsification across.** *One
evidence banner over two evidence classes*, run in REVERSE: there it laundered an unmeasured claim UP;
here it dragged a MEASURED claim DOWN.

## THE BIG ONE -- THE DEPLOYED LAMBDA RUNS PRE-FIX BYTES

```
etf-positioning-producer  LastModified 2026-08-24T23:10:47Z  member 44,478 B (tree 49,469, +4,991)
  CASH_NAME_MARKERS  True   <- POSITIVE control
  zzz_no_such_token  False  <- NEGATIVE control
  mmkt               FALSE  |  ULTRA_SHORT_SUB_ASSET_CLASS  FALSE
  => BOTH 0c03c359f2 AND 2548d22787 UNDEPLOYED
```
**Left alone, the books fill at 13:00Z and SALXX -- the cash sleeve of BOTH DIVZ and IDVZ -- renders
as EQUITY, on the first day Andrew ever sees those funds.**

Within four minutes `0.4.0_DS_ClientPlatform~Z`, `3.0.0_SA_CVO~Z`, `2.0.0_SA_COO~Z` and
`0.7.0_AE_CloudOps~Z` reported it landed / verified / pushed. **EVERY REPORT WAS TRUE -- ALL FOUR
VERIFIED THE COMMIT. Nobody read the DEPLOYED ARTIFACT.** Four seats is 4x confidence in ONE rung and
zero coverage of the others; **the rung nobody stood on was CODE.**
`0.7.0_AE_CloudOps~Z`'s formulation is the keeper: ***"a timestamp comparison proves NOT THIS COMMIT;
only reading the artifact proves WHAT IS IN THERE."***

## A GATE I MANUFACTURED AT 01:5xZ AND DISSOLVED AT 02:38Z

AE~Z sat *"holding for the GO."* **No law requires one** -- Rules 1/26/4/22a are MECHANISMS, Rule 13
gives the lane to CloudOps, and NEVER#5 records this incident nearly verbatim (*"I approve on COOs
behalf, they should not be gating this"*). **The gate was MINE**: my *"deploy-or-hold is COO~Z's"*
was meant to lift my own block and read as naming an approver. **`2.0.0_SA_COO~Z` never claimed it.**

**AND THE CORRECTION NEEDED ITS OWN CORRECTION FOUR MINUTES LATER.**
`0.4.0_DS_ClientPlatform~Z`'s one-minute peer check found `test_..._forward.py:185` pinned
`sub_asset_class_vocab_size == 12` while the vocabulary went to **13** -- **a test that would have
FAILED ON THE CORRECT BUILD and read as a regression on the very morning DIVZ/IDVZ populate.** Fixed
as a **reconciliation against the composition, not re-pinned** (@7204fb077c).
>> **PEER CHECK vs GATE -- the test is whether work STOPS and who may restart it.** Bounded, specific,
asker keeps the decision = KEEP. Open-ended, needs someone else's word = NEVER#5.

## AND A PHANTOM DEFECT KILLED BY AN OFFSET

`3.0.0_SA_CVO~Z` read `0c03c359f2` as landing BEFORE the 23:10:47Z build -> *"the package was not built
from the tree it postdates."*
**`-04:00` puts that commit at 2026-08-25T01:40:34Z -- AFTER the build. The offset CROSSES MIDNIGHT, so
the DATE itself differs.**
**No stale checkout. Two commits, one deploy.** Their token census is CORRECT and I re-derived it --
**the measurement answered WHAT and was right; the timestamp answered WHY and was wrong** (Rule 22
exactly). Retracted in full by its author; `2.0.0_SA_COO~Z` independently confirmed.

**CORRECTED 02:47Z, BY `3.0.0_SA_CVO~Z` (7266) -- I ATTRIBUTED A MECHANISM I INFERRED AND NEVER
MEASURED.** I wrote *"a date is exactly where nobody looks for a timezone"*, which asserts the
CLAUDE.md-documented **hidden-offset** hazard. **They ran `%aI`. THE OFFSET WAS PRINTED. They saw it
and did not apply it.**
```
(A) FORMATTER HIDES THE OFFSET   -> the reader CANNOT know    REMEDY: %aI / %cI / iso-strict
(B) FORMATTER SHOWS THE OFFSET   -> the reader IGNORES it     REMEDY: *** NOT COVERED BY (A) ***
```
>> **THEIRS IS (B): THEY HAD THE PRESCRIBED REMEDY IN PLACE AND FAILED ANYWAY. Banking "use an
offset-carrying formatter" as tonight's lesson would cover the case that DID NOT happen and leave the
one that DID.** << **And the reason my wrong attribution felt confirmed is that it FIT A DOCUMENTED
HAZARD -- a known failure mode is the most persuasive place to file an unmeasured cause.** I hold
every seat to Rule 22 and asserted a causal claim about a peer's reasoning with no access to their
command.
**THE CONTROL FOR (B), stated because "look harder" is care and not a control: A TIMESTAMP COMPARISON
THAT DECIDES SOMETHING MUST BE *COMPUTED*, NEVER *READ*.** Displaying the offset helps a human; it
does not make a human comparison reliable. My own read was right only because python converted both
sides to UTC and evaluated `>` -- **the machine did the comparing, and that is the whole difference.**

## OTHER RULINGS THIS WINDOW

- **04:00Z RUN DROPPED ENTIRELY** (not moved to 04:15Z). `0.4.0_DS_ClientPlatform~Z` measured it as
  **exactly local midnight -- zero-second margin**; I measured that its only consumer is
  `etf-positioning-producer-daily cron(0 13)`, so **it could not move Andrew's clock by one minute** --
  and hand-firing it would put a client-facing number on an ad-hoc artifact (**NEVER#4**).
  **I priced it "a FREE OPTION" at 00:5xZ and never re-priced it when the consumer's schedule became
  known. AN OPTION PRICED ONCE AND NEVER RE-PRICED IS A STANDING COMMITMENT IN OPTION'S CLOTHES.**
- **TWO FREEZE DEADLINES, NOT ONE.** `2.0.0_SA_COO~Z` found the 11:00Z pull is a **LOCAL desktop task**,
  not EventBridge; I read the task action -- it EXECs a `.cmd` **inside the repo**, so it runs the
  WORKING TREE. `etf_daily_pull.py` freezes at **07:00 LOCAL (11:00Z)**; the gold Lambda at 13:00Z.
  **My 02:27Z boundary collapsed them and would have called a 09:00Z edit "comfortably inside."**
  Two positives nobody had: the task **ran 08-24 07:00:01 rc=0**, and a **07:30-local freshness check
  already exists** and also ran clean. **Nothing to build; the moratorium is not in play.**
- **SEATING ASK to `0.0.0_AB_MSTR~Z`:** `0.0.3_BG_BBGTerminal` is **not among the 7 live seats**, and the
  11:00Z pull needs a signed-in terminal plus this box awake. DAPI `ok=true` at 02:29Z -- **a reading of
  NOW, not a forecast.** Explicitly **not** an alarm or monitor proposal.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| boto3 + pandas | 12 days x 2 providers, bronze date fields | Pathfinder forward-dates weekends; TrueShares netassets clean T-1 |
| boto3 groupby | `silver/holdings/2026-08-24` by `source` | **filepoint 08-24 / trueshares 08-21 -- the split is OURS** |
| aws lambda get-function + zipfile | deployed member, 4 tokens, both controls | **both commits UNDEPLOYED** |
| git log `%cI` + python UTC convert | commit-vs-build ordering | **both AFTER the build -- no build defect** |
| Get-ScheduledTask | the task ACTION, not the name | local `.cmd` inside the repo -> working tree; ran rc=0 |
| aws events list-rules / list-targets-by-rule | the gold consumer | `cron(0 13)` -> Lambda `etf-positioning-producer` |
| bloomberg_health | DAPI reachability | ok=true 02:29Z (a reading of now) |

## Blockers

None at this seat. **1 RESERVED at Andrew: what we stamp for PATHFINDER ON A WEEKEND** -- his 23:0xZ
provenance ruling has no sound source there. **Z-S16 needs no ruling: a defect under every limb of that
fork.** Deploy authorised by his 01:21Z word (`0.0.0_AB_MSTR~Z`'s reading, ratified);
**`0.7.0_AE_CloudOps~Z` owns it, ~10h to 13:00Z, NEVER#6 binds whoever starts.**
