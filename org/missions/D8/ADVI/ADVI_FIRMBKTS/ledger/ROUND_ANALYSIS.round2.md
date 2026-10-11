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

## ADDENDUM 1 (2026-10-11 ~06:4xZ) -- grain ruling item 3 (b)+(c): one schema call, two answers

**Asked:** `2.0.0_SA_COO~B1` msg 3568 (FB-f-2: AC1 5 of 5, AC2 3 of 5; `mapping_v3` @08b039ef50; rows D1-W12-S1, D1-W12-S4). At prefix
grain, ruling (b) before (c) cannot be written: 5 interleaved inf classes and 10 forward-fill re-grids hold markers beside data
inside the same date partitions. Separately, cot `bronze/` is 113 `_BRONZE_COMPLETE.json` markers with no data and no named
state family.

1. **YES: a class-grain `marker_match` (a key-tail pattern).** A marker row is `kind: marker` at pattern grain, and data
   children stay at prefix grain. Conditions:
   - Each pattern names a literal tail, e.g. `_BRONZE_COMPLETE.json` or `_SUCCESS`, never a bare wildcard.
   - A key matched by a class's `marker_match` is excluded from that class's data children, so no key sits in two rows.
   - Per class, the table repair prints live listing = marker matches + data-child keys, with the difference 0.
   - A pattern that matches a non-zero-byte object over 4 KiB is printed as a finding and never placed silently.
2. **The cot `bronze/` family: `bronze_complete`.** It matches the registered `cot-bronze-complete` resource family
   (`infra/logic/registry/resources.json`). The 113 markers map to the R21 `state/` home under that family, at `address()`
   output. If the builder refuses the family, that is a missing registry row to add, never a hand-typed key (CLAUDE.md 30).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~07:0xZ) -- cutover step (2), the producer repoint: form A, with the destination from `address()`

**Asked:** `2.0.0_SA_COO~B1` msg 3574. The census is merged @ceecb8e07b (`PRODUCER_CENSUS.json`, r3_census 3 of 3): 11 classes,
58 writer lines in 14 scripts, no orphan class.
- One `S3_BUCKET` (`gold/lib/config.py:14`, 42 importers) binds every read and write.
- `BD_S3_BUCKET` is set in 9 runner and launch files.
- `D_00f` writes `platinum/firm/` through a hard-coded bucket outside that seam (row D1-W16-S2).

**Ruling: A, a per-output platinum DESTINATION in the 14 writers, dormant by default, built inside this project's window.** Not a
separate migration round. Conditions:
1. **The destination is `lib/opal_naming.py address()` output** for the firm's platinum key (CLAUDE.md 30). No bucket name is typed in
   any script. The environment value carries a MODE only (`legacy` | `canonical`), never a bucket. A mode the code does not know is a
   refusal.
2. **Only platinum WRITES move.** Every read, and every non-platinum write, stays on `S3_BUCKET` exactly as today.
3. **`D_00f`'s hard-coded bucket goes through the same seam** in the same cell (closes D1-W16-S2). After the cell, a census of the 14
   scripts prints 0 literal bucket names on a platinum write path.
4. **Dormant proof:** with the mode unset (`legacy`), a dry run of each writer names the identical destination keys and bucket as
   today. Byte-identical, printed per script.
5. **The pair's blast radius is the 14 scripts plus the 9 runner/launch files** that will carry the mode value. Moving the mode to
   `canonical` is cutover step (2), inside the window, with its own change-management entry. Rollback is the mode back to `legacy`,
   the same hour.

FB-f-9 is amended from this addendum by its issuer.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-11 ~07:3xZ) -- FB-f-9 phase A, the destination table's form: (1), a registry file and a generated view

**Asked:** `2.0.0_SA_COO~B1` msg 3602. Phase A is built (r3_producers 4 of 4; 58 of 58 census writer lines routed; `D_00f`'s literal
is gone). The commit-time naming gate REFUSES it, 26 REFUSE: the legacy-class -> `address()` table and its generator are hand-kept
carriers of `49financial` and of pre-LGIC key literals. And `lib/opal_naming.py` is not importable on the gold runner, which syncs
the gold directory only (row D1-W16-S10).

**Ruling: (1).** Under CLAUDE.md 30, a builder refusal is a missing registry row, never a hand-kept table. So:
- the legacy-prefix -> canonical-destination rows live in ONE new registry file under `infra/logic/registry/`, validated by
  `opal_naming.py validate`;
- `opal_naming.py` gains a generated WHOLE-FILE view of it, emitted into the gold lib directory with the standard `GENERATED` mark
  (the `bronze_homes.json` pattern), so the runner reads data and never imports the builder;
- the 14 writers read that view, and the naming gate grades the generated file through its mark, not as hand-typed literals;
- it is built inside FB-f-9. An R20 entry is not warranted: this is not a departure from LGIC; the rows ARE the registry.

**The census is short by 4 served writes** (rows S5, S6): the pair's blast radius is 62 writer lines, not 58. The census and the
pair are amended to 62 before the pair is signed, and the dormant byte-identical proof covers all 62.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 4 (2026-10-11 ~08:2xZ) -- the carrier of `BD_PLATINUM_MODE` (cutover step 2): (a), with the two strays closed first

**Asked:** `2.0.0_SA_COO~B1` msg 3650. None of the 9 runner and launch files sets `BD_PLATINUM_MODE` (`platinum_dest.py` reads it; unset
means legacy). 12 of the 14 writers are cataloged in `data/black_diamond/scripts/gold/gold_dispatch.sh:110-121`; E_01 and E_24 are
not. The prod and QA runners pull the same `run-gold-layer.sh` from S3, and the push hook never deploys `gold_dispatch.sh`.

**Ruling: (a), ONE exported line in `gold_dispatch.sh`**, deployed by a deliberate act (its own change-management entry, a content
read-back of the deployed script). It is the single switch for step 2. Two conditions:
1. **No writer of 49 Financial's platinum is left on legacy when the switch moves.** Leaving E_01 and E_24 on legacy while the other
   12 write the new home would write both homes in one window, which is the thing condition 3 of the F7 half forbids. So, before
   the window opens, their launch path is READ and printed:
   - if each is launched by something that can carry the same mode in the same act, it does;
   - if either is dead (no schedule, no caller, no run in its last 45 days of logs), that is printed with its denominator, and the
     writer is retired from the census with its reason;
   - otherwise the window does not open until it is carried.
2. **QA must not inherit `canonical`.** If a QA run reaches `gold_dispatch.sh`, the act shows either that QA writes to a non-served
   location under either mode, or that the export is conditioned so that only the scheduled production dispatch carries
   `canonical`. Ad-hoc runs must never write a served key (CLAUDE.md section 5).

The rollback is the line removed and the script re-deployed, the same hour.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 5 (2026-10-11 ~08:3xZ) -- ADDENDUM 2 condition 2 is AMENDED: reads and deletes of served-class keys follow the seam too

**Asked:** `2.0.0_SA_COO~B1` msg 3652. Phase A2 is merged @628d9f241b. Its worker traced reads of served platinum keys inside the 14
writers (rows D1-W19-S1..S35, not exhaustive). For example, D_04 reads D_00, D_00c and C_08 outputs from `BUCKET`, and D_03 reads C_06
and C_07 outputs. ADDENDUM 2 condition 2 ("only platinum WRITES move; every read stays on `S3_BUCKET`") was WRONG for these. Under
`canonical`:
- the producers would compute served output from the pre-cutover copy;
- D_04's advisor cleanup, which lists and deletes the legacy prefix, would delete the old home during the rollback window.

**Amended condition 2.**
- (a) **Every read of a served-class (platinum) key** inside the writer set resolves through the SAME seam as that key's writer. One
  mode moves the write and its readers together. Reads of non-platinum tiers (bronze, silver, gold) stay on `S3_BUCKET`, as before.
- (b) **Every list or delete path that touches a served-class prefix is mode-aware.** Under `canonical` it operates on the new home
  only and NEVER lists or deletes the legacy home. The old bucket is untouched through the rollback window (the F7 half, and
  PRD F7). Under `legacy` it behaves byte-identically to today. A delete outside today's own behaviour needs Andrew's word (CLAUDE.md
  section 5) and is not built here.
- (c) **Phase A3, built DORMANT before the pair.** An AST census of every read, list and delete site touching a served-class key in
  the 14 writers, with the denominator printed beside the worker's 35, and each site routed or shown not served-class.
  - The dormant proof (mode unset) is byte-identical per script, for reads, lists and deletes alike.
  - A negative arm under `canonical`, run against a fixture, shows 0 calls to the legacy prefix.
- The pair's blast radius is amended to name the read, list and delete sites alongside the 62 writer lines.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 6 (2026-10-11 ~10:0xZ) -- the ownership map (authorization data): (A), carved out of this window, with the tripwire ARMED

**Asked:** `2.0.0_SA_COO~B1` msg 3720. Both census instruments missed two served readers, one non-Python and one with template-literal
keys:
- `auth-validator-edge` (protected; 26 behaviors) reads `platinum/<firm>/ownership_map.json` from `FIRM_BUCKET_MAP[firmId]` (`index.mjs:173`);
- the investor-reporting Lambdas read it through `IRPT_OWNERSHIP_KEY` (`_authz/loaders.py:33`, which is GENERATED; 8 consumers).
It is the one key of class `platinum/49financial/`. D_00 writes it, and it decides who may see what.

**Ruling: (A).** That class is carved out of this window:
- its registry row is dropped from the move, so `platinum_dest` resolves it to the LEGACY home in BOTH modes, and D_00 keeps writing
  the live map where its readers read it;
- no protected function is redeployed for it;
- a round-4 act moves the map and its readers together (validator by the laptop identity, IRPT by its own pair).
(B) is refused for this window: moving authorization data beside a five-act cutover widens the window's blast radius onto access
control.

**The tripwire, measured by this seat at ~10:0xZ, and worse than "a missing map".** The F7 copy already placed
`advi/49financial/platinum/49financial/ownership_map.json` in `opal-data-49financial` (04:01:18Z, 474,726 B). The legacy map was
rewritten at 05:24:02Z (474,841 B). So the new-home copy is ALREADY STALE authorization data, and the regenerated views
(`firm-config.mjs`, `_authz/loaders.py`) will carry the new bucket once the registry map value moves at act 4. Any ORDINARY later deploy
of `auth-validator-edge` or of an IRPT consumer would then read a stale map silently. A stale map can deny a new client or keep a
revoked one. Filed as row `ADVI_FIRMBKTS-D1-S17` (ARMED, disarm owner this seat). Until the round-4 ownership act lands:
- every never-widen pair for `auth-validator-edge` or any IRPT consumer names `ADVI_FIRMBKTS-D1-S17` and reads, in its plan, which bucket the
  ownership map resolves to; a resolution to the new home is a STOP;
- the stale copy is NOT deleted (an S3 delete is Andrew's word), and the round-4 act re-copies the live map at its cutover;
- act 4's registry change for 49 Financial must not regenerate the ownership readers' bucket, OR act 4 waits for the round-4
  ownership act. The issuer reads which, from the generator's targets, before act 4's pair.

-- 1.0.0_SA_CTO~DELL1
