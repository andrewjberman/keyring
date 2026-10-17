# TO SOC2_MSLOGS.TO-R2-k2 -- the read client: paging, who-acted, Desktop print-out, MFA session, derive

<to_id>SOC2_MSLOGS.TO-R2-k2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~10</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Risk note:** LOCAL: the cell calls nothing live; its tests use injected invokers and a fake `boto3`.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-k-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 (second half), FWD-2, FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-k-2`. A member of the access group reads the door with `data/m365_metadata/scripts/silver/read_timeline.py`. Round 1 left three gaps that this cell closes in the CLIENT (the door cannot push to a machine):
(1) the door's `detail` answer is cut at 1000 rows or 5,000,000 bytes with `truncated` true and no cursor, so a busy day needs paging; and the printed line did not say WHO acted;
(2) Andrew-direct 2026-10-16 ~23:40Z, VERBATIM: "we need to have a mechanism with the globgrph lambda where it can do a print out to the desktop on this machine." (CTO ruling: the caller's client writes the file);
(3) two stopgaps hold what the client lacks: `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/read_timeline_to_desktop.ps1` (a named AWS profile, the MFA device, a six-digit code traded for a short session, the Desktop file) and
`org/tier1_exec/2.0.0_SA_COO~S1/deliverables/derive_days.py` (ask the door to rebuild silver for some dates). READ both before you write, then DELETE both: the client replaces them.

READ first: `data/m365_metadata/scripts/silver/read_timeline.py` and `data/m365_metadata/scripts/tests/test_read_timeline.py` (round 1), the two stopgaps above, the DOOR CONTRACT in `infra/aws/lambda/globgrph-trino-access/handler.py`'s docstring
(`timeline`, `detail`, `derive_silver`), and the check `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py` (the functions `paging`, `desktop`, `retire`, `_door_rows`, `_fake_door`, `_FakeBoto`: this is exactly how your work is measured, and the fakes show the interfaces it expects).

BUILD TO THIS CONTRACT (all in `data/m365_metadata/scripts/silver/`):

`door_client.py` (new; stdlib, with `boto3` and `botocore` imported lazily INSIDE the functions that need them):
- `build_invoker(profile=None, mfa_code=None, mfa_serial=None, boto3_module=None) -> invoker`. `boto3_module` is the injected module (default: import boto3). The session: `s = boto3_module.Session(profile_name=profile)` when a profile is given, else `Session()`. With an `mfa_code`: it must be exactly six digits (else `ValueError`, before any call);
  `iam = s.client("iam")`, devices from `iam.list_mfa_devices()["MFADevices"]` (`SerialNumber`); with `mfa_serial` given use it; with exactly one device use it; with none, or several and no `mfa_serial`, raise `ValueError` whose message lists the serial numbers found;
  `sts = s.client("sts")`, `sts.get_session_token(SerialNumber=<serial>, TokenCode=<code>)["Credentials"]`, then the lambda client `boto3_module.Session().client("lambda", aws_access_key_id=..., aws_secret_access_key=..., aws_session_token=..., region_name="us-east-1", config=<botocore Config(read_timeout=290, connect_timeout=10, retries={"max_attempts": 1})>)`.
  With no `mfa_code` the lambda client is built from the profile session with the same config. The invoker calls `client.invoke(FunctionName=<the door's name>, Qualifier="member", Payload=<json bytes>)` and returns the parsed JSON of `Payload`; a reply carrying `FunctionError` raises `RuntimeError("door error")` without printing the payload.
  The door's name is `lib.opal_naming.name("globgrph", None, "trino-access", "lambda")` resolved as `read_timeline.py` does today (the repository root onto `sys.path`). The three session keys live only in the client objects: they are never printed, logged or written.
- `desktop_dir(environ=None, platform=None, known_folder=None) -> str`: the user's Desktop folder, derived and never typed. `known_folder` is a callable returning the shell's Desktop path or None (default: on Windows, the shell's Desktop through `ctypes` `SHGetFolderPathW` with CSIDL_DESKTOPDIRECTORY 0x10; elsewhere None). If it returns a path use it; otherwise `<USERPROFILE or HOME>/Desktop` from `environ`.
- `write_desktop(text, account, start, desktop=None, repo_root=None) -> str`: writes `text` UTF-8, no BOM, exactly as given, to `<desktop>/timeline_<safe account>_<yyyymmdd of start>.txt` where the safe account replaces every character outside `[A-Za-z0-9@._-]` with `_`, and returns the path. `desktop` defaults to `desktop_dir()`, `repo_root` to the repository root of the module. It raises `ValueError`, writing nothing, when the Desktop folder is inside `repo_root` (the file is never to reach git).
- `derive_dates(invoker, dates) -> list`: every date must match `YYYY-MM-DD` and be a real calendar date, else `ValueError` before ANY call. One `{"op": "derive_silver", "date": d}` call per date, run concurrently (a thread pool of at most 8), result list in the INPUT order of `(date, "ok rows=N")` or `(date, "REFUSED (reason)")` (the reason is the reply's `error`, else "no reason given").

`read_timeline.py` (round 1's file, extended; keep `fetch`, `render`, `ACCOUNT_RE` working):
- `fetch(invoker, account, start, end, detail=False)`. With `detail` false it is EXACTLY round 1: one call, payload `{"op","account","start","end"}`. With `detail` true: payload also carries `"detail": true`, and it PAGES: while a reply is `truncated`, the next call's `start` is the time of the LAST row of the reply (inclusive), rows already held are dropped by `record_id`, and the merged reply is
  `{"ok": true, "rows": [...in time order, each once...], "truncated": false}`. If a reply is truncated and its last row's time equals the `start` it was asked with (no progress), raise `RuntimeError` saying more rows share one second than a page holds. At most 200 calls, then `RuntimeError`. A reply whose `ok` is not true raises `RuntimeError("door refused timeline: ...")` as today.
- `render(reply)`: one line per row, ascending by time, Eastern `YYYY-MM-DD HH:MM:SS`, then `user_id`, `feed`, `operation`, `result_status`, `client_ip`, `item_name` (blank for None), two spaces between, trailing space trimmed. The empty and truncated lines stay as round 1.
- `main(argv, invoker=None, out=None, desktop=None, repo_root=None) -> int` (tests inject the first four; `out` defaults to `sys.stdout`; the invoker defaults to `door_client.build_invoker(args.profile, args.mfa_code, args.mfa_serial)`). Flags: `--account --start --end` (required unless `--derive`), `--detail`, `--json`,
  `--desktop`, `--profile`, `--mfa-code`, `--mfa-serial`, `--derive DATE [DATE ...]`.
  - Normal run: prints `render(fetch(...))` followed by a newline to `out`. With `--json` it prints the merged reply as indented JSON instead.
  - `--desktop`: writes the text it would have printed (the render, or the JSON with `--json`) plus a final newline through `door_client.write_desktop(text, <the stripped, lower-cased account>, <the --start value>, desktop=desktop, repo_root=repo_root)`, and prints ONLY the file path (and a newline) to `out`.
  - `--derive`: calls `door_client.derive_dates` and prints one line `"<date> <verdict>"` per date; returns 1 if any verdict is not `ok`.
  - Neither an account, a record nor a session key is ever printed to a log.

Tests: `data/m365_metadata/scripts/tests/test_door_client.py` (new) and `test_read_timeline.py` (extended), written against injected fakes like the check's, no network. Hard limits: ASCII only in code and comments.

DELETE: `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/derive_days.py` and `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/read_timeline_to_desktop.ps1`.

### ACCEPTANCE

<criterion id="R2-k2-AC1" cell_refs="SM-k-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py paging</invocation><expect>R2-PAGING-OK</expect></criterion>
`R2-k2-AC1` -- `detail` pages through a 1000-row door once per row in time order, a stuck page raises, the non-detail call is round 1's exactly, and every line says who acted.

<criterion id="R2-k2-AC2" cell_refs="SM-k-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py desktop</invocation><expect>R2-DESKTOP-OK</expect></criterion>
`R2-k2-AC2` -- `--desktop` lands the answer as one file on the derived Desktop, byte for byte what the screen would show, refused inside the repository; the MFA code becomes a session on the member alias with no key printed.

<criterion id="R2-k2-AC3" cell_refs="SM-k-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py retire</invocation><expect>R2-RETIRE-OK</expect></criterion>
`R2-k2-AC3` -- `derive_dates` and `--derive` do what `derive_days.py` did, and both round-1 stopgap files are gone.

<expected_criteria>R2-k2-AC1,R2-k2-AC2,R2-k2-AC3</expected_criteria>

Dry-run at the base 2026-10-17 ~06:2xZ: AC1 `R2-PAGING-REFUSED TypeError: fetch() got an unexpected keyword argument 'detail'`; AC2 and AC3 `... missing ...door_client.py` -- each FAIL as expected. Run from the repository (worktree) root. The real door and a real MFA session are NOT reachable from here; the live proof is the release's and Andrew's.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit. The two deletions are inside the grant.
- **LOCAL work only; NOTHING is called live.** No AWS call, no network. Tests inject every client. Never write a session key anywhere.
- `read_exposure.py` is another cell's file (SM-e-2, built against `door_client`'s contract above): never create or edit it. The door's Lambda files and the Terraform are not yours.
- **Refusal clause.** If a criterion cannot be met as written (or a check looks wrong), stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W10-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~10 <0.9.0_WK_SOC2_MSLOGS~10@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
data/m365_metadata/scripts/silver/door_client.py
data/m365_metadata/scripts/silver/read_timeline.py
data/m365_metadata/scripts/tests/test_door_client.py
data/m365_metadata/scripts/tests/test_read_timeline.py
org/tier1_exec/2.0.0_SA_COO~S1/deliverables/derive_days.py
org/tier1_exec/2.0.0_SA_COO~S1/deliverables/read_timeline_to_desktop.ps1
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-k-2`.
<owned_cells>SM-k-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-k2-AC1, R2-k2-AC2, R2-k2-AC3. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~10/SOC2_MSLOGS.TO-R2-k2.read-client.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-k2-AC1,R2-k2-AC2,R2-k2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three check lines, the `pytest` summary line (`python -m pytest data/m365_metadata/scripts/tests/test_door_client.py data/m365_metadata/scripts/tests/test_read_timeline.py -q`), the files deleted, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell (the client uses the member's own identity).
comp-adversary: DECLARED-NOT-APPLICABLE -- key non-disclosure and the in-repo refusal are in the checks.
lane: the <paths> block IS the grant.
</preflight>

Source: the CTO's round-1 analysis section 3 item 1 (@843819d1ab) and the carried ruling `ledger/CTO_CARRIED_ROUND2_DESKTOP_PRINTOUT_20261016.md`; the 4th-criterion reason does not arise (three criteria). The one PRD line the ruling adds (C-RESIDUAL: a printed answer on a Desktop sits outside the door's protection, the reader's to keep or delete) is the CTO's edit, not this cell's; the client's `--desktop` help text states it in one sentence.
