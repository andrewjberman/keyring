# AMGT_RESAPP round 19 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ HEAD after `4b578f8d76`, LOCAL (the push is `0.0.0_AB_MSTR~Z`'s,
LD-0522). **Written:** 2026-09-21 ~20:2xZ.
- **State:** DRAIN-END, complete. 4 of 4 terminal, 0 open.
- **Issued:** as one slug @`fe7d6cc756` (decomposition s.27, four orders, both COO halves), per Andrew-direct ~15:12Z.
- **Pairs:** completed by the CTO halves @`694f5f1aba`.
- **Waves, as s.27c set them:** rk-76 went first, then rk-75 once its pair was complete. rk-77 followed after rk-76
  drained, and rk-78 after rk-77 drained.

## 1. Round state, final

| cell (slot) | drain | second instrument (this seat's own) |
|---|---|---|
| rk-76 (~76), slash-safe key | `e37f29cc16` | Called the new functions on inputs the worker's tests did not use: a multi-slash key `A/B/C_XX_Equity` round-trips, a key already carrying `-SLASH-` is REFUSED, and `security_key_partition('BP/_LN_Equity')` = `security_key=BP-SLASH-_LN_Equity`. Merged tree: identity + api = 240 passed. |
| rk-75 (~75), readable NOT_SEARCHED reason | `f33b359869` | Leaf-diffed each of the 3 keys, pre-act VersionId against latest. Each has 3 versions, and the changed leaves are EXACTLY `ceo_public_profile.basis` and `ceo_public_profile.reason_code`. raw/bloomberg counts are unmoved (CAT 12, CSL 14, 6861 14). RAN `scoped_amgt.ceo_profile_reading` on the post-act objects: NOT_SEARCHED, `urls_returned` None, with the table sentences. Management suite: 84 passed. |
| rk-77 (~77), serve the fallback roster | `03af0dd7a9` | Live `get-function-configuration` shows CodeSha256 `hP+6OO5P...`, Active / Successful. The thesis leaf was invoked for 4 names. CSL is SERVED BLOOMBERG_FALLBACK with 14 officers (14 listed); 6861 the same with 1 officer; CAT is SERVED with roster_source FILING; ASML is ABSENT ZERO_OFFICERS 0. api + identity: 246 passed. |
| rk-78 (~78), render the fallback source and reason | workspace `a6ada7dc1a` (the append conflict on the channel was resolved by adding W78-S1's exact row to ours, 459 + 1 = 460, then `--continue`); portal branch `wk-amgt-19-78-portal` @`95d96edb`, UNPUSHED | Read the 7-file portal diff myself. All committed blobs are CRLF 0 and non-ASCII 0. The code change is 3 hunks: the Confirmed cell, the extra absent case, and the fallback line. **/frontend-dev screenshots** of that branch against live `/thesis` bodies: CSL shows the fallback line above the table and "per Bloomberg, not the filing" on all 14 rows; the CAT control is unchanged (no fallback line, "confirmed from the filing"). The light text sits inside the dark Panel, as the colour law requires. |

Every worker reported every criterion PASS-by-output, and every proof instance is VALID (rc 0, from each worktree's own
checker). No rollback fired. Both deploy-ledger entries (rk-75, rk-77) were opened before their live write and closed on
their read-back.

## 2. For the grade

1. **rk-78's portal DEV push is owed, and it is not yet done.** The branch `wk-amgt-19-78-portal` @`95d96edb` is routed
   to `0.0.0_AB_MSTR~Z` (LD-0522), along with the superproject gitlink move. The PROD promote is STANDING for AMGT page
   features (CTO adjudication @`c7bbb53f2a`, item 1), so it goes through the DT owner after DEV. **Z-S194 is served
   live now** (rk-77); **the page half is live once DEV + PROD land.**
2. **Row W75-S1:** AC1's prose said "1 of 1" headings, but both halves measure 2 (an H1 and an H2 both name rk-75). The
   refusal rule never fired, so there is no grade impact.
3. **Row W78-S1:** the worktree's `core.autocrlf=true` checked out CRLF. It was fixed on disk, and the committed blobs are
   LF. There is no grade impact.

## 3. Rows filed by this seat this round (all @ SITEZ, LOCAL)

- `Z-S194` (the false ZERO_OFFICERS label): remedied by rk-77 + rk-78.
- `Z-S195` / `Z-S196`: the JP-President rule and its disarm. The rule is now in PRD v0.16.
- `Z-S197` (a literal "None" in Keyence's reason): OPEN, disarm owner the CTO, remedied by R20-A.
- `Z-S198`: VOID. Superseded by `Z-S199`, crossed messages; the CTO's msg 24043 arrived 2 minutes after the commit.
- `Z-S200` (CSL's stale, technical reason): OPEN, remedied by R20-A's second write.
- **From this seat's own screenshots:**
  - `Z-S201`, INERT: a doubled full stop on every not-searched CEO line, and a "from the filing" subtitle over a
    Bloomberg table. This is portal-side.
  - `Z-S202`, **ARMED**: CAT, a validation name, serves a **1-officer RESOLVED roster** (its Chief Legal Officer only)
    because its 10-K Item 10 says the officers "appear in Item 1D", and the parser does not follow that
    cross-reference. There is no CEO on CAT's page, and the roster is served as complete.

## 4. What this seat asks of L9/L10

- Grade the 4 terminal cells on their branch-HEAD criteria; none carries a judgment criterion.
- **Round 20** is R20-A (rk-79). It is ruled in full (CTO msg 24049) and adds a second write for CSL. The drafted order is
  being amended to that ruling, and it is cut after this round's L10.
- **For the CTO's analysis:** `Z-S202` is the most manager-visible open defect on the three validation names, and
  `Z-S201` is the cheapest to fix.
