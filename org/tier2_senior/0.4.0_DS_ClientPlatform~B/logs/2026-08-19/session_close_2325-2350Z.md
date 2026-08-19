# Session close -- quiesce work, a retraction that travelled, and a self-inflicted truncation (2325-2350Z)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

**Serial:** `0.4.0_DS_ClientPlatform~B` | **Window:** 2325Z -> 2350Z
**Commits:** `8e015ba765`, `1900910a52` (the bad one), `e313e096ef`, `96bf88a153`, `20d29e3932`. Unpushed.

---

## Summary

Worked through COO's 23:32Z broker quiesce (sends held, S3/commits explicitly unaffected). Three
things happened and two of them were my own errors.

## 1. I retracted my own headline figure an hour after publishing it

I labelled `L1-L2` as "MEMBERSHIP" and told COO it was **90.8% of the gap**. Wrong: L1 is
accrual+cash-inclusive (CRO~A's finding) and L2 is positions-grain (**my own finding, from earlier
the same session**), so `L1-L2` fuses the missing-member term with the measure term. **I had both
halves in hand and built a decomposition that crossed them.**

Sound figures: total `L1-L3` = **$2,086,553,267.96**; on the 24 exact-tie groups the roster agrees so
`L1-L2` there is **pure basis, -$1,964,099.38**. **No per-group membership/basis split is producible
from group-grain qt6** -- that needs per-account data I do not hold.

**What survives:** the 24 cent-exact ties, and the newly *tested* result that our own coverage is not
the driver (+29.70% fully-covered vs +29.08% partially -- indistinguishable). Direction intact, split
withdrawn.

## 2. The retraction had already travelled -- and that is the transferable bit

I withdrew it in the record at ~2335Z **during the quiesce**, so it could not be sent. CRO~A's next
message adopted the withdrawn figure verbatim as "the headline mechanism". **A correction committed
to the record but not yet on the wire does not stop propagation.** Corrected to both seats on release;
CRO~A then verified containment by grepping their own sent files (the figure reached exactly one
recipient -- its author -- and never entered COO's record through them). My own 2323Z send to COO was
retracted directly.

## 3. I truncated the T1 deliverable to zero bytes and committed it

`1900910a52`: 463 deletions, 0 insertions. **Mechanism:** python evaluates `open(path,"w")` --
which **truncates on open** -- *before* the argument expression it is handed, so an expression that
then raises still leaves an emptied file. The exception looked like "nothing happened"; the
truncation had already committed. A second script's guard assert correctly failed and **still could
not save the file, because the damage was upstream of the guard.**

Caught within one command by **reading the commit stat instead of trusting rc=0**. Restored from git,
verified **byte-identical by sha256** with a negative control; nothing reconstructed from memory.
Subsequent edits used a non-truncating tool and write-to-temp-then-`os.replace`.

> **The lesson: when a script "fails", check the FILE, not just the exception. An exception tells you
> the program stopped; it does not tell you what it had already done.**

## 4. The join CRO~A handed me -- NEGATIVE

Their 24 unexplained identity outliers vs my 49 widest-gap groups: **overlap 9, expected 5.9 by
chance**, mixed-sign residuals. No meaningful excess -- **the two anomaly sets are independent.**
Their residual is market appreciation (it re-prices monthly: Jun -0.099%, Jul +0.064%, Aug +1.469%).
**Removes a candidate rather than confirming one.** I did not force a story out of 9-vs-5.9.

Also recorded from them, because I commissioned the read that would have produced the false findings:
`residual = EMV - (BMV + NetFlows - Fees)` is **implied market appreciation** -- the identity does not
close by construction, so **a near-zero residual would be the anomaly**. Read as an error term it
would have manufactured 215 false findings in one pass.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `git show <commit>:<path>` | recover the truncated deliverable | PASS -- byte-identical sha256, positive + negative control both run |
| `.tools/proof-of-spec-check.py` | T1 instance after each correction | PASS -- VALID rc=0 throughout |
| `.tools/safe-commit.sh` | 5 commits incl. the restoration | PASS -- risk-reflex clean each time |
| ad-hoc join (`pandas`/`json`) | my wide set vs CRO~A per-group residual | PASS -- negative result, chance baseline computed rather than eyeballed |

**What worked:** computing the chance baseline (5.9) before interpreting the overlap (9) -- without it,
"9 groups overlap" reads as a finding. **What failed:** my own `open(...,"w")` truncation, above.
**Gap found:** none new tool-side.

## Blockers

**None.** Only dim 436 remains, at Andrew via COO -- a template write is not a bigger read, so the
scanning grant does not cover it. Nothing I built depends on it arriving.

## Current State

- T1-ORACLE: all three legs MEASURED, 200/201 groups. T2-DIMS: minted, verified, accepted 4/5 with
  T2-3 correctly FAIL. Both proofs VALID rc=0.
- T1 deliverable at 522 lines, four addenda, every superseded figure marked **at the point of use**.
- `platinum/advi/49financial/` = 0 keys. Serving untouched.

## Next Steps

1. [`2.0.0_SA_COO`] dim 436 at Andrew; the AE publisher invocation contract still unanswered.
2. [`0.4.0_DS_ClientPlatform~B`] On dim 436 landing: re-run, `is_primary` populates, T2-3 closes.
3. [`0.4.0_DS_ClientPlatform~B`] Nothing owed. Event-driven.
