# ANDREW-DIRECT -- a CRO looks into Black Diamond's "Portfolio Group" key and the Cottonwood Advisor Intelligence page (recorded by 2.0.0_SA_COO~C1, 2026-10-17 ~01:45Z)

**Channel:** Andrew, in the `2.0.0_SA_COO~C1` terminal session (dell1), after the seat's round-106 wait explanation.

**Verbatim:**

> Something else we need to look into with Black Diamond/Cottonwood is how they structure their "Portfolio Group" key, because that's how we'll be able to run everybody's book properly. I want to have a CRO agent look into this, give me a brief handoff on the subject, naming how as a result we have very wonky stuff going on with their Advisor Intelligence page, which needs to not be doing whatever it's doing right now and should be taking on the Inflection Shape visually. Namely how we are just listing all the accounts in a list on the first tab and it's generally all a mess.

**Scope (verbatim, not widened):** a CRO agent researches the key and hands Andrew a brief. This record orders no portal change and no change to any served table; the page work follows the normal route after his read. The routing to `4.0.0_SA_CRO~DELL1` is the COO's act on his word.

## Grounding for the CRO (all read from files this session; none re-measured live)

**What the repo already says about `portfolio_group` (ADVI_COTBKF):**
- The Cottonwood silver table `account_attributes` carries four columns: `account_supervised`, `account_billable`, `position_only`, `portfolio_group` (`deliverables/2.0.0_SA_COO~C1/dc1_fire_read.py` line 32). Its writer is `A_00`; the manual reader is `D_05`.
- 122 accounts are multi-book (two or more rows in the newest partition). For them `portfolio_group` is taken from the FIRST row in vendor file order, so the value is decided by file order, not by a rule, and can flip when the vendor reorders the file (`ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_CTO_HALF.md` condition C-1, lines 22-27).
- Round 105 measured 130 portfolio-group changes (171 in any column) from merging the table (`decompositions/ADVI_COTBKF_DECOMP.round106.md` line 7).
- No portal or gateway code reads `portfolio_group` (same CTO half, line 13, measured 2026-10-16); no file under `portal/src/pages/AdvisorIntelligence` mentions it.
- Silver `account_attributes` stopped at 2026-08-20; round 106 applied the one-line fix and the first scheduled silver fire is about 2026-10-17 13:00Z. The close read counts how many of the 122 change between two builds.

**The Cottonwood page today (`portal/src/pages/AdvisorIntelligence/_partners/cottonwood/index.tsx`):**
- Two tabs: Distribution, and Books (admin-only). One synthetic advisor, "Cottonwood Capital Advisors" (DS `A_01`), so the advisor level carries no information.
- The first tab (Distribution) stacks `DistributionTab`, then `CottonwoodClientsSection`, the firm-level clients roster ("ADVI_COTMVP B, Andrew-direct"). That roster is the long account list Andrew describes.
- The Inflection page it should look like has the tabs Advisors | Distribution | Books | Profile (`_partners/inflection/index.tsx` lines 26 and 149-159).

## What the CRO is asked to answer (one brief to Andrew)

1. What is Black Diamond's Portfolio Group: its place in the Black Diamond hierarchy (account, household, relationship, book, advisor), whether it is one-to-one or one-to-many with an account, and what a multi-book account means.
2. Which of Cottonwood's data holds the key today, how complete and how stable it is, and what must be true for it to serve as the unit of "everybody's book".
3. How the missing or unstable key produces the Cottonwood page's current shape (a flat account list, one synthetic advisor), and what the Inflection shape needs from the key to be reproduced.

Unknown to the COO and not asserted here: what Black Diamond means by the term. The brief is the CRO's (`4.0.0_SA_CRO`, L1); the COO does not write it.

Related, for collision only: `4.0.0_SA_CRO~DDD` is on the Cottonwood gap diff (MDPF_CANON FWD-10).

-- 2.0.0_SA_COO~C1
