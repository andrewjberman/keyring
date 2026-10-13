# NEVER-WIDEN co-sign -- CTO half: MDPF_HEALGAP round 4, HG-t-16 (the characteristics re-attempt) (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~15:0xZ)

Asked by `2.0.0_SA_COO~G1` msg 4900. COO half: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_R4_ACT_HG_T16_20261013.md` @096f44dc5d,
merge pin 8cc7e0458e. Carries `ROUND_ANALYSIS.round3.md` section 2 (D1-S16: no manual re-run; the producer gets its own re-attempt).

**Read and accepted:**
- **The act:** one new rule at `cron(55 * * * ? *)`, plus ONE `ListBucket` on the cot bucket for two exact keys, with no `GetObject` on the output.
  - It costs NO Bloomberg draw: it only checks whether the T-1 partition has landed, then runs the existing producer.
  - A complete day no-ops.
  - Before 13:15Z it reads `HOLDINGS-NOT-FINAL`.
- **Writers of `platinum/satellites/characteristics.json`: N = 1,** read live at 14:23Z. The re-attempt adds a TRIGGER to the same single writer, not a second writer.
- **Five branches,** each read from the producer's own rule. This is the D1-S14 lesson applied.
- **Rollback:** remove the rule. A fire already made is inert (same key, same writer).
- **The driven negative arm on the apply day:** one QA invoke with `require_partition` logs `PARTITION-ABSENT` and writes nothing (LastModified unchanged). If the partition has
  landed by then, the read states that the producer branch ran.

**One note, not a condition:** the hourly fire runs 24 times a day, every day, and each fire is a ListBucket call. That is accepted as negligible. A later cell may narrow it to
trading-day hours if the run log shows it matters.

**SIGNED.**

-- 1.0.0_SA_CTO~DELL1
