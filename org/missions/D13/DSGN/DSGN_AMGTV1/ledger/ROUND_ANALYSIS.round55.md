# DSGN_AMGTV1 -- ROUND 55, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~01:5xZ)

**Inputs:** `deliverables/2.0.0_SA_COO~D1/round55/ROUND55_CLOSE.md` @e7acc2964c, read whole. This is the first round on dell1 (re-placed
@a4bcfa869f on Andrew-direct 2026-10-08 ~22:5xZ). The candidate review was sent as msg 1319 (PASS); this file is its carrier.

## 1. What is live

Portal DEV `8d2a08a9` = `84e13d0f` + AV-zzg-1 (3 files under `src/pages/Freshness/`, +11 -5), fast-forwarded by `0.0.0_AB_MSTR~DELL1` and
read on origin by this seat (ls-remote). PROD `f73f9ab0` is unchanged. Nothing served on PROD moved this round.

## 2. Graded

- **AV-zzg-1: MET.** Read on the signed-in walk at 01:50Z on the local dev build of DEV `8d2a08a9` (`tmp/ui-walk/20261009T015010Z`,
  95 rows): the head reads "Built analysis" with no "Research pack" left, the day cells stay on one line, and only the Seeking Alpha
  sentences wrap. The `data-state` attribute is graded by r54 arm 1 (4 of 4). The walk is a local dev read and is not PROD acceptance.
- **Walker hygiene: MET.** It was disarmed after the walk: the row reads disabled, the password is refused at `/auth/login` (401), and
  the parameter was NOT deleted (an unrecoverable act; CTO msg 1327).

## 3. Rulings

- **R1, the date forms (walker finding UIW-...-001).** One page, one date form. The cells and the footer "Data as of" use the same form,
  the one the portal's other pages already use; the decomposition reads which form that is and cites it. This predates the round and is
  not a regression.
- **R2, Lenovo 992 HK (Seeking Alpha last read 2026-09-22, the 1 of 95 older than 7 trading days).** This is a producer fact, not a
  page defect. It goes to AMGT_HARVST (`2.0.0_SA_COO~W1`) as a row. Seeking Alpha collection is a site-Z producer, so the row's
  owner may be site Z. The page draws what is served.
- **R3, the walker's disarm stops at `ssm:DeleteParameter`.** A disarm that tries an unrecoverable delete every time is a skill
  defect. `/ui-walk`'s disarm should end at "row disabled + password refused" and never delete. Routed to `0.0.0_AB_MSTR~DELL1` for the
  skill's owner.
- **R4.** The console's two 401s at the sign-in probe and the duplicate `createRoot` warning are not Freshness defects. They are noted
  and carry no cell.

## 4. ENRICHMENT LIST, round 56 (ONE issuance by `2.0.0_SA_COO~D1`)

1. R1: one date form across `/freshness`, with a test pinning footer and cells to the same form.
2. R2: an AMGT_HARVST row for Lenovo 992 HK's stale Seeking Alpha read, filed by D1, owner W1 or site Z by the census.
3. Any carried item from site Z's round-54 list not served by AV-zzg-1, as the hand-over names it.
