# AMGT_RESAPP -- panel briefs intake: what each CRO brief adds to existing art, and where it lands

**Owner:** `1.0.0_SA_CTO~Z` (L2-L4 for AMGT_RESAPP). **Living document** -- one section per brief, appended as each arrives.
**Why it exists:** Andrew-direct 2026-09-18 ~16:2xZ at the `1.0.0_SA_CTO~Z` terminal, verbatim: *"i am having CRO~Z go through
the various functions (Lead Panel, Thesis, Exec Mgmt, etc.) and write briefs covering current versus desired state enrichment
and development process. I want you to read them as they come in because some of it may be additive to existing art on these
functions."*

**When the addendum is written -- Andrew-direct 2026-09-18 ~17:2xZ at this terminal, verbatim:** *"I want to wait until CRO
and I have gone through all the pages and brought forward al the briefs, we still have a couple more to do. Exec Mgmt brief is
being refined with one more piece, then we will go on to Peers, Model, and Posture."* **So no PRD addendum is drafted, staged or
applied until every panel brief is in.** Remaining: Exec Management (one more piece), Peers, Model, Posture.

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

## 2B. Exec Management -- FIRST READ by message (msg 23697, 16:52Z); the brief itself follows at Andrew's word

Measured by `4.0.0_SA_CRO~Z` with the adapter's own `read_management` over the crosswalk's 33. **The headline figure was
re-measured here on a different instrument** (the served thesis bundle's `management` block, keys `%2F`-encoded): **agrees
exactly -- 12 SERVED, 7 with officers (62 officers), 5 with ZERO officers, all 5 `UNRESOLVED-SOURCE`** (ASML, HAL, INTU, KMB,
PBR).

| # | finding | existing art | disp. | lands as |
|---|---|---|---|---|
| E1 | ⛔ **SERVED is a status, not content.** 5 of the 12 "served" rosters carry 0 officers. Real coverage is **7 of 33**, and tenure plus a pool comparison exists for **4** (BA, COST, HD, SAP) | `C-EXEC-MANAGEMENT` (:597) defines the roster's SOURCE, not what "served" must contain | **ADD -- and it corrects figures in circulation** | a contract clause: a roster with zero officers is not SERVED, it is ABSENT with its reason. **Corrects this seat's own "management 12 of 33"** (msg 23693 and the register row) -- see s.3 |
| E2 | The 5 empty rosters have TWO causes, neither a failed pull: ASML/PBR -- *"the persisted 20-F carries an EMPTY officer section (Item 6) -- the item was not cut from the primary document"*, an upstream CUT defect in the filings stage; HAL/INTU/KMB -- *"no declared shape read this section"* (20 / 4 / 194 usable lines, 0 candidates), a roster-SHAPE gap | -- | **ADD** | two different fixes in two different stages. The round-13 drain record labels them `pull-missed` (msg 23691); **that understates both** -- the pulls ran, the cutter and the shape reader did not. Flagged for the completion record |
| E3 | Row quality on the 7 good rosters: BABA, NU, VLO have officers with no role start; **VLO's role reads "... and President 60" -- the age leaked into the role field** | `C-EXEC-MANAGEMENT`: role start is filing-sourced | **EXEC** | a parser defect in `roster.py`, not a spec gap |
| E4 | **The CEO profile line misstates WHY on 7 of 12.** `ceo_profile_reading` (`scoped_amgt.py:2285-2296`) maps "no url count" to NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY, and `ExecManagementTab.tsx:84-87` then tells the reader *the search returned unreadable links*. For 7 of 12 **no search ran** -- no declared IR domain, or no CEO because the roster is unresolved -- and each object carries `absence_class: NOTHING_FOUND`, which the reader ignores. True split: 1 CONFIRMED, 4 searched-and-unreadable, 7 not searched | FWD-9-class rule: a reason shown must be the TRUE reason | **ADD -- a page that tells the reader something false** | the reader must render the object's own `absence_class`. The most user-visible defect in the panel: it is not absent-and-honest, it is present-and-wrong |
| E5 | **The tenure pool fragments by run**: `_pool/2026-09-15` = 4.08y over 40 officers of 5 names; `_pool/2026-09-18` = no value, 2 rosters, 0 officers with a role start. NU and VLO show the pool ABSENT; each run pools only itself | `C-EXEC-MANAGEMENT`: *"the pool-average tenure is computed over the union universe"* | **FIX-ART / EXEC** | the ratified text says the pool is over the UNIVERSE; the code pools over ONE RUN. The art is right and the code violates it |
| E6 | **The batch census splits security keys on `/`** -- `batch.py:81-84`, `obj["Key"].split("/")` taking `parts[2]` and requiring `parts[3]` to end `.source.json` -- **verified at source here.** `BP/_LN_Equity` and `NG/_LN_Equity` can NEVER be built, even after Thesis tier 1 gives them real 20-Fs | -- | **ADD -- a production defect of the exact class this seat committed twice in analysis today** | the fix is the one banked in memory: take keys from the population of record, never by splitting a path. It will silently drop two London names on every run and report success |
| E7 | **The same census counts UNRESOLVED-SOURCE placeholders as filings**: 188 = 12 real + 176 placeholder names. Enabled, a run would write **~176 zero-officer rosters that the adapter serves as SERVED** | -- | **ADD -- and E1 makes it serious** | together with E1 this is the panel's worst latent defect: one enable would turn 7 real rosters into 183 "served" ones, 176 of them empty |
| E8 | `OpalResearch-ExecManagement` is DISABLED, its path is **split at the space** (Execute = `C:\Users\Opal`), it has never run (267011); `run_batch.cmd` pins universe 2026-09-15; enrichment is scoped by `domains.json`, 5 hand-declared names | `C-EXEC-MANAGEMENT`: the harvest estate owns the collection lane | **EXEC** | **the IDENTICAL launcher defect and date pin found on the Thesis task (T5, T6)** -- so it is a pattern in how these tasks were registered, not two incidents. Fix once, in the registration, for every research task |

### 2B.1 The full brief -- `BRIEF_EXEC_MANAGEMENT_CURRENT_TO_DESIRED_20260918.md` @`36ed77f347` (msg 23705), at Andrew's word *"This is good, write the brief and bring it to the CTO~Z"*

It confirms every figure above on a re-read with no change, and adds:

| # | finding | existing art | disp. | lands as |
|---|---|---|---|---|
| E5' | **The pool fragmentation has a cause at source**: `compute_pool`'s docstring (`enrich.py:582-588`) promises the average over EVERY name with a roster; the code keeps only objects named exactly that `as_of` (`:594`) | `C-EXEC-MANAGEMENT`: *"computed over the union universe"* | **EXEC -- code vs its own docstring AND the ratified text** | E5 is now a code defect with a line number, not a data gap. Two authorities (docstring, contract) agree and the code disagrees with both |
| E9 | **Bloomberg `COMPANY_EXEC_OFFICERS` is NAME + TITLE only, no role start** -- measured on HSBC, KDDI, Roche | L9/T12 left this UNMEASURED | **ANSWERS this seat's open question** | as a second source it can fill the TABLE but never tenure or the pool -- the same gap card 2 held against Lusha. So the ratified-text change narrows to: a LABELLED table-only fallback |
| E10 | The officer-section cut lives in the FILINGS stage (`fetch.py:116` 10-K Item 10, `:147` 20-F Item 6; persisted `:440-447`); an empty cut is recorded as an empty success | -- | **ADD** | an empty cut must be a FAILED cut with its reason. Same honesty rule as E1 and L2, one stage upstream |
| E11 | The empty roster renders "0 officer(s) from Item 6 ..." over an empty table; `roster_status` and `roster_reason` ride the payload and are never rendered (`ExecManagementTab.tsx:95-137`) | FWD-9-class: a reason carried must be shown | **ADD** | pairs with E4 -- the page has the true reason in hand on both lines and prints neither |
| E12 | **Enrichment is a hand list**: `domains.json` declares 5 names; every other name is SKIPPED | -- | **ADD** | the domain must come from the site the filings battery VERIFIED (right entity), never the hand list or Bloomberg's raw web address (a subsidiary or branch for HSBC, ICICI Bank, SSE) |
| E13 | **No trigger**: every roster so far came from a hand run | `C-EXEC-MANAGEMENT` names the harvest estate as owner of the collection lane | **ADD -- the instantiation gap in one line** | the roster builds when a security's filing lands, as a step of instantiation |

**Two cards for Andrew** (brief s.2), both genuinely his:
- *"Should an officer list from Bloomberg fill the table when the filing gives none?"* -- CRO rec: yes, LABELLED, table only,
  tenure and pool left ABSENT with that reason. **This seat concurs**: it gives 21 blank panels named executives without
  claiming a tenure the source lacks, and it is the value-carries-its-claim rule applied to a roster. If he says yes, the
  change to `C-EXEC-MANAGEMENT` is this seat's to write and the CVO's to sign.
- *"Should Lusha profile links be part of instantiating a new security?"* -- billed per use; CRO rec: decide after the
  three-name validation reports. **This seat concurs.**

**ANSWERED ~17:1xZ -- both YES**, verbatim *"1.) Yes. 2.) Yes they should."* (record
`ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md`, brief UPDATE 1 @`f45a7c551e`, msg 23708). Card 1 in the recommended
form; card 2 AHEAD of the recommended timing -- he chose not to wait for the validation.

⭐ **So the `C-EXEC-MANAGEMENT` amendment is now OWED BY THIS SEAT at L4, and the CVO signs it.** It must carry, per brief s.8:
- `roster_source` on every object (FILING / BLOOMBERG_FALLBACK);
- **the filing roster's own failure reason travels WITH the fallback** -- otherwise the fallback hides the five broken filing
  rosters that the cut and shape fixes exist for. ⛔ This is the clause to get right: a fallback that erases the reason it
  exists is the same status-over-content defect as E1, moved one layer down;
- the filing WINS when it arrives;
- the field rides an existing Bloomberg pull beside `CIE_DES` / `CIE_DES_BULK`;
- censuses print FILING and BLOOMBERG_FALLBACK separately;
- Lusha enrichment is a step of instantiation, its domain from the battery's VERIFIED site only, NOT ATTEMPTED with its reason
  when there is none, Bloomberg-fallback officers enrichable, credits measured on the validation names before any scale.

**Put back to Andrew, NOT decided:** the Bright Data CEO-profile search (card 2 did not name it), and whether the running
three-name validation should exercise Lusha. His "no fleet run until validated end to end" stands over both cards.

**The "one more piece" -- the CEO search, redesigned by Andrew ~17:2xZ** (brief s.9 @`32a4882d81`, msg 23713), verbatim: *"We
should also do that, search the CEO's name with Bright Data SERP, and have an agent go through it and pull/organize the relevant
results."* The CEO step changes from one `site:<IR domain>` query plus a host test to a SERP on the CEO's NAME, then an agent
that organizes the results. It joins the same `C-EXEC-MANAGEMENT` amendment.

| # | finding | disp. | lands as |
|---|---|---|---|
| E14 | ⛔ **A FAILED search reads as an EMPTY one.** `serp_brightdata` (`data/find/dualbiz/scripts/serp.py:264-272`) does `except Exception: break` on a request error and `break` on a bad JSON body, returning whatever list it had -- usually `[]`. `enrich.py:434-439` then records 0 urls as **NOTHING_FOUND**, and its own `except` at `:431` is dead for that path because the primitive never raises. **Verified at source here.** | **ADD -- the failed-retrieval-returns-a-value class** | a request failure must surface as a failure with its cause, never as an empty result. Must land BEFORE the redesign runs, or a bad key or a network fault will be recorded as "the CEO has no public profile" for every name |
| E15 | `serp_brightdata` returns URLS ONLY -- title and snippet are dropped (`:278-282`), so an agent cannot judge relevance | **ADD** | the redesign needs the organic result's title and snippet |
| E16 | Namesakes: CEO names collide | **ADD** | an identity test before any organized fact is kept |
| E17 | Every organized fact carries its url and a quote that re-locates verbatim in the fetched page; a fact with no quote is held | RESTATE of `C-FILINGS-ANALYZER`'s verbatim discipline, extended | the same guarantee Thesis enforces, applied to web results |
| E18 | The "opaque redirect wrappers" label on the 4 real searches is the module's own and is **unverified** | **MEASURE FIRST** | one query read before the label is repeated anywhere |

No contact data (the module's CONTACT_STEMS / CONTACT_KEYS carry over); a `ceo_profile` block replaces `ceo_public_profile`;
cost measured on the validation names first. Recorded narrow: CEO only. The running validation's scope is unchanged (no Lusha,
no Bright Data), because that question is still open with Andrew.

**Owed by THIS seat when round 14 cuts it:** build item 1 (the honest CEO line and empty-roster rendering) changes what the
adapter and page serve for every one of the 12 served names, so it needs a **CTO+COO never-widen pair** -- this seat writes the
CTO half against the exact diff.

**Running now, per the brief s.7:** a three-name instantiation validation (a subagent of `4.0.0_SA_CRO~Z`, authorized
~16:5xZ) -- one US, one English-international, one non-English name, end to end. Its report is the first measurement of the
instantiation process itself, and it lands in the Thesis and Exec Management briefs.

### Net for this panel

**The panel's headline number was a status count.** Seven names have a roster; four have tenure; and the page tells the reader
a search failed on seven names where no search ran. **Three defects share one root with Thesis** -- the launcher split at the
space (E8/T5), the pinned universe (E8/T6), and a census that splits keys on `/` (E6, and this seat's own error twice today).
**The instantiation lens (s.2.2) fits exactly:** every one of E2, E6, E7 and E8 is a place where "stand up management for a NEW
security" has no working answer.

---

## Cross-panel: items that are ONE question, not two

| question | panels | why one |
|---|---|---|
| Filing identity for the 21 names without one | Thesis T8/T9, Lead Panel header L9 (management) | management's roster is read from the filing, so every name Thesis reaches, management reaches |
| `publication-links/v1` coverage | Lead Panel L3 (chatter), L4 (news feed) | both chatter lists and the feed read the same store |
| Bloomberg as a second authority | Lead Panel L9, Thesis T12 | the same ratified-text change to `C-EXEC-MANAGEMENT` |
| Scheduled-task registration (launcher split at the space, universe pinned to a date) | Thesis T5/T6, Exec Mgmt E8 | the same registration defect on two research tasks -- fix it where tasks are registered, once |
| Key census by splitting a path on `/` | Exec Mgmt E6 (production code); this seat's own analysis twice | two London names silently dropped, success reported |
| "SERVED" meaning a status rather than content | Exec Mgmt E1/E7; Lead Panel L2 (a list of zeros reading COMPLETE) | a producer can report success over an empty payload -- one honesty rule across panels |

---

## 3. Corrections this intake forced on this seat's own record

- **"Management 12 of 33" is a STATUS count, not coverage** (E1). This seat reported it in the 33-vs-34 retraction (msg 23693)
  and the register row @`1620bdddef` still says *"management commentary 5 -> 14 names"* -- wrong twice: 14 was an object count
  (12 names plus two pool files), and 12 is served-status, of which **7 carry officers**. Re-stated in the register row with
  this intake's commit.

- **The DEV push is NOT a reachability act** (L10). The phrase this seat carried from the CVO's verdict into the register row
  and the verdicts ledger -- "a durability act before it is a reachability one" -- implies the push eventually makes the pages
  reachable. It does not: **pushing DEV makes the pages durable, never reachable**, because no environment serves DEV. Only
  the PROD promote reaches a user, and Andrew has deferred it. (This seat's terminal reports to Andrew described the push as
  keeping the pages off one machine's disk -- durability -- which stands.) The register row is re-stated at the next tick.
