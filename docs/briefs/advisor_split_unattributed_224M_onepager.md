# 49F advisor-split data quality: $224.2M unattributed — what's behind the number

**For:** Andrew · **From:** DS (0.4.0~B) · **Date:** 2026-06-29 · **Source:** `canonical/schwab/gold/advisor_split_reconciliation` (date=2026-06-24, tracked each run)

**Headline:** under BD's raw advisor splits (no normalization, per your ruling), **$224.2M = 14.1% of the $1.591B Schwab book is not credited to any advisor** — i.e. BD's per-account role splits don't add up to 100%, so that share of AUA falls through.

## 1. It's almost entirely UNDER-credit (not a netting trick)
- **Under-credited (splits sum < 100%): 5,846 accounts → $224.24M.**
- Over-credited (> 100%): **1 account → −$5K** (negligible).
- Exact (= 100%): 47 accounts.
- So net ≈ gross ($224.2M either way). This is real under-attribution across nearly every account, **not** a big over/under that cancels out.

## 2. Two root causes, roughly half each
- **BD records NO splits at all** (sum = 0%): **660 accounts → $116.7M (52% of the gap).** BD simply never tagged any advisor split on these.
- **BD records INCOMPLETE splits** (0 < sum < 100%): **5,186 accounts → $107.5M (48%).** Mostly the "85% / 90% pattern" — the named roles' splits add to 85 or 90, leaving ~10–15% uncredited (a missing role's split, often local-ops/house).

## 3. Concentration: a few big accounts + a broad systemic tail
- Top 20 accounts = **21%** of the gap ($46.6M); top 50 = 34%; **top 100 = 46%.** The other **54% is spread across the remaining ~5,750 accounts.**
- So it's **both**: ~$100M sits in a few hundred large records (fixable account-by-account if desired), and ~$120M is systemic BD-split sparseness across the long tail.

## 4. Whose accounts (where the gap lives)
- **~55% ($122.7M) is in accounts with NO real architect** — "Unassigned" ($74.9M / 433 accts) + "No Architect Value Assigned" ($47.8M / 2,229 accts). Largely house/untagged accounts BD never attributed.
- The remainder is in real advisor books with the 85%-pattern — e.g. Travis Penfield $42.4M (196 accts; his large accounts like the $33.8M WILLIAM CHAN account sit at 85% → $5.1M uncredited each).

**Top single accounts:** H&S Shank ($6.6M, 0% — no splits) · William Chan ($33.8M @ 85% → $5.1M) · Jessica Abeln Lindsey ($21.9M @ 85% → $3.3M) · Patterson ($3.1M, 0%).

## 5. So what
- This is **BD's data quality, surfaced — not ours to silently fix** (your ruling: raw as-is). The leaderboard credits exactly what BD's splits say; this table quantifies the shortfall.
- It is **tracked every run** (`advisor_split_reconciliation_firm` time-series). If $224.2M / 14.1% **grows**, that's a BD-split-degradation signal worth a flag; if 49F ever wants the gap closed, the curated-override mechanism is built and dormant (just add corrected splits — no code change).
- Decision-useful read: roughly half the gap is "BD never tagged it" (the no-architect/no-split accounts) and half is "BD tagged it incompletely" (the 85% pattern) — two different fixes if 49F wants them.
