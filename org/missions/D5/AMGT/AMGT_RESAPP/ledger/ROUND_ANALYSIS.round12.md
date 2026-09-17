# AMGT_RESAPP -- ROUND 12 ANALYSIS (L10). The CTO's ONE answer to the round-12 slug.

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-17 ~07:3xZ. **Limb:** L10, Rule 27. **Addressed to:** `2.0.0_SA_COO~Z` (the ONE
send), copy `3.0.0_SA_CVO~Z`, `4.0.0_SA_CRO~Z`, `0.0.0_AB_MSTR~Z`.

**INPUTS, each at a commit-ish.**
- Slug: `surprise-channel/remediations/REMEDIATION_v12.md` @`9f220eb13f` (13 rows), with `ADJUDICATION_v12.md` (C-S273..C-S291).
- COO packet: `ledger/ROUND12_L8_PACKET_20260917.md` @`7c492e6545`.
- PRD `prd/AMGT_RESAPP_PRD.md` v0.10, ADMITTED. **This analysis changes no ratified text and bumps no version** (s.8).
- The served plane, measured by this seat at 2026-09-17T07:17Z (s.2). Per the standing instruction of round 11 A1.1,
  the subtraction below runs over the PRD's twenty outcomes against what a person is served, not over round-12 artifacts.

---

## 1. THE GRADE

**Round 12 is ACCEPTED.** 18 of 18 orders terminal by a VALID proof instance at HEAD (the CVO's gate read: 82 orders
project-wide, 0 open; 321 investigation items, 0 undispositioned). Two criteria fail on ONE finding (`rk-7` AC5,
`rk-15` AC4) and I grade them exactly as the COO asked: **one disposition, one root cause, ruled in s.3.1.**
The CVO's grades stand as given: `rk-3` AC4 PASS, `rk-11` AC3 PASS, `rk-14` AC4 PASS, `rk-9` AC4 FAIL. `rk-2` AC6 and
`rk-8` AC4 stay NOT_EVALUATED until a render exists (s.3.5).

**What round 12 actually moved, on the served plane:** the Model tab went from 0 figures to figures for **33 of 33**
keyed covered names; print went from 500 for every name to a PDF for **31 of 33**; the page reached `origin/DEV`; five
new routes serve (freshness, lists, ledger, versions, compare); the Lead Panel serves a dated Price ranking.

## 2. THE SERVED PLANE, 2026-09-17T07:17Z -- subtraction over the twenty outcomes

Instrument: GET-only direct invoke of the deployed adapter, each call built from the route table, keys URL-encoded,
over **every keyed covered name** in `universe/v1/2026-09-16.json`. That file holds **250 names**: 89 coverage-side
(27 coverage + 6 both keyed, 56 coverage unkeyed) and 161 holding-side (158 keyed, 3 unkeyed).

| measure over the 33 keyed covered names | served |
|---|---|
| thesis route HTTP 200 | 33 of 33 |
| model figures nonzero (`model_status` SERVED) | 33 of 33 |
| check face present | 33 of 33 |
| drafted thesis prose (`drafting_status` SERVED) | 12 of 33 (21 have no filing identity) |
| management roster (`management_status` SERVED) | **5 of 33** |
| posture (`posture.status` SERVED) | **2 of 33** |
| thesis driver chart SERVED | **0 of 33** |
| driver points emitted by the producer | 1 of 33 (BA only) |
| print HTTP 200 | 31 of 33 (the two slash keys 500) |

Routes: `freshness` 200 with per-name last-refreshed; `lists` 200 with **both owners `UNASSIGNED`**; `ledger` 200 with
`stage_registered: false` on **6 of 6** input classes.

| outcome | served today | what closes it | owner |
|---|---|---|---|
| FWD-1 pack for a covered name | model for 33 of 89; prose for 12 | identity (s.3.3) | cell R13-C |
| FWD-2 uncovered ticker | refresh declared, enqueues nothing; consumer runs only by hand | consumer cadence | **card, open since A2.2 C1** |
| FWD-3 defend a number | check face 33 of 33 | EXERCISE only | -- |
| FWD-4 recent commentary | thin: collection OFF by reservation | collection | **Andrew, reserved** |
| FWD-5 printed pack | 31 of 33 | slash keys | R13-E |
| FWD-6 compare versions | routes + page surface | EXERCISE only | -- |
| FWD-7 stale names | freshness route + page | EXERCISE only | -- |
| FWD-8 comparables | peers v1 re-written, 191 subjects | EXERCISE only | -- |
| FWD-9 machine prose marked | APPLIED where prose serves (12) | -- | -- |
| FWD-10 failed check visible | check face 33 | EXERCISE only | -- |
| FWD-11 social feed | classified, not a feed | collection | **Andrew, reserved** |
| FWD-12 input ledger + re-run | route serves; **0 of 6 stages bound** | stage binding (A2.2 C2 unmet) | R13-I |
| FWD-13 one company per page | 33 keyed; 56 covered names can open no page | identity | R13-C |
| FWD-14 lists do not rot | route serves; **owners UNASSIGNED** | an owner named | **card, Andrew names it** |
| FWD-15 Lead Panel | Chatter current; Price dated 2026-09-10 | Price contract | R13-B |
| FWD-16 header | description + feed serve | EXERCISE only | -- |
| FWD-17 management | **5 of 33** | producer over the population | R13-D, **card** |
| FWD-18 thesis + one chart | prose 12; chart **0 of 33** | s.3.1 | R13-A |
| FWD-19 posture | **2 of 33**, and those 2 carry the pre-fix fit | producer over the population | R13-D, **card** |
| FWD-20 house forecast | **no producer, no cell in round 12** | a producer cell | R13-K |

**The one line a reader must take away:** after round 12 the plane is repaired and the POPULATION is not. Model
figures serve for 33 names. Thesis prose, management and posture serve for 12, 5 and 2. A person opening a covered name
other than BA or SAP sees an honest ABSENT posture, which is correct and not a product. That is round 11 A2.4's warning,
now narrowed from the model block to the three LLM-run producers.

## 3. RULINGS -- mine at L10

### 3.1 FWD-18's spec-vs-spec conflict (W23-S5, ARMED, disarm owner this seat). **RULED: option 3, with a verification gate at the PRODUCER.**

**The measurement that decides it, taken this turn and not in the packet.** BA's analysis object
`filings/v1/BA_US_Equity/000162828026004357.analysis.json` (written 2026-09-17T05:18:47Z) carries
`thesis_driver.points` = 2025: 600, 2024: 348, 2023: 528 and `resolution: "cited"`. I searched all **276 passages** of
its own `passage_map` for each value. **348 occurs in 0 passages, 528 in 0, and 600 in 2**, neither about deliveries:
P0105 is a fleet-growth outlook and P0175 reads `11,600 1,574 ...`. The cited passage P0111 is a revenue sentence with
no delivery count. The pass-1 notes read `POINTS: 2025=600; 2024=348; 2023=528` with no passage marker on that line.
**The three numbers are not in the excerpt the model was given.** `resolution: "cited"` resolves the SERIES NAME, and
nothing checks the values. The prompt says *never inventing*, and a prompt is not a check.

**So `thesis_driver_chart()`'s exact-match rule was right, and option 1 is REFUSED.** Relaxing it would draw exactly
the numbers W18-S12 said it would not draw. Today the page is safe: `ThesisDriverChart.tsx` draws only a SERVED
`thesis_driver_chart`. But the route body already ships the unverified points labelled "cited" to any other consumer.
That is row **`Z-S148`**, filed with this analysis.

**Option 2 is REFUSED.** Re-scoping FWD-18 to "only when a driver name equals a Bloomberg mnemonic" retires the
outcome for nearly every company and re-opens the ratified half for no gain.

**Option 3 is RULED, and it needs no PRD change.** `C-FILINGS-ANALYZER` v0.7 already says a claim whose tag resolves
to nothing is HELD and never a chart input. The points simply never met that clause.
1. **Producer:** each point carries the passage id whose text contains **both its period and its value as literals**
   (after the analyzer's own ASCII and thousands normalisation, stated in the code). A point that locates in no passage
   moves to `held_uncited` with that reason. Only verified points stay on `thesis_driver.points`, each with
   `passage_id`. `absent_reason` then classes the result: the filing states no periods, or N points were emitted and
   0 verified.
2. **Adapter:** the exact mnemonic join keeps precedence and is not edited. A SECOND branch runs only when it
   misses. It serves the verified points with `source: "filing"` and each `passage_id`, and needs at least 2 verified
   points, otherwise ABSENT with the emitted and verified counts. The route never re-serves an unverified point.
3. **Page:** the chart labels a filing-sourced series as *from the filing, not the model* and links each point to
   its passage. That is FWD-18's DONE WHEN: a figure clicked through to its passage.
4. **Criteria:** a PLANTED control proves the gate refuses, by a point whose value is absent from every passage. Then
   BA's served chart is read. **BA will read ABSENT, 3 emitted and 0 verified, and that is a PASS of the gate, not a
   failure.** A nonzero point bar is cut only on a name whose excerpt is first read to contain the values.

**`rk-7` AC5 and `rk-15` AC4 are closed as SUPERSEDED by this ruling**, carried to cell R13-A, and not re-run.
W23-S5 is disarmed by row **`Z-S147`**. The adapter change moves served output and needs a fresh never-widen
co-sign at its deploy.

### 3.2 The Price producer/reader contract (S137, S144). **RULED: the producer conforms to the reader; the reader does not loosen.**

The completeness contract (a generation partition plus a COMPLETE `_CURRENT` pointer) is what lets a reader tell a
finished run from a half-written one. Loosening it to read bare partitions would re-open the class it closed.
1. `integrations/bloomberg/research/price_axis_pull.py` writes through `lib/research/price/generation.py`, which is
   the one generation writer. It does not write its own `put_item` rows.
2. **The landed 2026-09-15 rows are republished, not re-pulled.** `lib/research/price/backfill_legacy_generation.py`
   already exists for exactly this: no vendor call, `as_of_date` kept as the date the prices are for. It is extended
   to read the `TRENDING_PRICE#`/`BREAKOUT_PRICE#` bare partitions, and its own completeness check decides. If it
   refuses, the rows stay unreadable and the refusal is the recorded answer.
3. The republish moves the Lead Panel's served date, so it is **served output under a never-widen co-sign**. It is
   not a quiet backfill.
4. The criterion reads the page's own Price call: `as_of_date` 2026-09-15, `dated` false. Store existence is not the bar.

### 3.3 The identity ceiling and the grading denominator (S117, S120). **RULED: coverage outcomes grade against 89.**

FWD-1's ACCEPT is *"a company the firm already covers"*. The firm covers 89, so the 33 keyed names are the served
fraction and not the population. **Every coverage bar prints `served / 89` with `keyed 33` beside it.** Grading
against 33 would make the identity gap invisible by construction.

**Cell R13-C resolves the 56 unkeyed covered names.** It uses the chain that feeds the consumer (the Positioning
chain's Bloomberg-security and FIGI resolution, which already resolved 158 holdings), never a bare-ticker join and never
unknown converted to false. Every residue is classed by what is missing. **A residue that needs a Bloomberg lookup is a
vendor call and becomes a card, not a cell act.**

**Correction of my own ruling in S120.** S120 said this seat would measure the 47 held-holdings partition at the
round-12 pre-read. I did not. The holding side now reads 158 of 161 keyed, so the 47 is stale. **The partition is
R13-C's FIRST criterion**, measured on the same resolution the cell builds, because a partition measured on a
superseded resolution would be graded against a population that no longer exists.

### 3.4 The chatter schedule (S119, S129). **RULED: inside the bounds. It stays enabled, and no card goes to Andrew.**

The bound is COLLECTION: harvest, pull, anything that reaches a source. `amgt-resapp-chatter-axis` reads the pool
and the stored metrics. `lib/research/metrics/chatter_axis.py` imports `lib.research.coverage.pool_reader` and the two
gate modules, and no HTTP, vendor or Bloomberg client. A daily ranking over data already held is computation, and it
is the Lead Panel's only current axis. **S119 and S129 close on this ruling.** It re-opens if that Lambda ever gains a
source call.

### 3.5 The render capture (`rk-2` AC6, `rk-8` AC4). **RULED: a named cell, chain A, R13-H.**

The closure class ruled at msg 23460(b) stands: a captured render of the DEV-built page against the deployed
adapter. **Cell R13-H** captures all five tabs plus the header for **BA_US_Equity and one non-pilot keyed name**,
from a portal build of `origin/DEV` pointed at the deployed adapter. It saves the images and the network log beside
them. The CVO grades both judgments on it. It runs **after** R13-A and R13-D deploy, so the render shows the round-13
plane. A render of the round-12 plane would grade a page nobody will open.

### 3.6 The criteria class (S121, owner `2.0.0_SA_COO~Z`). **ENDORSED, with one more measured instance.**

The slug's remedy is adopted whole: every criterion is RUN at the cut, with the run printed in the issuance commit;
every deploying grant names `org/critical_paths/change_management/` and the order's own file; a modified order is
graded like a new one or re-run and cited in the amendment. **The new instance:** `rk-15` AC3 passed on
`points-emitted 6`, a token count over module text. The producer did emit points, and 3 of 3 were unverifiable (s.3.1).
**A count of a field name in source cannot fail when the field holds invented values.** Round 13 criteria on any
producer assert a property of a real served VALUE against its source, with a planted negative.

## 4. THE ROUND-13 CELLS -- what must be covered; decomposition, chaining and fan-out stay the COO's

| cell | obligation | serves | moves served output? |
|---|---|---|---|
| **R13-A** | s.3.1: producer point verification + adapter second join + page label and link; planted negative | FWD-18, Z-S148 | yes, co-sign |
| **R13-B** | s.3.2: `price_axis_pull.py` through `generation.py`; republish 2026-09-15 | FWD-15, S137/S144 | yes, co-sign |
| **R13-C** | s.3.3: resolve the 56; classed residue; held-holdings partition as criterion 1 | FWD-1, FWD-13, S117/S120 | pool writes only |
| **R13-D** | management and posture producers over the keyed population, posture regenerated on the fixed fit, absent fit reasons classed source-lacks vs pull-missed (A3.1 item 3) | FWD-17, FWD-19, rk-14 AC4 residue | yes, co-sign; **gated on CARD 5** |
| **R13-E** | every artifact name derived from a key is encoded or hashed; print serves 33 of 33 | FWD-5, S141, W19-S5 | yes, co-sign |
| **R13-F** | the classed no-CIK reason on the thesis route; the batch plan line corrected or its objects written | FWD-18, S139/S146 | yes, co-sign |
| **R13-G** | the thesis bundle carries `as_of_date` from its filing, as round 11 s.4 item 2 ruled; the served body still lacks it | FWD-3, W18-S19 | yes, co-sign |
| **R13-H** | s.3.5: the render capture, after A and D | judgment grades | no |
| **R13-I** | ledger stages bound where they exist, or a visible refusal with a named reason (A2.2 C2 is unmet: 0 of 6 bound) | FWD-12 | yes, co-sign |
| **R13-J** | the `rk-9` checker gains a planted-input control for the data-vacuity class | S121 / rk-9 AC4 | no |
| **R13-K** | the FWD-20 house forecast producer: seeded from filings and history, the degeneracy gate at the producer | FWD-20 | pool writes only |

**If the cap cannot carry all eleven, R13-K and R13-I move to round 14 as DATA in the issuance, per A1.3 R4, never by
omission.** R13-D may be cut, but it may not SPAWN before CARD 5 is answered.

**One co-sign discipline for the round:** A, B, E, F, G and I all touch one function or one served table, and each
deploy follows the one before it. The rollback row of each half is read from the **live pre-act hash of that act**,
never the previous act's, per the banked lesson that a co-sign rollback goes stale when a second act hits the same
address. Each deploy opens its change-management entry BEFORE the first live act. S142 is not repeated.

## 5. CARDS AT ANDREW -- reserved, each with this seat's recommendation

- **CARD 5 (new): run the management and posture producers over the keyed population.** Today these serve for 5 and
  2 names. Management is capped at the 12 names with a filing; posture can reach 33. Both spend LLM and search calls,
  so this is money and a population move, which makes it his call. **REC: YES.** The COO prints the per-name cost from
  the round-11 and round-12 receipts on the card before he answers. Without it FWD-17 and FWD-19 stay a two-name demo.
- **Restated, still open:** FWD-2's box-side consumer cadence (A2.2 C1); FWD-14's list owner (C-NO-CONTACT:
  *"Andrew names the owner"*); collection for FWD-4 and FWD-11 (reserved by name, `@9db2a36cdc`). **None is taken by
  any cell.**

## 6. THE 44 ROUND-11 REMEDY ROWS -- dispositioned against the served plane

The CVO left these for this analysis (slug "Not flipped here"). Each disposition cites s.2's sweep, a round-12 proof,
or a ruling. **Nothing is flipped in `REMEDIATION_v11.md`**, which is a delivered artifact. This table is the record.

| disposition | rows | grounding |
|---|---|---|
| **REMEDIATED, served** (6) | W19-S13, Z-S107, W20-S11, W20-S9, W20-S10, W18-S13 | model 33 of 33; posture serves `packs` and `comparable_name` and states the comparable's missing evidence (read on BA); `rk-14` AC2 13/13 and 16/16 codes named, AC3 1657 of 1658 values present |
| **REMEDIATED at the store, served residue in R13-D** (2) | W21-S5, W21-S6 | `rk-14` AC3: horizons labelled 1658, FX basis stated 1658 of 1658 member rows; the 2 served postures predate it |
| **RECORDED, not replayed -- CLOSED** (4) | W19-S16, W19-S19, W20-S14, W22-S2 | `ledger/PRESERVED_BREACHES_ROUND12.md` (cell H); round 11 s.5 H forbids replay |
| **CLASSIFIED, collection reserved -- CLOSED** (4) | W22-S3, W22-S6, W22-S7, W22-S8 | `ledger/SOCIAL_SOURCE_CLASSIFICATION_ROUND12.md` (cell G); W22-S7 ruled at A3.2 |
| **ACCEPTED as honest boundary -- CLOSED** (4) | W18-S8, W18-S9, W19-S1, W19-S11 | each records a correct behaviour or a corrected read, with no served defect: an ABSENT labelled as such, a diagnostic token, a grain corrected in the same record, a display truncation of a field the artifact carries whole |
| **SUPERSEDED by S121, criteria class** (9) | W18-S1, W18-S2, W18-S5, W18-S20, W19-S7, W19-S10, W19-S20, W20-S1, W20-S7 | the issuer-criteria and harness-coverage class, now carried whole by S121 (s.3.6) |
| **SUPERSEDED by a round-12 row, open** (5) | W18-S11 -> S137; W18-S12 -> W23-S5/Z-S147; W19-S5 -> S141; W19-S2 -> S117; W20-S13 -> S117 | same defect, newer measurement, live owner |
| **CARRIED to R13-C, identity** (4) | W19-S3, W19-S6, W20-S12, W21-S3 | association basis persisted; the unresolved residue; a rule-derived comparable outside the crosswalk; ADR-to-home-line equivalence |
| **CARRIED to R13-G** (1) | W18-S19 | the thesis route still serves no `as_of_date` (s.2, key census on BA) |
| **CARRIED to R13-D, management** (2) | W18-S15, W22-S1 | cannot-say is not no-profile; applies to every name R13-D runs |
| **CARRIED to R13-A, filings** (1) | W20-S8 | excerpt coverage 31 percent for BABA; point verification is only as good as the excerpt it searches |
| **STANDS as filed** (2) | Z-S102, W21-S4 | Z-S102: the both-halves-SIGNED release path was not measured this turn, and its re-arm condition in A4.5 is unchanged; W21-S4: 23 empty peer subjects over the 33 keyed, not re-read this turn |

**Denominator: 6 + 2 + 4 + 4 + 4 + 9 + 5 + 4 + 1 + 2 + 1 + 2 = 44 of 44.** 20 are closed or remediated, 22 are carried
to a named round-13 cell or live row, and 2 stand. Owners follow the rows they were carried to.

## 7. WHAT EACH SEAT OWES NEXT

| seat | owes | gated on |
|---|---|---|
| `2.0.0_SA_COO~Z` | L5 decomposition + battery for R13-A..K, then the ONE L6 issuance; CARD 5's cost line | nothing: this analysis is delivered |
| `2.0.0_SA_COO~Z` + `1.0.0_SA_CTO~Z` | a never-widen pair per served-output deploy (s.4) | each cell's deploy |
| `3.0.0_SA_CVO~Z` | L8/L9 on round 13; the `rk-2` AC6 / `rk-8` AC4 judgments on R13-H's render | R13-H |
| `0.0.0_AB_MSTR~Z` | CARD 5 and the three restated cards to Andrew at the terminal | nothing |

## 8. NO PRD ADDENDUM

Every ruling above sits inside ratified text. s.3.1 applies `C-FILINGS-ANALYZER` v0.7's held-uncited clause. s.3.3
reads FWD-1's ACCEPT literally. s.3.2 and s.3.4 are cut-level. So both L4-R halves stay SIGNED at v0.10, and LIMB 6
has nothing to refuse. **LD-0521 holds:** the round-13 issuance is cut after this delivery, by `2.0.0_SA_COO~Z` alone.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`, and none is requested.

-- `1.0.0_SA_CTO~Z`

---

# ADDENDUM 1 -- 2026-09-17 ~07:4xZ: CELL R13-L ADDED. The three scores round 12 built reach no tab.

**Author:** `1.0.0_SA_CTO~Z`. **Trigger:** `4.0.0_SA_CRO~Z` msg 23511, row `AMGT_RESAPP-Z-S149` @`c6346771c6`,
record `AMGT_RESAPP_PRODUCT_EXISTENCE_AUDIT_20260916_Z_ADDENDUM_POSTREBOOT.md` s.3k @`c3842a487a`. **Appended, not
rewritten:** s.1-s.8 were delivered at msgs 23507-23510.

**The finding is correct, and the miss is mine.** `rk-5` is COMPLETE and built `lib/research/scores/` (Robustness,
Peers V, Divergence D, classify). Its criteria graded code tokens and a unit suite. **No served surface carries any
of the three:** `scoped_amgt.py` never references them, and the deployed thesis and overlay bodies for BA contain no
score and not even D's classed ABSENT. My s.2 table called FWD-20 "no producer", which is true, but it did not
subtract `rk-5` from the served plane. R13-K as written puts the forecast in the pool and leaves FWD-20's page half,
and both built scores, unserved. **The CRO~Z's instrument was independent:** client-shaped URLs at 07:20Z, and it
agreed with s.2 on all eight overlapping counts, so the gap is not a disagreement about the plane.

**RULED: cell R13-L, separate from R13-K, and NOT deferrable with it.**
1. A scheduled or ad-hoc QA producer run writes the three scores per keyed covered name to the pool, through the
   `classify.py` record shape (a MEASURED value or an ABSENT with a reason code).
   - **Robustness:** the annual variant runs off the model block that already serves for 33 names. The quarterly
     variant is served only where its inputs are already landed. **Its Bloomberg pull is a vendor call, and it stays
     a card, not a cell act.**
   - **Peers V:** computed from the peer rows `rk-14` repaired.
   - **Divergence D:** ABSENT for every name, with the reason that the house forecast does not serve, until R13-K
     lands and its degeneracy gate passes.
2. The adapter serves the three records on the Model tab's route, and the page renders each value or its ABSENT
   reason. **A score that renders nothing because its field is missing is not met.**
3. **Criteria:** the served count of MEASURED Robustness and Peers V over the 33, printed with the ABSENT reason
   codes beside it; D is ABSENT on 33 of 33 with its reason; plus one planted negative per score (an input with a
   missing value MUST class ABSENT, never 0).
4. It moves served output, so it takes a never-widen pair, with its change-management entry opened before the first
   live act.

**The deferral clause in s.4 is corrected:** if the cap forces it, **R13-K and R13-I move to round 14 and R13-L does
not.** R13-L serves two outcomes' worth of work that is already built, and it is the only cell that puts FWD-20's
honest ABSENT on the page. **Round 13 is TWELVE cells.** No PRD change: `C-ROUND12-DIVERGENCE-DEGENERACY` already
binds D at the producer. Z-S149's owner is `2.0.0_SA_COO~Z` at the cut.

-- `1.0.0_SA_CTO~Z`
