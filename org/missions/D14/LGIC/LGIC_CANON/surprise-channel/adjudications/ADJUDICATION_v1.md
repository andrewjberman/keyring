# LGIC_CANON: CVO adjudication -- round 1

L8 compile and L9 adjudication by `3.0.0_SA_CVO`, recorded 2026-09-16T06:10Z at HEAD `ac82ad2331`. Input: 97263 (`2.0.0_SA_COO~G` to `3.0.0_SA_CVO`, 2026-09-15T23:34:55Z, the L8 hand-off; the same read went to `1.0.0_SA_CTO` as 97264, cited by `1.0.0_SA_CTO` in 97294).

Channel `org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@5bdaa031c0`: **16 rows, 1 json fence, 0 carried** -- no adjudication existed, so all 16 are compiled here. C-S1 is the grade record for the six judgment criteria. C-S2 and C-S3 dismiss 4 rows with reasons; C-S4 to C-S8 and C-S11 graduate 12 rows; C-S9, C-S10, C-S12 and C-S13 are four findings of this seat's own, each graduated. Closing count: carrier-less **0 of 16**.

THE DENOMINATOR MOVED WHILE THIS WAS BEING WRITTEN, AND THE COUNT IS SAID TWICE ON PURPOSE. The hand-off named 15 rows at `05ace72349`, and this seat read 15 at `a6eb2ed504`. `2.0.0_SA_COO~G` appended `LGIC_CANON-S3` at 05:52Z (`5bdaa031c0`), so the population is 16. It was caught by counting the fence again at write time rather than by trusting the hand-off's figure; an L8 that compiles the count it was handed compiles a count, not a channel. Two ARMED rows now stand, with different disarm owners: `W8-S1` (`1.0.0_SA_CTO`) and `S3` (`2.0.0_SA_COO~G`).

ORDERS: 12 of 12 terminal (10 `complete`, 2 `pending` with VALID proofs -- CN-j-3 and CN-o-2, terminal under `1.0.0_SA_CTO`'s 96806). This seat re-ran `proof-of-spec-check.py` BOUND by `--governing-order` with each order's own `<expected_criteria>` on every instance at HEAD: **12 of 12 VALID**, denominator = instances found under `deliverables/0.9.0_WK_LGIC_CANON~*/`.

VINTAGE WARNING, AND IT CHANGED A MEASUREMENT MID-ADJUDICATION. At `a6eb2ed504` the canon's diff against the judging vintage `671925aecc` was EMPTY. At `783e2f3887` it is NOT: `4.0.0_SA_CRO` re-rendered the generated naming section against `NAMING_SCHEMA.json` v1.9 (gate G-V19R, `--check` STALE -> FRESH). Every canon finding below was therefore RE-MEASURED at `783e2f3887`, after that re-render, and every one still holds. That is a stronger result than the judging vintage alone: the schema bump is the obvious hypothesis for fixing them, and it did not.

FWD outcomes are `1.0.0_SA_CTO`'s to grade at the round-1 analysis. This seat grades the six judgment criteria only.

```json
[
 {
  "id": "LGIC_CANON-C-S1",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "ROUND-1 L9 GRADE RECORD: the six JUDGMENT criteria -- K1-J1 FAIL (four named places where the one document does not settle the question, over an instrument that reached 14 of 21 rules), L1-J1 PASS (qualified: the column grades the DECISION, never the work), R1-J1 PASS (qualified: one blanket sentence, not a row-by-row walk), R2-J1 PASS, J3-J1 PASS, O2-J1 PASS.",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: a JUDGMENT criterion is graded by the CVO against the order that issued it, never self-graded; the verdict lives in `grades`. The round's 12 orders carry 6 judgment criteria (K1-J1, L1-J1, R1-J1, R2-J1, J3-J1, O2-J1); the other 6 orders' faces name none.",
  "world_is": "Denominator by subtraction, not recall: 12 order files, `judgment=\"true\"` present in 6 of them (CN-j-3, CN-k-1, CN-l-1, CN-o-2, CN-r-1, CN-r-2) and absent from the other 6 (CN-j-1, CN-j-2, CN-n-1, CN-n-2, CN-n-3, CN-o-1). Each grade below names its own instrument; where a worker's instrument was re-used it is said so, and where this seat re-derived by a DIFFERENT instrument that is said too.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/task-orders/ -- 12 files, `judgment=\"true\"` in 6, at HEAD 783e2f3887",
    "RUN: python .tools/proof-of-spec-check.py <instance> <order's expected_criteria> --governing-order <order> over all 12 instances at HEAD: 12 of 12 VALID (rc=0)",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-a.tsv@537f49b8fd and judge-b.tsv@98ed3177ff",
    "infra/logic/02_DOCTRINE.md@783e2f3887 (574 lines) and infra/logic/06_CONFORMANCE_LEDGER.md@783e2f3887 (221 lines)"
   ]
  },
  "grades": [
   {
    "criterion": "K1-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/LGIC_CANON.TO-CN-k-1.canon.proof_of_spec.json@daa5b3ba75",
    "verdict": "FAIL",
    "reason": "Bar: 'a seat can apply each rule from this document alone' (TO-CN-k-1 :66). FAIL on the word EACH, in four named places, all re-measured at 783e2f3887 AFTER the v1.9 re-render. (a) A1 has no rule of its own: s.2's A1 row (:88) names R9 and R18, neither of which states a law on an arrival mechanism, and s.3 carries no A1 heading; the one measured A1 departure is decided by R20, which s.2 lists on no axis (:94). Two blind judges split there (row W7-S1). (b) The canon carries no adjacency test for `bd`: a case-insensitive census of the file for 'adjacen' and 'next to' returns 0 and 0, while N4 (:277) names both referents with no rule for choosing; both judges therefore read the key's ALIAS case as OUT-OF-PATTERN (row W7-S2). (c) R1's census tag (:130, '53 of 53 non-SmartX monolith planes CONFORMANT') and R1's own text give opposite answers on the same planes; a judge who takes the tag answers A3 differently (row W5-S1). (d) The axis verdict vocabulary the judging required is not in the canon at all -- CONFORMS 0, VIOLATES 0, DECLARED-EXCEPTION 0 occurrences; it came from the order face, byte-identical in both orders (row C-S9). COVERAGE, and it is the half the mechanical criteria cannot supply: the only instrument that tried to APPLY the rules reached 14 of the 21 rules the s.0 census counts; R3, R8, R14, R15, R17, R19 and R21 were never exercised by any arm this round (row C-S10), so on a third of the domain the bar is unevidenced in either direction. NOT the ground of this FAIL: the seven mechanical criteria K1-AC1..K1-AC7 all PASS with a red-first negative control (all seven FAIL on v0.3), the two worker choices offered for grading (the ADVI clause's decider; the RULED marks citing the PRD) are both within the order, and W1-S1's s.1 rewording moves words and no rule."
   },
   {
    "criterion": "L1-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~2/LGIC_CANON.TO-CN-l-1.ledger.proof_of_spec.json@831a86ba6f",
    "verdict": "PASS",
    "reason": "Bar: 'no row reads as finished while part of it waits' (TO-CN-l-1 :54). Re-derived by a DIFFERENT instrument from the worker's `ledger_recount.py`: this seat parsed the ledger's markdown tables directly at HEAD, sectioned s.1-s.5, and cross-read each row's `decided` cell against its own disposition text. Result: 68 plane rows, 68 carrying the column, 65 DECIDED and 3 WAITING (Andrew) -- the three `opal-data-etfs` rows at :103-105 -- and ZERO rows reading DECIDED while their own text names an open wait (an AWAITING token, or X3 or X5, both OWED). The register was read entry by entry, 7 of 7: X1, X2, X4, X6 GRANTED PERMANENT; X7 GRANTED CONDITIONAL with its condition and owner; X3 and X5 OWED with decider Andrew. The one row that cites X7 (:112) reads DECIDED, and that is right: X7 is GRANTED and its condition is a future EXPIRY trigger, not an owed act. QUALIFIED, twice, and both qualifications are the ledger's own: s.8 states the column's semantic narrowly ('says whether a word is still owed on a row's disposition ... nothing about whether the move is done, scheduled or safe'), so a DECIDED MIGRATE is an undone migration and the bar is about the DECISION; and s.0 states that row-state from the projects' own channels is NOT joined here, so a part waiting in a project channel is invisible to this bar by construction."
   },
   {
    "criterion": "R1-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.TO-CN-r-1.fwd2-record.proof_of_spec.json@83afab6973",
    "verdict": "PASS",
    "reason": "Bar: 'the evidence supports each clause' (TO-CN-r-1 :39). Three clauses, each re-checked by printing the bytes at the cited line rather than searching for the quote. CLAUSE 1 (one sitting): the nine-calls record @c6be748be7 :15-18 is one sentence answering the whole nine-card set, with :32, :34, :39 and :40 the cards, and the ticklist @6dab0d76a7 :14-16 and :69-70 record the same single time -- HOLDS. CLAUSE 2 (enough beside every row): the table as put to him @54a764cb28 :44-64 gives every one of rows 1-19 a census cell, a confidentiality cell, a ruled DEFAULT and an already-ruled cell ahead of its TICK box, with no blank -- HOLDS, printed in full. CLAUSE 3 (the pre-decided rows pre-filled): @54a764cb28 :62-64 carry rows 14, 15 and 16 with a ticked 'ruled' cell while every other tickable row shows an empty box, and :66 says so -- HOLDS. QUALIFIED: 'one sitting' is a single blanket sentence ('agree with all but keep opal-data-demo'), not a row-by-row walk, so the clause rests on clause 2 -- the blanket answer is only as sound as what sat beside each row. The record's own note that the three counts are 'not all on one basis' is honest and they reconcile: rows 1-16 want a tick (16, card 3's figure), of which 14-16 were pre-ticked, leaving the 13 that v0.2 names, plus rows 17 and 18 by word."
   },
   {
    "criterion": "R2-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~3/LGIC_CANON.TO-CN-r-2.fwd3-record.proof_of_spec.json@6386bd663a",
    "verdict": "PASS",
    "reason": "Bar: 'the record supports the branch named for each project' (TO-CN-r-2 :38). Both branches checked at their cited bytes. IRPT_FNTEND, branch `derived`: the report @a4cc0cb681 :15-16 reads 'their grade is DERIVED from IRPT_BCKEND's rows 1, 1b and 3' and :33-34 carry the per-surface DERIVED FROM cells -- HOLDS. IRPT_BCKEND, branch `list-of-changes`: the report @a4cc0cb681 :18 names three CONTRADICTS and :35, :36, :37 are the three rows with a named cheap resolution each -- HOLDS. Card 1 (@c6be748be7 :32) ended the pause for BOTH by name, and the two branches differ because the branch describes what the runner can point AT, not which act lifted the pause; that reading is the one FWD-3's ACCEPT states. The record's 0-of-3 absorption claim was re-derived here by a DIFFERENT instrument than its own token census: a direct coordinate read of the PRD at HEAD -- v0.14 at :8, :196 and :312 still write PLATINUM JSON to '<FIRM bucket per FIRM_BUCKET_MAP>/investor-reporting/...' with no tier segment, :311 still has gold-named runners write platinum with no gold parquet between, and :199 and :313 still put the vendor PDFs under `opal-data-ycharts`. 0 of 3 absorbed, CONFIRMED."
   },
   {
    "criterion": "J3-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~7/LGIC_CANON.TO-CN-j-3.judge-compare.proof_of_spec.json@562462e25d",
    "verdict": "PASS",
    "reason": "Bar: 'every disagreement is traced to the canon rule it exposes' (TO-CN-j-3 :46). The denominator is written as a SUBTRACTION, which is what the bar needs: 13 comparisons (5 axis verdicts + 5 axis rule sets + 3 cases against the key), 11 agreeing, 2 disagreements -- D1 (A1's rule set, judge against judge) and D2 (J-N3, both judges against the key). Both are traced to named canon coordinates with file:line at the judging vintage, and this seat re-read every one of them at 783e2f3887, after the v1.9 re-render: s.2's A1 row at :88, R20 listed only under Process at :94, N4's two-referent line at :277, and 'adjacen'/'next to' still 0 and 0. The one comparison that could have sat outside the denominator -- the canonical forms -- is argued as a CONSEQUENCE of D2 rather than a fourth axis, and the TSVs bear that out: the forms differ on J-N3 alone. E1 (row W5-S1, A3's tag-versus-text) is recorded although it did not split the pair, which is the right direction of error. The record's one honestly UNREAD item -- where the axis verdict vocabulary and its severity order came from -- is ANSWERED by this seat at row C-S9: the order face. Answering it does not weaken the trace; the vocabulary did not split the judges, so it was never a disagreement to trace."
   },
   {
    "criterion": "O2-J1",
    "instance": "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~7/LGIC_CANON.TO-CN-o-2.checklist-review.proof_of_spec.json@b736df9041",
    "verdict": "PASS",
    "reason": "Bar: 'every mark's reason holds' (TO-CN-o-2 :35). All 16 marks read, not sampled -- the bar says every and the population is 16. The test the review states is applied consistently and is the order's own, and the harder direction is the one the order warns about ('marking a real judgement step MECHANICAL to pass is exactly the defect this cell exists to catch'), so the 11 MECHANICAL marks carry the risk. The linchpin of many of them, the inputs table at :32-42, was read in full: 7 input rows, and they do carry display name, email domain, surfaces and bindings (Step 1's mark) and the portal paths and first users (Step 14's), and they do NOT carry a source directory name, a master row label, a table name, a partition form, a resource set or a function word (the marks on Steps 3, 7, 8 and 9). Step 14's mark was re-derived here with the reviewer's own instrument and WIDENED: grade() reads opal-partner-demo, -49financial, -cottonwood and -inflection all OUT-OF-PATTERN, so the conflict is a live condition of 4 of 4 existing firms, not a hypothesis about a new one (row C-S12); and the register was read entry by entry, 7 of 7, with no entry declaring it. Step 6 is the mark that most invited an error and is right: the reviewer found a real defect in the prescribed copy and still marked MECHANICAL, because the defect asks the runner to decide nothing -- and that defect is verified here at the template's :69-98 (row C-S13). QUALIFIED: the review's decidedness test admits 'a named owner: a STOP' as deciding a value, which is defensible but means 11 MECHANICAL is not 11 RUNNABLE -- Steps 10, 15 and 16 are marked MECHANICAL and all three are blocked today at Step 10's STOP, so the checklist cannot be run end to end at this vintage for a reason independent of the JUDGEMENT count."
   }
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade record, not an investigation item: it adjudicates no row and carries the six judgment verdicts. The rows the grades bear on are carried by C-S5 (W7-S1, W7-S2, W5-S1), C-S7 (W7-S3) and C-S9 to C-S13.",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S2",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "Three rows the round itself closed: S1 (R1's code/ non-application) by CN-k-1 item 6, W1-S1 (section 1's tier and code-home vocabulary) by the same edit, and W2-S2 (the ledger had no change log) by the ledger v1.0's new section 9. Each is read here at the artifact, not at the worker's claim.",
  "class": "OBSERVATION",
  "spec_asserts": "Spine L9: every row in the channel is dispositioned. A row whose remedy landed inside the round is dismissed with the remedy named, not graduated -- graduating it would ask the CTO to re-decide a thing already decided.",
  "world_is": "S1: R1's non-application at 02_DOCTRINE.md@783e2f3887 now names the LEGACY root code/ homes, and K1-AC7's run printed 'R1 NON-APPLICATION LINES NAMING code/: 1  WITHOUT legacy: 0' with a red-first control (FAIL-K1-R1-CODE-UNQUALIFIED on v0.3). W1-S1: the s.1 tier, state, code-home and firm rows now point at the generated section; the edit changes words and no rule's text, and it is graded under K1-J1 at C-S1, where it is NOT a ground of the FAIL. W2-S2: the ledger at 783e2f3887 carries a s.9 CHANGE LOG, its pre-v1.0 entries read from the file's git history, and L1-AC1's recount reads the counts it states.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 rows LGIC_CANON-S1, LGIC_CANON-W1-S1, LGIC_CANON-W2-S2",
    "infra/logic/02_DOCTRINE.md@783e2f3887 -- s.0 census line ':28 RULES CARRYING ALL THREE PARTS: 21 of 21'; R1's non-application naming the LEGACY root code/ homes",
    "infra/logic/06_CONFORMANCE_LEDGER.md@783e2f3887 :206 '## 9. CHANGE LOG'",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/0.9.0_WK_LGIC_CANON~1/canon.r1.result.md -- the seven-criterion negative control on v0.3, all seven FAIL"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-S1",
   "LGIC_CANON-W1-S1",
   "LGIC_CANON-W2-S2"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each row's remedy landed in this round and is read here at the artifact at HEAD, with the criterion that measures it and its red-first control. Nothing is carried forward from any of the three.",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S3",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "S2's premise was overtaken before issuance: the CRO read the decomposition's v1 choice of the ETFs tree, and the decomposition's own v2 struck that choice and moved the judged tree to MDPF, which is the tree the round actually judged.",
  "class": "OBSERVATION",
  "spec_asserts": "PRD DEC-2: one real pipeline tree carries at least one row where the tree breaks a canon rule and one DECLARED EXCEPTION.",
  "world_is": "The decomposition at HEAD says so in its own words at s.3a.1: 'v1's choice below was WRONG on grain and is corrected in v2 to MDPF (section 0b). The v1 text is kept, struck, because the reading of DEC-2 it states is right and the tree it names is not.' The single fixed tree input the issuance carries is CN_TREE_MDPF.md, 1 of 1 CN_TREE reference in the decomposition. DEC-2's bar is met on that tree and was exercised: both judges graded A2 VIOLATES as an UNDECLARED departure, and both named X1, X2 and X7 as the declared exceptions the tree carries. So the cross-pipeline pairing S2 warned about does not arise on the tree that was judged.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 row LGIC_CANON-S2",
    "org/missions/D14/LGIC/LGIC_CANON/decompositions/LGIC_CANON_DECOMP.md@783e2f3887 s.3a.1 -- the struck v1 ETFs choice and the v2 correction to MDPF; :156 names CN_TREE_MDPF.md as the fixed input",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-a.tsv@537f49b8fd row A2 and judge-b.tsv@98ed3177ff row A2 -- both VIOLATES, both naming X2 and X7 as the declared cover"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-S2"
  ],
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The row is correct about the v1 decomposition and the v1 decomposition was superseded by its own author before the issuance. Nothing carries forward: the ETFs tree was not judged, and the ETFs exceptions X3 and X5 are carried instead by the ledger, where they read OWED with Andrew as decider (C-S1's L1-J1 grade).",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S4",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "Two defects in the round's own instrument, both found by workers forbidden to fix it: check_canon_r1.py decodes git output in the locale codepage, so a citation whose bytes cp1252 cannot decode reads as a citation that does not stand; and its l1-column limb selects plane tables by header cell alone, never by section, so any future table headed `disposition` outside sections 1 to 5 enters the count.",
  "class": "OBSERVATION",
  "spec_asserts": "The checker's own docstring: every subcommand prints its evidence and one VERDICT line, and 'A missing input is a FAIL verdict, never a traceback'. TO-CN-l-1 2d scopes plane tables to sections 1 to 5.",
  "world_is": "Both stand, and both are the issuer's to fix because a round's fixed inputs are read-only to workers. The cp1252 limb's failure direction is a FALSE FAIL (a true citation read as absent), never a false PASS, and it did not move R1-AC2's verdict because the four v0.2 citations decode. The l1-column limb was worked around this round by renaming section 7's header cell to 'disposition class' -- the LEDGER moved to fit the CHECKER, so the checker's scope is still wrong and a later ledger edit reintroducing that header re-opens it. Graduated as a pair because they share one owner and one file.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 rows LGIC_CANON-W3-S1 and LGIC_CANON-W2-S1",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py -- git() runs subprocess with text=True and no encoding; l1_column skips a table only when 'disposition' is not one of its header cells",
    "infra/logic/06_CONFORMANCE_LEDGER.md@783e2f3887 :145 -- section 7's header now reads 'disposition class', the workaround this round applied"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-W3-S1",
   "LGIC_CANON-W2-S1"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S5",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "The three places the blind exercise found the canon short, each RE-MEASURED at 783e2f3887 after the v1.9 re-render and each still standing: A1 has no rule of its own and R20 sits on no axis (W7-S1); the canon carries no adjacency test for `bd`, so its own reading of the key's ALIAS case is OUT-OF-PATTERN (W7-S2); and R1's census tag contradicts R1's text on the same planes (W5-S1).",
  "class": "BLOCKING",
  "spec_asserts": "PRD DEC-2: a disagreement returns to CN-k-1 as a canon defect. FWD-1's ACCEPT: the same answer from both judges, 'including which rule decided it'.",
  "world_is": "Measured at HEAD, after a different seat re-rendered the generated naming section from schema v1.9: s.2's A1 row still reads 'R9, R18' at :88 and R20 is still listed only under 'Process' at :94; a case-insensitive census of the whole file for 'adjacen' returns 0 and for 'next to' returns 0, while N4 at :277 still names both referents of `bd` with no rule for choosing between them; and R1's census tag at :130 still reads '53 of 53 non-SmartX monolith planes CONFORMANT' over planes R1's own text grades out of the grammar. THE DISCRIMINATOR IS THE RE-RENDER ITSELF: the obvious hypothesis is that a schema bump carries the missing test into the canon, and this bump did not, so the remedy is an authored one -- the schema or the renderer for W7-S2, and CN-k-1's own text for W7-S1 and W5-S1.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 rows LGIC_CANON-W7-S1, LGIC_CANON-W7-S2, LGIC_CANON-W5-S1",
    "infra/logic/02_DOCTRINE.md@783e2f3887 :88 A1's rule list, :94 Process R18/R19/R20, :130 R1's census tag, :277 N4's `bd` row; 'adjacen' 0 hits and 'next to' 0 hits over 574 lines, case-insensitive",
    "git diff 671925aecc 783e2f3887 -- infra/logic/02_DOCTRINE.md: 3 insertions, 4 deletions, all inside the generated naming section (stamps, N2's source line, the demo bullet). No axis table, rule text or census tag moved",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-compare.md@62dcc19f6c s.4 D1 and D2, and s.4 E1"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-W7-S1",
   "LGIC_CANON-W7-S2",
   "LGIC_CANON-W5-S1"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S6",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "Now that the canon points at the ledger for the register's entries, X6 is the one entry that does not fit the schema the canon keeps: its axis reads `tenancy`, outside the A1-A5 domain, and the two carriers are now one so there is nowhere else for it to be right.",
  "class": "OBSERVATION",
  "spec_asserts": "02_DOCTRINE.md section 4's register schema line: an entry is 'pipeline . axis (A1-A5) . ...'. CN-k-1 item 7 makes the ledger the entries' one home.",
  "world_is": "Read at the register itself, 7 of 7 entries at HEAD: X1 A1, X2 A2, X3 A2, X4 A2/A5, X5 A5, X7 A2 -- and X6 `tenancy`. Six fit the domain and one does not. The remedy is one of two Rule-24 acts and they are not equivalent: give X6 an axis inside A1-A5, or widen the schema's axis domain with its own four-postulate record. This seat does not choose between them; the register's entries are written by 1.0.0_SA_CTO and 4.0.0_SA_CRO. INERT because a register entry classifies and moves nothing (PRD DEC-9).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 row LGIC_CANON-W1-S2",
    "infra/logic/06_CONFORMANCE_LEDGER.md@783e2f3887 :132-138 -- the seven register rows read one by one; :135 X6 `opal-data-demo` axis `tenancy`, PERMANENT, GRANTED",
    "infra/logic/02_DOCTRINE.md@783e2f3887 section 4's schema line and its pointer to 06_CONFORMANCE_LEDGER.md section 6"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-W1-S2"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S7",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "The four onboarding rows, and they are one finding at two grains: a new firm's LONG and SHORT forms derive from nothing (W6-S1), its sign-in acts have no CONTRACTS builder (W6-S2), its dashboard is served through keys the builders refuse to produce with no legacy list to admit them (W6-S3), and a reviewer who did not write the checklist marks 5 of its 16 steps JUDGEMENT (W7-S3).",
  "class": "BLOCKING",
  "spec_asserts": "PRD DEC-6 and FWD-5: taking on a new firm is one checklist run end to end, with no step where somebody has to invent an answer; CLAUDE.md Rule 30: every name a step produces is the builders' output.",
  "world_is": "The four rows are graduated together because a cell-by-cell recut would answer them one at a time and they have one shape: the canon fixes a pipeline's homes, formats, compute and name grammar and does not fix its CONTENTS, and the inputs table carries none of the contents either. W6-S1 is the identity row's contents, W6-S2 the sign-in plane's, W6-S3 the served plane's, and W7-S3's steps 3, 7, 8 and 9 are the pipeline's. Step 14 is W7-S3's fifth mark and a different cause, widened at C-S12. THIS SEAT'S OWN QUALIFICATION, and it is not in any of the four rows: 11 MECHANICAL is not 11 RUNNABLE. Steps 10, 15 and 16 are marked MECHANICAL and all three are blocked today at Step 10's STOP, so the checklist cannot be run end to end at this vintage even if the JUDGEMENT count were zero. A recut that drives the five JUDGEMENT marks to zero and does not answer W6-S3 leaves FWD-5 exactly as unrealized.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 rows LGIC_CANON-W6-S1, LGIC_CANON-W6-S2, LGIC_CANON-W6-S3, LGIC_CANON-W7-S3",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md@894b41f920 -- all 16 marks read by this seat, not sampled; TALLY 11 MECHANICAL, 5 JUDGEMENT [3, 7, 8, 9, 14]",
    "infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e :32-42 -- the inputs table read in full: 7 rows, carrying the two firm forms, display name and email domain, surfaces, bindings, the vendors and master ids, the portal paths and the first users, and carrying no source directory, table name, partition form, resource set or function word",
    "infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e Step 10's STOP, which Steps 15 and 16 both depend on"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-W6-S1",
   "LGIC_CANON-W6-S2",
   "LGIC_CANON-W6-S3",
   "LGIC_CANON-W7-S3"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S8",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "The round's one ARMED row, graduated ARMED and not disarmed here: grade()'s _new_served reads a trailing entity partition as a file leaf and rewrites the entity id's bytes, so address() and grade() give different answers for the same platinum key. 1.0.0_SA_CTO's ruling in 97211 is prose, and a disarm in prose disposes nothing.",
  "class": "OBSERVATION",
  "spec_asserts": "CLAUDE.md section 2: an ARMED hazard disarms same-turn via the row's disarm_owner. The disarm is admitted as the ARMED -> DISARMED clock advance on this round's remediation row, never as a sentence.",
  "world_is": "The ruling stands on the substance: address() and NAMING_SCHEMA key.partition are right, grade()'s _new_served is the defect, it is INERT while org/mcp/naming-gate.enforce is absent, and the fix is a cell of LGIC_ENFORCE round 2. What does not stand is the DISARM: 97211 is a message, the row still reads ARMED, and the gate admits only the clock advance. So this row is graduated ARMED with disarm.state ARMED, disarm.owner 1.0.0_SA_CTO and disarm.at null on its remediation row, and 1.0.0_SA_CTO advances that clock. 1.0.0_SA_CTO said in 97294 that it does so the same turn the remediation row exists; the row now exists.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 row LGIC_CANON-W8-S1, hazard_standing ARMED, disarm_owner 1.0.0_SA_CTO",
    "1.0.0_SA_CTO 97294 (2026-09-16T05:27:32Z): 'the gate admits a disarm only as the ARMED->DISARMED clock advance on the L9 remediation row (surprise-row-gate.py _monotone_advance); 1.0.0_SA_CTO advances that clock the same turn the remediation row exists'",
    ".tools/surprise-row-gate.py _monotone_advance -- ARMED->DISARMED with `at` moving from null to a timestamp, every other field byte-equal, is the only admitted advance",
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/remediations/REMEDIATION_v1.md (same slug) row LGIC_CANON-W8-S1, carrying the two-state disarm block"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-W8-S1"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO"
 },
 {
  "id": "LGIC_CANON-C-S9",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "The two blind judges are not independent on the scale they graded with: the axis verdict vocabulary AND its severity order were supplied by the task-order face, byte-identical in both orders, and three of the five verdict values appear nowhere in the canon -- so FWD-1's five-of-five verdict agreement is agreement on a scale the ORDER fixed, not one the canon fixed.",
  "class": "BLOCKING",
  "spec_asserts": "FWD-1's ACCEPT: 'two people who have never worked together each judge the same pipeline from the one document and give the same answer, including which rule decided it'. PRD DEC-2: each judge is 'briefed with the canon alone'.",
  "world_is": "TO-CN-j-1 :21 and TO-CN-j-2 :21 are the SAME LINE, byte-for-byte (cmp on the two extracted lines reports no difference). It reads: 'The verdicts are CONFORMS; VIOLATES (an undeclared departure); DECLARED-EXCEPTION (a departure a register entry covers); DEPARTS-RECOMMENDED (a recommended form not followed); and UNDETERMINED (the facts given do not decide). Where an axis carries several findings, write the most severe, in this order: VIOLATES, UNDETERMINED, DECLARED-EXCEPTION, DEPARTS-RECOMMENDED, CONFORMS.' Censused over the canon at 783e2f3887, 574 lines: CONFORMS 0 occurrences, VIOLATES 0, DECLARED-EXCEPTION 0, DEPARTS-RECOMMENDED 1 (at :436, a grading value for recommended cells), UNDETERMINED 1 (at :564, inside GAP-2). No severity order appears at all. THE DISCRIMINATING CONTRAST IS INSIDE THE SAME EXERCISE: the NAMING case vocabulary IS canon-carried -- CONFORMANT 16 occurrences, ALIAS 2, OUT-OF-PATTERN 4, RAISE 3 -- and that is precisely the half where the judges went OFF the key (W7-S2). So the half of the exercise the canon supplied is the half that failed, and the half the order supplied is the half that agreed. This is CLAUDE.md Rule 22's shared-dependency shape at the top of the instrument: a check scoped to the two judges cannot see a defect in what the two judges share, and each per-judge arm passes. It does NOT void the round: the rule-set split (W7-S1) and the off-key cases (W7-S2) are real findings measured through it, and A1's UNDETERMINED verdict is exactly the value the ORDER's severity order produced, which is why judge-compare recorded the ranking as coming from outside the canon without being able to say where. IT DOES BOUND THE CLAIM: no reading of 5-of-5 verdict agreement is evidence about the canon until the canon carries the verdict vocabulary or the order stops supplying it.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-j-1.judge-a.md:21 and org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-j-2.judge-b.md:21 -- extracted and compared with cmp: IDENTICAL BYTES",
    "infra/logic/02_DOCTRINE.md@783e2f3887, 574 lines: CONFORMS 0, VIOLATES 0, DECLARED-EXCEPTION 0, DEPARTS-RECOMMENDED 1 (:436), UNDETERMINED 1 (:564); CONFORMANT 16, ALIAS 2, OUT-OF-PATTERN 4, RAISE 3",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-compare.md@62dcc19f6c s.4 D1 'Also exposed, but it did not split the judges' -- 'The axis verdict vocabulary and its order therefore came to the judges from outside the canon, and this worker did not read where.' This row is the answer to that sentence",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-a.tsv@537f49b8fd row A1 'UNDETERMINED' with its reason 'which is less severe than UNDETERMINED', and judge-b.tsv@98ed3177ff row A1 'UNDETERMINED is the more severe finding' -- both judges reasoning explicitly from the order's ranking"
   ]
  },
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S10",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "The only instrument this round that tried to APPLY the canon reached 14 of its 21 rules; R3, R8, R14, R15, R17, R19 and R21 were never cited by either judge, in any direction, so on a third of the canon FWD-1's 'a seat can apply each rule' is unevidenced rather than met or failed.",
  "class": "OBSERVATION",
  "spec_asserts": "TO-CN-k-1 K1-J1: 'a seat can apply each rule from this document alone'. The canon's own section 0 census line: 'RULES CARRYING ALL THREE PARTS: 21 of 21'.",
  "world_is": "Computed as a SUBTRACTION from the printed denominator, never as a forward list: the canon's rule ids at 783e2f3887 are R1 to R21 with no gaps (21 whole-value ids, matching the s.0 census line at :28); the rule ids appearing anywhere in judge-a.tsv and judge-b.tsv combined are R1, R2, R4, R5, R6, R7, R9, R10, R11, R12, R13, R16, R18, R20 (14, and this count admits a rule cited only to say it is NOT engaged, which is the generous reading); 21 minus 14 leaves R3, R8, R14, R15, R17, R19, R21. This is a COVERAGE fact about the instrument, not a claim about those seven rules. It bounds what the mechanical criteria can be read to mean: K1-AC1 certifies that 21 of 21 rules carry an authority, a census tag and a non-application, which is a fact about the document's SHAPE and says nothing about whether a seat can apply them. A second tree, chosen to engage the seven, is the cheap instrument -- the seven are a general-data rule, the 2x2 grid, the most-derived-consumer rule, the tier-plane purity rule, the migration rule, the state-class rule and the vendor-master rule, and no one of them is exotic.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "infra/logic/02_DOCTRINE.md@783e2f3887 :28 'RULES CARRYING ALL THREE PARTS: 21 of 21'; whole-value census of R-ids over the file returns exactly R1..R21",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/exercises/judge-a.tsv@537f49b8fd and judge-b.tsv@98ed3177ff -- whole-value census of R-ids over both files combined returns 14 distinct ids",
    "SUBTRACTION, run rather than recalled: comm -23 over the sorted 21 and the sorted 14 returns R14 R15 R17 R19 R21 R3 R8",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/CN_TREE_MDPF.md -- the one tree judged; a second tree is what would move this number"
   ]
  },
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S11",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "S3, and it is CORROBORATED not repeated: 2.0.0_SA_COO~G found the renderer's registry branch never reads a FIRM row's note field, and this seat found the same loss from the other end, in the diff -- the v1.9 re-render deleted the demo bullet carrying RULING DM, and a judge briefed with the canon alone can no longer resolve a demo naming case from the one document.",
  "class": "OBSERVATION",
  "spec_asserts": "PRD DEC-1 b: the schema is the one owner of the naming enumerations and the canon only presents them. FWD-1 and TO-CN-j-1's blindness clause: a judge reads ONLY the canon, the tree file, the case list and the order, and resolves the naming cases 'from the canon's generated section ... with no second document'.",
  "world_is": "TWO INSTRUMENTS, AND THEY DIFFER, which is what makes this corroboration rather than the same read twice (CLAUDE.md Rule 22: a second seat's confirmation via the FIRST seat's method is repetition). 2.0.0_SA_COO~G read render_naming_section.py's two source paths and found the mechanism -- the schema path emits a per-firm note, the registry path reads long and short and never note -- then ran --write and measured the diff. This seat came the other way: git diff 671925aecc 783e2f3887 on the canon is 3 insertions and 4 deletions, one of which is the whole demo bullet, and then read the two surviving carriers to establish that the FACT is not lost (NAMING_SCHEMA.json v1.9 carries W6-S4 once, RULING DM twice, 'demo reads as a firm' once; the registry's demo row note carries the same text). WHAT THIS SEAT ADDS TO S3 IS THE CONSEQUENCE: the presentation is what FWD-1 measures, and BOTH carriers that still hold the ruling are documents the judging order forbids the judge to open -- so the loss is exactly on the axis this project exists to establish, and it would show up next as an unexplainable judge disagreement rather than as a missing line. And the class is general: --check's contract is that the section's bytes equal a fresh render, so any content the schema stops emitting leaves the canon with a green check and no review; S3's own negative control says the same thing from the tool's side (--check FRESH, 0 failures, over the loss). HAZARD STANDING: the filer wrote ARMED and this row keeps ARMED. Read on its own this seat would have said INERT under PRD DEC-9 -- the canon classifies and moves nothing, grade() reads the schema and not the canon -- but a hazard standing is the filing seat's call and a disarm is the disarm owner's act, not the adjudicator's, so it is carried as filed and the difference is recorded here rather than resolved by downgrade. NOT A CRITICISM OF THE RE-RENDER: G-V19R did what it was built to do, 1.0.0_SA_CTO's RULING R-1 (97306) is right that a canon disagreeing with its own schema at HEAD is the worse state, and CN-k-1's worker exercised the registry branch on scratch copies before it landed. K1-AC2 is UNAFFECTED and this seat confirms S3's own note on that point: the section IS a fresh render, and the finding is about what a fresh render omits.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@5bdaa031c0 row LGIC_CANON-S3, filed by 2.0.0_SA_COO~G at 2026-09-16T05:52Z, ARMED, disarm_owner 2.0.0_SA_COO~G",
    "MEASURED INDEPENDENTLY by 3.0.0_SA_CVO before S3 was read: git diff 671925aecc 783e2f3887 -- infra/logic/02_DOCTRINE.md, 3 insertions and 4 deletions, the deleted demo bullet at the old :199, the changed N2 source line, the two stamp lines",
    "783e2f3887 -- 'render(infra/logic/02_DOCTRINE.md, 4.0.0_SA_CRO): gate G-V19R ... --check STALE (2) -> FRESH (0)'; and S3's negative control, --check FRESH with 0 failures AFTER the loss",
    "org/standards/NAMING_SCHEMA.json at ac82ad2331 -- version v1.9, firm_forms absent, strings 'W6-S4' (1), 'RULING DM' (2), 'demo reads as a firm' (1); infra/logic/registry/scopes.json row demo -- its note carries the same ruling. The ruling survives at its owner; only the presentation is gone",
    "org/missions/D14/LGIC/LGIC_CANON/task-orders/LGIC_CANON.TO-CN-j-1.judge-a.md -- the blindness clause forbidding the judge to read the schema or any other infra/logic document"
   ]
  },
  "adjudicates": [
   "LGIC_CANON-S3"
  ],
  "disposition": "GRADUATED",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~G"
 },
 {
  "id": "LGIC_CANON-C-S12",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "Step 14's prescribed-name conflict is not a hypothesis about a new firm: grade() reads the partner table of every one of the four firms that exist today as OUT-OF-PATTERN, and the exception register's seven entries, read one by one, declare none of it.",
  "class": "OBSERVATION",
  "spec_asserts": "The checklist's Step 12 applies a name only when it reads CONFORMANT; its Step 14 mandates opal-partner-<LONG>. Canon R20: an undeclared departure is a violation; a declared one is the pattern working.",
  "world_is": "The review measured two names. This seat ran the same call over all four firm forms in the registry and got OUT-OF-PATTERN four times: opal-partner-demo (canonical opal-demo-partner-table), opal-partner-49financial (opal-49f-partner-table), opal-partner-cottonwood (opal-cot-partner-table), opal-partner-inflection (opal-inf-partner-table). There is one hand-written module file per firm in infra/aws/terraform/partner-firms/ -- 49financial.tf, cottonwood.tf, demo.tf, inflection.tf -- so four live tables carry the refused shape. The absence of a declaration was re-derived by a BETTER instrument than the review's scoped census: not the absence of hits, but a direct read of the register itself, all 7 entries (X1 MDPF Orion JWT, X2 MDPF global, X3 ETFs, X4 Pathfinder/TrueShares, X5 ETFs platinum, X6 opal-data-demo, X7 MDPF 49financial category-views), none of which names a partner table. WHY IT MATTERS BEYOND THE CHECKLIST: a JUDGEMENT mark on a step nobody has run is a document defect, and this is a live undeclared departure on four resources the sign-in path depends on. The remedy is the same either way -- an R20 entry naming the auth handler's requirement, or a rename that breaks sign-in -- but the first reading makes it a checklist edit and the second makes it a register act with an owner.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "RUN by this seat at 783e2f3887, read-only: from lib.opal_naming import grade; grade(n,'DYNAMODB_TABLE') over the four firm forms returned ('OUT-OF-PATTERN', 'opal-demo-partner-table'), ('OUT-OF-PATTERN','opal-49f-partner-table'), ('OUT-OF-PATTERN','opal-cot-partner-table'), ('OUT-OF-PATTERN','opal-inf-partner-table')",
    "infra/aws/terraform/partner-firms/ -- 49financial.tf, cottonwood.tf, demo.tf, inflection.tf, one per firm, plus main.tf and CHANGELOG.json",
    "infra/logic/06_CONFORMANCE_LEDGER.md@783e2f3887 :132-138 -- the seven register entries read one by one; none names a partner table",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md@894b41f920 STEP 14, and infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e :287-289 against :261-263"
   ]
  },
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 },
 {
  "id": "LGIC_CANON-C-S13",
  "project": "LGIC_CANON",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-09-16T06:00Z",
  "one_line": "Step 6's prescribed replace-all rewrites a comment block that is NOT the header into false text and a dangling citation: the new firm's Terraform would assert that its bucket is the bd/49F firm's client bucket and cite a ledger entry that does not exist. The review found it, marked the step MECHANICAL for the right reason, and no channel row carries it.",
  "class": "OBSERVATION",
  "spec_asserts": "Checklist Step 6: 'Replace every 49financial with <LONG>' and, separately, 'Replace the header comment with one line that names this checklist, Step 6 and the identity row.'",
  "world_is": "The template has TWO comment blocks. The header is the OPAL_ADVIPOINTERS block at the top, which Step 6 replaces. The second, at :69-98, is the cross-firm Deny's standing record, which Step 6 does not mention and the replace-all therefore rewrites. Verified at the bytes: :74 reads 'opal-data-49financial IS the bd/49F firm's client bucket', which becomes a false sentence for any other firm; and the Rollback line at :97-98 names the ledger entry 20260915T0334Z_lgic-enforce-fence-49financial_deploy_completion.md, which becomes a path that does not exist. The block also carries the LGIC_ENFORCE EN-f-1 DEC-4 replacement note and the resolution of an over-inclusive Deny, which is standing record, not boilerplate. The review's MECHANICAL mark is CORRECT on its own test -- the runner decides nothing, they follow the instruction -- and that is exactly why this needs a row: a defect that asks the runner to decide nothing is invisible to the JUDGEMENT count, so driving that count to zero would not touch it. Remedy is one line in Step 6 naming the second block.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "infra/logic/10_ONBOARDING_CHECKLIST.md@05d5131e5e :149-157 -- the enumerated edits 'and no others', including the replace-all and the header-comment replacement",
    "infra/aws/terraform/shared-infra/s3-49financial.tf@783e2f3887 :1-12 the header block; :69-98 the second comment block; :74 'opal-data-49financial IS the bd/49F firm's client bucket'; :97-98 the Rollback line naming org/critical_paths/change_management/20260915T0334Z_lgic-enforce-fence-49financial_deploy_completion.md",
    "org/missions/D14/LGIC/LGIC_CANON/deliverables/CHECKLIST_REVIEW.md@894b41f920 STEP 6 -- 'That is a defect in the copied comments, and it asks the runner to decide nothing'",
    "org/missions/D14/LGIC/LGIC_CANON/surprise-channel/investigations/INVESTIGATION_v1.md@05ace72349 -- 15 rows, none naming this"
   ]
  },
  "disposition": "GRADUATED",
  "hazard_standing": "INERT"
 }
]
```

-- 3.0.0_SA_CVO
