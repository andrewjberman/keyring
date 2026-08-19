# CVO VERDICT — D3 package (Account-Level Model Overlay)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D3_ACCOUNT_MODEL_OVERLAY_PRD.md` @375c874a9e (219 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D3_ATOMDECOMP/run_20260819.md` @375c874a9e (63 lines)

**Verdict: ACCEPT — 0 P0, 2 P1, 1 P2. The strongest package of the five read so far.** No finding
touches the design. Three things it does that I want on the record because they are the pattern the
other packages should copy:

1. **The evidence INVERTED the design and the PRD says so.** §5.3: reading `a06_dim_identity_crosswalk.py`
   reframed the precondition from *"build a join"* to *"close and classify the residual"* — the
   ground-truth chain doing exactly its job, caught before decomposition rather than at TO authoring.
2. **It consumes instead of duplicating, and names the failure mode.** §3: the advisor slice consumes
   `dim_portfolio_group`/`bridge_group_account` from D2's decomposition, *"duplicating the build here
   would be the two-homes defect."*
3. **It carries the overlap invariant that D1 asserted away.** §3's overlap-handling rule and §4.4 make
   never-sum-across-groups a component-level invariant, and TO-D3.4's acceptance **exercises** it
   (*"no figure sums an account into 2+ books"*). **Same author, same day, same measurement — carried
   here, contradicted in D1.** That contrast is the evidence for D1's P0-2, and it is why I rank D1's
   as P0 and file nothing equivalent here.

---

## P1-1 — For CTO. The PRD under-declares its own run by two cells, and its own §2 cites outside the declared range. Second instance of this defect.

§1's ground-truth pointer reads: *"(cells **#1-#11**, U1-U3)"*. The run contains **#1–#13**.

The two excluded cells are the newest and most consequential — **#12** (Portfolio Group = the advisor's
book; 216 groups; Travis $456.8M group-grain vs $373M role-attributed) and **#13** (groups OVERLAP,
90.6% of accounts in 2+ groups, ~$10.2B vs ~$1B, `Primary Portfolio Group` as partition key). **§2
cites them explicitly** (*"run #12/#13, CRO~A"*), as do §3's overlap rule and §4.4. So the PRD's
declared range excludes rows the PRD itself relies on.

**This is the second instance** — D1 pinned *"rows R1-R14"* against a run of R1–R17, and there too the
excluded rows carried the newest material. **Both are late-landing rows (CRO~A's same-day scan) that
did not propagate into the pointer.** Recommend fixing as a family-level check rather than two edits:
**when a run gains rows after the PRD pointer is written, the pointer is part of the amendment.** Cheap
mechanical form — assert the declared range against the run's actual max row at absorption time.

---

## P1-2 — For CTO. §4.2's coverage-breach flag has no named reader, which makes a breach ship silently. Fourth instance of one class tonight.

§4.2 error case: *"join coverage below the spec's registered floor = publish WITH the breach flagged in
manifest (**no alarm machinery -- moratorium**; the floor consumer is the parity/acceptance read)."*

**The moratorium call is correct and I am not challenging it** — a flag in the manifest is a record, not
an alarm, and that is the right instrument. The gap is the second half: *"the floor consumer is the
parity/acceptance read"* names a consumer **class**, not a **reader with a moment**. TO-D3.5 is a
one-time acceptance pass; after it closes, nothing in the PRD reads the flag again. So an ongoing
coverage regression publishes with a flag nobody opens — the manifest is honest and unread.

**Recommend:** name the reader and the moment (e.g. the flag is asserted in the producer's own next-run
manifest comparison, or read at each publisher pair run — a check at a moment that already executes,
per D0's governing test *"free-to-check at an existing moment"*). One line; no new apparatus.

---

## P2-1 — For CTO. Vocabulary: a fourth spelling, and it is the epistemically cleanest one.

D3's run declares **MEASURED | RECORD | INFERRED**. Across five packages: D2 `MEASURED-AT-RECORD`,
D7 `MEASURED-RECORD`, D1 `MEASURED (record)`, D3 **`RECORD`**. You ruled `MEASURED-AT-RECORD` canonical
at @36a7fbd70e and **I am not asking you to reopen a fresh ruling.**

One observation for the record only: **D3's `RECORD` is the only spelling that does not attach the word
MEASURED to a claim the author did not measure** — which was the root cause I named in D2's P0-1. Your
own drafting instinct, unprompted and in the same pass, reached for the cleaner form. If the canonical
spelling ever gets revisited, that is the datum. **Deferring to your ruling; no action requested.**

---

## Explicit deferrals

- **U1 (SmartX model-identity edge) unresolved** — correctly marked as an investigation atom, explicitly
  *"not an expected-value"* in the run's own boundaries, and owned by TO-D3.1 which gates on nothing.
  **Conforming; the pattern D0's TO-5 should have followed.**
- **Cell #5 verdict RECORD, not MEASURED** — the run says *"NOT identified this run … record only; no
  source read this session."* Honest and correctly downgraded. No finding.
- **The book-definition question (§7 Q4)** — served-semantics, P4-class through CTO, carried
  **consistently in both D2 §9 Q3 and D3 §7 Q4** with the same recommendation and the same measured
  basis. Cross-PRD consistency verified; not a defect. Andrew's word, not mine.
- **§6 existence checks** — in protocol form (`git log` on the PRD path, comp-find name scan with
  denominator 18/1059, tree read for the absent producer, run #7 for the UI components). Conforming.
- **`platinum/advi/` absence claim (#6)** — names its bucket AND its exact prefix and carries a positive
  control. **This is the firm-scope absence discipline CLAUDE.md Rule 21 demands, applied correctly
  and unprompted.**

---

## What you should have asked but did not

**The moratorium removed the wrong reflex and never supplied the replacement — and tonight's packages
show the gap in four places.**

Across five packages I have now found the same shape four times:

| Package | The record that exists | Why nobody reads it |
|---|---|---|
| D2 | C4's ours-vs-Schwab adjudication | clears us using our own input as our own witness (§3 derivation) |
| D7 | the SLA receipt timestamp | lives only in Analyst memory; an un-ticketed mail leaves no durable trace |
| D1 | `category_views` absent → fallback | a failed rollout renders identically to a correct pre-rollout state |
| D3 | the coverage-floor breach flag | named consumer is a class, not a reader at a moment |

**None of these is an alarm problem, and in every case the author correctly refused to build an alarm.**
The moratorium is right: *"a monitor on an unsettled route measures the wrong thing precisely."* But its
stated remedy is **CANONICAL ROUTES AND SCHEDULES FIRST** — *define the flow* — and "who reads this
record, at which moment" **is** the flow. That half is not being supplied, so honest records are landing
with no consumer, which is the alarm anti-pattern's mirror image: instead of apparatus that watches a
class nobody defined, we get a defined class nobody watches.

**Recommend a family-level convention rather than four fixes:** every PRD error-case or flag that lands
a record names its **READER + MOMENT**, and "the acceptance pass" only counts if the check recurs at a
moment that already executes. This is not new machinery — it is the discipline D0's own governing test
already states (*free-to-check at an existing moment*), applied to records instead of to fixes. Worth
ruling once now, while eight of these packages are still pre-dispatch, rather than discovering it four
more times.

— 3.0.0_SA_CVO
