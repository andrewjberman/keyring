# CTO ROUND-198 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- per-firm pins: each firm moves by the cash rule only (2026-10-15 ~01:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `2.0.0_SA_COO~P2` msg 7909 and the round-197 drain-end
`deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_197_P_DRAIN_END_20261015.md` (commit 0ca19670e2), row D2-S178. **No PRD addendum.**

## 1. What round 197 found

The revert pin `5fad7eaaa8` (b1d354cfc9 with the CUSIP port reverted) moves 49 Financial by **119**, not the expected 32. Cause (D2-S178):
**the live 49 Financial `holdings_snapshot.py` already carries the CUSIP port.** The live file equals b1d354cfc9 minus the 40 signed cash-rule
lines. Reverting the port for 49 Financial would remove behaviour that is already serving: a regression, not a hold-back.

## 2. Ruling: per-firm pins, YES

**The principle stays round 197's: each firm's release moves its served output by the signed cash rule ONLY.** The pin that does that
differs by firm because the live bytes differ by firm (W383-S3):

| firm | pin | moved by | expected count |
|---|---|---|---|
| 49 Financial | `b1d354cfc9` (port kept: it is already live there) | the cash rule | 32 |
| Cottonwood | `5fad7eaaa8` (port reverted: not live there) | the cash rule | 255 |
| Inflection | `5fad7eaaa8` | the cash rule | 841 |

**Conditions:**
1. **Each firm's bundle is ONE commit's bytes** (CLAUDE.md 22a). The built-bundle differential for each firm against its own live bundle
   reproduces the counts above. Every change attributes to the cash rule; an UNATTRIBUTED change is a STOP.
2. **The per-firm divergence is a named, temporary fork, not a standing one** (Andrew: "identical naming structure and operations per
   firm"). It is recorded in packet v3 and closed by the CUSIP port's own release, which brings Cottonwood and Inflection to the port after
   the read of the 45 absent Cottonwood sub-class values. That release's pair names the reconvergence as its goal.
3. **Packet v3** carries the per-firm pin table and the three differentials. Both halves sign, then the apply runs per firm under round 193's
   business-date rule and the manifest-anchor rule.

-- 1.0.0_SA_CTO~DELL2
