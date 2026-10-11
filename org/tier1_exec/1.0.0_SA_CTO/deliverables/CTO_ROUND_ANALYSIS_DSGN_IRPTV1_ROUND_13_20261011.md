# CTO ROUND-13 ANALYSIS -- DSGN_IRPTV1 -- answering the rounds 11-12 L10 slug (2026-10-11 ~07:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v7.md`
@ea5246b8fc (3.0.0_SA_CVO msg 4337). **Prior analysis:** `CTO_ROUND_ANALYSIS_DSGN_IRPTV1_FROM_WATERMARK_20261002_20261011.md`
@10d7d46e49. **No PRD addendum.**

## 1. Where the project stands

Rounds 11 and 12 ran tonight on a lane seated four hours ago. Landed on portal DEV: the S60 press test (6f70e36b) and the S61
Holding-cell wording (1cd1cf25, client-facing; its PROD push is Andrew's word). The state table reads 14 of 23 outcomes
EXERCISED, 9 APPLIED, 0 DESIRED; it is the issuer's table, not a grade. **FWD-1, the thread, has no whole signed-in trace.**

## 2. The slug's three items, ruled

**1. An API-runner trace does not meet FWD-1. Accepted, and the cell is DROPPED.** This seat ordered a signed-in trace under a
read-only pair (msg 4198), then ruled four questions on its draft (msg 4338). The reviewer's answer is right: FWD-1 is a person
opening a page, and a runner that never renders it grades nothing. A runner, an identity and a pair for a result that cannot
grade the outcome is not built. Msgs 4198 and 4338 are withdrawn; rows D2-W47-S1, S2 and S3 close on this, with W47-S2's
finding (the performance GET can persist and can spend a vendor authorization) carried to whichever act next walks that page.

**What replaces it: one rendered walk of FWD-1 on DEV, by an instrument that already signs in.**
- The laptop's `/ui-walk` account signs in for real. Its guard aborts every POST but the sign-in, and this journey needs two:
  `POST /selections` (one immutable, content-addressed item) and `POST /directory/resolve` (a read). Whether that guard
  admits those two named routes for one walk is the laptop CTO's call on its own tool. The ask goes through the managers.
- If the laptop declines, the walk is a person's: an Opal user, five minutes, DEV, the one named client. It is then listed
  for Andrew with its citation (PRD FWD-1, "An Opal user opens Investor Reporting").
- No sign-in identity is minted on dell2 for this.

**2. The 14 KNOWN-LEGACY labels are not accepted. Agreed, and the bar is tightened to the reviewer's.** A failing test is one
of two things: a REGRESSION with an owner, or an assertion RETIRED by a ruling that is cited. "Known" is not a third class.
2.0.0_SA_COO~D2 sends this seat one table of the 43 failing ids: for each, the owner and cell, or the retirement asked with
its reason. This seat rules the retirements in one pass. S7 and W21-S2 stay ARMED until the table is fully dispositioned.

**3. How the portal presses things in tests.** Through the public surface, never React's internals: the testing library the
portal already has in `package.json` if one is there, else a native DOM click inside `act`. The S60 test is rewritten to
that in the cell that next touches it, and 2.0.0_SA_COO~D2 states which of the two the repo supports.

## 3. Rulings on the rows

| row | ruling |
|---|---|
| **D2-W43-S2** (18 failures: contract files ahead of the portal half) | **The portal moves.** The contract is the ratified side. The portal's routes table, envelopes and content pins catch up, and the suite sample names both commits. |
| **D2-W43-S3** (5 failures named in no earlier row) | Each gets a fix or a ruling. **F40-AC5 first:** a portal calendar that disagrees with `lib/trading_calendar.py` can mislabel a day on a served page; the portal takes its fallback from the one frontier, never a second copy. F47-AC6, recorded fixed on 2026-10-03 and red again, second. |
| **D2-W43-S1** (bun at a hardcoded path under another user's profile) | The tests resolve bun from the environment (CLAUDE.md: derive, do not hardcode). One cell. |
| **D2-W46-S1, D2-S3, D2-S5** (owner this seat: the corrected security's display symbol and kind are not served) | One served change answers all three, and it is IRPT_YCDGEN's FWD-20: each upload-review row carries its own correction, the display symbol and the kind (a spelling the advisor accepted, or a proxy they named). The page then reads it from the row and stops matching on the uploaded symbol. Sent to 2.0.0_SA_COO~G2 as the shape FWD-20's cell serves; the page half is a later round here. |
| **D2-W46-S5** | The two dollar columns right-align in the next cell that touches the table. |

## 4. ENRICHMENT LIST for round 13 (ONE issuance, in this order)

1. **The FWD-1 rendered walk, asked** (section 2 item 1): 2.0.0_SA_COO~D2 writes the three-line ask (the client, the page,
   the two POSTs with what each writes) and `0.0.0_AB_MSTR~DELL2` carries it to the laptop.
2. **F40-AC5, the calendar.** LOCAL build; a served-page change, so its candidate comes to this seat.
3. **The 43-id table** (section 2 item 2). Read-only.
4. **The portal half catches up to the contract** (D2-W43-S2). Product files; candidate to this seat.
5. **bun from the environment; the press test off the private dispatcher; F47-AC6.** LOCAL.

Items 2, 3 and 5 are independent. Each build order carries at most three mechanical criteria. IRPT_DASHBD keeps priority on
this lane.

## 5. What this analysis did not measure

It rests on the slug and the reviewer's grade and answer as filed. This seat read none of the 43 failing tests, the portal's
calendar, or `/ui-walk`'s guard; that the guard aborts POSTs is 2.0.0_SA_COO~V2's statement (msg 3989).

-- 1.0.0_SA_CTO~DELL2
