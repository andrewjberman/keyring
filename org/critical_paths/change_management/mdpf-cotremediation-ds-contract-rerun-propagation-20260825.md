# DEPLOY-COMPLETION LEDGER -- MDPF_COTREMEDIATION DS leg (contract, re-run, propagation)

**Owner:** `0.4.0_DS_ClientPlatform~M` · **NEVER#6 / COTR-inv-9**
**TO:** `MDPF_COTREMEDIATION.TO-R1-DS.silver-contract-rerun-and-payload-proof`
**Decomp:** `workflows/atom_decomposition/runs/mdpf-cotremediation/20260825T161149Z/DECOMP.md` @`7807a52e75`
**Authority:** Andrew-direct 2026-08-25 ~14:20Z (*"That needs to get fixed immediately"*) · D8
**Closure authority:** `2.0.0_SA_COO` ruling 2026-08-25 ~17:54Z -- *"your NEVER#6 discharges on cottonwood. Close your ledger entry. You do not hold a defect that existed before your project did."*

⛔ **NOT vendor drift.** We amended the BD holdings template ourselves (`@17c38a26f2`, 2026-08-20T17:56:24Z, under a CTO pin). The vendor changed nothing. The silver-contract step was never sequenced.

## ⛔ PROCEDURAL DEVIATION, DECLARED RATHER THAN BACKDATED

**This entry was created at CLOSEOUT (~17:5xZ), NOT at deploy-start as the TO instructs.** The Terraform deploy leg belonged to `0.5.0_AE_OpalETL~B`, who correctly opened `mdpf-cotremediation-ae-silver-bd-contract-20260825.md` at 17:07:45Z; my own acts (re-run, gold, publish) are producer invocations rather than a Terraform apply, and I did not open a parallel entry when I began them. **Stating it plainly instead of writing a start time I did not record.** The acts below all carry their own independently-recorded run ids and timestamps, so the record is complete even though the ledger was late.

## Legs

| # | Act | Evidence | Status |
|---|---|---|---|
| 1 | Silver header contract: declare `Account Supervised` (idx 8) + `Holding Supervised` (idx 20) as Rule-17 passthrough, dtype `string` | commit `288807f747`, 1 file, +2 lines, LOCAL on CLOUD | **DONE** |
| 2 | Deployed-bytes confirmation (`COTR-c-2`) -- AE's leg, my obligation to confirm | package member read: 21 cols, idx 8 / idx 20, sha256(LF) `1ef7577547ae7af3` == repo source | **DONE** |
| 3 | Three-partition re-run (`date=2026-08-20`, `2026-08-21`, `2026-08-24` -- **THREE, not five; 08-22/08-23 are Sat/Sun**) | `aws lambda invoke` rc 200, run_id `20260825T172050Z-f26cf779`, all three `converted`, cols=21, rows 18,088 / 18,102 / 18,107 | **DONE** |
| 4 | Silver verified on LIVE state, not the producer's self-report | `comp-keys partitions` -- 55 -> **58** partitions, latest `2026-08-24` | **DONE** |
| 5 | Gold propagation (ad-hoc) | `mdpf-gold-lambda` 17:30:14-17:30:47Z; cottonwood gold `2026-08-24.json` written 17:30:48Z | **DONE** |
| 6 | Platinum publish (ad-hoc) | `opal-assets-mdpf-portal-publisher` run_id `20260825T173631Z-2d006242`, published 14, failed [], all_present true | **DONE** |
| 7 | AC2 -- cottonwood SERVED payload restored | `as_of_last` 2026-08-19 -> **2026-08-24**; `n_dates` 458 -> **461** (+3, exactly the three partitions); `source_keys` -> `.../2026-08-24.json` | **DONE** |
| 8 | AC4 -- healthy partners unmoved | 49financial 0 of 111 data-bearing fields moved; inflection 0 of 135. Sole delta both: `_provenance.written_at` | **DONE** |
| 9 | One discriminating global run (COO-ruled) | started 17:51:41Z, 21 min after the fresh cottonwood input; `CROSS-AXIS COHERENCE GATE FAILED (global) -- REFUSING TO EMIT` at 17:52:16Z | **DONE -- outcome REFUSE** |

## AD-HOC DISCLOSURE (NEVER: ad-hoc runs)

Legs 3, 5, 6 and 9 were **AD-HOC invocations by this seat**, fired to restore a dark client-facing product on Andrew's *"immediately"*. Per the standing rule they are a **QA/repair instrument and are NOT production evidence**. **AC6 closes on the SCHEDULED run** -- `mdpf-scheduled-floor` cron(30 13 * * ? *) -> `mdpf-gold-lambda`, then `opal-assets-mdpf-portal-publisher-daily` cron(50 13). Nothing this seat ran today is offered as AC6 evidence.

## WHAT IS NOT CLOSED BY THIS ENTRY

⛔ **`global` remains at `as_of_last=2026-08-19`.** Its `CROSS-AXIS COHERENCE GATE` refuses to emit on a **2026-08-19 foreign-day roster** (`7791 -> 8260 -> 7791`, +469/-469, net 0). **MEASURED INDEPENDENT of this repair:** the gate first fired **2026-08-24T13:31:04Z** (log retention `None`, so the absence on 08-20..08-23 is real), and it refused again on a clean run with fresh cottonwood gold in hand. **This is a separate defect that predates this project, matching a finding CTO filed 28 hours earlier.** COO ruled it gets **its own seat**; it is NOT carried by this entry.

⛔ **The coherence gate was NOT weakened, bypassed, forced, or made permissive, and `2026-08-19`'s data was NOT touched.** A guard refusing to emit incoherent data is the guard working (`COTR-inv-3`, extended to this gate by COO+CTO ruling).

## STATUS: **CLOSED** 2026-08-25 ~17:5xZ by `0.4.0_DS_ClientPlatform~M`, on COO's explicit closure authority above. No leg stranded. Nothing half-landed.
