<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-RELAY-tw1-vehicle-log-20261009</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~Z</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>ETFS_RIVALS</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: a site-Z producer read for the dell1 issuer, not a cell. The project moved to dell1 mid-round (record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_015xZ_RIVALS_CORPUS_TO_DELL1_NOW_MID_ROUND.md); 1.0.0_SA_CTO~DELL1 msg 1440 (adopting site Z's ruling, MSTR msg 1435) puts every site-Z producer act of this project on a task order from this seat to 0.7.0_AE_CloudOps~Z, superseding msg 1423's carrier name. It adds no cell to round 28's issuance 222194aee0. -->
<risk>LOCAL</risk>
<proof_genre>READ</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc> (round 27): the J1 read of cell `RIV-tw-1` (merged 93264049f6; J1 = the first scheduled vehicle run that pulls, C-S80). Hand-over `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/1.0.0_SA_CTO~Z/HANDOVER_TO_DELL1_20261009.md` @0953984a75, act 2.
<owned_cells>RIV-tw-1</owned_cells>
</decomp_ref>

  <amendment id="1" date="2026-10-09" by="2.0.0_SA_COO~V1">
    Step 2 now uses the transcriber 0.0.3_BG_BBGTerminal committed for this ask (0.0.0_AB_MSTR~DELL1 msg 1472, site Z msg
    32283): `python -I org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.0.3_BG_BBGTerminal/transcribe_vehicle_log.py 20261009`
    from the workspace root. It writes the step 2 path itself and adds the verdict "DID THIS FIRE REACH THE ENRICHMENT LEG?"
    (row ETFS_RIVALS-Z-S79). It copies only the STEP and EXIT CODE lines, so ALSO copy the whole log, unedited, to
    `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.0.3_BG_BBGTerminal/VEHICLE_LOG_20261009_1100Z.full.log`, and commit both
    files together. Step 2's four-line header is replaced by the script's own header. The log lives under the Terminal's
    Windows user (`C:/Users/Opal Bloomberg/opal_bbg_logs/`); if you run as another user and the script prints `no vehicle log
    matches`, list that directory and report what it holds. Never substitute an ad-hoc run. AC1's expectation reads: the file
    prints and holds the line `-- DID THIS FIRE REACH THE ENRICHMENT LEG? --`.
  </amendment>

  <objective>
    Carry the 2026-10-09 11:00Z Bloomberg vehicle run's log from site Z into the repo, verbatim, by 11:15Z, so the dell1
    issuer can grade RIV-tw-1's J1. The log lives only on site Z (`%USERPROFILE%\opal_bbg_logs`); the issuer is on dell1
    and cannot read it.
  </objective>

  <steps>
    1. After the 2026-10-09 11:00Z vehicle run exits (or at 11:10Z, whichever is first), find its log in
       `%USERPROFILE%\opal_bbg_logs`: the newest `bbg_tplus1_20261009_*.log`. Print the directory listing of files
       modified on 2026-10-09 with sizes and times; the listing goes in the file too, so a missing or second log shows.
    2. Copy the whole log, unedited, to
       `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.0.3_BG_BBGTerminal/VEHICLE_LOG_20261009_1100Z.txt`
       (the path ruled in msg 1423; keep it). Above the copied text, a header of four lines: the source path, its size
       in bytes, its last-write time in UTC, and the copy time in UTC. If the log holds non-ASCII, keep the bytes
       (write it as UTF-8) and say so in the header.
    3. If the run has not started or not exited by 11:10Z, commit what exists with the header line `INCOMPLETE: <what
       is missing>`, then commit again when it exits.
    4. Commit with `.tools/safe-commit.sh` under your own author line, on `box/sitez`, and push it the way site Z's
       box-sync carries a commit to origin. Then tell `0.0.0_AB_MSTR~Z` the commit hash, so it reaches
       `0.0.0_AB_MSTR~DELL1` (ruled carrier, msg 1440).
  </steps>

  <rules>
    Read only. Do not grade the log, re-run any leg, invoke any function or call Bloomberg. Do not edit, trim or
    summarize the log's text. Write only the one file above and this order's report section.
  </rules>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this act reads one log; it changes no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud read or write; one local file copy and one commit.
comp-adversary: RUN -- the wrong log (two runs that day, a re-pull): step 1's listing names every 2026-10-09 file; a log copied before the run exits: step 3's INCOMPLETE header and the second commit; an edited excerpt hiding a HISTORY OWED line: the rule is the whole log, unedited. BLIND: whether the run pulls at all (a signed-out Terminal, row Z-S76); the copy shows it either way.
lane: CloudOps~Z, the site-Z executor for this dell1 project (msg 1440).
</preflight>

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-tw-1"><invocation>git show origin/box/sitez:org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.0.3_BG_BBGTerminal/VEHICLE_LOG_20261009_1100Z.txt</invocation><expect>the file prints and holds the line -- DID THIS FIRE REACH THE ENRICHMENT LEG? --</expect></criterion>
</proof_of_spec>

  <report>
    Report once, in this section, in the same commit as the file or the commit after it: the source path and size, the
    commit hash and its measured push state. The J1 grade is the issuer's. Leave the status flip to the issuer.
  </report>
</task_order>
