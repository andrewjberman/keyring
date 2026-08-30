# /self-drive D2 & D3 — tick 87 (2026-08-30 12:52Z; fires 87–91 coalesced) — state: ARMED

Covers the inter-tick acts since the tick-86 log (`9af48e0566`, LOCAL; origin @`416a116c8b` unchanged since the
09:36Z CLOSE — ls-remote read 12:52Z) and five cron fires (`1c261f82`, :07/:37) that landed during a laptop-side
session pause 10:00–12:52Z, folded into ONE tick per MSTR's ruling on ticks 79–81. The fabric was quiet in the
pause: 3 inbox files (09:59Z ×2, 12:52Z). Paired `/drive D2 & D3 @ 2.0.0_SA_COO` (its tick 15 @`b4c9e8ae83`).

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete). Open TOs **24** (D2 20 + D3 4; +1 since tick 86:
`ADVI_49F.c02-ENUMERATOR`, cell C02-g-9, cut at `0.7.0_AE_CloudOps~L` @`e646e3b9e9` LOCAL — 87264). Ledger
**19 / 0 unconsumed**. Acked READ this stretch: 87210, 87215, 87225, 87234, 87250, 87256, 87257, 87264, 87267,
87274, 87277.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 5** (R1–R5 unchanged; R2 = W1/W2 at Andrew via MSTR on 6a99820c40). No pitch.

## Verdicts since the tick-86 log (§3)

**0 on pitched calls.** Rulings read: **COO 87225** — the dispatch billing row retires ONLY on a same-day,
two-writer arm A CONTENT-EQUAL on billing (shape (i)); a pre-retirement single-writer day is a FINDING, the row
stays, the read repeats. **COO~X 87277** — surprise 2 DISARMED at (i): the portal graph gets a content-addressed
carrier (row 0 of AE~Y's declaration unit, sha256 `ba5d7dd5…db27b` checked at the pin, a CUSTODIAN named — the
gate's clause adopted), rows 1–4 certified over that pin; the stitch sibling stays with `0.7.0_AE_CloudOps`.

## Driver's own acts (tick 86 → 87)

1. **The two-arm read's frame COMPLETED before the fire** (87217, 87220): DS~V's three N/A conditions accepted
   with three scoring sharpenings — arm B still binds under single-writer and a pre-retirement single-writer day
   is a finding; the value limb on the ACCOUNT-KEY INTERSECTION with its denominator, a cross-date value limb
   informational, the column delta binding; "before the apply" read from LastModified vs the chain log's start
   line. On the CVO's consequence (87215: 86649's retirement condition unmet under N/A) the gate's REC was (i) —
   arm B never compares the chain to the writer being retired — and the issuer ruled (i) (87225).
2. **The gate's own "by definition" phrase WITHDRAWN** (87269): DS~V MEASURED date-invariance (08-28 vs 08-29:
   911/911/911, 17 cols, 3 moved / 13 identical) and declared the one-period trap; three classes stand
   (DATE-VARYING reported; PERIOD-VARYING scored only if the pair shares a period, TESTED; REFERENCE scored). The
   definitional read is owed LAZILY per mismatching column; a REFERENCE mismatch prints INFORMATIONAL first
   (the same one-pair trap).
3. **The gate's 86979 reading WITHDRAWN at source** (87287): the c02 refusal appends
   (`c02_twr_engine.py:224/:232/:253/:257 @ac7792ac50`) carry NO `bmv` (0 of 4, the gate's own grep), the OK
   append `:275` does, and two tests pin BOTH shapes (`:208` all-refused omits the operand columns; the next pins
   the mixed partition's NULL operands). The operand is ABSENT by contract, the NaN is the frame union's; **no
   C02-g-5 amendment**; the tick-85 observation closes as EXPECTED SHAPE. DS~N's other three lines accepted:
   a07:352/:500 a BYPASS defect (hand-rolled stamp, not `rc.stamp_provenance`) → its own cell as 86729 placed;
   a04:44-46 by design; c04's `anomalous_return_census` NOT WIRED is deliberate and disclosed — **owner
   `1.0.0_SA_CTO`**, sequenced after the D-1 mirror remedy, on the gate's remediation list from this tick.
4. **Surprise channel (sec-7b, out of D2/D3 scope; gate acts):** surprise 1 — the carrier finding's owner NAMED
   by git read (`rectangle.c0.json @5f551f70ec` = `2.0.0_SA_COO~X`, `.owned-paths` cited at `:83/:329`; 87236).
   Surprise 2 — the gate's line under Rule 28 (87260): REC (i) because a sha on a gitignored file has no
   custodian; if (ii), the row names the holding device and its expiry. AE~Y's full sha and the scope note
   (CVO's and AE~Y's reads are ONE measurement of ONE copy) on the channel (87274); COO~X cut (i) with the
   custody clause (87277).
5. **COO's drive tick 15** (87250): DS~N's four source lines un-sequenced from M-4 — agreed, no act.

## In motion, not mine

AE base's (v)/(vi) on the inf-silver-chain APPLY word (87206, given at tick 86; no report yet); the CVO's grade
of (iv)–(vi); **M-4 — the 12:45Z fire's a06 line read by DS~N from the S3 chain log at ~12:50Z (due now)**;
DS~V's two-arm read after the first post-deploy fire; AE~L's C02-g-9 (E-1/E-2 to the gate first); Andrew's word
on W1/W2 via MSTR; S1e at the next 04:35Z fire; the next window carries `9af48e0566`, `eb0694d45b`,
`dbbbfb89b2`, `bc42f4d35b`, `e646e3b9e9`, `b4c9e8ae83`, this log.

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`directives-check.py --json`, the ledger count, inbox listing by timestamp (the pause census: 3 files); `git show`
+ `grep` on the c02 append lines and the two test bodies @ac7792ac50 (the gate's own instrument for the 86979
withdrawal); `git show --format=%an` for the rectangle's author; `ls-remote` for origin. No comp-find, no
comp-state.

state: ARMED · next log at a verdict or tick 93 (floor)
