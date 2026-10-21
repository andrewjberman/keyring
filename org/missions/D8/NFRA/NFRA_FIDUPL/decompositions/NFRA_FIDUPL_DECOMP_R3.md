# NFRA_FIDUPL -- L5 decomposition, ROUND 3 (coverage from the switcher, daily logout and recovery, backfill, the schedule on) -- v1.0, FROZEN AT THE CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-21 ~01:40Z | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path.
**Authority:** CTO msgs 8891, 8909 ("GO on the three open items in this order: switcher read + per-G secret, daily logout, schedule addendum; backfill cells cut now beside them") and the PRD v0.5 @c4f8dc3d51 (v0.4.6: coverage is every G number the switcher lists; the agent recovers the full browser sign-in once per run). Rounds 1 and 2 proved the thread: six files of 20261019 sit in `s3://opal-data-assets/fidelity/alongside/bronze/` (run record `run-20261021T012004Z.json`, ALL_LANDED).
**Input:** the worker reference sections 1 to 12 (section 12 is this round's interfaces); `RESEARCH_20261020_NFRA_FIDUPL_SWITCHER_LIST_READ.md`; `RESEARCH_20261021_NFRA_FIDUPL_FILE_DATE_AND_ACCOUNT_COLUMNS.md`.

## 0. The design in one paragraph

The login's G Number Switcher is the authority on which G numbers exist. Each run reads its list (the `gswitch` form parse already used by the attribution sweep), maps each label to a firm by the CRO's table (an unmatched label lands under `alongside` and is named by ordinal), and checks the list against the per-G secret, which is no longer the source but the cross-check; the secret's value is written once from the live read on the box. Every run ends with the logout the lander's session close already performs; the run now records its statuses. If the scripted sign-in is refused, the run tries the full sign-in once more in the box's own OS-launched Chrome unit (CDP attach), recorded, never looped. The backfill runner walks each G back as far as Fidelity serves, with a run cap and a daily sign-in cap. The schedule is turned on against a named secret version.

## 1. Gaps that are NOT in this round (stated so none is silent)

1. **The on-demand export request** (Export Custom with a date range; Historical Prices and Positions Export) is still unmeasured: the real `ExportClient` adapter of the backfill waits for Andrew's capture. FT-s-4 builds the runner against a fake.
2. **The account-number column of position, balance and transact** (the CRO has only account.txt = 0): `config.json` still holds the account-column map as measured on the box.
3. **Firm scope rows** for firms the table maps but the registry lacks are the CRO's (eight scope rows exist per its report).

## 2. The rectangle (cut by write set)

| cell | what it builds (one adapter) | write set (disjoint; the investigation file is shared and append-only) | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-1** | The switcher read and the per-G secret seed: the live list through the request object, the firm table, the cross-check, the seed payload and the box command `perg_seed.py` (signs in, reads, puts the one secret, logs out) | `infra/aws/ec2/canonical-fidelity/switcher_list.py`, `.../perg_seed.py`, `.../tests/test_switcher_list.py` | C-TENANCY, FWD-9 | WORLD |
| **FT-s-2** | The daily orchestration reads the live list each run, cross-checks it, writes a coverage record and the logout statuses, and tries the recovery once on a password refusal | `.../box/daily.py`, `.../box/run.py`, `.../tests/test_box_daily.py` | C-TENANCY, C-SIGNIN, FWD-3 | WORLD |
| **FT-s-3** | The in-run recovery: a CDP attach to the OS-launched Chrome unit, one full sign-in, logout on close | `.../signin_recover.py`, `.../tests/test_signin_recover.py` | C-SIGNIN | WORLD |
| **FT-s-4** | The backfill runner: per G the earliest date reached and the stop reason, a run cap and a daily sign-in cap | `.../backfill_run.py`, `.../tests/test_backfill_run.py` | C-BACKFILL | WORLD |
| **FT-s-5** | The box role may put the one per-G secret: one per-secret statement in the Terraform root, planned and applied | `infra/aws/terraform/canonical-fidelity-ec2/`; `org/critical_paths/change_management/`; `org/critical_paths/.open_deploys/` | C-TF | WORLD |
| **FT-s-6** | After FT-s-1, FT-s-2 and FT-s-5 are on the box: run the seed once on the issuer's GO, read the secret version (no value), turn the three schedule rules ON against that version, apply under `safe-apply` | the same Terraform root and ledger paths | C-TF, C-WINDOW, FWD-2 | WORLD |

Every order declares WORLD: GATE (xii) floors any `infra/` path there. Criteria are fixture tests plus structure checks; the live proof is the seed run and the first scheduled fire.

## 3. Edges

Data edges: `FT-s-1 -> FT-s-6`, `FT-s-2 -> FT-s-6`, `FT-s-5 -> FT-s-6` (delivery to the box by TO-FU-s-10 sits between). FT-s-1..FT-s-5 are built against the section 12 interfaces and fakes, so they start ready. Maximal paths: `FT-s-1 -> FT-s-6`, `FT-s-2 -> FT-s-6`, `FT-s-5 -> FT-s-6`, `FT-s-3`, `FT-s-4` (five). `fanout: 5 of 5 chains, cap 8`; four worker slots (~4 to ~7) take FT-s-1..FT-s-4, and FT-s-5 and FT-s-6 go to the CloudOps lane `0.7.0_AE_CloudOps~NFRA1` (rule 34).

## 4. Taxonomy record (rule 24)

- **(i) MECE:** the CTO's four items map to cells: switcher read + per-G secret = FT-s-1 (+ FT-s-5 for the put grant); daily logout = FT-s-2 (the close already logs out; the cell records it); schedule addendum = FT-s-6; backfill = FT-s-4; Andrew-direct v0.4.6's recovery = FT-s-3 (+ the hook in FT-s-2). 4 of 4 items covered. Not covered by design: gaps in section 1.
- **(ii) same grain:** one cell is one adapter with one write set. **(iii)** build and apply are separate orders. **(iv)** `complete` means fixtures plus structure pass; FT-s-6 and the live seed are the only cells that touch the world.

## 5. Battery

`comp-iam`: RUN at FT-s-5 (one statement added) and FT-s-6; BLIND to the root's computed names. `comp-schedule`: RUN at FT-s-6 (three rules turned ON). `comp-adversary`: RUN-NOT-APPLICABLE until FT-s-6 (the schedule is the first standing automated sign-in).

## 6. Addendum 2026-10-21 ~01:50Z (issuer, CTO relay of Andrew-direct MSTR 8912: the earliest date is found empirically, nothing waits on Andrew)

Andrew's method: on-demand exports at progressively earlier dates until the channel refuses or returns empty; land what it gives; the completion record names, per file type, the earliest business date landed, the total volume and any hard limit with its evidence. The measured calls already exist (`status.json` with a `dateString`, then `downloadExport.do`, `fetch.fetch_day`), so a past business day is one `fetch_day`. This closes gap 1 of section 1 for the first empirical pass without his capture.

| cell | what it builds (one adapter) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-7** | The real backfill adapter over `fetch.fetch_day` (one business day per window; empty status = retention stop, refusal = entitlement stop) and `backfill_main.py`, the box command that signs in once, walks back through `backfill_run.run`, lands each served day and writes the completion record | `infra/aws/ec2/canonical-fidelity/backfill_adapter.py`, `.../backfill_main.py`, `.../tests/test_backfill_adapter.py` | C-BACKFILL, FWD-6 | WORLD |

Edge: `FT-s-4 -> FT-s-7` (the runner's interface, reference section 12). Executor: worker slot ~8.

## 7. Addendum 2026-10-21 ~02:50Z (issuer, CTO msg 8940: the firm split is Andrew's deliverable 1; GO on a daily-mode proof run on a config copy)

Measured on the box (names and indexes only): the account-number column is account 0, position 5, balance 0, transact 0; prices and security carry none. The proof run exercises, once, the stages that have only run on fakes: the switcher sweep over the 31 G numbers, the account lister's paging, the split under `fidelity/<firm>/`, and the coverage record, on a COPY of the box config so the scheduled fires keep running the raw land.

| cell | what it builds (one adapter) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-8** | On the box: create `config.daily.json` (the config plus `mode`, `firm_labels`, `account_columns`), and on the issuer's GO run `box/run.py` once on it; read the per-firm counts | the same Terraform root and ledger paths (a ledger for the config file and the run) | C-TENANCY, FWD-9 | WORLD |

Edge: `FR-s-2 REPAIR 4 -> FT-s-8` (a delivery of `split.py` sits between). Executor: `0.7.0_AE_CloudOps~NFRA1` (rule 34).

## 8. Addendum 2026-10-21 ~03:45Z (issuer: the live proof run found no working page-2 form among eleven candidates, CloudOps row D1-S13)

The account lister's page 1 returns 2000 rows of 5204 available and none of the eleven candidate paging forms (FR-s-6 REPAIR 1) added a row. The form has to be MEASURED, not guessed again. The cheapest measurement that settles it is a read-only probe in one signed-in session on the current G: per candidate form its status, row count, new-row count and the response's own `pageResponse` and `statuses` codes; and the `accountNumber` search semantics (one request per leading character with `length` 1, reading only `available`), because the human UI may narrow by search and never page.

| cell | what it builds (one module) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FT-s-9** | `box/paging_probe.py`: one sign-in, page 1, the eleven forms and a 36-character prefix sweep, counts-only lines, logout in a finally | `box/paging_probe.py`, `tests/test_paging_probe.py` | C-TENANCY, FWD-9 | WORLD (infra path floor) |

Edge: `FT-s-9 -> FT-s-8` (the probe's measurement cuts the next lister repair). Executor: worker slot ~5; the run is 0.7.0_AE_CloudOps~NFRA1 under TO-FT-s-8 (amended); workstream fidelity-r3-paging, a write set disjoint from fidelity-r3-split.
