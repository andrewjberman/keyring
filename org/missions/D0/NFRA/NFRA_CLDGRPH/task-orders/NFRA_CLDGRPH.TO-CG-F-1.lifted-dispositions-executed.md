# TO NFRA_CLDGRPH.TO-CG-F-1 -- CG-s-21 (ADDED at decomposition v0.6 on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S21): THE LIFTED DISPOSITIONS EXECUTED -- `kuzu_db` RETIRED WITH A TOMBSTONE naming its tarball `snapshots/20260612/graph-20260612.tar.gz`; `kuzu_ac7.db` ARCHIVED to S3 under NFRA_GLOBGRPH.ITEM-3 and then removed locally; `kuzu_load.py` RETIRED (no named reader exists); nothing deleted before its archive object is verified by head-object; the reader census still 0 with its control; `ls -d` reads 0 of 2 stores beside a positive control. FWD-7's EXISTENCE clause

<to_id>NFRA_CLDGRPH.TO-CG-F-1</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~1</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-09</issued_date>
<status>complete -- FLIPPED 2026-09-09T18:4xZ by 0.9.0_WK_NFRA_CLDGRPH~1 on branch wk-cldgrph-6-1 (push state LOCAL). The acts are commit dcdf0581b1 (the archive, the tombstone, the builder's removal, the deletions and the W1-S32 row); this flip and the proof instance are the second commit. The instance org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-F-1.lifted-dispositions-executed.proof_of_spec.json validates VALID rc 0 on F1-AC1,F1-AC2,F1-AC3,F1-AC4,F1-AC5,F1-AC6, and every MECHANICAL row reads PASS by its own output: F1-AC1 STORES_PRESENT=0 of 2 with STORE_PROBE_CONTROL=FIRED; F1-AC2 TARBALL_PRESENT=true size=71671 and ARCHIVE_OBJECTS=2 of 2 sha256_match=2 of 2; F1-AC3 READERS=0 of 486 files, BUILDER_PRESENT=false, both reader controls FIRED; F1-AC4 TOMBSTONE_PRESENT=true with 8 of 8 fields and TOMBSTONE_PROBE_CONTROL=FIRED; F1-AC5 BUILDER_AT_HEAD_RC=128. F1-AC6 is judgment=true and carries its reading with NO verdict, status UNVERIFIABLE-BY-INSTRUMENT naming 3.0.0_SA_CVO at L9. One surprise row filed, NFRA_CLDGRPH-W1-S32 (OBSERVATION, INERT). ISSUED AS: pending -- GO = the spawn (spine v3 L7): slot ~1 on a fresh worktree from CLOUD at this issuance. ROUND 6 of NFRA_CLDGRPH (the recut as ONE issuance on the CTO's round-5 analysis @30027295be / msg 94610; FWD-7 NOT_REALIZED by two OWNED acts, this is the first). Slot ~1's FIRST order; TO-CG-F-2 (the site-Z exercise, laptop half) follows on the same subagent after this order's drain, and its instants are FIXED (19:00Z, 20:00Z, 21:00Z today) -- this order is cut to finish before them. PREMISE RE-GROUND at hand-off: the two stores present in the MAIN workspace by absolute path (`ls -d C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/globgrph/kuzu_db C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/globgrph/kuzu_ac7.db`); the tarball present in S3 (head-object 71,671 B, 2026-06-12); the P7 hold LIFTED by its author at C-S26 (read it in ADJUDICATION_v1.md at your HEAD); if any fails, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS; a FAIL row leaves the order open as the final report; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.6 @`30027295be` (FWD-7 existence; s.7 row S21) · **Decomp cell:** `CG-s-21` (decomposition v0.6, this recut) · **Lane:** `0.8.0_AE_CloudComp` -- the local graph builders under `infra/aws/globgrph/` · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~1`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~1 <0.9.0_WK_NFRA_CLDGRPH~1@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/`.** The two stores and their manifests live in the MAIN workspace (gitignored): you READ them by absolute path, you UPLOAD the archive object, and you DELETE them there ONLY after the archive object is verified -- the one act this round's law permits on the main workspace, on the CVO's lifted hold (C-S26) and the CTO's row S21. Nothing else in the main workspace is touched.
- **Every probe, capture or script you write carries `f1_` in its name** (three rounds of a slot folder reused across orders collided on generic names: W1-S31, W2-S34, W3-S13). Scratch: `<your worktree>/.scratch/` only.
- **Surprise = ONE ROW, never a message.** Append to `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` inside the fenced json array, per `org/surprise_channel/schemas/investigation_item.schema.json`; id `NFRA_CLDGRPH-W1-S<k>`, `<k>` the next unused within W1 (W1-S1..S31 exist at HEAD; start at S32); restate the header denominator by parsing every fenced block (151 rows at this cut); never edit an existing row; keep working.
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most. The S3 upload may use `timeout 600`.
- **NEVER:** delete a store before its archive object (or, for `kuzu_db`, the tarball it is reproducible from) is verified by head-object with a printed size and checksum; open a store with an engine (`kuzu.Database` CREATES an absent store; counts come from manifests); run any loader; write anything but the archive objects to S3 (bucket `opal-313476888678-globgrph` is NOT the bucket -- the bucket is `opal-313476888478-globgrph`; a typo'd bucket is a BLOCKING row, never a retry with a guess); touch `kuzu_stitch_db` (S26's, LAST in the chain), the cloud engine or the thin client; non-ASCII in code; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read <file> --for "..."` / `--enumerate '<regex>'`; `python .tools/comp-find '<pattern>' <pathspec>`; raw recursive grep/find in Bash is refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws` (CLI v1; `--output text` rows end in CR). Region us-east-1, account 313476888478.

## THE CELL (decomposition v0.6, this recut, s.1a; PRD v0.6 s.7 row S21 verbatim in its accept)

> **CG-s-21** | S21 EXECUTE THE LIFTED DISPOSITIONS (E-3's, the P7 hold lifted by its author at C-S26): `kuzu_db` RETIRE_WITH_TOMBSTONE naming `snapshots/20260612/graph-20260612.tar.gz` (present in S3, 71,671 B, 2026-06-12); `kuzu_ac7.db` ARCHIVED under NFRA_GLOBGRPH.ITEM-3 then removed locally; `kuzu_load.py` retired or rescoped to a NAMED reader -- a builder beside the projection is the path back | FWD-7 (existence) | claim: measured (0 readers of 487 files by AST and 0 of 982 by comp-find, C-S26; both stores still on disk) | status: OPEN -- ROUND 6 (recut) | lane `0.8.0_AE_CloudComp` | placement laptop | depends_on: CG-s-19 -> DONE (the dispositions recorded; the hold lifted) | **closes on (the PRD's accept, verbatim):** `ls -d` reads 0 of 2 stores on this device beside a positive control; the tarball and the archive objects present by head-object with their sha256 in the tombstone/manifest; the reader census still 0 with its control; NOTHING deleted before its archive object is verified

**THE CTO's reason (round-5 analysis s.2):** *the EXISTENCE clause -- no second, older copy anyone could still be reading from -- is met only when the LIFTED dispositions are EXECUTED; a builder beside the projection is the path back.*

## MEASURED BY THE ISSUER AT THE CUT (2026-09-09 ~17:5xZ), so you do not spend a discovery step on it

- **`kuzu_db`** (main workspace): 9,224,192 B, mtime 2026-06-12 09:55 local; manifest `kuzu_db._build_manifest.json` (403 B after E-3's claim fields: `built_at 2026-06-12T13:55:02Z`, `node_count 1166`, `edge_count 2488`, `edge_count_claim merge_attempts`, `artifact_claim historical`, `source_kind tarball`, `source_vintage.tarball_key snapshots/20260612/graph-20260612.tar.gz`). **The tarball it is reproducible from** is in S3 NOW: `s3://opal-313476888478-globgrph/snapshots/20260612/graph-20260612.tar.gz`, head-object at the cut: ContentLength 71,671, LastModified 2026-06-12T02:02:27Z, ETag `3925738fbea21729290cf6d9ae640e3d`. The CVO's C-S26 lifted P7 on exactly this reproducibility. **Disposition: RETIRE_WITH_TOMBSTONE** -- no archive upload for `kuzu_db` (the tarball IS its archive); the tombstone cites the tarball's key, size, ETag and the manifest content verbatim.
- **`kuzu_ac7.db`** (main workspace): 4,050,944 B, mtime 2026-06-12 10:57 local; E-3 wrote a CLAIM CARD beside it (`kuzu_ac7.db._build_manifest.json`, 908 B: `artifact_claim historical`, `edge_count_claim unknown`, `source unknown`, no counts). Its builder was NFRA_GLOBGRPH.ITEM-3 (`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/NFRA_GLOBGRPH.ITEM-3.ae-kuzu-cypher-load.md`, June 2026); the empty dir `kuzu_ac7/` (2026-06-09) beside it. **Disposition: ARCHIVE then REMOVE** -- the archive key `s3://opal-313476888478-globgrph/archive/NFRA_GLOBGRPH.ITEM-3/kuzu_ac7.db` + `.../kuzu_ac7.db._build_manifest.json` (the claim card travels with it); upload with `--checksum-algorithm SHA256` if the CLI supports it, else compute sha256 locally BEFORE the upload and after a head-object, put the sha256 in the archive manifest and the tombstone; delete the local files and the empty dir only after head-object returns the size you uploaded.
- **`kuzu_load.py`** (tracked; E-3's disposition KEEP_WITH_NAMED_READER named NO reader -- it named the store's own builder). The CTO's row: *retired or rescoped to a NAMED reader; a builder beside the projection is the path back.* No reader exists (0 of 487 by AST, 0 of 982 by comp-find). **Disposition: RETIRE** -- `git rm infra/aws/globgrph/kuzu_load.py`; its methodology is preserved in git at HEAD~ (cite the hash) and in the tombstone; `kuzu_load.py`'s `_stamp_claim` helper (E-3's) retires with it -- S27 (a sibling order, slot ~3) moves the claim into `_provenance.write_manifest` for every producer, so nothing depends on this file's helper after this round. If you find a LIVE reader by AST (your own census), that is a row and the disposition becomes RESCOPE, not RETIRE -- say which.
- **The reader census** (C-S26; E-3's `no_readers.sh` @d3a03a7b7b): `READERS=0 of 487 files` over `.tools org/modules/graph org/modules/heatmap infra/aws/globgrph` with the builder declared. Re-run it (your own `f1_no_readers.sh`, the same AST walk) at your HEAD AFTER `kuzu_load.py` is removed: the builder exclusion is then empty and the census must still read 0.
- **The tombstone** is a TRACKED file at `infra/aws/globgrph/kuzu_db.TOMBSTONE.md` (in `<paths>`): what was retired, when, on whose word (Andrew @61d5ef55dd for the canonical copy; the CVO's C-S26 lift for these), the tarball key + size + ETag, the manifest quoted, the archive keys and sha256 for `kuzu_ac7.db`, and the retired builder's last hash. A reader who finds the store gone reads why here.

## DELIVERABLE -- in this order

1. **Verify BEFORE anything moves:** head-object on the tarball (size, ETag); `ls -d` + sizes + sha256 of both local stores and their manifests (`f1_before.txt`).
2. **Archive `kuzu_ac7.db`** + its claim card to the ITEM-3 key; head-object both; sha256 equality printed (`f1_archive.txt`).
3. **The tombstone** written; **`kuzu_load.py` retired** (`git rm`), `bash .tools/commit-gate.sh` not needed for a removed file; the reader census re-run.
4. **Delete** `kuzu_db`, `kuzu_db._build_manifest.json`, `kuzu_ac7.db`, `kuzu_ac7.db._build_manifest.json`, the empty `kuzu_ac7/` -- ONLY after steps 1-3; `ls -d` after (`f1_after.txt`).
5. **The record** `CG-s-21.lifted-dispositions-executed.result.md`: one fenced JSON block (per artifact: before size/sha256/mtime, the archive key + head-object result, the disposition executed, the after state; the tarball's head-object; the tombstone path; the builder's last hash) then prose. Then the proof instance, validate, and -- ONLY if every mechanical row is PASS -- flip and commit (instance, deliverables, the tombstone, the removal, the flip together).

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="F1-AC1" cell_refs="CG-s-21"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/f1_stores_absent.sh</invocation><expect>STORES_PRESENT=0 of 2[\s\S]*STORE_PROBE_CONTROL=FIRED</expect></criterion>
`F1-AC1` -- BOTH STORES ABSENT ON THIS DEVICE: `ls -d` by absolute path on `kuzu_db` and `kuzu_ac7.db` (and their manifests and the empty dir, printed) reads 0 of 2, beside a positive control (`ls -d` on a path that IS present in the same directory, e.g. `projection_client.py`, prints it).

<criterion id="F1-AC2" cell_refs="CG-s-21"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/f1_archives_verified.sh</invocation><expect>TARBALL_PRESENT=true size=71671[\s\S]*ARCHIVE_OBJECTS=2 of 2 sha256_match=2 of 2</expect></criterion>
`F1-AC2` -- THE ARCHIVE OBJECTS ARE VERIFIED BY HEAD-OBJECT: the tarball present at its key with the size the cut measured; the two `kuzu_ac7.db` archive objects present with sizes equal to the uploaded files and sha256 equal to the pre-upload local sha256 recorded in the tombstone (`sha256_match=2 of 2`; a mismatch is FAIL, and the local files would then NOT have been deleted -- say so).

<criterion id="F1-AC3" cell_refs="CG-s-21"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/f1_no_readers.sh</invocation><expect>READERS=0 of [0-9]+ files[\s\S]*BUILDER_PRESENT=false[\s\S]*READER_PROBE_CONTROL=FIRED[\s\S]*READER_BAND_CONTROL=FIRED</expect></criterion>
`F1-AC3` -- ZERO READERS AND NO BUILDER: the AST walk over the tool homes for a path or open naming `kuzu_db` or `kuzu_ac7` in CODE reads 0, `kuzu_load.py` absent at HEAD (`BUILDER_PRESENT=false`), the planted reader caught, the docstring mention not counted.

<criterion id="F1-AC4" cell_refs="CG-s-21"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/f1_tombstone.sh</invocation><expect>TOMBSTONE_PRESENT=true[\s\S]*TOMBSTONE_NAMES=tarball_key,tarball_size,tarball_etag,manifest,archive_keys,archive_sha256,builder_last_hash,authority[\s\S]*TOMBSTONE_PROBE_CONTROL=FIRED</expect></criterion>
`F1-AC4` -- THE TOMBSTONE CARRIES EVERY FIELD A READER NEEDS: tracked at `infra/aws/globgrph/kuzu_db.TOMBSTONE.md`, its fenced JSON parsed for the eight named fields; a planted tombstone missing one field is caught.

<criterion id="F1-AC5" cell_refs="CG-s-21"><invocation>git show HEAD:infra/aws/globgrph/kuzu_load.py; echo BUILDER_AT_HEAD_RC=$?</invocation><expect>BUILDER_AT_HEAD_RC=128$</expect></criterion>
`F1-AC5` -- THE BUILDER IS RETIRED AT HEAD (`git show` fails on the removed path; the last hash carrying it is in the tombstone). If the disposition became RESCOPE (a live reader found), this criterion is the one that FAILS honestly and the row says why.

<criterion id="F1-AC6" cell_refs="CG-s-21" judgment="true"/> `F1-AC6` -- THE EXISTENCE READING: whether "no second, older copy anyone could still be reading from" is now TRUE on this device for the canonical graph (the two stores gone; the stitch store deliberately NOT touched -- S26's, last in its chain -- and said so); what the tarball's continued presence in S3 means for that clause (reproducible is not the same as present); what would make the reading false again (a builder re-landing; the stitch store). A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>F1-AC1, F1-AC2, F1-AC3, F1-AC4, F1-AC5, F1-AC6</expected_criteria>

## SURFACES

`infra/aws/globgrph/kuzu_load.py` (retired) · `infra/aws/globgrph/kuzu_db.TOMBSTONE.md` (new, tracked) · the main workspace's two stores and manifests (read, archive, delete -- by absolute path) · `s3://opal-313476888478-globgrph/` (the tarball READ; the ITEM-3 archive prefix WRITE, two objects) · the E-3 record `deliverables/0.9.0_WK_NFRA_CLDGRPH~3/CG-s-19.residual-stores.result.md` and its probes (READ; reuse the AST walk) · `surprise-channel/adjudications/ADJUDICATION_v1.md` C-S26 (READ: the lift).

## BOUNDS

- **Order of acts is the law:** verify, archive, verify, tombstone, retire the builder, THEN delete. A deletion out of order is a NEVER-class error, not a shortcut.
- **Two S3 objects written, nothing else on S3.** No engine opened. The stitch store untouched.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
infra/aws/globgrph/kuzu_load.py
infra/aws/globgrph/kuzu_db.TOMBSTONE.md
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-F-1.lifted-dispositions-executed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.6 (this recut), cell CG-s-21 (s.1a; ADDED on the CTO's round-5 analysis @30027295be, PRD addendum v0.6 row S21, over rows NFRA_CLDGRPH-W3-S6 and C-S26).
<owned_cells>CG-s-21</owned_cells>
Read-dependencies, NOT claimed: CG-s-19 (DONE). Downstream, yours next: CG-s-22 (TO-CG-F-2, the site-Z exercise's laptop half, handed at this order's drain, with FIXED instants). Siblings, NOT yours: CG-s-23..26 (slot ~2), CG-s-27 (slot ~3), CG-s-28 (slot ~4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25 across 5 carriers; C2 6 open deploy-ledger entries; NEEDS-READ 137); the C3 moratoria bind BOUNDS (a builder beside the projection is the shadow pipeline).
comp-iam: DECLARED-NOT-APPLICABLE -- two PutObject acts on the globgrph bucket with the seat's existing credentials (the same instrument round 1's V-1 used); no principal, policy or grant changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5); v0.6's rows cited at @30027295be; the deliverable's validator context is the L9 seat's compose.
comp-find: RUN at the cut -- the reader census per C-S26 (0 of 982) and E-3's AST walk (0 of 487); re-run by F1-AC3 after the builder's removal.
</preflight>

<proof_of_spec>
Criterion ids minted at the recut by the issuer: `F1-AC1`..`F1-AC6`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-F-1.lifted-dispositions-executed.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> F1-AC1,F1-AC2,F1-AC3,F1-AC4,F1-AC5,F1-AC6` (from the worktree root) BEFORE the complete flip; the flip requires rc 0 AND every mechanical row PASS. `F1-AC2` (sha256 equality) and `F1-AC3` (the census) are the controls that must be able to FAIL. `F1-AC6` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.** "Together" at the flip means TWO commits (the acts, then the instance + flip pinning them), and the face says so (W2-S39).
</proof_of_spec>

<compiler_tools_mandate>
BEFORE ANY ACT: `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/adjudications/ADJUDICATION_v1.md --for "C-S26: the P7 hold lifted -- which stores, on what reproducibility, and any condition the author attached"`; `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/CG-s-19.residual-stores.result.md --for "each artifact's disposition, owner, reason and later_act_if_any"`. No `.py` is added by this order; one is removed.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the spawn.**
