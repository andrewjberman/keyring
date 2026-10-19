# NFRA_FIDUPL -- L5 decomposition, ROUND 1 (the FWD-1 thread) -- DRAFT v0.2, NOT CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-19 ~18:4xZ | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path, read at HEAD.
**Status:** DRAFT, on the CTO's word (msg 8430, "read now, cut nothing yet"; msg 8435, "re-base the decomp on v0.2"). **No task order is cut by this file.**
Nothing is cut until L4-R signs both halves of the PRD, which waits on Andrew confirming the DONE WHEN lines. Not frozen: it versions until the cut.
**Input:** PRD v0.2 `../prd/NFRA_FIDUPL_PRD.md` @c09ae3894a (LOCAL when read); endpoint FWD-1..FWD-8; brief `docs/briefs/auto-fidelity-uploader-brief-20261019.md` @ea34e538ae; fork research `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_L4_FORKS.md` @b99a64cd4e (cited by the PRD, not read in full).
**Row:** `../project.json`, `dep_stage: PRD`. This file does not flip it (row owner: the CTO).
**v0.2 vs v0.1 (@a9bfb78e16):** forks (a) Playwright, (b) new SSM-only Linux box started on demand, (c) Secrets Manager per-secret grants are ruled. The scope row is no longer a cell: `4.0.0_SA_CRO~FIDELITY` lands it (C-NAMES) the turn the CVO rules tenancy (fork (d), REC: a COMPOSITE `alongside` scope). Cells renumbered; a Windows box is gone.

## 0. What I measured (2026-10-19, HEAD of box/dell1)

| item | state | consequence |
|---|---|---|
| `fidelity` VENDOR row in `infra/logic/registry/systems.json` | LANDED @a492c648da (CRO) | C-NAMES half 1 done |
| a Fidelity scope row in `infra/logic/registry/scopes.json` | ABSENT at my read (0 hits) | gate G-1 below; `address("fidelity", ...)` refuses until the CRO lands it |
| Quo SMS read | `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py` (Quo `/v1/messages`, recency window, secret `quo/api-key`); PRD v0.2 pins the read by line id and Fidelity sender | FU-s-1 ports it; it does not invent it |
| Playwright split | PRD cites `infra/aws/ec2/inf-exporter/src/stepwise/orion_export.ts:428-453` (session minted in a browser, calls run inside) | prior art for FU-s-2/3 |
| Start-on-demand Linux boxes | `infra/aws/ec2/EC2_MANIFEST.json` (`cot-exporter`: "Stopped between runs; started by cot-bd-session-trigger Lambda via SSM doc"); `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf` | prior art for FU-s-4/5 |
| Schwab window | `canonical-schwab-ec2/monolith-daily-schedule.tf`: 09:45 / 10:15 / 10:45 UTC = 05:45 / 06:15 / 06:45 ET | C-WINDOW target; Fidelity's generation hour unmeasured until the 2026-10-20 rows |

NOT READ: the Terms of Use; the fork research doc in full; the HAR captures (not in the repo); `bd-49f-session-chain.tf`, `orion_export.ts` and `EC2_MANIFEST.json` beyond the lines above; `iam.tf`/`monolith-iam.tf`.

## 1. Gates over cells (not cells)

| gate | holder | holds |
|---|---|---|
| L4-R sign-off, both halves | CVO (ratified text), CRO (brief half) | every cut |
| **G-1** the Fidelity scope row(s) | `4.0.0_SA_CRO~FIDELITY`, the turn `3.0.0_SA_CVO~DELL1` rules tenancy (fork (d)) | FU-s-3 (landing addresses), FU-s-5 (IAM scope on the bronze prefix), FU-s-6 |
| **G-2** C-TOU: Andrew's word on Wealthscape Terms of Use | Andrew | the live arm of FU-s-2, FU-s-3, FU-s-6's on-demand run, and FU-x-1. Authoring and unit proof proceed |
| **G-3** the Wealthscape credential written into its Secrets Manager secret | Andrew (never in repo or chat, per the Schwab precedent `secrets.tf:30`) | the live arm of FU-s-2 |

## 2. The rectangle (round 1 = the thread's hops)

Domain (postulate i): the hops FWD-1 walks, in order: **code read -> session mint -> list/download/land/record -> box runtime -> setup and schedule -> apply -> the live trace**. Subtracted from the PRD's cell candidates 0-3: candidate 0 = G-1 (a gate now); 1 = FU-s-1 + FU-s-2; 2 = FU-s-3; 3 = FU-s-4 + FU-s-5 + FU-s-6. The trace is FU-x-1. **7 cells, 4 candidates covered, 0 uncovered.**
Out of round 1 (the next cut): C-BACKFILL (FWD-6), the Monday read (FWD-4), the ordinary-morning window read (FWD-2), the both-run morning (FWD-8; the separate box makes it an observation, not a design risk), the deliberately failed sign-in read (FWD-3's second arm).

Cell ids: `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, `FU-s-<n>` (thread cell), `FU-x-<n>` (closing pass for FWD-<n>). Read against `.tools/proof-of-spec-check.py:657-658`: both shapes match by reading the pattern; the checker has not been run on this file.

| cell | what it builds (one adapter) | write set (disjoint) | PRD rows | risk |
|---|---|---|---|---|
| **FU-s-1** | The Quo reader: given the line id and the Fidelity sender, returns the newest code inside a recency window opened at the SMS-send step; never logs the code; a distinct result for "no code arrived" | `infra/aws/ec2/canonical-fidelity/quo_otp.*` | C-SIGNIN (code leg), PRD ruling 5 | LOCAL |
| **FU-s-2** | The session mint: Playwright signs in (password, `OTPSMS`, code from FU-s-1, authorize), keeps a persistent profile or saved state, hands back a signed-in context; distinct failures for sign-in refused and code never arrived; exercises once whether a persisted device cookie skips the SMS step and records the result | `infra/aws/ec2/canonical-fidelity/signin.*` | C-SIGNIN (ruling (a)) | WORLD |
| **FU-s-3** | The pull, inside the minted context: status list for the day, `downloadExport.do` for each of the six files, raw land at the scope row's addresses, sha256 per file, business date from file content checked against `lib/trading_calendar.py`, one run record with the four failure classes | `infra/aws/ec2/canonical-fidelity/fidelity-daily-pull.*` | C-PULL, C-RAW, C-DATE, C-RECORD | WORLD |
| **FU-s-4** | The box runtime: bootstrap that installs Chromium, Playwright and the runtime on a Linux image, the persistent-profile directory, and a run wrapper that calls the puller at the path fixed in section 3, fails loud on every "nothing to do" path, and takes no secret from an environment variable | `infra/aws/ec2/canonical-fidelity/box/` | C-SIGNIN, C-ISOLATION (ruling (b)) | LOCAL |
| **FU-s-5** | The Terraform root beside `canonical-schwab-ec2/`: EventBridge schedule, the on-demand start and stop of the box, the box, its SSM-only security group, the Wealthscape secret (metadata only, `prevent_destroy`), per-secret grants (no prefix wildcard), bronze write grant; every name from `name()`; `terraform plan` only | `infra/aws/terraform/<root named by the builder>/` | C-TF, C-WINDOW (cron stated, not fixed), ruling (c) | LOCAL |
| **FU-s-6** | Apply FU-s-5 under `safe-apply` with a change-management ledger opened at start and closed at completion; deploy FU-s-1..4's files to the box by a code deploy, never a hand edit | the root's state; the box's code path | C-TF | SERVED |
| **FU-x-1** | Closing pass for FWD-1: one on-demand run through the real chain (start, SSM, wrapper, sign-in, pull, stop); six files listed, downloaded, landed; an analyst-side read opens them; the record shows no person signed in | none (read and run only) | FWD-1 | WORLD |

Hookups that belong to no cell, added by the COO at the merge: the `project.json` `decompositions` line; any registry-generated target the lint demands.

## 3. Dependency edges (keyed to OBSERVED completion, a real data dependency each) and interface bounds

```
FU-s-1 -> FU-s-2                 (the session mint consumes the code reader)
FU-s-2 -> FU-s-3                 (the pull runs inside the minted context)
FU-s-3 -> FU-s-6                 (the box deploys the pull that exists)
FU-s-4 -> FU-s-6                 (the box deploys the runtime that exists)
FU-s-5 -> FU-s-6                 (the apply applies the root)
FU-s-6 -> FU-x-1                 (the trace runs the deployed chain)
```

**Interface bounds (not edges, so the cells run apart):** the wrapper (FU-s-4) calls the puller at `.../canonical-fidelity/fidelity-daily-pull.*` and the puller reads the context from `signin.*`; those paths are fixed in section 2 and a task order may not move them. The six files and the run-record shape are the contract between FU-s-3 and the landing (G-1).
Maximal paths: `s-1 > s-2 > s-3 > s-6 > x-1`, `s-4 > s-6 > x-1`, `s-5 > s-6 > x-1`. Ready at the cut: FU-s-1, FU-s-4, and FU-s-5 once G-1 reads LANDED; three independent chains, so the fanout is about 3 workers against the default cap of 8, stated as `fanout:` data in the issuance commit.

## 4. Taxonomy record (rule 24)

- **(i) MECE over a declared domain:** the PRD CONTRACTS rows are 12 (C-TOU, C-NAMES, C-TENANCY, C-SIGNIN, C-PULL, C-RAW, C-DATE, C-RECORD, C-WINDOW, C-ISOLATION, C-TF, C-BACKFILL). Counted by subtraction: C-SIGNIN, C-PULL, C-RAW, C-DATE, C-RECORD, C-TF, C-WINDOW, C-ISOLATION each have a cell; C-NAMES and C-TENANCY are G-1; C-TOU is G-2; C-BACKFILL is enrichment. 12 accounted, 0 uncovered. Ruling (c) lands in FU-s-4/5.
- **(ii) same grain:** one cell is one adapter with one write set.
- **(iii) intent coherence:** FU-s-5 authors, FU-s-6 applies; separate acts, separate risk classes.
- **(iv) state coherence:** `complete` on FU-s-2/3 does not mean its live arm ran. Each carries a LOCAL/unit arm that proceeds before G-2 and G-3 and a live arm that does not; a task order names which arm it grades.

## 5. Battery (round 1 default)

| lens | disposition |
|---|---|
| `comp-iam` | **RUN** at the cut: the thread touches IAM (FU-s-5). Denominator printed then; not run in this draft |
| `comp-schedule` | DECLARED-NOT-APPLICABLE: thread round; the lens runs on the enrichment round that touches the schedule (FWD-2) |
| `comp-adversary` | DECLARED-NOT-APPLICABLE: same reason |

## 6. Open at the cut (stated, not settled here)

1. **FU-s-6 is an AWS apply.** CLAUDE.md rule 34 routes every CloudOps order of a macro's projects to `0.7.0_AE_CloudOps~NFRA<n>`. If FU-s-6 is a CloudOps order it goes there, not to a worker. Confirm at L6.
2. **A build TO carries at most three mechanical criteria** (spine v3.16-3.18); FU-s-3 has four contract rows (C-PULL, C-RAW, C-DATE, C-RECORD). The cut splits them between the TO and the drain's hygiene run, or the CTO rules FU-s-3 into two cells.
3. **Start-on-demand mechanism.** The PRD says started on demand and stopped after the run. Whether the start is a trigger Lambda via an SSM document (the `cot-exporter` shape) or EventBridge calling SSM Automation is a FU-s-5 design choice; the lead time between the start and the 05:45 ET window is C-WINDOW's, set after the first recurring row.
4. **The CRO's and CVO's turn order.** G-1 reads LANDED only after the CVO rules tenancy and the CRO lands the row; if the REC is not taken, FU-s-3's landing path and FU-s-5's bronze grant change shape.
