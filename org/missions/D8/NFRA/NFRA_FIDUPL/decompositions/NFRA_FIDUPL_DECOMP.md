# NFRA_FIDUPL -- L5 decomposition, ROUND 1 (the FWD-1 thread) -- DRAFT v0.5, NOT CUT

**Author:** `2.0.0_SA_COO~P1` | 2026-10-19 ~18:5xZ | spine `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L5, cited by path, read at HEAD.
**Status:** DRAFT, on the CTO's word (msgs 8430, 8435, 8453: "decompose on that basis"). **No task order is cut by this file.**
Nothing is cut until L4-R signs both halves of the PRD, which waits on Andrew confirming the DONE WHEN lines (open call `e141`). Not frozen: it versions until the cut.
**Input:** PRD v0.3 `../prd/NFRA_FIDUPL_PRD.md` @6d747e7737; endpoint FWD-1..FWD-8 (FWD-2 and FWD-4 amended in place at v0.3); brief `docs/briefs/auto-fidelity-uploader-brief-20261019.md` @ea34e538ae; CVO tenancy verdict `org/tier1_exec/3.0.0_SA_CVO/deliverables/GOVERNANCE_VERDICT_NFRA_FIDUPL_TENANCY_20261019.md` @bc07810172; Terms of Use finding `...RESEARCH_20261019_NFRA_FIDUPL_WEALTHSCAPE_TERMS_OF_USE.md` @e999b31f1f (cited by the PRD, not read in full); fork research `RESEARCH_20261019_NFRA_FIDUPL_L4_FORKS.md` @b99a64cd4e (not read in full).
**Row:** `../project.json`, `dep_stage: PRD`. This file does not flip it (row owner: the CTO).

**v0.5 (this edit), CTO msg 8455:** C-NAMES landed @bd84d81948 (I read the `alongside` row in `scopes.json` and ran `address('fidelity','alongside','bronze','account','20261016')`, which resolves today to `s3://opal-data-assets/fidelity/alongside/bronze/account/20261016` because `bucket_provisioned` is false). RULED: the cell that provisions `opal-data-alongside` runs before any cell that lands bytes and flips `bucket_provisioned` in the same commit; landing happens once, at its final address read from `address()` at landing time, never in the monolith and moved later. So the bucket becomes its own cell, **FU-s-5**, in its own small root, applied early; it precedes the lander (FU-s-4), and the box runtime, Terraform root and apply renumber to FU-s-6, 7, 8. 9 cells now.
**v0.4, what moved and why:**
- The Terms of Use prohibit robots and agentic AI without Fidelity's approval. Three paths are in terms: Fidelity's written approval, an Integration Xchange transmission, or a person's daily download. The CTO: only the automated sign-in waits on `c3a6`; landing, record, schedule and Terraform serve every in-terms path.
- So the old pull cell splits in two. The **lander** (raw land, sha, content date, run record) takes six files from ANY source and has no session in it. The **fetch** (status list and download inside a minted session) is the only cell that exists for the automated path. The lander is then independent of the sign-in chain, and the split also takes the old cell under the three-criteria cap.
- 8 cells at v0.4. Fork (d) ruled: FIRM scope `alongside` (v0.3 of this file).

## 0. What I measured (2026-10-19, HEAD of box/dell1)

| item | state | consequence |
|---|---|---|
| `fidelity` VENDOR row in `infra/logic/registry/systems.json` | LANDED @a492c648da (CRO) | C-NAMES half 1 done |
| the `alongside` FIRM scope row and cross-firm gate edit | LANDED @bd84d81948 (CRO); row read, `bucket: opal-data-alongside`, `bucket_provisioned: false`; the gate edit's diff not read | G-1 is met; FU-s-6 is the next link |
| Quo SMS read | `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py`; PRD v0.3 pins the read by line id and Fidelity sender | FU-s-1 ports it |
| Playwright split | `infra/aws/ec2/inf-exporter/src/stepwise/orion_export.ts:428-453` (cited by the PRD, not read) | prior art for FU-s-2/3 |
| Start-on-demand Linux boxes | `infra/aws/ec2/EC2_MANIFEST.json` (`cot-exporter`, "started by cot-bd-session-trigger Lambda via SSM doc"); `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf` | prior art for FU-s-7/7/8 |
| Schwab window | `canonical-schwab-ec2/monolith-daily-schedule.tf`: 09:45 / 10:15 / 10:45 UTC = 05:45 / 06:15 / 06:45 ET | C-WINDOW target; Fidelity's generation hour unmeasured until the 2026-10-20 rows |

NOT READ: the Terms of Use or the finding in full; the fork research in full; the HAR captures (not in the repo); `bd-49f-session-chain.tf`, `orion_export.ts`, `EC2_MANIFEST.json` beyond the lines above; `iam.tf`/`monolith-iam.tf`.

## 1. Gates over cells (not cells)

| gate | holder | holds |
|---|---|---|
| L4-R sign-off, both halves | CVO (ratified text), CRO (brief half) | every cut |
| **G-4** Andrew's confirmation of the DONE WHEN lines (open call `e141`) | Andrew | L4-R. The CVO's verdict: before `e141` or `c3a6` closes, no landing cell runs (its LIVE arm) |
| **G-1** MET @bd84d81948: one commit by `4.0.0_SA_CRO~FIDELITY` (C-NAMES, msg 8445): the FIRM scope row `alongside` plus the `_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` entries in both directions | the CRO | nothing now; it fed FU-s-4, FU-s-6 and FU-s-8 |
| **G-2** C-TOU, open call `c3a6`: Andrew's word on automated Wealthscape access, or Fidelity's written approval, or an Integration Xchange transmission standing in for the sign-in | Andrew | the LIVE arm of FU-s-2 and FU-s-3, and FU-x-1. Nothing else waits on it |
| **G-3** the Wealthscape credential written into its Secrets Manager secret | Andrew (never in repo or chat) | the live arm of FU-s-2 |

## 2. The rectangle (round 1 = the thread's hops)

Domain (postulate i): the hops FWD-1 walks: **code read -> session mint -> fetch -> land and record -> box runtime -> setup and schedule -> apply -> the live trace**. Subtracted from the PRD's cell candidates 0-3: candidate 0 = G-1 (a gate); 1 = FU-s-1 + FU-s-2; 2 = FU-s-3 + FU-s-4; 3 = FU-s-5 + FU-s-6 + FU-s-7 + FU-s-8 (the bucket, the box runtime, the root, the apply). The trace is FU-x-1. **9 cells, 4 candidates covered, 0 uncovered.**
Out of round 1 (the next cut): C-BACKFILL (FWD-6); the on-demand chain run with the live schedule read (FWD-2) and the on-demand Monday-export pull landing once (FWD-4), both amended to on-demand at PRD v0.3; the both-run morning (FWD-8; the separate box makes it an observation); the deliberately failed sign-in read (FWD-3's second arm).

Cell ids: `org/standards/DECOMP_CELL_ID_CONVENTION.md` shape 1, `FU-s-<n>` (thread cell), `FU-x-<n>` (closing pass for FWD-<n>). Read against `.tools/proof-of-spec-check.py:657-658`: both match by reading the pattern; the checker has not been run on this file.

| cell | what it builds (one adapter) | write set (disjoint) | PRD rows | risk |
|---|---|---|---|---|
| **FU-s-1** | The Quo reader: given the line id and the Fidelity sender, returns the newest code inside a recency window opened at the SMS-send step; never logs it; a distinct result for "no code arrived" | `infra/aws/ec2/canonical-fidelity/quo_otp.*` | C-SIGNIN (code leg), PRD ruling 5 | LOCAL |
| **FU-s-2** | The session mint: Playwright signs in (password, `OTPSMS`, code from FU-s-1, authorize), keeps a persistent profile or saved state, returns a signed-in context; distinct failures for sign-in refused and code never arrived; records once whether a persisted device cookie skips the SMS step | `infra/aws/ec2/canonical-fidelity/signin.*` | C-SIGNIN (ruling (a)) | WORLD |
| **FU-s-3** | The fetch, inside the minted context: status list for the day, `downloadExport.do` for each of the six files, written to a local directory with a listing file; the directory and listing are the handoff to FU-s-4; distinct failure for "export not generated yet" and "download refused" | `infra/aws/ec2/canonical-fidelity/fetch.*` | C-PULL | WORLD |
| **FU-s-4** | The lander, source-independent: reads the handoff directory (from the fetch, an Integration Xchange drop or a person's download), lands the six files raw once, at the address `address()` returns AT LANDING TIME (never cached, never the monolith path), sha256 per file, business date read from content and checked against `lib/trading_calendar.py`, a re-served day lands once, one run record with the four failure classes | `infra/aws/ec2/canonical-fidelity/land.*` | C-RAW, C-DATE, C-RECORD | WORLD |
| **FU-s-5** | The bucket, ruled by the CTO (msg 8455): a small Terraform root that creates `opal-data-alongside` (name from `name()`; bucket policy with the write grant to the box role only; encryption and public-access block as the other firm buckets carry them) and, in the SAME commit, flips `bucket_provisioned` to true on the `alongside` row; applied under `safe-apply` with a change-management ledger. Runs before any cell that lands bytes | `infra/aws/terraform/<bucket root named by the builder>/`; `infra/logic/registry/scopes.json` (the one flag on the `alongside` row) | C-TENANCY, C-TF | SERVED |
| **FU-s-6** | The box runtime: bootstrap that installs Chromium, Playwright and the runtime on a Linux image, the persistent-profile directory, and a run wrapper that calls fetch then lander at the paths in section 3, fails loud on every "nothing to do" path, and takes no secret from an environment variable | `infra/aws/ec2/canonical-fidelity/box/` | C-SIGNIN, C-ISOLATION (ruling (b)) | LOCAL |
| **FU-s-7** | The Terraform root beside `canonical-schwab-ec2/`: EventBridge schedule, the on-demand start and stop of the box, the box, its SSM-only security group, the Wealthscape secret (metadata only, `prevent_destroy`), per-secret grants (no prefix wildcard), the box role's write grant on `opal-data-alongside` named by `name()` (the bucket itself is FU-s-5's); every name from `name()`; `terraform plan` only | `infra/aws/terraform/<root named by the builder>/` | C-TF, C-WINDOW (cron stated, not fixed), ruling (c) | LOCAL |
| **FU-s-8** | Apply FU-s-7 under `safe-apply` with a change-management ledger opened at start and closed at completion; deploy FU-s-1..4 and FU-s-6's files to the box by a code deploy, never a hand edit | the root's state; the box's code path | C-TF | SERVED |
| **FU-x-1** | Closing pass for FWD-1: one on-demand run through the real chain (start, SSM, wrapper, sign-in, fetch, land, stop); six files listed, downloaded, landed; an analyst-side read opens them; the record shows no person signed in | none (read and run only) | FWD-1 | WORLD |

Hookups that belong to no cell, added by the COO at the merge: the `project.json` `decompositions` line; any registry-generated target the lint demands.

## 3. Dependency edges (keyed to OBSERVED completion, a real data dependency each) and interface bounds

```
FU-s-1 -> FU-s-2                 (the session mint consumes the code reader)
FU-s-2 -> FU-s-3                 (the fetch runs inside the minted context)
FU-s-5 -> FU-s-4                 (the lander lands at the bucket's final address; the bucket exists and the flag is flipped first)
FU-s-3 -> FU-s-8                 (the box deploys the fetch that exists)
FU-s-4 -> FU-s-8                 (the box deploys the lander that exists)
FU-s-6 -> FU-s-8                 (the box deploys the runtime that exists)
FU-s-7 -> FU-s-8                 (the apply applies the root)
FU-s-8 -> FU-x-1                 (the trace runs the deployed chain)
```

**Interface bounds (not edges, so the cells run apart):** the handoff between FU-s-3 and FU-s-4 is a local directory holding the six files as served plus one listing file (fileName, fileType, profileId, requestId, fileCreatedTimestamp); the paths of `signin.*`, `fetch.*` and `land.*` are fixed in section 2 and a task order may not move them; the wrapper calls them in that order.
Maximal paths: `s-1 > s-2 > s-3 > s-8 > x-1`, `s-5 > s-4 > s-8`, `s-6 > s-8`, `s-7 > s-8`. Ready at the cut: FU-s-1, FU-s-5, FU-s-6 and FU-s-7 (G-1 is met). Four chains, so the fanout is about 4 workers against the default cap of 8, stated as `fanout:` data in the issuance commit. FU-s-5 is on the critical path: the lander's task order cannot be worked until the bucket is applied.

## 4. Taxonomy record (rule 24)

- **(i) MECE over a declared domain:** the PRD CONTRACTS rows are 12 (C-TOU, C-NAMES, C-TENANCY, C-SIGNIN, C-PULL, C-RAW, C-DATE, C-RECORD, C-WINDOW, C-ISOLATION, C-TF, C-BACKFILL). Counted by subtraction: C-SIGNIN (FU-s-1, 2, 6), C-PULL (FU-s-3), C-RAW, C-DATE, C-RECORD (FU-s-4), C-TF (FU-s-5, 7, 8), C-WINDOW (FU-s-7, 8), C-ISOLATION (FU-s-6), C-TENANCY (G-1 for the row, FU-s-5 for the bucket); C-NAMES is G-1; C-TOU is G-2; C-BACKFILL is enrichment. 12 accounted, 0 uncovered. Ruling (c) lands in FU-s-6 and FU-s-7.
- **(ii) same grain:** one cell is one adapter with one write set.
- **(iii) intent coherence:** FU-s-7 authors, FU-s-8 applies, FU-s-5 authors and applies one small root because its apply must come first; the fetch and the lander are separate because one serves only the automated path and the other every path.
- **(iv) state coherence:** `complete` on FU-s-2, 3 and 4 does not mean its live arm ran. Each carries a LOCAL/unit arm that proceeds now (fixtures only; the real files hold client PII and are never committed) and a live arm held by G-2 (FU-s-2, 3) or `e141`/`c3a6` (FU-s-4). A task order names which arm it grades.

## 5. Battery (round 1 default)

| lens | disposition |
|---|---|
| `comp-iam` | **RUN** at the cut: the thread touches IAM (FU-s-7). Denominator printed then; not run in this draft |
| `comp-schedule` | DECLARED-NOT-APPLICABLE: thread round; the lens runs on the enrichment round that touches the schedule (FWD-2) |
| `comp-adversary` | DECLARED-NOT-APPLICABLE: same reason |

## 6. Open at the cut (stated, not settled here)

1. **FU-s-5 and FU-s-8 are AWS applies.** CLAUDE.md rule 34 routes every CloudOps order of a macro's projects to `0.7.0_AE_CloudOps~NFRA<n>`. If they are CloudOps orders they go there, not to a worker. Confirm at L6.
2. **Start-on-demand mechanism.** A trigger Lambda via an SSM document (the `cot-exporter` shape) or EventBridge calling SSM Automation is a FU-s-7 design choice; the lead time before the 05:45 ET window is C-WINDOW's, set after the first recurring row.
3. **How the other firm buckets are built.** FU-s-5 says "as the other firm buckets carry them" for encryption and public-access settings; I did not read how they are provisioned, so the worker face must cite the real precedent at the cut. Settled by msg 8455: the bucket is FU-s-5's, not the box root's.
4. **Live landing before `c3a6` closes.** The CVO's verdict holds every landing cell's live arm until `e141` or `c3a6` closes. The CTO's message says the landing cells proceed. This draft reads both as: authoring and fixtures now, the live arm after one of the two calls closes. If the CTO means the live arm too, FU-s-4's live arm is not held by `c3a6`.
5. **The cross-firm gate edit** (`.tools/ds-precommit-check.py`) is in G-1 and the CRO's commit, not a worker cell.
