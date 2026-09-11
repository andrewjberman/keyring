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
