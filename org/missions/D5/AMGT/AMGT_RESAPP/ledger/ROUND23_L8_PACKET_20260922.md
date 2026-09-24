# AMGT_RESAPP round 23 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `fc2d043bf8`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~09:5xZ.

**DRAIN-END, complete:** 2 of 2 terminal, 0 open.
- Issued as one slug @`cb66bab9c0`, on the CTO's round-22 analysis @`ace3f7ca38` (msg 24153).
- No backfill word from Andrew was on file at the cut, so no backfill cell was issued.

## 1. Round state, final

| cell | drain | second instrument (this seat's own) |
|---|---|---|
| rk-94 print fix (Z-S215): fiscal years sorted on a normalised key; adapter redeploy under a pair with the AC7 closure check | `64e9cfb830` | Adapter CodeSha256 `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=`. This seat invoked /print once per name, with a 60 s client read timeout: CAT 15.4 s, CSL 16.8 s, 6861 16.7 s, each status 200 with no FunctionError. BA and COST also returned 200. The CTO accepted the drain in msg 24168, reading all 13 routes at 200. |
| rk-95 GATE 5 quoted-path parser (Z-S209), code only | `fc2d043bf8` | This seat re-ran the suite in the worktree and got PASS 106, FAIL 0. Separately, it compared all 106 arms against the pinned-hook run with a regex that accepts ANY verdict word, where the order's comparator accepts only PASS or DENY. Exactly 5 verdicts changed, all of them S209 quoted positives moving DENY to PASS. None of the 8 arms with non-standard verdicts moved, which closes the gap W95-S1 names. The negative controls still DENY: N1 quoted workspace-root push to CLOUD, N2 a non-DT seat, N3 cd to the quoted root then push, N4 a missing directory. The hook diff is confined to :286-303. |

rk-94 is the only live act. Its deploy ledger was opened before the deploy and closed on the read-back. No rollback fired, and no S3 object was deleted. rk-95 has no live surface.

## 2. For the grade

1. **rk-94 fixed Z-S215 and exposed Z-S216 (ARMED, owned by the CTO).**
   - The print route now renders, but takes 15-17 s warm against a hard 29 s ceiling.
   - CloudWatch REPORTs hit 29,000 ms at 08:13:32Z and 08:14:30Z.
   - The CTO pre-ruled the fix for round 24 (msg 24168): measure, then fix the dominant term. This seat measured it: render CPU is 70-75% of the time, and the cold cost falls inside the first print rather than in Init.
   - The CTO accepted rk-97 (memory 512 -> 1769) as drafted (msg 24170) and will sign its half at round 24's cut.
2. **Z-S217 (the layer's stripped .pyc) and Z-S218 (a pypdf extraction whose result is discarded) are INERT, owned by the CTO.** They were filed at the CTO's request @`5816e85978`. Each becomes a cell only if rk-97 misses a target. The pypdf removal also rides chain G's first adapter cell regardless.
3. **rk-94 row W94-S1:** AC5's literal script hit an uninitialised terraform worktree (a fresh worktree needs `terraform init`). The worker worked around it and the ledger was unaffected. This is an issuer-text defect of this seat's, the same class as rk-90's. The lesson is carried into rk-97's brief.
4. **rk-95 row W95-S1:** the order's a-priori `arms old 106 new 106` read 100, because the comparator's regex skips 6 pre-existing arms whose verdict word is not PASS or DENY. That is also an issuer-text defect of this seat's. The substance holds on the order's own comparator, and item 1's wider-regex instrument above covers the 6 skipped arms. REC: dismiss it, and widen the regex only if GATE 5 is edited again.

## 3. Rows (this round)

| row | disposition |
|---|---|
| Z-S209 | the fix is merged; for L9 to disarm on rk-95 |
| Z-S215 | the fix is merged; for L9 to disarm on rk-94 |
| **Z-S216** | **ARMED**, owned by the CTO; round 24's rk-97 |
| Z-S217, Z-S218 | INERT, owned by the CTO; see s.2 item 2 |
| W94-S1, W95-S1 | OBSERVATION; issuer-text defects of this seat's |
| W88-S1 | still OPEN, owned by this seat: the SERP wiring must use max_pages=1 or refuse |

## 4. What this seat asks of L9/L10

- Grade the 2 terminal cells on their branch-HEAD criteria. Neither carries a judgment criterion.
- **Round 24 candidates, both already drafted:**
  - rk-96: the NaN refusal on the silver and filings copies. This seat's L5 ruling is REFUSE, never map, and it includes `filings.py:183`.
  - rk-97: the memory lever for Z-S216. The CTO signs its half at the cut.
- The backfill cells (B1..B5) are added only when Andrew's per-use word is on file.
