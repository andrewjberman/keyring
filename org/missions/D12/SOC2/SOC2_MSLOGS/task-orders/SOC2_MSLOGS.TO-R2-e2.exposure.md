# TO SOC2_MSLOGS.TO-R2-e2 -- FWD-2 starts: the exposure read (door module and client)

<to_id>SOC2_MSLOGS.TO-R2-e2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~13</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Risk note:** WORLD only by the gate's path floor (a Lambda path is in `<paths>`); the cell calls nothing live. The issuer wires the new op into `handler.py` at the merge.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-e-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** FWD-2 | **depends_on:** none (builds to the EXPOSURE CONTRACT v1 and the DOOR CLIENT CONTRACT v1, both fixed in the decomposition)

---

## WORKER FACE

### THE CELL

`SM-e-2`. FWD-2: for a window, the responder knows the exposure -- what the account opened, and everything that went to someone outside. Silver holds one row per audit record, with the whole record in `raw_json`. This cell computes the exposure lists from those rows (a door module) and prints them (a client). Andrew-direct premise:
"if any opal user is hacked, we want to be able to know the exposure; what was seen, what the duration period was". No content is ever fetched (the PRD's C-CONTENT): the audit records are metadata, and where they do not say something the answer SAYS they do not.

READ first: `org/missions/D12/SOC2/SOC2_MSLOGS/prd/SOC2_MSLOGS_PRD.md` rows FWD-2, C-CONTENT, C-READS; `data/m365_metadata/scripts/silver/read_timeline.py` (the pattern for `fetch`, `render`, `main`; do NOT edit it); `infra/aws/lambda/globgrph-trino-access/silver_builder.py` (the row columns and `raw_json`);
the check `org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py` (the functions `exposure_door` and `exposure_client`: the synthetic rows there show the record shapes and are exactly how your work is measured).

BUILD TO THIS CONTRACT:

*Door module* `infra/aws/lambda/globgrph-trino-access/exposure.py` (stdlib only): `compute(rows, account) -> {"opened": [...], "left": [...], "unrecorded": [...]}`. `rows` are the silver reader's detail rows: dicts with `time` (ISO UTC Z), `feed`, `operation`, `client_ip`, `item_name`, `user_id`, `record_id`, `result_status` and `raw_json` (a JSON STRING of the whole record).
Rows whose `user_id` is not the lower-cased, stripped `account` are ignored. Every list is ascending by `time`, ties in input order. The account's DOMAIN is the part after `@`, compared case-insensitively.
- `opened`: a row whose `operation` is one of `MailItemsAccessed`, `FileAccessed`, `FileDownloaded`, `FilePreviewed`, `FileSyncDownloadedFull`, `FileSyncDownloadedPartial`. Entry keys: `time`, `operation`, `feed`, `item_name`, `client_ip`, `record_id`.
- `left` (to someone outside the domain). Entry keys: `time`, `kind`, `recipient`, `operation`, `item_name`, `record_id`.
  - `share_invitation`: operation `SharingInvitationCreated`; `recipient` is the raw record's `TargetUserOrGroupName`; included when it is an address with a domain other than the account's, or when the raw `TargetUserOrGroupType` is `Guest`; a colleague in the domain with another type is NOT included.
  - `anonymous_link`: operation `AnonymousLinkCreated`; `recipient` is the fixed text `anyone with the link`; always included.
  - `forward_rule`: operations `New-InboxRule`, `Set-InboxRule`, `UpdateInboxRules`. The raw record has a `Parameters` list of `{"Name": ..., "Value": ...}`. For each parameter named `ForwardTo`, `ForwardAsAttachmentTo` or `RedirectTo`, split `Value` on `;`, `,` and whitespace, strip a leading `smtp:` (any case) from each piece, and make ONE entry per address whose domain differs from the account's.
  - `mailbox_forward`: operation `Set-Mailbox`; the same rule over the parameters `ForwardingSmtpAddress` and `ForwardingAddress`.
  - A raw record that is not valid JSON, or lacks a field, never raises: that row simply yields no `left` entry.
- `unrecorded`: a list of `{"category": ..., "reason": ...}`. ALWAYS `mail_recipients` (reason: the audit feed does not say who a sent mail went to). Also `mail_opened` when no row of the input has operation `MailItemsAccessed` (reason: no MailItemsAccessed record in this window, so mail opened is not recorded for this account or licence, or none was opened).
- NO entry carries `raw_json`, a raw record or `ObjectId`.

*Client* `data/m365_metadata/scripts/silver/read_exposure.py`:
- `fetch(invoker, account, start, end) -> reply`: validates the account exactly as `read_timeline.fetch` does (string, stripped, lower-cased, `local@domain`, else `ValueError` before any call), calls `invoker({"op": "exposure", "account": ..., "start": ..., "end": ...})` exactly once, and raises `RuntimeError("door refused exposure: ...")` when the reply's `ok` is not true.
- `render(reply) -> str`: three sections in this order, each headed by its word alone on a line: `OPENED`, `LEFT`, `NOT RECORDED`. One line per entry, Eastern `YYYY-MM-DD HH:MM:SS` first then the fields (opened: operation, item_name, client_ip; left: kind, recipient, item_name; not recorded: category and its reason), two spaces between, trailing space trimmed.
  An empty section prints the single line `none`. If the reply has `truncated` true, a final line `TRUNCATED: narrow the window`.
- `main(argv, invoker=None, out=None, desktop=None, repo_root=None) -> int` with flags `--account --start --end --profile --mfa-code --mfa-serial --desktop`; the invoker defaults to `door_client.build_invoker(args.profile, args.mfa_code, args.mfa_serial)`, imported INSIDE `main` (another cell writes `door_client.py` to the DOOR CLIENT CONTRACT v1 in the decomposition; it does not exist in your worktree, so your tests inject the invoker and never import it).
  Prints `render(fetch(...))` and a newline to `out` (default `sys.stdout`); with `--desktop` it writes the same text plus a newline through `door_client.write_desktop(text, account, start, desktop=desktop, repo_root=repo_root)` (also imported inside `main`) and prints only the returned path. Never print an account or a record to a log.

Tests: `infra/aws/lambda/globgrph-trino-access/tests/test_exposure.py` and `data/m365_metadata/scripts/tests/test_read_exposure.py`, synthetic only. Hard limits: ASCII only; stdlib only (the client imports `door_client` lazily).

### AMENDMENT 1 (issuer 2.0.0_SA_COO~S1, 2026-10-17 ~08:4xZ) -- the door serves the op: apply the issuer's hookup patch

The module and the client are merged (8ed6ce721a plus 96d701d119). The one hookup of the round, wiring `exposure` into `handler.py`, belongs to this cell ("Hookups at the merge" in the decomposition). The issuer wrote it and it is saved as the patch
`org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/hookup_exposure.patch` (143 lines): `handler.py` gains the `exposure` entry in `ALIAS_OPS["member"]` and in `KNOWN_OPS`, `EXPOSURE_MAX_ENTRIES = 5000`, the function `_exposure`, its dispatch branch and docstring lines; `tests/test_handler.py` gains the updated op-set test and five exposure tests.
(The issuer's own commit of those two files was refused by the lane gate, lane CLOUD_OPS_OR_ETL; the lane holder applies the patch.) Your worktree is a fresh one from the current branch head; the earlier commits of this order are already merged.
1. `git apply --check org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/hookup_exposure.patch`, then `git apply` of it. If `--check` fails, that is a BLOCKING row with the error; do not hand-edit to make it fit. You write no new logic.
2. `python -m pytest infra/aws/lambda/globgrph-trino-access/tests -q` all pass; `python -m ruff check --target-version py39 infra/aws/lambda/globgrph-trino-access` clean.
3. New criterion AC3 below; commit the two patched files, the rewritten proof instance (now three rows) and the order flip, as before.
Dry-run at the base 2026-10-17 ~08:3xZ: AC3 `R2-HOOKUP-REFUSED member answer is ['error', 'ok']; ...` FAIL as expected; with the patch applied `R2-HOOKUP-OK`.

### ACCEPTANCE

<criterion id="R2-e2-AC1" cell_refs="SM-e-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py exposure_door</invocation><expect>R2-EXPOSURE-OK</expect></criterion>
`R2-e2-AC1` -- from detail rows the door module lists what was opened and what left to an outside recipient, says plainly what the feed does not record, and carries no raw record.

<criterion id="R2-e2-AC2" cell_refs="SM-e-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py exposure_client</invocation><expect>R2-EXPCLIENT-OK</expect></criterion>
`R2-e2-AC2` -- the client asks for exactly the `exposure` payload, refuses a bad account before any call, and prints the three sections in Eastern time.

<criterion id="R2-e2-AC3" cell_refs="SM-e-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py hookup</invocation><expect>R2-HOOKUP-OK</expect></criterion>
`R2-e2-AC3` -- (AMENDMENT 1) the door serves `exposure` on the member alias only, asks the reader for detail rows once, answers opened, left, unrecorded and truncated, logs `op=exposure outcome=ok`, and refuses a bad account.

<expected_criteria>R2-e2-AC1,R2-e2-AC2,R2-e2-AC3</expected_criteria>

Dry-run at the base 2026-10-17 ~06:2xZ: AC1 `R2-EXPOSURE_DOOR-REFUSED missing ...exposure.py`; AC2 `R2-EXPOSURE_CLIENT-REFUSED missing ...read_exposure.py` -- each FAIL as expected. Run from the repository (worktree) root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL work only; NOTHING is called live.** No AWS call, no network.
- `handler.py` and `tests/test_handler.py` are granted for AMENDMENT 1 only, to apply the issuer's patch; you write nothing else in them. (Before AMENDMENT 1 they were another queue's files.) `read_timeline.py` and `door_client.py` are another cell's: never create or edit them.
- **Refusal clause.** If a criterion cannot be met as written (or a check looks wrong), stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W13-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a check to pass it. A record shape you believe Microsoft ships differently from the contract is a surprise row, not a silent change of the contract.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~13 <0.9.0_WK_SOC2_MSLOGS~13@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/lambda/globgrph-trino-access/exposure.py
infra/aws/lambda/globgrph-trino-access/handler.py
infra/aws/lambda/globgrph-trino-access/tests/test_handler.py
infra/aws/lambda/globgrph-trino-access/tests/test_exposure.py
data/m365_metadata/scripts/silver/read_exposure.py
data/m365_metadata/scripts/tests/test_read_exposure.py
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-e-2`.
<owned_cells>SM-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-e2-AC1, R2-e2-AC2, R2-e2-AC3. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~13/SOC2_MSLOGS.TO-R2-e2.exposure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-e2-AC1,R2-e2-AC2,R2-e2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two check lines, the `pytest` summary line (`python -m pytest infra/aws/lambda/globgrph-trino-access/tests/test_exposure.py data/m365_metadata/scripts/tests/test_read_exposure.py -q`), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell; it adds a read op and a client.
comp-iam: DECLARED-NOT-APPLICABLE -- the new op is served on the existing member alias; no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE; the no-raw-record rule is in AC1.
lane: the <paths> block IS the grant.
</preflight>

Source: the CTO's round-1 analysis section 3 item 7 (@843819d1ab); PRD v0.2 FWD-2 and C-READS `exposure`; decomposition round 2 cell SM-e-2 and its EXPOSURE CONTRACT v1. The record shapes are Microsoft's documented audit schema; the first real read of them is the release's and Andrew's.
