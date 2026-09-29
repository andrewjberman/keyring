# AMGT_CORPUS task order -- `CRPS-p-3` -- ROUND 14: FWD-17 on a scratch library -- a new report lands, the dossier moves, the prior object still reads, and an unchanged rebuild writes nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-p-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- offline: the store is the package's own StubS3Client.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 14. Serves **FWD-17 (a new report moves the dossier; unchanged inputs write nothing)**.

## 1. THE CELL -- `CRPS-p-3`

**Where this came from.** FWD-17's fence (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md`): *"a new report lands, a new report_id16
appears BESIDE the old, the dossier's inputs_sha16 changes, the page serves the newer pillars, and the prior as_of object still
reads; and a rebuild with UNCHANGED inputs writes NOTHING and says so"*. The chain is `lib/research/corpus/`: `library` (the folder
root, `library.ENV_LIBRARY_ROOT`) -> `ingest` (bronze, keyed by content) -> `extract` -> `typed` -> `continuation` (thesis pillars)
-> `dossier` (`write_one`, `read_dossier`; objects `as_of=<date>.<inputs_sha16>.json`, `write_one` no-ops when stored method and
inputs equal the current ones). Every stage takes a `client=`; `lib/research/corpus/substrate.py` `StubS3Client` is the package's
in-memory stand-in for the one bucket (list/get/put/head). **Ruled by the issuer:** the store is `StubS3Client`, never the served
bucket (a drive on the served bucket would put a fabricated report into served gold); the fence's page limb is read as
`dossier.read_dossier`'s pillars (the page render belongs to AMGT_RESAPP / DSGN_AMGTV1).

**RULED -- what you build:** `lib/research/corpus/tests/test_fwd17_scratch_drive.py` (new, offline). Under `tmp_path`: a scratch library with ONE
covered folder (resolved through the identity layer the way the real chain resolves it -- stub or fixture the identity layer
only if the chain offers no seam, and say which) holding one report whose thesis pillars you control; drive the real stage
functions with one `StubS3Client` through to `dossier.write_one`; record the report_id16, the dossier's inputs_sha16 and object
key, and the pillars `read_dossier` returns. Then ADD one newer report to the folder with different pillars, drive the chain
again, and assert: a new report_id16 appears BESIDE the old in the stub's bronze; the new dossier object's inputs_sha16 differs;
`read_dossier` returns the NEWER pillars; the PRIOR dossier object still reads (get by its key). Then drive `write_one` once more
with nothing changed and assert it writes nothing and says so (its own returned/printed no-op). After the asserts, `print()` ONE
line, exactly: `fwd17 new_report_id16_beside_old True inputs_sha16_changed True newer_pillars_served True prior_as_of_reads True
unchanged_rebuild_wrote 0`. The newer report must carry a later `as_of`/date than the older one by the chain's own dating rule;
freeze or inject the clock only through a seam the code already has. Edit NO file under `lib/` other than your test; a limb the
chain cannot show offline is a row and a REFUSAL.

## 3. SURFACES

<paths>
lib/research/corpus/tests/test_fwd17_scratch_drive.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-p-3.fwd17-scratch-drive.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library on the synced drive. Scratch `.scratch/p3/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call. NO S3 client other than StubS3Client (never boto3, never store._default_client()), NO write to the live library.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-p-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p3_AC1.sh</invocation><expect>(?m)^fwd17 new_report_id16_beside_old True inputs_sha16_changed True newer_pillars_served True prior_as_of_reads True unchanged_rebuild_wrote 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-p-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p3_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-p-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p3_AC3.sh</invocation><expect>(?m)^paths_outside_grant 0$</expect></criterion>
</proof_of_spec>

- AC1 the driven exercise's line; AC2 the whole corpus suite with your test in it; AC3 the bound: nothing outside your grant.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-p-3.fwd17-scratch-drive.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: each AC line, the two report_id16s and inputs_sha16s, and every seam you stubbed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-13 analysis s.4 item 3 @`f1c482d24f` (msg 26603). Checks dry-run at the base `dbafd14c52`: p3_AC1 FAIL (no drive line); p3_AC2 PASS (444 passed); p3_AC3 PASS (paths_outside_grant 0).
Store ruled offline (decomposition v14.0 s.1a).
<risk>LOCAL</risk>
<status>complete</status>
<round>14</round>
<slot>~3</slot>
<fabric>site-z</fabric>
