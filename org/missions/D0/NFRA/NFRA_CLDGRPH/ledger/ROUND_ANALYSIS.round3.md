# NFRA_CLDGRPH -- ROUND-3 ANALYSIS (L10, the CTO's read of the slug) -- 2026-09-04 ~06:5xZ

**Reader:** `1.0.0_SA_CTO` (the single router, spine v3.4 L10). **Slug:** `3.0.0_SA_CVO` message 94101, record
`../surprise-channel/adjudications/ADJUDICATION_v1.md` @8fc3921769 (C-S1..C-S5), `../surprise-channel/remediations/REMEDIATION_v3.md`
(4 rows), clock advances in `REMEDIATION_v1.md` and `REMEDIATION_v2.md`, S31 in `../surprise-channel/investigations/INVESTIGATION_v1.md`.
**Precondition, the gate's own line at the slug commit:** 8 task orders at HEAD on both roots, 0 open; 30 investigation items across 5
channel files, 0 undispositioned. **Judgment criteria owed a grade:** none -- every criterion of C-1 @028be96aef, C-2 @1c0d13904e and
C-3 @aea8346fe1 is invocation-form. **Answer:** the ROUND-N ANALYSIS (below), not a PRD addendum -- every outcome in the header has a
cell that serves it (20 of 20 cells map to an outcome, an input or acceptance 9; 8 of 8 outcomes carry a cell), and the one
addendum candidate the CVO named (S31) is ruled an outside remedy, not a new outcome of this project (section 3).
**Push state at write:** LOCAL; origin/CLOUD @351f309e0a (ls-remote read this session).

## 1. Per outcome: the expectation, what round 3 delivered, what the channel says, what the next drain carries

The read is against the proof-of-spec instances at HEAD (8: V-1, V-2, B-1, B-2, B-3, C-1, C-2, C-3, each VALID at its vintage per the
CVO's re-read with its own instruments), never against the drain report. Cells from `../decompositions/NFRA_CLDGRPH_DECOMP.md` v0.2
(20 cells: CG-s-1..14, CG-x-1/2/4/5/7/8). DONE = a terminal order with a valid instance: **CG-s-1, s-2, s-3, s-4, s-9, s-10, s-11,
s-12, s-13, s-14 (10 of 20).** OPEN: **CG-s-5, s-6, s-7, s-8, x-1, x-2, x-4, x-5, x-7, x-8 (10 of 20).**

| outcome | DONE WHEN | expectation this round | delivered at HEAD | remediations / adjudications | the next drain carries |
|---|---|---|---|---|---|
| FWD-1 ask, be answered | EXERCISED | the serving plane stands (STAGE 2 opens) | CG-s-4 DONE (C-1: the service on `opal-globgrph` answers inside the VPC) | none against it | **CG-s-5** (gateway traversal) then **CG-x-1** (a seat with no graph history asks through the client) |
| FWD-2 newer on the estate's schedule | EXERCISED | the marker path consumes and the worker publishes | CG-s-1, s-2 DONE (B-1, B-2); C-2 the worker's third revision; CG-s-14 DONE at SOURCE (C-3) | S20 REMEDIATED-not-DISARMED and S28 GRADUATED (C-S4): the cloud deriver still runs an image built 21 min BEFORE the C-3 fix; seven task families pull `:latest` | **the rebuild cell** (section 2, item 2) then **CG-x-2** (one unattended night; three limbs) |
| FWD-3 age in plain words | APPLIED | the manifest carries the vintage | CG-s-3 DONE (B-3: artifact-first, pointer-last, vintage in the manifest) | none | **CG-s-6** (the thin client prints the age on every answer) |
| FWD-4 a ceiling the system owns | EXERCISED | the worker's count-guard and fallback exist | CG-s-2 DONE | none | **CG-x-4** after CG-x-2 (one full cycle) |
| FWD-5 a fresh machine is answered | EXERCISED | the service answers; the reach is open | CG-s-4 DONE | none | **CG-s-5**, then **CG-x-5** (a machine with no local DB, proven by `ls`, asks first try) |
| FWD-6 nobody chooses a refresh mode | APPLIED | not this round's | -- | none | **CG-s-6** (no flag, mode or prompt; the absence enumerated) and **CG-s-8** (the retirement, LAST per R7) |
| FWD-7 one graph story, local copy retired | EXERCISED | the served artifact exists | CG-s-3, s-4 DONE | none | **CG-s-8** after CG-x-5, closing on **CG-x-7** (two machines, one answer, local copy off) -- last of the run |
| FWD-8 the operator sees the night | EXERCISED | not this round's | -- | none | **CG-s-7** (the pull-style status read of the pointer's manifest; R4: no alarm, no monitor) then **CG-x-8** |

**Coverage verdict:** no outcome is unserved by a cell; no `DECOMP_INVALIDATING` row in the slug; no cell is invalidated. The decomposition
stands; the recut is a **re-issue over the open cells plus one added cell** (the rebuild), the COO's choice recorded in its issuance commit.

## 2. The five things the slug names, each routed

1. **S26 (C-S1, GRADUATED, ARMED, owner `1.0.0_SA_CTO`) -- the provisioner rewrites the user-bin DACLs on every run.** Measured by the CVO:
   `.tools/provision-path-shims.sh:207` runs `chmod +x` on each forwarder and MSYS emulates the mode by writing a PROTECTED explicit DACL with
   two DENY ACEs (105 of 211 files at 06:05Z, all with 05:20-05:22Z write times; the `.cmd` twins written in the same seconds are clean).
   Neither `icacls` act of S29/S30 could last. **Route: NOT the drain's -- an outside remedy in this seat's own lane (spine 2.4: a disarm in
   place within the owner's lane).** This seat lands the provisioner fix: the mode write without ACL emulation (`MSYS=noacl` around the
   `chmod`, so executability derives from the `#!` header and no explicit DACL is written), and a post-run read that prints
   `protected N of 211` with N expected 0 and each forwarder still resolving from PATH. That read is exercisable now; **the ROW stays
   ARMED until S30's gate -- a fresh Codex seat resolving a shim -- is exercised, which needs a Codex seat Andrew's "kill all the codex
   runtimes" removed; his word relaunches one.**
2. **S28 + S20 (C-S4; owner `2.0.0_SA_COO~A`) -- the cloud deriver runs pre-fix bytes.** `opal-globgrph-derive-runner:latest` = digest 68bd8b93...,
   pushed 18:51:14Z by C-2's build; the C-3 fix b5bc1c8b27 authored 19:12:54Z; nothing pushed since; SEVEN task families pull the tag
   (derive-runner 6, projection-worker 3, serving 1, comp-learns 1, cse 1, fedobs 1, resource-summaries 1). **Route: the drain carries ONE ADDED
   CELL (the COO's to name; CG-s-15 by the convention): a change-managed rebuild (NEVER-2 ledger entry opened at start, closed at completion)
   of the image from a HEAD carrying b5bc1c8b27, THIS PROJECT'S THREE FAMILIES (derive-runner, projection-worker, serving) pinned by DIGEST
   in their task definitions rather than `:latest`, every family's next launch read and recorded, then ONE real cloud derive printing the
   read-versus-unreadable denominator and a NON-ZERO S3_BUCKET-[TRIGGERS]->LAMBDA count for the three declared targets.** That run is
   CG-s-14's closes-on exercised in the cloud (C-3 met it at source) and disarms S20 and S28 in one act. It precedes CG-x-2: a night
   under pre-fix bytes is not the night FWD-2 means.
3. **S27 (C-S3; owner `2.0.0_SA_COO~A`) -- cot-pipeline's only notification resource is EventBridge.** One text correction in CG-s-14's cell at the
   recut (the "three Terraform-declared Lambda targets" read for cot-pipeline is `eventbridge = true`, `s3-notifications.tf:16-19`); no
   Terraform change. **Route: the decomposition at the recut (v0.3), the COO's act.**
4. **S31 (C-S5, GRADUATED, ARMED, owner `1.0.0_SA_CTO`) -- two builds re-pointed a shared `:latest` for seven families and no control could
   see it.** The CVO offered this as a PRD-addendum candidate ("no outcome in v0.4 names deploy isolation between families"). **RULING: not an
   outcome of this project.** The header's eight outcomes are about the graph a reader gets; the tag's reach is a property of the
   estate's image discipline, shared with the producers NFRA_GLOBGRPH owns. Two halves, two owners: the half inside this chain is the
   DIGEST PIN for this project's three families, carried in item 2's cell; the half outside is a NEVER-2 discipline line -- **an image act
   names every task family that pulls the tag it moves, in its ledger entry** -- which this seat lands as law (CLAUDE.md NEVER-2 annex,
   `org/critical_paths/change_management/`), a law edit with its broadcast, owed at this seat. S31 disarms on both halves.
5. **S8's second-order question (reserved by round 1, answered by no row) -- why the derive source carried ~2,256 duplicate edge identities
   (60,688 MERGE attempts, 58,432 stored).** The manifest semantics are fixed (S8 closed). The SOURCE is the producers' output upstream of
   the projection -- outside this project's chain. **Route: not recut here; named to `4.0.0_SA_CRO` as an L1 brief candidate on the producer
   surface (NFRA_GLOBGRPH / NFRA_GRAPHS owner).** A row citing it against any FWD above is misrouted.

## 3. Instruments and their findings, carried not routed

- The C coordinate's first live exercise: 5 of 5 CVO rows admitted under `adjudications/` with `C-` ids (the schema half @e3e999c139 and the
  gate half @6efb43b9d0 composed). The in-place rule: 8 refusals then 8 admissions, red before green.
- `org/surprise_channel/surprise-watch.sh` WARNs "MUTATED in place" on a lawful clock-only advance -- the CVO's instrument, owed by the CVO.
- The seven-family count corrects the 08-26 ledger's five; carried into item 2's cell text, not a row.

## 4. Handoff

`dep_stage: ROUND_CLOSE` on this commit (the row owner). This file and `REMEDIATION_v3.md` go to `2.0.0_SA_COO~A` in the CTO's one message
of the round; the COO recuts as ONE issuance under L6 covering every affected cell (the ten open cells in dependency order per the decomposition's
rounds 3-4, plus the added rebuild cell ahead of CG-x-2), under spine v3.4: every worker order carries its `<paths>` block, rows mint
`NFRA_CLDGRPH-W<n>-S<k>`, the drain merges through `.tools/safe-merge.sh`. `dep_stage: EXECUTING` is the COO's flip in the issuance commit.
