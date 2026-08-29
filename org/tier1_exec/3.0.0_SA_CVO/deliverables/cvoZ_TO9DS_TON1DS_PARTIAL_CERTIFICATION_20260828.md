# CERT — `ETFS_INGEST.TO-9-DS` **3 of 5** · `D1_CATVIEWS.TO-N1-DS` **3 of 8** — BOTH PARTIAL

**Certifier:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~19:5xZ · **Executors:**
`0.4.0_DS_ClientPlatform~Q` (TO-9-DS) · `0.4.0_DS_ClientPlatform~Z` (TO-N1-DS)
**Authority:** Andrew-direct ~19:3xZ — *"lets proceed whatever needs to be proceeded to categorically
close this out."*

```
TO-9-DS   rc=0 VALID  rows=5  violations=0   3 PASS · 2 UNCOMPUTABLE
TO-N1-DS  rc=0 VALID  rows=8  violations=0   3 PASS · 5 UNCOMPUTABLE
```
⛔ **NEITHER TO CLOSES.** Seven criteria across the two are UNCOMPUTABLE. ⚠ **AMENDED 2026-08-28 ~21:1xZ:
this line originally said “all seven lift at ONE event”. THAT GROUPING WAS WRONG and so was the date it
named — see §3 and the AMENDMENT block at the end.** This is a terminal state, not an open question.

---

## 1. ⛔ I WAS ONE TURN FROM CERTIFYING ON `rc=0`, AND THAT IS THE ENTRY THIS CERTIFICATE OWES

I told the fabric: *"decomp_ref repaired → I certify 3 of 5 the same turn."* The field was repaired,
I ran the checker, got **rc=0 VALID**, and was about to certify. `2.0.0_SA_COO~Z` stopped it.

**What rc=0 was hiding at that moment:** `decomp_ref.doc` had been pointed at
`runs/etfs-ingest/…/DECOMP.md` — **a real file, a real vintage, and a lineage that does not exist.**
Nothing in that TO derives from that decomp. **The schema checks SHAPE, not TRUTH**, so a decorative
provenance field satisfies it perfectly.
>> **THAT IS WORSE THAN AN UNPOPULATED PROVENANCE FIELD — it is populated with something false, which
   no consumer can reject on.** CLAUDE.md's *a value must carry its claim* names the consuming half as
   the whole mechanism; here the consuming half was satisfied by a lie.
⭐ **My own rule caught nothing because I did not apply it.** I have written twice today that a green
run from a refutation-only or shape-only instrument is not a correctness verdict — and then took one.

**RESOLVED, and the remedy is the precedent I had myself named** (`MDPF_GLOBAL.TO-ACCEPT-0826`):
```
  decomp_ref.doc            = the TO'S OWN PATH   (where its ids are actually minted)
  decomp_ref.vintage_commit = 3b9928d23b
  VERIFIED: `git cat-file -e 3b9928d23b:<that doc>` -> EXISTS
  NEGATIVE CONTROL: same probe at bf74d031c1 -> ABSENT, so the pin check discriminates
```
**The claim is now true, and rc=0 means something.**

### ⚠ AND ONE LIMB OF THE STOP'S OWN EVIDENCE DOES NOT DISCRIMINATE — corrected here, not repeated
`2.0.0_SA_COO~Z` cited two things: *all 5 rows `cell_refs=None`*, and *zero `INGEST-T*` ids on the
face*, with TO-8 as a positive control. **Measured at this seat: TO-8's instance rows carry
`cell_refs = None` on all SIX rows too** — and TO-8 *is* genuinely decomp-derived.
>> **So row-level `cell_refs=None` is NOT the discriminator; it is the same on both.** The conclusion
   stands entirely on the **face** limb — TO-9-DS face: **0** `INGEST-T*` ids; TO-8 face: **2**. Recorded
   so the finding is reusable on its sound half rather than its shared one.

### THE HOLD IS DISCHARGED, AND ITS CONDITION WAS SET BY THE SEAT THAT PLACED IT
`2.0.0_SA_COO~Z` held `TO-9-DS` and named the remedy. **Measured at this seat at certification time,
the remedy had already landed** (the file moved again between that seat's two messages):
```
  decomp_ref.doc            = the TO's OWN path      <- the named remedy, applied
  decomp_ref.vintage_commit = 3b9928d23b             <- pin CONTAINS that doc (verified, controlled)
```
**Its stated condition is met, so I am certifying rather than holding.** ⭐ And that seat narrowed its
own hold before it over-applied — re-running with a GENERAL cell regex plus a TIER-form probe plus a
positive control (TO-8 → 2 cells) rather than the single id shape it first used, **which is the exact
error the whole cell-id episode was about today.** The verdict survived a wider net; the evidence
became sound rather than lucky.

⚠ **AND THE HOLD WAS CORRECTLY NOT APPLIED TO `TO-N1-DS`.** That TO cites `D1-h-p2` and `D1-inv-4` —
real cells in the named decomp — so its `decomp_ref.doc` is honest and there was never a false
lineage. **The discriminator is whether the TO CITES CELLS, not whether the instance names a doc.**

### ⚠ ONE ROW-QUALITY GAP ON `TO-N1-DS` — NAMED, AND IT CHANGES NO VERDICT
**0 of 8 acceptance rows carry `cell_refs`**, while the face cites `D1-h-p2` and `D1-inv-4`.
Alignment is ANNOUNCE (the TO carries no formal `<decomp_ref>` block), so nothing is enforced and
nothing is violated — **but the criterion→cell join that exists in the TO does not exist in the
instance.** A future reader cannot trace it from the artifact alone.
**Not a defect in the evidence and not a blocker: certified as scored.** Recorded because the
traceability was available and free, and the same gap on a pipeline-cut TO would have been INVALID.

---

## 2. WHAT IS CERTIFIED

**`ETFS_INGEST.TO-9-DS` — AC1, AC2, AC5.**
- **AC1** — 7 completions round-tripped, **5 negative controls REFUSED / 0 accepted**, 50 assertions.
  ⛔ Recorded per the standing ruling as **UNFALSIFIED (refutation-only control)**, never PASS-as-
  correctness — more than one completion can round-trip to the same 30 chars. The sovereign
  ratification by sight (Andrew, 18:10Z) is a **separate line, not a second pass.**
- **AC2** — 23 distinct served values swept, 7 changed / 16 unchanged, **0 derived-but-labelled-observed**.
  The label follows the VALUE, not the table's involvement.
- **AC5** — planted collision RAISED, negative control on the real 7-entry table does not raise.

**`D1_CATVIEWS.TO-N1-DS` — AC1, AC2, AC8.** Each measured on an instrument *different* from the
executor's, which is what makes it corroboration:
- **AC1** — registry × predicate over 15 members: old `vp=="SMA"` matched **0 of 6**; shipped
  `_l0_of(vp)` matches **6 of 6**. **POSITIVE CONTROL: Models 9 of 9 both before and after**, so the
  probe was never blind.
- **AC2** — **AST walk on the DEPLOYED bytes**, negative-controlled against `70a0828226^`. Pre-fix the
  two branches of one `if/elif` were *different AST node types* (`Call` vs `Compare`); deployed, both
  are `Compare` of `_l0_of(...)`. **Raw `view_path` equality surviving: ZERO.**
- **AC8** — the estate-wide limb the commit recorded as "NOT CLAIMED" is now run **with its denominator.**

---

## 3. ⛔ THE SEVEN UNCOMPUTABLE ROWS ARE ONE EVENT, AND THAT IS THE HONEST TERMINAL STATE

```
TO-9-DS   AC3, AC4     served object 13:01:26Z   vs deployed fn 18:49:14Z   (~5.8h)
TO-N1-DS  AC3..AC7     served object 13:31:13Z   vs fix 16:04Z / apply 17:28:29Z
```
**In both cases the AFTER has no referent — the served artifact predates the deploy.** Every one of
the seven says *"from the served artifact"* or *"before and after"*, and that phrase governs both
halves. Marked UNCOMPUTABLE rather than scored, correctly, by both executors.

⭐ **`CATV-TON1-AC6` IS THE ONE MOST EASILY WAVED THROUGH AND THE EXECUTOR DID NOT:** the `D1-inv-4`
sum invariant **held at 1,762,750,154.52 WHILE THE DEFECT WAS LIVE.** A before-only reading of an
invariant that passes in *both* worlds has **no discriminating power at all** — passing it would have
been evidence of nothing. That is the single sharpest judgement in either instance.

**`CATV-TON1-AC7`'s gate has NARROWED to a clock.** Precondition 1 (package carries the fix) is
DISCHARGED and the executor measured it independently rather than relaying: pulled the live
`mdpf-gold-lambda` package, extracted the member, sha256 `8781c4d7ecde90…` — **matching the value
`0.7.0_AE_CloudOps~Z` obtained by `cmp`. Two seats, two instruments, one value.** State is **APPLIED,
explicitly NOT EXERCISED.**

>> ⛔ **RETRACTED AND REPLACED — SEE THE AMENDMENT BLOCK BELOW.** This paragraph said all seven, plus
   `TM1-AC1` and `CATV-TOV1-AC7`, lift at ~13:0xZ **2026-08-29**. **2026-08-29 IS A SATURDAY**, and the
   five `CATV-TON1` criteria lift **MONDAY 2026-08-31**, not tomorrow. The `TO-9-DS` pair sits on a
   DIFFERENT PIPELINE and its lift event is **UNMEASURED at this seat**. <<
   What survives unchanged: no ad-hoc run beats the scheduled fire — the TOs forbid it and an ad-hoc
   artifact is never production evidence.

---

## 4. SCOPE

- ⛔ **Neither TO closes, and D4 cannot be categorically closed on evidence tonight.** Any close must
  say **3 of 5** and **3 of 8** — a close implying full satisfaction is the same falsehood class as
  *"STAGED, never started."*
- **It does not certify the truncation fix as correct.** AC1 is UNFALSIFIED on a refutation-only
  control; `basis` stays `inferred-from-truncation`.
- ⚠ **Surfaced by the executor, not mine to close:** all four served scopes carry the sovereign-citing
  *"A TRUE ZERO"* sentence; it is TRUE at cottonwood and inflection, FALSE at 49financial (which the
  TO covers) and **FALSE at `global`, which NO criterion on that TO names.** Routed to
  `2.0.0_SA_COO~Z` as issuer.
- **Push state:** both instances and this certificate **LOCAL** at authorship; push is the
  integrator's leg.

— `3.0.0_SA_CVO~Z`

---

## ⛔ AMENDMENT — 2026-08-28 ~21:1xZ: THE LIFT EVENT WAS WRONG TWICE, AND THE SECOND ERROR IS THE WORSE ONE

**Issued by the certifier against the certifier's own committed artifact.** Neither correction changes
a single VERDICT above — 3 of 5 and 3 of 8 stand, and every PASS and every UNCOMPUTABLE is unmoved.
What was wrong is **when the UNCOMPUTABLE rows become computable**, which is the operational half other
seats were scheduling against.

### 1. ⛔ 2026-08-29 IS A SATURDAY, AND I NAMED IT AS THE LIFT EVENT WITHOUT RESOLVING THE CALENDAR
```
  2026-08-28  Friday   <- issuance date
  2026-08-29  Saturday <- what this certificate called "THE NEXT SCHEDULED FIRE"
  2026-08-31  Monday   <- the real lift for the CATV rows
```
CLAUDE.md carries a **NEVER** on exactly this: *"NEVER call a pipeline stale/broken until you resolve
the TRADING CALENDAR — count trading days. Friday IS Monday's answer."* I wrote a lift schedule off a
calendar date without counting a trading day.

**MEASURED, and it is not merely that the market is shut:** the A6 manifest key
`_manifests/{data_as_of}/{run_ts}.json` records that **4 of 4 weekend runs computed the PRECEDING
FRIDAY's `as_of`** (denominator 42 manifests). A same-`as_of` run writes to an EXISTING key, so the
served object **does not advance**. Every one of the five `CATV-TON1` rows reads *"from the served
artifact"* or *"before and after"* — so the AFTER referent is not created on Saturday or Sunday.
⭐ **AND THE B0 REMEDY LANDED TONIGHT DOES NOT CHANGE THIS — IT MAKES THE NON-ADVANCE CORRECT RATHER
THAN ACCIDENTAL.** With `category-views` declared (`7604f2b4bd`), the weekend run now returns
`unchanged` instead of raising `KeyError`. **That is the RIGHT answer and it still writes nothing.**
A conflict is not a delivery; only a NEW `as_of` advances the object. **Monday 2026-08-31.**

### 2. ⛔ THE WORSE ERROR: "ALL SEVEN LIFT AT ONE EVENT" JOINED TWO DIFFERENT PIPELINES
```
  CATV-TON1-AC3..AC7   MDPF gold consolidator    13:30Z   EventBridge SCHEDULER
  TO-9-DS AC3, AC4     ETFS positioning          13:00Z   EventBridge RULES
```
**These are two producers, two planes, two schedules and two `as_of` derivations.** I measured the
MDPF surface and **extended its answer to a surface I never measured**, then presented the result as a
single event with a single date. That is the one-banner-over-two-evidence-classes failure, committed
inside a certificate whose own §1 is about a wrong-referent verdict.
⚠ **THE `TO-9-DS` LIFT EVENT IS UNMEASURED AND I AM LEAVING IT THAT WAY RATHER THAN GUESSING.** What I
did measure, with its denominator, is too thin to carry a claim and raises a separate question I am
not chasing into another lane:
```
  portal/gold/etfs/positioning/_manifests/   DENOMINATOR 2 objects / 2 dates: 08-20 Thu, 08-21 Fri
  portal/gold/etfs/positioning/book/         DENOMINATOR 2 objects / 2 dates: 08-20 Thu, 08-21 Fri
  weekend-dated: 0 -- BUT WITH n=2 AND NEITHER A WEEKEND, THAT ZERO MEANS NOTHING.
```
**Two observations, neither on a weekend, cannot distinguish "skips weekends" from "has not run since
08-21."** Surfaced to the owning lane as an OBSERVATION; it is not evidence for either reading.

### 3. WHAT DOES NOT CHANGE
- **No verdict moves.** 3 of 5 and 3 of 8; the seven UNCOMPUTABLE rows remain UNCOMPUTABLE and were
  correctly refused by both executors. **`CATV-TON1-AC6` remains the sharpest judgement in either
  instance** — the invariant held while the defect was live, so a before-only reading discriminates
  nothing.
- **No ad-hoc run beats the scheduled fire**, and the reason is unchanged.
- ⛔ **This certificate still does not close D4.**

— `3.0.0_SA_CVO~Z`
