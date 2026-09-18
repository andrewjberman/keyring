# AMGT_RESAPP -- panel briefs intake: what each CRO brief adds to existing art, and where it lands

**Owner:** `1.0.0_SA_CTO~Z` (L2-L4 for AMGT_RESAPP). **Living document** -- one section per brief, appended as each arrives.
**Why it exists:** Andrew-direct 2026-09-18 ~16:2xZ at the `1.0.0_SA_CTO~Z` terminal, verbatim: *"i am having CRO~Z go through
the various functions (Lead Panel, Thesis, Exec Mgmt, etc.) and write briefs covering current versus desired state enrichment
and development process. I want you to read them as they come in because some of it may be additive to existing art on these
functions."*

**Existing art it is measured against:** the PRD `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` at **v0.10** (the
ratified constraints, by ID), the decomposition, and the surprise channel. **Every row below cites the PRD by constraint ID or
line, or says 0 hits.**

**How it lands.** Round 13 is open and the spec is FROZEN mid-round (Rule 27), so nothing here amends the PRD now. Each
ADDITIVE item becomes an input to this seat's round-13 ROUND_ANALYSIS and the round-14 PRD addendum. The one exception is a
direct Andrew-authorized act (cards A and B), which is sequenced separately and is not a round cell.

Disposition codes: **ADD** = new to the art, becomes a round-14 L4 input · **FIX-ART** = the art is wrong or stale and the
brief corrects it · **EXEC** = the art already specifies it; the gap is in running it · **RESTATE** = the art already has it.

---

## 1. Lead Panel + header -- `BRIEF_LEAD_PANEL_CURRENT_TO_DESIRED_20260918.md` (read at HEAD, UPDATES 1-4, @`9136ff9e73`)

| # | finding (brief section) | existing art | disp. | lands as |
|---|---|---|---|---|
| L1 | The architecture is sound: producers rank once, commit behind `_CURRENT`, the panel only selects (s.1) | `C-SERVER-SIDE-RANKING` (PRD :940) | RESTATE | nothing -- agreement with ratified text |
| L2 | **Trending x Chatter ranks ten names that ALL have zero articles and score 0, in alphabetical order** -- it looks finished and carries no signal (F2) | `C-SERVER-SIDE-RANKING` fixes `TOP_N=10` but has **no rule against ranking a zero** -- the ratified text PRODUCES this list | **ADD** | a constraint: *a ranking never includes a member with no signal; a day where no member has signal is EMPTY with its reason* (brief item 8) |
| L3 | **The article store covers 3 names** (BA, COST, HD); 188 of 191 have zero articles; AAPL/NVDA/MSFT/JPM/TSLA have no lookup key at all (F1) | `C-ONE-STORE` (:1268) names `publication-links/v1` as the store; `C-HARVESTER-COMPUTE` (:952) and `C-VENDOR-WORD-HARVESTERS` (:999) design the harvesters | **EXEC + ADD** | the design exists; it is not running at coverage. ADD: the diagnostic question the art never asked -- **ingestion (nothing fetched) or association (fetched, not keyed to the name)**; the empty lookup keys point at association. L4 question, this seat |
| L4 | **The news feed and both chatter lists are ONE gap** -- all read `publication-links/v1` (9.1, item 10) | PRD treats feed and chatter as separate surfaces | **ADD** | one source fix closes three surfaces; the round-14 cell must be scoped as ONE, not three |
| L5 | Breakout x Chatter's empty list HAS a reason -- the producer computes `BELOW_MIN_ABSOLUTE_JUMP` for 191 of 191 and discards it (F3) | **0 hits** for `empty_reason` | **ADD** | a pointer-contract field `empty_reason`, written by BOTH generation writers (`chatter_axis.py`, `price/generation.py`, which share the contract), carried through the adapter to the panel. Changes interface G-1 -- L4 |
| L6 | **Breakout x Price has no sign test**: 23 of 32 listed "breakouts" are FALLING names (F4) | **0 hits** for `MIN_ABSOLUTE_JUMP` / a price floor; verified at source `movement_gate.py:413-428` returns `(True, "NO_RATIFIED_ABSOLUTE_FLOOR")` | **ADD (Andrew-ruled)** | card B: positive move >= +5% vs trailing 30-day mean. **The ratified text must record it**, or the PRD lags a sovereign word. Executed as a direct act WITH card A, B first (msg 23684) |
| L7 | Price lists are 3 trading days stale; price has no leg in the daily job (s.1) | `C-PRICE-RANKING-BOXSIDE` (:945) specifies the box-side shape, **not a cadence** | **ADD (Andrew-ruled)** | card A: prior-day prices on the existing daily job. Sequenced msg 23684: own exit codes 80-83, never-widen pair, change record first |
| L8 | **The description line's primary route is dead**: `CIE_DES` is on 0 of the model blocks -- the pull never requests it. `CIE_DES_BULK` is populated for all 21 names without a filing identity (9.1, 11.3) | **0 hits** for `CIE_DES` | **ADD** | cheapest fix on the panel: one field added to an existing pull, no model call, no new source. The adapter must read the field by the name the pull writes |
| L9 | **Management stops at 12 because it follows the FILING**: the 12 management names are exactly the 12 drafted-thesis names. Bloomberg's `COMPANY_EXEC_OFFICERS` is populated for the other 21 (11.2) | `C-EXEC-MANAGEMENT` (:597): *"The roster ... come[s] from the FILING's executive-officer section (the authority)"* | **ADD -- touches ratified text** | using Bloomberg makes it a SECOND roster authority. That changes `C-EXEC-MANAGEMENT`, which is ratified text; the CRO framed this correctly as an L4 question, not a pull change. **This seat's question to answer.** Linked to Thesis T-tier-1 below: filing identity lifts BOTH panels at once |
| L10 | **DEV deploys nothing BY DESIGN**: `ci.yml` has no deploy step; `deploy.yml` runs only on PROD (9.2) | PRD :1179 says *"nothing portal promotes, PROD or DEV"* -- **it treats DEV as a promotable environment, and it is not one** | **FIX-ART** | correct the art: there is no DEV environment. **The DEV push is a DURABILITY act only, never a reachability one; the only path to a user is the PROD promote.** This also corrects this seat's own framing in msgs to Andrew and in the register row -- see s.3 |
| L11 | A star round trip "on DEV with a real login" (s.3 check 2) | -- | **FIX-ART** | by L10 it cannot happen on DEV at all: nothing serves DEV. The check is local-only or post-promote. Held earlier for "a test identity"; the real blocker is that the environment does not exist |
| L12 | Refresh is wired and refused: no queue exists (s.1, item 5) | PRD :627 already requires *"the adapter DECLARES its queue carrier"*; :996 fixes that starring queues nothing | **EXEC + ADD** | the obligation is ratified; its DEFINITION is not. ADD the three questions the art leaves open: what the queue is, what "queue the harvesters for one name" means PER harvester, what the panel shows while pending. L4, before any L5 cell |
| L13 | Traps: no render-time re-ranking, count trading days before "stale", never transplant the chatter floor onto price, no monitor (s.6) | `C-SERVER-SIDE-RANKING`; CLAUDE.md NEVERs; `movement_gate.py` docstring | RESTATE | nothing |

### Stale text inside the brief itself -- flagged to its author, not corrected here

- **s.1**, parenthetical: *"The round's own model-figure denominator is 34 keyed names"* -- that 34 was THIS seat's error,
  retracted (msg 23693). UPDATE 4 corrects it at s.11, but a top-down reader meets the wrong figure first.
- **s.4 item 6** still reads *"DEV deploys, and CI goes green"*, superseded by s.9.2's finding that nothing deploys to DEV.

### Net for round 14, from this brief

**Eight ADD items** (L2, L3-diagnostic, L4, L5, L8, L9, L12-definition, plus L6/L7 recorded as ratified text),
**two FIX-ART** (L10, L11), **one EXEC** gap (L3 coverage). **One touches ratified contract text** (L9,
`C-EXEC-MANAGEMENT`) and is the item to take most carefully: widening an authority is exactly what a never-widen reading
exists to catch.

---

## 2. Thesis -- `BRIEF_THESIS_CURRENT_TO_DESIRED_20260918.md` + `THESIS_FOREIGN_FILINGS_CHANNELS_20260918.md` (read at HEAD, @`9136ff9e73`; msg 23694)

Denominator is **33** throughout (the brief's s.0, diffed against the crosswalk's MEASURED `model_key`s on an instrument
different from this seat's; the CRO's earlier 34 was the 33 plus NVIDIA, with no parsing error).

| # | finding (brief section) | existing art | disp. | lands as |
|---|---|---|---|---|
| T1 | ⛔ **Bloomberg returns NO filing text** -- docsvc and news refuse; BQL refuses on entitlement. The SEC EDGAR "stand-in" is the only working source (research note; brief s.3) | `C-FILINGS-ANALYZER` (PRD :577): *"The analyzer reads the filing **Bloomberg pulls** (a public filing stood in for the measurement)"*; PRD :1277: *"measure one Bloomberg-pulled filing before the public stand-in is retired"* | **FIX-ART -- ratified text** | **the largest item in either brief.** The ratified contract names Bloomberg as the filing source, and that premise is now measured false. The stand-in became the source without the text saying so, and :1277's retirement condition can never be met. The round-14 addendum must re-state the source as EDGAR (plus tiers 2-3), and say what Bloomberg is and is not for |
| T2 | Drafting is correct wherever it runs: 389 of 389 sentences PASS the verbatim check; the chart refuses unverified points (s.1) | `C-FILINGS-ANALYZER` v0.7 clause: every claim resolves to a passage, unresolved claims held uncited, never a chart input | RESTATE | agreement -- the ratified verbatim/verification discipline is working as written |
| T3 | **Chart 1 of 33 is a STALE-ANALYSIS gap**: 10 analyses predate rk-19's points branch and have no `thesis_driver.points` field; ASML's 3 points do not verify (s.1.1) | `C-FILINGS-ANALYZER` requires a THESIS DRIVER field *"EXERCISED on a real filing before ... claimed to exist"* | **EXEC** | the art is right; ten analyses were written before the code met it. A re-run (~$6) on the current analyzer. ASML may correctly stay ABSENT |
| T4 | The brief says **no analyzer version is stamped**, so the batch cannot tell a stale analysis from a current one (s.1.2 #3, s.4 item 2) | `C-FILINGS-ANALYZER` v0.7: the analysis persists *"the retrieval time and the **parser version**"* | ⛔ **CORRECTED BY MEASUREMENT HERE -- the version IS stamped; it is NEVER BUMPED** | read from the pool, six analyses: **every one** -- the four stale ones written 17 Sep 02:1x-02:3xZ with no driver points, AND BA and ASML written 15:35-16:02Z with points -- carries the **identical** `analyzer_version = "opal-filings-analyze/1.0.0"` and `prompt_version = "rj6-two-pass/1"`. The field exists and cannot discriminate, because the output contract changed (rk-19's points branch) without the version moving. ⚠ **TRAP FOR ROUND 14: the brief's own item 2, built literally on the existing field, "skip a name whose analysis was written by the current analyzer", would SKIP the ten stale analyses forever** -- they already claim the current version. The fix is a version that MOVES when the output contract moves, then the skip rule; in that order, never the reverse. Routed to `4.0.0_SA_CRO~Z` |
| T5 | **The scheduled task cannot launch**: `Execute = C:\Users\Opal`, the path split at the space in "Opal Bloomberg" -- enabling it runs nothing and reads like a quiet week (s.1.2 #1) | 0 PRD hits; `C-FILINGS-ANALYZER`: *"It runs as a scheduled batch over the union universe"* | **EXEC** | a defect of exactly the class banked for site Z (unquoted path with a space, reports success shape). Fix before any enable; the task stays disabled until Andrew's word |
| T6 | Launcher pinned to `universe/v1/2026-09-15.json`; the 16 Sep universe lists ASML twice under one CIK (s.1.2 #2, #4) | 0 PRD hits | **ADD** | resolve the newest vintage, never a typed date; deduplicate by CIK. Minor, cheap |
| T7 | **Two writers of `drafting/v1/<key>.json`**: `batch.py:150` and `analyze.py:1215` (s.1.2) | -- | **ADD, and it binds this seat** | any never-widen half naming what that key holds must PRINT N=2 writers and read both rules (CLAUDE.md s.5). This seat co-signed the drafting-cache rebuild this round on ONE key; a future half on that key must count both |
| T8 | **Tier 1: +6 names (12 -> 18 of 33) with NO new source** -- Bloomberg's `CENTRAL_INDEX_KEY_NUMBER` supplies a CIK the SEC ticker table misses; the form measurement and name-collision guard already exist in `build_universe.py:491-531` (s.3) | 0 PRD hits for a second CIK source | **ADD** | the cheapest coverage gain in the series: one fallback CIK source feeding checks that already exist. **Moves Thesis AND management together** (L9) |
| T9 | Tier 2: +6 names via ESEF/UKSEF at `filings.xbrl.org` by LEI; needs a second section cutter (no "Item 1A" in an ESEF report) and must state the fiscal year held (s.3, s.4 item 6) | 0 PRD hits | **ADD -- L4 first** | a new source AND a new cutter; the brief rightly routes it through L4 before any cell. Egress for a producer is a new act needing its own word |
| T10 | Tier 3: the last nine need nine adapters or a purchased feed; ask the Bloomberg rep first (s.2) | -- | **AT ANDREW** | card "where do the last nine come from" -- buy-or-build is his |
| T11 | Card "may the filings batch run" -- once now, then weekly (s.2) | `C-FILINGS-ANALYZER` requires a scheduled batch; cadence is not his to be skipped | **AT ANDREW** | the CRO's rec -- YES only after T5 and T4 land, so the first weekly fire is the last full-price one -- is sound and this seat concurs |
| T12 | **Management = Thesis coverage exactly**; Bloomberg `COMPANY_EXEC_OFFICERS` would be a second roster authority. The CRO **withdrew** its note's claim that it "closes most of the management gap" (s.4) | `C-EXEC-MANAGEMENT` (:597) | same as L9 | one L4 question, asked once, across both panels. Note the card-2 precedent the brief cites: a vendor roster (Lusha) was already rejected for carrying no tenure -- tenure on `COMPANY_EXEC_OFFICERS` is **unmeasured**, and should be measured before the question is put |

### Net for round 14, from this brief

**One FIX-ART on ratified text that outranks everything else in the series so far (T1)**: the analyzer's source is written as
Bloomberg and Bloomberg cannot supply filings. **Two EXEC gaps where the art is already right and the code lags** (T4, T5). **T4 was
corrected by measurement here: the version is present and never moves -- and the brief's fix, built on it as written, would
lock the stale analyses in permanently.** **Three ADD** (T6, T7, T8), of which T8 is the best value-for-cost item
found yet and T7 is a standing obligation on this seat's own co-sign practice. **Two cards at Andrew** (T10, T11).

### 2.1 Andrew answered both Thesis cards (~16:3xZ) -- and re-framed the series

Record `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_16xxZ_THESIS_NO_RERUN_AND_FILINGS_BATTERY.md`
@`1c6e685ae6`, read from the commit (verified an ancestor of HEAD), verbatim:

> *"I dont care about rerunning until the process is completely validated end to end and the product is basically done.
> [...] for every security, we basically have a battery on how to get its filings: If US 1.) Start with EDGAR, 2.) Try the
> BBG resolution, 3.) Try websearch maybe surfaced through an IR page. If International: 1.) I dont know but we need a plan.
> The premise behind this is that we will be adding things over time and the more important thing than establishing a
> pipeline itself is the process behind full "security analysis" backend instantiation for a new security."*
> and: *"a translation functionality will be required in cases like these and that should be included in the spec/brief"*

**What it changes in the rows above:**

| row | was | now |
|---|---|---|
| T3 (stale-analysis chart) | EXEC: a ~$6 re-run | **ACCEPTED AS IT STANDS** -- no re-run until the process is validated end to end. The one-name chart is not a defect to fix now |
| T4 (version never moves) | EXEC, correctness | still correct and still load-bearing -- but it is correctness work for WHENEVER the job is enabled, not urgent. The CRO applied the correction to its brief (@`1c6e685ae6`) after re-reading 12 of 12 analyses |
| T10 (the last nine) | AT ANDREW: buy or build | **RE-FRAMED: not a source for nine names but a per-security BATTERY every security goes through.** US order is his; the international order is his open ask. CRO proposal (Thesis s.8.2): EDGAR by ticker -> EDGAR by Bloomberg CIK -> ESEF by LEI -> company site -> national regulator -> UNRESOLVED-SOURCE carrying every attempt |
| T11 (may the batch run) | AT ANDREW | **ANSWERED NOT NOW** -- no fleet run ahead of validation. Whether a validation exemplar run is inside that line is put back to him, not assumed |
| T1 (C-FILINGS-ANALYZER names Bloomberg as the source) | FIX-ART | **FITS THE BATTERY DIRECTLY:** the contract's source becomes "the battery's winning document", with Bloomberg supplying the KEYS (CIK, LEI, name) and never the text. That is a cleaner correction than any this seat had drafted |
| NEW T13 | -- | **Translation is IN the Thesis spec**, by his word. CRO s.8.4 recommends analyzing the ORIGINAL and translating the OUTPUT, so every span still re-locates verbatim in the filing; translating first would verify against the model's own translation. **This seat concurs, and it is the only design that keeps C-FILINGS-ANALYZER's verbatim discipline (T2) intact.** Open for L4: chart-point locale parsing, roster script, cost |

⛔ **The entity test is load-bearing in any battery.** The same domains serve SUBSIDIARIES' annual reports (Roche Holdings Inc,
RWE Finance Europe BV, Zurich Life), and Bloomberg's web address points at a subsidiary or branch for 3 of 22. A step that
returns *a* current annual report from the issuer's domain has not passed until it is the RIGHT ENTITY's. The CRO names one
acceptance test per step -- right entity, current, known document family -- and that should be the battery's contract.

### 2.2 The premise re-frames this intake, not just the Thesis panel

His priority is **the process for instantiating the full security-analysis backend for a NEW security**, ahead of any one
pipeline. The CRO will write that as an L1 instantiation brief when the panel walk ends. **The three cross-panel questions below
are exactly the rows where that process has no answer yet** -- so this intake and the instantiation table should converge, and
the round-14 PRD addendum should be organized around the instantiation stages rather than around panels. Proposed validation
(CRO): instantiate one US, one English-international and one non-English name end to end.

---

## Cross-panel: items that are ONE question, not two

| question | panels | why one |
|---|---|---|
| Filing identity for the 21 names without one | Thesis T8/T9, Lead Panel header L9 (management) | management's roster is read from the filing, so every name Thesis reaches, management reaches |
| `publication-links/v1` coverage | Lead Panel L3 (chatter), L4 (news feed) | both chatter lists and the feed read the same store |
| Bloomberg as a second authority | Lead Panel L9, Thesis T12 | the same ratified-text change to `C-EXEC-MANAGEMENT` |

---

## 3. Corrections this intake forced on this seat's own record

- **The DEV push is NOT a reachability act** (L10). The phrase this seat carried from the CVO's verdict into the register row
  and the verdicts ledger -- "a durability act before it is a reachability one" -- implies the push eventually makes the pages
  reachable. It does not: **pushing DEV makes the pages durable, never reachable**, because no environment serves DEV. Only
  the PROD promote reaches a user, and Andrew has deferred it. (This seat's terminal reports to Andrew described the push as
  keeping the pages off one machine's disk -- durability -- which stands.) The register row is re-stated at the next tick.
