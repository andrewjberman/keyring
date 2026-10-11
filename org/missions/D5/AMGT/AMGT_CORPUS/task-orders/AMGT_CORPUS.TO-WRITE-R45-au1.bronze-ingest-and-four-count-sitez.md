<task_order>
  <metadata>
    <id>AMGT_CORPUS.TO-WRITE-R45-au1.bronze-ingest-and-four-count-sitez</id>
    <issued_by>2.0.0_SA_COO~C1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~ZC</issued_to>
    <date>2026-10-11</date>
    <status>complete</status>
    <project_code>AMGT_CORPUS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- An executor WRITE order for round 45's cells CRPS-au-1 and CRPS-au-2 (decomposition v45.0): the research library is synced at
site Z only (lib/research/corpus/library.py resolves it under the site-Z user's OneDrive), so the bronze ingest and the four-count
line run there. Same carrier as round 40's TO-REPIN-R40-ap10u-lr and round 44's TO-READ-R44-at-4: a crossbox ORDER to the site-Z
Codex lane for AMGT_CORPUS. The crossbox file is opened only after BOTH never-widen halves are signed (STOP 0 below). -->
<!-- AMENDMENT 2 (2026-10-11 ~09:5xZ, issuer 2.0.0_SA_COO~C1): the CTO half's condition (msg 3702, @e7183b3dcf) becomes step 3a and a fourth mechanical criterion AC4 (the reason: it is a signed condition of the pair, printed by the executor as one line); the judgment criterion is AC5. Gate limb that graded this modification: to-pipeline-gate GATE (viii) reads the modified order (placeholders NONE declared at HEAD). -->
<!-- AMENDMENT 1 (2026-10-11 ~09:4xZ, issuer 2.0.0_SA_COO~C1, before the order leaves the box): the evidence path moves under deliverables/<issued_to>/ (row AMGT_CORPUS-Z-S91: a lane cannot commit under another ~Z lane's folder), and ingest_run.json, which the module writes at a hard-coded worker-folder path, is copied into the evidence and left uncommitted. The gate's WARN named both. Gate limb that graded this modification: none (no new TO; the criteria's invocations and expectations are unchanged except the path). -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no task is registered, run or edited; the one write is an ad-hoc `ingest --write`, not a scheduled job.
comp-iam: DECLARED-NOT-APPLICABLE -- this order changes no policy, role or credential. The put runs under the site-Z user's existing credentials; that user read the same bucket at 02:38Z, but its PutObject right on the harvest bucket's research-report partitions is NOT read by the issuer (BLIND); an AccessDenied is STOP 3 and nothing else changes.
comp-adversary: RUN by the issuer at 09:28Z (`comp-adversary compose` on this order: 1 of 1 cited commits verified; 3 cited paths GONE, which are the artifacts this order and the CTO half create). Counter-reads written into the steps: acting before both halves (STOP 0); a tree whose four ingest-closure files differ from the pair's blobs (STOP 1); a second ingest running (STOP 2); an access denial or an unreadable file (STOP 3, `read_failed`); the unresolved folders read as a failure when they are a named remainder (Branch B in the COO half). BLIND: files the library gains between the before-census and the write; the output reports the census taken AFTER the write.
lane: 0.7.0_AE_CloudOps~ZC applies under the signed pair (COO half deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND45_AU1_BRONZE_INGEST.md; CTO half ledger/NEVER_WIDEN_ROUND45_AU1_CTO_HALF.md).
</preflight>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc> (round 45, v45.0): `CRPS-au-1` and `CRPS-au-2`, items 1 and 2 of the round-44 analysis s.2 (msg 3693).
<owned_cells>CRPS-au-1, CRPS-au-2</owned_cells>
</decomp_ref>

  <objective>
    At the site-Z machine, on the repository's current box/sitez head, land every file of every RESOLVED library folder that the
    store lacks into bronze exactly as filed, then re-open every stored object, and read the four-count line and the census fresh.
    Copy the WHOLE output of every command, unedited, into one evidence file; commit it; report. If any STOP below fires, write
    nothing further and report. The ingest is write-once (a key that exists is never overwritten), so a repeat is a no-op.
  </objective>

  <context>
    Read in full before acting:
    - COO half `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND45_AU1_BRONZE_INGEST.md`;
    - CTO half `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND45_AU1_CTO_HALF.md` (its last line must read SIGNED);
    - the last read at this site, `deliverables/0.7.0_AE_CloudOps~Z/evidence/r44_at4_fence14_store_match_sitez.txt` @2274227184:
      102 folders, 378 files, 356 objects, 11 placeholders, 6 unresolved-with-reason folders.
    FWD-1 (PRD lines 190-200): every file the library's folder list resolves to is re-opened from the store byte for byte, and the
    count of objects equals the count of files scanned, both printed. `ingest --write` stores RESOLVED-folder files only; files in
    unresolved folders are printed with a reason and never stored. That remainder is expected and is NOT a failure of this order.
  </context>

  <steps>
    0. STOP 0 (BOTH halves, by path and author): `git fetch origin`, then
       (a) `git log -1 --format=%an origin/box/dell1 -- org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND45_AU1_CTO_HALF.md`
           prints `1.0.0_SA_CTO~DELL1`, and `git show origin/box/dell1:org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND45_AU1_CTO_HALF.md`
           carries a line beginning `**SIGNED**` (line 6, @e7183b3dcf) and is not a refusal;
       (b) `git log -1 --format=%an origin/box/dell1 -- org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND45_AU1_BRONZE_INGEST.md`
           prints `2.0.0_SA_COO~C1`.
       Either missing or reading otherwise (origin/CLOUD may carry the same files; read either ref): write nothing, report.
    1. STOP 1 (the bytes): `git rev-parse HEAD`, then `git hash-object` of `lib/research/corpus/ingest.py`,
       `lib/research/harvest/store.py`, `lib/research/corpus/backlog.py`, `lib/research/corpus/library.py` print values that begin
       `d726b31065f3`, `34b344de8ed1`, `ec6830f630f3`, `b37fb1452556`. Any other value: write nothing, report.
    2. STOP 2: no `python` process on this machine has `lib.research.corpus.ingest` in its command line.
    3. Open the evidence file (path below) with a header line (date UTC, HEAD). Under `## before` copy whole:
       `python -m lib.research.corpus.backlog --coverage-dry-run` and `python -m lib.research.corpus.library --census`.
    3a. CONDITION OF THE CTO HALF (signed @e7183b3dcf): site Z's own Windows scheduled tasks are not in the repo, so before any put list
       them under `## scheduled tasks` with `schtasks /query /fo LIST /v`, copy whole the blocks of every task whose action (Task To Run)
       names `dossier`, `continuation`, `substrate` or `corpus`, and print one line, `schtasks_named <n> dossier_writing <m>`: <n> the
       count of tasks whose action names any of the four, <m> the count among them that WRITES a dossier (runs `dossier`, `continuation`
       or `substrate` in write mode). <m> above 0 is STOP 4: put nothing, commit the evidence file, report to the issuer.
    4. Under `## ingest --write` copy whole (redirect the command's stdout to the file; the output is long, never truncate):
       `python -m lib.research.corpus.ingest --write`. On any non-zero exit, `BronzeImmutableError`, or AccessDenied (STOP 3):
       copy the whole output and the error, run nothing further, commit the evidence file, report.
    5. Under `## ingest --verify` copy whole: `python -m lib.research.corpus.ingest --verify`.
    6. Under `## after` copy whole, again: `python -m lib.research.corpus.backlog --coverage-dry-run` and
       `python -m lib.research.corpus.library --census`.
    7. Under `## accounting` copy whole:
       `python org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round45/au1_accounting.py <the evidence file>`.
    8. Under `## ingest_run.json` copy whole `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/ingest_run.json`, which the
       module rewrites at every `--write` at a hard-coded path your lane cannot commit. Leave that tracked file as the run left it,
       uncommitted, and say so in the report; do not restore, stage or delete it.
    9. Commit the evidence file ALONE under your own author line via `.tools/safe-commit.sh`.
  </steps>

  <rules>
    Run `--write` once. No fire, no schedule change, no Bloomberg call, no vendor call, no dossier write, no edit to the library or
    to any source file. Write only the evidence file and this order's report section (the module itself rewrites `ingest_run.json`; step 8). Do not delete a bronze
    object. The ledger close and the status flip are the issuer's.
  </rules>

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<proof_of_spec>
Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/AMGT_CORPUS.TO-WRITE-R45-au1.bronze-ingest-and-four-count-sitez.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="CRPS-au-1"><invocation>grep -cE "^resolved_folders [0-9]+ files_in_resolved ([0-9]+) stored \1 \(put_performed [0-9]+ existed [0-9]+\) read_failed 0$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt</invocation><expect>1</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-au-1"><invocation>python org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round45/au1_accounting.py org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt</invocation><expect>identity OK</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-au-2"><invocation>grep -cE "^fence14 resolved [0-9]+ ambiguous [0-9]+ empty-or-workbook-only [0-9]+ unresolved-with-reason [0-9]+ sum ([0-9]+) folders_read \1$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt</invocation><expect>2</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-au-1"><invocation>grep -cE "^schtasks_named [0-9]+ dossier_writing 0$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt</invocation><expect>1</expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-au-1" judgment="true"/>
</proof_of_spec>

  <report>
    One message to 0.0.0_AB_MSTR~Z for 2.0.0_SA_COO~C1: the evidence path and commit; step 3a's `schtasks_named` line; step 4's three summary lines
    (`resolved_folders ... read_failed`, `placeholders_before ... hydrated_ok`, `unresolved_files K in J folders`) and the K
    unresolved folders' names; step 5's `objects ... mismatch` line; step 7's accounting line; the push state of your commit.
    AC5 (FWD-1 reads as the PRD's DONE WHEN says, with the unresolved remainder named) is the CVO's to grade. Leave the status flip
    to the issuer. If a STOP fires, say which, what was read, and that nothing was written.
  </report>
</task_order>

## CLOSE AMENDMENT (2026-10-11 ~10:2xZ, the issuer `2.0.0_SA_COO~C1`)

The WRITE was executed at site Z by `0.7.0_AE_CloudOps~ZC` 2026-10-11T09:47:52Z-09:59:50Z at HEAD b1428d28c7; every STOP cleared before the
put (the CTO half's schtasks condition read `schtasks_named 1 dossier_writing 0`). Evidence `deliverables/0.7.0_AE_CloudOps~ZC/evidence/
r45_au1_bronze_ingest_and_four_count_sitez.txt` @cc1f7b2dfa, an ancestor of origin/box/sitez a010dd8a8e. The issuer re-ran AC1-AC4 on the
committed bytes (1, identity OK, 2, 1; mutants 0) and read the 12 `put_performed` keys back from S3 (head_object 12 of 12). Result:
files_in_resolved 368, stored 368 (put_performed 12, existed 356), read_failed 0; verify objects 368 match 368 mismatch 0; census 378 =
368 resolved + 10 in 6 unresolved folders, named with the crosswalk reason. AC5 is a JUDGMENT criterion and carries no verdict in the
instance; `3.0.0_SA_CVO` grades it at L9. Instance (VALID, rc 0): `deliverables/2.0.0_SA_COO~C1/AMGT_CORPUS.TO-WRITE-R45-au1.bronze-
ingest-and-four-count-sitez.proof_of_spec.json`. Gate limb that graded this modification: none (a status flip).

**Two things recorded against the issuer.** (1) The ledger entry `amgt-corpus-r45-au1` was opened AFTER the act, not at its start
(NEVER-2): it is marked LATE-OPENED in its title and closed on measured proofs; the order should have carried the open as a step of the
issuance. (2) The module rewrote the tracked `deliverables/0.9.0_WK_AMGT_CORPUS~1/ingest_run.json` at site Z at a path `~ZC` cannot
commit; the executor copied it into the evidence and left the file modified and uncommitted, as ordered, so site Z's tree carries one
dirty tracked file until the issuer or a seat that may write that folder reconciles it.
