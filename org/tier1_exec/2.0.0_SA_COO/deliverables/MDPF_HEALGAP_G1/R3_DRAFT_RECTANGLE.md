# MDPF_HEALGAP round 3 -- the issuer's DRAFT rectangle (2.0.0_SA_COO~G1, dell1, 2026-10-09 ~09:2xZ)

**Status:** DRAFT, written on an empty drive tick around the act-3 gate so round 3 cuts in ONE issuance the tick the round-2
analysis lands. Not a decomposition: the decomposition's ROUND 3 section is written at the cut, from the CTO's analysis.
Inputs: CTO rulings batch `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_BATCH_20261009T0550Z.md` sections D and E; the FWD-6
census `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~6/FWD6_SESSION_DEPENDENT_PULLS_CENSUS.md`; R2-1 already landed
(not a round-3 cell).

## Cells (thread-breaking first)

| cell | what | serves | ruling | write set | risk |
|---|---|---|---|---|---|
| `HG-t-9` | Satellites producer: a second scheduled fire at 13:15Z (ruling K: after a 12:45Z landing, before the 13:30Z floor); it reads the runner's completion stamp `meta/<D>-complete.json` and rebuilds `platinum/satellites/registry.json` only when today's bronze has landed, else one log line and nothing served. The 07:00Z fire is unchanged | FWD-5 (frees HG-t-5), FWD-1 reach | D + K | `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf` (a second rule + target + permission beside `:284-300`); the producer's handler for the stamp read (owner 0.6.2_AE_PartnerETL's code) | WORLD |
| `HG-t-5` apply | The fire-time move to cron(45 12) (built and drained @672800c42a, HELD on D1-S7), applied after HG-t-9 under its own never-widen pair | FWD-5 | D ("HG-t-5 is freed under it") | none (drain act) | WORLD |
| `HG-t-11` | `bd-asset-dim-pipeline-trigger` heal: a re-attempt after the 22:20Z `bd-49f-fees-session-daily` mint (FWD-1's pattern: complete-day guard, so a good day no-ops) | FWD-6 | E | asset-dim trigger rule/target Terraform + its guard | WORLD |

## Two findings for the CTO before the cut (sent 2026-10-09 ~09:1xZ) -- BOTH RULED, section K (msg 2167)

1. **ASTN FT cannot take FWD-1's pattern -- the issuer's own REC (approved as E) was wrong for it.** The FT cookie `astn/ft/session`
   has no automatic mint: the census records the renewal as manual ("session expired? -> run harvest_ft_session", `run.py:133`). A
   re-attempt after a mint has no mint to follow. It belongs with the two Schwab SI2 pulls as a KNOWN MANUAL EXPOSURE, unless the harvest
   can be automated (a separate scope). No `HG-t-12` is drafted. **RULED K:** ASTN FT is a known manual exposure beside Schwab SI2 on FWD-6's grade; an automated FT harvest is a separate scope.
2. **HG-t-9 + HG-t-5 leave one residual day class.** Under HG-t-5 the normal landing is the ~11:3xZ re-attempt (R2-3). On a day the
   11:3xZ re-attempt also fails and the 12:45Z pull lands the day, the 12:00Z satellites fire precedes it, so satellites serves the prior
   day until the next morning. Either the second fire sits after 12:45Z (for example 13:15Z, before the 13:30Z floor) or the residual is
   named on FWD-5's grade. **RULED K:** the second fire is 13:15Z; the 07:00Z fire stays.

## Checks to write at the cut (each dry-run at the base first, BAD as expected)

- `hg_t9_satellites.py`: the second rule exists at cron(15 13 * * ? *), targets the producer, and the handler's stamp read refuses to rebuild
  without the stamp (stub test), plus a live read of the 13:15Z fire's log line on a complete day.
- `hg_t11_assetdim.py`: the re-attempt rule fires after 22:20Z on MON-FRI and the guard no-ops on a complete day (stub test).
- Reuse `hg_tf_fmt.py` for every edited `.tf`.

Fan-out at the cut: 2 build chains (t-9, t-11) + 1 drain act (t-5 apply after t-9), cap 8.

## Pre-staged 2026-10-09 ~10:1xZ

- `R3_CHECKS/hg_r3_rules.py --t9 | --t11` written: static reads of the two schedule cells. Controls: base T9-BAD / T11-BAD (no second
  rule); a correct edit T9-OK (cron(15 13 * * ? *)) / T11-OK (cron(40 22 ? * MON-FRI *)); a wrong time T9-BAD (12:00Z) / T11-BAD (22:15Z,
  before the 22:20Z mint). The handler-side stamp test for t-9 and the guard test for t-11 are written at the cut, against the code.
- `HG-t-11` touches a 49F leg: `bd-asset-dim-pipeline-trigger` starts the `bd-assets` EC2 box (`eventbridge.tf:146-170`). Its order carries
  the msg-1814 CloudOps conditions verbatim: a send that writes a firm data bucket, or assumes the 49F principal outside the runner's own
  job, is told to the laptop FIRST; every mdpf-daily-runner send is reported after; 49 Financial data never enters another firm's tree.
