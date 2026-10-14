# NFRA_MCPORTAL -- PC ROUND-1 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-14 ~17:5xZ

**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 34161, `surprise-channel/remediations/REMEDIATION_v5.Z.md` @580db3fb7b.
L8: `adjudications/ADJUDICATION_v5.Z.md`. **Issuer:** `2.0.0_SA_COO~MP`. **PRD:** v0.8 (unchanged; no addendum needed).

## 1. PC round 1, as read

6 of 6 orders terminal, served at `bacec95ccd` (the MP-pc-5 release). MAY-CLOSE.

| item | grade | why |
|---|---|---|
| G1 three-state refusal display (Z-C-S31) | **REALIZED** | served; laptop reads "refused: false", sitez "not recorded"; flipped REMEDIATED (REMEDIATION_v4.Z) |
| FWD-21 read half (F1, the People view) | served, **FWD-21 NOT_REALIZED** | FWD-21 is "sees, then changes"; the change half (F2) is not built. The view is untested under its real reader path (Z-W24-S2) |
| FWD-22 first cell (U1, account source) | served, **FWD-22 NOT_REALIZED** | account is credential-free on 1 of 4 boxes; the 5-hour and weekly remaining have no source yet |
| MP-pc-4 AC2 | PASS, bounded (Z-C-S35) | the bound is the 1-of-4 above |

## 2. Rulings

1. **Z-W24-S2 is closed by a seat, not by Andrew's sitting.** The operator role reads `/api/admin/people` through the
   served route and compares it with the grant store for the same person, for each data-grant tool, with the denominator
   printed. Andrew's sitting (call 21d9) still reads it as the owner, but nothing waits on that.
2. **FWD-22's usage source is a status-line command, proven on site Z first.** The 5-hour and weekly fields are
   inferred from the binary, so the cell's first act is to see one live `rate_limits` payload on this box. Only then does
   it write anything. Configuring the status line changes every site Z seat's Claude Code settings. The cell names that
   blast radius, and its rollback is removing the one settings key. The other three boxes are other fabrics: once site
   Z is proven, a cross-box direction (MSTR to MSTR) carries the same setting there, and each box's account source is
   read there, never assumed.
3. **F2 (FWD-21's write half) is cut now on the C18 contract, with one dependency named.** The grant-writer record kind
   and the on/off write, with the change history and a test principal, are built and proven against the store. A
   change takes effect on a real call only when NFRA_OPLGTW's C-PERSON reader is live. F2's served-effect criterion waits
   on that cell, and nothing else in F2 does. Writes stay Andrew-only (laptop CTO ruling @f469cb665f).
4. **The unexercised refusal branch (rc != 0) stays unexercised.** No box produces it today, and forcing one would
   mean a planted failure on a live box, which is not worth its cost. It is graded when it first occurs.

## 3. NEXT ROUND -- ENRICHMENT LIST, cut in ONE issuance

| cell | content | risk |
|---|---|---|
| **R1** | Z-W24-S2: the operator-role read of `/api/admin/people` vs the grant store, per data-grant tool, denominator printed | SERVED |
| **F2** | C18 record kind + the channel/tool on/off write through the one grant writer, change history (FWD-4), a test principal; served-effect criterion depends on OPLGTW C-PERSON | WORLD |
| **U2** | FWD-22 usage on site Z: see one live `rate_limits` payload; then the status-line command writing it to a local file; the panel reads it; blast radius and rollback named | WORLD |

The cross-box carry of U2 to laptop, dell1 and dell2 is NOT a cell of this round. It follows U2's proof as a direction.
