# ADVI_FIRMBKTS -- ROUND 2, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~05:4xZ)

**Inputs:**
- `3.0.0_SA_CVO` slug msg 3519: `surprise-channel/adjudications/ADJUDICATION_v3.md` and `remediations/REMEDIATION_v3.md`
  @ff86d9f579 (MAY-CLOSE; 24 rows dispositioned; no BLOCKING or ARMED row open);
- the issuer packet `deliverables/2.0.0_SA_COO~B1/round2/R2_CLOSE.md` @27bd0e5f9e;
- this seat's WORLD read `ledger/R2_CTO_WORLD_READ_FB_E5_FB_E6_20261011.md` @36ecbc2323.

**PRD header:** `fabric` is moved from `laptop` to `dell1` to match `project.json`. This is a header-only edit and re-opens no
half; `prd-signoff.py status` reads both halves `current` after it.

## 1. Graded

- **FWD-1 (the thread): PARTIAL.** Canonical arm: the readers agree on all four fields at 195 of 209, and both are right at
  193 of 207. The contents clause is MET on the CVO's read; round 1's gap there is closed. Independence is NOT MET: both readers
  were subagents of the issuing session, and nothing could show which files a reader opened (row D1-S3 stays OPEN). The ruling
  in section 2 makes independence a property of the reader's disk, not of its instructions.
- **FWD-2 (the table): enriched, not graded.** 444 census classes: MOVE 212, HOME 110, RETIRE 85, DECISION 2, FAULT 89. 168 of
  round 1's 226 FAULT classes are re-gridded or placed, and the 28 collisions are ruled at a measured overlap of 0. The 89 are
  ruled by grain in section 2.
- **F4's negative arm: EXERCISED.** An `irpt-cot-ycharts-research-role` session was refused ListObjectsV2 on
  `opal-data-inflection` by the explicit resource-policy deny. The own-firm admit is still shown only by policy text (row
  D1-W7-S1; section 2).
- **F7's copy: EXACT to its manifest.** On this seat's own listing, 52,910 of 52,910 objects equal the manifest; the one
  multipart key was checked by sha256 against its manifest version. The snapshot is already stale (a source rewrite at
  05:10:08Z), as the F7 half conditioned. The CVO's 05:18Z `COPY-NOT-COMPLETE` is the instrument's fault: it hashes the
  current source, not the manifest version (row D1-C-S7, the COO's). Nothing reads the prefix.
- **F6: built DORMANT.** The live router `:26` lacks `handleWithMap`, and HEAD has it.

## 2. Rulings (the rows REMEDIATION_v3 names to this seat)

1. **The cutover family (D1-S4, D1-S7, D1-S9): D1-S8's step (4) names BOTH gates.** The v3 router activates the canonical path
   only when `CANONICAL_PLATINUM_BUCKETS` (`index.mjs:128`, `Object.freeze([])` today) lists the bucket AND
   `FIRM_BUCKET_MAP[scope]` resolves to it. Step (4) is therefore: add `opal-data-49financial` to the list, move the 49 Financial
   map value, and deploy F6, all in one never-widen pair. The staff proxy's requests (`?firm=49financial`) are read before and
   after (closes D1-S7). The window's order is unchanged:
   1. the advTenant remedy;
   2. F10's platinum producers repoint to `address()` keys;
   3. a delta copy against a fresh manifest, whose compare reads destination-vs-manifest apart from source drift (D1-C-S7's
      fix);
   4. the list entry, the map value and the F6 deploy.
   No act opens before its change-management entry, per the WORLD read's waiver condition. D1-S9 closes on this text.
2. **The router goes all-ASCII at F6's deploy (D1-W9-S1).** The 5 pre-existing non-ASCII comment lines are replaced in the
   same cell that deploys F6: "all non-ASCII out", the first of the two safe moves in CLAUDE.md section 4. Close: the deployed
   file reads 0 bytes above 127.
3. **The FAULT grain (D1-W4-S2..S6), one rule per shape:**
   - (a) **A zero-byte object whose key equals its class prefix** (a folder placeholder) is RETIRE. It holds no data. This
     unblocks `bd gold/clients/` (2,949 objects), which stays FAULT today only because of such a marker (W4-S3).
   - (b) **Completion markers (`state/complete` groups)** carry `kind: marker` in the table and map to the R21 `state/` home of
     the class they mark. They are never re-gridded beside data (W4-S2).
   - (c) **Classes that interleave markers and data** are split by (b), then re-gridded PER DATE PARTITION with no child cap.
     The 25-child limit was a worker's choice, not a rule (W4-S5: 6 classes, 23,977 objects).
   - (d) **A new class that collides with a round-1 placed class** follows round 1's collision rule: a deliberate merge with
     its reason, or a split, decided at a measured key overlap. The round-1 row is not displaced by default (W4-S4).
   - (e) **Denominators:** the re-grid counts against the live listing; the census stays the census. Each table repair prints
     both and their difference (W4-S6, closed by this ruling).
   Close: the round-3 table repair applies (a)-(d) and prints FAULT before and after, with an owner on every remaining class.
4. **F4's own-firm admit must be EXERCISED; the policy text is not sufficient (D1-W7-S1).** The difference control needs one
   read that SUCCEEDS through the fence: a principal whose identity policy grants a read on `opal-data-cottonwood` and that the
   fence admits, as a named act printed with its ARN. If no such principal exists, the cell says so, and that is a finding
   against F4's serving grants, not a waiver.
5. **The gate disagreement (D1-S10) is not this project's cell.** `round-close-check.py` and `to-pipeline-gate.py` must resolve
   a proof instance by one rule. Build ladder rung 2: `round-close-check.py` adopts the gate's resolver (the stem, or the path in
   the order's proof block). It goes to the gate owner as one surprise row on that tool's own channel. Until it lands, the COO's
   cut names the stem in every worker order.
6. **F4's PRD wording (D1-S1, open limb).** The premise "the fence denies `s3:*` to every identity this estate holds" is false
   at HEAD: the admit list carries named users and both CloudOps users, and F4 runs as adopt-and-repair with an exercised pair
   (item 4 above and section 1). The ENDPOINT is unchanged. The text edit sits in `CELL CANDIDATES` (the BRIEF half). It lands
   as an addendum AFTER the round-3 issuance, so that a re-hash cannot refuse that issuance at LIMB 6. Until then this paragraph
   is the operative reading.

## 3. ENRICHMENT LIST (round 3, ONE issuance by `2.0.0_SA_COO~B1`)

1. **The cutover window for 49 Financial (FWD-4, F7 + F10 + F6), section 2 item 1.** Four acts in order, each with its own
   never-widen pair and change-management entry opened first. The window closes when a firm session and the staff proxy read
   byte-identical pages through the page's own route before and after, every served key answers from `opal-data-49financial`,
   and nothing writes the old platinum keys after step (2). The old bucket is untouched through the rollback window.
2. **The F7 compare instrument (D1-C-S7)** reads the manifest's source VersionId and prints destination-vs-manifest apart from
   source drift. It lands before step (3) uses it.
3. **The table repair under the grain ruling (FWD-2), section 2 item 3.**
4. **FWD-1's independence, by construction.** Each reader works in a worktree whose sparse checkout holds ONLY the location
   list (no `org/`, no `docs/`, no project folder), so the forbidden files are absent from its disk. The CVO lists each reader's
   worktree before grading. Same grading as round 2, with denominators printed.
5. **F4's own-firm admit, exercised** (section 2 item 4).

Every invocation in the round-3 orders carries an absolute worktree root (D1-W9-S2, the COO's).

## 4. ACTS ONLY ANDREW CAN DO (cited)

- FWD-7 and FWD-8, the prohibited key and B2 (DEC-13). Every act on `opal-data-inf` waits on them.

-- 1.0.0_SA_CTO~DELL1
