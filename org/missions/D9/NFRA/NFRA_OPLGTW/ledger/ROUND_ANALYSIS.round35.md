# NFRA_OPLGTW -- ROUND-35 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-13 ~14:4xZ. **Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33649,
`remediations/REMEDIATION_v18.md` @e3df1c8b49. L8: `ADJUDICATION_v26.Z.md`. **Issuer:** `2.0.0_SA_COO~O`.

**Standing (Andrew-direct 2026-10-12 ~20:5xZ, item 2):** the project stays OPEN until Andrew has read the gateway
breakdown, which is NFRA_MCPORTAL FWD-20 and is being built now (record
`ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md`). This analysis cuts what is owed, nothing beyond it.

## 1. Round 35, as read

MAY-CLOSE. The CVO re-read three rows live and all three are met:
- **Z-S97:** the DLQ policy has `ChangeMessageVisibility`, and the 10-13 sweep ran with 0 errors.
- **Z-W55-S2:** the host's `site_to_s3.py` equals `d9f2ebded9`.
- **Z-S92:** the dell1 simulate on the teams bearer reads implicitDeny.

**Z-S91 is met for schwab only**: four families still drain the whole DLQ, which holds 12 messages. Seven rows are dismissed;
Z-S95 and Z-S100 graduate. From round 33, OG-tl-1 passes, bounded. OG-rl-16 stays ungradable because no `fee_statement`
object exists, and it stays dell2's debt.

## 2. Rulings

| item | ruling | cell |
|---|---|---|
| **OG-bd-1 re-cut, on Andrew's YES** (record `ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_..._CTLPLN_SCOPE.md` row 3, "Yes that is fine"). COO~O msg 33650 measured two facts: (i) caller `fc9aed2e22` (standard, 1 call, already DENIED by the tool's gate) has NO principal, 0 of 255,023 lake records; (ii) the only profile kind is `restricted`, and a restricted profile CONFINES its holder on the data-grant family (`data_entitlement.py` decide(), :448-470), so a profile on master_admin `2cdb43ed4d` would narrow its Schwab reach | **(b) for the master_admin, plus (c) for the unlinked caller.** Andrew's outcome is: the real callers keep their access, and an unknown principal no longer reaches client fee data. A restricted profile on master_admin would cut its Schwab access, which he did not approve, so do not profile it. The deny names `master_admin` tier as an admitted class for `blackdiamond_list_fees`; that is the existing admin tier, not a new grant. The unlinked standard caller cannot be admitted (it has no principal) and is ALREADY denied, so it loses nothing it has; it can be admitted by profile the day it signs in under a principal. Then ship the deny for unprofiled, non-master_admin principals. Grade: a simulate or replay of the master_admin caller reads ALLOWED; a planted unprofiled standard principal reads DENIED; the real unlinked caller reads DENIED, as today | **E1** |
| **Z-S91, the remaining four families** (etf, smartx, orion, bd49finsurance / eclipse / blackdiamond, as deployed) | Port the schwab per-family drain (OG-fd-1's rule) to each remaining family, one release per family or one shared release. Each family keeps only its own messages and returns the rest. The grant is already in place (OG-ap-12) | **E2** |
| **Z-S100**: the sweep's DLQ drain report is a discarded return value | `run_sweep` writes its drain dict into backfill-status for every family, so a drain is readable after the fact. Folds into E2's code | **E2** |
| **Z-S95**: `/hx/teams/channels/.../messages` answers 502 about 2 in 1440 polls, cause unread | **READ first:** the gateway's error body for each 502 (route, Graph status, throttling or timeout). Fix it if it is the gateway's; name it as upstream if not. No retry layer until the cause is read | **E3** |
| **dell2's OneDrive asks** (CTO~DELL2 msg 6905, on Andrew's card 3; row NFRA_TRNSPT-D2-S29; laptop relay 33502) | **One tool, two needs.** A gateway tool that takes a sharing URL and resolves it via Graph `/shares/u!<b64>/driveItem`, then lists children and reads content. It is READ class and reaches only what is shared to the signed-in user. It also gives D2-S29's search miss a listing path; the interim stands (no consumer reads a search zero as absence). With it, ONE read: the gateway request log for 2026-09-29 filtered on the 06-01 meeting's id, with the result to `1.0.0_SA_CTO~DELL2` | **E4** |

## 3. ROUND 36 -- cut in ONE issuance

E1 (BD-fee deny, master_admin admitted by tier, the unlinked caller stays denied), E2 (per-family drain for the remaining
families, plus the drain record), E3 (the 502 read), E4 (the sharing-URL tool and the 09-29 log read). Every WORLD cell
carries its never-widen pair.

-- 1.0.0_SA_CTO~Z
