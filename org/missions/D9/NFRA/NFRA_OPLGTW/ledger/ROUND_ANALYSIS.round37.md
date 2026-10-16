# NFRA_OPLGTW -- ROUND-37 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-16 ~11:2xZ.
**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 34958, `surprise-channel/adjudications/ADJUDICATION_v31.Z.md` (with v29 and v30) @880ff8aacc.
**Issuer:** `2.0.0_SA_COO~O`. **PRD:** v3.14.

## 1. Round 37, as read

The round is MAY-CLOSE, with 7 of 7 judgment criteria graded.

**The gateway finish (Andrew, EOD 10-16) is served:**
- OG-ap-23, release `3d5c9c8bf1`, is LIVE with 27 of 27 tools. Client admission is master_admin only (v3.14), with 0 reads on refusal.
- C1, C2 and via_internal_reader are MET (v28).
- OG-ap-27 and ap-26 are applied.
- MX-r-15 (B `0cb4a87bcb`) has landed, and the MCPORTAL segmentation is served.

| criterion | grade | what is owed |
|---|---|---|
| ap-18, ap-19, ap-20, ap-21 AC3 | MET | -- |
| ap-23 AC3 | PARTIAL | client holdings carry no weight unit or currency |
| ap-14 AC3 | NOT MET | OG-mg-1's writes (all three halves signed 11:1xZ), then the BBGTerminal seat's own 8-tool re-exercise |
| hv-2 AC3 | NOT MET | the FWD-21 stand-in read, then the named asset manager's driven call |

## 2. Rulings

1. **ap-14 closes by its own chain.** OG-mg-1 Phase B writes, then `0.0.3_BG_BBGTerminal` re-exercises the 8 tools.
   - The ask's premise is open: a Schwab-family grant may not admit `opal_discover` or `ycharts_freshness`.
   - So the re-exercise reads per tool. A DENIED tool is a BLOCKING row naming its gate; it is never a pass by assumption.
2. **hv-2:** the stand-in read is a seat's act and is cut. The named asset manager's driven call is a person's act. It goes on
   site Z's open list as an act, with its citation, and is not a cell.
3. **ap-23 PARTIAL is a defect of the envelope, not of admission.** Client holdings state their weight unit (fraction or percent)
   and currency per row, from the adapter's source. It is a code cell that rides the next batched release.
4. **Z-S173 (Alyssa's live grant holds `download_filtered` against PRD v2.2/v2.3's no-download)** is with Andrew as act row bd68.
   His 10-08 words set it. No cell until he answers.
5. **The muse narrowed client (route C, M365 mail and Teams only)** is folded into this project on Andrew's word (records
   @66f25c55e2, @adb8e79330). It is cut this round.

## 3. ROUND 38 -- ENRICHMENT LIST, cut in ONE issuance

| cell | content | risk |
|---|---|---|
| **E1** | OG-mg-1 Phase B: R1 and R2 writes, ledger, revoke as rollback (signed) | SERVED |
| **E2** | ap-14 close: the BBGTerminal 8-tool re-exercise, per-tool reading, DENIED = BLOCKING row | SERVED |
| **E3** | hv-2 stand-in read (FWD-21) | SERVED |
| **E4** | client holdings envelope: weight unit and currency per row, with a test on each adapter's real row | LOCAL, rides the next release |
| **E5** | a coverage floor beside an empty news answer: "no articles in window W, newest article at T" (ap-19 enrichment) | LOCAL |
| **E6** | harvest chatter states its lag in trading days (enrichment) | LOCAL |
| **E7** | the 49F SmartX served read: count candidates whose advisor maps to another firm, with the denominator (v28 enrichment; expected 0) | SERVED |
| **E8** | the muse-only narrowed OAuth client: M365 mail and Teams tools (read and send) plus whoami. A planted Schwab call and portal call by its client both REFUSE; Andrew's client is unchanged | WORLD |

The name_rulings `ruling_ref` work (OG-rr-2 plus the 110-row backfill) is already issued and is not recut.

## Update ~12:2xZ -- CVO v32/v33 (msg 34988, @c49cc748ce): 8 of 8 graded, MAY-CLOSE

- **ap-14 AC3 and mg-1 AC3: MET, bounded.** After OG-mg-1's writes (R1 and R2), the Bloomberg seat's own re-exercise reads 7 PASS and
  0 DENIED. `gateway_query_catalog` is admitted, but its data path is unexercised. The premise this seat doubted (a Schwab grant
  admitting non-Schwab tools) held because R2 unscopes the principal. E1 and E2 of round 38 are therefore discharged.
- **Z-S176:** `round-close-check` grades from the first CVO row, not the grade of record. That tool is NFRA_CTLPLN's, so it goes
  cross-box to `2.0.0_SA_COO~C` (XB below). It is not a cell here.
- **Z-S175: a key-lookup failure returns HTTP 403.** A missing key is not a forbidden one. Added as round-38 cell **E9**: a missing
  key answers 404 (or the gateway's not-found envelope), a denied one answers 403, and a test covers both arms.
