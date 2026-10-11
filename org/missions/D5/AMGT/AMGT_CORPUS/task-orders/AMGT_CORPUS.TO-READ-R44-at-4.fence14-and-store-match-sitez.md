<task_order>
  <metadata>
    <id>AMGT_CORPUS.TO-READ-R44-at-4.fence14-and-store-match-sitez</id>
    <issued_by>2.0.0_SA_COO~C1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~ZC</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>AMGT_CORPUS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- An executor READ order for round 44's cell CRPS-at-4 (decomposition v44.0): the research library is synced at site Z only
(lib/research/corpus/library.py:41-73 resolves it under the site-Z user's OneDrive), so FWD-14's four-count line and FWD-1's store
match run there. Same carrier as round 40's TO-READ-R40-ap10b-lv: a crossbox ORDER to the site-Z Codex lane for AMGT_CORPUS. -->
<risk>LOCAL</risk>
<proof_genre>READ</proof_genre>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only; no task is run, registered or edited.
comp-iam: DECLARED-NOT-APPLICABLE -- the dry runs below read the local library and the store; nothing is written (--coverage-dry-run, --verify, --census are read-only modes).
comp-adversary: RUN by the issuer at the cut -- the library is absent on dell1 (LibraryAbsentError), which is why this is site Z's read; the last live four-count line is r39 (sum 96, folders_read 97, before the round-40 fix).
EGRESS CLASS, declared: NONE beyond Opal's own S3 reads. No Bloomberg, no vendor call.
</preflight>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc> (round 44, v44.0): `CRPS-at-4`, items 4 and 6 of the close read @987284b18e.
<owned_cells>CRPS-at-4</owned_cells>
</decomp_ref>

  <objective>
    READ ONLY. On the site-Z machine, at the repository's current box/sitez head, run three read-only commands and copy their
    WHOLE output, unedited, into one evidence file; commit it; report. Run nothing else, register nothing, edit nothing outside your
    deliverables folder.
  </objective>

  <context>
    FWD-14 (PRD lines 469-482): the four-count line over every library folder -- resolved / ambiguous / empty-or-workbook-only /
    unresolved-with-reason -- sums to the folder count every time. Printer: `lib/research/corpus/backlog.py` `_print_fence14_line`.
    FWD-1 (PRD lines 194-197): the store matches the drive at the current folder count (last read: 356 objects, 356 files, 95 folders;
    the library now holds 97 folders).
    Also, for the FWD-12 cell: whether the master `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx` exists anywhere in the library.
  </context>

  <steps>
    1. `git rev-parse --short HEAD` (record it).
    2. `python -m lib.research.corpus.backlog --coverage-dry-run` -- copy the whole output under `## fence14`.
    3. `python -m lib.research.corpus.ingest --verify` and `python -m lib.research.corpus.library --census` -- copy both whole
       outputs under `## store vs drive`.
    4. Under `## master template`: `Get-ChildItem -Recurse -Filter "FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx"` over the
       library root the corpus uses (print the root and every match with its full path and LastWriteTime; zero matches is written as
       `0 matches under <root>`, never left blank).
    5. Write all of it to
       `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~Z/evidence/r44_at4_fence14_store_match_sitez.txt`
       with a header line (date UTC, HEAD), and commit that one file under your own author line via `.tools/safe-commit.sh`.
  </steps>

  <proof_of_spec>
    <criterion id="AC1" cell_refs="CRPS-at-4"><invocation>grep -cE "^fence14 resolved [0-9]+ ambiguous [0-9]+ empty-or-workbook-only [0-9]+ unresolved-with-reason [0-9]+ sum ([0-9]+) folders_read \1$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~Z/evidence/r44_at4_fence14_store_match_sitez.txt</invocation><expect>1</expect></criterion>
    <criterion id="AC2" cell_refs="CRPS-at-4" judgment="true"/>
  </proof_of_spec>

  <report>
    One message to 0.0.0_AB_MSTR~Z for 2.0.0_SA_COO~C1: the evidence path and commit, the fence14 line, the verify line, and the
    master-template count. AC2 (the store matches the drive at the current folder count) is the issuer's to grade.
  </report>
</task_order>
