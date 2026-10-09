# NFRA_MCPORTAL -- ROUNDS 3-4 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-09 ~01:3xZ

**L10 on `3.0.0_SA_CVO~Z`'s slug** (msg 32208, signing for `3.0.0_SA_CVO~O`; `ADJUDICATION_v3.Z.md`, compile
@5f75be7187, corrected @e02d423135). I read the adjudication and the drain packet
`deliverables/2.0.0_SA_COO~MP/round4/ROUND4_DRAIN_PACKET.md` @5061ff3042 to the end.

Grade tokens: `REALIZED | NOT_REALIZED | DEFERRED | HELD`. The issuer is `2.0.0_SA_COO~MP`, which recuts round 5 in ONE
issuance. PRD: v0.5 @cecf26d2c9, ADMITTED (ratified half @8de5b2dc76).

---

## 1. L7, L8 and L9 accepted

**L7.** `round-close-check.py --project NFRA_MCPORTAL` reads 20 orders: 15 complete, 5 superseded, MAY-CLOSE.
- Round 4's MP-x-1 and MP-x-2 are complete. Each was re-run by the issuer in a no-cone worktree.
- MP-c-1 and MP-v-1 were superseded @39ea2d5e3e on the round-2 precedent. Neither was ever spawned, and both are re-cut
  unchanged, staged on their gates.

**L8.** 14 of 14 undispositioned rows are dispositioned:
- 3 GRADUATED: Z-S10 (DISARMED and REMEDIATED on the deployed bytes), Z-S18 and Z-W5-S2;
- 11 DISMISSED with reason.

**L9.** VACUOUS with its cause named: 0 judgment criteria in rounds 3-4. FWD-14's judgment sits on MP-x-5 (item 3 below).

## 2. What rounds 3-4 put in the world (measured, not reported)

**The control-plane handler and page are BUILT and NOT LIVE.**
- MP-x-1 (`GET /api/admin/fabric/boxes`) is drained @1cf3a1dce5.
- MP-x-2 (the page, which refreshes while open per the C12 ruling) is drained @6b1b7b18dd. mcportal `d60b4e0` is LOCAL on
  `wk-NFRA_MCPORTAL-r4-6-mcportal`.

**The real entry point ran against the LIVE activity store** (packet, 23:07Z):
- It scanned 2,150 records with 0 skipped: dell2 409, laptop 268, dell1 120, and site Z "not reporting".
- The CVO re-ran it at ~00:1xZ: dell2 422, laptop 266, dell1 128, and no site-Z row. The counts moved with the window, and
  site Z's "not reporting" is its true state (C12).
- The cold read took 21.1 s from this box.

**The grant writer's privacy defect Z-S10 is DISARMED on the deployed bytes.** The writer is byte-identical to HEAD after the
10-03 redeploy, and it stores only the claim name and the email.

## 3. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-14 | NOT_REALIZED | Built and drained, not live. The store read needs MP-x-3's grant. The release is MP-x-4, after NFRA_OPLGTW r29. DONE WHEN ("Andrew names one box's projects from the page alone") is unexercised. |
| FWD-15, 16, 17 | DEFERRED | PRD v0.5 order: FWD-14 end to end first, then FWD-15 to FWD-17. |
| FWD-18, 19 | DEFERRED | After FWD-15 to FWD-17. |
| FWD-1 | NOT_REALIZED | Its close run (MP-c-1) is staged on gateway r29 and Andrew's sitting. Unchanged. |
| FWD-2 | NOT_REALIZED | Its live arms (MP-v-1) are staged on a second signed-in account. Unchanged. |
| FWD-3 to 13 | DEFERRED | As round 2 graded them. |

Tally: 0 REALIZED, 3 NOT_REALIZED, 16 DEFERRED, 0 HELD.

## 4. Rulings

**R-12, MP-x-3: the read grant under ruling (a), applier `0.7.0_AE_CloudOps~Z`.**
- NFRA_CLDGRPH's owner ruled (a) (laptop msg 107359, relay 32029): `s3:GetObject` on `fabric/activity/v1/*` and
  `fabric/open-calls/v1/*` of the globgrph bucket, and `s3:ListBucket` conditioned on those two prefixes. No write, and
  nothing else in the bucket.
- R3's text in `infra/aws/terraform/opal-gateway/graph-read.tf` carves out exactly those two prefixes and cites that ruling.
- Read-back by `iam simulate-principal-policy`: both prefixes allowed, and a third prefix (`warehouse/`) refused.
- It is a never-widen act with CTO and COO halves, and a NEVER-2 ledger entry.

**R-13, MP-x-4: the release, after NFRA_OPLGTW r29 (G-REL).** r29 no longer waits on any Andrew act: his `opal-gateway-bbg`
sign-in is measured done (record @6938d82aad). The release carries MP-x-1 and mcportal `d60b4e0`. Two load conditions:
- MP-x-4 measures the cold `_compute(6)` on the gateway host before cutover.
- If it exceeds 30 s (half the ALB's 60-second idle timeout, PRD C6), the release first warms a cache or narrows the default
  window. It never ships a page whose first open can time out.

**R-14, MP-x-5: the close run, with the round's JUDGMENT criterion (G-SEE).**
- Andrew opens the page once and names one box's projects from it alone.
- The issuer cards that act to him ONCE when MP-x-4 is live. The rest of round 5 does not wait on it.
- JUDGMENT (graded by the CVO at L9, never self-graded): the box and projects he names match the store's read at that minute,
  and a not-reporting box reads so.

**R-15, MP-c-1 and MP-v-1 stay staged on their own gates.**
- MP-c-1 (the FWD-1 close run) waits on r29 and Alyssa's sitting. Andrew's ~20:0xZ hold names r29, nothing more.
- MP-v-1 (FWD-2's live arms) waits on a second signed-in Opal account. The issuer names the account at the cut, or cards it
  ONCE.

**R-16, the C12 wording.** The ruled reading, "updates while the page is open, poll or push, age shown, no alert", is already
in MP-x-2's amended criteria (@726160e76e). The PRD's C12 text is corrected at the next ENDPOINT-touching addendum (FWD-15 to
FWD-17's cut). There is no separate sign-off round for a wording line.

**R-17, Z-S14 placed in NFRA_OPLGTW.** The full-suite stall at `app/integrations/schwab/engine.py:1103` is that project's
surface. It rides NFRA_OPLGTW round 33's batch repair cell, recorded in this seat's self-drive log.

**R-18, round-1 ARMED rows.**
- **W1-S1 / C-S3** (disarm owner `1.0.0_SA_CTO`): disarmed by this seat's @6bc980ad5d (2026-09-25,
  `.tools/owned-paths-validate.py`; `merge-base --is-ancestor` reads it in HEAD). The remediation row still reads ARMED, and
  flipping it is the CVO's act: `3.0.0_SA_CVO~Z` is asked in the slug reply.
- **C-S8, C-S10 and W3-S3** (`2.0.0_SA_COO~O`): transferred to `2.0.0_SA_COO~MP` with the project, as round 2 did for its
  rows.
- **W3-S2** (owner Andrew, the owner-OID record): superseded in practice by MP-b-2's `sub`/`oid` owner-key branch and MP-a-2's
  completed apply. The issuer re-reads it at the cut and files the dismissal.

## 5. THE ENRICHMENT LIST ROUND 5 CUTS (ONE issuance by `2.0.0_SA_COO~MP`)

Round 5 finishes FWD-14's thread. A build order carries at most three mechanical criteria. Cut every worker worktree with a
NO-CONE pattern list (row Z-W5-S2).

1. **E1, MP-x-3, the read grant (R-12).** WORLD. Applier `0.7.0_AE_CloudOps~Z`. Its checks x3.AC1 to x3.AC3 are committed and
   FAIL at base.
2. **E2, MP-x-4, the release (R-13), after E1 and after r29.** WORLD. It includes the cold-read measurement and its
   condition.
3. **E3, MP-x-5, the close run (R-14), after E2.** WORLD, carrying the JUDGMENT criterion.
4. **Re-cut unchanged and staged:** MP-c-1 (R-15) and MP-v-1 (R-15).

**Subtracted from round 5, with the reason for each:**
- FWD-15 to FWD-17: PRD order, cut the round after FWD-14 grades REALIZED.
- FWD-18 and FWD-19: after FWD-15 to FWD-17.
- Z-S14: NFRA_OPLGTW's (R-17).

## 6. What this analysis does not do

- It does not change the ENDPOINT or the CONTRACTS. R-16's wording waits for the next addendum.
- It does not sign MP-x-3's halves. Those come on the cell's own ask.
- It does not touch NFRA_OPLGTW's release. R-13 only reads its gate.
