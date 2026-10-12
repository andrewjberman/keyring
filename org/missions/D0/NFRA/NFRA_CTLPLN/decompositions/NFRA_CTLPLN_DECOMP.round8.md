# NFRA_CTLPLN decomposition -- round 8: the firm-access registry build (FWD-28), the intake install defect, the crossbox ack design (issuer 2.0.0_SA_COO~C; cut 2026-10-12)

**Status: ISSUED in one issuance (four worker orders, one staged worker order, one staged seat order, plus the issuer acts below). FROZEN at the cut.**

**Input.** `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round7.md` (1.0.0_SA_CTO msg 108494), section 3: E1-E8 carried, E9 FWD-27 (gated on Andrew), E10 FWD-28 (a: `CT-u-7`, done; b: the registry build in the proposal's section-7 order), E11 the graduations.
Cut on PRD v0.25. Round 7 closed first (`round-close-check --round 7` MAY-CLOSE). **First act, done before this cut:** `TO-CT-u-3/u-4/u-5` withdrawn (commit 04236a87ad) so the row gate reads no staged order.
Plan of record: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~64/PROPOSAL_FIRM_ACCESS_REGISTRY_ROW.md` (CVO MET, C-S23; five points ruled by the CTO,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_CTLPLN_CT_V2_FIRM_ACCESS_REGISTRY_FIVE_POINTS_20261012.md`).

## Measured at the base (issuer, 2026-10-12 ~08:3xZ, box/laptop)

1. `python -I lib/opal_naming.py validate` is the registry's validator (verbs: validate, generate, vectors, targets, census); the model test is `lib/tests/test_opal_naming_bronze_homes.py`.
2. `infra/logic/registry/` holds `scopes.json`, `systems.json`, `resources.json` and 12 more files; no `firm_pages.json`.
3. The data proxy holds `_ROUTES_OPEN_TO_VERIFIED_LOGINS` (two route strings) and gates by tier (merged @6a1607d1e0, LIVE since CT-u-7).
4. `intake_receive.py install` runs `pip install --user` for every wheel into `sys.executable`'s user site (row D1-S10).
5. E4: dell2's ack of laptop->dell2 `XB-20261012T070501Z-cb95` is outstanding at the time of this cut; `CROSSBOX-MATRIX pairs=12 with_file=12 acked=9 closed_both=5 none=0`.

## Cells

| cell | what | serves | risk | issued to |
|---|---|---|---|---|
| `CT-w-1` | The registry build, step 1-2 of the proposal's section 7: `infra/logic/registry/firm_pages.json` (4 firm rows, 2 open-route rows, the TEN page paths named for `GET /aum/metrics`, no ALL token), the builder edit to `lib/opal_naming.py` (REGISTRY_FILES, OPTIONAL_REGISTRY_FILES, the VIEWS entry, WHOLE_FILE_TARGETS, TARGET_REGISTRY_KEYS, BLOCKS, `_blk_route_firms`, validate() rows) in its OWN commit through commit-gate, the regenerated `infra/aws/lambda/portal_data_proxy/firm_page_access.py`, and its tests | FWD-28 | WORLD by path floor (applies nothing) | `0.9.0_WK_NFRA_CTLPLN~65` |
| `CT-w-2` | Step 3-4: the handler patch (the two open routes check `firmId` against `ROUTE_FIRMS`; every other route unchanged), the source-map `files` entry, and the test edits (T3-T6) | FWD-28 | WORLD by path floor (applies nothing) | `~65` (queue, after `CT-w-1`) |
| `CT-w-3` | Step 5-7: the CloudWatch pre-apply read (a table by firmId and tier), the apply under a SECOND signed pair with a NEVER-2 ledger, the post-apply calls | FWD-28 | WORLD | `0.7.0_AE_CloudOps~U7` (laptop), staged until `CT-w-2` is merged and the pair is signed |
| `CT-w-4` | Step 8: the portal carrier: a second generated target `portal/src/lib/firmAccess.ts` ([FIRM_ALLOWED_PATHS] block) with its new span rule, a portal-side drift test, committed to the portal repository's DEV branch first; the workspace gitlink after. PROD waits on Andrew's word. | FWD-28 | LOCAL for DEV; the PROD push is Andrew's | `~66`, staged until `CT-w-1` is merged |
| `CT-w-5` | `intake_receive.py install` takes a target interpreter (or installs `--target` into a given folder) and never `--user` into `sys.executable` unless asked; tests | FWD-15 (row D1-S10) | LOCAL | `~67` |
| `CT-w-6` | A DESIGN proposal for the CTO, nothing applied: the crossbox ack moves to a per-recipient-box file so two boxes stop writing one JSON (61 of 69 conflicted paths since 2026-10-09). Reads `.tools/crossbox-call.py`, `crossbox-matrix.py`, `box-sync.sh` and the E8 census; writes one document. | FWD-8, FWD-3 | LOCAL | `~68` |

E9 (FWD-27): `CT-u-1`/`CT-u-2` are complete; the per-box cells are re-cut ACTIVE with their GO when Andrew's public keys land (the withdrawn orders' text is the template). It stays a qualified essential wait on Andrew's word (decomposition `NFRA_CTLPLN_DECOMP.remote1.md`).
E11: the CVO graduates D1-S8 and D1-S10 at this round's drain (no staged FWD-27 order remains).

## Rule 24

**Domain:** E1-E11 of the round-7 analysis.

| item | served by |
|---|---|
| E1 | measured and committed in round 7 (`E1_THREAD_TRACE_LGIC_BLANKFIX_R9.txt`); no cell |
| E2 | `TO-CT-x-1`, complete |
| E3 | `CT-v-1`, `CT-v-3`, complete; `CT-w-5` closes the defect the route showed; the read-aloud to Andrew is issuer act A3 |
| E4 | issuer act A4 (dell2's ack; the two other open files are their owners') |
| E5 | `TO-CT-t-3`, complete |
| E6 | issuer act A6 |
| E7 | issuer act A7 |
| E8 | census committed in round 7; `CT-w-6` is the design for the fix |
| E9 | `CT-u-1`, `CT-u-2` complete; per-box cells on Andrew's keys |
| E10 | `CT-u-7` complete; `CT-w-1`..`CT-w-4` |
| E11 | the CVO's act at the drain |

No item is unowned. **Same grain / one intent each. State coherence:** `CT-w-1`, `-2`, `-4`, `-5`, `-6` change only files in this repository (and the portal's DEV branch for `-4`); `CT-w-3` changes one Lambda's code under a pair.

## Dependency chains and fan-out

- Chain A: `CT-w-1` -> `CT-w-2` -> `CT-w-3`; and `CT-w-1` -> `CT-w-4`. One connected chain; worker `~65` takes `CT-w-1` then `CT-w-2` as its queue, worker `~66` takes `CT-w-4` when `CT-w-1` is merged, and `CT-w-3` is the seat order.
- Chain B: `CT-w-5` (worker `~67`). Chain C: `CT-w-6` (worker `~68`).
- M = 3 chains; N = 4 workers is more than M, so the queue rule holds the count to M: `~65` runs `CT-w-1`, `CT-w-2` and then `CT-w-4`; `~67`, `~68` run their cells. **N = 3.** (`~66` is not spawned; `CT-w-4`'s issued_to is `~65`.)

`fanout: 3 of 3 chains, cap 8, reason: the registry build is one chain on one worker queue (CT-w-1, CT-w-2, CT-w-4); the intake fix and the crossbox ack design are independent chains; CT-w-3 is a staged seat order`

## Issuer acts (the COO's one real run of each outcome, at the close)

- **A3:** read the click-route record (`deliverables/0.7.0_AE_CloudOps~CT1/NFRA_CTLPLN.TO-CT-v-3.*`) aloud to Andrew, including the account-takeover question; his act, at his time.
- **A4:** dell2's ack on `XB-20261012T070501Z-cb95` (through `0.0.0_AB_MSTR`).
- **A6:** `3.0.0_SA_CVO~L` reads `XB-20261008T203134Z-a3f0` against FWD-12 and FWD-22; Andrew reads `open-calls.py list --all --cloud` once.
- **A7:** each box's manager runs `seat-list.py write`; MSTR spawns one seat of each kind and asks what it is.
- **Second pair for `CT-w-3`:** the COO half is written at the GO; the CTO half is `1.0.0_SA_CTO`'s.
