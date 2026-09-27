# MX-s-4 closes on step 2 alone, and step 1's REST replacement is measured out of this lane — 0.7.0_AE_CloudOps~I

**archetype:** MIXED

**Date:** 2026-09-27 20:50Z - 22:30Z
**Task Order:** `NFRA_MCPINDEX.TO-MX-s-4.bd-asset-dim-login` (amended A5 @fc2001d2a6)
**Status:** step 2 COMPLETE and world-verified; step 1 amended out; deploy ledger CLOSED

## Objective

Pick up a lane whose predecessor died ~18:0xZ, read the order at HEAD rather than at the amendment
named in the launch prompt, and drive whatever was addressable before tonight's 02:45Z git freeze.
The order arrived carrying amendment A3; HEAD carried A4, which superseded A3's mechanism outright.
Reading the pinned amendment instead of HEAD would have sent this seat to build a token-based login
that A4 had already replaced with a REST pull.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `comp-find 'bd-49f-(fees-)?runner' --band DEF --limit 40` | 2 DEF of 2541 total — collapsed the haystack to the two lines defining the runner names |
| `comp-read` | `comp-read .../field_dictionary.md --enumerate 'Super\|super_class\|superClass\|Alternative\|alternative'` | 16 hits over a printed denominator of 963 lines / 46 sections; ZERO for a super-class dimension |
| `comp-read` | `comp-read data/cot/scripts/bronze/cot_bronze_ingest.py --for '...template or queryTypeId'` | found `load_template` + the two per-table dicts in one pass over 1387 lines |
| `comp-read` | `comp-read .tools/surprise-row-gate.py --for '...allowed values...'` | pointed at the real schema instead of the 3176-line gate |
| `comp-find` | `comp-find 'opal-bd-asset-dim-download' --limit 30` | surfaced the two change_management entries and the OPEN ledger the predecessor left |

**What worked:** `comp-read --enumerate` is the reason the super-class ZERO is reportable at all. A bare
grep miss and an out-of-corpus read are the same output; the printed denominator is what separates them.

**What failed:** nothing in the comp rail. Two non-comp failures, both device-class and both already
banked: native Python cannot open an MSYS `/c/...` path (the xlsx read failed until switched to
`C:/...`), and an unquoted bash heredoc expanded `$(date ...)` inside what was meant to be literal
Python — fixed by writing the script to a file instead.

**Gap found:** `aws lambda get-layer-version`'s presigned URL rejects `HEAD` with 403, so the
range-read trick for reading a layer zip's central directory needs its size from a ranged `GET`'s
`Content-Range` instead. Recorded here rather than filed: it cost one retry and no verdict.

## Deployment Sequence

| # | leg | act | evidence |
|---|---|---|---|
| 1 | read | measure the open ledger against the world before touching it (NEVER-2) | `nfra-mcpindex-bd-asset-dim-shutdown-order` read HELD-SOVEREIGN-GATED, L1/L2/L3/L5 closed, L4 open |
| 2 | verify | re-read the deployed document rather than trust the ledger's own proof | `describe-document` → Latest 3, Default 3, Active, Hash `490af524…d442129`, matching L2's recorded post-hash |
| 3 | verify | re-read the live runCommand | 66 lines; `shutdown -h` at index 58, `exit 1` at 63; LIVE == repo |
| 4 | activation | start `i-0e6f6dc014fdcf1cd`, wait for SSM | `stopped → pending` 22:09:05Z; SSM `Online` 22:10:23Z |
| 5 | verify | the planted L4 ordering probe | `ssm:e77e84c7-6e1f-4772-9dae-d00dc52b9965` → **Failed**, rc=1 |
| 6 | verify | the instance stops on its own schedule | running 22:16:53Z → stopping 22:17:16Z → **stopped** 22:17:38Z |
| 7 | git | ledger closed, all 5 legs proven, sentinel removed | `deploy_ledger.py close` OK |

No Terraform ran. No code was deployed. The only mutation outside the repo was starting an instance
that then stopped itself, and one planted log object under `logs/_planted_probes/`.

## Verification

**AC4, the one criterion left, and the gap the prior entry itself named.** The predecessor's AC4
evidence rested on a REAL failing run (the 70th) and explicitly told the grader to weigh one thing
against it: the honest exit as *first* deployed also stranded the runner, and the v3 repair for that
had no behavioural evidence of its own. That gap is now closed.

The probe was built to need **no vendor contact**. The script under test is the LIVE v3 runCommand
indices 52-65, copied programmatically out of `ssm get-document` rather than retyped, with exactly
ONE substitution — the log destination moved to `logs/_planted_probes/` so the probe can never be
miscounted inside the `asset-dim-download-*.log` corpus that AC1 globs. `DOWNLOAD_RC=1 MERGE_RC=99`
are planted, which AC4 admits in terms (*"a real or planted failure"*).

Both wanted properties were observed in one run, **each with its own witness**:

- stdout emits `Shutting down in 2 minutes...` BEFORE `ERROR: Asset-dim pipeline failed
  (download_rc=1 merge_rc=99)` — the ordering.
- stderr carries the operating system's own `Shutdown scheduled for Sun 2026-09-27 22:17:03 UTC`
  beside `failed to run commands: exit status 1` — so the shutdown was really **armed**, not merely
  echoed. An echo-only read could not have told those apart, which is the whole reason Z-S17 existed.
- the instance then halted on exactly that schedule.

**What the probe does NOT cover, stated rather than left to inference:** the bun downloader and the
BD portal login were not invoked, so this proves the wrapper's exit/shutdown ordering and *not* that
a real login failure yields the non-zero rc. That second link is carried by the real 70th-failure run
and the 69 before it. The Monday 2026-09-28 22:10Z scheduled fire remains the unforced end-to-end
acceptance.

## Decisions Made

1. **Read the order at HEAD, not at the commit the launch prompt pinned.** A3 was named in the
   handoff; A4 had already superseded its mechanism and A5 landed mid-session. The pinned citation
   aged separately from the text it quoted.
2. **Answered A4 step 1.1 by measurement rather than by reading the catalogue.** The documented field
   dictionary says one thing; the live artifacts say another. Comparing the two live xlsx headers —
   31 columns against 71 — is what settled it, and it settled it the opposite way from the
   convenient answer: the downloader is *not* merely redundant.
3. **Did not silently widen `<paths>`.** Three write surfaces were needed, two of them outside the
   order and one of those rule-13 DS-owned in cot's tree. Filed Z-S30 BLOCKING, named three routes,
   took none. The issuer ruled (c) in four minutes.
4. **Did not fire the dead vendor login, and said why.** The order's preflight cites Andrew's egress
   word as covering *"this session"* — a session that is not this one. A planted probe produced L4's
   evidence with no vendor contact, so the question never had to be escalated. Availability was not
   authorization here, and it did not need to be.
5. **Did not re-execute the CTO's patch.** `git apply --check` failed because the content was already
   present; the artifact read showed the predecessor had landed it at `765093b0e3` and that it is on
   origin. World-done, so it was reported, not repeated.

## Files Modified

| path | commit |
|---|---|
| `org/missions/D9/NFRA/.../surprise-channel/investigations/INVESTIGATION_v1.md` | `e8fcf04e58` (row Z-S30) |
| `org/missions/D9/NFRA/.../deliverables/0.7.0_AE_CloudOps~I/...proof_of_spec.json` | this commit |
| `org/critical_paths/change_management/20260927T0121Z_...shutdown-order_deploy_completion.md` | this commit |
| `org/critical_paths/.open_deploys/nfra-mcpindex-bd-asset-dim-shutdown-order.json` | this commit (sentinel removed) |
| `org/missions/D9/NFRA/.../task-orders/NFRA_MCPINDEX.TO-MX-s-4.bd-asset-dim-login.md` | this commit (`<status>` → complete) |

## Blockers

**None owed by this seat.** One item is owed BY others and is not a blocker on MX-s-4:

- **Step 1.2 (the REST pull)** is `1.0.0_SA_CTO~O`'s to design per A5. Evidence is row Z-S30.
- **Z-S30 and Z-S17** are both ARMED with `2.0.0_SA_COO~O` as `disarm_owner`. Z-S17's two disarm
  conditions are now BOTH satisfied — the instance is stopped and the reorder landed — so it is
  disarmable at the issuer's convenience.

## Current State

MX-s-4 is step 2 only and step 2 is done, deployed, and verified in the world. The SSM document
`opal-bd-asset-dim-download` is at version 3, Active, default, with the shutdown armed before the
failing exit; a failing run now reports Failed to SSM *and* releases its t3.medium. The deploy
ledger carries five proven legs and no sentinel. The instance is stopped.

The asset-dim data itself is still frozen — `silver/bd_assets.parquet` and `bd_assets_dim.parquet`
have not moved since 2026-04-14, and the last good bronze is 2026-06-18. **That is unchanged by this
order and was never in it:** the freeze's cause is BD's MFA, its repair is step 1.2 (now the CTO's),
and the compaction/rebuild legs went to the DS lane as MX-s-6. Nothing here should be read as
un-freezing the bridge.

## Next Steps

**[`3.0.0_SA_CVO~O`]** Grade AC4 at L9. It is recorded UNVERIFIABLE-BY-INSTRUMENT and carries two
halves — a real failure and a planted ordering probe — with the planted probe's limits stated inside
the instance.

**[`2.0.0_SA_COO~O`]** Disarm Z-S17 (both conditions met) and carry Z-S30 into the round-N analysis.

**[`1.0.0_SA_CTO~O`]** Design step 1.2. The cheapest starting point is that the asset-dim template is
query type 2 — the same type `bd-49f-runner` already pulls — so the route needs a captured template
body, not a new crawler; and `asset_super_class` is the one column with no documented route at all.

**[this seat]** Report once to the issuer, then event-driven on the inbox.
