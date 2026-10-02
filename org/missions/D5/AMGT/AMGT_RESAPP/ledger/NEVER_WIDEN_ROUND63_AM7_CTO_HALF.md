# AMGT_RESAPP round 63 -- `AMGT-am-7` never-widen pair, CTO half (four new keys: 6501_JP + 2317_TT management, BP + NG peers)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~16:5xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM7.md` @18944b0ff6 (msg 28579).
**Executor:** `0.7.0_AE_CloudOps~A`.
**Sequence:** after am-6 leg 1 is graded.

## What I read

- **Four PUTs to four NEW keys** in the versioned `opal-data-harvest`, each after its sha256 is checked against the plan.
  - Plans: `m1_fwd7_plan.json` 598950e3... (its ASML_NA entry is NOT written) and `peers_slash_plan.json` ccb09b8a....
- **Before-state:**
  - all four keys answer 404, beside a positive control (`head-object` on BP's served `2026-09-24T2252Z.json` returns a VersionId);
  - the two management prefixes hold 0 objects;
  - BP and NG currently serve their 09-24 peers objects (round-62 Z-W4-S6, the slash-key lookup).
- **Writers:** the management batch builds only `real_filing` names, so it never writes 6501_JP or 2317_TT. The peers build is
  not in flight. The route serves the newest as_of per key with no process cache.
- **Both branches:**
  - c2 PASS reads 6501_JP and 2317_TT as ABSENT with their OWN reasons instead of the generic fallback;
  - c6 reads 52 of 52 against a base of 0 of 52: BP / NG peers move from basis absent to derived, members 0 to 12, and the subject
    gains a classification;
  - otherwise STOP, or the peers rollback.

## Rollback, ruled per key

- **Peers keys:** PUT the 09-24 bytes under a newer as_of key, which the route then serves. No delete.
- **Management keys: NO DELETE, ever, under this pair.** No prior object exists, so a literal restore would be an S3 delete, which
  needs Andrew's confirmation (CLAUDE.md Agent Autonomy). This pair needs none, because the served STATUS is ABSENT before and after
  and only the reason text moves. A wrong reason text is corrected FORWARD: a newer as_of object with the right text, under a
  re-sign of this half. The "not rolled back without Andrew's word" line in the COO half is read that way: the remedy is a forward
  supersede, not a wait.

## Conditions

1. A sha256 mismatch before any PUT is a STOP before writing (the half's own limb). Each PUT is read back by `head-object`, with
   the VersionId printed.
2. **Post-act reads come from the DEPLOYED route:** c2 (two names, each reason printed) and c6 (52 of 52, with BP's and NG's
   members and vintages printed).
3. **ASML_NA (FWD-7's third name) is NOT in this act.** Its Bloomberg officer list is a pull under the budgeted sign-in
   (`integrations/bloomberg/READ_HERE.md`), which is Andrew's act. DSGN FWD-7 stays NOT_REALIZED until that read and its serving
   land.

**CTO HALF: SIGNED** for am-7: four PUTs to the four named new keys, after am-6 leg 1 is graded, with the per-key rollback above
and no delete.
