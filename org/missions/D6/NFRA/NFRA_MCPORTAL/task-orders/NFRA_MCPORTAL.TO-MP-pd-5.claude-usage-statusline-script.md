# NFRA_MCPORTAL task order -- `MP-pd-5` -- WORKSTREAM PC ROUND 2: the Claude Code status-line command that records the account and the 5-hour and weekly usage (FWD-22, U2 script)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pd-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pd-5</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~29</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a command Claude Code runs on its own status-line refresh; this cell schedules nothing and changes no setting.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS and no IAM. The script reads one local JSON file and writes one local file.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a payload with no limits, an absent payload after a measured one, bad input, a failure mid-write, the credentials file).
EGRESS CLASS, declared: none. No network, no AWS, no vendor.
</preflight>

## 1. THE CELL -- `MP-pd-5` (workstream PC round 2, decomposition sections PD.1 and PD.4)

Your worktree is `C:/tmp/mp-pd-29` (branch `wk-NFRA_MCPORTAL-pd-29`). Work and commit only there.

Andrew wants to see, per box, the Claude account each Claude Code login is signed in to and how much of its 5-hour and weekly
limits remain (PRD v0.8 FWD-22). The finding behind this cell (read it whole first):
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~23/U1_CLAUDE_ACCOUNT_AND_LIMITS_SOURCES.md`. In short: the
account (email, plan, organization) is readable without any credential from the `oauthAccount` object of `~/.claude.json`; the
5-hour and weekly figures are NOT readable from a file, but Claude Code's STATUS-LINE command receives a JSON object on stdin
with a `rate_limits` member (`five_hour` and `seven_day`, each `{used_percentage, resets_at}`), present only for a subscription
login after the first API response. That field layout is INFERRED from the binary's strings: no value has been seen, so write
the reader defensively and never assume a member exists.

Build ONE script, `.tools/claude-usage-statusline.py` (Python 3 standard library only, ASCII only, runs on Windows and Linux).
Claude Code runs it once per status-line refresh with the payload on stdin. It does this, in order:

1. Reads all of stdin and parses it as JSON. If that fails, print NOTHING, change NOTHING, exit 0.
2. Finds the snapshot directory: the environment variable `CLAUDE_CONFIG_DIR` when set and non-empty, else `<home>/.claude`
   (`os.path.expanduser("~")`). The snapshot file is `<dir>/usage_snapshot.json`. If the directory does not exist, print nothing and exit 0.
3. Reads the account from `~/.claude.json` (the `.claude.json` in the home directory, NOT inside the config dir) `oauthAccount`
   object, and only these keys: `emailAddress` -> `email`, `organizationType` -> `plan`, `organizationName` -> `organization`.
   Any other key of that object is ignored, and the file `~/.claude/.credentials.json` is NEVER opened, listed or read (not for
   existence either). A missing file, missing object or missing key gives `"account": null` and `"account_claim": "absent"`; all
   three present gives the object and `"account_claim": "measured"`.
4. Reads `rate_limits` from the payload. For each of `five_hour` and `seven_day` that is present as an object with a numeric
   `used_percentage`, build `{"used_percentage": <number as given>, "remaining_percentage": <100 - used, never below 0>,
   "resets_at": <the member as given, or null>}`. If both are present: `"rate_limits_claim": "measured"`, `"reason": null`.
   If one is missing, that one is null and the claim is still `"measured"` with a reason naming the missing one. If neither is
   present (no `rate_limits` member, or no usable member): `"rate_limits_claim": "absent"`, `"reason": "rate_limits member not in the
   status-line payload (present only for a subscription login after the first API response)"`, both null.
5. Writes `{"schema": 1, "written_at": "<ISO Z>", "rate_limits_claim", "reason", "five_hour", "seven_day", "account",
   "account_claim"}` ATOMICALLY: write a temp file in the same directory, then `os.replace` it over the snapshot. ONE exception:
   if the new result is `"absent"` and the existing snapshot parses and holds `"rate_limits_claim": "measured"`, leave the existing
   file untouched (its own `written_at` is its age). An absent payload never replaces a measured snapshot.
6. Prints ONE short line to stdout and exits 0: `5h <used>% wk <used>%` (rounded to whole numbers; use `--` for a missing one) when
   measured, else `usage n/a`. Wrap the whole thing so that ANY unexpected error prints nothing, leaves the previous file, and
   exits 0. The script must never print a token, a path, an email or a traceback.

**Tests**, in the new file `.tools/tests/test_claude_usage_statusline.py`, by these exact names. Import the script as a module
(by path with `importlib`) and call its main function with injected stdin text, config dir and home directory, or run it as a
subprocess with `CLAUDE_CONFIG_DIR` and `HOME`/`USERPROFILE` pointed at a temp directory; either way never touch the real home
directory or the real `~/.claude`:
- `test_measured_payload_writes_snapshot_with_remaining`: used 42 and 10 give remaining 58 and 90, claim measured;
- `test_payload_without_rate_limits_writes_absent_with_reason`: no member -> claim absent, the reason text above, both null;
- `test_absent_never_replaces_measured_snapshot`: write a measured snapshot, then run an absent payload: the file is byte-for-byte unchanged;
- `test_never_opens_credentials_file`: plant a `.credentials.json` in the temp home and patch `builtins.open` and `os.path`/`pathlib`
  reads so that any access to a path ending `.credentials.json` fails the test; run a full measured payload; no such access happened;
- `test_bad_stdin_prints_nothing_exits_zero_and_keeps_previous_file`: stdin `not json` -> empty stdout, return 0, previous file untouched;
- `test_atomic_write_leaves_no_partial_file`: make `os.replace` raise; afterwards the snapshot dir holds no half-written snapshot
  (the previous file, if any, is intact) and no stray temp file, and the script still returned 0 with empty stdout;
- `test_account_fields_only_named_keys`: an `oauthAccount` object holding the three keys plus `accessToken`, `billingType`,
  `organizationRateLimitTier` yields an `account` object with exactly `email`, `plan`, `organization`.

This cell changes NO Claude Code setting. Do not edit `~/.claude/settings.json` or any `settings*.json`, do not run `claude`, do not
add a `statusLine` anywhere. Enabling it is a later order.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No network, no AWS, no deploy, no edit of any setting file, no real home-directory write.
2. If a criterion cannot be met as written, REFUSE it with its measurement. Never repair a criterion.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a).
   `.tools/*.py` passes `.tools/commit-gate.sh` (py_compile, ds-precommit, ruff py39): fix what it reports in your own file.

## 3. SURFACES

<paths>
.tools/claude-usage-statusline.py
.tools/tests/test_claude_usage_statusline.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~29/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: the U1 finding named in section 1, `.tools/tests/` (for the test conventions), and
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/`. Do NOT read `~/.claude/.credentials.json`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W29-S<k>` (the next free k for W29). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pd-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd5.AC1.sh; echo "exit=$?"</invocation><expect>statusline tests: 0 failed; named tests PASSED 7 of 7 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pd-5"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pd/checks/pd5.AC2.sh; echo "exit=$?"</invocation><expect>rc=0 stdout_lines=1; snapshot read with claim measured, five_hour_used=42, remaining=58, ok=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~29/NFRA_MCPORTAL.TO-MP-pd-5.claude-usage-statusline-script.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- the script's printed line for a measured payload and for an absent one;
- any assumption about the payload you could not avoid, and why;
- any row.
Your next order on this queue, `MP-pd-6`, is staged and arrives only when the issuer continues you.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC round-2 issuance (decomposition v10) from the round-1 analysis ruling 2: "FWD-22's usage source is a
status-line command, proven on site Z first." The snapshot object is PD.4. The panel and the transport are NOT in this round (PD.8
item 3): this cell makes the snapshot, MP-pd-6 enables it and sees one live payload. Checks dry-run at base 18:0xZ: AC1 FAIL (test
file absent), AC2 FAIL (script absent). The `rate_limits` layout is INFERRED (U1); the script must degrade to `absent`, not guess.

<status>complete</status>
<round>2</round>
<workstream>PC</workstream>
<slot>~29</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
