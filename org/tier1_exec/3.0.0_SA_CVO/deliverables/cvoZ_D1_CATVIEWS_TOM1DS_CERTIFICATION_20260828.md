# CERT — `D1_CATVIEWS.TO-M1-DS` — **PARTIAL: 4 of 5 CERTIFIED, `TM1-AC1` CORRECTLY UNCOMPUTABLE**

**Certifier:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~17:1xZ · **Executor:** `0.4.0_DS_ClientPlatform~Z`
**Instance:** `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/D1_CATVIEWS.TO-M1-DS_PROOF_OF_SPEC.json` @`c5b405f643`
**Producer build:** `a5227cf161` · **TO face:** @`98c35fa0e1` (post-ROUTE-A)
**Authority to certify:** Andrew-direct ~16:5xZ — *"If CVO~Z needs to do some final certifications and etc. on ETFS or D4 work, that is fine, i can handle that with them directly."*

---

## VERDICT

```
TM1-AC1   UNCOMPUTABLE   NOT certified. Correctly withheld by the executor. See §1.
TM1-AC2   CERTIFIED      on the EXERCISED plane, which the instance names itself.
TM1-AC3   CERTIFIED      (denominator CITED, not independently confirmed -- §5)
TM1-AC4   CERTIFIED ON THE CLAIM, WITH A FINDING -- the claim is TRUE, its CITATIONS
                         RESOLVE TO NOTHING AT ANY REF. See §3.
TM1-AC5   CERTIFIED      (same denominator caveat as AC3 -- §5)
```
**THE TO DOES NOT CLOSE.** One criterion is outstanding and its lifting event is not this lane's act.

---

## 1. `TM1-AC1` — UNCOMPUTABLE, AND THE WITHHOLDING IS RIGHT

AC1 requires every L2 node under `Models` to carry a dollar value **on the SERVED artifact, from a
SCHEDULED run**. The executor marked it `UNCOMPUTABLE` — *"nothing measured contradicts the criterion;
the instrument's subject does not exist yet"* — and refused the ad-hoc run the TO forbids.

⭐ **THAT IS THE CORRECT STATUS AND IT IS THE HARDER ONE TO WRITE.** The build half is done and
exercised (8 of 9 Models L2 nodes carry a value at ≥1 scope, over real cached gold inputs). It would
have been easy to score that as PASS and let the served restatement follow. `UNCOMPUTABLE` is
neither PASS nor FAIL and it is the only honest cell here.

⛔ **AND THE LIFTING EVENT HAS TWO PRECONDITIONS, NOT ONE — THE SECOND IS MEASURED AND UNMET.**
The instance names the lift as *"the next scheduled mdpf-gold fire AFTER the gold-lambda package
contains `a5227cf161`."* Both halves are required, and the deploy half is **currently false**:

| instrument | seat | reading |
|---|---|---|
| `lambda get-function-configuration` | `2.0.0_SA_COO~Z` (13442) | `LastModified 2026-08-28T01:12:11Z` — predates the 15:51Z fix |
| **deployed package bytes, downloaded and read** | `1.0.0_SA_CTO~Z` (13457) | `view_path == "SMA"` still at `:591`; `_l0_of` occurrences **0**, against a positive control of **3** in the fixed source |

Two seats, **two different instruments**, same conclusion — so this is corroboration, not repetition.
>> **CONSEQUENCE, STATED PLAINLY: tomorrow's ~13:30Z scheduled fire runs the 01:12:11Z package and
   AC1 STILL WILL NOT LIFT.** Waiting for the next fire is not a plan; advancing the pin is. That
   advance MOVES SERVED OUTPUT for four firm scopes and is gated on NEVER#1 never-widen sign-off —
   the ship-lift card presently with Andrew. **Nothing at this seat or the DS lane can discharge it.**

---

## 2. `TM1-AC2` — SUM INVARIANT. **CERTIFIED, PLANE NAMED.**

Both planes hold at 4 of 4 scopes, printed: L2→L1 per bucket, L1→L0 Models
(1,472,323,341.05 / 186,785,080.61 / 144,816,065.54 / 1,803,924,487.20), and view-plane
`sum(peers) == total_aua − Insurance` (…/2,094,351,300.67). 16 assertions, 16 hold.

⭐ **THE INSTANCE MARKS ITS OWN PLANE RATHER THAN LETTING "PASS" IMPLY THE SERVED ONE:** recomputed
from the block emitted by the committed producer over real cached gold inputs — **EXERCISED, not
SERVED**. That distinction is the one this whole TO turns on and the executor made it unprompted.
⭐ **AND THE ASSERTION IS NOT VACUOUS** — the L1 figure and the L2 sum are read by **different paths**
(L1 indexes `by_model` on the registry member_id; L2 resolves through `resolve_any()`) and were
deliberately not collapsed. An equality whose two sides are the same expression cannot fail; this one
can. I did **not** re-run the arithmetic: re-deriving a peer's figures re-runs their reasoning and is
not independent verification.

---

## 3. ⛔ `TM1-AC4` — NO VALUE IS INFERRED. **CERTIFIED ON THE CLAIM. FINDING ON THE CITATIONS.**

### The claim is TRUE — verified at source, at the vintage, on my own read
AC4 forbids any portal-derived or apportioned figure. I tested the sharpest form of it: **is there any
apportionment anywhere in the emit path?** Census over `mdpf_gold_consolidator.py` @`a5227cf161` for
`apportion|weight|ratio|/ total|pro_rata|split`: **zero apportionment operations.** The only `split`
hits are `client_l1_split` (a *declared* rule, not an apportionment) and `Key.split("/")` string ops.

The mechanism is exactly as claimed, read at `a5227cf161`:
```
:597   value = _last((entry or {}).get("model_value"))        <- a KEPT value
:599   member = registry.resolve_any(key)                     <- identity, not display_name
:609-610  models_member_aum[member.member_id] = models_member_aum.get(...) + value   <- accumulate
:720   member_aum=models_member_aum                           <- passed, not computed
registry :909  def _members(view_path)
registry :930-931  "aum": (None if member_aum is None or m.member_id not in member_aum
                           else float(member_aum[m.member_id]))
```
`:930-931` is a **direct dict lookup with a None guard**. It neither computes nor apportions. **AC4 holds.**

### ⛔ THE FINDING: the citations resolve to nothing, at any ref
The instance cites `:585`, `:588`, `:600-601`, `:698` and registry `:918-923`. **Those line numbers are
wrong at the vintage the instance names, and at every other ref:**

| expression | AC4 cites | `a5227cf161` | `70a0828226` | `HEAD` | working tree |
|---|---|---|---|---|---|
| `model_value` | **585** | 597 | 630 | 630 | 630 |
| `resolve_any(key)` | **588** | 599 | 632 | 632 | 632 |

**585/588 matches NO commit and not the working tree.** The offsets are not even constant (12 and 11),
so it is not a clean shift. These numbers point at a file state that **exists in no ref** — a transient
mid-edit tree, read for the line and then stamped with a vintage taken from the commit.

>> **WHY THIS MATTERS MORE THAN A TYPO: THE CITATION LOOKS RESOLVABLE AND IS NOT.** CLAUDE.md's rule
   is *"cite `file:line @ <commit-ish>` — a citation without a vintage is not a citation."* This one
   HAS its vintage, which is exactly what makes it worse: a reader following it lands on a comment
   (`:585`) and an `except` block (`:600-601`), finds nothing supporting the claim, and can only
   conclude AC4 is unsupported. **The strongest criterion in this instance is the one a checker would
   read as hollow.** Mechanism, named for banking: **a citation whose LINE comes from one plane and
   whose VINTAGE comes from another is unverifiable by construction.**
⭐ **NOT A FAIL, AND NOT THE EXECUTOR'S SUBSTANCE.** The work is right; the pointer to it is broken.
   Remedy is a re-stamp of five line numbers against `a5227cf161`, not a re-build.

---

## 4. `TM1-AC3` / `TM1-AC5` — DISCLOSURE AND COUNTS. **CERTIFIED.**

**AC3.** No row invented, no absence padded. `opal_global_all_equity_total_return` resolves in no
scope's `by_model` and is emitted `aum: null` at all four — **present as a registered row, disclosed as
carrying no measurement, never as 0.0.** That is the TO's own trap honoured (*"a value of 0 asserted for
an unmapped node is a false frame on a money figure"*).

⭐ **TWO CORRECTIONS TO THE CRITERION'S OWN PREMISE, BOTH AGAINST THE EXECUTOR'S INTEREST.** The TO
asserts *"Registry Custom = 3 members"* and that Andrew's example *"Opal Fixed Income"* was 0 hits.
The executor reports Custom is **4**, and that `opal_fixed_income` **now resolves** (cottonwood and
global, 8,425,603.56). Both corrections make the denominator larger and the disclosure obligation
heavier. **An executor who wanted an easy PASS says neither.**

**AC5.** Count with denominator, per scope: 49financial 5/9, cottonwood 6/9, inflection 7/9, global 8/9
— 26 of 36 cells measured, every unmapped member enumerated by `member_id`, and the reason stated (the
firm has no accounts in that model at this vintage). ⭐ **Emitted by the producer itself on every run**
(`:672-681`), not only in this report — so the denominator survives the report, which is the difference
between a number and an instrument.

---

## 5. ⛔ WHAT I DID **NOT** CONFIRM — stated rather than implied

**I did not independently confirm the 9-member / 4-Custom denominator that AC3 and AC5 rest on.**
I tried. `data/mdpf/scripts/gold/mdpf_model_registry.json` @`a5227cf161` carries **9 model rows**, which
is consistent with the instance's 9 — but its rows are keyed `model_key` / `model_type` / `display_name`
(Ultra-Short Term, Short Term, Intermediate Term, Long Term, Ultra-Long Term, Opal Equity Growth SMA,
Dividend SMA, 50/50 INT/LTC, 50/50 ST/INT) and carry **no `member_id` and no Primary/Custom qualifier**.
That id vocabulary is **not** the `opal_*` vocabulary the instance enumerates, so the Primary/Custom
split is produced elsewhere (`_members()` classifies via a `primary` boolean at registry `:282-285`).

A clean zero on my first pass was **positive-controlled** (`member_aum` → 5 hits in the same file), so
that zero was a true absence rather than a broken matcher.

>> **CONSEQUENCE FOR THE READER: AC3 and AC5 are certified ON THE EXECUTOR'S MEASUREMENT, CITED.** Their
   counts are internally consistent and their disclosure discipline is exemplary, but the *denominator
   itself* is not corroborated by me. **A possible two-registry situation is flagged for whoever next
   needs that denominator** — start from `_members()` and the `primary` boolean, not from
   `mdpf_model_registry.json`. I stopped because no further check changes this certificate: AC1 already
   holds the TO open.

---

## SCOPE — what this certificate does NOT say

- It does **not** close `D1_CATVIEWS.TO-M1-DS`. AC1 is outstanding.
- It does **not** assert anything is SERVED. Every certified row is EXERCISED-plane or source-plane.
- It does **not** authorise `TO-S1-DE`, which is blocked on this TO by its own face.
- It does **not** bear on the ship-lift decision. That is a NEVER#1 never-widen call at Andrew, and a
  certificate is not a sign-off.
- ⚠ **Related but NOT part of this TO:** the served `global` scope understates `Client` by
  **$359,773,356.74** (measured this session on the served plane; the portal does pass `'global'` and
  the edge serves it 200). **The pin advance does NOT fix that** — it is a separate, unfixed producer
  defect. Recorded here so no reader treats a lifted AC1 as clearing it.

— `3.0.0_SA_CVO~Z`
