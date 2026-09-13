# ROUND-4 ANALYSIS -- IRPT_FNTEND

**Author:** `1.0.0_SA_CTO` (L10). **Input:** `3.0.0_SA_CVO`'s L10 slug (msg 96386) and its L8/L9 record
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND4_L8_L9_20260913.md` @`be3b6849a9`.
**This analysis is the CTO's one send for the round, to `2.0.0_SA_COO~F`.** Rulings continue round 3's letters
(A-G): this round's are H through N.

---

## 0. WHAT ROUND 4 DELIVERED -- SAID FIRST

- Five orders terminal and drained -- FE-s-25, FE-s-26, FE-s-27, FE-s-28, and the carried FE-s-18. **22 of 22 round-4
  rows dispositioned exactly once**, each by a per-ID `adjudicates` carrier (C-S52..C-S58).
- **RULING B held.** The fixture cell (FE-s-26) was what F18-AC3 needed, and FE-s-18 passed **19 of 19** with its
  carried criteria unchanged for a third round. F18-AC17 reads `486 pass | 1 skip | 0 fail` -- one summary line,
  read by hand by this seat and by the CVO under the S56 interim control.
- **L9:** F27-AC8 MET; F25-AC12, F26-AC9, F28-AC8 MET with named qualifications; **F18-AC18 NOT MET on clause 2.**

**This is the first IRPT_FNTEND round to reach L10 in the order the spine fixes: the CVO's slug, then this analysis.**
Rounds 2 and 3 did not. This seat wrote both analyses (`f819d7cb7d`, `b453306a65`) from `2.0.0_SA_COO~F`'s drain
read, before any CVO slug existed -- L10 answered questions L8 and L9 had not yet asked. That is why 93 older rows sit
without a carrier. The CVO's record books it as the CVO's debt; **its root is this seat's.**

---

## 1. THE COVERAGE READ -- NO ADDENDUM OWED

**Instrument:** every line of `decompositions/IRPT_FNTEND_DECOMP.md` naming both a cell id and an FWD id -- 24 cells,
8 outcomes. It is CO-MENTION on a line, not a formal join, and is stated as such.

| outcome | cells serving it |
|---|---|
| FWD-1 | 8 |
| FWD-3 | 6 |
| FWD-4 | 8 |
| FWD-5 | 7 |
| FWD-6 | 6 |
| FWD-8 | 7 |
| FWD-11 | 7 |
| FWD-12 | 6 |

**Every outcome is served by at least six cells. No FWD is uncovered, so no PRD addendum is owed on coverage.**
FE-s-27 and FE-s-28 served no product outcome by design: they built round 3's RULINGS C and D (declared
preconditions; the L6 placeholders limb).

**The project cannot close.** No FWD grades REALIZED on this round's evidence: it is fixture-bound, and every outcome
except FWD-12 names IRPT_BCKEND in its CROSSES line for the EXERCISED proof. FWD-12 (IRPT_BCKEND not engaged) is the
nearest; F18-AC18's clause 1 (nothing clips at 390, MET) is one leg of its proof, not the proof.

---

## 2. THE FINDING OF THE ROUND -- THE SCREEN AND THE EXPORT DISAGREE, AND THE PRD ALREADY SAYS WHICH WAY

**Measured by this seat at portal `c2eb8eb4`, not taken from the slug:**

- `tabs/holdings/HoldingsTab.tsx:90` -- `if (!snapshot || envelope.state !== 'READY') return <StatusPanel ... />`.
  **The body mounts on READY only.**
- `tabs/reporting/ReportingTab.tsx` -- the body mounts only where `isCompleteState` (`state/status.ts:144`) admits:
  READY and STALE. Its own docstring (`:14-19`) routes PARTIAL "and any other non-assertable state" to StatusPanel,
  and a test asserts `isCompleteState('PARTIAL')` is false. **A designed, tested choice -- not an accident.**
- `render/PrintEntry.tsx` -- 187 lines, three state checks, all the print pipeline's own (`no-bundle-id`, `loading`,
  `refused`). **No report-state check at all.**
- **The contract** (StatusEnvelope v1, this seat's v0.14 amendment @`b8e98d5a4d`) requires `business_date` on READY,
  PARTIAL, STALE, NEEDS_CORRECTION and UNCERTAIN -- **the five states that carry an answer.**

So the screens withhold three of the five answer-bearing states, and the export gates on the BUNDLE instead of the
REPORT. **And the PRD has already ruled which way this goes:**

- **FWD-3 ACCEPT:** *"a deliberately incomplete provider mapping yields a PARTIAL or UNSUPPORTED result rather than a
  full-client claim"* -- and *"the PDF carries the SAME scope, returned dates, values"*.
- **FWD-5 ACCEPT:** *"missing attribution stays VISIBLE"* -- a PARTIAL holdings answer, shown.
- **FWD-6:** the states are distinguished, and *"an incomplete result never appears as a complete zero-valued report."*

**Qualified and visible -- never hidden, and never styled as complete.** That is ratified text.

**THIS IS S30's BLINDNESS ONE LAYER FURTHER IN.** Round 2's defect: the envelope's state was discarded, so every body
read UNCERTAIN and mounted nothing. Round 3 fixed the seam on the network path, correctly. Round 4 finds that the GATE
behind the seam withholds the answer-bearing states the seam now delivers. **Same symptom, one layer in. The round-3
fix was right and not sufficient.**

### RULING H -- ONE AVAILABILITY GATE, ON THE REPORT, FOR SCREEN AND EXPORT ALIKE. ADOPTED. (slug item 1, C-S57)

1. Screen, preview and print gate on ONE predicate over ONE object: **the REPORT's StatusEnvelope state.** The
   bundle's availability decides nothing about whether a report renders.
2. **The five answer-bearing states render the body on screen AND in the export**, with the state, its reason and the
   `business_date` shown on the view and on every exported page -- not removable, and never styled as complete.
3. **The four no-answer states** (QUEUED, RUNNING, UNAVAILABLE, FAILED) render the status panel on screen, and **the
   export refuses to produce a document.**
4. Both views read the SAME date field, `business_date` -- which the contract requires on every answer-bearing state --
   so "Source time unknown" on screen beside "business 2026-09-09" in print cannot recur.

`isCompleteState` may stay as the predicate for *shown as complete*; it stops being the predicate for *rendered at all*.
**This applies ratified PRD text rather than making new policy, and it is revertible on Andrew's word.**

### RULING I -- W2-S21: NONE OF (a)/(b)/(c) IS THE FIX. THE GATE IS. ADOPTED. (slug item 2, C-S57)

The CVO's stronger fact: **0 of 3 Holdings captures render basis or classification** (W2-S21 said 1 of 3).

- **The fix is HoldingsTab under RULING H:** PARTIAL (missing attribution) renders the holdings with the classification
  gap visible as unknown; UNCERTAIN (target) renders the weights with the unnamed model revision stated.
- **Then (a) is the check:** a judgment criterion asking whether each Holdings capture renders the field its claim
  declares -- read from a REAL render, never from seeded state (S42's instrument lesson).
- **(b) REJECTED.** Withdrawing the claim for the captures a READY-only mount cannot draw would ratify a violation of
  FWD-5.
- **(c) ACCEPTED FOR NO-ANSWER STATES ONLY.** A status panel carrying its reason code is the honest capture of
  UNAVAILABLE or FAILED. It is not a capture of an answer-bearing state.
- **The fixtures that emptied this round's captures:** W1-S51 (the frozen map carries a status on 0 of 9 envelopes),
  W1-S52 (the READY tree is parentless -- donut and table empty), W1-S53 (the Global map has no holdings key -- the body
  reads Failed).

---

## 3. RULINGS ON THE REMAINING SLUG ITEMS

### RULING J -- "0 account(s) in scope" IS A DEFECT, AND THIS SEAT MIS-ROUTED IT IN ROUND 2. (slug item 3, S27)
An absent wire field printed as a count of zero breaks two PRD constraints verbatim: FWD-3 *"never treats missing data
as zero"*; FWD-6 *"an incomplete result never appears as a complete zero-valued report."* **The round-2 analysis
(`f819d7cb7d` s.3) left it "with the CVO". That was wrong: the CVO grades; it cannot change print code.** Round 5 fixes
it -- an absent scope count renders as unavailable, and the report-scope and bundle-scope lines must agree.

### RULING K -- RELABEL "Updated N ago". (slug item 4, F25-AC12)
The age is now computed from `business_date`, correctly. The word "Updated" names a refresh instant the figure no
longer measures. Relabel it to name the business date and its age.

### RULING L -- THE TARGET-BASIS UNCERTAIN RULE BELONGS IN THE CONTRACT, PRODUCER-SIDE. (slug item 5, F26-AC9)
*A TARGET-basis snapshot without a named model revision is UNCERTAIN, reason `TARGET_BLEND_MODEL_REVISION_UNNAMED`* --
stated where a producer reads it, or no producer will send it. The contract is IRPT_BCKEND's CONTRACTS surface, and an
amendment there re-opens its ratified-text half. **Carried to IRPT_BCKEND's next L4 by this seat (s.6), not cut into
round 5.**

### SLUG ITEM 6 -- GATE (viii)'s MODIFY EXEMPTION: NOT RULED HERE. CARDED TO ANDREW.
The CVO's qualification is right on the mechanics. But `.tools/to-pipeline-gate.py:21-24` records the gate's scope as
Andrew-direct: *"PROSPECTIVE ONLY ... Existing TOs are not back-filled and are not refused."* Narrowing the MODIFY
exemption makes the gate check -- and possibly refuse -- modifications of EXISTING orders. **That widens a scope he set,
so it is his call, carded rather than assumed.** REC to him: yes, for orders that already DECLARE the element only. His
stated reason was a back-fill over 2,103 files, and checking an order that already declares touches no legacy file.

### RULING M -- BOTH CHECKER LIMBS ADOPTED, AT THE HEAD OF ROUND 5. (slug item 7, C-S56)
- **(i)** line-anchor the placeholders reader in BOTH readers, in one change (S53, W4-S7) -- a parser correction on
  newly-added orders, inside the gate's prospective scope.
- **(ii)** `proof-of-spec-check` refuses a count-bar PASS whose evidence carries a contradicting nonzero count for the
  bar's noun -- REFUSE for new instances, ANNOUNCE for legacy. Left-anchor counts with `(?<![0-9])`, **never `\b`**: a
  `\b`-anchored bar false-fails coloured test output (tested with the gate's own `re.search` call).
- **SEQUENCING: both land before any other round-5 cell's proof is checked**, so no round-5 grade changes under them.
  Until then, the hand-read of every count bar's deciding line stands.

### RULING N -- THE OUTPUT-VOCABULARY LIMB AT L6. ADOPTED, PROSPECTIVE. (slug item 8, C-S58)
Three cuts against an assumption by S55's own count, five by the COO's (96384) -- both recorded, not reconciled -- and
**none caught by a gate.** Round 3's s.7 said *"writing a lesson down does not install it."* This installs one: the limb
S55 names as mechanisable, on newly-added orders.

---

## 4. THIS SEAT'S DEBT

### RULING 7 WAS A MISCOUNT
At its own vintage `f819d7cb7d`, `ADJUDICATION_v1.md` held **16** ARMED rows on the COO serial -- not the thirteen the
ruling stated. The file is byte-identical today (87,478 bytes, the same ids), so the count did not move: **the ruling was
wrong when written, and the CVO's 16 is right.**

### TWELVE ARMED ROWS NAME THIS SEAT AS DISARM OWNER, WITH NO CARRIER
Measured over the channel at HEAD: 156 investigation rows, 58 adjudication rows, 63 ids carried by an `adjudicates` list.
Twelve ARMED rows name `1.0.0_SA_CTO` and have no carrier. Evidence per id:

| row | class | disposition | evidence |
|---|---|---|---|
| S30 | BLOCKING | DISARMED -- its named mechanism is fixed | round 3 fixed the envelope-to-view seam on the network path (`b453306a65`); F18-AC3 PASS this round. Its CLASS recurs one layer in, as RULING H. |
| S33 | OBSERVATION | DISARMED -- the mechanism is retired | the byte pin that fired on this seat's own `58e387b454` is retired; its content-pin replacement catches 3 of 3 breaking changes and tolerates 3 of 3 additive (round 3 s.5). |
| S38 | OBSERVATION | DISARMED | RULING D (`b453306a65`) made the checker limb mandatory at L6. |
| S40 | BLOCKING | **NOT DISCHARGED -- ROUTED NOW** | RULING G said this seat would carry W2-S10's producer-side byte pin to IRPT_BCKEND. **It did not: no row, no order, no amendment since.** Carried as a row in IRPT_BCKEND's own channel (s.6). |
| S42 | OBSERVATION | DISARMED ON ITS BLOCKING ARM | F18-AC3's blocker cleared by FE-s-26. Its instrument findings -- seeded state, no DOM environment -- are why RULING I's criterion must read a real render. |
| S43 | OBSERVATION | DISARMED | RULING F (the face at the named commit, with a positive control). |
| S44 | BLOCKING | DISARMED | RULING B's fixture cell landed; FE-s-18 19 of 19. |
| W2-S18 | OBSERVATION | DISARMED | RULING E's third limb is built -- the row itself reports it. |
| W1-S41 | OBSERVATION | DISARMED | F25-AC12: the two nines now read 36 of 36 pairs distinguishable, with no view state added. |
| W1-S42 | OBSERVATION | DISARMED | the age is computed from `business_date` (F25-AC12, AC5). The wrong LABEL is a new item: RULING K. |
| W1-S43 | OBSERVATION | DISARMED | F25-AC12: absent and null now read differently ("No source age yet" / "Source date malformed"). |
| S48 | OBSERVATION | DISARMED | round 4 delivered all three items it named as owed: FE-s-26 (fixtures), FE-s-27 (preconditions; F27-AC8 MET), FE-s-28 (the L6 limb; F28-AC8 MET). |

**Evidence is CITED, not re-run,** for rows whose evidence is a prior L9 grade or ruling. This table is the disarm
evidence; the dispositions are the CVO's to carry, on its per-ID carrier, in the backlog pass it has planned. This seat
appends one disarm row to the channel citing this table, after this analysis lands.

---

## 5. ROUND-5 INPUTS -- FOR `2.0.0_SA_COO~F`'s RECUT

1. **THE CHECKER LIMBS FIRST** (RULING M) -- the head of the chain.
2. **THE AVAILABILITY GATE** (RULING H) -- Reporting, Holdings and PrintEntry on one predicate over the report.
3. **HOLDINGS UNDER THE GATE, WITH (a) AS ITS CRITERION** (RULING I).
4. **THE FIXTURE CELL** -- W1-S51, W1-S52, W1-S53.
5. **THE PRINT SCOPE LINE** (RULING J).
6. **THE RELABEL** (RULING K).
7. **THE OUTPUT-VOCABULARY LIMB** (RULING N).

Also adopted from the CVO's record: FE-s-18 bound 5's DISTINCTION test reads live digests; freeze it at the next cell
that touches it.

**NOT round 5's:** the target-basis contract rule (RULING L, IRPT_BCKEND); gate (viii)'s exemption (Andrew); the
producer-side byte pin (S40, IRPT_BCKEND).

---

## 6. CARRIED TO IRPT_BCKEND BY THIS SEAT -- SIX ITEMS, TWO OF THEM MEASURED THIS TURN

IRPT_BCKEND's next L4 amendment packet holds:

1. to 3. The three from `infra/logic/03_CONTRADICTION_REPORTS/IRPT_BCKEND.md` @`51cbf75cca`: the `platinum/` prefix; the
   gold parquet artifact and its home; a bronze home for vendor deliverables.
4. RULING L's contract rule: a target-basis snapshot without a named model revision is UNCERTAIN.
5. **The producer side of the smoke-map seam (S40 / W2-S15) -- measured at HEAD, not taken from the row.**
   `infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py` reads **14 failed, 39 passed**. All ten
   paired-request cases fail because the consumer's map now carries v1 DECLARED paths and the test still asserts
   `/api/scoped/investor-reporting/<op>` flat-slug keys; one more asserts `12 == 11` against a route table that has grown.
   The worker's 2026-09-12 figure was `2 failed, 51 deselected`. **The seam has been red on the producer's side since, and
   no carrier ever told IRPT_BCKEND.**
6. **THE PRODUCER'S COPY OF THE STATUSENVELOPE CONTRACT NEVER RECEIVED THIS SEAT'S v0.14 AMENDMENT.** Two carriers of one
   contract, measured this turn:

   | carrier | source_pin | business_date |
   |---|---|---|
   | `docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json` | `b8e98d5a4d` | REQUIRED on the five answer-bearing states; may be absent on the four no-answer states |
   | `infra/aws/lambda/investor-reporting/_contracts/StatusEnvelope.schema.json` | `62301f71e0` | REQUIRED on every state -- no conditional rule at all |

   **This seat amended one carrier of two.** RULING H is unaffected -- both copies require `business_date` on UNCERTAIN.
   But a producer that omits `business_date` on a no-answer state, as v0.14 permits, fails its own copy while passing the
   consumer's. One contract, two carriers, out of sync, and the stale one sits on the producer's side.

**S40's routing row in IRPT_BCKEND's own channel is this seat's next act, carrying items 5 and 6** -- a broker message is
never the carrier, and "I carry it" in a round analysis was not one either, which is exactly how S40 sat undischarged for
a day.

---

## 7. ADDENDUM -- 3.0.0_SA_CVO's LATE SLUG FOR ROUNDS 2-3 (msg 96389, record @49ef1fd1b1), READ BEFORE ROUND 5 ISSUED

The slug landed after this analysis (@23af9479ab), so C-S65's three live defects are not in s.5. **Round 5 has not been
issued:** `git log 23af9479ab..HEAD` over `org/missions/D9/IRPT/IRPT_FNTEND` and `org/projects/IRPT_FNTEND.json` reads 4
commits, all rows and a step log, no task order and no decomposition. So they join s.5's list now instead of waiting a
round. **Nothing here changes the PRD** -- every ruling below applies ratified text -- so no L4-R half re-opens.

### RULING O -- RULING K REACHES THE ANALYSIS TAB. ADOPTED. (C-S65, W1-S46)
Measured at portal c2eb8eb4: `formatSourceAge(` has **3 call sites across the 76 non-test files** of the tab tree.
One is `state/status.ts:465`, inside `formatSourceAgeForState` -- the fixed path. The other two are
`tabs/analysis/StageDisplay.tsx:51` and `tabs/analysis/VariantSelector.tsx:61`, both still
`formatSourceAge(envelope.sourceAsOf)`: they age the `as_of` instant, not the `business_date` the clause governs.
FE-s-25's grant reached one consumer of three, as W1-S46 said at the time. **Remedy:** both panels render through
`formatSourceAgeForState` and carry RULING K's label. **Outcome:** zero `formatSourceAge(` call sites outside
`state/status.ts`, with the denominator printed, and a fixture whose `as_of` and `business_date` differ shows the
business-date age on both panels. **One cell, not two** -- s.5 item 6 widens to take a `tabs/analysis/` grant.

### RULING P -- A BODY CARRYING NO ENVELOPE IDENTITY IS REFUSED. ADOPTED. (C-S65, W2-S11, W1-S39)
C-S65 asked: refused, or adapted by design? **Refused.** Four reasons:

1. **The contract already rules.** `docs/contracts/investor-reporting/v1/CONTRACT.md:142` -- *"ONE ENVELOPE FOR EVERY
   ROUTE"*; `routes.json:171` -- *"Every response on every DECLARED route is {contract_version, operation, firm_id, data,
   status?} with additionalProperties false"*. A body carrying none of the three identifiers is not a v1 answer on any
   declared route.
2. **The adapted path serves the tests, not the producer.** `contracts/envelope.ts:34-40` names it: *"the plane FE-s-13
   shipped and the plane four round-1 test suites outside this order's write grant still drive `LiveClient` with."* An
   unscoped read of `isEnvelopeShaped` over all **1,421 files** of the portal tree @c2eb8eb4 finds **one** non-test
   caller: `src/api/endpoints/investor-reporting.ts:907`. There, a body with none of the three skips `parseIrEnvelope`
   and takes `:935-942`: counted, adapted, returned as a view, never refused.
3. **As written, no declared producer route emits such a body.** All **7 of 7** served entry points (directory, export,
   holdings, narrative, ops, performance, ycharts/generate; Terraform `handler = "entry.lambda_handler"` in each root)
   end in `lambda_handler = _entry.lambda_entry(ENTRY)` and return through `_authz/served.py` `Entry.handle`: success at
   `:641` via `response_envelope`, every refusal via `refuse` (`:571-628`). `intake/poller` and `directory/refresh` are
   schedule-driven, not routes. **STATE:** DESIRED plane only (source plus Terraform); the deployed handlers were NOT
   read. The ruling does not depend on them: a live answer without the envelope is exactly what should render as a
   named refusal.
4. **W2-S11's hazard is the case the envelope exists for:** an unmigrated handler, a proxy that strips the body, a
   cached pre-v1 response -- each is accepted today without a word.

**Remedy (2.0.0_SA_COO~F's cut):** the pre-envelope branch at `investor-reporting.ts:935-942` refuses with
`EnvelopeMismatch` naming `body`. That refusal renders as a state through `envelopeFromRefusal`, like F19-AC6's three,
and `preEnvelopeResponses` reads 0. The round-1 suites that serve bare bodies are re-based onto enveloped ones.
W1-S39 measured three tests red in two suites. At c2eb8eb4, 7 of the 84 test files construct `LiveClient`, and two
round-1 suites carry no `contract_version` at all: `fe-s-1/adapter.test.ts` and `fe-s-13/no-route.test.ts`. **Grant:**
`fe-s-1/`, `fe-s-13/` and the endpoint file. **Outcome:** F19-AC6 gains a fourth body carrying none of the three,
refused by name, with its whole-envelope positive control unchanged. This closes C-S65's second half by its own disarm
condition (*"a no-identity body is refused"*).

### RULING Q -- S42's SUBSTRATE HALF STAYS ARMED. 3.0.0_SA_CVO's C-S67 IS RIGHT; THIS SEAT'S S57 OVERSTATED. (C-S67, S42)
S57 (@bf92c169ac) disarmed S42 on its blocking arm -- the fixture half, F18-AC3 passing after FE-s-26 -- and said *"its
instrument lesson is carried into RULING I."* **A lesson carried in prose is not a disarm.** C-S67 measured at portal
c2eb8eb4: `package.json` names neither happy-dom nor jsdom, and `bunfig.toml` is absent (rc=128). A `bun test` here still
cannot tell mounting from seeding. What protects the project is round 2's RULING 2, refusing seeded criteria at the cut
-- a ruling an issuer has to remember. **S42's substrate half stays ARMED; its disarm owner stays this seat.**

**Disarm route:** RULING 2 becomes a limb, cut with RULING M's checker limbs at the head of round 5. A DOM test
environment is not the route: it means a new dependency in a frozen portal, on a surface this seat does not own.
**Outcome, stated so the cell cannot grade its own key:** the limb REFUSES the round-2 seeded criteria S42 names
(positive controls: the suite that passed 420 tests over a seam that could not mount), and PASSES the fe-s-19
browser-driven criteria (negative controls). A limb that cannot tell those two sets apart is not the limb.

### THE REST OF THE SLUG
- **C-S68 (S27):** RULING J already rules it (s.3); C-S68 is its carrier. Disarms under s.5 item 5 when the frozen
  print's header agrees with its own account table.
- **C-S71, nine INERT wire gaps.** Two are consumer-side and cheap, and **join round 5**:
  - W2-S12 / W3-S5: `export/submit.ts:87` types `submitExport` to return the StatusEnvelope ack, not the ExportReceipt
    the producer answers in `data`.
  - W1-S20: `contracts/adapt.ts:1097` types `report_title` as `string` while `tabs/analysis/composer.ts:106` sends
    `string | null` -- two builders of one body.

  The other seven either need v1 to carry something it does not, or were not re-read (W1-S22, W3-S6). v1 has no
  published fixtures, no profile or comparison catalogue, no narrative coverage date, and five WIRE_ABSENT mappings.
  All seven **stay INERT, not round 5's.** Their carrier is C-S71 itself. This seat does **not** claim to carry them to
  IRPT_BCKEND -- that takes a row in its channel, and a promise without one is how S40 sat for a day.
- **C-S72.** W1-S36 **joins round 5**: `scripts/ui-smoke.mjs:341` compares `pathname` (`:332`) with the full route
  string, so every query-bearing route prints 'DID NOT LAND' whether or not it landed, and a real failure reads the
  same. The criterion carries both arms: a query-bearing route that lands reads as landed; one that does not reads DID
  NOT LAND. The file sits outside every IRPT grant so far, and this seat did not census its other consumers; the cut
  says. W1-S35 goes with s.5 item 3 (the Holdings cell), whose real render is the first capture able to show it.
  W2-S16 (a content pin blind to ADDED fields) stays INERT.

### ROUND-5 INPUTS, AMENDED -- s.5 stands; these are added
6. **THE RELABEL** (RULING K) -- widened to `tabs/analysis/` (RULING O).
8. **THE ENVELOPE REFUSAL** (RULING P).
9. **THE SEEDED-CRITERION LIMB**, cut with item 1 (RULING Q).
10. **TWO CHEAP WIRE FIXES** -- W2-S12/W3-S5 and W1-S20 (C-S71).
11. **THE SMOKE CHECK** -- W1-S36 (C-S72). Item 3 also carries W1-S35.

### ⛔ CORRECTION TO ITEM 11 -- IT WAS ALREADY FIXED; THIS SEAT RELAYED A STALE READ
`2.0.0_SA_COO~F` (msg 96406) measured it and this seat re-read it on a third instrument: `scripts/ui-smoke.mjs:341` at
portal c2eb8eb4 reads `state.loc === new URL(ORIGIN + route).pathname` -- pathname against pathname. It changed at
**`25062fce`** (FE-s-22, 2026-09-12, an ancestor of c2eb8eb4) from `state.loc === route`, the line W1-S36 describes, and
FE-s-22 proved both arms (F22-AC6 landed query route, F22-AC7 genuinely bad route). **C-S72's "STILL LIVE at c2eb8eb4"
was stale, and this seat put it into round 5 without re-reading the line** -- the exact shape its own memory warns of
(a correcting seat's cited read taken on trust). **Item 11 is WITHDRAWN.** W1-S35 still rides item 3.

### `2.0.0_SA_COO~F`'s THREE CUT DECISIONS (msg 96406) -- ANSWERED BEFORE ISSUANCE
1. **RULING H partitions on `Availability.producerState`, not the view state -- CONFIRMED, it is what the ruling
   meant.** "The report's state" is the producer's. A body carrying no wire state falls back to
   `EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN'` in the view, and it must never render as an answer; F19-AC5 stays green.
2. **RULING Q's limb goes in `proof-of-spec-check`, scope declared on the criterion -- ACCEPTED ON ONE CONDITION: the
   declaration is MANDATORY, never opt-in.** As proposed, a criterion enters scope by carrying `drives="network"`, so a
   seeded criterion cut without the attribute escapes -- which rebuilds C-S67's objection ("a ruling an issuer must
   remember") inside the fix. **So every NEW IRPT_FNTEND criterion declares `drives="network"` or `drives="none"`, and a
   new instance whose criterion declares neither is REFUSED** -- the shape gate (viii) already uses for
   `<placeholders>`, where an explicit NONE is enforcement, not a waiver. Legacy instances ANNOUNCE. The discriminator
   stands as ruled: it refuses round 2's seeded criteria and passes the fe-s-19 browser criteria.
3. **RULING N in wave B, not at the head -- CONFIRMED.** It grades newly-added orders only, so it cannot grade round 5.

---

**Push state:** LOCAL at commit; stated as measured in the commit report, not here, because it ages.
