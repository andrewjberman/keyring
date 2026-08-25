# ANDREW-DIRECT 2026-08-25 ~00:5xZ — the CLIENT L1 composition ruleset, PER FIRM

**Terminal:** `0.4.0_DS_ClientPlatform~F` (D1_CATVIEWS round-1 DS lane).
**Trigger:** this lane asked (call 2) for the per-Partner composition rulesets he offered on 08-24.
**Status:** RECORDED VERBATIM + BROADCAST SAME TURN. This is the D1-h-c1/c2/c3 answer.

## VERBATIM

> I'll break down the logic here for what this looks like by firm. "Client" for 49 Financial is ALL
> non-Model/non-SMA assets, specifically it is ALL "Client - Supervised". For Inflection, "Client" is
> all non-Model assets (Inflection does not have SMAs); these Client Assets are all "Client -
> Unsupervised", because we do not look over the non-model Assets. For Cottonwood it is a little more
> complex. Client is all non-Model assets (where there are Primary and Custom Models at play). Of
> that Client Group, the Client - Supervised portion is the remainder of any account containing Opal
> Models, essentially the Non-Model residual of any accounts that have Opal Model Exposure. Client -
> Unsupervised is anything else.

## THE RULESET, RESTATED AS THREE COMPUTATIONS

| firm | Client = | Supervised | Unsupervised | grain needed |
|---|---|---|---|---|
| **49financial** | total − Models − SMA | **ALL of Client** | **0** | firm-level; already have it |
| **inflection** | total − Models (no SMAs) | **0** | **ALL of Client** | firm-level; already have it |
| **cottonwood** | total − Models (Primary + Custom) | non-model residual of accounts **holding Opal Models** | everything else | **ACCOUNT-GRAIN** |

## WHAT IT BINDS, AND WHAT IT MOOTS

### 1. THE CLIENT L1 IS NOW COMPUTABLE ON ALL THREE FIRMS. `predicate: "unavailable"` IS MOOT.
The emitted block currently carries `predicate: "unavailable"` on all three firms. Two of the three
are now pure arithmetic on figures already in hand, and the third is a defined account-grain
computation rather than a missing source. **The unavailable marker survives only as the shape for a
firm that later has neither.**

### 2. IT SUPERSEDES THE FLAG I MEASURED — HIS RULE IS DERIVED, NOT LOOKED-UP.
This lane measured two per-firm fee flags and neither is this rule:
- **cot** `account_supervised ∈ {Supervised, Unsupervised, unflagged}` (`D_05.supervised_split.py`)
  — a STORED FLAG. His rule derives Supervised from **Opal Model exposure per account**, which is a
  different definition and has **no third state**.
- **inf** `is_fee_earning` (789 / 122 accounts, $197.4M / $12.5M) — TRUE, LIVE, and **not this
  predicate**: it partitions *every* account including model-held ones, whereas his rule concerns
  only the **non-model portion**. His answer for inflection is a flat "all Unsupervised, because we
  do not look over the non-model Assets."

⛔ **Q-h3 (the third `unflagged` bucket) IS PROBABLY MOOT** — his rule is deterministic (an account
either holds Opal Models or it does not), so no account is unclassifiable. **Not concluded here:**
whether his rule SUPERSEDES `D_05`'s stored flag for the MDPF view, or whether the flag is meant to
implement it, is a question routed with this record — the two disagree and only he or CTO settles
which is authoritative.

### 3. IT CORROBORATES HIS 00:4xZ SMA WORD FROM A SECOND DIRECTION.
"Inflection does not have SMAs", stated in passing here, independently matches the measurement that
inf carries no `cohort_class='sma'` entry and his earlier "only 49 has SMAs".

### 4. 49F's "PENDING D3 JOIN" IS MOOT.
The TO contemplated 49F's split being blocked behind D3's SmartX↔BD account join. His rule needs no
join: 49F is **100% Supervised** at firm level.

## WHAT THIS LANE STILL NEEDS (routed, not assumed)
**COTTONWOOD ONLY:** the account-grain read — per account, does it hold any Opal Model (Primary or
Custom), and what is its non-model residual. That is cot BD data this lane can measure. Everything
else in the ruleset is arithmetic on figures already emitted.

**Author:** `0.4.0_DS_ClientPlatform~F`. **Project:** D1_CATVIEWS, cells D1-h-c1 / c2 / c3, D1-b-1.
