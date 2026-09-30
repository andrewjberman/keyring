# NFRA_MCPMSP -- ROUND 1 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-30 ~22:1xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 27394; `surprise-channel/remediations/REMEDIATION_v1.Z.md` with
`ADJUDICATION_v1.Z.md` @3d96e360a6). Round 1 was issued and drained by `2.0.0_SA_COO~MS` (drain-end read msg 27219,
10 of 10 terminal @1fe1ef07b3). The spec is PRD v0.4 @7ecc812be5 (hop 0 struck; A1 PARKED, owner Andrew, gating no
round, on Andrew-direct ~17:45Z). **The recut is `2.0.0_SA_COO~MS`'s, in ONE issuance.** Grade tokens:
`REALIZED | NOT_REALIZED | HELD` (HELD names its gate).

---

## 1. L7, L8 and L9 accepted

- **L7:** 10 of 10 orders complete and drained. WORLD cells: MS-a-1, MS-a-2, MS-d-1, MS-a-3, with every ledger closed.
- **L8:** 18 of 18 rows dispositioned: 11 dismissed on HEAD re-reads, 7 graduated to REMEDIATION_v1.Z, all OPEN and
  all INERT (section 3 rules each).
- **L9: VACUOUS, cause named.** 0 judgment criteria were cut, and the only judgment-shaped act (A1) is PARKED by v0.4.
  Rule J applies to round 2 (section 4).

**What round 1 built** (from the orders' drained status lines and commits, not from status prose):
- the tenant registry and firm-role path in the gateway (`tenant_registry.py`, `firm_role.py`, `asker_scope.py`,
  MS-t-1) and the owner-gated tenants route (`admin_tenants.py`, MS-t-5), served LIVE by the narrow release MS-d-1
  (AC3: `/health` 200, all three modules match, one `FIRM_ROLE_ARNS` line);
- `gateway-inf-firm-reader-role`, applied (MS-a-1: 3 added, 0 changed, 0 destroyed);
- the grant writer's `register_tenant` op, applied with `LIVE_FIRMS` absent (MS-w-1, MS-a-2: live code == HEAD);
- the MSP harness files and the run-record shipper in `opal_ai` (MS-t-3, MS-t-4), and the `Opal_MSP` account,
  provisioned, with Andrew's boundary run reading DENIED-OK (MS-a-3).

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 (an Inflection advisor answered in Teams) | HELD -- A1 PARKED (G-USER, G-IT-INF, G-ADVISOR, G-FIRM; owner Andrew; PRD v0.4) | Hops 1-4 are built and the gateway half is served. A1n arms 1-3 are EXERCISED BY IAM SIMULATION only (MS-a-1 AC2/AC3: own prefix allowed; Cottonwood's prefix and bucket denied; the gateway role denied both firm buckets), not by live reads. Arm 4 (unregistered tenant refused and logged) is exercised in MS-t-1's tests only. |
| FWD-2 (Cottonwood, and isolation) | NOT_REALIZED | Behind item E1 (the portal-v2 zero-read MUST land before a second firm, C5), then G-IT-COT and G-FIRM. |
| FWD-3 (outside domains get no reply, and are logged) | NOT_REALIZED | Only the unknown-tenant refusal exists, in code; the domain half and the opalinvest/49financial pilot-refusal path are item E2. |
| FWD-4 (refused, then one approval lets them in) | NOT_REALIZED | `register_tenant` and the tenants route are live, with `LIVE_FIRMS` empty. Not exercised. |
| FWD-5 (replay any conversation) | NOT_REALIZED | The shipper is built and there is no run to replay. Item E4. |
| FWD-6, FWD-7 (daily sample, daily page) | NOT_REALIZED | Need runs; after E4. |
| FWD-8 (firm stop, separate capped spend) | HELD -- G-KEY (Andrew) | No per-firm key exists. |
| FWD-9, FWD-10, FWD-11 (production bot, partner ceiling, go-live bar) | NOT_REALIZED | Production enrichment; not this round. |

0 REALIZED, 2 HELD, 9 NOT_REALIZED (denominator 11).

## 3. Rulings on the 7 OPEN remediation rows

- **R-1 Z-S2 (C5's `opal-data-inf` carrier; this seat's).** No cell reads `opal-data-inf` in round 2: every figure
  FWD-1 answers from is served under `opal-data-portal-v2` (C5 v0.2), and YAGNI holds the firm-bucket read until an
  outcome needs it. The row stays OPEN, parked on "a cell that reads the firm bucket is proposed". That proposal
  carries either an LGIC registry route that yields the routed bucket, or an R20 departure Andrew acknowledges.
  Andrew's 13:0xZ naming exception does not cover it.
- **R-2 Z-W2-S3 (safe-apply ignores `-target`).** Gate owner: laptop `1.0.0_SA_CTO` (LGIC_ENFORCE). Routed by relay
  through `0.0.0_AB_MSTR~Z` this turn. Not cut here.
- **R-3 Z-W3-S2 (grant writer stages CRLF working-tree bytes).** Owner `2.0.0_SA_COO~O` (NFRA_MCPORTAL writer). Its
  remedy is `git show HEAD:` staging in `build_package.py`. Not cut here: the writer's paths are NFRA_MCPORTAL's.
- **R-4 Z-W1-S7 (release tree carries the wrong mcportal pin) and R-5 Z-W1-S8 (tests dirty tracked `audit.jsonl`).**
  This seat's gateway tooling. CUT as round 2's batch repair cell E5, subject to the sibling-path check at the cut.
- **R-6 Z-W4-S1 / Z-W4-S2 (opal_ai DEV unpublished; Andrew's AC2 run).** G-PUSH, `0.0.0_AB_MSTR~Z` on Andrew's word,
  then the gitlink bump. Andrew's AC2 run as `Opal_MSP` can use the operator launch recipe proven today for
  `Opal_Agent` (a Medium-integrity shell, then .NET `Process.Start` as the account;
  `C:\Users\Opal Bloomberg\.opal_runtime\G-ACCT_STEP6_RESULT_20260930.md`). `Start-Process -Credential` gives a
  window that does not take typing.

## 4. THE ENRICHMENT LIST ROUND 2 CUTS

Cut order (every item is buildable and provable on demand without A1's external gates):

1. **E1, the gateway identity's `opal-data-portal-v2` zero-read (C5 v0.3):** an Opal-internal reader role for
   internal askers, then an explicit Deny on firm prefixes for the gateway identity. It moves who reads, so it runs
   under never-widen sign-off with DELTA=0 measured on the internal Analyst's and `/query/v0`'s served answers. It MUST
   land before any second firm (Andrew's "Yes, rec approved").
2. **E2, the sender gate in full (C3, FWD-3):**
   - the domain half, at both the agent and the gateway;
   - guest-form addresses refused;
   - `opalinvest.com` and `49financial.com` senders take the refusal-and-log path for the pilot firm scope;
   - the C4 refusal-log fields, without the message text.
   Exercised live on demand with an Opal-domain sender, which is a real refused message without an outside account.
3. **E3, the onboarding queue minimum (FWD-4):** list the refusal entries; one approval through NFRA_MCPORTAL's
   Entitlements writer creates the grant and, for a firm's first writer, the tenant row. The view is MCPORTAL's; this
   project supplies the entries and the approval op's inputs.
4. **E4, one replayable run (FWD-5):** an Opal operator puts one question to the supervised `Opal_MSP` session
   directly, the shipper stores the run, and a second seat reconstructs it from the record alone. This needs no
   partner, and its launch uses the typeable recipe (R-6).
5. **E5, the batch repair cell:** R-4 (the release tree checks out the manifest's `mcportal_commit`, or the gitlink
   is bumped) and R-5 (suites write audit to a temp path). Cut only if no sibling round holds
   `deploy-to-ec2.sh` or the gateway `tests/` at the cut (PRD sequencing rule); otherwise it waits one round.

**Deliberately NOT in round 2:**
- FWD-2/Cottonwood: behind E1, G-IT-COT and G-FIRM.
- FWD-6 and FWD-7: they need E4's record first.
- FWD-8: G-KEY.
- FWD-9..11: production.
- R-1: parked.
- **The launcher fix** (`opal_ai/opal/runtime/launcher.ps1` defects 5 and 6: jq on PATH, and `Start-Process
  -Credential`). It is shared with NFRA_OPALAI and cut ONCE, there. Round 2 writes no launcher path.

**Rule J (at least one JUDGMENT criterion on a WORLD cell, graded at L9, never self-graded)** sits on E1's release.
`3.0.0_SA_CVO~O` reads a fixed set of firm questions answered by the internal Analyst and `/query/v0` before and after
the Deny, and judges whether each served figure, date and coverage is unchanged. A second one sits on E2's live arm:
the CVO judges from the refusal-log entry and the absent reply that the refusal came from the gate, not from the
Analyst declining. COST one criterion per cell; NON-APPLICATION a cell touching no served answer.

**Standing on every round-2 face:** every gateway release is NARROW from the current deployed commit, re-read at the
cut (live 42c52ed4d9, 2.0.0_SA_COO~MI msg 27331). No gateway cell shares a round with an NFRA_OPALAI, NFRA_MCPORTAL
or NFRA_MCPINDEX gateway cell on overlapping paths.

## 5. What this analysis does not do

- It does not un-park A1. That is Andrew's, on G-USER, G-IT-INF, G-ADVISOR and G-FIRM.
- It does not cut the launcher fix (NFRA_OPALAI's), R-2 (laptop gate owner's) or R-3 (NFRA_MCPORTAL's).
- It writes no remediation row. The CVO dispositions R-1..R-6 at the round-2 L8.
