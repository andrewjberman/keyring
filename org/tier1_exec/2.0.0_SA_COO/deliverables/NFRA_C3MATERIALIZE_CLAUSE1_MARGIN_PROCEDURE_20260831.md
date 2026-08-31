# NFRA_C3MATERIALIZE — Addendum 1i clause 1: the DERIVED MARGIN PROCEDURE

**Issuer:** `2.0.0_SA_COO~X` · **declared 2026-08-31T00:0xZ** · governed by **Addendum 1u `@a3f6f2fb22`**
(margin DERIVED not chosen; residual choice is the multiplier, declared from a general principle and
committed **before the candidate's implementation runs**) and **Addendum 1i** (the two-clause entry oracle,
both clauses on ONE frozen implementation, population, pair predicate and `(K, T)`).

⛔ **NO CANDIDATE EXISTS AND NONE HAS BEEN MEASURED.** No firm-carrying second view has been built, run or
inspected. This document is committed **before** any implementation of the candidate arm, which is the
evidence 1u names: *the pin is the evidence.*

---

## 1. What is being declared, and what is deliberately not

**DECLARED HERE:** the procedure that computes clause 1's margin, and the multiplier principle it uses.
**NOT DECLARED HERE, because it is not a free parameter:** any scalar margin. There is no number in this
document that a later result could have suggested — by construction, which is the whole point of 1u (i).

**NOT TOUCHED:** 1i's two clauses. **CONTRIBUTION** (fused AUC beats a predeclared permutation null by the
margin) and **ADEQUACY** (fused AUC at least the better of the two inputs alone) stand exactly as ruled and
are uncontested. Adequacy needs no margin and gets none here.

## 2. The null battery

Per 1i clause 1 and the disqualifying grounds recorded on the retired arm's Rule-28 card
(`4e7016f471`, verdict **UNSOUND AS A GATE**):

- **Permutation null on the FIRM LABELS**, holding the fusion method, population, pair predicate and
  `(K, T)` fixed — the same frozen configuration clause 2 is evaluated on.
- **`N >= 20` draws.** A single draw is one of that card's three disqualifying grounds and is not a null.
- **Per-draw declared seed, independent streams.** A shared RNG stream makes draws order-dependent — the
  card's second ground. Seeds are recorded per draw, so the battery is re-runnable to the same values.
- **Immutable, retrievable input** — the card's third ground. The input artifact is pinned by content, not
  by path.
- **Its own failure signal** (§5).

Let `A_fused` be the candidate's fused AUC on the frozen configuration, and let the battery yield draws
`x_1 … x_N` with mean `m_null` and **sample** standard deviation `s_null` (Bessel-corrected, `N-1`).

## 3. THE PROCEDURE — the margin is a function of the null's own dispersion

```
margin  =  k(N) * s_null
CLAUSE 1 PASSES  iff  A_fused - m_null  >  margin
```

Evaluated **per run**, from that run's own battery. Nothing is carried between runs and no value is stored.

## 4. THE MULTIPLIER, and why it is a principle rather than a pick

```
k(N)  =  t(0.95, df = N - 1)        one-sided
```

**JUSTIFICATION, stated from a general principle and not from any measurement of this system:**

1. **One-sided**, because clause 1 is a directional claim: a second view must *add* discrimination. A
   two-sided bar would credit a view that made fusion reliably *worse*.
2. **95%**, the conventional single-comparison false-positive rate. Clause 1 is **one** pre-registered
   comparison on **one** frozen configuration, so no multiplicity correction is owed. Had the design
   admitted a family of candidate views scored together, this principle would require one — and that is a
   change to the *design*, not a licence to retune `k` afterwards.
3. **Student's `t`, not the normal quantile, and this is the part that is easy to get wrong.** `s_null` is
   **estimated from the battery**, not known. Using the normal `1.645` treats an estimated dispersion as if
   it were the true one, which **understates the bar precisely when `N` is smallest** — exactly the regime
   1i's `N >= 20` floor permits. `t(0.95, 19) ≈ 1.729`; the two converge as `N` grows, so this choice is
   conservative where it matters and costless where it does not.
4. **`k` is a function of `N`, not a constant.** A larger battery earns a slightly smaller multiplier
   because it estimates dispersion better. **This makes the bar harder to fit than a scalar would be:** it
   must hold for every `N >= 20`, and no single run's outcome can be improved by choosing it.

**IMPLEMENTATION NOTE, so the value is auditable rather than asserted:** the arm must state where its
`t` quantile comes from (library and version, or a committed table) and record the `k` it used beside the
`N` it used. A `k` that does not match `t(0.95, N-1)` from the stated source is a **defect**, not a
variant.

## 5. Failure signal — distinguishable from a genuine negative

The Rule-28 card requires an instrument to fail *loudly* rather than quietly return a verdict.

- `s_null` **zero, non-finite, or undefined** (`N < 2`) — **REFUSE.** A degenerate null makes the margin
  `0` or `NaN`, and a comparison against it would PASS or ERROR while looking like a measurement.
- Fewer than `N = 20` completed draws — **REFUSE**, and report the count. A partial battery is not a
  smaller battery.
- Any draw failing to reproduce from its recorded seed — **REFUSE.** The battery's re-runnability is what
  makes it evidence rather than an anecdote.

**These refuse; they never return a PASS or a FAIL.** An instrument that cannot distinguish its own
breakage from a real negative is the class the retired arm died of.

## 6. The negative anchor

Per 1u (iii), the known **firm-blind** partner (view 1 fused with a permuted view 2) is a **CONTROL, not a
fit**: a candidate that cannot beat a firm-blind partner has not demonstrated firm-carrying behaviour. It
enters as a control arm, and **no threshold is derived from its historical values.**

## 7. Falsifiers, carried from 1u so this is arguable later

This declaration is **VIOLATED** if either occurs:

1. **A margin appears as a literal** in the arm, with no procedure behind it.
2. **The multiplier's principle is revised after a candidate has been measured** — including a switch from
   `t` to normal, from one-sided to two-sided, or from 95% to another rate, once any candidate output
   exists.

**A revision BEFORE any candidate runs is legitimate** and must land as an amendment to this record with
its own justification, at a pin, before the implementation.

---

**PLACEMENT MEASURED:** origin/CLOUD `61d975d1d5` (own `ls-remote` read 23:59:05Z). This record is LOCAL at
declaration and rides the next window; **its pin, not its content, is the pre-registration evidence.**
