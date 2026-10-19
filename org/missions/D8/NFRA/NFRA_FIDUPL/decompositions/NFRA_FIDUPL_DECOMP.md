# NFRA_FIDUPL -- L5 decomposition, ROUND 1 (the FWD-1 thread) -- DRAFT v0.1, NOT CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-19 ~18:3xZ | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path, read at HEAD.
**Status:** DRAFT, pre-read on the CTO's word (`1.0.0_SA_CTO~DELL1`, msg 8430: "read now, cut nothing yet"). **No task order is cut by this file.**
Nothing is cut until L4-R signs both halves of the PRD, which waits on Andrew confirming the DONE WHEN lines. Not frozen: it versions until the cut.
**Input:** PRD v0.1 DRAFT `../prd/NFRA_FIDUPL_PRD.md` @3324161d52 (LOCAL when read); endpoint FWD-1..FWD-8; brief `docs/briefs/auto-fidelity-uploader-brief-20261019.md` @ea34e538ae.
**Row:** `../project.json`, `dep_stage: PRD`. This commit does not flip it (row owner: the CTO).

## 0. What I measured before drafting (2026-10-19, HEAD of box/dell1)

| item | state | consequence |
|---|---|---|
| `fidelity` VENDOR row in `infra/logic/registry/systems.json` | LANDED @a492c648da (CRO) | C-NAMES half 1 is done; `address("fidelity", ...)` still needs a SCOPE row |
| a Fidelity scope row in `infra/logic/registry/scopes.json` | ABSENT (0 hits for "fidelity") | cell FU-s-1 is still owed, and waits on fork (d) tenancy |
| Quo SMS read | exists: `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py` (Quo `/v1/messages`, recency window, secret `quo/api-key`) | FU-s-2 ports the read; it does not invent it |
| Schwab chain | EventBridge -> SSM -> Windows task as Administrator -> puller from S3; box-wide lock `C:\schwab-sdd\.sdd-session.lock`; run record `_ops/daily_pull/` and `meta/pulls/` | prior art for FU-s-5/6 and the C-RECORD shape |
| Schwab window | `monolith-daily-schedule.tf`: crons at 09:45 / 10:15 / 10:45 UTC = 05:45 / 06:15 / 06:45 ET | C-WINDOW target; Fidelity's own generation hour is still unmeasured (first recurring row is 2026-10-20) |

NOT READ: the Terms of Use; any HAR capture (not in the repo); `sdd-daily-pull.ps1` beyond its lock and manifest limbs; `iam.tf` and `monolith-iam.tf`; `kms.tf`.

## 1. Gates that stand over cells (not cells)

| gate | holder | holds |
|---|---|---|
| L4-R sign-off, both halves | CVO (ratified text), CRO (brief half) | every cut |
| C-TOU: Andrew's word on Wealthscape Terms of Use | Andrew | FU-s-3 live run, FU-s-4 live run, FU-s-6 on-demand run, FU-x-1. Authoring and unit proof proceed |
| fork (a) sign-in driver: browser or raw HTTP | CTO rules on CRO research | FU-s-3 design |
| fork (b) reuse the Schwab box or a new one | CTO rules on CRO research | FU-s-5, FU-s-6 |
| fork (c) vault or Secrets Manager for the Wealthscape login | CTO rules on CRO research | FU-s-5, FU-s-3 (where it reads) |
| fork (d) C-TENANCY | CTO rules on CRO research | FU-s-1, FU-s-4 (landing paths) |

## 2. The rectangle (round 1 = the thread's hops)

Domain (postulate i): the hops FWD-1 walks, in order: **names -> code read -> sign-in -> list/download/land/record -> setup and schedule -> the live trace**. Subtracted from the PRD's cell candidates 0-3: candidate 0 = FU-s-1; 1 = FU-s-2 + FU-s-3; 2 = FU-s-4; 3 = FU-s-5 + FU-s-6. The trace is FU-x-1. **7 cells, 4 candidates covered, 0 uncovered.**
Out of round 1 (enrichment, the next cut): C-BACKFILL (FWD-6), the Monday read (FWD-4), the ordinary-morning window read (FWD-2), the both-run morning (FWD-8), the deliberately failed sign-in read (FWD-3's second arm).

Cell ids: `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, `FU-s-<n>` (thread cell), `FU-x-<n>` (closing pass for FWD-<n>). Read against `.tools/proof-of-spec-check.py:657-658` (`[A-Z][A-Z0-9]*-[a-z]{1,4}-[a-z]?\d+`): both shapes match by reading the pattern; the checker itself has not been run on this file, since no task order carries the ids yet.

| cell | what it builds (one adapter) | write set (disjoint) | PRD rows | risk |
|---|---|---|---|---|
| **FU-s-1** | The Fidelity scope row(s) in the registry, with `address("fidelity", ...)` printing the landing path for each of the six file families and the run-record path | `infra/logic/registry/scopes.json` (and the regenerated targets the registry lint names) | C-NAMES, C-TENANCY | LOCAL |
| **FU-s-2** | The Quo reader: given the digital line and a login-start time, returns the newest Fidelity code inside a recency window, never logs it, returns a distinct result for "no code arrived" | `infra/aws/ec2/canonical-fidelity/quo_otp.py` | C-SIGNIN (code leg) | LOCAL |
| **FU-s-3** | The sign-in: password, `OTPSMS`, code from FU-s-2, authorize; returns a signed-in session; fails with one of two distinct classes (sign-in refused, code never arrived) | `infra/aws/ec2/canonical-fidelity/signin.*` (extension per fork (a)) | C-SIGNIN | WORLD |
| **FU-s-4** | The pull: status list for the day, download of each of the six files, raw land at FU-s-1's addresses, sha256 per file, business date read from file content and checked against `lib/trading_calendar.py`, one run record with the four failure classes | `infra/aws/ec2/canonical-fidelity/fidelity-daily-pull.*` | C-PULL, C-RAW, C-DATE, C-RECORD | WORLD |
| **FU-s-5** | The Terraform root beside `canonical-schwab-ec2/`: schedule, box or box role, secret homes, IAM grants, names from `name()`; `terraform plan` only | `infra/aws/terraform/<root named by the builder>/` | C-TF, C-WINDOW (cron stated, not fixed), C-ISOLATION | LOCAL |
| **FU-s-6** | Apply FU-s-5 under `safe-apply` with a change-management ledger opened at start and closed at completion; install the puller on the box by a code deploy, never a hand edit | the root's state; the box's puller path | C-TF, C-ISOLATION | SERVED |
| **FU-x-1** | Closing pass for FWD-1: one on-demand run through the real chain; the six files listed, downloaded and landed; an analyst-side read opens them; the record shows no person signed in | none (read and run only) | FWD-1 | WORLD |

Hookups that belong to no cell, added by the COO at the merge: the `project.json` `decompositions` line; any registry-generated target the lint demands.

## 3. Dependency edges (keyed to OBSERVED completion, a real data dependency each)

```
FU-s-2 -> FU-s-3                 (the sign-in consumes the code reader)
FU-s-1 -> FU-s-4                 (the pull lands at the addresses FU-s-1 prints)
FU-s-3 -> FU-s-4                 (the pull rides the signed-in session)
FU-s-1 -> FU-s-5                 (the root cites builder output)
FU-s-4 -> FU-s-6                 (the box installs the pull that exists)
FU-s-5 -> FU-s-6                 (the apply applies the root)
FU-s-6 -> FU-x-1                 (the trace runs the deployed chain)
```

Maximal paths: `s-2 > s-3 > s-4 > s-6 > x-1` and `s-1 > s-5 > s-6 > x-1`, joined at `s-4` by `s-1`. Ready at the cut: FU-s-1 (after fork (d)) and FU-s-2 (no fork). Three chains of cells run apart before the join, so the fanout is 2 to 3 workers against the default cap of 8; the issuer states it as `fanout:` data in the issuance commit.

## 4. Taxonomy record (rule 24)

- **(i) MECE over a declared domain:** the six PRD CONTRACTS rows C-SIGNIN, C-PULL, C-RAW, C-DATE, C-RECORD, C-TF each have a cell; C-NAMES, C-TENANCY via FU-s-1; C-WINDOW, C-ISOLATION via FU-s-5/6; C-BACKFILL is enrichment; C-TOU is a gate, not a cell. Counted by subtraction from the PRD's CONTRACTS table rows: 12 rows (6 with a cell, 2 via FU-s-1, 2 via FU-s-5/6, C-BACKFILL enrichment, C-TOU a gate), 0 unaccounted.
- **(ii) same grain:** one cell is one adapter with one write set.
- **(iii) intent coherence:** FU-s-5 authors, FU-s-6 applies; the two are separate acts with separate risk classes.
- **(iv) state coherence:** a cell flipped `complete` does not mean its live arm ran: FU-s-3 and FU-s-4 carry a unit/LOCAL arm that proceeds before C-TOU and a live arm that does not. Each task order names which arm it grades.

## 5. Battery (round 1 default)

| lens | disposition |
|---|---|
| `comp-iam` | **RUN** at the cut: the thread touches IAM (FU-s-5). Denominator printed then; not run in this draft |
| `comp-schedule` | DECLARED-NOT-APPLICABLE: thread round; the lens runs on the enrichment round that touches the schedule (FWD-2) |
| `comp-adversary` | DECLARED-NOT-APPLICABLE: same reason |

## 6. Open questions for the cut (stated, not settled here)

1. **C-NAMES is CRO-owned in the PRD, and the decomposition says every cell is served by a worker.** FU-s-1 may need the CRO to land the scope row itself (the system row already was). The CTO decides.
2. **FU-s-6 is an AWS apply.** CLAUDE.md rule 34 seats CloudOps one lane per macro per box and routes every CloudOps order of that macro's projects to it. If FU-s-6 is a CloudOps order, it goes to `0.7.0_AE_CloudOps~NFRA<n>`, not a worker. Confirm at L6.
3. **A build TO carries at most three mechanical criteria** (spine v3.16-3.18); FU-s-4 has four contract rows. The cut splits criteria across the TO and the drain's hygiene run, or the CTO rules FU-s-4 into two cells (pull+land, then record).
4. **Windows or Linux for the Fidelity box** follows fork (a) and (b). If a browser-driven sign-in on the Schwab box is chosen, C-ISOLATION binds the lock and the console session; if raw HTTP, a scheduled container could replace the box and PRD decision 1 would need reopening. This draft assumes the box.
