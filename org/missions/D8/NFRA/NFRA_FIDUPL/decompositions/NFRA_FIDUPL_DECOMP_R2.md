# NFRA_FIDUPL -- L5 decomposition, ROUND 2 (per-G daily pull, firm split, backfill, schedule) -- v1.0, FROZEN AT THE CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-20 ~15:10Z | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path.
**Authority:** CTO msg 8663 (PRD v0.4.5 @e4bb46835e, still ADMITTED): "Issue the round-2 build cells NOW, built against fakes with disjoint paths, in parallel with attempt 3: (a) the per-G daily pull and firm split, (b) the backfill per G, (c) the schedule. The schedule turns on after one good on-demand run." Andrew-direct `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261020_1455Z_FIDUPL_PER_G_DAILY_AND_MAX_BACKFILL.md` @b329e1c5f3. Round 1 is still open (FU-x-1 attempt 3); this round runs beside it, in its own workstream.
**Input:** PRD v0.4.5 (read the C-TENANCY and C-BACKFILL rows and the change log); the worker reference sections 1 to 11 (section 11 is this round's interfaces).

## 0. The design in one paragraph

The scheduled export covers the whole ALONGSIDE domain (about 4,959 accounts) and lands raw under `fidelity/alongside` (round 1). **Attribution** is by the account lists Fidelity itself serves under each G number: the session switches the CURRENT G number through the measured JSP form (never the default), reads `accountList.json` under each of the 31 options and so maps every account to its G numbers and the G's label. **The split** then writes each firm's accounts' lines of the six files, byte-for-byte, to that firm's own prefix, once per firm. The **backfill** walks back per G number as far as Fidelity serves, naming each stop. The **schedule** is turned on after one good on-demand run.

## 1. Gaps that are NOT in this round and that Andrew or the CRO can close (stated so none is silent)

1. **The account-number column of each of the six files** is unmeasured (the custom export has no header row; only the column COUNTS are known: 141, 62, 43, 44, 45, 66). `split.py` takes a config map; the real values need Andrew's screenshot or copy of the Export Custom step-2 column order for each file, or FU-x-1's account.txt read extended to name it.
2. **The on-demand export request** (Export Custom with a date range; Historical Prices and Positions Export) is unmeasured, so the backfill's real `ExportClient` adapter cannot be written yet. Andrew's capture of creating one on-demand transactions export for a past date range, and of the Historical Prices and Positions Export, closes it. FR-s-3 builds the planner and the stop logic against a fake.
3. **`accountList.json` paging** (the offset field name past 2,000 rows) is unmeasured; FR-s-1 assumes `start` and files a row.
4. **The live sign-in** (round 1, FU-x-1) gates every live proof of this round.
5. Firm scope rows for the 17 unregistered firms are the CRO's (msg 8663).

## 2. The rectangle (this round = the three CTO items, cut by write set)

| cell | what it builds (one adapter) | write set (disjoint; the investigation file is shared and append-only) | PRD rows | risk |
|---|---|---|---|---|
| **FR-s-1** | The G-number switch and the attribution sweep: `GSwitcher` over the measured JSP form, and `sweep_attribution` over every option with an injected account lister; restores the starting G in a `finally`; never sets the default; counts-only summary | `infra/aws/ec2/canonical-fidelity/gswitch.py`, `.../attribute.py`, `.../tests/test_gswitch.py`, `.../tests/test_attribute.py` | C-TENANCY, FWD-9 | WORLD |
| **FR-s-2** | The firm split: from the staged raw day and the attribution, write each firm's lines byte-for-byte to `address('fidelity', <firm>, 'bronze', ...)`, once per firm; list conflicts, unplaced accounts, unmapped labels and firms without a scope row; one split record | `.../split.py`, `.../tests/test_split.py` | C-TENANCY, FWD-9 | WORLD |
| **FR-s-3** | The backfill per G: the backward window planner, stop detection with its named reasons, and the per-G per-kind record, against an injected `ExportClient` and `lander` | `.../backfill.py`, `.../tests/test_backfill.py` | C-BACKFILL | WORLD |
| **FR-s-4** | The daily orchestration: `box/daily.py` runs sign in, fetch, land staged, attribute, split, record, and `box/run.py main()` chooses it from `config["mode"]` | `.../box/daily.py`, `.../box/run.py`, `.../tests/test_box_daily.py` | C-TENANCY, C-WINDOW | WORLD |
| **FR-s-5** | The schedule and the per-G list home in the Terraform root: a `schedule_enabled` variable (default false) controlling the three rules' state, the SSM SecureString parameter for the per-G list (name from the builder, value ignored after creation) and the box role's read grant on that one parameter; plan only | `infra/aws/terraform/canonical-fidelity-ec2/` | C-TF, C-WINDOW, CTO msg 8637 | WORLD |

Every order declares WORLD: GATE (xii) floors any `infra/` path there. Each cell's criteria are fixture tests plus the structure check; the live proof is the daily orchestration's first on-demand run after FU-x-1 closes.

## 3. Edges and interface bounds

No data edges: the cells are built against fakes and the interfaces in worker reference section 11, so all five chains start ready. The wiring FR-s-4 imports the real modules lazily; its smoke at the merge proves the names. After merge: FR-s-5 is applied by `0.7.0_AE_CloudOps~NFRA1` (a later order); the real `ExportClient` adapter and the live runs wait on the gaps in section 1.
Maximal paths: five single-cell chains. `fanout: 5 of 5 chains, cap 8`.

## 4. Taxonomy record (rule 24)

- **(i) MECE:** the CTO's three items map to cells: (a) per-G daily pull and firm split = FR-s-1, FR-s-2, FR-s-4; (b) backfill = FR-s-3; (c) schedule = FR-s-5. 3 of 3 items covered, 0 uncovered. Not covered, by design and named in section 1: the account-column map, the export-request adapter, live proofs, firm scope rows.
- **(ii) same grain:** one cell is one adapter with one write set. **(iii)** authoring and applying are separate (FR-s-5 is plan only). **(iv)** `complete` means fixtures plus structure pass; no cell here has been run live.

## 5. Battery

`comp-iam`: RUN at FR-s-5's drain (the parameter read grant); BLIND to the root's computed names, as in round 1. `comp-schedule`: RUN at FR-s-5's drain over the three rules' state variable. `comp-adversary`: DECLARED-NOT-APPLICABLE: build round on fakes; runs when the live round touches the surface.
