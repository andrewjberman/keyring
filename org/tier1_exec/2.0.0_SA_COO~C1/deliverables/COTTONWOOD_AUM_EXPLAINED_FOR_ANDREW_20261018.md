# Cottonwood: what is in and out of 555m, 563m, 530m and the MDPF 530m

From 2.0.0_SA_COO~C1, 2026-10-18. Plain English, numbers exact. Value date 2026-10-15 unless stated.

## The answer to your question

**Yes. Insurance is inside the 530m, as supervised.** The 96 annuity and insurance carrier-feed accounts total $8,860,829.31 on 10/15. BD's own flag on each is `Supervised`, so they sit in the supervised number, not outside it. Take them out and supervised would be $521,561,158.83.

Nothing about insurance is unsupervised. The unsupervised money ($33.1M) is other accounts.

## The four numbers, side by side

| Figure | All accounts | Supervised | Unsupervised |
|---|---:|---:|---:|
| BD dashboard, 10/15 | 563,559,898 | **530,421,988** | 33,137,910 |
| What Opal displayed before the fixes ("555m"), 10/15 | 554,632,228.45 | 521,561,158.83 | 33,071,069.62 |
| MDPF now, 10/15 | not shown (supervised only by design) | **530,421,988.14** | excluded |
| MDPF now, 10/16 | not shown | **524,463,230.11** | excluded |

ADVI (the Advisor Intelligence page) now reads the same as MDPF on both dates, and the CVO graded that on the served figures.

## What explains each gap

1. **555m (554.63m) versus 563m (563.56m), a gap of $8,927,669.55.**
   - $8,860,829.17 of it is the 96 insurance and annuity carrier-feed accounts. Opal's morning pull carried them at $0, because BD posts their values after our 07:30 ET pull. The cause is timing. No account was missing.
   - The other $66,840.38 sits on the unsupervised side (BD dashboard 33,137,910 against Opal's 33,071,069.62). The CRO findings do not explain that residual, and I have not either.
2. **563m versus 530m, a gap of $33,137,910.** These are the accounts BD flags Unsupervised (held-away and position-only). They are not insurance: the 96 carrier-feed accounts all appear in BD's Supervised export, and none of Opal's unsupervised accounts appear in it.
3. **"555m" was the whole book.** It added supervised and unsupervised together, with the insurance accounts at $0. That is why it was neither BD's 563m nor BD's 530m.
4. **What we serve now.**
   - Cottonwood in MDPF and in ADVI counts only accounts BD flags Supervised (FWD-10, on your word "We want that 530.42m number").
   - The insurance values are re-pulled after BD posts them, so the 96 are counted at their real values.
   - On 10/15 that reads 530,421,988.14, which equals BD's own supervised export total (530,421,988.14) to the cent.
   - ADVI read 530,370,482.38 on 10/17 until 10/18, when a fix to one bond holding that two lots shared a name (a "Van Alstyne" holding, about $51.2K to $51.5K a day) brought it to 530,421,988.14.

## Why 10/16 reads 524,463,230.11

It is $5,958,758.03 below 10/15. What I have read: 8 accounts that held $1.996M on 10/15 are still blank in BD's 10/16 file, because BD has not posted them yet. I have not decomposed the remaining ~$3.96M, so I do not call it market movement. Treat 10/16 as provisional until BD posts those 8 accounts.

## The ruling behind it

On 2026-08-24 you excluded insurance from MDPF ("we don't take fees on it"). Your 2026-10-17 word, "we want that 530.42m number", is later and more specific, and the CTO applied it to Cottonwood only: the 96 count. 78 of the 96 do carry a BD management fee ($5,300.70 year to date in total). 49 Financial and Inflection insurance treatment is unchanged. If you reverse it, Cottonwood reads $521,561,158.83 with "excluding $8.86M insurance" stated on the page.

## Insurance accounts, by carrier-feed prefix (10/15)

| Prefix | Accounts | Ending market value |
|---|---:|---:|
| DTCCR_ | 78 | 4,890,211.59 |
| ASLAA_ | 13 | 2,527,925.27 |
| AEGON_ | 3 | 1,060,666.07 |
| LNANN_ | 1 | 226,189.95 |
| EQUIT_ | 1 | 155,836.44 |
| **Total** | **96** | **8,860,829.31** |

They sit in 47 relationships across all three advisor books.

## Sources

- `org/tier1_exec/4.0.0_SA_CRO~DDD/deliverables/COTTONWOOD_SUPERVISED_GAP_FINDINGS_20261017.md` (table at lines 21-24, Addendum 1 at lines 72-106, Addendum 2 at lines 108-131).
- `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md`, change log v2.24, v2.25, v2.26 and v2.30.
- CVO grade `ADJUDICATION_v22` @9b46853f3e.
- CRO~DDD run-time messages of 10/17 and 10/18 (8 accounts blank in BD's 10/16 file; the 10/17 ADVI figure).

I did not re-pull BD. Every figure above is read from those sources; the only arithmetic is the gaps, checked as differences.
