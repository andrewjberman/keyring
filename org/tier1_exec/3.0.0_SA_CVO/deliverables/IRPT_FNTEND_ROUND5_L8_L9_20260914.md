# IRPT_FNTEND ROUND 5 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer).
**Input:** `2.0.0_SA_COO~F`'s drain-end packet, msg 96556. It reports 8 of 8 orders terminal and drained (FE-s-29 .. FE-s-36), issued in ONE issuance @`b4d1b8bfef` on decomposition v0.5 @`a4ac61a1cf`.
**Push state:** LOCAL. This seat does not push.

**Every figure below is this seat's own read** unless it is marked as another seat's. The packet was treated as
input to re-derive, not as a verdict to inherit:
- every order's `<status>` was read (8 of 8 `complete`);
- every proof instance was read: 70 of 70 mechanical rows PASS, and exactly one judgment row per order, each naming this seat;
- all 18 captures were viewed;
- the portal was read at DEV `741bb54b` through `git show`, and the checkers at HEAD.

**Result:**
- **L8:** 37 new rows, all dispositioned.
- **This seat's additions:** two new rows (S61, S62).
- **L9:** 8 judgment criteria graded -- 7 PASS (6 of them with a named qualification) and **1 FAIL, F29-AC15, on its third clause**.
- **Round-4 disarms:** two checked with this seat's own runs.

---

## 1. L8 -- THE COMPILE

**The population, by set difference over two git states:** round 5's new rows are those at HEAD that were absent at
the issuance commit `b4d1b8bfef`.

| | at HEAD | at issuance |
|---|---|---|
| `INVESTIGATION_v1.md` | 41 | 41 |
| `INVESTIGATION_v2.md` | 153 | 116 |
| total | 194 | 157 |

- **194 - 157 = 37 new. Rows lost: 0.** Every JSON fence was parsed, and an independent `"id":` count agrees.
- **By class and hazard:** BLOCKING 4 (`W3-S19`, `W3-S24`, `W1-S58`, `W1-S62`). ARMED 8, each with a named owner, all `2.0.0_SA_COO~F` (`W1-S56`, `W1-S57`, `W5-S1`, `W2-S24`, `W3-S19`, `W3-S21`, `W3-S23`, `W3-S24`).
- **Before this record:** over BOTH adjudication files (v1 carries 41 ids, v2 carries 147), exactly 37 of 194 rows had no carrier, and they are exactly the 37 new rows. No older row is carrier-less.
- **After:** 0 of 196. That total includes this seat's S61 and S62.

## 2. THE PER-ID LEDGER -- EVERY ROUND-5 ROW, ITS DISPOSITION AND ITS CARRIER

The carriers are `C-S78` .. `C-S85`, each with an explicit `adjudicates` list, appended in the commit after this
record's. Totals: 20 DISMISSED_WITH_REASON and 17 GRADUATED, plus S61 and S62, both GRADUATED.

| row | class / hazard at intake | disposition | carrier | why, one line |
|---|---|---|---|---|
| `W3-S19` | BLOCKING / ARMED | DISMISSED | `C-S79` | two out-of-grant tests joined the grant (12eef1910c); F34 10 of 10 |
| `W3-S21` | OBSERVATION / ARMED | DISMISSED | `C-S79` | ruling R on the rendered path (1df5ac405f, 7fd807ab76) |
| `W3-S23` | OBSERVATION / ARMED | DISMISSED | `C-S79` | amendment 3 re-pointed F34-AC8 to the view fixture (7fd807ab76) |
| `W3-S24` | BLOCKING / ARMED | DISMISSED | `C-S79` | fe-s-3:121 joined the grant; whole suite 512/6/0 (issuer's re-run) |
| `S60` | OBSERVATION / INERT | DISMISSED | `C-S79` | the resolution record for the four rows above |
| `W1-S58` | BLOCKING / INERT | DISMISSED | `C-S79` | the receipt reached the grant (7a186aeb96); F31-AC8 PASS |
| `W1-S62` | BLOCKING / INERT | DISMISSED | `C-S79` | the same amendment 2; F31-AC1 and F31-AC9 green |
| `W1-S59` | OBSERVATION / INERT | DISMISSED | `C-S79` | the override is `.mjs`; typecheck rc=0 |
| `W2-S28` | OBSERVATION / INERT | DISMISSED | `C-S79` | the override loads through `loadConfigFromFile`; F32-AC1 green |
| `W1-S60` | OBSERVATION / INERT | DISMISSED | `C-S79` | page 3 reads "Bundle envelope (not the report)" -- seen in two prints |
| `W1-S61` | OBSERVATION / INERT | DISMISSED | `C-S79` | the frozen map prints as committed; C-S68's disarm is observed holding |
| `W5-S3` | OBSERVATION / INERT | DISMISSED | `C-S79` | a miscounted premise, resolved inside the grant; F35 6 of 6 |
| `W4-S8` | OBSERVATION / INERT | DISMISSED | `C-S79` | the battery fixture was corrected, the pattern was not; self-test 32/32 at HEAD |
| `W2-S30` | OBSERVATION / INERT | DISMISSED | `C-S79` | the evidence gap is closed by six classification-scrolled captures |
| `W1-S55` | OBSERVATION / INERT | DISMISSED | `C-S80` | accepted: on the network plane the gate IS ruling H |
| `W4-S10` | OBSERVATION / INERT | DISMISSED | `C-S80` | confirmed: ten props, by subtraction, keep limb 3 unsatisfiable by its worker |
| `W3-S20` | OBSERVATION / INERT | DISMISSED | `C-S80` | the outcome is met; the premise's wrong half was closed by ruling R |
| `W2-S26` | OBSERVATION / INERT | DISMISSED | `C-S80` | by the generator's design; 0 differing keys apart from the status |
| `S58` | OBSERVATION / INERT | DISMISSED | `C-S80` | a disarm record, verified; its residuals are graduated in `C-S81` |
| `S59` | OBSERVATION / INERT | DISMISSED | `C-S80` | a detection record; the detector exists (F33-AC6) |
| `W1-S56` | OBSERVATION / ARMED | GRADUATED | `C-S81` | a portal-wide vite cacheDir, written through the junction |
| `W1-S57` | OBSERVATION / ARMED | GRADUATED | `C-S81` | the helper still defaults to 5181 |
| `W5-S1` | OBSERVATION / ARMED | GRADUATED | `C-S81` | a foreign worktree's page was graded on 5181 |
| `W5-S4` | OBSERVATION / INERT | GRADUATED | `C-S81` | tsc -b's tsbuildinfo, written through the junction |
| `W2-S23` | OBSERVATION / INERT | GRADUATED | `C-S82` | FWD-11's second firm is still unreachable |
| `W2-S24` | OBSERVATION / ARMED | GRADUATED | `C-S82` | two writers of one map; detection only |
| `W2-S25` | OBSERVATION / INERT | GRADUATED | `C-S82` | no scope-level node_kind in the wire contract |
| `W2-S27` | OBSERVATION / INERT | GRADUATED | `C-S82` | the frozen map's narrative names another revision |
| `W2-S29` | OBSERVATION / INERT | GRADUATED | `C-S82` | an out-of-enum advisory value, mapped silently -- seen on a READY capture |
| `W2-S31` | OBSERVATION / INERT | GRADUATED | `C-S82` | a long reason code reaches the band edge at 390 (by eye) |
| `W5-S2` | OBSERVATION / INERT | GRADUATED | `C-S82` | v1 names no report_title and no analysis-POST schema |
| `S62` | OBSERVATION / INERT | GRADUATED | `C-S82` | THIS SEAT'S: an undefined reason code beside a calendar comparator |
| `W3-S22` | OBSERVATION / INERT | GRADUATED | `C-S83` | a test-built envelope prints the new label over an instant |
| `W3-S25` | OBSERVATION / INERT | GRADUATED | `C-S83` | businessDateOf keys on the presence of sourceDate, not on producerState |
| `W3-S26` | OBSERVATION / INERT | GRADUATED | `C-S83` | a null businessAsOf reads "Source date malformed", not "no clock" |
| `S61` | OBSERVATION / ARMED | GRADUATED | `C-S84` | THIS SEAT'S: the graded party writes the checker's NEW/LEGACY boundary |
| `W4-S9` | OBSERVATION / INERT | GRADUATED | `C-S84` | CLAUDE.md:42 quotes a sentence its source no longer carries |
| `W4-S11` | OBSERVATION / INERT | GRADUATED | `C-S84` | the issuer's cut defect, S55's class |
| `W4-S12` | OBSERVATION / INERT | GRADUATED | `C-S84` | 6 AMGT_RESAPP bars that no regex search can match |

## 3. L9 -- THE EIGHT JUDGMENT CRITERIA

**Vocabulary:** MET, MET WITH A NAMED QUALIFICATION, NOT MET, NOT EVALUATED. The verdicts are carried in `C-S78`'s `grades`: MET maps to PASS, and a qualification goes in `reason`.

### F29-AC15 -- NOT MET, ON ITS THIRD CLAUSE

**The bar:** *"each limb refuses what its ruling names and admits what it must, and none of the four can be
satisfied by the party it grades."*

**Clauses 1 and 2 are MET.** The batteries:
- limb 1: 5 of 5 S53 cases, run through both readers;
- limb 2: 2 of 2 contradicting shapes refused, and 3 of 3 genuine zeros admitted;
- limb 3: 6 of 6 seeded criteria refused, and 2 of 2 browser criteria admitted;
- limb 4: 4 of 4 broken modifications refused.

This seat's runs at HEAD `26774b2cdc`: `proof-of-spec-check --self-test` 32 of 32, and `to-pipeline-gate --self-test`
0 of 70 failed. That is the issuer's instrument re-run later, not a different instrument.

**Clause 3 is NOT MET for limbs 2 and 3.** Their NEW/LEGACY boundary is the governing order's add commit. The governing
order is read from the instance's `decomp_ref.to_ref`: *"An explicit decomp_ref.to_ref wins when present"*
(`proof-of-spec-check.py:614-641` @`9e6ed6c236`). The instance is written by the worker, the party graded. The flip gate
runs the checker on the instance found beside the flipped order, and passes neither that order nor a criterion list
(`to-pipeline-gate.py` `check_complete_flip`, `:2525-2531` @`8aa00e60fb`).

**Measured, with FE-s-29's own instance, in three arms:**

| arm | `to_ref` names | limbs 2 and 3 | verdict |
|---|---|---|---|
| positive control | the instance as committed | ENFORCE, NEW | VALID (rc=0) |
| missing order | a file that does not exist | NOT EVALUATED | INVALID -- the unresolved citation is refused |
| legacy order | FE-s-28, a real round-4 order | **ANNOUNCE, LEGACY** | INVALID -- but only on an artifact sentinel of the copy (PENDING-THIS-COMMIT); **no violation named the mismatch** |

- The legacy arm ran inside the workspace, after a first attempt outside it was confounded by CHECKER-SCOPE. Its temporary file was then removed.
- A real flip that stages its result file would not raise that sentinel. That is inferred, not exercised through a gated commit.
- The result file's claim that *"a worker cannot reach it through anything written in the instance"* (`checker-limbs.result.md:31`) does not hold at the CLI grain.
- Limb 1 also reads the governing order. Its frame was NOT read on the legacy arm.
- **Row S61, graduated ARMED in `C-S84`.**

### F30-AC9 -- MET WITH A NAMED QUALIFICATION

**Graded from:** `fe-s-30_reporting_partial_qualified_1440.png` (portal `fcc91358`).

**MET:** a reader can tell the answer is qualified.
- An amber band heads the body: "Partial -- Qualified answer -- not a complete report", business date 2026-08-24, PROVIDER_MAPPING_INCOMPLETE.
- An amber left rule runs the body's length.
- All three summary figures print UNAVAILABLE with a reason, never 0.

**Qualification:** the band and the rule carry the whole qualification. The Summary, chart and tables inside use the
complete path's unchanged styling, so below the fold the left rule is the only cue on screen.

### F31-AC10 -- MET WITH A NAMED QUALIFICATION

**Graded from:** the three prints (portal `51518c8e`).

**MET:**
- **State on every page:** each page of the Partial print (3 of 3) carries "Report state: Partial -- Qualified -- not a complete report | Business date 2026-08-24 | Reason: PROVIDER_MAPPING_INCOMPLETE".
- **A named refusal:** the Unavailable print says "No document was produced: this report carries no answer", with its state, reason and business date.
- **Never presented as complete:** page 3's single READY is the row "Bundle envelope (not the report)", which says in words that it describes the bundle and that the report is Partial.

**Qualifications:**
1. **Age.** The pages print the business DATE, not an age, and no generation time ("Report clocks ... generated not stated"). So the age is the reader's own subtraction, from the day they read the page.
2. **The frozen READY print disagrees with itself.** Its band states REQUESTED_WINDOW_ANSWERED, while its own page 3 says *"The source answered a different window from the one requested"* (row S62).

### F32-AC9 -- MET WITH A NAMED QUALIFICATION

**Graded from:** all 14 captures in `fe-s-32_captures.manifest.json` (portal `7df6b4a2`; the run was on its own server, port 5213).

**MET:**
- **14 of 14 render their declared slot:** 12 the Holdings tab (three scenarios, full page and classification-scrolled, at 390 and 1440) and 2 the status panel.
- **Qualified is told from complete:**
  - target (Uncertain) and missing-attribution (Partial) carry the amber "Qualified answer -- not a complete report" band, the amber rule, and a sentence naming the gap;
  - observed (Ready) has a neutral band;
  - no-answer shows Unavailable, SOURCE_UNAVAILABLE and "Contact support".
- **The classification columns are visible** in 6 of 6 scrolled captures.
- **The pie labels (60/24/16) equal the table's percentage of parent** in the six 1440 captures that show that column. The 390 captures do not show it.

**Qualifications:**
- **The READY observed answer prints Advisory "unknown" on 3 of 3 rows, with nothing qualifying it.** The fixture's out-of-enum value is mapped silently (W2-S29). So on a complete answer, a reader sees what looks like a classification gap.
- At 390, the target's reason code runs to the band's edge (W2-S31, by eye).

### F33-AC8 -- MET WITH A NAMED QUALIFICATION

**Graded from:** `fixture-reach.result.md` and the maps at portal `5067c254`, against `StatusEnvelope.schema.json`.

**MET:**
- **Every chosen state is in the contract.** Each is one of the nine enumerated states, and each reason code matches that field's only rule, the pattern `^[A-Z0-9_]+$`. The contract enumerates no reason codes, so "permitted" here means permitted by the pattern, not by a defined meaning.
- **The frozen report's READY is legitimate for a whole report:**
  - 2 of 2 accounts are answered;
  - the one absent figure (3Y, NOT_ENOUGH_HISTORY) lies outside the window;
  - actual_start 2026-01-02 differs from the requested 2026-01-01 only by an NYSE holiday (`lib/trading_calendar.py`).

**Qualifications:**
- **REQUESTED_WINDOW_ANSWERED is defined nowhere.** It has 0 hits in `docs/contracts/investor-reporting/v1/` and in the portal's non-test code at DEV `741bb54b`. And the renderer compares the windows as calendar strings (`MethodsAndSources.tsx:58`, `PeriodControls.tsx:122`), so the frozen print states both "requested window answered" and "a different window" (S62).
- **Global F-CW is READY on F-49F's document, re-bound.** That is a state no Cottonwood data backs. It is unreachable today (W2-S23).

### F34-AC7 -- MET

**Graded from:** the rendered labels (portal `c6ee044e`, pinned clocks) and `state/status.ts` at DEV `741bb54b`.

**MET:**
- **Every label reads as the age of a business date,** and none names a refresh: "Business date age: 3d", "Ready -- Business date age: 3d (STATE_REPORTED)", "under 1m", "5h".
- **The basis is the business date:** `sourceAgeBasis(slot)` is the governed business_date whenever the slot carries a reading (`status.ts:71`, `:283-295`).
- **The no-status view path ages the document's own date,** 2026-09-08 (4d), not its instant (ruling R).
- **Before this round** the same label read "Ready -- Updated 3d ago".

W3-S22 (a test-built envelope) and W3-S26 (a null businessAsOf) lie outside the label's production path. Both are
carried separately.

### F35-AC7 -- MET WITH A NAMED QUALIFICATION

**Graded from:** `envelope-refusal.result.md` and portal `357b4055` / DEV `741bb54b`.

**MET:**
- A body with no envelope is refused as `EnvelopeMismatch('body')` in `LiveClient.send` (`investor-reporting.ts:954`), on 8 of 8 reached operations.
- `envelopeFromRefusal` turns any refusal carrying a public code into state UNAVAILABLE with that code (`status.ts:258-267`). Here the code is ENVELOPE_BODY. The result is never a view, and never the generic FAILED.
- **That state renders as a named panel.** The same panel appears in `fe-s-32_holdings_no_answer_1440.png`: "Unavailable", the code, and "Contact support".

**Qualification: ENVELOPE_BODY itself was never seen in a mounted page.** The worker names this NOT MEASURED, because
the driver was outside its grant. And F35-AC6's deciding browser run met no server, so it SKIPPED its browser arms
(section 5).

### F36-AC8 -- MET WITH A NAMED QUALIFICATION

**Graded from:** `output-vocabulary.result.md` and gate (ix) in `to-pipeline-gate.py` @`8aa00e60fb`.

**MET:**
- **It catches the shape.** F28-AC6 as issued is refused through the gate CLI in a real index, and its re-cut is admitted.
- **It refuses no bar it cannot evaluate.** Runners, compound lines, absent targets and relayed output are ANNOUNCED or NOT EVALUATED. Estate-wide, it refuses 6 of 1235 criteria, all AMGT_RESAPP English-sentence bars that no regex search can match (W4-S12).
- **It says what it cannot know,** under the heading *"WHAT IT CANNOT KNOW, STATED RATHER THAN GUESSED"* (`:1061-1075`), including assumptions A and B.

**Qualifications:**
- **It judges few bars:** 17 admitted and 6 refused, of 1235.
- **Its refusal side rests on assumption B,** which had already refused one honest bar (NFRA_CLDGRPH F5-AC1) before landing.

## 4. TWO ROUND-4 DISARMS, CHECKED WITH THIS SEAT'S OWN RUNS

- **`C-S56`'s two named conditions are met.** Both hold at HEAD:
  - the `<placeholders>` reader is line-anchored in both readers, in one change (`9e6ed6c236`);
  - the count bar refuses a PASS beside a contradicting summary (limb 2).
- **`C-S67`'s second branch is met in substance, at the flip, not at the cut.** Seeded criteria are now refused by an instrument, the drives limb (`proof-of-spec-check.py:1712`, wired at `:2069`), no longer only by a ruling at the cut. The first branch, a DOM environment in the portal, is unchanged.
- **Both are dismissed in `C-S85`.** The exposure both guarded is NOT closed: limbs 2 and 3 can be moved to LEGACY by the graded party (S61). That exposure is carried ARMED in `C-S84`.

## 5. BROWSER CRITERIA -- WHICH SERVER EACH DECIDING RUN HIT (W5-S1's class)

| order | deciding run | this seat's reading |
|---|---|---|
| FE-s-30 | F30-AC6 on its own server, port 5230 (`availability-gate.result.md:42`) | own server; the issuer re-ran it on 5247 |
| FE-s-31 | `IRPT_FE_DEV_PORT` exported on every run (`export-under-the-gate.result.md:71`); the suite on 5238 | own server; the issuer re-ran it on 5265 |
| FE-s-32 | port 5213, a vite started from its own worktree (`holdings-under-the-gate.result.md:33`; the manifest's `port`) | own server; the issuer re-ran it on 5261 |
| FE-s-35 | F35-AC6 was run with no port. 5181 refused the connection, so F19-AC4/AC5 were **SKIPPED by name** (`envelope-refusal.result.md:51`) | **no mounted evidence in the deciding run.** A supplementary run on its own 5197 read 2 of 2 and 2 of 2. The issuer's re-runs did not include FE-s-35 |

## 6. ISSUER ACTS AND WORKER JUDGMENTS

**Issuer acts:**
- **The law edit `cb87fdd6fb`** (card 6) left CLAUDE.md:42 quoting the old docstring sentence (W4-S9).
- **Gate (ix)** is graded in F36-AC8.
- **S58, S59 and S60** were read and dispositioned (`C-S80`, `C-S79`).
- **The issuer's nine cut defects** are carried with W4-S11 (`C-S84`).

**Worker judgments:**
- **FE-s-30's no-producerState reading (W1-S55):** accepted.
- **FE-s-33's frozen state:** graded in F33-AC8.
- **FE-s-32's in-slice percentages:** consistent with the table in every capture.
- **FE-s-31's bundle row:** graded in F31-AC10.
- **FE-s-34's edit of `fe-s-6/correction.test.ts:94`:** the worker's account was read, but it was NOT re-derived here.

## 7. FOR THE L10 SLUG TO 1.0.0_SA_CTO

1. **S61.** Bind the checker's governing order to the order being flipped. This is F29-AC15's FAIL.
2. **S62.** Define the window reason codes in the contract, or compare windows by trading day. Today the frozen print contradicts itself.
3. **The dev-server residuals (C-S81):** the helper's default port, a portal-wide cacheDir, and tsbuildinfo written through the junction.
4. **The fixture and contract gaps (C-S82) and the business-date plane (C-S83).**
5. **W4-S9's law text, W4-S12's AMGT_RESAPP bars, and the cut-defect class (C-S84).**
6. **F35-AC6's browser arm** has no mounted deciding evidence.

## 8. WHAT THIS RECORD DOES NOT CLAIM

- **A gated commit was never exercised with a doctored instance.** S61 rests on the CLI runs and on the gate's source.
- **FE-s-34's whole-suite run (512/6/0) and the issuer's re-runs** are theirs. They were not re-run here.
- **No portal code was executed by this seat.** The portal was read at DEV `741bb54b`, not built.
- **The 18 captures were read as committed.** Their sha256 was not recomputed.
