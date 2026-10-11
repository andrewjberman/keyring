<task_order>
  <metadata>
    <id>AMGT_CORPUS.TO-WRITE-R47-aw10.template-put-sitez</id>
    <issued_by>2.0.0_SA_COO~C1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~ZC</issued_to>
    <date>2026-10-11</date>
    <status>pending</status>
    <project_code>AMGT_CORPUS</project_code>
  </metadata>
<direct_act>true</direct_act>
<workstream>TEMPLATE</workstream>
<!-- An executor WRITE order for round 47's cell CRPS-aw-10 (decomposition v47.1): the research library is synced at site Z only
(lib/research/corpus/library.py resolves it under the site-Z user's OneDrive), so the one put of the master template runs there. Same carrier
as round 45's TO-WRITE-R45-au1: a crossbox ORDER to the site-Z Codex lane for AMGT_CORPUS. The crossbox file is opened only after BOTH never-widen
halves are signed (STOP 0 below). WORKSTREAM `TEMPLATE`: a disjoint write surface (one bronze key, one evidence file) and a different lane
(~ZC) from the round's two worker orders; GATE (x) keys the census by (workstream, round) (Rule 27). -->
<!-- AMENDMENT 1 (2026-10-11 ~18:2xZ, issuer 2.0.0_SA_COO~C1; after ~ZC's STOP 3, site Z msg 33355, row AMGT_CORPUS-Z-S92): (a) step 3's invocation gains `PYTHONPATH=.` (the script imports lib.research; `python <path>` puts the script's directory on sys.path, so the first form failed with rc=1); (b) the locate script now ALSO lists the files directly inside the library root's PARENT folder, because the SharePoint item sits in `Shared Documents/Asset Management/`, the parent of the derived root `.../Asset Management/Research` (the issuer's Graph listing of that folder), and the first walk covered the root only. Criteria, paths and every other step are unchanged. Gate limb that graded this modification: GATE (viii) reads the modified order (placeholders NONE declared at HEAD). -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no task is registered, run or edited; the one write is an ad-hoc `--put --write`, not a scheduled job.
comp-iam: DECLARED-NOT-APPLICABLE -- this order changes no policy, role or credential. The put runs under the site-Z user's existing credentials, the same that ran round 45's ingest (put_performed 12); an AccessDenied is STOP 5 and nothing else changes.
comp-adversary: RUN by the issuer at the cut on dell1 HEAD (the COO half names it): counter-reads written into the steps -- acting before both halves (STOP 0); a tree whose three closure files differ from the pair's blobs (STOP 1); a second put running (STOP 2); zero or several files carrying the master's name, or a file of another size (STOP 3, STOP 4); an access denial or a read-back mismatch (STOP 5); a scheduled task that writes a dossier or a research_template object (STOP 6, the CTO half's condition). BLIND: whether the synced file equals the SharePoint item byte for byte (the size is compared, the hash of the item is not); the evidence prints the stored sha256.
lane: 0.7.0_AE_CloudOps~ZC applies under the signed pair (COO half deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND47_AW10_TEMPLATE_PUT.md; CTO half ledger/NEVER_WIDEN_ROUND47_AW10_CTO_HALF.md).
</preflight>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc> (round 47, v47.1): `CRPS-aw-10`, item 4 of the round-46 analysis s.3 and ADDENDA 2 and 3 (msgs 3994, 4001).
<owned_cells>CRPS-aw-10</owned_cells>
</decomp_ref>

  <objective>
    At the site-Z machine, on the repository's current box/sitez head, find the ONE file in the synced research library that carries the master
    template's name, print its label count, and store it write-once in the `research_template` bronze table; then repeat the put once to prove the stored
    object. Copy the WHOLE output of every command, unedited, into one evidence file; commit it; report. If any STOP below fires, write nothing further and report.
  </objective>

  <context>
    Read in full before acting:
    - COO half `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND47_AW10_TEMPLATE_PUT.md`;
    - CTO half `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND47_AW10_CTO_HALF.md` (its last line must read SIGNED);
    - the issuer's search: `deliverables/2.0.0_SA_COO~C1/evidence/r47_aw7_master_template_search_20261011.md` (SharePoint site `Shared`, item
      `01L6LHKFRTYYYRWCI37VGLHJQPCL3KMJXN`, 383839 bytes, modified 2026-07-24T13:04:50Z).
    The master's file name is `FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx`. Two older siblings of the same stem (`..._v1.xlsx`) may sit in the
    library; they are NOT the master and are never put.
  </context>

  <steps>
    0. STOP 0 (BOTH halves, by path and author): `git fetch origin`, then
       (a) `git log -1 --format=%an origin/box/dell1 -- org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND47_AW10_CTO_HALF.md`
           prints `1.0.0_SA_CTO~DELL1`, and `git show origin/box/dell1:org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND47_AW10_CTO_HALF.md`
           carries a line beginning `**SIGNED**` and is not a refusal;
       (b) `git log -1 --format=%an origin/box/dell1 -- org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND47_AW10_TEMPLATE_PUT.md`
           prints `2.0.0_SA_COO~C1`.
       Either missing or reading otherwise (origin/CLOUD may carry the same files; read either ref): write nothing, report.
    1. STOP 1 (the bytes): `git rev-parse HEAD`, then `git hash-object` of `lib/research/corpus/template.py`, `lib/research/corpus/team_sheet.py`,
       `lib/research/harvest/store.py` print values that begin `e03d6a8acf65`, `0442f28ed1f6`, `34b344de8ed1`. Any other value: write nothing, report.
    2. STOP 2: no `python` process on this machine has `lib.research.corpus.template` in its command line.
    3. Open the evidence file (path below) with a header line (date UTC, HEAD). Under `## locate` copy whole:
       `PYTHONPATH=. python org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/checks/round47/aw10_locate.py`
       (it walks the library root and lists the files directly in the root's parent folder; exit 0 only with exactly one match).
       STOP 3 unless it printed `matches 1`. STOP 4 unless its last line reads `size_equal True`. Either: write nothing further, commit the evidence, report.
    3a. CONDITION OF THE CTO HALF (signed, msg 4031): site Z's own Windows scheduled tasks are not in the repo, so before any put list them under
       `## scheduled tasks` with `schtasks /query /fo LIST /v`, print the denominator (the number of tasks listed), copy whole the blocks of every task
       whose action (Task To Run) names `dossier`, `continuation`, `substrate`, `corpus` or `template`, and print one line,
       `schtasks_named <n> dossier_writing <m>`: <n> the count of tasks whose action names any of the five, <m> the count among them that WRITES a
       dossier or a `research_template` object (runs `dossier`, `continuation` or `substrate` in write mode, or `template --put ... --write`).
       <m> above 0 is STOP 6: put nothing, commit the evidence file, report to the issuer.
    4. Under `## labels` copy whole, with `<path>` the single `template_locate match` path:
       `python -m lib.research.corpus.template --labels "<path>"`.
    5. Under `## dry-run` copy whole: `python -m lib.research.corpus.template --put "<path>" --item-id 01L6LHKFRTYYYRWCI37VGLHJQPCL3KMJXN --source-mtime 2026-07-24T13:04:50Z`.
    6. Under `## put` copy whole (redirect stdout to the file): the same command with `--write`. On any non-zero exit, `BronzeImmutableError`, or
       AccessDenied (STOP 5): copy the whole output and the error, run nothing further, commit the evidence file, report.
    7. Under `## put again` copy whole: the same `--write` command a second time. It must print `put_performed False existed True` with the same key.
    8. Commit the evidence file ALONE under your own author line via `.tools/safe-commit.sh`.
  </steps>

  <rules>
    Run `--write` exactly twice, as steps 6 and 7. No fire, no schedule change, no Bloomberg call, no vendor call, no dossier write, no edit to the library or
    to any source file. Write only the evidence file. Do not delete a bronze object. The ledger close and the status flip are the issuer's.
  </rules>

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r47_aw10_template_put_sitez.txt
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<proof_of_spec>
Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~C1/AMGT_CORPUS.TO-WRITE-R47-aw10.template-put-sitez.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="CRPS-aw-10"><invocation>grep -cE "^template_put key amgt/harvest/bronze/research_template/template=01L6LHKFRTYYYRWCI37VGLHJQPCL3KMJXN/[0-9a-f]{16}/FactSet Based ONE PAGER TEMPLATE 2026 03 09_v2.xlsx sha256 [0-9a-f]{64} put_performed (True|False) existed (True|False)$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r47_aw10_template_put_sitez.txt</invocation><expect>2</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aw-10"><invocation>grep -cE " put_performed False existed True$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r47_aw10_template_put_sitez.txt</invocation><expect>1</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-aw-10"><invocation>grep -cE "^template_labels measured [0-9]+ metric_name [0-9]+ pass_through [0-9]+ two_label_left [0-9]+ fallback [0-9]+ bloomberg_held [0-9]+ codes [0-9]+$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r47_aw10_template_put_sitez.txt</invocation><expect>1</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-aw-10"><invocation>grep -cE "^schtasks_named [0-9]+ dossier_writing 0$" org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r47_aw10_template_put_sitez.txt</invocation><expect>1</expect></criterion>
</proof_of_spec>

  <report>
    One message to 0.0.0_AB_MSTR~Z for 2.0.0_SA_COO~C1: the evidence path and commit; the locate lines (`matches`, the match path, `size_equal`); the
    `template_labels` line; the two `template_put` lines; the push state of your commit. Leave the status flip and the ledger close to the issuer. If a STOP
    fires, say which, what was read, and that nothing was written.
  </report>
</task_order>

<round>47</round>
