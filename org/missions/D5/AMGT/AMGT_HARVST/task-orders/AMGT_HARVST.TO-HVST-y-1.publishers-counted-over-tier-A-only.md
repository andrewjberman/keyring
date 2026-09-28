# AMGT_HARVST task order -- `HVST-y-1` -- ROUND 10 cell 1 of 3: count event publishers over TIER-A ONLY, and carry the round's JUDGMENT criterion

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-y-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~28</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on lib/research/harvest/publication_gold.py; this cell arms nothing and deploys nothing.
comp-iam: RUN at L5 on the DESIRED plane -- AC3's ad-hoc rebuild needs S3 GET on the gold mention snapshot and PUT on chatter_event. A refusal is a BLOCKING row, never a workaround.
comp-adversary: RUN at L5 -- the adversary is a criterion that counts 8 events and passes while two event_ids are silently orphaned. AC2 exists for that.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO VENDOR CALL and NO NETWORK except our own S3** (Opal-owned, permitted, not a vendor act). You will make
   no request to seeking-alpha, bloomberg, wsj, ft or barrons, and you will not invoke
   `lib/opal_data_harvest`'s `run` command.
2. **NO S3 DELETE, ever.** AC3 WRITES one new `chatter_event` snapshot; it removes nothing.
3. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~28/scripts/` -- **never
   `.scratch/`.**
4. ⛔ **YOUR INSTANCE MUST BE NAMED EXACTLY**
   `.../deliverables/0.9.0_WK_AMGT_HARVST~28/AMGT_HARVST.TO-HVST-y-1.publishers-counted-over-tier-A-only.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-y-1.publishers-counted-over-tier-A-only`. A gate globs that exact stem
   and refuses anything else before any limb runs (decomp `s.14x`).

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~28/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE CHANGE -- one clause in a PURE function

`C-HV-EVENT-SPINE` is amended (PRD v0.3, ratified half signed by `3.0.0_SA_CVO~O` @`0797bae2d5`): **the publisher
count is taken over TIER-A articles only.** `min_articles` still counts tier A **or** B.

**Today** `publication_gold.event_rows` (PURE -- explicit args, no I/O, no clock) qualifies a day on
*"at least `min_articles` tier A or B rows from at least `min_publishers` distinct publishers"* -- the publisher
set is built over A **and** B. **Amend it so a publisher counts only if it contributes at least one TIER-A
article on that day.**

⭐ **THE ISSUER HAS ALREADY MEASURED YOUR DISCRIMINATOR -- use it, do not invent one.** Two 2-row inputs, run
in-memory at this cut:

| input | today | required AFTER |
|---|---|---|
| 2 x tier-A, 2 publishers | 1 event | **1 event** (must STILL qualify) |
| 1 x tier-A + 1 x tier-B, 2 publishers | **1 event** | **0 events** (only ONE publisher contributes tier-A) |

⚠ **`published_utc` MUST BE A `datetime`, NOT AN ISO STRING** -- `_day_of` calls `.tzinfo` on it directly and an
ISO string raises `AttributeError`. Measured at this cut; it cost the issuer one run and it is not a defect.

## 2. THE EXPECTED DIFF ON REAL DATA -- NAMED, not discovered

`3.0.0_SA_CVO~O` measured it at daily grain (`ADJUDICATION_v17`): **12 events -> 8**, the **4 spurious ones
absent**, AND ⛔ **2 SPANS NARROW SO THEIR `event_id` CHANGES** -- `BA` 09-07..08 -> **09-08**, `HD` 08-17..20 ->
**08-18**.

⛔ **`_event_id` IS `sha256(security_key|first_day|last_day)`, so a narrowed span is a NEW ROW WITH A NEW ID, not
an edited row.** A criterion that only counted "8 events" would PASS while silently orphaning two ids. **AC2
requires both ids named and matched.**

## 3. BOUNDS

1. **Three criteria, no fourth.** A fourth finding is a surprise ROW; you keep working.
2. **Do not change `EVENT_MIN_ARTICLES`, `EVENT_MAX_GAP_DAYS` or `_EVENT_QUALIFYING_TIERS`.** Only the publisher
   count's population moves.
3. **`event_rows` STAYS PURE.** No I/O, no clock, no default that reads the world. Its purity is what makes AC1
   and AC2 provable without S3.
4. **AC3's rebuild is an AD-HOC QA RUN, not production evidence** (CLAUDE.md). It is safe because **no served
   surface reads `chatter_event`** -- measured 0 hits across 10,085 files in `portal`/`infra/aws`/`data`, so
   NEVER-1's never-widen pair does not fire. **If you find a served reader, STOP and file a BLOCKING row.**

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical + ONE judgment

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-y-1"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line -k event</invocation><expect>THE AMENDED RULE IS PINNED BY TESTS THAT FAIL ON THE OLD BEHAVIOUR. New cases, named in the -rA output: (a) 2 tier-A rows from 2 publishers on one day still yields 1 event; (b) 1 tier-A + 1 tier-B from 2 publishers yields ZERO events, where today it yields 1 -- this is the negative control and the criterion FAILS if it passes against HEAD's unamended function; (c) purity, two identical calls returning equal row lists. Print the whole-suite count before and after so a new red test elsewhere is not hidden by the -k filter</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-y-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~28/scripts/ac2_expected_diff.py</invocation><expect>THE WHOLE NAMED DIFF, IN MEMORY OVER THE LANDED MENTION ROWS, with no gold write. Print: the BEFORE event count (expected 12) and the AFTER count (expected 8) from the same input; the 4 spurious events ABSENT, each named by security_key and span; and the TWO event_id MOVES proved by printing, for BA and HD, the old span, the new span, the OLD event_id and the NEW event_id and showing they differ and that the new one equals publication_gold._event_id(security_key, new_first_day, new_last_day). A run that reports 8 events without naming both id moves FAILS this criterion. Also print C-HV-GOLD-REBUILDABLE: two builds over the same input produce identical row lists</expect></criterion>

  <criterion id="AC4" cell_refs="HVST-y-1" judgment="true"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~28/scripts/ac4_are_the_eight_real.py</invocation><expect>JUDGMENT, PRESENTED AND NOT GRADED -- status UNVERIFIABLE-BY-INSTRUMENT with status_reason naming 3.0.0_SA_CVO at L9 as the oracle. ARE THE SURVIVING 8 EVENTS THE REAL COVERAGE BURSTS? For each of the 8 print the security, the span, lead_headline, articles_total, publishers_distinct, tier_a/tier_b, and BESIDE IT the headlines of every article in the span. Then state per event whether the lead_headline names what the burst was about, and where it does not, say what the span actually looks like. Andrew's own test is the standard: an event about a DIFFERENT company's product is not this security's burst. Present the text; record NO verdict of your own</expect></criterion>
</proof_of_spec>

## 5. WHAT THIS CELL DOES NOT DO

No vendor call. No S3 delete. It does not build the timeline page (`y-3`) or touch FWD-4 (`y-2`). It does not
re-grade FWD-6 -- that is the CVO's at L9.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **s.14x honoured: every invocation was RUN at this cut.** AC1's pytest path collects; AC2/AC4 name scripts the
   criterion creates (s.14x's stated non-application). The in-memory discriminator and the `datetime` trap were
   both found by running, not by reading -- and the trap is handed to the worker rather than left to cost it a
   cycle.
2. **AC2's id clause is the whole reason this cell is not a one-liner.** `_event_id` hashes the span, so the two
   narrowings are new rows. A count-only criterion passes over an orphan.
3. **The judgment criterion is HERE, not on `y-3`, deliberately.** The round-8 rule requires it on a cell issuable
   without a pending Andrew word; `y-3` was blocked on a placement ruling when this was cut, and holding the
   judgment with it would have left round 10 judgment-less for a third consecutive round.
4. **NEVER-1 checked and does NOT fire** -- census in decomp `s.22.2`, with the zero's bounds stated. **It WILL
   fire the round after `y-3` ships a served reader.**

## 6. THE VERDICT -- `complete`. VALID (rc=0), and the worker built TWO controls nobody asked for

**Measured at the merged HEAD after the drain (`72401942b5`), re-read post-merge:** violations 0,
invocation-alignment 3/3, artifact-resolution 5 of 5 resolved at pin. **VALID (rc=0).**

| | |
|---|---|
| AC1 | `17 passed, 129 deselected` on `-k event`. ⭐ **A MUTANT CONTROL proves the new test is not vacuous** -- `test_one_tier_a_one_tier_b_two_publishers_no_longer_qualifies` FAILS against the unamended predicate (`assert [{...BA_US_Equity...}] == []`). Whole-suite **146/146** after vs **145/145** before |
| AC2 | **12 -> 8 events**, the 4 spurious named (`992_HK`, `COST`, `DELL`, `MSFT`), and **BOTH `event_id` MOVES PROVED** -- `OLD != NEW` **and** `NEW == _event_id(security_key, new_first, new_last)` for `BA` and `HD`. `C-HV-GOLD-REBUILDABLE: True`; two runs byte-identical |
| AC4 | JUDGMENT, **PRESENTED with no verdict**, oracle `3.0.0_SA_CVO` at L9 named. All 8 events with span, lead, counts and member headlines |

⭐ **THE SECOND UNASKED CONTROL:** the pre-amendment baseline was measured **in an ephemeral detached worktree
that the worker then removed**, leaving the shared tree untouched. That is the discipline 14b wants and no
clause in this order required it.

### THE LOOP THIS CELL CLOSES, across three rounds

`HVST-w-3`'s AC4 presented the cross-company `lead_headline` as a judgment question -> `3.0.0_SA_CVO~O`'s L9
(`ADJUDICATION_v17`) found **4 of 12 events were not coverage about their own security** -> `1.0.0_SA_CTO~Z`
amended `C-HV-EVENT-SPINE` by addendum -> **this cell's amendment removes exactly those four.** ⛔ **A mechanical
column was green on all 12 the whole way.** Only the judgment criterion could have started it.

**ISSUER CLOSE-VERIFICATION (rule 22), run separately from the worker:** at the merged HEAD,
`2x tier-A / 2 publishers -> 1 event` and `1x A + 1x B / 2 publishers -> 0 events`. The rule behaves as
specified in the shared tree, not only on the branch.

**NO ROWS FILED, reported as an outcome:** the discriminator, the `datetime` trap and the existing-test
collateral were all anticipated by the order, so there was no surprise to file.

<risk>LOCAL</risk>
<status>complete</status>
<round>10</round>
<slot>~28</slot>
<fabric>site-z</fabric>
