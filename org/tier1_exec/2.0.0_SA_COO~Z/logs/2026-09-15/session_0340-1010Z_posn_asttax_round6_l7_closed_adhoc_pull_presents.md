# POSN_ASTTAX round 6: L7 CLOSED -- B6 deployed and driven, F4/F5 on the portal ref; the real ad-hoc pull landed and PRESENTS; the promote clock -- 2.0.0_SA_COO~Z

**archetype:** COORDINATE

**Date:** 2026-09-15 03:4xZ - 10:1xZ
**Task Order:** none held by this seat; L6/L7 owner of POSN_ASTTAX round 6; the R2/R3 halves and the driven runs of the ad-hoc pull.
**Status:** round 6 L7 CLOSED (the close commit named in the Files table). L8/L9 at `3.0.0_SA_CVO~Z`; L10 drafted by `1.0.0_SA_CTO~Z`;
the portal merge and promote by 13:00Z are `0.0.0_AB_MSTR~Z`'s on Andrew's word. The third driven characteristics run is armed on the
~11:05Z models publish (R3/A3); B6's 12:30Z fire is the organic arm (ledger L8).

---

## Objective

Andrew ~02:3xZ: fix the Satellites mode completely tonight. Andrew ~07:4xZ (via the laptop MSTR): the merge and promote ride on a REAL
ad-hoc pull and the data presenting properly on ASTTAX. Andrew ~08:0xZ: the portal promoted by 9 AM ET (13:00Z).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| safe-commit | the issuance 910815809f; amendments 1b791c6a11, 6aaf98db39, aacde43a63, 973d4a5f6f, 7bcc47d6fe, 03a334e357; halves b2560929dc (R2), f083f68e17 (R3); records e53147ebe0 .. ad3a87b244 | PASS | gate (viii) graded every modification; one refusal (a preflight line's denominator on a continuation line), one lint refusal (a copied script), both fixed |
| safe-merge | drains 72830dc797 (F5), ec1cc68aec (B6), 8e81206eba (B6 re-run), 09006e6887 (F5 re-run), 51c6108f7e (F4), + the final F4 drain | PASS | channel conflicts as the union by id; PORTAL_REFS as the union of both appended lines; one merge REFUSED by the peer's staged index, one aborted by my own wrong expect-ids (nothing landed either time) |
| git (portal) | `refs/drains/posn-6-portal` dd1d33c6db -> 10a2799c -> 5ddce2c7 -> ebbee2e6 (a merge of F4 onto F5's re-cut) | PASS | gitlink e85f6eb84f unmoved; the merge commit carries the repo's default author (the amend was refused by a hook -- a record note) |
| Agent (worker) x7 | ~24 (B6) x2, ~26 (F5) x2, ~25 (F4) x4 incl. one HUNG run stopped at 09:21Z | 3 of 3 orders complete | four spawns for F4, three on the issuer's invocation defects (W25-S1/S2/S6) |
| Agent (Explore) x2 | B6 backend and the portal at dd1d33c6db | line-referenced reports | the decomposition's premises |
| aws (shim) / boto3 | the driven runs (04:53Z by the worker; 08:09Z and the armed third by this seat), read-backs, the fixture fetches by VersionId | PASS | every read back on the served key |
| ui-smoke + w25 instruments | the presentation on the ref against six served keys | 0 of 512 cells; the MSTR 0 of 544 | two instruments, one verdict |
| ack_messages / send_message | 22958 .. 23112 acked; sends: the B6 half ask, the step-2 split, the step-2 report, the vintage plan, the steward read, the slot notices | heads-down otherwise | every send a flow carrier |

**What worked:** re-cutting the round's order defects the turn a worker refused them, never repairing by hand; draining and adjudicating each
run the turn it landed; pinning every fixture by VersionId + md5 so a key that moved live (twice) never made two renders incomparable;
the MSTR's independent instrument agreeing with this seat's on every count.

**What failed (mine):** (1) the F5 act-1 wording added a word the constraint does not carry ("portfolio values always"), caught by the
worker (W26-S6) and re-cut; (2) three F4 invocation defects in one order -- an MSYS path handed to native python, and TWO limbs anchored
to the moving drain ref (W25-S2, then W25-S6 after I fixed only two of three); (3) the B6 order's two unrunnable invocations (a lens with
no positional; a recorder with a positional first) and a FLAT/repo-path citation that named the opposite of its bytes; (4) the second F4
resume HUNG for 1h46m re-running a criterion that stood, and I read "still in progress" from the harness rather than from the worktree
until the CTO measured it; (5) the sparse cones cut without the paths the commit gates read (W26-S7, W24-S2/S8 -- banked).

**Gap found:** an issuer's paraphrase of a constraint at L5 is a second carrier of the spec's sentence; cite the sentence. A bar's
anchor is the branch base recorded in PORTAL_REFS, never `refs/drains/*`.

---

## Work Completed

1. **Round 6 cut and closed:** decomposition + three orders on PRD v0.10, re-pinned to v0.11 with three amendments the same hour; B6 deployed
   (CodeSha256 rN/jcmeQ..., rule cron(30 12 * * ? *), the READ widening incl. GetItem on etf-classifications) and driven; F5 and F4 on the ref.
2. **The real ad-hoc pull, end to end:** the 07:00Z registry fire (organic, Z-S165), the CTO's ad-hoc Bloomberg pull bbg/2026-09-14 (07:52Z),
   the second driven characteristics run (08:10Z, PXyBGaqn...), the presentation on the ref (Z-S171), the MSTR's independent PASS (23103).
3. **The vintage qualifier answered:** R3/A3 for a third driven run after the ~11:05Z models publish; no models task fired early.
4. **Rows:** Z-S137, Z-S140..Z-S174 (adjudications, disarms, the organic arm, the presentation, the cosmetics carried to L10).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| The Holdings panels' footer and the treemap legend given to F4 under the constraints' plain text (Z-S136, Z-S144) | Andrew's words name the mode and the view, not one panel; the file is F4's; rows carry the reading for L10 |
| The F5 label rule taken from the PRD's clarification, not my first reading | the worker was notified mid-run before any commit; Math.round never became a byte |
| B6's B4 ledger L8 SUPERSEDED by the rescheduled rule's first fire | Rule 27: the mechanism driven, the organic arm the negative case |
| The hung F4 worker stopped and re-spawned with a hard box rather than waited | the slot; the shipped bytes were already verified twice |
| The third driven run armed on the models publish, not on firing the models task early | the MSTR's read: it moves the served Models key and double-publishes |

---

## Files Modified (all LOCAL)

| File | Change | Commits |
|---|---|---|
| decompositions/POSN_ASTTAX_DECOMP_round6.md | NEW, CUT | 56f4d41933, 910815809f |
| task-orders/TO-W1-1, TO-W2-1, TO-W3-1 | NEW + amendments/re-cuts | 910815809f .. 03a334e357 |
| ledger/NEVER_WIDEN_ROUND6_COO_HALF.md | NEW + R1 (table read), R2, R3 | 56f4d41933, 1b791c6a11, 6aaf98db39, b2560929dc, f083f68e17 |
| surprise-channel/investigations/INVESTIGATION_v1.md | Z-S137 .. Z-S174 + the drained worker rows | many |
| deliverables/2.0.0_SA_COO~Z/present_20260915_0813Z/ | the presentation artifacts | ad3a87b244 |
| project.json | ROUND 6 ISSUED -> L7 CLOSED | 910815809f, the close |
| this log | NEW | the close |

---

## Blockers

None at this seat for L7. The promote (13:00Z) is the MSTR's on Andrew's word; the third driven run waits on the models publish; B6's
12:30Z fire is a read.

---

## Current State

POSN_ASTTAX: PRD v0.11 @ab2ee8052a ADMITTED. Round 6 L7 CLOSED; portal ref ebbee2e6 published provisionally by the MSTR to the portal
origin as sitez/posn-asttax-r6. Served: holdings.json 5tjkvDfu... (07:00Z), characteristics.json PXyBGaqn... (08:10Z). All commits LOCAL.

---

## Next Steps

1. **[this seat]** ~11:05Z: the third driven run on the models publish, re-render, report the VersionId to the MSTR; ~12:3xZ: read B6's
   first scheduled fire and close ledger L8 with a row; worktree cleanup of slots ~24..~26 at L9 (with the operator's word on deletion).
2. **[3.0.0_SA_CVO~Z]** L8/L9 on the round-6 rows; the slug. **[1.0.0_SA_CTO~Z]** L10 (drafted) carrying Z-S146/S151/S154/S163/S169/S172.
3. **[0.0.0_AB_MSTR~Z]** the merge and promote by 13:00Z.
