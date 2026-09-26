# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.4 (COO_Y.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: `/closer-drive IRPT_BCKEND~Y` every 30m (cron 2f72865f), per CTO 101100 (Andrew-direct ~03:0xZ, 09-26; record
`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`). Lease FAST until 2026-09-26T15:01:17Z. Vendor API egress
is permitted but ledgered; served moves need the CTO's never-widen half. Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`.
As of 2026-09-26T14:30Z. Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/STATUS.md` (13:45Z).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-mvp-y-20260922` at `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` |
| Workspace candidate pin | `a9fba2f3e9` (hops 1-7 offline on a deferred v2 template input: READY, vendor upload carries AAPL 10.01 / VNQ 2.02) over `58280c8dd4` (Y2 deferred arms: XLSX, weights, correction) over `522afcfd17` (test module-identity fix, P 100860) over `d16b7c8743` (hop-3 input-owner lookup) over `10a16bd89d` (attribution fix) over `bb1eb7f92b` RESOLVE_UPLOAD (CVO handoff 18:29Z) over `b398d27731` |
| P composition patch | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/P_UPLOAD_COMPOSITION_20260924.{patch,md}`: hops 2+3, applies clean to P `9efaf2850e` |
| Portal candidate pin | n/a (portal candidates go to `2.0.0_SA_COO~D`) |
| Deployed artifact pin | resident `irpt-analysis-resident.service`, package `ab2e088b5b` (P receipt 100483; not re-read by Y) |
| Push state | Y branch LOCAL; not on origin (brief section 2: origin holds only `CLOUD`) |

## Live thread

State: LIVE THROUGH HOP 1d (upload -> resolve -> NORMALIZED). At 13:54:56Z Y made ONE `POST /analysis/inputs` by API as
the admin+Dev walk principal `irpt-uiwalk-1790430787@opal.test` (packet v3 blob `07b7a000`, K4; CTO `b70ede1756`, CRO
`a157c45762`; P 101191):
- the POST answered RESOLVING;
- the resident logged `handled=1` at 13:55:02Z;
- NORMALIZATION# reads NORMALIZED;
- `INPUT#portfolio_99e76df8...` is `irpt-normalized-portfolio.v2`: total 12.03, AAPL 10.01, VNQ 2.02, both resolved by
  YCharts.

Evidence with every row and object key: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/LIVE_UPLOAD_1203_EVIDENCE_20260926.md`
@3cc73f2b79. The scrubbed log is `LIVE_UPLOAD_1203_20260926_RUN2.json`. The 03:17Z failure (the missing `interactive_access`)
was fixed by P at `45d905110c`, served as generate `IJD6bd1I` at 13:30Z; the closure check exits 0.

Hop 3 was ATTEMPTED as K5 (packet v5 `6813377a`: CTO `3b43a23f92`, CRO `80b1a711f3`; CTO 101203). At 14:18:08Z Y made ONE
`POST /analysis` (Overview) on that input, which answered UNEXPECTED, `corr-8c5e097ea21e`: generate raised
ModuleNotFoundError `jsonschema`.
- `ycharts/generate/composition_admission.py:11` imports jsonschema and referencing at module level.
- Zip `IJD6bd1I` carries neither.
- Nothing was written: no row, no job, no queue message, no vendor call.
- Log: `LIVE_SUBMIT_1203_20260926.json`.

The closure check passed that zip because it walked only first-party imports (surprise row S144 @fa8aff523f). Y fixed it
@2664fe084c: it now FAILS on `IJD6bd1I`, naming jsonschema and referencing [MODULE]; a positive control with stubs passes.

The principal was deleted at 14:22:22Z (P 101232). The input's owner binds to that deleted principal, so hop 3 needs:
- P's repackage (jsonschema plus its dependencies, with rpds-py as a Lambda-platform wheel) under CTO 101230's three
  conditions;
- then a new window: a fresh upload plus a submission, or Andrew's own upload plus Generate.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Y1 custody + owned CSV/XLSX + disposition | OFFLINE + one real-object run | interpreter @47b2adf6df, oracle 15/15 |
| Y2 immutable normalized input | LIVE for Dollars CSV (one run, 13:55Z, @3cc73f2b79); the other arms OFFLINE | deferred lane @bb1eb7f92b + @58280c8dd4: Dollars 12.03, XLSX, TARGET_WEIGHT with notional, missing notional refused by name, correction lineage, race arm; SHARES refused by name (no price source) |
| Y3 acceptance, dispatch, recovery | INSTALLED, not exercised | P 100483 |
| Y4 vendor PDFs (3 variants) | NOT STARTED live | session graded |
| Y5 certified typed report | OFFLINE ONLY | publisher |
| Y6 polling/history/reload/downloads | ROUTES SERVED, not exercised | P batch 42/43 |
| Y7 reconciled full trace per case | NOT STARTED | none |

## Write claims

None in flight. RESOLVE_UPLOAD landed @bb1eb7f92b and @10a16bd89d. The scratch worktree `irpt-y-pcompose-20260924` was
removed by 0.0.0_AB_MSTR at 13:3xZ after Y's content check (101172); its branch is kept. Y makes no commit on P's branch.

## Next proof

Live hops 1a-10 per `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/RUNBOOK_1203_LIVE_JOURNEY_20260923.md` once Andrew
posts `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv` as an Opal viewer. At 22:12Z on 09-25 there are
still 0 UPLOAD#/NORMALIZATION#/INPUT# rows in all three firms. Portal 5174 is at `8242412d` and still carries the template lane
(`prospect.ts:65`). No Y build item is unblocked:
- Custody hop 4 is P's composition (CTO 100649). It needs P's binding store, current_selection and M's publication_for.
  Y's part is delivered: `build_custody_ports` @47b2adf6df and the decoder rung-2 read @70c464cec9.
- Comparisons need M's policy consumer.
- Shares is parked on CTO 100887.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Upload design card + word | 2.0.0_SA_COO~P | CTO 100667 | not needed to build; Y built on the accepted shape |
| Patch applied (`a58859baa7`); ledger `irpt-upload-hop2-20260924` R1 resident package, then L1 generate rebuild (runbook B2 order) | 2.0.0_SA_COO~P | `P_UPLOAD_COMPOSITION_20260924.md` | AWAITED |
| `ports["ordinary_authorizer"]` producer (partner viewers) and `get_catalogue` (hop 3) | 2.0.0_SA_COO~P | generate_installed absent producers | AWAITED; an Opal viewer is not blocked by it |
| Restore M's viewer seam `485b69c061` onto `_scope/maintained_sources.py` (8 conflict hunks vs `bc3727b3a3`) | 2.0.0_SA_COO~P (M reads semantics) | Y 100842; M 100846: `test_maintained_viewer_sources.py` 27/27 | DONE at P `19b38e2f22` (LOCAL); rides the hop-2 deploy |
| Grants for hop 2 (both roles) | 2.0.0_SA_COO~P | P `54bc1359f4` APPLIED 19:22Z | DONE: Y reach-check 19:3xZ, DDB PutItem + SQS SendMessage allowed, with a negative control |
| Portal: template body, RESOLVING adapter + poll, `.xlsx` (spec `D_UPLOAD_TEMPLATE_LANE_SPEC_20260924.md`) | 2.0.0_SA_COO~D | ~D 100877: edits 1-3 LANDED on portal DEV `088386fe` (the 5174 server's HEAD, Y read 20:2xZ); edit 4 (wire regen) waits on the contract patch | DONE for the live run |
| First live 12.03 upload (file `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv`) | 2.0.0_SA_COO~D's signed-in PROD walk with a HAR (Andrew via CTO 101075, record @37025a10e9); P mints the test principal (Opal-class, confirmed by Andrew in f7284ddeed); the walk must select a concrete firm, since Global refuses FIRM_BINDING (Y addendum 03:0xZ) | runbook hops 1a-1d; Y reads its part from the committed HAR plus the rows | AWAITED -- notified 20:2xZ. Baseline 20:2xZ: irpt-requests UPLOAD#/NORMALIZATION#/INPUT# = 0 in cottonwood, 49financial and inflection (consistent query; control SELECTION# cottonwood = 14). Contract landed at P `a47102cc8f` (100878). |
| Contract: request template lane + result RESOLVING/findings (`P_UPLOAD_CONTRACT_20260924.patch`, `--check` clean at P `7f6b5589f6`) | 2.0.0_SA_COO~P | Y 20:1xZ | AWAITED |
| Custody composition (hop 4) | 2.0.0_SA_COO~P | Y 47b2adf6df; decoder read `CUSTODY_DECODER_RUNG2_READ_20260924.md` (rung 2 empty for py3.12: 18 layers, 2 pyarrow, both py3.11) | AWAITED |
| First live Analysis submission | Andrew (browser) | after a composition serves | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Shares price source (Y2 Shares cells): CTO 100887 ruled (c), refused by name for v1; (b) has no known estate table; (a) goes to Andrew | 2.0.0_SA_COO~Y (re-ask the CTO) | the Dollars journey is graded |
| `intake/tests/test_security_resolution.py:31` needs IRPT_LOOKUP_FIXTURE_ROOT | 2.0.0_SA_COO~Y | the next edit to that suite |
| `reports/tests/test_generate_installed.py:58` expects 22 schemas; the tree holds 23 (fails at P's own tip) | 2.0.0_SA_COO~P | P's next edit to that suite |
| The Y worktree is a sparse checkout (`firm_destination_policy.json` is S), so two `test_broker_recovery_evidence` arms fail only here | 2.0.0_SA_COO~Y | a suite needs that file on this worktree |

## Limits

Hops 2+3 are deployed (generate `LdjdnnLh`, 09-24 19:49Z), but no live upload has succeeded: the one attempt failed on the
missing module before any write. The resident resolution uses no price source: SHARES templates answer
NEEDS_CORRECTION by name until one is composed. No vendor call is made by this seat; the resident's one batched
`securities_info` GET is the standing host-workflow authorization (CTO 100667 (1)).
