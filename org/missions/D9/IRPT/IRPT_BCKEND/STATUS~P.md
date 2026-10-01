# IRPT_BCKEND~P (Performance, shared auth/routes/IaC/packaging) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). **Mode FAST** from 2026-10-01 04:31Z to 12:31Z: lease `IRPT_BCKEND~P`, `org/mcp/drive-mode.log` line 32,
on Andrew's word of ~04:2xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`
@c48af273cc). Loop: `/canonical-drive 10m` (LIVE_ARMS RELAUNCH row); each tick reads the lease and runs `/closer-drive`. IRPT_DASHBD
workstream B stays FULL. As of 2026-10-01 ~06:5xZ. Earlier forms are in git (the 05:0xZ form @723ce58d3f).

## Standing Andrew words that govern this workstream (read first)

- **2026-09-28 ~22:2xZ call 3 and ~22:4xZ:** performance is end-of-day holdings only, every firm in ONE consolidated gold shape.
- **2026-09-30 ~04:3xZ:** YCharts is `2.0.0_SA_COO~Y`'s (@fe6326f6b0). This seat does no YCharts or resident work.
- **The D2 hold on ADVI_PERFRP** stands until Andrew lifts it; FAST relaxes no hold and no never-widen sign-off.

## Pins (served function -> live artifact, read at each apply)

| Function | Live CodeSha256 | Applied (Z) | What it runs | Packet / proof |
|---|---|---|---|---|
| irpt-performance-adapter | `PCcoNYrB...` | 10-01 06:22:07 | `served.py` 455cd77ea46e, the IB-yr-293 profile reader, three other closure members at CLOUD; 65 members untouched | packet 2 @5ff5bac77f |
| irpt-export-render | `BIYEQ3PK...` | 10-01 06:24:06 | `served.py` 455cd77ea46e, `loaders.py` | packet 2 |
| irpt-directory-search | `AVSIaHEh...` | 10-01 06:26:24 | whole bundle at f9a00f732c | packet 2 |
| irpt-holdings | `TG8b/SEH...` | 10-01 06:31:21 | whole bundle at 21eca74f40, `snapshot.py` at `2.0.0_SA_COO~M`'s ADDENDUM 1 pin | packet 2; after-read PASS @eea9f2844e |
| irpt-ycharts-generate | `ESedDkLy...` | 10-01 05:23:14 | `served.py` f6c6b56f40 over a STALE reader: still admits a foreign firm for a service subject | packet 1; `2.0.0_SA_COO~Y`'s whole bundle replaces it |
| irpt-status | `ZYr+IDMp...` | 09-28 14:04 | unchanged | `2.0.0_SA_COO~Y`'s whole bundle (legs G5, F6) |
| irpt-narrative | `es/S9azu...` | 09-21 | unchanged; no selection branch on its live boundary | excluded |
| inf-ec2-launch-monitor | `t1QrzaDe...` | 09-30 16:19:48 | pr-242 | A1 observation HELD (item 6) |

The service-principal boundary, read by `2.0.0_SA_COO~Y` as `svc-irpt-analysis` (`IRPT_MVP_Y/V1_SERVICE_BOUNDARY_REREAD_20261001.md`
@164c3dec00): foreign firm refused and cottonwood not refused on the adapter, export-render, directory-search and holdings (4 of 5);
row S238's directory control is refused; `irpt-ycharts-generate` is the fifth. Ten-minute log windows after packet 2: zero
error-class lines, 4 of 4. Ledger `irpt-service-principal-boundary-served-20261001`: G1-G4, F1, F2, F3, F4, F5 closed @cff3497d62;
V1 closes on `1.0.0_SA_CTO`'s read of that print (condition 9); G5 and F6 close on `2.0.0_SA_COO~Y`'s proof.

Commits: packet 1 @40c790a0bf (CTO @d9972c6eb4), applied @07cbc7684b; `served.py` item 4 @f9a00f732c; re-pins and the two gates
@6dbec1b0bd; builds @88317195ba and @fb4e852bf1; packet 2 @d8e1782d32 (CTO @5ff5bac77f), applied @cff3497d62.

## Write claims

- `2.0.0_SA_COO~P`: the `lambda-source-map.json` rows of irpt-performance-adapter, irpt-export-render, irpt-directory-search,
  irpt-holdings and irpt-narrative; the five `service_profile_read.tf` files; `_authz/served.py`; this file. The rows of
  irpt-ycharts-generate and irpt-status are `2.0.0_SA_COO~Y`'s (CTO batch 62 lane grant); the export `entry.py` live-byte pin stays.
- No root carries a pending plan from this lane except ops (`service_profile_read.tf`, the grant G5, add-only), which rides
  `2.0.0_SA_COO~Y`'s irpt-status move.

## Next (the order `1.0.0_SA_CTO` ruled in batch 63; one item at a time)

1. **49 Financial holdings gold for 2026-09-29** (sweep-5 section 2 item 3): read whether the producer accepts an as-of date; if
   yes, one fire through its own path under both halves naming that one key; if no, the gap is declared.
2. **The Inflection date basis** (batch 63 items 2-3; row S245): find the seam's day across 2026-05-01..09; read the same question
   for Cottonwood and re-confirm 49 Financial; the producer change; the rebuild; three hand reproductions; then IB-pr-221.
3. **NNA Branch A packet (W97-S3):** three literal keys (866, 769, 1096; partition 2026-09-24); the CTO signs on read.
4. **The mirror items** (batch 63 items 5-7; rows W99-S3, W99-S4): the coerced 09-29 parquet admitted only on a three-date
   equality; a second scheduled fire; an unknown key class as a counted SKIP.
5. **A1 observation** of the launch monitor: the first stop log line after 2026-09-30T16:19:48Z, due by 11:20Z today.
6. **A named refusal for a directory search with no client firm** (`served.py` answers `UNEXPECTED` for `BucketUnmapped`; 4 of 14
   walker searches at 06:34Z; the BEFORE bytes answer the same). A served `served.py` change: its own packet.

IRPT_DASHBD workstream B, done this session: SERIES contract @b80543a03c; TO-DB-b-1 amendments 5 and 6 (@f4f57b6fe4, @34ae583549);
TO-DB-b-3 amendment 3 @dd82147640; the four checks rewritten counterexample-first @ea2e7145ee. Owed next there: land the DS seat's
contract 0.2.0 when it reports it.

## Parked (owner; condition that un-parks it)

- The cause of the late 09-29 Schwab silver landing -- `0.6.2_AE_PartnerETL~C` (`TO-IB-pr-274`, parked); that lane registers LIVE.
- The served perfrp figure, rows W100-S2 / S237 / S239 -- base `2.0.0_SA_COO` on ADVI_PERFRP; Andrew lifts the D2 hold for that cell.
  The shared code table's two foreign-tax rows (row IRPT_DASHBD-S6 limb e, graded INERT) ride the same cell.
- `test_unguarded_census.py`, 6 failures at CLOUD HEAD since 2026-09-27 -- this lane; `export/entry.py`'s `lambda_handler` wrapper
  (f3995c0d31) carries no guard marks, so the census reads three export routes as declared by no entry. Live routing is unaffected.
  Un-parks when irpt-export-render next takes its `entry.py` (the live-byte pin is dropped in that move).
- The firm of the adapter's 47 reopens and 114 egress refusals since 09-29 16:40Z -- `1.0.0_SA_CTO` (asked 06:48Z); its answer.
- S216 (fact_positions past 09-27) -- this lane; item 4. S232 -- `2.0.0_SA_COO~Y`; the first job under `svc-irpt-analysis` ends.
- The six export and adapter A1 legs from 09-27/28 and `irpt-adapter-holdings-gold-49f-r3-20260929` A1 -- this lane; a live walk's
  read of each surface, and for r3 the first scheduled 49F producer fire that finds its silver.
- Scratch for a human to delete: DIR `C:\r27c`, DIR `C:\r27d`; the private worktree DIR `C:\Users\AndrewBerman\Desktop\coo-p-pr275`
  stays while this lane builds.

## Limits

- No scripted authenticated human request exists here. Served checks use `lambda invoke` with a NON-EXISTENT user (a refusal after
  enforcement), log reads, `2.0.0_SA_COO~Y`'s service-principal run and `2.0.0_SA_COO~D`'s signed-in walker.
- A member list says nothing about a member's vintage. Before any `served.py` move: `IRPT_MVP_P/served_import_closure.py` (every
  closure member beside CLOUD) and `IRPT_MVP_P/sibling_interface_check.py` (bundled siblings accept the calls made into them),
  both on the uploaded zip, and the zip compared with a bundle assembled and rehearsed locally BEFORE the upload.
