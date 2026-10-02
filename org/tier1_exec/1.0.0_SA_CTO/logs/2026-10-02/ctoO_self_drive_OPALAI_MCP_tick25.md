# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 25 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** the inter-tick acts 02:3xZ-03:2xZ, and tick 25 (03:23Z). Cron 84d0ab03.
**state:** ARMED

## Since tick 24

1. **8194 WFP wall: DONE.**
   - Andrew ran `wall-dapi-8194-wfp.ps1` elevated (~22:25 local; `C:\opal-elev\wfp_8194_run.txt`).
     - The permit scan found 3 loopback-permit sublayers at 0x0002, 0x0004 and 0x0007, all below 0xFFFF.
     - VERIFY: both filters OK; sublayer FAIL; exit 4, so step (d) did not run.
   - This seat signed the Terminal in: 1 attempt, ledger 28; SPY 763.99, a real read.
   - **AC3** (@52640d92c7): Opal_Agent and Opal_MSP read 8194 REFUSED and 8790 OPEN; the operator reads 8194 OPEN.
   - CTO position (msg 031045Z): grade on behavior plus the filter VERIFYs; the sublayer line is a read-back defect,
     filed as a row; persistence is read at the next natural reboot.
   - `2.0.0_SA_COO~AI` **closed OA-f-11 @3f534f490a** (AC3 PASS on the amended apply limb).
   - **R3 met: the item-0 close run un-holds.** Andrew was told he may sign the Terminal out.
2. **CVO verdict 28159** (@ba8deeb52a, ledger row 2): CONCUR on one audited override commit by this seat, after
   G1 (D9 members still list both) and G2 (restore 10 rewritten `path@sha` pins: my path class admitted `@`), with
   G5 (land before either issuance).
   - **G5 is not met this boundary.** MCPINDEX round 7 issued into D9 @9108f11494 at 02:40Z, after my 02:25Z release
     and before the verdict.
   - **Ruled:** the move is DEFERRED to the next JOINT round boundary. It will be rebuilt from that HEAD with G1 and G2
     applied, and announced first.
   - I do not re-litigate the verdict; this is its timing condition, read literally.
3. **The OPLGTW walkthrough principal was corrected** (COO~O 28153). My 28152 (Menachem, one sitting) conflicted with
   Andrew-direct 9/28 Call 1: Menachem is deferred, and Alyssa tests with his G-E grant after Andrew's own speed and
   efficacy tests.
   - Corrected (reply 20261002T023358Z): the principal is **Alyssa**. The G-C no-test-user retirement stands.
   - The FWD-3 denial arms are graded on her ONLY if the entitlement guard evaluates a WRITE_CAPABLE session's grant
     (measured at `3a7d6a7dc8`, plus one ungranted-master probe). Otherwise they are carried UNEXERCISED.
4. **Notice** (MSTR~Z 28172): the laptop adds `outlook-global-transcripts-pull-role`, reading `gateway/mail/bearer`,
   and a daily /hx/mail pull inside C7's caps. It is not applied. If it touches OPLGTW's secret policy or Terraform,
   it wants this seat's read first.

## Calls

No open calls in scope OPALAI_MCP_SITEZ (tick 25). The rulings above were closed as they arrived.

## Acts only Andrew can perform (each with its citation)

1. **Sign the Bloomberg Terminal out** (his bandwidth choice: "i had turned it off to save bandwidth").
2. **His own speed and efficacy tests, then Alyssa's OPLGTW walkthrough** (Andrew-direct 9/28 Call 1).
3. **The Alyssa sitting for MCPINDEX r6.J1 plus MCPORTAL G-CLOSE.**
4. **opal_ai DEV fast-forward** fd8ab8a -> 9c0a80b. REC: approve.
5. **G-W:** the R20 acknowledgement for `platinum/advi`.
6. **An invitation to the Research Team Meeting series.**
7. **Re-authorize the operator upload client** before 2026-10-15.
- **Done:** the 8194 WFP elevated run.

## Completion test

NOT DONE: 0 of 5 complete.
- REACHABLE 3:
  - OPLGTW (issuing r13 items 2-7);
  - MCPINDEX (round 7 executing);
  - **OPALAI (newly reachable: the close run un-held).**
- UNREACHABLE 2: MCPMSP and MCPORTAL, both PARKED.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| python | read `wfp_8194_run.txt` (utf-16) | 3 permits below 0xFFFF; 2 of 3 VERIFY OK | the tee wrote UTF-16 |
| bbg_signin | fill (screenshot verified), then submit | 1 attempt; SPY 763.99 | |
| git log | in-scope commits since 02:45Z | OA-f-11 closed @3f534f490a | |
