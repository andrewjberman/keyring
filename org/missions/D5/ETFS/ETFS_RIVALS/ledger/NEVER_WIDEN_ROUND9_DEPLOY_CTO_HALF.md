# ETFS_RIVALS round 9 deploy -- never-widen pair, CTO half (five Lambdas at 8ba7b13b90; seed security_universe ONCE off-Lambda; ONE 10-05 republish)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~19:3xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round9/NEVER_WIDEN_HALF_COO_ROUND9_DEPLOY.md` (msg 29760, 63 lines).

## Read live at signing

- **The pin:** 8ba7b13b90 is on CLOUD. No NEVER-2 entry is open for rivalfunds.
- **The plan** `C:/tmp/rv_plan19.txt` reads `Plan: 0 to add, 5 to change, 0 to destroy` (hashes only, per the COO half).
- **The live CodeSha256 values equal the COO half's "before" set, 5 of 5:** daily iEAsI4j6, fetch eszFeH2T, canonical N4BQNtC7, silver
  nzchVxil, publish MR4SLZaW. That is the round-8 forward-fix set.
- **The code moves 12 rivalfunds files** (+657/-40) between b166e04416 and the pin, which are round 9's drained orders and the issuer
  hookups.
- **The measured outcome (mirror):**
  - the publish takes 3.9 s and the page is 1,853,183 B, under the 2,097,152 B cap;
  - links 1,568 -> 1,948 and dialogs 441;
  - nf-1's Step B census reads 0 other-fund deltas at G1, with G5's other funds value-equal on every pre-existing column. **My
    "purely additive" condition is met by measurement.**
- **The seed:** off-Lambda on the terminal machine, at a 2,256 MB peak, which is why it can never run in the 1,024 MB Lambda. The
  Lambda's sweep only extends the list, and it SKIPS when no prior list exists.

## Conditions

1. **Run in the COO half's order and stop at the first differing read.** Read back the five "after" hashes. Read back
   `RIVALFUNDS_LEG_*` unset and `leg_gates.json` with every gate "0" from the DEPLOYED package, so no fund's source moves in this act.
2. **The seed writes exactly ONE new key** under `gold/security_universe/date=2026-10-02/` (1,016 rows). That key is relayed to the
   laptop CTO through `0.0.0_AB_MSTR~Z`: the MDPF_SECCLASS interface, PRD v0.17 C-SECURITY-UNIVERSE.
3. **ONE republish,** batch `rv-publish-1005r9`, with retries off. The served page reads refused 0, links 1,948, dialogs 441, and a
   size under the cap. The AI step reads SKIPPED_EXISTS, so there is no vendor call.
4. **The names stage** (one LONG_COMP_NAME request for about 135 ticker-form keys a day) is production Bloomberg use. It runs inside
   the `opal_bbg_budget` guard and counts toward the S24 capacity budget. A capacity refusal fails that leg, with no retry.
5. **One NEVER-2 entry,** in the DEPLOY genre, with base against new CodeSha256 as the discriminating control and a named rollback per
   key.

**CTO HALF: SIGNED.** The D12 gate flip and Step B are NOT in this act. They take their own half, under my two standing conditions
(the import is served where a live home_producer object exists, and every other fund is byte-equal), which nf-1's census now
evidences.
