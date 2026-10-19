# NFRA_FIDUPL -- L5 decomposition, ROUND 1 (the FWD-1 thread) -- DRAFT v0.9, NOT CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-19 ~19:1xZ | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path, read at HEAD.
**Status:** DRAFT, on the CTO's word (msgs 8430, 8435, 8453, 8455, 8473). **No task order is cut by this file.**
Nothing is cut until L4-R signs both halves of the PRD, which waits on Andrew confirming the DONE WHEN lines, FWD-9 included (open call `e141`). Not frozen: it versions until the cut.
**Input:** PRD v0.4.3 `../prd/NFRA_FIDUPL_PRD.md` @37a9865739 (the v0.4 to v0.4.3 diff read in full at v0.9); endpoint FWD-1..FWD-9; brief `docs/briefs/auto-fidelity-uploader-brief-20261019.md` @ea34e538ae; Andrew-direct record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_190xZ_FIDUPL_SIGNIN_AUTHORIZED_RELAY_DELL1.md` (read in full; the laptop primaries 6e7a80f56f and 6d6f14e6bc are not on this box); CVO tenancy verdict @bc07810172 (superseded in part, see below); Terms of Use finding @e999b31f1f and fork research @b99a64cd4e (cited by the PRD, not read in full).
**Row:** `../project.json`, `dep_stage: PRD`. This file does not flip it (row owner: the CTO).

**v0.9 (this edit), CTO msg 8503:** Andrew confirmed FWD-1..9 as written (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1950Z_FIDUPL_DONE_WHEN_CONFIRMED.md` @9e2ef4a08f, "Confirm as written."); G-4 is MET and the ratified-text half is re-delivered to `3.0.0_SA_CVO~DELL1`. Finished against PRD v0.4.3 @37a9865739 (the v0.4 to v0.4.3 diff read in full; the G number research `RESEARCH_20261019_NFRA_FIDUPL_G_NUMBERS.md` @14f422aa7d read in full: a G number is `G` plus 8 digits, 31 on this login, none in the five files on hand). Andrew recalls no G Number filter in the wizard, so the split plans on the custom `account.txt` column, and **FU-s-2's first run captures that file itself**. Read (1), the wizard filter, is dropped from FU-s-2: with land-all it would only matter if it limited the pull, which Andrew ruled out. FU-s-2 is back to two mechanical criteria.
**v0.8, CTO msg 8486 (PRD v0.4.3 @37a9865739; Andrew-direct 19:05Z, VERBATIM "We should land all of it so we have it ready.", record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261019_1905Z_FIDUPL_LAND_ALL_FIRMS.md`, not read here beyond the message):** the full pull lands raw under `fidelity/alongside`, every G number included; the 17 non-registry firms stay staged there; only Cottonwood, Inflection and 49 Financial split to `fidelity/<firm>/bronze` (FWD-9). No filter limits the pull, so the CTO's 19:00Z G-filter note is superseded: the two FU-s-2 reads still feed the split field. G-6 is closed by this; the one-profile-per-firm shape is gone.
**v0.7, CTO msg 8481 (PRD v0.4.1, C-TENANCY ruling @1b813b3b3b; the CRO's measurement @14f422aa7d, neither read here beyond the message):** the CRO found 31 G numbers with one firm each, but 0 of 5,007 file accounts carry a G number. RULED: round 1 lands the full pull raw at `address('fidelity','alongside','bronze',...)`. The sign-in cell's first live exercise also captures two reads, folded into FU-s-2's criteria: (1) whether Export Custom step 3 offers a G Number filter (if so, later cells use one profile per Opal firm, landing direct at `fidelity/<firm>/bronze`); (2) the custom `account.txt` column list (if so, the split cell splits on that column). G-5 is therefore no longer a wait on the CRO; it is those two reads. Non-Opal firms' accounts are at the CVO.
**v0.6, CTO msg 8473 on Andrew's word ~19:0xZ:**
- **C-TOU is MET and `c3a6` is closed.** The automated sign-in is no longer gated. The CVO's hold on landing (before `e141` or `c3a6` closes) lifts with it; the live arms are held by the cut and by G-3 only.
- **No new bucket.** Landing goes to `opal-data-assets` through `address('fidelity', <scope>, 'bronze', ...)`; `opal-data-alongside` is not provisioned. The bucket cell of v0.5 is dropped and the cells renumber back to FU-s-1..7. The v0.5 ruling to land only after the bucket is applied (msg 8455) is superseded.
- **FWD-9 is new:** each firm's Fidelity files in that firm's own place, split on the G Number. The CRO is measuring whether each firm has its own G number (a scope row per firm, landing direct) or there is one (stage under `alongside`, split on a named field). Its research sets the split cell.
**Earlier versions:** v0.5 @dfefb15801 (bucket cell), v0.4 (fetch and lander split), v0.3 (fork (d) ruled), v0.2, v0.1 in git.

## 0. What I measured (2026-10-19, HEAD of box/dell1)

| item | state | consequence |
|---|---|---|
| `fidelity` VENDOR row; the `alongside` FIRM scope row and cross-firm gate edit | LANDED @a492c648da, @bd84d81948 (CRO); `address('fidelity','alongside','bronze','account','20261016')` printed `s3://opal-data-assets/fidelity/alongside/bronze/account/20261016` | G-1 is met; the staging scope exists today |
| Per-firm scope rows | ABSENT; wait on the CRO's G Number measurement | the split cell is not cut in this draft |
| Quo SMS read | `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py`; PRD pins the read by line id and Fidelity sender | FU-s-1 ports it |
| Playwright split | `infra/aws/ec2/inf-exporter/src/stepwise/orion_export.ts:428-453` (cited by the PRD, not read) | prior art for FU-s-2/3 |
| Start-on-demand Linux boxes | `infra/aws/ec2/EC2_MANIFEST.json` (`cot-exporter`: "started by cot-bd-session-trigger Lambda via SSM doc"); `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf` | prior art for FU-s-5/6/7 |
| Schwab window | `canonical-schwab-ec2/monolith-daily-schedule.tf`: 09:45 / 10:15 / 10:45 UTC = 05:45 / 06:15 / 06:45 ET | C-WINDOW target; Fidelity's generation hour unmeasured until the 2026-10-20 rows |

NOT READ: the Terms of Use or the finding in full; the fork research in full; the HAR captures (not in the repo); `bd-49f-session-chain.tf`, `orion_export.ts`, `EC2_MANIFEST.json` beyond the lines above; `iam.tf`/`monolith-iam.tf`; the G Number structure (the CRO's measurement).

## 1. Gates over cells (not cells)

| gate | holder | holds |
|---|---|---|
| L4-R sign-off, both halves | CVO (ratified text), CRO (brief half) | every cut |
| G-4 Andrew's confirmation of the DONE WHEN lines, FWD-9 included (`e141`) MET @9e2ef4a08f | -- | nothing now |
| **L4-R delivery** the CVO signs the re-delivered ratified-text half; the L4 notifier delivers to the COO | `3.0.0_SA_CVO~DELL1`, then the notifier | the cut (`/dispatch`) |
| **G-3** the Wealthscape credential written into its Secrets Manager secret | Andrew (never in repo or chat) | the live arm of FU-s-2 |
| **G-5** the one read FU-s-2's first live exercise captures: which column of the custom `account.txt` holds `G\d{8}` tokens, if any | the FU-s-2 worker, then the CTO reads | the FWD-9 split cell's split field, which is the next round's. If no column holds them, the split has no key and goes back to the CTO as a row |
| G-6 (the 17 non-registry firms) CLOSED by msg 8486: they stay staged under `alongside`; only the three registry firms split | -- | nothing |
| G-1 (scope row and gate edit, @bd84d81948) MET. G-2 (C-TOU, `c3a6`) MET, closed on Andrew's word | -- | nothing now |

## 2. The rectangle (round 1 = the thread's hops)

Domain (postulate i): the hops FWD-1 walks: **code read -> session mint -> fetch -> land and record -> box runtime -> setup and schedule -> apply -> the live trace**. Subtracted from the PRD's cell candidates 0-3: candidate 0 = G-1 (met); 1 = FU-s-1 + FU-s-2; 2 = FU-s-3 + FU-s-4; 3 = FU-s-5 + FU-s-6 + FU-s-7. The trace is FU-x-1. **8 cells, 4 candidates covered, 0 uncovered.**
Out of round 1 (the next cut): the **FWD-9 split** (shape set by G-5; named here so it is not lost); C-BACKFILL (FWD-6); the on-demand chain run with the live schedule read (FWD-2) and the on-demand Monday-export pull landing once (FWD-4); the both-run morning (FWD-8; the separate box makes it an observation); the deliberately failed sign-in read (FWD-3's second arm).

Cell ids: `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, `FU-s-<n>` (thread cell), `FU-x-<n>` (closing pass for FWD-<n>). Read against `.tools/proof-of-spec-check.py:657-658`: both match by reading the pattern; the checker has not been run on this file.

| cell | what it builds (one adapter) | write set (disjoint) | PRD rows | risk |
|---|---|---|---|---|
| **FU-s-1** | The Quo reader: given the line id and the Fidelity sender, returns the newest code inside a recency window opened at the SMS-send step; never logs it; a distinct result for "no code arrived" | `infra/aws/ec2/canonical-fidelity/quo_otp.*` | C-SIGNIN (code leg), PRD ruling 5 | LOCAL |
| **FU-s-2** | The session mint: Playwright signs in (password, `OTPSMS`, code from FU-s-1, authorize), keeps a persistent profile or saved state, returns a signed-in context; distinct failures for sign-in refused and code never arrived; records once whether a persisted device cookie skips the SMS step. **Its first live exercise also captures the custom `account.txt` itself (CTO msg 8503)** by one status list and one `downloadExport.do` inside the minted context, and writes a record of its COLUMN COUNT (141 expected) and, per column index, how many values match `^G\d{8}$`. No value, no account number and no row is written anywhere and the file is not committed (client PII). Two mechanical criteria: the sign-in, and the record | `infra/aws/ec2/canonical-fidelity/signin.*`; `infra/aws/ec2/canonical-fidelity/signin_recon.*`; `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/<worker serial>/FU-s-2_account_gnumber_read.md` (the spine's `deliverables/<serial>/` home; the slot is known only at the cut) | C-SIGNIN (ruling (a)), C-TENANCY (the read) | WORLD |
| **FU-s-3** | The fetch, inside the minted context: status list for the day, `downloadExport.do` for each of the six files, written to a local directory with a listing file; the directory and listing are the handoff to FU-s-4; distinct failure for "export not generated yet" and "download refused" | `infra/aws/ec2/canonical-fidelity/fetch.*` | C-PULL | WORLD |
| **FU-s-4** | The lander, source-independent: reads the handoff directory, lands the six files raw once into `opal-data-assets` at the path `address('fidelity', <scope>, 'bronze', ...)` returns AT LANDING TIME (the scope is a parameter, and round 1 ruled it `alongside`: the full pull lands raw at `fidelity/alongside/bronze`; never a typed path), sha256 per file, business date read from content and checked against `lib/trading_calendar.py`, a re-served day lands once, one run record with the four failure classes | `infra/aws/ec2/canonical-fidelity/land.*` | C-RAW, C-DATE, C-RECORD, C-TENANCY | WORLD |
| **FU-s-5** | The box runtime: bootstrap that installs Chromium, Playwright and the runtime on a Linux image, the persistent-profile directory, and a run wrapper that calls fetch then lander at the paths in section 3, fails loud on every "nothing to do" path, and takes no secret from an environment variable | `infra/aws/ec2/canonical-fidelity/box/` | C-SIGNIN, C-ISOLATION (ruling (b)) | LOCAL |
| **FU-s-6** | The Terraform root beside `canonical-schwab-ec2/`: EventBridge schedule, the on-demand start and stop of the box, the box, its SSM-only security group, the Wealthscape secret (metadata only, `prevent_destroy`), per-secret grants (no prefix wildcard), the box role's write grant on the Fidelity prefix of `opal-data-assets` (no bucket is created); every name from `name()`; `terraform plan` only | `infra/aws/terraform/<root named by the builder>/` | C-TF, C-WINDOW (cron stated, not fixed), ruling (c) | LOCAL |
| **FU-s-7** | Apply FU-s-6 under `safe-apply` with a change-management ledger opened at start and closed at completion; deploy FU-s-1..4 and FU-s-5's files to the box by a code deploy, never a hand edit | the root's state; the box's code path | C-TF | SERVED |
| **FU-x-1** | Closing pass for FWD-1: one on-demand run through the real chain (start, SSM, wrapper, sign-in, fetch, land, stop); six files listed, downloaded, landed; an analyst-side read opens them; the record shows no person signed in | none (read and run only) | FWD-1 | WORLD |

Hookups that belong to no cell, added by the COO at the merge: the `project.json` `decompositions` line; any registry-generated target the lint demands.

## 3. Dependency edges (keyed to OBSERVED completion, a real data dependency each) and interface bounds

```
FU-s-1 -> FU-s-2                 (the session mint consumes the code reader)
FU-s-2 -> FU-s-3                 (the fetch runs inside the minted context)
FU-s-3 -> FU-s-7                 (the box deploys the fetch that exists)
FU-s-4 -> FU-s-7                 (the box deploys the lander that exists)
FU-s-5 -> FU-s-7                 (the box deploys the runtime that exists)
FU-s-6 -> FU-s-7                 (the apply applies the root)
FU-s-7 -> FU-x-1                 (the trace runs the deployed chain)
```

**Interface bounds (not edges, so the cells run apart):** the handoff between FU-s-3 and FU-s-4 is a local directory holding the six files as served plus one listing file (fileName, fileType, profileId, requestId, fileCreatedTimestamp); the paths of `signin.*`, `fetch.*` and `land.*` are fixed in section 2 and a task order may not move them; the wrapper calls them in that order; the lander's scope parameter is the only thing the FWD-9 split changes.
Maximal paths: `s-1 > s-2 > s-3 > s-7 > x-1`, `s-4 > s-7`, `s-5 > s-7`, `s-6 > s-7`. All four chains start ready at the cut (G-1 is met). The fanout is about 4 workers against the default cap of 8, stated as `fanout:` data in the issuance commit.

## 4. Taxonomy record (rule 24)

- **(i) MECE over a declared domain:** the PRD CONTRACTS rows are 12 (C-TOU, C-NAMES, C-TENANCY, C-SIGNIN, C-PULL, C-RAW, C-DATE, C-RECORD, C-WINDOW, C-ISOLATION, C-TF, C-BACKFILL). Counted by subtraction: C-SIGNIN (FU-s-1, 2, 5), C-PULL (FU-s-3), C-RAW, C-DATE, C-RECORD (FU-s-4), C-TF (FU-s-6, 7), C-WINDOW (FU-s-6, 7), C-ISOLATION (FU-s-5), C-TENANCY (G-1 for the row, FU-s-4 for the landing scope, the split in the next round); C-NAMES is G-1; C-TOU is met; C-BACKFILL is enrichment. 12 accounted, 0 uncovered. ENDPOINT outcomes: FWD-1 has the thread; FWD-9 is deferred to the next cut by G-5, named in section 2, not dropped. Ruling (c) lands in FU-s-5 and FU-s-6.
- **(ii) same grain:** one cell is one adapter with one write set.
- **(iii) intent coherence:** FU-s-6 authors, FU-s-7 applies; the fetch and the lander are separate because one serves only the automated path and the other every path.
- **(iv) state coherence:** `complete` on FU-s-2, 3 and 4 does not mean its live arm ran. Each carries a LOCAL/unit arm (fixtures only; the real files hold client PII and are never committed) and a live arm; FU-s-2's live arm waits on G-3. A task order names which arm it grades.

## 5. Battery (round 1 default)

| lens | disposition |
|---|---|
| `comp-iam` | **RUN** at the cut: the thread touches IAM (FU-s-6). Denominator printed then; not run in this draft |
| `comp-schedule` | DECLARED-NOT-APPLICABLE: thread round; the lens runs on the enrichment round that touches the schedule (FWD-2) |
| `comp-adversary` | DECLARED-NOT-APPLICABLE: same reason |

## 6. Open at the cut (stated, not settled here)

1. **FU-s-7 is an AWS apply.** CLAUDE.md rule 34 routes every CloudOps order of a macro's projects to `0.7.0_AE_CloudOps~NFRA<n>`. If it is a CloudOps order it goes there, not to a worker. Confirm at L6.
2. **Start-on-demand mechanism.** A trigger Lambda via an SSM document (the `cot-exporter` shape) or EventBridge calling SSM Automation is a FU-s-6 design choice; the lead time before the 05:45 ET window is C-WINDOW's, set after the first recurring row.
3. **FWD-9 in round 1 or later.** The split goes in the next round: it splits the staged pull to `fidelity/<firm>/bronze` for Cottonwood, Inflection and 49 Financial on the `account.txt` column FU-s-2's read names (G-5), which cannot exist before round 1's first live sign-in; the other 17 firms stay staged. The other five files carry accounts, not G numbers, so the split joins them to `account.txt` on the account number; that join is the split cell's design. It is the round-N analysis's enrichment item, so the CTO names it there. Round 1 delivers the staged raw pull, which is what both shapes start from.
4. **Landing at `alongside` as staging, then a firm copy.** Andrew's word allows staging under `alongside` and parsing out afterwards. That creates a firm slice as a second write from raw staged bytes, not a move of served output; the CTO or CVO states this if the cross-firm gate reads it differently.
5. **The cross-firm gate** (`.tools/ds-precommit-check.py`) now covers `alongside`; a per-firm scope row is a further gate edit, the CRO's.
