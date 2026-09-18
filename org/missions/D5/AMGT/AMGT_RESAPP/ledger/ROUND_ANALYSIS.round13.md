# AMGT_RESAPP -- ROUND 13 ANALYSIS (L10). The CTO's ONE answer to the round-13 slug.

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-18 ~19:xxZ. **Limb:** L10, Rule 27. **Addressed to:** `2.0.0_SA_COO~Z` (the ONE
send), copy `3.0.0_SA_CVO~Z`, `4.0.0_SA_CRO~Z`, `0.0.0_AB_MSTR~Z`.

**INPUTS, each at a commit-ish.**
- Slug: `surprise-channel/remediations/REMEDIATION_v13.md` @`0f1dcbc631` (20 rows; W31-S3's clock flipped DISARMED by
  `f17ec013f4`), with `ADJUDICATION_v13.md` (C-S292..C-S321).
- COO packet: `ledger/ROUND13_L8_PACKET_20260918.md` @`9e0ff02a70`.
- The panel briefs, read against the PRD one row per finding: `org/tier1_exec/1.0.0_SA_CTO/deliverables/
  CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md` (Lead Panel, Thesis, Exec Management, Peers, Model, and the three-name
  instantiation validation @`b527b93214`). Each brief was checked against its NEWEST commit.
- PRD `prd/AMGT_RESAPP_PRD.md` v0.10, ADMITTED. **This analysis carries a PRD ADDENDUM, v0.11** (s.8): it re-opens BOTH
  L4-R halves.
- **Timing, by Andrew's word.** ~17:2xZ: the addendum waits until the panel briefs are in. ~18:2xZ and ~18:4xZ: *"After you
  integrate that [the Model brief], we may proceed; no need to wait for Posture brief"* and *"the greater fabric does not
  need to be held up on that."* The Posture brief is NOT waited on; its rows land in a later addendum.
- **The frame, by Andrew's word ~16:3xZ:** *"the more important thing than establishing a pipeline itself is the process
  behind full 'security analysis' backend instantiation for a new security."* **So round 14 is organized by the STAGES OF
  INSTANTIATING A NEW SECURITY, not by panel** (s.4).
- **Capacity, by Andrew's word ~18:2xZ:** this device is dedicated to AMGT_RESAPP and its CPU and memory are to be used.
  `2.0.0_SA_COO~Z` measured the ceiling at 16 concurrent workers, bounded by the serialized drain, not CPU (msg 23726).

---

## 1. THE GRADE

**Round 13 is ACCEPTED.** 97 of 97 orders terminal on the gate's own resolver (`rk-26` WITHDRAWN @`5dc9089ca7` on Andrew's
*"write off the frontend TO"*); 52 of 52 items dispositioned. Acceptance over the round's 15 orders: **26 PASS / 3 FAIL /
0 UNVERIFIABLE**, and all three FAILs are CRITERION defects, graded as the CVO gave them and never flipped:
`rk-23` AC1 (a raw slash where the page sends `%2F`), `rk-20` AC1 (a shape the world never had), `rk-30` adapter AC1
(measured values the round never committed to produce -- this seat's ruling `Z-S173`, adopted as the grade). No judgment
grade is recordable: `rk-26` has no instance, and `rk-2` AC6 / `rk-8` AC4 stay NOT_EVALUATED naming the missing
instrument -- an authenticated browser capture through the real edge, which mandatory MFA blocks (s.3.5).

**What round 13 moved, on the served plane, over the 33 keyed names** (population of record `crosswalk/v1/2026-09-15.json`,
MEASURED = 33; measured by this seat 2026-09-18 ~16:xxZ, keys sent in the page's own `%2F`-encoded shape): thesis answers
**33 of 33**; model figures **33 of 33**; drafted prose **12**; posture **33** (from 2); management **12 by status, 7 with
officers** (from 5) -- the other 5 served rosters are EMPTY; scores with a value **0**; all 13 read routes answer. Round 13's
page work is on `origin/DEV` @`625a0888`, which is durable and NOT reachable: nothing deploys to DEV by design.

**Three figures in circulation this round were weaker than they read, and the record now says so:** "34 keyed names" (33;
the model store is wider than the population, and a key census split `BP/_LN_Equity` at its own slash); "management 12"
(7 carry officers); and "389 of 389 sentences PASS the verbatim check" -- a sentence with no quoted span passes VACUOUSLY
(validation D18: 17 of 39 for CAT, 16 of 40 for CSL).

---

## 2. WHAT THE WALK FOUND -- the one pattern worth naming first

The panel walk and the three-name validation converge on one sentence: **every stage except the chatter Lambda needs a
person to run it, and every reader keys on the POOL crosswalk -- so a security produced end to end still renders nothing
until its identity lands in the pool.** That is the gap round 14 closes.

**And one root cause explains why so many producers cover the pilot names and miss everyone else:** three production code
paths read or write a WORKER'S deliverables folder -- the unit map (`integrations/bloomberg/research/model_block_pull.py:286-288`
reads `deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json`, the cause of all 348 Model refusals), the SEC ticker cache
(`lib/research/identity/build_universe.py:503-507`, worker `~19` -- a 33-row cache whose miss is REPORTED as absence from the
full 10,422-row table, so Caterpillar is missed), and the peer candidate universe (`lib/research/peers/universe.py`,
worker `~21`, rewritten even under `--dry-run`). A worker's folder is the proof artifact of ONE task order and covers
whatever names that worker handled. **One constraint, `C-PRODUCTION-HOME`, retires the class** (s.8).

---

## 3. RULINGS -- the seven slug rows this seat owns, and one unowned residue

### 3.1 One issuer per round (S154, OPEN). **RULED: a TOOL cell, keyed to the round.**
Round 13 was issued twice by two continuations of one seat serial. A refusal keyed to the SERIAL cannot see it; the L6 gate
refuses a second issuance into a round that already has one, keyed to the ROUND. If a collision happens anyway, the SECOND
issuance is withdrawn and its orders re-cut into the first by its issuer. Cell **R14-T1**.

### 3.2 Peers V (S162, OPEN, ARMED/DISARMED 00:12Z). **RULED: part (3) is ANSWERED; parts (1) and (2) are cells.**
Andrew answered the measure question by adopting the Peers brief (*"Agree with everything youve got"*, @`a2fdbad164`):
floors 5 peers / 5 per measure, `|M| >= 3` unchanged. Part (2) -- SEDOL-stem peer identity -- is OVERTAKEN by his
Seeking-Alpha design (SA returns US listings and ADRs), so it is not built. Part (1) -- peers_v's EMPTY `absent_reason` --
is a one-field fix. **This seat's L4 reading, for the CVO to sign:** the measure runs AS WRITTEN on its own Bloomberg
`FIELDS` pulled for the SA peer tickers -- SA chooses WHO, the measure's own fields say WHAT; feeding it SA's metrics would
be a translation layer. Cells **R14-P2**, and the empty-reason fix inside it. `Z-S164`'s forward path is withdrawn by
`Z-S174` and overtaken here.

### 3.3 Acceptance at L10 (S169, OPEN, ARMED; disarm owner `2.0.0_SA_COO~Z`). **RULED: a TOOL cell; hand sweep until then.**
The census counts an order terminal on a VALID instance whatever its verdicts, so a close can read clean over failing
criteria. The L10 precondition gains an acceptance read: per criterion, over every order of the round, in three classes
(PASS / FAIL / UNVERIFIABLE), denominator printed. Until the tool lands, every close runs the sweep by hand, as this one did.
Cell **R14-T3**.

### 3.4 Slash-safe routing (W27-S10, OPEN, ARMED). **RULED: remove the question rather than answer it.**
Five instruments are closed on whether the gateway forwards `%2F` encoded; the sixth -- an authenticated edge capture -- is
blocked by MFA. So `handler()` is made INDIFFERENT to an encoded versus a literal slash in `security_key`, and the question
stops mattering. It moves served output: never-widen pair. Cell **R14-T7**.

### 3.5 MFA and the capture (W31-S3, DISARMED within this project by `Z-S175` @`e53c49af20`). **RULED there; the estate half is Andrew's.**
No order is cut whose criterion needs a HEADLESS authenticated session. A criterion that needs the authenticated page is
either HUMAN-IN-THE-LOOP (one person enters the code once in a headed session; MFA stays on for everyone, nobody exempted) or
a JUDGMENT criterion graded by a human at L9. A criterion that needs only the data tests the adapter directly and says so.
**The ~27 frontend-dev constitutions in OTHER projects that rely on the same login are a card** (s.5).

### 3.6 The peer universe cache (W32-S4, OPEN). **RULED: under `C-PRODUCTION-HOME`.** Cell **R14-H1**.

### 3.7 The Terraform plan blocked by a missing build zip (W34-S1, OPEN, ARMED). **RULED: a build cell.**
`chatter-axis-schedule.tf:124` must tolerate the absent `.build` zip, or the build step is committed, so an unrelated
resource can never block a targeted plan. Infra, `CLOUD_OPS_OR_ETL` lane. Cell **R14-T5**.

### 3.8 The unowned residue -- the other 11 `drafting/v1` objects (slug body, carried only on closed W27-S3). **RULED: DEFERRED, placed.**
The 11 were derived from analyses written BEFORE the analyzer emitted driver points, and Andrew ruled *"I dont care about
rerunning until the process is completely validated end to end"*. Rebuilding drafting from stale analyses buys nothing. It
is carried as DATA in the round-14 issuance, owner `2.0.0_SA_COO~Z`, re-opened only after the analyzer is validated (R14-F6).

---

## 4. THE ROUND-14 CELLS -- by instantiation stage; decomposition, chaining and fan-out stay the COO's

**Built for width.** The chains below share no write surface unless the table says so, so they can run concurrently; the
COO's measured ceiling is 16 in flight. Within a chain, cells that edit the SAME FILE are sequenced (marked `->`); every
other pair is independent. Every cell is PROVEN ON THE VALIDATION NAMES (CAT, CSL, Keyence -- one US, one English
international, one non-English) or on a dry run. **No cell is a fleet run or a re-run** (Andrew's word stands); a run on
the three validation names is the validation he set as the bar.

| chain | cell | obligation | serves | co-sign? |
|---|---|---|---|---|
| **I -- identity (the entry point)** | **R14-I1** | ONE "add a security" step: one Bloomberg call lands identity in the POOL crosswalk -- name, exchange, LEI, SEC id, CIK, the yellow key appended; registers the four unregistered corpus folders (Alphabet, Eli Lilly, Quanta Services, UnitedHealth) | FWD-2, V1 | pool writes |
| | **R14-I2** | battery step 1 reads the LIVE SEC ticker table with the existing name guard; a miss is reported against the table actually read | FWD-18, V2/D1 | no |
| **H -- production home** | **R14-H1** | `C-PRODUCTION-HOME`: the unit map to config beside its producer; the SEC cache and the peer candidate universe to the pool at builder-made addresses; **a dry run writes nothing** | S-W32-S4, M1, V7/D24 | no |
| **M -- model block** | **R14-M1** | the unit map built for EVERY name; re-derive from the raw bytes already landed (no new pull). Clears the 348 refusals | FWD-10, M1 | yes (served figures change) |
| | R14-M2 `->` M3 `->` M4 | M2 the rolling history window (`HIST_END` fixed today); M3 forecasts FY1-FY3 from Bloomberg `BEST_` with the explicit override, SA fallback per cell, source and fiscal year on every cell, headers from `BEST_PERIOD_END_DATE`; M4 the five missing sheet rows and `CIE_DES`/`CIE_DES_BULK` as pulled fields (the header description) | FWD-1, FWD-16, M2-M5, L8 | yes, each |
| **F -- filings** | **R14-F1** | the battery in code: US order EDGAR -> Bloomberg-resolved CIK -> IR page; each step's acceptance test (right ENTITY, current, known document FAMILY); UNRESOLVED-SOURCE carrying every attempt; the family recorded. Includes tier 1 (Bloomberg `CENTRAL_INDEX_KEY_NUMBER` as a CIK fallback, +6 names) | FWD-18, T1, T8, T10, T15 | pool writes |
| | **R14-F2** | a document layer for non-EDGAR reports: PDF reflow (9.3% -> 91.6% coverage measured), family-keyed cutting, and an EMPTY cut recorded as a FAILED cut with its reason; the 20-F `riskfactors` wrong-object fallback removed (D9) | FWD-18, V3, E10 | no |
| | **R14-F3** | TRANSLATION, design A: analyze the original, translate the output; Unicode passages (`passages.py:67-79` keeps 6.8% of Japanese today), pre-cut citation blocks, a character-level verbatim rule | FWD-18, T13, V4 | no |
| | **R14-F4** | the verbatim gate closed: every drafted sentence carries a verbatim span or is held; pass counts report vacuous vs on-span | FWD-9, FWD-18, V6/D18 | yes (served prose) |
| | **R14-F5** | the batch made correct BEFORE it can ever run: an analyzer version that MOVES with the output contract, then skip-on-unchanged (in that order, or the skip locks the stale analyses in); dedupe by CIK; one writer of `drafting/v1`; the newest universe vintage, not a typed date; the task launcher path quoted and read back | FWD-18, T4-T7 | no |
| **E -- management** | **R14-E1** | honesty first: the CEO line prints four states honoring the object's own `absence_class`; an empty roster renders its reason; a zero-officer object is not SERVED | FWD-17, E1, E4, E11 | yes |
| | **R14-E2** | the batch census: real filings only, never a placeholder; keys cut slash-safe (`batch.py:81-84`); launcher quoted, universe unpinned | FWD-17, W32-S3, E6-E8 | no |
| | **R14-E3** | one pool: `compute_pool` reads the newest object per name across dates, as its own docstring and the contract say | FWD-17, E5' | yes |
| | **R14-E4** | the roster parser: a title is never a name (D20); the "Name (age) Role (year)" table (D21); original-script names kept (D22); the age-in-role mis-split; the HAL / INTU / KMB section shapes | FWD-17, V5, E2, E3 | pool writes |
| | R14-E5 `->` E6 | E5 Andrew's card 1: the Bloomberg `COMPANY_EXEC_OFFICERS` fallback for the TABLE only, labelled, `roster_source` on every object, the filing's own failure reason travelling with it; E6 the CEO search as a SERP on the name with an organizing agent -- FAILED distinct from EMPTY in the primitive FIRST, title and snippet kept, a namesake test, every fact quoted verbatim | FWD-17, cards 1 and s.9 | yes, each |
| | R14-E7 | Lusha enrichment as an instantiation step (card 2): domain ONLY from the battery's verified site; no verified domain = NOT ATTEMPTED with its reason | FWD-17, card 2 | **gated on R14-F1** |
| **P -- peers** | **R14-P1** | the Seeking Alpha peer path: entity-tested SA slug (`ROG` = Rogers Corporation is the standing negative control), the four GETs through the existing `rest_fetch.py`, raw landed before derivation (at a builder-made address), derivation to R-1 with a source on every cell and the Bloomberg growth fill -- **each PEER ticker's Bloomberg join also passes a name-agreement check**, the same trap as ROG; a REHARVEST stops the run. **Proven on the validation names only until card 3(a)** | FWD-8, P1-P7 | pool writes |
| | R14-P2 `->` P3 | P2 Peers V over the SA set at floors 5/5 on its own Bloomberg `FIELDS`, and peers_v's empty `absent_reason` fixed; P3 the page renders SA's shape with per-cell source labels | FWD-8, S162 | yes, each |
| **L -- lists** | **R14-L1** | a ranking never includes a member with no signal; every EMPTY generation carries `empty_reason`, written by BOTH generation writers and shown on the panel | FWD-15, L2, L5, V8/D25 | yes |
| | **R14-L2** | MEASURE, not build: why `publication-links/v1` covers 3 names -- ingestion (nothing fetched) or association (fetched, not keyed to the name). Its answer is this seat's next L4 | FWD-4, FWD-11, FWD-16, L3, L4 | no |
| **T -- tools and process** | **R14-T1** | S154 (s.3.1) | process | no |
| | **R14-T2** | S153: every order issued with a `<status>` element, checked on the newly-added limb | process | no |
| | **R14-T3** | S169 (s.3.3) | process | no |
| | **R14-T4** | W34-S2: a co-signed direct act either carries a minted order or the lane gate reads a signed pair as a grant | process | no |
| | **R14-T5** | W34-S1 (s.3.7) | infra | no |
| | **R14-T6** | W31-S1: portal-cell worktrees provisioned with `portal/` checked out; the issuance says which | process | no |
| | **R14-T7** | W27-S10 (s.3.4): `handler()` slash-indifferent | FWD-13 | yes |

**Count: 27 cells in 7 chains, of which 20 are independent of every other cell** (bold ids). That is wider than the COO's
16-worker ceiling on purpose: the ceiling is the DRAIN, so the COO waves them, and nothing waits on a sequence that does
not exist.

**Not a cell, and why:** Lead Panel cards A and B (prior-day prices on the daily job; the +5% POSITIVE-move Breakout floor)
are ONE direct Andrew-authorized act, B first, already sequenced (msg 23684) with `2.0.0_SA_COO~Z` executing -- the addendum
records them as ratified text. The Refresh queue needs its DEFINITION at L4 before any cell (L12). Tier 2 (ESEF) and tier 3
wait on Andrew's international battery order (s.5).

**One co-sign discipline for the round:** every cell marked `yes` moves served output and gets a never-widen pair naming its
blast radius, each writer COUNTED, and a rollback read from the LIVE pre-act hash of THAT act. Each deploy opens its
change-management entry BEFORE the first live act and is committed, not staged.

---

## 5. CARDS AT ANDREW -- each with this seat's recommendation

1. **The international filings battery order.** His US order is ratified; for international he said *"I dont know but we
   need a plan"*. PROPOSED (Thesis brief s.8.2): EDGAR by ticker -> EDGAR by Bloomberg CIK -> ESEF/UKSEF by LEI -> company
   site -> national regulator -> UNRESOLVED. **REC: YES**, with the company site BEFORE the regulator -- measured, it covers
   8 of the last 9 with one generic adapter.
2. **The Model cases (Upside / Base / Downside).** EPS now has a source; the multiple and the scenario spread are Opal's
   judgment. **REC:** base = consensus EPS x the security's own trailing-median multiple; upside and downside at fixed,
   labelled spreads Andrew names -- or leave ABSENT with that reason until he does.
3. **Seeking Alpha as a PRODUCTION source -- and its terms of use.** ⛔ **A real conflict, found drafting the Peers clause:**
   the PRD's `C-SA-VENDOR-WORD` (`:907`) marks Seeking Alpha production use NOT AUTHORIZED, and the Peers design runs it once
   per security at instantiation -- production use. Andrew's *"Agree with everything"* adopted the design but did not say it
   lifts `C-SA-VENDOR-WORD`, and this seat will not read that into it. Separately `C-SA-TERMS-BEFORE-SCHEDULE` bars a
   SCHEDULED read until the terms are read and his ruling recorded. **REC:** (a) YES to SA as a per-security production
   source at instantiation, recorded as lifting `C-SA-VENDOR-WORD` for the Peers path by name; (b) a task to read the terms
   now, so a scheduled refresh can follow his ruling. **Until (a), R14-P1 is built and proven on the validation names only.**
4. **Lusha inside the validation** (about 6 credits). **REC: YES** -- card 2 made Lusha an instantiation step, and a step not
   exercised in validation is not validated.
5. **Should a drafted sentence with NO verbatim span be HELD, or served labelled?** Measured: a sentence with no quoted span
   passes today (17 of 39 for CAT, 16 of 40 for CSL). Holding them withholds roughly 40% of drafted prose and reverses the
   v0.7 choice to keep passage support and exact quotation separate. **v0.11 serves them LABELLED "not anchored to a quote"
   and makes every pass count print its split**, which is honest without withdrawing prose. **REC: HOLD** -- a thesis sentence
   that cannot be tied to the filing's own words is the claim FWD-9 exists to stop being mistaken for evidence; the label is
   the interim.
6. **Headless authenticated capture, estate-wide** (the other ~27 frontend-dev constitutions). **REC:** retire it as a class
   and correct `portal/.frontend-dev/auth/README.md`, which still documents both logins as working; separately, move the
   two plaintext passwords out of the tracked `credentials.json`.

---

## 6. THE 20 ROUND-13 REMEDY ROWS -- dispositioned

| disposition | rows | grounding |
|---|---|---|
| **REMEDIATED in round** (7) | S155, S159, W27-S3 (for BA), S149, S168, W27-S11, W33-S1 | the CVO's REMEDIATION_v13 states and this seat's per-act verifications (Z-S161/163/165/167/168/172) |
| **CARRIED to a round-14 cell** (11) | S154 -> T1; S153 -> T2; S169 -> T3; W34-S2 -> T4; W34-S1 -> T5; W31-S1 -> T6; W27-S10 -> T7; W32-S4 -> H1; W32-S3 -> E2; W32-S2 -> E1 + E7; S162 (1) -> P2 | s.3 and s.4 |
| **ANSWERED by Andrew, remainder a cell** (1) | S162 (3) | the Peers brief adoption, s.3.2 |
| **DISARMED in project, estate half a card** (1) | W31-S3 | Z-S175; card 5 |
| **OWNED ELSEWHERE, carried** (1) | W31-S2 -> `0.4.0_DT_ClientPlatform` | the npx decoy is a portal-config act in the DT lane |

**Denominator: 7 + 11 + 1 + 1 + 1 = 21 dispositions over 20 rows** -- S162 appears twice because its parts land differently.
Round-12 rows still open (S117, S119, S121) stand as filed and are not re-graded here.

---

## 7. WHAT EACH SEAT OWES NEXT

| seat | owes | gated on |
|---|---|---|
| `3.0.0_SA_CVO~Z` | sign the RATIFIED-TEXT half of PRD v0.11 (s.8) | this delivery |
| `4.0.0_SA_CRO~Z` (or a live `2.0.0_SA_COO~Z`) | sign the BRIEF half of PRD v0.11 | this delivery |
| `2.0.0_SA_COO~Z` | L5 decomposition + battery for the 27 cells, then the ONE L6 issuance, fan-out up to its measured 16; the W27-S3 residue carried as data | both halves SIGNED (LIMB 6 refuses a new order against an unsigned half) |
| `2.0.0_SA_COO~Z` + `1.0.0_SA_CTO~Z` | a never-widen pair per served-output deploy | each cell's deploy |
| `1.0.0_SA_CTO~Z` | L4 on the chatter source after R14-L2 reports; the Refresh queue definition; the Posture rows when that brief lands | R14-L2; the Posture brief |
| `0.0.0_AB_MSTR~Z` | the six cards to Andrew | nothing |

---

## 8. THE PRD ADDENDUM -- v0.11

Unlike round 12, this round's rulings do NOT sit inside ratified text, so the PRD moves. **Both halves re-open.**

**Ratified-text half (ENDPOINT + CONTRACTS), `3.0.0_SA_CVO~Z` signs:**
- `C-FILINGS-ANALYZER` -- the source is the per-security BATTERY's winning document; Bloomberg supplies keys, never text;
  document family recorded; translation design A; no re-run before validation.
- `C-EXEC-MANAGEMENT` -- Andrew's cards 1 and 2 and the CEO search, with `roster_source` and the travelling failure reason;
  a zero-officer roster is not SERVED; one pool across dates.
- `C-SIMILARITY-RANKER` -- split: FWD-8's peer set moves to a new `C-PEER-SET-SA` in Seeking Alpha's shape, with
  `C-PEERS-V-FLOORS`; **FWD-19's comparable stays under the existing ranker until the Posture brief is integrated.**
- the ENDPOINT's stale "Eighteen outcomes" at `:457` corrected (the v0.9 note claimed it was fixed; the bytes were not).

**Brief half (s.0 and s.2-s.9), `4.0.0_SA_CRO~Z` or a live COO signs:**
- `C-UNIT-MAP-MEASURED` -- built for every name at instantiation.
- `C-VERBATIM-GATE` -- every drafted sentence carries a span; vacuous passes reported.
- `C-SERVER-SIDE-RANKING` -- no rank without signal; `empty_reason`.
- new: `C-MODEL-FORECASTS` (Bloomberg primary, SA fallback, the fallback waiting on `C-SA-VENDOR-WORD`), `C-MODEL-WINDOW-AND-ROWS`,
  `C-PRICE-BREAKOUT-FLOOR` (card B: +5% UNSMOOTHED over the 30-day mean, not a `MIN_ABSOLUTE_JUMP` entry), `C-PRICE-DAILY-LEG`
  (card A), `C-DESCRIPTION-LINE` (a validated drafted sentence first, Bloomberg's field second -- reversing today's reader order).
- a new section 10: THE INSTANTIATION STAGES -- every stage in the battery's shape (ordered attempts, one acceptance test, an
  explicit terminal state, the route recorded), with the validation's measured trigger per stage; and three new pipeline
  constraints there: `C-INSTANTIATION-ENTRY`, `C-PRODUCTION-HOME` (a pipeline-shape rule, the same class as the brief half's
  `C-STAGE-PERSISTS`, so the brief-half signer carries it) and `C-VALIDATION-NAMES`.
- the stale `:353` citations of `C-LIST-OWNER` -- five, on preamble lines 94, 124, 127 and 131 -- repointed to its definition,
  which sits at `:947` at v0.11. (The preamble belongs to neither half, so this moves nothing signed.)

**The change note sits as a `###` in the preamble, before `## 0.`** -- the only placement that moves neither half by itself.
The halves are MEASURED after the write: v0.10 ratified-text `1246a6ea32fc` -> v0.11 `2ea7e0a99695`; v0.10 brief `0455fc3d1e95`
-> v0.11 `14e406e0d673` (`prd_signoff_lib.half_hashes`; `prd-signoff.py status` reads both STALE, owed by `3.0.0_SA_CVO~Z` and
`4.0.0_SA_CRO~Z`, both live). 1,363 -> 1,637 lines.

**LD-0521 holds:** the round-14 issuance is cut after this delivery AND both v0.11 halves SIGNED, by `2.0.0_SA_COO~Z` alone.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`, and none is requested.

-- `1.0.0_SA_CTO~Z`
