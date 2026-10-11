<task_order>
  <metadata>
    <id>ETFS_RIVALS.TO-RELAY-tw1-vehicle-log-20261009</id>
    <issued_by>2.0.0_SA_COO~V1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~ZV</issued_to>
    <!-- AMENDMENT 2 moved it to ~ZV; AMENDMENT 3 restored ~Z; AMENDMENT 4 sets ~ZV again -->
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

  <amendment id="8" date="2026-10-11" by="2.0.0_SA_COO~V1">
    ONE MORE FILE FOR 20261010, AND FOR ANY DATE WHOSE ENRICHMENT EXIT CODE READS 97. The 20261010 transcription
    (@4b8e5e530a at origin/box/sitez) is read: STEP at log line 176, `ENRICHMENT EXIT CODE: 97 -- nothing written` at line 178,
    no HISTORY OWED line, no vendor-session-failure line. The cause of the 3 (which maps to 97) is the module's printed JSON
    result (`enrichment_bloomberg.py:1269`), which is the log line BETWEEN the two and was not copied (the selector is
    `STEP|EXIT CODE`). ACT: from the same untracked log, copy log lines 170 through 178 inclusive, unedited (the lines are the
    STEP line, the module's output and the exit line, plus the leg-90 line above it), to
    `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.7.0_AE_CloudOps~ZV/VEHICLE_LOG_20261010_1100Z.enrich.txt`, with a
    one-line header naming the source path, the byte count and the line numbers copied. Commit that one file and tell
    `0.0.0_AB_MSTR~Z` the hash. For a later date whose exit line reads 97, the same: the STEP line minus 6 through the exit line.
    Read only; do not run the module; do not edit a line. Nothing else in this order changes.
    Gate limb: GATE (viii) grades this modification (placeholders NONE declared at HEAD); LIMB 6 does not fire.
  </amendment>

  <amendment id="7" date="2026-10-11" by="2.0.0_SA_COO~V1">
    DATES OWED, STANDING: the 20261009 transcription is done (AMENDMENT 6). Now owed, one file per date, until the CVO
    grades RIV-tc-1 J1 REACHED: `20261010` (Saturday), `20261011` (Sunday), then each later date on a request from the issuer.
    Why a weekend date is owed: the task trigger is `-Daily` (`register_daily_task.ps1:62`), and every path of
    `scheduled_daily_pull.cmd` (success, pull failure, rc 50) reaches `:prune` and from there the rivalfunds legs
    (`:389-:422`), so a non-trading day still writes the STEP and EXIT CODE lines J1 reads. Read at origin 2026-10-11 ~05:0xZ:
    `VEHICLE_LOG_20261010_1100Z.txt` is absent at `origin/box/sitez` bd4025ade2 and `origin/CLOUD` 12f40e0cd1 (control
    20261009 present); `tw1_j1_read.py` reads NO-FILE (CVO ADDENDUM 6 @044ce5c831).
    ACT, per date `<D>`: run the transcriber from AMENDMENT 1 with `<D>`; copy its printed `.txt`, unedited, to
    `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.7.0_AE_CloudOps~ZV/VEHICLE_LOG_<D>_1100Z.txt` (AMENDMENT 5's path;
    the folder is yours); commit that one file; tell `0.0.0_AB_MSTR~Z` the hash. The log stays on disk by date, so a copy
    made at any later time is still this act (AMENDMENT 3 TIMING). If the transcriber prints `no vehicle log matches`, list
    `C:/Users/Opal Bloomberg/opal_bbg_logs/` for that date and commit the listing as the file: that is a measured
    "the run did not fire", which the CVO grades as such. No ad-hoc run.
    OWNER/UN-PARK CONDITION: `0.7.0_AE_CloudOps~ZV`, or any live site-Z CloudOps lane the site-Z manager names; un-parks
    when a site-Z seat registers. At 2026-10-11 05:0xZ no site-Z seat is live (`get_live_agents`: 0 of 19 at site Z;
    `~ZV` NOT REGISTERED).
    Gate limb: GATE (viii) graded this modification (the order already declares `<placeholders>NONE</placeholders>` at HEAD)
    and passed (to-pipeline-gate, commit 9e6b96a315 receipt: "1 of 1 staged-MODIFIED tree order(s) ... were graded").
    LIMB 6 did not fire (no newly-added order).
  </amendment>

  <amendment id="6" date="2026-10-09" by="2.0.0_SA_COO~V1">
    The full log is NOT owed. `*.log` is gitignored (.gitignore:68), so AMENDMENT 5's `.full.log` path cannot be committed
    (0.0.0_AB_MSTR~DELL1 msg 2347, option (a)). The transcription VEHICLE_LOG_20261009_1100Z.txt @2a0a40bfe4
    (0.0.3_BG_BBGTerminal folder) is the whole deliverable. Its sha256 line (8aa04796...4fa5) ties it to the source.
    The untracked copy stays at site Z. The issuer's reader tw1_j1_read.py reads REACHED on it (@4d688f78a7).
    Gate limb: no gate grades this modification.
  </amendment>

  <amendment id="5" date="2026-10-09" by="2.0.0_SA_COO~V1">
    PATH: the ruled folder `deliverables/0.0.3_BG_BBGTerminal/` is owned by that seat and refuses your commit (msg 2336). Commit the
    two files under YOUR OWN deliverables folder instead, same names:
    `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.7.0_AE_CloudOps~ZV/VEHICLE_LOG_20261009_1100Z.txt` and
    `.../VEHICLE_LOG_20261009_1100Z.full.log`, unedited (sha256 of the full log as you measured it). Either location satisfies AC1;
    the issuer reads both. Do not wait for 0.0.3_BG_BBGTerminal.
  </amendment>

  <amendment id="4" date="2026-10-09" by="2.0.0_SA_COO~V1">
    ASSIGNEE: `0.7.0_AE_CloudOps~ZV`, LIVE, the site-Z Codex lane for ETFS_RIVALS. Site Z lifted its hold on the ~Z* lanes
    (0.0.0_AB_MSTR~DELL1 msg 1643, site Z bus 91f67522): site-bound acts go there, per 1.0.0_SA_CTO~DELL1's table
    (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_035xZ_DELL1_RUNS_OWN_DEPLOYS_SITE_BOUND_ONLY_TO_SITE_Z.md`).
    This read is site-bound (the Terminal user's log). AMENDMENT 3 is superseded; its TIMING note stands. Everywhere above,
    "0.7.0_AE_CloudOps~Z" reads "0.7.0_AE_CloudOps~ZV".
  </amendment>

  <amendment id="3" date="2026-10-09" by="2.0.0_SA_COO~V1">
    AMENDMENT 2 IS WITHDRAWN: the assignee is `0.7.0_AE_CloudOps~Z` again, as issued. 1.0.0_SA_CTO~DELL1 msg 1610: the four
    site-Z lanes (~ZV, ~ZQ, ~ZW, ~ZC) hold no act until Andrew answers site Z's question on site-bound acts; leave a
    site-bound order as issued. Site Z 1.0.0_SA_CTO~Z msg 32344 notes `0.7.0_AE_CloudOps~Z` keeps NFRA_OPLGTW; whether this
    read runs there is site Z's to rule. TIMING: the log stays on disk and the transcriber selects it by date, so a copy
    made after 11:15Z is still this order's act. Do not substitute an ad-hoc run.
  </amendment>

  <amendment id="2" date="2026-10-09" by="2.0.0_SA_COO~V1">
    ASSIGNEE: `0.7.0_AE_CloudOps~ZV`, site Z's Codex lane for ETFS_RIVALS (site Z CTO msg 32331; Andrew ~03:3xZ "use codex for
    the new cloudops seats"; relayed by 0.0.0_AB_MSTR~DELL1 msg 1588). This act is site-bound (the Terminal user's log), so it
    stays at site Z. Everywhere above, "0.7.0_AE_CloudOps~Z" reads "0.7.0_AE_CloudOps~ZV". Nothing else changes.
  </amendment>

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
    2026-10-11 06:0xZ, executor 0.7.0_AE_CloudOps~ZV: AMENDMENT 7 date 20261010 DONE; 20261011 NOT YET DUE.

    20261010 (Saturday). The weekend fire DID run, which AMENDMENT 7 predicted on the -Daily trigger and the
    :prune path. Transcriber run as ordered, not by hand:
    `python -I org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.0.3_BG_BBGTerminal/transcribe_vehicle_log.py 20261010`.
    It writes into its own seat's folder; the UNEDITED copy was placed at AMENDMENT 5/7's path under this seat's
    own folder and committed alone: 4b8e5e530a,
    org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.7.0_AE_CloudOps~ZV/VEHICLE_LOG_20261010_1100Z.txt.
    Copy verified byte-identical rather than taken on report: transcript and copy both 1927 bytes, both
    sha256 fc7221aee8df0547a15c9e9c7ff26114ad70a019797146f6bcf331bd9ce3b421; copied 2026-10-11T05:26:32Z.
    Source C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261010_070002.log, 13451 bytes, last-write
    2026-10-10T11:07:26.057054Z, sha256 e7bc12180128a46fd7d8d4b11eec337005f274c136043e59ecdd7b4163894cef.
    EXACTLY ONE log matches bbg_tplus1_20261010_*.log -- the transcriber prints a NOTE on more than one and
    printed none, and the directory was listed beside it -- so there is no second or re-pull run to disambiguate.
    AC1's expectation is met on the bytes, read at origin with a positive and a negative control (an absent
    path fatals rc=128 rather than reading clean-empty): the file holds
    "-- DID THIS FIRE REACH THE ENRICHMENT LEG? --".

    20261011 (Sunday) IS NOT A NON-FIRE AND NO did-not-fire LISTING WAS COMMITTED FOR IT. Measured, not assumed:
    Get-ScheduledTaskInfo OPAL_BBGTML_daily_pull reads NextRunTime 2026-10-11T11:00:00Z, LastRunTime
    2026-10-10T11:00:01Z, LastTaskResult 0, NumberOfMissedRuns 0, State Ready. At the time of this report the
    trigger has not arrived, so AMENDMENT 7's no-match branch would record "the run did not fire" as a measured
    fact when the true cause is "not yet due" -- the one reading that branch must not be used to produce. A
    settle-wait is armed on the log path; the date is transcribed and committed when the log appears and its
    size stops changing. The order itself carries the owed date, so this is parked on a carrier and not on a
    live session: OWNER 0.7.0_AE_CloudOps~ZV per AMENDMENT 7.

    The issuer's own reader, run read-only on what is now at origin, for the issuer's convenience and NOT as a
    grade: 20261010 "J1-READ: NOT-REACHED -- J1 reads UNVERIFIABLE for this run, never PASS" (enrichment exit
    97); 20261009 control "J1-READ: REACHED" (exit 94); 20261011 "J1-READ: NO-FILE". Since 20261010 reads
    NOT-REACHED, the standing per-date obligation continues. The enrichment leg's own reason for the 97 is
    copied verbatim under TO-CLOSE-XB-AND-AMENDMENT8 act B @55d280983b, and the instrument disagreement it
    exposed is surprise row ETFS_RIVALS-Z-S81 @982563d244 (ARMED, disarm_owner 2.0.0_SA_COO~V1).

    PUSH STATE, measured by ls-remote at 06:0xZ (origin/box/sitez 84da5399cf) with a discriminating control:
    4b8e5e530a ON ORIGIN, 982563d244 ON ORIGIN, 55d280983b LOCAL. This seat cannot push box/sitez --
    never-rules-gate refused it and named the integrator as the branch's only pusher -- so step 4's publication
    path is the hash relayed to 0.0.0_AB_MSTR~Z, sent 05:45Z and again 06:08Z.

    Read only. No ad-hoc run, no Bloomberg call, no grading, no edit to the transcription's text. The J1 grade
    is the CVO's; the status flip is the issuer's.
    2026-10-09 07:10 Eastern: 0.7.0_AE_CloudOps~ZV executed the canonical transcriber and copied the full source bytes.
    Source: C:/Users/Opal Bloomberg/opal_bbg_logs/bbg_tplus1_20261009_070014.log; 14020 bytes;
    last-write 2026-10-09T11:08:47.312871Z; copied 2026-10-09T11:10:26.655412Z.
    Source and full-copy SHA256: 8aa0479677c2d96382f64133d608b3ae8c77b227a16343b783094dad3afe4fa5.
    One file modified today in the source directory; listing, UTC metadata and copy hash appended to the canonical transcription.
    Scheduled task observed Ready; last run 07:00:13 Eastern, LastTaskResult 0. No ad-hoc run, Bloomberg request or grading performed.
    Evidence prepared at the two exact ordered paths: VEHICLE_LOG_20261009_1100Z.txt and VEHICLE_LOG_20261009_1100Z.full.log
    under org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.0.3_BG_BBGTerminal/.
    BLOCKED-PUBLICATION: safe-commit refused both files because TREE_DELIVERABLES permits only the serial named in their folder;
    agent 0.7.0_AE_CloudOps~ZV is not permitted for 0.0.3_BG_BBGTerminal. No override or alternate author attempted.
    Evidence commit hash: NONE (commit rejected); files remain prepared in the working tree for the authorized owner to commit.
    Push state LOCAL/UNCOMMITTED for evidence. git ls-remote origin refs/heads/box/sitez failed with connection reset;
    current remote hash unverified. Routing exact files and hashes to the owner and issuer; status remains pending for issuer.

    Report once, in this section, in the same commit as the file or the commit after it: the source path and size, the
    commit hash and its measured push state. The J1 grade is the issuer's. Leave the status flip to the issuer.
  </report>
</task_order>
