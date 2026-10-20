# NFRA_FIDUPL -- L5 decomposition, ROUND 1 (the FWD-1 thread) -- v1.0, FROZEN AT THE CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-19 ~20:1xZ | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path, read at HEAD.
**Status:** RATIFIED for the cut. L4-R is ADMITTED at PRD v0.4.3 @37a9865739 (`python .tools/prd-signoff.py status NFRA_FIDUPL`: ratified-text SIGNED by `3.0.0_SA_CVO~DELL1`, brief SIGNED); Andrew confirmed FWD-1..9 as written (`ANDREW_DIRECT_20261019_1950Z_FIDUPL_DONE_WHEN_CONFIRMED.md` @9e2ef4a08f). From this commit the decomposition does not version during the round; a cell that looks wrong is a surprise row.
**Input:** PRD `../prd/NFRA_FIDUPL_PRD.md` v0.4.3; brief `docs/briefs/auto-fidelity-uploader-brief-20261019.md` @ea34e538ae; worker reference `NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (this folder); the CTO's rulings in msgs 8435, 8453, 8473, 8481, 8486, 8503, 8507, 8510.
**Row:** `../project.json`, flipped `PRD -> DECOMP` in the commit that lands this file; the issuance commit flips it to `EXECUTING`.
**History:** v0.1 to v0.9 are drafts in git (last @e78a163ce5).

## 0. What is settled, in one place

- Fresh sign-in every run by a Playwright browser that mints the session; the two data calls run inside it. A new SSM-only Linux box, started on demand and stopped after the run. Secrets Manager with per-secret grants. C-TOU is MET (Andrew, ~19:0xZ).
- Landing: `opal-data-assets` through `address('fidelity','alongside','bronze',...)`; the full pull lands raw, every G number included. `opal-data-alongside` is not provisioned and no cell provisions it.
- FWD-9 (per-firm split): CVO verdict @6e5e420536 (not read here beyond the CTO's msg 8510): no tree reads another firm's data. RULED (msg 8510): the split attributes accounts with Fidelity's own per-G `accountList.json`, called inside the uploader's session, with no Orion or BD read; the first authorized session measures the G switch (msg 8514: User Options > G Number Selection changes the CURRENT G number, lists all 31, and leaves the default alone; the probe switches once, reads `accountList.json` before and after, switches back); if the list narrows, the split maps all 31 G numbers per day with no crosswalk, and if Fidelity offers no per-G list the CTO puts a narrow crosswalk to Andrew. Until then the full pull stays staged under `fidelity/alongside`. **The split cell is HELD (section 5) and is not in this round's rectangle.**

## 1. Gates over cells (not cells)

| gate | holder | holds |
|---|---|---|
| L4-R, G-1 (scope row, @bd84d81948), G-2 (C-TOU), G-4 (`e141`) | -- | MET |
| **G-3** the Wealthscape credential written into its Secrets Manager secret | Andrew (never in repo or chat) | the live run of FU-x-1 only; every other cell builds and proves on fixtures |
| **Probe** the G switch and the `account.txt` G-number column, read by FU-x-1's first live session | FU-x-1 | the HELD split cell |
| **Seat** FU-s-7 is an AWS apply; CLAUDE.md rule 34 routes CloudOps orders of a macro's projects to the macro lane. No `0.7.0_AE_CloudOps~NFRA<n>` is live on dell1 (live: `0.7.0_AE_CloudOps~DELL1`, IDLE). This issuance addresses FU-s-7 to `0.7.0_AE_CloudOps~DELL1`, staged, and says so; the CTO or MSTR re-seats it if rule 34 binds | CTO | FU-s-7 only |

## 2. The rectangle (round 1 = the thread's hops)

Domain (postulate i): the hops FWD-1 walks: **code read -> session mint -> fetch -> land and record -> box runtime -> setup and schedule -> apply -> the live trace**. Subtracted from the PRD's cell candidates 0-3: candidate 0 = G-1 (met); 1 = FU-s-1 + FU-s-2; 2 = FU-s-3 + FU-s-4; 3 = FU-s-5 + FU-s-6 + FU-s-7. The trace is FU-x-1. **8 cells, 4 candidates covered, 0 uncovered.**
Out of round 1 (the next cut): the HELD FWD-9 split; C-BACKFILL (FWD-6); the on-demand chain run with the live schedule read (FWD-2) and the on-demand Monday-export pull landing once (FWD-4); the both-run morning (FWD-8; the separate box makes it an observation); the deliberately failed sign-in read (FWD-3's second arm).

Cell ids: `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1: `FU-s-<n>` (thread cell), `FU-x-<n>` (closing pass for FWD-<n>). Read against `.tools/proof-of-spec-check.py:657-658`: both match.

**Risk classes are the gate's floor, not my estimate.** `.tools/to-pipeline-gate.py` GATE (xii) infers WORLD for any order whose `<paths>` names an `infra/` entry, and every cell below writes under `infra/`; so every order is `WORLD`, declared. Each cell's LOCAL arm (fixtures) is what a worker grades; the live arm is FU-x-1's.

| cell | what it builds (one adapter) | write set (disjoint; the investigation file is shared and append-only) | PRD rows | risk |
|---|---|---|---|---|
| **FU-s-1** | The Quo reader: given the line id and the Fidelity sender, returns the newest code inside a recency window opened at the SMS-send step; never logs it; a distinct result for "no code arrived". Seam probe against the real Quo (read only) | `infra/aws/ec2/canonical-fidelity/quo_otp.py`, `.../tests/test_quo_otp.py` | C-SIGNIN (code leg) | WORLD |
| **FU-s-2** | The session mint (Playwright: password, `OTPSMS`, code from FU-s-1, authorize; persistent profile; distinct failures `sign-in refused` and `code never arrived`), PLUS two live-session helpers FU-x-1 will run: the `account.txt` G-number column read (column count and per-column `G\d{8}` match counts, no value written) and the G-switch probe the CTO ruled (msg 8514): switch the session's CURRENT G number once through User Options > G Number Selection with `Set As Default` never checked, read `accountList.json` before and after (counts only) to see whether it narrows, and switch back to the starting G number even on error | `.../signin.py`, `.../signin_recon.py`, `.../tests/test_signin.py`, `.../tests/test_signin_recon.py`, `.../tests/test_gprobe.py` | C-SIGNIN, C-TENANCY (the reads) | WORLD |
| **FU-s-3** | The fetch, inside the minted context: status list for the day, `downloadExport.do` for each of the six files into a handoff directory with `listing.json`; distinct failures `export not generated yet` and `download refused` | `.../fetch.py`, `.../tests/test_fetch.py` | C-PULL | WORLD |
| **FU-s-4** | The lander, source-independent: reads a handoff directory, lands the six files raw once at `address('fidelity', <scope>, 'bronze', ...)` read AT LANDING TIME, sha256 per file, content date from the first field, trading-calendar check, re-served day lands once, one run record with the four failure classes | `.../land.py`, `.../tests/test_land.py` | C-RAW, C-DATE, C-RECORD, C-TENANCY | WORLD |
| **FU-s-5** | The box runtime: `box/bootstrap.sh` (Chromium, Playwright, runtime; no secret in the environment) and `box/run.py` (calls signin, fetch, land in order, always lets the lander write the record, exits non-zero on any failure) | `.../box/bootstrap.sh`, `.../box/run.py`, `.../tests/test_box_run.py` | C-SIGNIN, C-ISOLATION | WORLD |
| **FU-s-6** | The Terraform root beside `canonical-schwab-ec2/`: EventBridge schedule (the three Schwab-window crons), an SSM Automation document that starts the box, runs the wrapper and stops it, the box (Linux, SSM-only, no ingress), the Wealthscape secret (metadata only, `prevent_destroy`), per-secret grants, the box role's write grant on the Fidelity prefix of `opal-data-assets` (no bucket created); names from `name()`; `terraform plan` only | `infra/aws/terraform/canonical-fidelity-ec2/` | C-TF, C-WINDOW (cron stated, not fixed), ruling (c) | WORLD |
| **FU-s-7** | Apply FU-s-6 under `safe-apply` with a change-management ledger opened at start and closed at completion; deliver FU-s-1..5's files and the naming builder's minimal tree to the box by SSM | the root's state; `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/` | C-TF | WORLD |
| **FU-x-1** | Closing pass for FWD-1: one on-demand run through the real chain; six files listed, downloaded, landed; the run record shows `source: automated`; then the two probes: the `account.txt` G-number read and the G-switch probe, each written as a counts-only record | `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/<worker serial>/` (granted by the tree convention) | FWD-1, C-TENANCY | WORLD |

Hookups that belong to no cell, added by the COO at the merge: the `project.json` `decompositions` line (done in this commit); any registry-generated target the lint demands.

## 3. Dependency edges (keyed to OBSERVED completion, a real data dependency each) and interface bounds

```
FU-s-1 -> FU-s-2                 (the session mint consumes the code reader)
FU-s-2 -> FU-s-3                 (the fetch runs inside the minted context)
FU-s-3 -> FU-s-7                 (the box receives the fetch that exists)
FU-s-4 -> FU-s-7                 (the box receives the lander that exists)
FU-s-5 -> FU-s-7                 (the box receives the runtime that exists)
FU-s-6 -> FU-s-7                 (the apply applies the root)
FU-s-7 -> FU-x-1                 (the trace runs the deployed chain)
```

**Interface bounds (not edges, so the cells run apart):** the handoff directory and `listing.json` between FU-s-3 and FU-s-4, the run record, the landing addresses and the session interface are fixed in the worker reference sections 4-6 and 5a; the module paths are fixed there (section 8) and a task order may not move them.
Maximal paths: `s-1 > s-2 > s-3 > s-7 > x-1`, `s-4 > s-7 > x-1`, `s-5 > s-7 > x-1`, `s-6 > s-7 > x-1`. Four chains, all ready at the cut (G-1 is met).

## 4. Taxonomy record (rule 24)

- **(i) MECE over a declared domain:** the PRD CONTRACTS rows are 12 (C-TOU, C-NAMES, C-TENANCY, C-SIGNIN, C-PULL, C-RAW, C-DATE, C-RECORD, C-WINDOW, C-ISOLATION, C-TF, C-BACKFILL). Counted by subtraction: C-SIGNIN (FU-s-1, 2, 5), C-PULL (FU-s-3), C-RAW, C-DATE, C-RECORD (FU-s-4), C-TF and C-WINDOW (FU-s-6, 7), C-ISOLATION (FU-s-5), C-TENANCY (G-1 for the row, FU-s-4 for the landing scope, FU-s-2 and FU-x-1 for the probes, the HELD split for the rest); C-NAMES is G-1; C-TOU is met; C-BACKFILL is enrichment. 12 accounted, 0 uncovered. ENDPOINT: FWD-1 has the thread; FWD-9 follows the probe, named in section 5, not dropped.
- **(ii) same grain:** one cell is one adapter with one write set.
- **(iii) intent coherence:** FU-s-6 authors, FU-s-7 applies; the fetch and the lander are separate because one serves only the automated path and the other every path.
- **(iv) state coherence:** `complete` on FU-s-1..6 means the LOCAL arm passed on fixtures and a read-only seam probe; it does not mean a live Fidelity sign-in ran. That is FU-x-1, which needs G-3.

## 5. The HELD cell (not in the rectangle above, so the coverage limb does not count it; stated here so it is not lost)

**FU-s-8, the FWD-9 split:** attribute the staged accounts per firm with Fidelity's per-G `accountList.json` called inside the uploader's session, and write each of Cottonwood, Inflection and 49 Financial's slice to `address('fidelity','<firm>','bronze',...)`, listing the accounts no firm claims; no Orion or BD read. **Held on** FU-x-1's G-switch probe (if Fidelity offers no per-G list, the CTO puts the narrow crosswalk to Andrew) and on the per-firm scope rows (the CRO). Its task order is cut as an addendum after the probe, by the CTO's word (msg 8507: "cut it after the verdict").

## 6. Battery (round 1 default)

| lens | disposition |
|---|---|
| `comp-iam` | **RUN** at FU-s-6's drain, on the written root: the thread touches IAM. BLIND to the root today (it does not exist); the denominator is printed at the drain |
| `comp-schedule` | DECLARED-NOT-APPLICABLE: thread round; the lens runs on the enrichment round that touches the schedule (FWD-2) |
| `comp-adversary` | DECLARED-NOT-APPLICABLE: same reason |

## 7. Open at the cut (stated, not settled here)

1. **Code distribution to the box.** The builder homes the `code` tier of scope `alongside` in the unprovisioned `opal-data-alongside` (measured), so no S3 code home exists under rule 30. FU-s-7 delivers by SSM `send-command` and files a surprise row if the size does not fit; the CTO owns the final code home.
2. **The run record sits in the bronze tier** as table `_runs` because the builder admits no `meta` or `_ops` tier for this scope (measured). A reader of the bronze tree sees a `_runs` table beside the six. The CTO confirms or names another home.
3. **Rule 34 and FU-s-7** (section 1, Seat).
4. **FU-s-6 builds the start-and-stop as an SSM Automation document** (no Lambda). That is my choice from the `cot-exporter` precedent; the worker files a row if the document cannot express the lead time before the window.

## 8. ADDENDUM 2026-10-20 (CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_FIDUPL_AUTOSHUTDOWN_OFF_20261020.md` @630242a029, msg 8621; Andrew-direct `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261020_125xZ_FIDELITY_SECRET_SET_AND_AUTOSHUTDOWN_OFF.md`)

The CTO rules one order now, not a round-2 item. The decomposition is otherwise frozen; this is the only cell added to the round.

| cell | what it builds (one adapter) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FU-s-9** | Autoshutdown off for the Fidelity box: one edit of the Terraform root adds the tag `AutoShutdown=disabled` to the instance and removes the `stopInstance` step from `automation.tf` (with the `onFailure` references to it), applied by the CloudOps seat under `safe-apply` AFTER FU-x-1's automation run has ended | `infra/aws/terraform/canonical-fidelity-ec2/`; `org/critical_paths/change_management/`; `org/critical_paths/.open_deploys/` | C-TF, FWD-7 | WORLD |

Edge: `FU-x-1 -> FU-s-9` (the apply waits until no automation execution is in progress). Executor: `0.7.0_AE_CloudOps~NFRA1`.

## 9. ADDENDUM 2026-10-20 (issuer, no spec change)

The live trace needs the repaired sign-in code on the box after each worker repair; code delivery is the CloudOps seat's act (FU-s-7 leg 3). The issuer reopens this order for each later repair rather than cutting a new one.

| cell | what it builds (one adapter) | write set | PRD rows | risk |
|---|---|---|---|---|
| **FU-s-10** | Keep the box's code equal to the repo: re-deliver every shipped file of `infra/aws/ec2/canonical-fidelity/` (and `box/`) to `/opt/fidelity-uploader/` by SSM, md5-checked, the box left running | `org/critical_paths/change_management/`; `org/critical_paths/.open_deploys/` | C-TF | WORLD |

Edge: `FU-s-2 -> FU-s-10 -> FU-x-1`. Executor: `0.7.0_AE_CloudOps~NFRA1`.
