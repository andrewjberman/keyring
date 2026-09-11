# AMGT_RESAPP -- surprise channel, ADJUDICATION v1 (round 1, site Z)

**Home:** the project tree's adjudication document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 4a; lane
`TREE_CVO`). **Who writes:** `3.0.0_SA_CVO~Z`, and only the CVO. Round 1's CVO rows carry
`AMGT_RESAPP-Z-C-S<k>`, `k` starting at 1 here.

**Round 1 L8/L9 read (L8 ENGAGE `1.0.0_SA_CTO~Z` msg 21143, routing `2.0.0_SA_COO~ZZZ`'s drain-end read
21137).** Per spine s.1, L8 compilation is this seat's limb and its engagement with the project BEGINS there,
so the packet's arithmetic is **verified here, not accepted**. L8 stamped `@9ec260e3b2`
(`prd/stamps/L8.r1.json`).

**WHAT THIS DOCUMENT CARRIES, stated as a PREDICATE rather than a count because the channel is append-only
and a count ages the moment the next cell files:** the round-1 L9 disposition of EVERY investigation item
open at the drain -- `C-S1` the identity-collapse cluster (verified ALREADY REMEDIATED in the artifact),
`C-S2` the criterion-cannot-discriminate class, `C-S3` the device/worktree instrument traps, `C-S4` the
substantive data and semantic findings, `C-S5` the single dismissal, and `C-S6` the externally-blocked
AMGT-s-b4 TLS row.

> **WHY SIX ROWS AND NOT ONE.** `.tools/surprise-row-gate.py:404` applies an adjudication row's SINGLE
> `disposition` to EVERY id in its `adjudicates` list, so a row cannot carry mixed dispositions. One row per
> disposition-and-class is the grain the gate permits; bundling `C-S5`'s dismissal with the graduations would
> have silently flipped it to GRADUATED.

> **COVERAGE, BY SUBTRACTION AND NOT BY RECALL.** The channel's own denominator at the drain is **24**
> investigation items, all UNDER_INVESTIGATION. The six rows below adjudicate 4 + 7 + 4 + 7 + 1 + 1 = **24**,
> and the id set was taken from `comp-surprise --project AMGT_RESAPP --json` rather than assembled by hand,
> so a missed member would show as a count disagreement rather than as silence.

> ⚠ **L10 IS NOT CUT BY THIS DOCUMENT.** `AMGT-s-b4` is externally blocked and a slug needs every task order
> terminal; that gate is `1.0.0_SA_CTO~Z`'s and Andrew's (21143). L8 and L9 expressly do not wait on it.

---

## C-S1 -- W7-S3, S3, W1-S1, W9-S1: the 16-way identity collapse is REAL and ALREADY REMEDIATED; 32 MEASURED of 32 distinct, measured here

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S1",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T03:05Z",
    "one_line": "ALL FOUR GRADUATE, AND THE HAZARD IS ALREADY GONE FROM THE ARTIFACT -- measured here, not taken from any seat's report. The 16-way 'AAPL US' collapse in AMGT-s-12's universe.json is REAL and is REMEDIATED: current ticker_status_partition reads MEASURED 32 / INFERRED 0 / UNRESOLVED 57 over denominator_folders 89, and of those 32 MEASURED values there are 32 DISTINCT -- one to one, zero repeats, and 'AAPL US' appears as MEASURED ZERO times. The arithmetic closes on the rows' own figures: 48 MEASURED with 33 distinct is 32 singletons plus one value on 16 folders, and 48 - 16 = 32. The 16 are not deleted or quietly overwritten either -- they are DISCLOSED in the artifact under its own `shared_ticker_placeholders_downgraded` key, which names all sixteen folders from AstraZeneca to Total Energies including the CRO's own control folder 'SAP GY'. So four workers and the issuer each surfaced one true defect, and the fix landed inside the round with its own provenance. W7-S3's ARMED standing is DISARMED BY EXERCISE, not by the edit alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "GRADUATED",
    "adjudicates": [
      "AMGT_RESAPP-Z-W7-S3",
      "AMGT_RESAPP-Z-S3",
      "AMGT_RESAPP-Z-W1-S1",
      "AMGT_RESAPP-Z-W9-S1"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE REMEDIATION, measured at this seat by reading the served artifact rather than any report (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json): denominator_folders 89; ticker_status_partition MEASURED 32 / INFERRED 0 / UNRESOLVED 57 (32+57 = 89, so the partition is complete and MECE over the declared domain).",
        "THE DISCRIMINATOR THAT SETTLES IT, and it is the one a status count alone cannot give: I recounted the MEASURED values MYSELF from the `names` list -- 32 MEASURED, 32 DISTINCT, most common value count = 1. A collapse survives a status partition unchanged (16 rows can all read MEASURED), so only a DISTINCT-vs-TOTAL comparison can see it. 'AAPL US' as a MEASURED value: 0 occurrences.",
        "THE FIX IS DISCLOSED, NOT SILENT: `shared_ticker_placeholders_downgraded` carries the literal key 'AAPL US' mapped to its sixteen folders (AstraZeneca AZN, Canadian National Railway CNR, Clorox CLX, Copa CPA, Imperial Brands IMB LN, JD.com 9618 HK, Michelin ML FP, Mitsubishi UFJ 8306 JP, Nestle NESN SW, Nokia FH, Orange ORA FP, SAP GY, Sanofi SAN FP, Shopify SHOP CA, Tokyo Marine 8766 JP, Total Energies TTE FP). Sixteen named members, matching the rows' count exactly. A reader can see WHAT was removed and WHY, which is the property that makes the downgrade auditable rather than a quiet number change.",
        "THE DOWNGRADE DIRECTION IS THE CORRECT ONE: the 16 went from MEASURED to UNRESOLVED, not to INFERRED. A shared placeholder is not weak evidence of an identity, it is NO evidence, and INFERRED would have claimed more than the world supports. INFERRED reads 0.",
        "S3 (the issuer's read) is confirmed on its own terms as well: it re-measured 48 MEASURED / 33 distinct / one value on 16 folders and REOPENED the order with AC7 inside the round rather than deferring to round 2, on the stated ground that four consumers hang off the identity root. The artifact's present state is what that reopening produced."
      ]
    },
    "spec_asserts": "AMGT-s-12's identity layer supplies the resolved security identity every downstream cell keys on, and a MEASURED status asserts the value was read from a source rather than guessed.",
    "world_is": "The collapse was real at the vintage the four rows were filed, and at HEAD the artifact carries 32 MEASURED values that are 32 distinct values, with the sixteen shared placeholders downgraded to UNRESOLVED and named in the artifact itself.",
    "notes": "⭐ WHY THIS DEFECT MATTERED MORE THAN A WRONG NUMBER, stated because the class recurs: a wrong FIGURE is checkable against the data, but A WRONG IDENTITY CHANGES WHAT THE DATA IS QUERIED FOR. Sixteen unrelated companies resolving to Apple's ticker would have had four downstream consumers confidently fetching the wrong company's fundamentals, and every per-figure check would have passed on them. ⛔ AND NOTE THE RESIDUAL, WHICH IS NOT A DEFECT BUT IS NOT NOTHING: 57 of 89 folders now read UNRESOLVED. That is the honest state, and it is the work the identity layer still owes -- it should be read as a measured gap with an owner, never as a regression from the 48 that included sixteen falsehoods. A smaller honest number beat a larger contaminated one.",
    "disarm_owner": "W7-S3 -> DISARMED BY EXERCISE and confirmed at the artifact, not by the disarm_owner's word: its named owner 2.0.0_SA_COO~ZZZ reopened AMGT-s-12 with AC7 and the downgrade landed, so the specific hazard (a MEASURED value shared across unrelated folders) cannot now recur on this artifact -- 32 of 32 distinct. The three OBSERVATION siblings were never armed. REMAINING and NOT disarmed by this row: the 57 UNRESOLVED folders, whose owner is AMGT-s-12's cell owner, not this seat."
  }
]
```

## C-S2 -- W7-S1, W2-S2, W3-S4, W7-S5, W3-S2, W7-S2, S2: seven criteria and instruments that cannot discriminate

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T03:05Z",
    "one_line": "ALL SEVEN GRADUATE AS ONE CLASS, AND IT IS THE MOST EXPENSIVE CLASS IN THIS CHANNEL: A CRITERION WHOSE INVOCATION CANNOT BE SATISFIED BY A CORRECT BUILD IS NOT A WEAK CRITERION, IT IS A NON-CRITERION -- it returns the same verdict on a correct world and a broken one, so nothing about the estate can move it. Three are ALWAYS-FAILS by construction: W7-S1 (AC4's string check cannot match the TO-NAMED tool's own hardcoded Status value), W2-S2 (AC6 greps `comp-routes behaviors`, which prints STATIC hand-authored comments and structurally cannot show a pure-add route; the route IS visible under the `api-routes` subcommand AC6 does not name), W3-S4 (AMGT-s-9's AC2 reads a top-level `figure_ids` key that NONE of AMGT-s-1's three landed files carries, because figures are keyed by a (scope, fiscal_year, mnemonic) tuple there). One is JOINTLY UNSATISFIABLE: W7-S5, where the issuer's instruction and the owned-paths gate cannot both be obeyed, because a TERMINAL order is not a live grant. Two are FACE-VS-GATE disagreements on the same field: W3-S2 and W7-S2, the proof-of-spec filename, where the worker face names a shorter stem than the gate's discovery glob requires. One is an INSTRUMENT GRAIN defect: S2, where receiving-check.py grades one file at a time so an issuance-set coverage limb refuses every member (owns 1 of 16) while the same gate over the set passes 16 of 16.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "adjudicates": [
      "AMGT_RESAPP-Z-W7-S1",
      "AMGT_RESAPP-Z-W2-S2",
      "AMGT_RESAPP-Z-W3-S4",
      "AMGT_RESAPP-Z-W7-S5",
      "AMGT_RESAPP-Z-W3-S2",
      "AMGT_RESAPP-Z-W7-S2",
      "AMGT_RESAPP-Z-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE COMMON PROPERTY, and it is what makes these one row rather than seven: in every case the criterion's verdict is INDEPENDENT of the thing it purports to measure. A correct build and a broken one produce the identical output, so the criterion carries zero discriminating power and its PASS or FAIL says nothing. That is the always-fails member of the three shapes (always-fails / always-passes / unsatisfiable-honest).",
        "W2-S2 IS THE SHARPEST INSTANCE BECAUSE THE EVIDENCE THE CRITERION WANTED DOES EXIST, one subcommand away: `comp-routes behaviors` renders each behavior's static hand-authored comment, never a computed route list, so no amount of correct building makes a new route appear there; `comp-routes api-routes` shows the declared route. The criterion named the wrong instrument, not a missing capability -- which is the version of this defect that wastes the most time, because the build is right and the reading is wrong.",
        "W7-S1 IS THE VERSION THAT IMPLICATES THE ORDER'S OWN TOOL CHOICE: AC4's patterns cannot match the Status value that .tools/deploy_ledger.py's cmd_close HARDCODES -- and deploy_ledger.py is the tool the task order itself names. So following the order exactly is what makes the criterion fail. A criterion must be run against the world BEFORE it is handed to a worker, and against the TOOL THE ORDER NAMES rather than against an imagined equivalent.",
        "W7-S5 IS A DIFFERENT SHAPE AND MUST NOT BE COLLAPSED INTO THE OTHERS: nothing is wrong with its criterion text. Two instructions are individually satisfiable and jointly contradictory -- the issuer required a regenerate whose code fix lives under lib/research/freshness/, a path granted ONLY by AMGT-s-7's own order, and AMGT-s-7 is COMPLETE. A terminal order is not a live grant. The worker correctly refused to commit rather than reaching outside its lane, which is the behaviour the lane gate exists to produce.",
        "W3-S2 AND W7-S2 ARE ONE DEFECT SURFACED TWICE, from two different workers, on the SAME field: the worker-face proof-of-spec filename versus to-pipeline-gate.py's check_complete_flip discovery glob, which requires the FULL task-order-filename stem. W7-S2 records that its own launch prompt dictated the shorter name, so a correctly-produced instance was INVISIBLE to the gate until renamed. Two independent surfacings of one face-authoring defect is corroboration, not duplication.",
        "S2's GRAIN DEFECT IS THE ONE THAT LOOKS LIKE A FAILURE AND IS NOT: receiving-check.py's per-file grain makes an issuance-set coverage limb read 'owns 1 of 16' for every member, while the same gate run over the SET reads 16 of 16. Same world, two denominators, opposite verdicts -- a check scoped to the member cannot answer a question about the set."
      ]
    },
    "spec_asserts": "Each acceptance criterion asserts that running its named invocation and meeting its stated expectation demonstrates the cell's outcome; and an issuer's instruction asserts it is executable within the lane the order grants.",
    "world_is": "Seven criteria or instruments cannot deliver that: three cannot be satisfied by any correct build, one is jointly unsatisfiable with the lane gate, two name a filename the gate will not discover, and one grades at a grain that cannot see the set it is asked about.",
    "notes": "⛔ THIS ROW CARRIES ARMED BECAUSE THE DEFECTS ARE IN ORDER AND TOOL TEXT THAT OUTLIVES THIS ROUND. A future cut copying any of these criteria inherits the same dead verdict, and the proof-of-spec filename defect in particular bit twice in ONE round. ⭐ THE PRACTICE WORTH PRESERVING IS THE WORKERS': every one of these was found because a worker RAN THE CRITERION AS WRITTEN, hit the impossibility, and filed a row instead of quietly substituting a working command and pasting a passing output. A worker that 'helpfully' fixes a criterion in its head leaves the defect in the order for the next round to pay for, and its PASS is then indistinguishable from a real one. ⚠ NOTE WHAT I AM NOT DOING: I am not relaxing, rewriting or re-grading any criterion. The cells' underlying work is not impeached by any of these -- in each case the world was right and the reading was wrong.",
    "disarm_owner": "PER-ROW, and NONE is disarmed by this round closing. CRITERION TEXT -> the criterion author at the cut (2.0.0_SA_COO~ZZZ) for W7-S1's AC4 patterns, W2-S2's AC6 invocation (substitute the `api-routes` subcommand), W3-S4's AC2 figure_ids key (read the (scope, fiscal_year, mnemonic) tuple AMGT-s-1 actually writes), and the W3-S2/W7-S2 worker-face filename (emit the full task-order stem the gate globs for). THE JOINT UNSATISFIABILITY W7-S5 -> the issuer, and it needs a GRANT decision not a text edit: either re-open AMGT-s-7's lane for the fix or cut the regenerate as its own cell. THE INSTRUMENT GRAIN S2 -> the gate's owner 1.0.0_SA_CTO~Z (receiving-check.py's per-file grain versus an issuance-set question). NOTHING IS BUILT, CHOSEN OR APPLIED BY THIS ROW."
  }
]
```

## C-S3 -- W2-S4, W2-S3, W1-S3, W1-S4: four device/worktree instruments that return a clean, confident, wrong answer

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S3",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T03:05Z",
    "one_line": "ALL FOUR GRADUATE, AND THEY SHARE ONE PROPERTY THAT MAKES THEM DANGEROUS: EACH RETURNS A CLEAN, CONFIDENT, WRONG ANSWER ON THIS DEVICE WITH NO ERROR. W2-S4 is the one every seat should read -- the BARE `comp-routes` PATH shim is baked to this device's MAIN checkout, a different directory that never had this branch's commits, so it reported '0' for a route that EXISTS; invoking the worktree's own tracked copy (`bash .tools/comp-routes`) lists it. The issuer's irreproducible '0' was an instrument artifact, not a blind extractor, and the worker re-measured rather than argued. W2-S3 is the same family: an `grep -r` counted a byte-coincidence inside a GITIGNORED terraform provider binary as a loopback violation, reading 1 instead of 0 until the ephemeral .terraform/ cache was removed. W1-S3: the root .gitignore ignores the whole lib/ tree at :47, so any NEW file under lib/research/ is gitignored and `git status`/`git add` report it clean-absent without -f, while already-tracked siblings are unaffected. W1-S4: this worktree's .gitmodules is EMPTY, so the pinned portal gitlink cannot be initialized here at all, and the named READ material was read from the shared main checkout, which carries a DIFFERENT portal commit that also lacks the pin.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "adjudicates": [
      "AMGT_RESAPP-Z-W2-S4",
      "AMGT_RESAPP-Z-W2-S3",
      "AMGT_RESAPP-Z-W1-S3",
      "AMGT_RESAPP-Z-W1-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE SHARED PROPERTY, which is why these are one row: none of the four fails loudly. A wrong shim, a gitignored binary, a gitignored path and an empty .gitmodules all produce rc=0 and a plausible number or a clean tree. A control placed INSIDE any of these reads healthy, because the instrument is answering a different question than the one asked.",
        "W2-S4 IS A CORRECTION OF AN ISSUER'S FIGURE AND IT WAS MADE THE RIGHT WAY -- re-measured, with the two invocations distinguished: bare `comp-routes` (PATH shim, baked to the MAIN checkout) versus `bash .tools/comp-routes` (this worktree's tracked copy). Same tool name, two different programs, opposite answers. This is the worktree-versus-shim class this estate has met before and it will recur on every branch that adds a route.",
        "W1-S3's MECHANISM IS EXACT AND CHECKABLE: git does not re-apply .gitignore to already-tracked paths, which is precisely why the trap is invisible -- lib/research/identity/ and its tracked siblings behave normally while a NEW sibling directory silently does not exist to git. The failure appears as absence, and absence is the reading that stops an investigation.",
        "W2-S3's hazard_standing is ARMED and its condition is EPHEMERAL: it depends on a .terraform/ cache being present at read time, so the same command is correct or wrong depending on whether anyone has run `terraform init` in that directory since. An intermittent instrument is worse than a broken one, because a single clean run reads as proof.",
        "W1-S4 IS A GRAIN/VINTAGE HAZARD, NOT A MISSING FILE: the material was read, and read from a real checkout -- just not from the commit the cell pinned. Two checkouts, two portal commits, NEITHER containing the pin. A citation satisfied from the wrong vintage looks exactly like a citation satisfied."
      ]
    },
    "spec_asserts": "A criterion's invocation asserts that running that command on this device measures the property the criterion names.",
    "world_is": "Four invocations on this device measure something else and say so with rc=0: a shim bound to another checkout, a grep reaching into a gitignored binary, a gitignore hiding new files under a partly-tracked tree, and an empty .gitmodules standing in for a pinned submodule.",
    "notes": "⛔ ARMED BECAUSE EVERY ONE OF THESE IS A PROPERTY OF THE DEVICE AND THE WORKTREE, NOT OF THIS ROUND -- they are live for the next worker on the next branch, and three of the four will recur by default rather than by accident. ⭐ THE GENERAL RULE THESE FOUR TEACH TOGETHER: WHEN AN INSTRUMENT RETURNS A NUMBER YOU CANNOT REPRODUCE, SUSPECT THE INSTRUMENT'S IDENTITY BEFORE ITS LOGIC -- which binary ran, which checkout it was bound to, which files it was allowed to see. W2-S4's worker did exactly that and converted an issuer's unexplained '0' into a named cause in one read. ⚠ AND THE ASYMMETRY WORTH NAMING: three of these four errors point toward ABSENCE (no route, no file, no submodule), and absence is the answer that ends an inquiry rather than provoking one.",
    "disarm_owner": "PER-ROW, all four outside this round's reach. W2-S4 and W2-S3 -> the comp-tool rail's owner 1.0.0_SA_CTO~Z: the shim-versus-worktree binding is a rail-wide hazard (a bare comp-tool on a branch answers from MAIN), and the grep-into-gitignored-binary case wants the ephemeral floor excluded by construction rather than by remembering to clean .terraform/. W1-S3 -> whoever owns the root .gitignore's lib/ line; the one-line remedy is a negation for lib/research/**, and until then every new file there needs -f. W1-S4 -> the device/fabric owner via the CTO: an empty .gitmodules in a worktree that pins a gitlink cannot be fixed from inside a cell. NOTHING APPLIED HERE."
  }
]
```

## C-S4 -- W1-S2, W4-S1, W3-S1, W5-S1, S1, W2-S1, W3-S3: the substantive findings about the world

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S4",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T03:05Z",
    "one_line": "ALL SEVEN GRADUATE AS SUBSTANTIVE FINDINGS ABOUT THE WORLD RATHER THAN ABOUT AN INSTRUMENT, and two of them are the ones I would not want lost. W1-S2: for the ADR (BABA US, fiscal year end 31 March), Bloomberg NEVER returns a row carrying both a price field and a fundamentals field -- 100% of rows split fiscal-period-end fundamentals from calendar-year-end prices -- so a fiscal-year join keyed on the calendar year of `date` marries each fiscal year's fundamentals to a price observation roughly NINE MONTHS LATER. That is a silently wrong ratio on every non-December fiscal-year-end security, and it is a correctness defect, not a coverage one. W4-S1: AC1's own required action re-runs a PEER's script whose OUTPUT_PATH is derived from `__file__`, so it TRUNCATES that already-completed worker's committed deliverable in place, by construction, on every run -- verified at source. The remaining five: W3-S1 ('the workbook' is not always one file -- 5 of 89 folders carry TWO disagreeing ONE PAGERs), W5-S1 (staleness is list-wide because the schemas name reviewed_at once per LIST, never per entry, so N is 0 or all; plus a `security_key` this project defines nowhere else), S1 (the manifest draws no S1->S6 edge although S1's raw landing needs the store S6 creates, absent at two vintages), W2-S1 (a disclosed deliberate exception to STORE_CONTRACT rule 1), W3-S3 (a ticker set reused from a sibling cell rather than derived independently).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "adjudicates": [
      "AMGT_RESAPP-Z-W1-S2",
      "AMGT_RESAPP-Z-W4-S1",
      "AMGT_RESAPP-Z-W3-S1",
      "AMGT_RESAPP-Z-W5-S1",
      "AMGT_RESAPP-Z-S1",
      "AMGT_RESAPP-Z-W2-S1",
      "AMGT_RESAPP-Z-W3-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W4-S1 VERIFIED AT SOURCE, not from the row's word: f6_remeasure.py:65 reads `OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"f6_remeasure.json\")` and :234 opens it in \"w\" mode, which TRUNCATES. The path is bound to the SCRIPT'S location, never to the caller's, so any worker re-running it overwrites 0.9.0_WK_AMGT_RESAPP~3's committed f6_remeasure.json. The script's own docstring at :48 says 'Writes: f6_remeasure.json beside this script' -- the behaviour is disclosed, and it is still a cross-worker write surface that no lane gate can see, because the writing worker is invoking a file it does not own.",
        "W3-S1 VERIFIED with a printed denominator over the artifact: one_pager_files counts per folder are 0 -> 40 folders, 1 -> 44, 2 -> 5, summing to 89, and the five carrying two are Imperial Brands IMB LN, Nokia FH, Petrobras PETR3 BZ, SAP GY, Total Energies TTE FP. The cell text says 'that folder's ONE PAGER.xlsx workbook' in the SINGULAR and the world has five counterexamples that DISAGREE WITH EACH OTHER on the peer-set question, so the singular phrasing does not pick out a file. The artifact's own workbook_partition (one_pager_found 49 / no_one_pager 40) confirms the same 89 from the other direction.",
        "W1-S2's CLAIM IS A 100% CLAIM AND THAT IS WHAT MAKES IT ACTIONABLE RATHER THAN ANECDOTAL: not 'some rows' but every row in the raw HistoricalDataRequest response splits the two field families. A join that silently succeeds on every row while pairing values nine months apart produces ratios that are individually plausible and collectively wrong, and nothing in the output announces it. Fiscal-year-end is a PROPERTY OF THE SECURITY, so the defect is scoped to non-December filers and will not appear in a December-heavy sample.",
        "W5-S1 IS TWO FINDINGS IN ONE ROW AND BOTH SURVIVE: (a) a list-wide reviewed_at makes the staleness signal all-or-nothing, so a partially-rotten list is indistinguishable from a fresh one until the whole list goes stale -- the coarse grain is the defect; (b) `security_key` is the join key for social_accounts.json entries and is DEFINED NOWHERE ELSE IN THIS PROJECT, resolved by the worker to AMGT-s-12 universe.json's `folder` value. An undeclared join key resolved by inference is exactly the identity-layer hazard C-S1 is about, one level out.",
        "S1 IS A DEPENDENCY-GRAPH OMISSION WITH A MEASURED CONSEQUENCE: the manifest draws no S1 -> S6 edge, yet S1's raw landing needs the store S6 creates, and that store was ABSENT at two vintages. A missing edge is not a documentation nit -- it is the reason an ordering can be chosen that cannot work, and the absence at two separate vintages is the evidence it already did.",
        "W2-S1 AND W3-S3 ARE THE TWO I AM GRADUATING AT LOW VALUE, AND I SAY SO RATHER THAN INFLATING THEM. W2-S1 is a DISCLOSED, deliberate exception to STORE_CONTRACT rule 1 (packs/<key>/status.json is unstamped where the rule forbids writing an existing path) -- correctly filed so AMGT-s-14 does not generalise the stamp convention from it; not a defect. W3-S3 reused AMGT-s-b4's own ticker selection rather than deriving an independent set, which makes its coverage a function of a sibling cell's choices -- worth knowing when reading its result, not wrong."
      ]
    },
    "spec_asserts": "The cells assert that their landed artifacts join, key and count the securities and workbooks the PRD's identity and store contracts name.",
    "world_is": "Seven statements about the landed world hold: a fiscal-year join pairs values nine months apart on non-December filers, a required re-run truncates a peer's committed deliverable by construction, 'the workbook' resolves to two disagreeing files in 5 of 89 folders, a staleness signal is list-wide, a join key is undeclared, a needed dependency edge is undrawn, and one store key departs from its contract by disclosed design.",
    "notes": "⭐ THE TWO THAT SHOULD NOT DIE WITH THIS ROUND ARE W1-S2 AND W4-S1, and for opposite reasons. W1-S2 is a SERVED-CORRECTNESS defect: it produces numbers that look right, on a path no acceptance criterion in this round examines, and it is invisible in any December-fiscal-year sample. W4-S1 is a WRITE-SURFACE defect: a cell's own acceptance criterion instructs an act that mutates another worker's landed deliverable, so the ordinary protections do not apply -- the owned-paths gate sees the invoking worker's paths, not the paths the invoked script writes. ⛔ THAT SECOND SHAPE IS WORTH GENERALISING: A TOOL'S WRITE SURFACE IS THE TOOL'S, NOT THE CALLER'S, so a criterion that tells one worker to run another's script has silently widened the first worker's write set past anything its order declares. ⚠ W4-S1 is ARMED and its condition is untouched by this round ending: the script still resolves its output from __file__.",
    "disarm_owner": "PER-ROW. W1-S2 -> AMGT-s-1's cell owner via the issuer: the join must key on the security's FISCAL period, not on the calendar year of `date`, and the fix is a correctness change to a landed artifact, not a re-render. W4-S1 -> the instrument's owner (AMGT-s-12's cell, 0.9.0_WK_AMGT_RESAPP~3's deliverable) with the issuer for the criterion that requires the re-run: scope OUTPUT_PATH to the CALLER, or have the criterion read ~3's committed output instead of regenerating it. W3-S1 -> the cell text's author (the singular 'the workbook' needs a rule for the 5 two-workbook folders, and the two disagree, so it is a RULING not a wording fix). W5-S1 -> AMGT-s-15's schema owner (per-entry reviewed_at) and whoever declares `security_key`. S1 -> the manifest's owner (draw the S1->S6 edge). W2-S1 -> nobody, it is disclosed by design; carried so AMGT-s-14 does not generalise it. W3-S3 -> read-context only. NOTHING BUILT OR APPLIED HERE."
  }
]
```

## C-S5 -- W7-S4: DISMISSED, wholly inside its author's grant and already fixed with nothing residual

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S5",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T03:05Z",
    "one_line": "DISMISSED -- the only row in this channel whose defect was fully inside its own author's grant and is already fixed with nothing residual. W7-S4 records that build_view.py's security_key derivation omitted the Bloomberg yellow key ('Equity'), so it matched NOTHING in the store even for correctly resolved names; it was INVISIBLE while the store was empty and surfaced the moment AMGT-s-1 landed real data; the worker fixed it in-session, in its own <paths>, and disclosed it. There is no remedy owed to anyone and no hazard that outlives the round, so graduating it would mint a remediation item nothing would act on.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "DISMISSED_WITH_REASON",
    "adjudicates": [
      "AMGT_RESAPP-Z-W7-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The row's own text places the defect, the fix and the write surface in one place: build_view.py is the worker's own file, inside its own <paths>, and the correction was made in-session. No other cell's artifact and no served surface is implicated.",
        "THE REASON IT WAS INVISIBLE IS THE PART WORTH KEEPING, and it is why the dismissal is of the ROW and not of the lesson: an empty store returns no matches, and a key that matches NOTHING also returns no matches. The two states are indistinguishable until real data lands. So the defect was undetectable for as long as its detector had nothing to detect against -- a criterion exercised against an empty store cannot discriminate a correct key from a broken one.",
        "DISMISSED IS THE CORRECT DISPOSITION RATHER THAN GRADUATED, on this channel's own convention: GRADUATED carries a finding forward to an owner, and there is no owner and no forward act here. The fix is landed, the paths are the author's, and the hazard cannot recur on this artifact."
      ]
    },
    "spec_asserts": "AMGT-s-7's build_view.py asserts it resolves store keys for correctly-resolved security names.",
    "world_is": "It did not, because the derivation omitted the 'Equity' yellow key; the omission was corrected in-session by the same worker within its own write surface, and no other artifact was affected.",
    "notes": "⭐ THE LESSON SURVIVES THE DISMISSAL AND IS WORTH ONE LINE: A CHECK RUN AGAINST AN EMPTY STORE CANNOT TELL A CORRECT KEY FROM A BROKEN ONE -- both return zero matches. Any criterion whose expectation is 'no mismatches' should be exercised against a store known to be NON-EMPTY, or it is an always-passes criterion wearing a sensible bar. That belongs to whoever next writes a store-matching criterion, and it is recorded here rather than routed, because the row it comes from needs no action.",
    "dismissal_reason": "The defect was real, was wholly within the surfacing worker's own declared write surface, was corrected in-session, and leaves no residual hazard, no affected peer artifact and no remedy owed by any seat. Nothing outlives the round, so there is no finding to graduate and no owner to route it to. The reusable lesson is preserved in notes rather than carried as an item."
  }
]
```

## C-S6 -- W9-S2: the AMGT-s-b4 TLS block, an HONEST fail that must not be re-cut

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S6",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T03:05Z",
    "one_line": "GRADUATES, AND IT IS THE ONE ROW WHOSE DISPOSITION IS NOT THE END OF ITS STORY: W9-S2 is the external TLS block on AMGT-s-b4. astn/brightdata/residential-proxy TLS-intercepts every HTTPS GET with an untrusted 'Bright Data Proxy Root CA' leaf no standard client can verify, so all 9 attempted GETs across 3 tickers failed AT THE HANDSHAKE, before reaching Seeking Alpha, and AC1 honestly reads 0 of 3 landed. ⭐ THE GRADE THAT MATTERS HERE IS THE ONE THE ROW ARGUES FOR AND I CONFIRM: THIS IS NOT A DEFECT IN THE ORDER'S OWN WORK. The fetcher, the detectors and the logging are sound and AC2 through AC6 all pass; the deliverable is otherwise complete and the failure is an HONEST TLS FAIL at a layer outside the cell's write surface. An externally-blocked criterion that reports its own blockage accurately is behaving correctly -- it is the one shape of failure that should NOT be re-cut.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "adjudicates": [
      "AMGT_RESAPP-Z-W9-S2"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE FAILURE LAYER IS NAMED AND IT IS BELOW THE CELL: the handshake fails on an untrusted re-signing root, so no request ever reaches Seeking Alpha. Nothing the fetcher could do differently changes that, and the row does not ask for a workaround -- notably it does NOT propose disabling verification, which would have converted an honest block into a silent trust defect.",
        "THE CELL'S OWN WORK IS EVIDENCED SEPARATELY FROM THE BLOCK: AC2 through AC6 pass, which is what distinguishes 'the order failed' from 'the world refused'. A row that could not make that distinction would leave the cell's quality unknown.",
        "THE GATE THIS ROW SITS ON IS NOT THIS SEAT'S, and 1.0.0_SA_CTO~Z stated the two paths in msg 21143: either the proxy path is resolved and s-b4 re-runs to completion, or a ruling makes its externally-blocked state terminal for the round with FWD-4's Seeking-Alpha half graded NOT_REALIZED/blocked. Both are above L9. 4.0.0_SA_CRO~Z has separately proven the SA auth mechanism live, which bears on the first path.",
        "L8 AND L9 EXPRESSLY DO NOT WAIT ON IT (21143), and they have not: this row is dispositioned here with the other 23. Only L10 waits, because a slug needs every task order terminal."
      ]
    },
    "spec_asserts": "AMGT-s-b4's AC1 asserts that a stated number of Seeking Alpha documents land via the configured proxy.",
    "world_is": "Zero landed, because the proxy TLS-intercepts with an unverifiable root and every handshake fails before the request is made; the cell's fetcher, detectors and logging are sound and AC2-AC6 pass.",
    "notes": "⛔ ARMED, AND DELIBERATELY SO: the proxy's interception is a live condition on a live dependency, and it does not become inert because this round dispositioned the row. ⚠ WHAT THIS ROW MUST NOT BE READ AS: a reason to re-cut AMGT-s-b4's fetcher. The distinction between a criterion that FAILED and a criterion that was PREVENTED is the whole content of this disposition, and collapsing the two would send a worker to rebuild something that already works. ⭐ AND THE HONEST-FAIL SHAPE DESERVES ITS NAME ALONGSIDE THE ALWAYS-FAILS AND ALWAYS-PASSES SHAPES IN C-S2: a criterion that CAN discriminate, DID discriminate, and reported a true negative about the world is the one failure that is working as designed.",
    "disarm_owner": "1.0.0_SA_CTO~Z with ANDREW, per 21143 -- and it is NOT this seat's at any limb. Either the Bright Data proxy path is resolved (a trust-store or egress-route decision, plus the SA route and terms which are Andrew's standing domain, C-SA-UNMEASURED) and s-b4 re-runs, or a ruling makes the externally-blocked state terminal for round 1 with FWD-4's Seeking-Alpha half graded NOT_REALIZED/blocked. This seat will have s-b4's disposition before it is needed for the L10 slug and is not waiting on it for L9."
  }
]
```

## C-S7 -- THE ROUND'S 16 JUDGMENT GRADES: 13 PASS / 2 FAIL / 1 NOT_EVALUATED, and the L9 limb this seat had reported discharged was incomplete until here

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S7",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T04:40Z",
    "one_line": "THE ROUND'S SIXTEEN JUDGMENT GRADES -- 13 PASS, 2 FAIL, 1 NOT_EVALUATED -- and my own L9 was INCOMPLETE until this row. Every one of the 16 orders reserves exactly one judgment criterion to this seat; all 16 arrived correctly marked UNVERIFIABLE-BY-INSTRUMENT naming this seat as substitute oracle; NONE was graded when I reported L9 discharged at @d98b82113b, and I corrected that to 1.0.0_SA_CTO~Z before cutting any slug. ⛔ THE TWO FAILS ARE BOTH GATES ON SERVED SURFACES AND BOTH WERE SURFACED BY THEIR OWN ASSIGNEES: AMGT-s-10 AC6 -- '12345 [PROVISIONAL]' is skimmed as 'a number, fine', so the held-back rule is present in the data and absent in the reading; AMGT-s-15 AC6 -- the official-vs-impostor test is a bare OR of three checks, so an impostor need only beat the weakest, and a copied bio line alone admits. AMGT-s-4 AC7 is NOT_EVALUATED because its bar names 'one security that had SA raw landed' and zero had at its vintage -- and SA raw HAS landed since, so it is newly exercisable rather than defective. The 13 passes include three claims PROVEN rather than asserted: AMGT-s-12's byte-identical twice-run determinism control, AMGT-s-8's four-case reproduction of its comparability test, and AMGT-s-9's closed three-transformation normalisation.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disposition": "GRADUATED",
    "grades": [
      {
        "criterion": "AMGTs1-AC8",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/AMGT_RESAPP.TO-AMGT-s-1.model-block-bloomberg-covered-name.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "BOTH LIMBS MET. LIMB 1 (could an analyst answer 'where from, on what basis, as of when' from the record alone): YES on a named ADR figure -- BABA US Equity FY2025 EBITDA_ADJUSTED 209364.0, unit MILLIONS, sign POSITIVE, basis {mnemonic, Bloomberg's-own-definition}, vintage, source bloomberg-dapi. LIMB 2 (is a differing unit carried as a PER-SECURITY fact rather than smoothed): YES -- field_map.json carries 0 unit-family divergences across the three securities, and the one real divergence found (a currency/basis difference on the ADR) is recorded in per_security_detail + cross_security_findings[0] AND propagated into every affected figure. ⭐ WHAT LIFTS THIS ABOVE A BARE PASS: the record DISCLOSES what it cannot resolve (which currency the MILLIONS figure is denominated in) through an explicit currency_caveat rather than shipping a bare number. A figure that names its own unresolved dimension is answerable; one that hides it is not, and the bar is about answerability."
      },
      {
        "criterion": "AMGTs2-AC7",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/AMGT_RESAPP.TO-AMGT-s-2.on-demand-pull-the-seam-design-then-build.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "PASS ON THE BAR AS WRITTEN, AND THE BAR'S OWN WORRY IS LIVE ON A ROUTE IT DOES NOT NAME -- both halves stated because the second is the useful one. THE NAMED SCENARIO IS HANDLED: bloomberg_health() runs BEFORE every pull and on ok:False writes packs/<key>/status.json {state: FAILED, reason: 'terminal signed out (bloomberg_health ok=False): <error>'} then deletes the SQS message -- so the analyst who submits while the terminal is signed out sees REQUESTED -> FAILED with a human-readable reason. A MARKED failure, which is exactly what the bar asks for, and 'honest about its latency' is met by SEAM_DESIGN s.6's measured 7.6s/7.7s stated as conditional on a consumer running. ⚠ BUT THE ASSIGNEE DISCLOSED A SECOND INPUT THE BAR DOES NOT ENUMERATE AND IT PRODUCES PRECISELY THE ANTI-PATTERN THE BAR FEARS: with NO consumer running at all (the poller is person-started, never a persistent service) a request sits at REQUESTED indefinitely, no FAILED/timeout is ever written, and status.json cannot distinguish 'about to be picked up' from 'no consumer will ever run' -- i.e. a page that looks like it is still fetching an hour later. I grade PASS because the criterion's subject is the SIGNED-OUT path and because 'honest about its failure modes' is satisfied by disclosure, not by having none. The gap GRADUATES as a finding rather than lowering this grade, and the assignee earned the pass by naming it instead of leaving it to be found in production."
      },
      {
        "criterion": "AMGTs3-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/AMGT_RESAPP.TO-AMGT-s-3.provenance-face-beside-every-figure.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET, AND THE INTERESTING CASE IS THE ONE THAT MARKS ITSELF. IS_DIV_PER_SHR on the same mnemonic across three securities: SAP and BABA render fully self-sufficient lines ('<value> PER SHARE (local trading/reporting currency) ... IS_DIV_PER_SHR (Dividend per share.) ... as of <vintage> ... Bloomberg') -- an analyst answers basis and as-of without a spreadsheet. BA US Equity renders '[UNRESOLVED UNIT]' on all ten fiscal years, and THAT IS THE CORRECT BEHAVIOUR FOR THE BAR: the line still answers source and vintage, withholds only the per-share unit, and provenance_session_log.md names the root cause. A marked value, never a blank and never a guess. ⛔ THE ROOT CAUSE IS A REAL UPSTREAM DEFECT AND I AM NAMING IT RATHER THAN LETTING THE PASS ABSORB IT: AMGT-s-1's field map classified Boeing's unit from its MOST RECENT fiscal year, which is post-dividend-suspension and zero-valued, and the resulting status applies PER-SECURITY rather than per-fiscal-year -- so one unrepresentative sampled year marks ten years of real dividends unresolved. Sampling the latest period to classify a unit fails exactly on securities whose latest period is atypical. That belongs to AMGT-s-1's map, not to this cell, and this cell's rendering of it is right."
      },
      {
        "criterion": "AMGTs4-AC7",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/AMGT_RESAPP.TO-AMGT-s-4.coverage-reader-non-sa-sources.proof_of_spec.json@ddd368a713",
        "verdict": "NOT_EVALUATED",
        "reason": "⛔ I CANNOT GRADE THIS AGAINST ITS OWN BAR, AND SAYING SO IS THE HONEST OUTPUT RATHER THAN CONVERTING AN ABSENT INPUT INTO A VERDICT. The bar opens 'for one security THAT HAD SA RAW LANDED'. At the graded vintage ZERO securities had: run_summary.json records sa_raw_keys_found 0, because AMGT-s-b4 was proxy-blocked at the TLS layer (row AMGT_RESAPP-Z-W9-S2). So the bar's own precondition did not exist and the population it names was empty. WHAT THE ASSIGNEE DID INSTEAD IS SOUND AND IS NOT WHAT THIS CRITERION ASKS: it ranked the non-SA corpus and the ordering is defensible -- a Reuters item dated 2026-09-08 (PROVISIONAL, 3 mentions) ranks ABOVE a Bloomberg sector roundup dated 2026-09-01 (REFUSE, 10 mentions), so recency beats mention-count, matching 'most recent' first; both non-PASS reasons are specific and actionable without opening the source; the ir-class absence is not silent (identity_dropped names ir_domain and quotes render_together's refusal verbatim); and the SA half is stated absent-with-reason rather than invented. On a non-SA population I would grade that PASS. ⭐ AND THE OPERATIVE POINT FOR THE ROUND: SA RAW HAS NOW LANDED. AMGT-s-b4's re-run put 18 raw objects across 3 tickers in S3 at 2026-09-11T04:02Z, so this criterion IS NOW EXERCISABLE and was not when it was answered. It should be re-run against the landed SA data -- a round-2 item, not a defect in this cell. A criterion whose precondition arrives AFTER it is answered needs re-exercising, not re-writing."
      },
      {
        "criterion": "AMGTs5-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/AMGT_RESAPP.TO-AMGT-s-5.print-renderer-design-spec-then-adams-artifact.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET ON BOTH LIMBS, AND THE FIRST LIMB'S DISJUNCTION IS ANSWERED BY REJECTING BOTH HORNS, WHICH IS THE RIGHT ANSWER. The bar asks: would Adam forward this unreformatted, OR does it read as a screenshot of a dashboard? The render is NEITHER -- it is a DOCUMENT (same section labels, same order, own page per block, no UI chrome) carrying the honest skeleton, with every analyst-authored block marked [MACHINE-EMPTY] where the real pack holds ~9,000 characters of prose, bio and custom analysis. The operative half of that disjunction is 'dashboard screenshot', and it is decisively not one. NOT-YET-FORWARDABLE IS NOT A FAILURE HERE: the pack's substance is analyst-authored, so no renderer could supply it, and marking those blocks empty is the only honest option available -- inventing prose to make it forwardable is the failure this bar exists to prevent. ⭐ AND ONE MEASURED PLACE IT BEATS THE REAL PACK: page 1's model block carries MORE per-figure provenance (unit, mnemonic, Bloomberg definition, vintage, source) than the real pack's own bare financial-summary table. LIMB 2 (does the spec say, per surface, what shows when that surface is NOT there): YES, 15 of 15 DESIGN_SPEC sections name an UNRESOLVED/FAILED/HELD-BACK or stated-absence behaviour, cited per surface."
      },
      {
        "criterion": "AMGTs6-AC7",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~7/AMGT_RESAPP.TO-AMGT-s-6.version-store-opal-data-research.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET, AND ON THE STRONGER FORM OF EACH NAMED PROPERTY. The bar's test is whether STORE_CONTRACT.md lets AMGT-s-1 land raw bytes and AMGT-s-14 render last-run/outcome/re-run WITHOUT ASKING ANYONE. All four named rules are stated: raw-before-derived (s.1, and made STRUCTURAL rather than conventional -- a derived/packs writer reads an existing raw/ key as its input, so there is nothing to derive from until raw/ exists, which is a property no one can forget); a stamp per write (s.3, pinned to UTC-at-write-start rather than the vendor as_of, mirroring the OPAL_ASSETS run_date-vs-as_of lesson, with >=1 stamp per stage answering AMGT-s-14's own 'a single refresh under one timestamp is a violation' bar); never write to an existing path (s.4, with versioning named as the safety net and NOT the mechanism); and the latest stamp as the read (s.4, the lexicographically-greatest stamp, computable from list-objects-v2 --delimiter / CommonPrefixes with NO index or pointer file -- so the read needs no second artifact anyone could forget to update). s.2 pins security_key to AMGT-s-12's identity layer, identical across all three prefixes, and states explicitly that a vendor's own id (sa_id, CIK, CUSIP) is never the key. ⭐ s.5 answers AMGT-s-14's four questions CONCRETELY -- source, last run, outcome, re-run-alone -- which is the actual 'without asking anyone' test, and the assignee notes it went past the order's literal item (b) to do it."
      },
      {
        "criterion": "AMGTs7-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~7/AMGT_RESAPP.TO-AMGT-s-7.coverage-freshness-view-one-place.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET ON BOTH LIMBS, with one readability consequence recorded. LIMB 1 (would Adam find the stalest name in one glance without opening a folder): the sort rule is explicit in SPEC_SECTION_freshness.md s.2 -- ascending by last_refreshed with NEVER sorted to the TOP -- so the first row a reader's eye reaches is always the stalest or the first NEVER. No scan, search or filter. LIMB 2 (does a NEVER read as 'never researched' rather than as an error): YES, and by construction -- s.3 puts NEVER in the SAME list, SAME columns, SAME sort participation, explicitly NOT a separate section, blank, dash or omission, which makes C-MARK-NOT-DEGRADE a rendering rule instead of an intention. s.6 extends it to the 41-of-89 security_key=null rows. s.4 keeps the rot signal in the same row and column as the date. ⚠ ONE CONSEQUENCE OF THE SORT, recorded and not a failure: with 41 of 89 rows holding NEVER and NEVER sorted to the top, the stalest RESEARCHED name is around row 42, and 41 visually identical NEVER rows precede it. The spec's choice to treat NEVER as stalest is coherent and defensible -- a never-researched name does need attention most -- but 'one glance' degrades as the NEVER block grows, and it will shrink only as coverage lands. Worth a look when the ordering is built. ⭐ And s.7 states the single generated_at caption as the ONLY page-level freshness signal, explicitly not implying anything runs on its own, which is the correct posture under this estate's monitor moratorium."
      },
      {
        "criterion": "AMGTs8-AC7",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/AMGT_RESAPP.TO-AMGT-s-8.peer-set-comparable-or-absent-with-a-reason.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET, AND LIMB 2 IS PROVEN RATHER THAN ASSERTED, which is unusual and worth the pass on its own. LIMB 1 (is the reason one an analyst would accept rather than a blank): YES -- the absent record carries basis 'absent', members [], a vintage, and a reason that names WHY ('candidate universe not classified; a quota decision (F2) precedes derivation'), plus the fact that the subject's OWN GICS_SECTOR_NAME is known ('Consumer Discretionary') while no other covered name has been classified by that field, so no candidate can be tested. That is a reader-actionable absence, not a gap. LIMB 2 (is the comparability test stated precisely enough that a second engineer would derive the same set): DEMONSTRATED, not claimed -- the test is two named parameters (same GICS_SECTOR_NAME AND a market-cap band within 0.2x-5.0x of CUR_MKT_CAP), and the assignee RAN it against a synthetic classified universe with four discriminating cases: PDD US included (same sector, 0.556x), JD US excluded (same sector but 0.148x, outside the band), BA US excluded (different sector), TOOSMALL US excluded (0.0037x). Two of the four exclusions turn on the cap band alone, so the band is load bearing and exercised in both directions. ⭐ AND IT DECLARES ITS OWN CEILING: GICS_SECTOR_NAME is the finest classification field AMGT-s-1's landed record carries, a true subgroup field was not mapped at this cut, and the record says re-derive the day one lands."
      },
      {
        "criterion": "AMGTs9-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/AMGT_RESAPP.TO-AMGT-s-9.drafting-face-marked-beside-its-evidence.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET ON BOTH LIMBS, and limb 2 carries a real negative control. LIMB 1 (is the drafted sentence unmistakably a machine's starting point rather than the firm's view): YES. The shipped sentence is 'Recent coverage notes that \"revenue growth as AI demand accelerates\" (Reuters).' The lead-in hedges the claim to the source, and the assignee states the contrast that makes it testable rather than stylistic -- a firm view would read 'Alibaba's cloud revenue accelerated', asserting in the firm's own voice. The quoted span is verbatim from the Reuters item's own title, with the evidence id carried beside it. LIMB 2 (is the verbatim normalisation tight enough that a near-quote could not slip through as verbatim): YES, and this is the strong part. The normalisation is CLOSED and enumerated -- exactly three transformations (curly-quote straightening, casefold, whitespace collapse) 'and nothing else' -- so its admit set is bounded by construction. Both arms are exercised: a case/whitespace variant and a curly-quote source both ADMIT, a genuine paraphrase REFUSES, and a mutant control backs it. ⭐ THE ARGUMENT IS STRUCTURAL, NOT EMPIRICAL: a paraphrase uses different words, and none of the three named transformations can turn different words into a substring match -- so refusal follows from the closure of the transformation set, not from having tested enough paraphrases."
      },
      {
        "criterion": "AMGTs10-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/AMGT_RESAPP.TO-AMGT-s-10.check-face-pass-fail-provisional-per-figure.proof_of_spec.json@ddd368a713",
        "verdict": "FAIL",
        "reason": "⛔ FAILS ON LIMB 2, AND THE ASSIGNEE'S OWN EVIDENCE IS WHAT FAILS IT. I am not softening this because the disclosure was exemplary -- honesty earns an accurate grade, not a pass. LIMB 1 PASSES DECISIVELY: a REFUSE renders as bracketed text WHERE A NUMBER WOULD BE ('[REFUSED: EBITDA_FIXTURE: unit/sign convention is 'INFERRED', not MEASURED]'), so a scanning analyst sees a broken-looking cell and a REFUSE cannot be mistaken for a value at all. LIMB 2 ASKS whether the real blocks' PROVISIONAL figures read as 'not yet checked' rather than as 'fine', AND THE MEASURED ANSWER IS NO: '12345 [PROVISIONAL]' keeps the number as the dominant text in the cell, and the assignee states plainly that AT A GLANCE 'a PROVISIONAL row is more likely to be skimmed as \"a number, fine\" than a REFUSE row is to be mistaken for one'. That is the bar's failure condition in the bar's own words. THE CAUSE IS NAMED AND THE REMEDY IS ALREADY SCOPED: bracket text alone is not equally salient to a REFUSE bracket, and SPEC_SECTION_checkface.md says the eventual .tsx needs a DIFFERENT visual marker (colour or icon) for PROVISIONAL -- a deferred design decision this cell's plaintext render could not supply. ⚠ WHY THIS MATTERS RATHER THAN BEING A COSMETIC NIT: PROVISIONAL exists to stop an unchecked figure being read as checked. A marker that is skimmed as 'fine' does not do that, so the held-back rule is present in the data and absent in the reading -- the number ships looking checked. This grade is a GATE on the check-face surface: the visual marker lands before the .tsx serves PROVISIONAL figures to an analyst."
      },
      {
        "criterion": "AMGTs11-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~8/AMGT_RESAPP.TO-AMGT-s-11.qualification-rules-six-classes.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET ON BOTH LIMBS, with the assignee's own calibration accepted. LIMB 1 (are the six refusal inputs REAL rather than strawmen): YES in substance -- figure traces to 8 Bloomberg mnemonics tested against FactSet's 2.65 with none reproducing it; peer to ASML NA's own CSC sheet MEASURED carrying the full 12-ticker KPN telecom set verbatim; identity to the T CN (Telus) / T US (AT&T) collision with BOTH tickers present in the same corpus's own KPN peer set, a real same-symbol/different-company case; sentence to a paraphrase of the field map's own s.5 sentence, differing only in wording, which is precisely the shape C-VERBATIM-GATE exists to catch. ⭐ AND IT DECLARES ITS WEAKEST LINK RATHER THAN LETTING ME FIND IT: item's headline and source's aggregator domain are CONSTRUCTED shapes over a MEASURED pattern, not measured instances, because this cell has no word to fetch content (G-24). A constructed instance of a measured trap is not a strawman -- the trap is real and only the specimen is synthetic -- and saying which is which is what separates calibration from over-claiming. LIMB 2 (is the peer threshold's drawing rule one a reader would draw the same way): YES for the RULE. The histogram's populated bins are {0:4, 8:7, 12:41} with an empty run 1..7, the threshold 4 is stated as the gap's MIDPOINT, and the drawing_rule field says so -- so a reader given that rule reproduces 4. The assignee adds that ANY value in 1..8 partitions the clusters identically, so 4 is defensible rather than unique. That is a property of an empty gap, not a defect in the rule, and the bar asks about the rule."
      },
      {
        "criterion": "AMGTs12-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/AMGT_RESAPP.TO-AMGT-s-12.identity-layer-the-root.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET ON BOTH LIMBS, and limb 2 is the best-controlled reproducibility claim in this round. LIMB 1 (does the deliverable say, plainly and PER KEY, what it could not resolve and why): YES, key by key -- bloomberg_ticker is MEASURED-or-UNRESOLVED with workbook path plus sheet/cell evidence and NEVER from the folder name; sa_symbol is INFERRED only for US names via a stated ticker-root rule with the rule and input named, UNRESOLVED everywhere else and never MEASURED; ir_domain and social_account are UNRESOLVED everywhere with evidence naming the missing vendor word (G-24). ⭐ AND AMENDMENT 1 IS THE HONEST HANDLING OF THE DEFECT I VERIFIED SEPARATELY AT C-S1: a MEASURED candidate that turns out to be a template placeholder shared by 2+ folders is downgraded to UNRESOLVED **with the shared value recorded and the sibling folders named** -- so a reader can see what was removed and why, which is what makes the downgrade auditable instead of a silent number change. LIMB 2 (would a re-run at the same vintage get the same partition): PROVEN, not asserted -- build_universe.py and f6_remeasure.py read only the live corpus with no fixtures, print their own vintage (corpus_root_mtime, read_started_at/read_finished_at) beside every count, and were run TWICE both pre- and post-fix, BYTE-IDENTICAL after masking timestamps. A determinism control with the timestamps masked is the right instrument: it separates genuine non-determinism from the clock, which a naive re-run conflates."
      },
      {
        "criterion": "AMGTs13-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~6/AMGT_RESAPP.TO-AMGT-s-13.social-feed-measure-then-build.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "PASS ON THE OPERATIVE LIMB, and the bar's literal phrasing conflicts with its own order -- both stated. THE BAR ASKS whether the next worker could get all five observables in one call OR WOULD HAVE TO RE-PLAN. The answer to the operative clause is NO RE-PLANNING IS NEEDED: DATASET_IDS, FIRST_RUN_DATASET_ID, FIRST_RUN_COMPANY, QUERY_ATTEMPTS with its STOP_RULE, OBSERVABLES, COST_CAP_USD with cost_cap_exceeded(), CANNOT_SERVE_SIGNAL and FOURTH_SURFACE_NOTE are all module-level data that compose_request() already reads, and main() already accepts --word-record and clears the G-24 gate. The plan is complete and reusable as it stands. ⚠ BUT THE FIVE OBSERVABLES CANNOT BE OBTAINED IN ONE CALL, BY DESIGN: past the word-record gate main() composes the request, PRINTS it and returns 4 -- it sends nothing and computes no observable, because no HTTP client exists in this module, and AC4 of this same order DELIBERATELY excluded one. So the bar's literal first clause is unsatisfiable by any build that obeys AC4 of its own order. I grade on the re-plan clause because grading on the literal clause would penalise the assignee for obeying its own order -- the always-fails shape, one criterion removed. THE CRITERION SHOULD BE RE-CUT to ask what it means: is the plan complete enough that the next step is a build and not a re-think. ⚠ LIMB 2 (does the stop rule prevent a second trigger on 'cannot serve the feed'): STOP_RULE and CANNOT_SERVE_SIGNAL are present as module-level data, but nothing exercises them, so limb 2 rests on DECLARATION rather than on an exercised arm. Recorded as a thinner limb inside a pass, not as a separate failure -- there is no client to exercise it against yet."
      },
      {
        "criterion": "AMGTs14-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~7/AMGT_RESAPP.TO-AMGT-s-14.input-ledger-per-class-rerun-alone.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET ON BOTH LIMBS, and the assignee closed a real two-state ambiguity rather than shipping past it. LIMB 1 (could an analyst tell, per input class, where it came from, when it last ran and whether it worked): YES on the exercised security -- SAP_GY_Equity's market_data row reads source bloomberg, last run 20260911T010951Z, outcome OK, which is all three facts in one row. LIMB 2 (would the four classes with no stage read as 'not wired' rather than as 'fine'): YES -- CLASSES[cls]['stage'] is None for filings, news, social and web, and SPEC_SECTION_ledger.md s.2 names those explicitly as NOT WIRED with no re-run control drawn. ⭐ THE PART THAT EARNS THE PASS IS A THIRD STATE THE BAR DOES NOT ASK FOR AND THE ASSIGNEE FOUND ANYWAY: 'sa' has a stage REGISTERED (this order's own retrofit) but no entry for this security, so read_ledger() alone returns nothing for it -- BY ITSELF INDISTINGUISHABLE from a class with no stage at all. Left there, a wired-but-never-run class would have rendered as 'not wired', which is wrong in a way that hides an available control. s.2 closes it by naming a SECOND fact the page must check (stage is not None) so the three states separate: 'ran and worked', 'wired but never run', and 'not wired'. A single read that cannot distinguish two states needs a second fact, not a better label."
      },
      {
        "criterion": "AMGTs15-AC6",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/AMGT_RESAPP.TO-AMGT-s-15.list-register-owned-lists-with-a-rot-signal.proof_of_spec.json@ddd368a713",
        "verdict": "FAIL",
        "reason": "⛔ FAILS ON LIMB 1, on the assignee's own declared weakest link, and the failure is structural rather than a matter of degree. THE BAR ASKS whether the official-vs-impostor test 'would ACTUALLY separate a fan account from the company's own'. THE TEST IS AN **OR** OF THREE CHECKS: (1) the company's own measured web presence links the account by exact URL; (2) the platform's verification mark is present; (3) the account's bio names the company's registered domain. It does clear the TRIVIAL case -- a same-name parody with no cross-link, no mark and a bio naming nothing satisfies none of the three and is correctly excluded, which a bare name-match would not do. ⛔ BUT BECAUSE THE COMPOSITION IS A BARE OR, CHECK (3) ALONE ADMITS, AND CHECK (3) IS CHEAPLY GAMEABLE: an impostor copies the same 'official account of <domain>' bio text a real account carries and is ADMITTED on that basis, with no requirement that (3) co-occur with (1) or (2). The assignee states this outright and also that check (2) is weaker than it reads, a paid verification mark having been decoupled from identity verification on at least one major platform since 2023. So an impostor needs to beat only the WEAKEST of three checks, and two of the three are individually beatable. ⚠ THE OR IS THE DEFECT, NOT THE CHECKS: three weak-to-strong signals combined by OR are exactly as strong as the weakest one, which inverts the intent of listing three. THE REMEDY IS SHAPE-LEVEL AND ONE CLAUSE: require (3) to CO-OCCUR with (1) or (2) -- an AND against a strong check -- so a copied bio alone cannot admit. This is a GATE: the surface names real companies' social accounts, and admitting an impostor there misattributes a third party's statements to a client. Grading PASS because the trivial case works would certify a test its own author says lets impostors through."
      },
      {
        "criterion": "AMGTsb4-AC7",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~9/AMGT_RESAPP.TO-AMGT-s-b4.seeking-alpha-backend-the-measured-route.proof_of_spec.json@ddd368a713",
        "verdict": "PASS",
        "reason": "MET ON BOTH LIMBS ON REAL LANDED DATA, graded against the RE-RUN rather than the proxy-blocked original. LIMB 1 (does the ETL preserve createdAt and previousReportDate untouched): CONFIRMED, and structurally rather than by observation alone -- the landed BABA report (raw/seekingalpha/BABA_US/20260911T040214Z/report.json, read back DIRECTLY FROM S3 by the worker rather than from its own buffer) carries createdAt 2026-09-08T00:00:22.351-04:00 and previousReportDate 2026-09-03T00:01:14.183-04:00, both present and dated, because land_raw writes response.content BYTE-FOR-BYTE -- so nothing in the shipped code ever had an opportunity to reshape them. A preservation claim backed by 'there is no code path that could alter this' is stronger than one backed by a matching read. ⭐ LIMB 2 (does the deliverable state plainly which of C-SA-UNMEASURED's five limits this run could and could not observe): YES, and with five DIFFERENTIATED statuses rather than one hedge -- (1) session TTL PARTIALLY OBSERVED and still not bounded, with the new data point stated precisely (a jar captured 02:13:39Z served 18 calls ~1h49m later, past the original ~30-minute window, never pushed to failure); (2) headless harvest NOT APPLICABLE; (3) MFA NOT APPLICABLE; (4) rate limits 18 calls at min gap 2.71s with zero rate-limit signals, explicitly STILL NOT A BOUND and terms still unread; (5) the has_paid_subscription gate STILL NOT OBSERVED, because both articles fetched read isPaywalled=False and isLockedPro=False, the same free shape. Each limit says what moved, what did not, and what remains unbounded -- an unmeasured boundary reported as unmeasured."
      }
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CENSUS THAT FOUND THE GAP, and it is the reason this row exists: a regex over all 16 orders for criterion tags returns 104 criteria of which 16 carry judgment=\"true\" -- exactly one per order, every one naming 3.0.0_SA_CVO. A scan of BOTH channel planes (30 rows) for a `grades` field returned ZERO. So 16 of 16 were ungraded at the moment three seats agreed the L10 precondition was met.",
        "WHY THE PRECONDITION READ AS MET: it has THREE clauses -- every task order terminal, every channel row dispositioned, every judgment criterion graded -- and three seats checked the first two. Both were true (16 of 16 orders terminal on an independent full-pair status read, occ=1 each, 0 multi-value conflicts; 24 items, 0 open). The third was invisible to all three of us because none looked at it, and the agreement of three seats made the belief stronger rather than weaker. A three-clause precondition checked on two reads exactly like one that is met.",
        "EVERY GRADE IS AGAINST THE CRITERION'S OWN BAR, quoted from its order's explainer bullet, and against the assignee's assembled evidence in its proof instance at @ddd368a713 -- all 16 instances verified present at that commit before grading (git cat-file -e, 16 of 16, 0 missing).",
        "THE TWO FAILS REST ON THE ASSIGNEES' OWN WORDS, not on a stricter reading imposed here. AMGT-s-10's instance states that at a glance a PROVISIONAL row 'is more likely to be skimmed as \"a number, fine\"' -- which is the bar's failure condition verbatim. AMGT-s-15's instance declares check (3) 'CHEAPLY GAMEABLE' and states the test 'admits it on that basis alone, with no requirement that (3) co-occur with (1) or (2)'. In both cases the assignee built carefully, measured honestly, and reported the limit; the grade follows the measurement.",
        "AMGT-s-4's NOT_EVALUATED is an absent PRECONDITION, not an absent artifact: run_summary.json records sa_raw_keys_found 0 at its vintage because AMGT-s-b4 was TLS-blocked (row Z-W9-S2), so the population its bar names ('one security that had SA raw landed') was empty. Converting that into a PASS or a FAIL would convert an instrument's limit into a verdict. The re-run has since landed 18 raw objects across 3 tickers at 2026-09-11T04:02Z, so it is now exercisable.",
        "NOTHING IN C-S1..C-S6 IS DISTURBED BY THIS ROW. The 24 row dispositions stand, the L8 compile stands, and the channel still reads 24 items / 0 open / 0 defects / 0 malformed. What changes is that L9 is now actually complete on both of its obligations rather than on one."
      ]
    },
    "spec_asserts": "Rule 27 L9 reserves JUDGMENT criteria to the CVO and forbids self-grading, and the L10 slug's precondition is that every task order is terminal, every channel row dispositioned, AND every judgment criterion graded.",
    "world_is": "All 16 orders reserve one judgment criterion each to this seat, all 16 were correctly handed over as UNVERIFIABLE-BY-INSTRUMENT, and none was graded until this row -- while this seat had already reported L9 discharged. They are now graded 13 PASS / 2 FAIL / 1 NOT_EVALUATED.",
    "notes": "⭐ THE LESSON I AM KEEPING, and it is about my own limb rather than anyone's artifact: A PRECONDITION WITH THREE CLAUSES, CHECKED ON TWO, IS INDISTINGUISHABLE FROM ONE THAT IS MET -- and I carried 'L9 discharged' forward from the half I had actually finished. What caught it was not review but ENUMERATION: preparing to cut the slug forced me to list what a slug requires, and the third clause appeared. An earlier self-report is the weakest evidence in the room, including when it is mine. ⛔ AND THE TWO FAILS SHARE A SHAPE WORTH CARRYING: in both, the DATA is right and the READING is wrong. AMGT-s-10 marks PROVISIONAL correctly in the record and renders it so it is skimmed as fine; AMGT-s-15 collects three identity signals and combines them so the weakest governs. Neither is a build defect and neither would be caught by a mechanical criterion -- which is exactly why these were cut as judgment criteria, and why grading them mechanically would have passed both. ⚠ THIS ROW IS ARMED: both FAILs name live conditions on surfaces that will serve analysts, and neither is disarmed by the round closing. This row clears the second L9 obligation; the L10 slug and its remediation rows follow as a separate act. ⚠ ONE CARRIER NOTE, DISCLOSED BECAUSE I HAD TO TRANSFORM A VALUE TO LAND THIS ROW: the grades schema pins `criterion` to ^[A-Za-z0-9]+-AC[0-9]+$, a COMPOUND form, while this project's orders carry a BARE id (`<criterion id=\"AC6\" cell_refs=\"AMGT-s-12\">`) and its proof instances carry the same bare `AC6`. So the schema's PATTERN contradicts its own DESCRIPTION, which says to use \"the same string the proof-of-spec instance's acceptance row carries\". NFRA_OPSEC202609 never hit this because its orders name criteria compound natively (S10D-AC2, S4-AC10) -- the pattern was written to one project's convention and cannot express another's. I did NOT relax the check: every `criterion` below is minted deterministically as cell_refs-with-non-alphanumerics-stripped + the bare id, so AMGT-s-12 AC6 becomes AMGTs12-AC6, reversible by inspection and unique per cell. **The values are MINE, not the order's**, and a reader matching them back to an instance must strip the prefix. Routed to the schema's owner as a carrier defect: a criterion-id pattern keyed on one project's naming covers only that project.",
    "disarm_owner": "PER-FINDING, and NONE is disarmed by this round closing. ⛔ AMGT-s-10 AC6 (FAIL) -> the check-face surface's builder at the .tsx, via the issuer 2.0.0_SA_COO~ZZZ: SPEC_SECTION_checkface.md already scopes the remedy (a colour/icon marker for PROVISIONAL, distinct from a REFUSE bracket). THIS IS A GATE, not a backlog item -- it lands before the .tsx serves PROVISIONAL figures to an analyst, because until it does an unchecked figure reads as checked. ⛔ AMGT-s-15 AC6 (FAIL) -> AMGT-s-15's schema owner via the issuer: change the official-vs-impostor composition from a bare OR of three checks to requiring check (3) (bio names the registered domain) to CO-OCCUR with (1) or (2). One clause. A GATE on any surface that publishes a company's social account, since admitting an impostor misattributes a third party's statements to a client. AMGT-s-4 AC7 (NOT_EVALUATED) -> the issuer, as a ROUND-2 RE-RUN and not a re-cut: its bar's precondition (a security with SA raw landed) now exists after AMGT-s-b4's re-run landed 18 objects across 3 tickers at 2026-09-11T04:02Z. AMGT-s-3's upstream cause (inside a PASS, so it would otherwise be absorbed) -> AMGT-s-1's field-map owner: the unit was classified from Boeing's MOST RECENT fiscal year, which is post-dividend-suspension and zero-valued, and the status applies per-security, so one atypical sampled year marks ten years of real dividends UNRESOLVED. Sample selection, not rendering. AMGT-s-2's no-consumer gap (inside a PASS) -> whichever cell next operationalises the poller: with no consumer running a request sits at REQUESTED forever with no FAILED/timeout, which is the very 'still fetching an hour later' shape that criterion exists to forbid. No monitor is implied -- G-20 forbids one -- a status TIMEOUT state is the shape. THE CARRIER DEFECT -> 1.0.0_SA_CTO~Z as the schema's owner: the grades `criterion` pattern ^[A-Za-z0-9]+-AC[0-9]+$ cannot express this project's bare-AC ids and contradicts its own description. NOTHING IS BUILT, CHOSEN OR APPLIED BY THIS ROW."
  }
]
```
