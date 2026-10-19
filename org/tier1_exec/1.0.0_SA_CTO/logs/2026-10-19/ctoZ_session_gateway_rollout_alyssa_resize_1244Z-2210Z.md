# 1.0.0_SA_CTO~Z -- session log: gateway rollout, Alyssa's Schwab session, the gateway hang and the t4g.large resize (2026-10-19 12:44Z-22:1xZ)

**archetype:** COORDINATE

Fresh session; zero crons (launch word). The `/self-drive 30m` live row (LIVE_ARMS.md:193) was NOT re-armed. Andrew was told
and has not asked for it.

## Andrew-direct records (all committed, verbatim)

| Time | Record | Summary |
|---|---|---|
| ~14:1xZ | `ANDREW_DIRECT_20261019_141xZ_GATEWAY_INDEXED_ALL_MCPORTAL_SURFACES_TOOLS_TESTED_PER_EMPLOYEE_CHEAT_SHEETS.md` @4a337dec2e | index every /gateway surface; test every tool; a cheat sheet per employee |
| ~17:2xZ | `..._172xZ_ALYSSA_3PM_SCHWAB_TEST_SENDS_YES_ROSTER_AS_OPEN_CALLS_SCHWAB_FULL_ACCOUNTS.md` @65a05f6658 | Alyssa at 3p; test sends yes (c5c2); roster as open calls; Schwab covers the full accounts |
| ~17:5xZ | `..._175xZ_ROSTER_OPEN_CALLS_YES_TO_RECS_SCRATCH_NO_REC_WIDENINGS.md` @50bd4a33b4 | yes to the six recs; 3599 and 7a80 scratched |
| ~18:3xZ | `..._183xZ_GATEWAY_EC2_RESIZE_TO_T4G_LARGE.md` @439343a969 | "lets raise it to large" |
| relayed | laptop `..._163xZ_SIX_HANGING_OPEN_CALLS_RESOLVED.md` and MSTR `..._195xZ_ALYSSA_SCHWAB_MASTER_0840_ADD_TO_ENTITLEMENTS.md` | f0d2/8ed7/def4/5b35 closed; 0840 for Alyssa |

## Acts

- **BBG daily pull:** I landed the BBG seat's fixes.
  - `scheduled_daily_pull.cmd` @805203d2b5 (rc 50 and UNVERIFIED reach the legs).
  - `dapi_check.py` @dce8dec408 (IMPORT-BLOCKED).
  - ETFS_POSITIONING Z-S22 @ef1d325510 and Z-S23 @65eed07b46: Z-S17 disarmed; the R-21 self-report recorded.
- **NFRA_MCPINDEX:**
  - PRD v0.18 (FWD-23, FWD-24, FWD-25) and v0.19 (the routing arm): each was refused once and cured. ADMITTED @4b8dcf3b86 and
    @7c42c0c743.
  - The round-22 analysis @44e6950a24, with A1 @848752f570 correcting the census to 14 channels and 127 tools.
- **Audit routing:** `CTO_RULING_GATEWAY_ASSETS_AUDIT_DEFECT_ROUTING_20261019_Z.md` covers parts 1-3 (@473f5177a8,
  @944f324225, @9e74fee971).
  - D1-D3, P4-P7, Y1/Y2/R1/T1 and H2 go to NFRA_OPLGTW round 47.
  - P1 goes to NFRA_MCPORTAL; P2 and the routing mismatches go to NFRA_MCPINDEX.
- **NFRA_MCPORTAL:** the z-round-1 analysis @11c572fef9 (P1 display; the CVO re-grades from its own served read).
- **Never-widen CTO halves:** OG-ap-50 @10285a7d35; OG-mg-2 (b) @48c508a3d8; OG-rz-2 @f39cd21642; OG-ms-2 @355bf20473. All four
  carry three signatures.
- **Open calls:**
  - c5c2 closed by Andrew.
  - Eight roster calls added and then closed on his word.
  - 88af added; it said "email", which is wrong. Corrected as 0c28 (Teams asker), held. 88af and a485 cannot be closed alone
    (CROSS-BOX).
- **Alyssa's 3p session:** a test plan PDF on the Desktop, sent by Taildrop to cloud-local (off git). Her grant moved to the
  current accounts at 18:58Z.

## Incident: the gateway hang, ~17:30Z-18:26Z

- The service hit its cgroup memory limit on t4g.small. The load was concurrent battery and audit calls, including uncapped
  replies of 743 KB and 585 KB.
- My direct order to `~NFRA1` was REFUSED by the broker (LD-0529: a Tier-2 seat acts only on a task order). COO~O cut OG-rs-1,
  but `~NFRA1` was mid-turn and did not read it (OFFER-EXHAUSTED).
- MSTR~Z restarted the service via SSM, with a ledger entry: /health 200 at 18:26Z.
- The fix is in hand: the t4g.large resize plus the 6400M cap (OG-rz-2, window 2026-10-20 06:00-06:45Z). Size caps P4-P7 are in
  round 47.

## Owed / next

- 06:03Z: COO~O's one-shot GO for OG-rz-2. It dies if that session ends; Andrew was asked whether this seat sets a fallback at
  05:55Z (unanswered).
- OG-ms-2 Phase B follows the batch15 CLOSED.
- MCPINDEX round 23 (assets first); OPLGTW round 47; OG-ev-13 no earlier than 2026-10-20 07:45Z.
- Open at Andrew: 0c28 (Cottonwood's tenant for the Teams agent).

## Compiler Tools

| tool | used for | result |
|---|---|---|
| comp-find | gateway code (asker_scope, data_entitlement, MemoryMax, t4g.small) and records | worked; the rail denied piped and blind greps 4 times, and each denial named the right form |
| open-calls.py | add / hold / close / publish | worked; a close of a CROSS-BOX act was refused (correct) |
| prd-signoff.py | status | reads "current" for addenda outside the hashed ENDPOINT section (a known gap; the CVO graded the text by hand) |
| safe-commit.sh | 20+ commits | worked; the surprise-row gate refused one in-place row edit (correct) |
| aws (shim) | instance type, target health | worked |
| msedge --print-to-pdf | the test plan PDF | worked; it could not be read back (no poppler) |
| tailscale file cp | the PDF to cloud-local | exit 0 |

**Gap:** a broker send to a Tier-2 seat in an incident cannot carry an act without a task order. The incident path is MSTR (SSM)
or a COO order, and this seat learned that the slow way.
