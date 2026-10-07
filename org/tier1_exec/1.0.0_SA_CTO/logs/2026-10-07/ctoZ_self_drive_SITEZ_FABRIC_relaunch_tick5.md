# /self-drive site-Z fabric -- tick 5 (1.0.0_SA_CTO~Z)

**archetype:** COORDINATE

- **Ticks covered:** 5 (11:49Z), plus the event-driven rulings since the tick-4 log (@0f7e460190). **state: ARMED**, cadence 60m,
  cron `12f228ad` (session-only).
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
  @d97558efe8.
- **Scope:** AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP, DSGN_AMGTV1, ETFS_RIVALS. Device sitez.
- **Inbox at tick 5:** 0 unread. Sequence not re-read (no stage moved).
- **Push state:** every commit below is LOCAL; origin CLOUD 324e7f0232 (ls-remote read at 11:49Z).

## Calls ruled since the tick-4 log

| # | call (msg) | ruling | carrier |
|---|---|---|---|
| 1 | opal-gateway r26, CTO half (COO~O 30813) | SIGNED on `feddb37244`; C1 an unreadable content hash skips the re-send dedupe, one read owed at the first real send; C2 the allowlist row never ships without the id check. All three halves now read signed (CVO~Z's relayed, 30818) | `CTO_HALF_NFRA_OPLGTW_OG-rl-12_GATEWAY_R26_20261007.md` @78d524e001 |
| 2 | ETFS_RIVALS: 96 securities with no stored currency draw no curve (COO~RV 30816) | the backfill's list includes formerly-held keys, inside the existing Bloomberg budget; until then no curve, with a plain reason. Term 4 of the currency repair accepted as proved (0 of 598 jumps) | message only |
| 3 | HARVST round 54: does the brand make the text check inert (COO~H 30822) | keep the brand; a graded sample decides, per brand, bar 29 of 30. The standing move of Z-S92 and Z-S94 re-routed to CVO~Z (my lane error, 30826) | message only |
| 4 | HARVST: the CVO's grade, Meta 29/30 and Lilly 29/30 (CVO~Z 30835, @cc31b43fbc) | both admitted on the collector's text plane; NO "about the company" threshold in the collector; aboutness is a derived attribute, routed to RESAPP's list as one read first | message only |
| 5 | HARVST: does that admit the brands to the GOLD matcher (COO~H 30841) | no; collector only. Gold is a third plane with its own census: a dry run, the added mention rows per brand, a CVO grade of 30 each | message only |
| 6 | DSGN round 47 candidate `ec9f9a0e` (COO~D 30830) | APPROVED for DEV from the diff and two captures | DSGN ledger, section ROUND 47, @07ff6ebe34 |
| 7 | DSGN round 48 candidate `97598dc3` = `ec9f9a0e` + one script commit (COO~D 30850) | rides the ONE DEV push on Andrew's word; FWD-18 and FWD-20 to CVO~Z for re-grade | message only |
| 8 | RESAPP ba-21 probe read branch B; ba-22 landed 86 of 86 (COO~Z 30846) | CRO~Z names candidate segment mnemonics (done, 30855, all from recall); ONE more AMD call with at most eight, product segments only. The slash-reader repair (row Z-S365) is a round-78 cell | message only |

## Clock-gated reads, 11:30Z (this seat's own)

- **Bloomberg vehicle** (`%USERPROFILE%/opal_bbg_logs/bbg_tplus1_20261007_070002.log`, task result 0): the tplus1 tripwire PASS with
  the new limb, "all 13 custom CIX series reach the as-of 2026-10-06"; published; served `data_as_of 2026-10-06`, generated
  11:07:26Z; every other leg exited clean. Rival-funds enrichment names: 6 asked, 0 named (PARTIAL, not a leg failure).
- **Freshness check** (`C:/opal-elev/freshness_check.log`, 11:30:02Z): PASS, trading_days_behind 1; per-series, 10 graded, every one
  ends on `data_as_of`. No summons; the escalation file was last written 2026-10-06 07:30 local.
- **First live read of both detection edits (fix-route ADDENDUM 6): both PASS.** Yesterday's result 2 was a true STALE read.
- **ETFS_RIVALS census** (COO~RV 30844, @b74bdc238b; not opened by this seat): holding_contribution MERGED 13 of 13, Nebius control
  MERGED, 0 wrong merges; ledger pk1-al1 CLOSED 4 of 4. buying_trend still splits 7 (row Z-S57, cause unread).
  `fund_sections missing 0`, which the handoff expected, is not in the message: UNREAD.

## Open, and who holds it

- `2.0.0_SA_COO~Z`: the second AMD probe; the pool re-mint after the CORPUS fire's read, then ba-23; the round-77 drain.
- `2.0.0_SA_COO~O`: r26 Phase B, waiting only on the origin push (today's send reads served).
- `3.0.0_SA_CVO~Z`: the DSGN re-grade of FWD-18 and FWD-20; the HARVST round-54 slug.
- `2.0.0_SA_COO~RV`: row Z-S57; the Lambda deploy.
- This seat: after 13:15Z the CORPUS fire read and the RIVALS sweep. DSGN FWD-7 re-grade on covered names after ba-22. At the next
  DSGN amendment: the covered-names rule into FWD-4, and PRD line 218.

## Acts only Andrew can do

1. The site-Z push and pull-merge (LD-0367/0368): r26 Phase B and the MDPF_SECHIST deploy wait on it.
2. The portal DEV push of `97598dc3` (product files; CLAUDE.md Portal: trunks move on his word through `0.0.0_AB_MSTR~Z`).
3. Lifting his Bloomberg no-modify order for `tzero/tools/bbg_pkl_tripwire.py` (branch `rv-bbgtml-guard4` built and proved).
4. In Entra: which grant carries the concierge's 17 scopes, then the revoke and the `/login` sign-in (row NFRA_OPLGTW-Z-W28-S11).
5. DSGN FWD-1: his own signed-in walk on the live product.

## Completion test

NOT DONE: 0 of 5 complete. All five read `status=active dep_stage=EXECUTING` at 11:49Z. All five REACHABLE.

## Compiler Tools

- `Get-ScheduledTaskInfo` on the OPAL tasks; the vehicle log and the checker log read by tail.
- `git diff` of the r26 release commit and of the portal candidate; one PNG read at full size, one reduced.
- Not run: `sequence-check.py`, `active-commitments.py` this tick.
