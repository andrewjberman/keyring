# NFRA_MCPORTAL task order -- `MP-pd-6` -- WORKSTREAM PC ROUND 2: enable the usage status line on site Z and SEE one live payload (FWD-22, U2 enable)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-6</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~29</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the status line runs on Claude Code's own refresh; this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS, no IAM. One local settings file is edited.
comp-adversary: DECLARED-NOT-APPLICABLE -- the rollback is proven on a copy before the live write, and the live file is re-read as JSON after it.
EGRESS CLASS, declared: none. No network, no AWS, no vendor. One local write outside the repository, named in section 3.
</preflight>

## 1. THE CELL -- `MP-pd-6` (workstream PC round 2, decomposition sections PD.1, PD.4 and PD.6)

**Do not start before the issuer's GO message.** The GO says that `MP-pd-5` is drained, so `.tools/claude-usage-statusline.py` is on
the trunk, and that the issuer has read it. You continue in your worktree `C:/tmp/mp-pd-29` (branch `wk-NFRA_MCPORTAL-pd-29`);
rebase nothing: the GO names the commit of the script, and you take the script from the MAIN workspace tree it names (see step 2).

What this changes, and who it touches (the BLAST RADIUS, which you restate in your pre-act record): the one write is a `statusLine`
entry in this Windows user's Claude Code settings file, `<home>/.claude/settings.json`. EVERY Claude Code session on this box that
reads that file runs the command at each status-line refresh and shows its one printed line at the bottom of the terminal: that is
every site Z seat. The command reads its stdin and two local files and writes one local file (`<config dir>/usage_snapshot.json`);
it makes no network call. The ROLLBACK is removing that one `statusLine` key (or copying the backup file back); nothing else
changes, and a seat's next status-line refresh then shows its previous (empty) status line.

Do these, in order:

1. **Pre-act record.** Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~29/MP-pd-6_PRE_ACT_RECORD.md`: the
   settings path, the blast radius and the rollback above in your words, the key names currently in the settings file (names only,
   never values), whether a `statusLine` already exists (if one DOES exist, STOP and file a BLOCKING row with the existing command;
   do not overwrite it), and the sha256 of the file. Commit it before any live write.
2. **The command string.** Derive the workspace root with `git -C C:/tmp/mp-pd-29 rev-parse --git-common-dir` (the main worktree is
   the common dir's parent) and take the script path in THAT main tree: `<main root>/.tools/claude-usage-statusline.py` (forward
   slashes). Check the file exists and `python <that path>` run once with `echo '{}'` as stdin and `CLAUDE_CONFIG_DIR` pointed at a
   temp directory exits 0. The entry to add is `{"type": "command", "command": "python \"<that path>\""}` (the path contains a
   space, so it is quoted inside the string). Never hard-code the workspace path: it is derived on this box.
3. **Rollback proven on a COPY first.** Copy the settings file to a temp path. On the copy add the `statusLine` key, then roll back
   by REMOVING that key, and check the parsed result equals the parsed original. Separately copy the backup over a second copy and
   check its sha256 equals the original's. Record both results. Only if both hold, continue.
4. **Backup, then the live write.** Copy the settings file to `<home>/.claude/settings.json.pd6-backup` (this backup stays OUTSIDE the
   repository and is never committed: the file may hold values you must not commit). Then write the live file: load it as JSON,
   add ONLY the `statusLine` key, write a temp file beside it in the same directory, `os.replace` it over the live file (encoding
   UTF-8, keep non-ASCII characters as they are, indent 2), and re-read the live file as JSON. Every key of the backup must be present
   with an equal value. If the re-read fails or any key differs, copy the backup back at once, record it, and STOP with a BLOCKING row.
5. **See one live payload.** The status line refreshes in interactive sessions after the setting is picked up. Poll for
   `<config dir>/usage_snapshot.json` (the `CLAUDE_CONFIG_DIR` environment variable's value if set, else `<home>/.claude`) every 20
   seconds for up to 15 minutes in total (use several short commands; a single command may not exceed 8 minutes). When it appears,
   read it: record `schema`, `written_at`, `rate_limits_claim`, `reason`, whether `five_hour` and `seven_day` are present, the two
   `used_percentage` values (percentages only), and `account_claim`. Do NOT copy the account email into any file you commit; record
   `account_claim` and that an email was present. If nothing appears in 15 minutes, record that, leave the setting in place, and
   report it: do not guess a payload and do not run the script yourself with a made-up one as evidence.
6. **Run file** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~29/pd6_run.json`: `{"settings_path",
   "backup_path", "backup_sha256", "blast_radius", "rollback_proven_on_copy": <bool>, "rollback_bytes_equal": <bool>,
   "snapshot_path", "waited_seconds", "snapshot_seen": <bool>, "pre_act_record"}`. Commit it, then run AC1.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3, plus, outside the repository, ONLY `<home>/.claude/settings.json` (the one `statusLine`
   key) and `<home>/.claude/settings.json.pd6-backup`. Edit no other settings file, no `~/.claude.json`, no `.credentials.json`
   (never open it), no hook, no skill, no repo script.
2. If a `statusLine` already exists, STOP (step 1). If the JSON re-read after the write is not byte-for-byte sound or any prior key
   moved, roll back at once (step 4) and stop.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a). If you
   cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~29/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/claude-usage-statusline.py` (in the main tree), `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`.
Outside the repository, write ONLY the two files named in section 2.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W29-S<k>` (the next free k for W29, after your MP-pd-5 rows). `surfaced_at` = `date -u +%FT%TZ` at filing.
`disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd6.AC1.sh; echo "exit=$?"</invocation><expect>run=read live_statusline_names_script=yes backup_keys_preserved=yes rollback_on_copy_equals_backup=yes snapshot=measured/ok or absent/ok blast_radius_stated=yes run_claims_rollback_proven=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~29/NFRA_MCPORTAL.TO-MP-pd-6.claude-usage-statusline-enable.proof_of_spec.json`.
Report once, with:
- the check output;
- the commit hash;
- the snapshot you saw (schema, written_at, claim, reason, which members, the two used percentages), or that none appeared in 15 minutes;
- the sha256 of the settings file before and after, and the key names added;
- the rollback proof on the copy (both results);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut STAGED at the PC round-2 issuance (decomposition v10). Gate G-ENABLE (PD.6): MP-pd-5 drained and read by the
issuer. The blast radius (every site Z seat's Claude Code settings) and the rollback (remove the one settings key) are the
round-1 analysis's own words (ruling 2). If the snapshot does not appear because a session must restart to pick up the setting,
that is a finding for the issuer, not a failure of the safety steps; the criterion then reads FAIL with the measurement and the
issuer rules. Check dry-run at base: AC1 FAIL (run file absent); green and red arms exercised with synthetic files.

<status>staged</status>
<round>2</round>
<workstream>PC</workstream>
<slot>~29</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
