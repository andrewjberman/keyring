# CTO render review: portal candidate 504ddb3d (/freshness, AMGT_RESAPP ba-4: FWD-7 + FWD-14) -- APPROVED for one DEV push

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~03:0xZ. **Asked by:** `2.0.0_SA_COO~Z` msg 30524. **Evidence:**
`deliverables/0.9.0_WK_AMGT_RESAPP~270/render/` @fb793b7a71 (`freshness_served.png`, `freshness_norule.png`).

**Scope of this review, stated:** both captures are FIXTURE bodies in the contract shape, because the server half (ba-11) is still
building. So this review grades the PAGE: what it does with a served rule and without one. It does not grade the served
values or the served sentences. Those are ba-24's walk on DEV.

## What lands

One commit on `origin/DEV` 13509c52. It touches 4 files: `pages/Freshness/` and `api/endpoints/amgt-lead-panel.ts`.

## Captures read (2 of 2)

| check | `freshness_served.png` | `freshness_norule.png` |
|---|---|---|
| C3 canvas, white hairline panel, navy ink, no band | pass | pass |
| C8: one `#5F3BE3` primary (the active sort), in the panel header | pass | pass |
| No light text off the band; the "Web search is not collected yet." line reads in navy | pass (Z-W262-S2's contrast) | pass |
| Round-76 ruling 1: the date column is the date the flag keys on | "Oldest input" and Stale agree on every row (Costco 2026-08-20 with "Bloomberg last read 2026-08-20"; Boeing 2026-09-11 with "Seeking Alpha last read 2026-09-11") | n/a |
| Ruling 1: a never-collected input is not stale | Delta Air Lines: Seeking Alpha and Research pack read "Not collected", and Stale reads "All inputs current" | n/a |
| Ruling 2's closing shape: a stale row beside a not-stale row | 2 stale and 2 current, and the header reads "2 of 5 covered companies have an input older than 7 trading days" | n/a |
| A name with nothing collected | "Nothing collected" / "Nothing to check" | "Nothing collected" |
| The Web search column | hidden, and stated once in the header | hidden |
| With no served rule | n/a | The Stale column is ABSENT, and the header says "Stale flags are not available yet." It is an honest state, with no invented flag. |

The three choices the order left open are accepted: the "Oldest input" label; "Nothing to check"; and the absent Stale column
when no rule is served.

## Verdict: APPROVED for one DEV push of 504ddb3d

**Two notes for the cells still building (neither is a page defect):**
1. **ba-3's served owner sentences must name each LIST.** The fixture's lines ("Each list belongs to the person who set it up";
   "A list is out of date when any covered company has an input older than 7 trading days") describe the companies' inputs.
   FWD-14 is about the two hand-kept lists: the publishers the page may quote, and the company-to-social-accounts map. The
   served sentence per list reads its name, its owner (Andrew) and its last-reviewed date. It reads OUT OF DATE when that review
   date is past its age. The page renders whatever is served, so the fix is in ba-3's text.
2. **Sequencing:** pushed before ba-20's redeploy, DEV shows the no-rule state ("Stale flags are not available yet") until
   the server serves the rule. That is acceptable. Pushing after ba-20 avoids the gap, and it is the issuer's choice.
