# CTO never-widen half -- NFRA_OPLGTW OG-rl-12, the opal-gateway r26 release

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~11:0xZ, in the place of `1.0.0_SA_CTO~O` (not live; ruling msgs 30779 and 30782).
**Ask:** `2.0.0_SA_COO~O` msg 30813, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-12_20261007.md`
@4d9d1208af (COO half SIGNED in its section 5).
**Release sha signed:** `feddb372443adbcf139febab35b69f109e49b664`, on live `240ac2fe5a`.

## VERDICT: SIGNED on `feddb37244`, under the ask's three preconditions and two conditions of this half (C1, C2).

## What this seat read at signing (its own reads of the release commit)

| read | result |
|---|---|
| `git rev-list --count 240ac2fe5a..feddb37244`, and the parent | 1 commit; parent `240ac2fe5a` |
| `git diff --stat 240ac2fe5a feddb37244` | 10 files, +467/-10, all under `infra/aws/ec2/opal-gateway/` |
| `identity_tool_allowlist.txt` | +6 lines: ONE row, `opalbloomberg@opalinvest.com opal_data_refresh_status`, not client-qualified, with Andrew's word cited in the comment |
| Andrew's record for that row (`ANDREW_DIRECT_20261007_041xZ_CONCIERGE_MAY_CALL_DATA_REFRESH_STATUS_TOOL_YES.md`) | "rec approved"; it authorizes this one read-only tool for this one identity, "in a later release". The row matches it and adds nothing else. |
| `integration.py`: the id check | `_check_execution_id` (`[A-Za-z0-9_:-]{1,200}`, fullmatch) runs in the status tool before the JWT is minted, and in `_read_status_once` before the GET. A refused id makes no request. No `.` or `/` can reach the URL path. |
| the binding term of `ROUND_ANALYSIS.round24.md` section 3 | MET at this sha: the allowlist row and the id check are in the same commit |
| `integration.py`: the dedupe | the signature is (name, size, content hash); `hash_readable` false skips the dedupe lookup, so the send fires. The item is resolved by a plain GET with no `$select`. |
| `app/server.py` | +1 line, the chart route. Its position before `/rivalfunds/{day}` is the COO half's read, not this seat's. |

Not read by this seat: the worker's ANNOUNCE, the host, the test runs, and the two verify scripts. The live sha is taken from the
ask; its step 1 re-reads live before the act and re-cuts if it moved.

## Consumers this half names

- **The daily Bloomberg send** (`/terminal-upload`, `/bbg-daily`, through `opal_data_refresh_upload`). Movement 4 changes what a
  repeated send does. Today a second send of same-named, same-sized files inside 30 minutes never fires. After r26 it fires when the
  content differs, which is the fix, and ALSO whenever a hash cannot be read on either file (C1).
- **The Teams concierge** (`/bbg-teams-assist`), which gains the status tool. That tool's `displayed_date` is null against the
  served manifest (row Z-W28-S13, not fixed by r26). So the concierge's first use reads a status and a null date. Disclosed in the
  slug; named here because r26 is what puts the tool in that caller's hands.
- **The rival-funds page** (ETFS_RIVALS md-1), not yet deployed. On release day the chart route can only return 404.

## C1 -- an unreadable hash must not silently switch the retry protection off

The ask discloses that the drive item's `file.hashes` shape was not probed and that the dedupe rests on offline tests. If Graph
returns no hash and no `cTag` for these files, r26 never dedupes, and a send repeated after a dropped transport fires the pipeline
a second time. r25 (live) dedupes that case on name and size.
- This seat accepts the release as built, because the send now returns right after `/trigger` and both caller skills say never to
  re-send on a dropped transport.
- **Owed by `2.0.0_SA_COO~O` at the first real send after the deploy** (it is another project's send; this is a read, not a send):
  whether each of the two items carried a readable hash. If the release gives no way to see that, the next issuance carries one
  cell that puts it in the send's return.
- (a) Readable on both: nothing more.
- (b) Unreadable on either: one cell in the next issuance falls back to the r25 name-and-size key when the hash is unreadable, and
  until it ships the callers are told a repeat fires.

## C2 -- the allowlist row lands with the check, or not at all

If the release set is ever re-cut or split before the act, the allowlist row does not ship without `_check_execution_id` in the
same deploy. Rollback trigger added to the ask's list: after the deploy, a status-tool call with an id containing `/` or `.`
makes a request. (The ask's rehearsal already shows 0 requests on a refused id; this keeps it as a post-deploy arm.)
- (a) Refused with no request: stands.
- (b) Any request made: roll back.

## Accepted as the ask states them

- The three preconditions: three halves on this sha; the four ETFS_RIVALS commits on origin; today's Bloomberg send confirmed served.
- The blast radius of section 2 and its "unchanged" list; the rollback (redeploy `/c/tmp/og-rb20`); the rollback triggers.
- The limits of section 3, including that the concierge's token still carries 17 scopes and that this release moves that in
  neither direction.

## Not covered by this half

- Any real send. The concierge's re-consent (Andrew's acts, R37). Row Z-W28-S17's older files.

-- 1.0.0_SA_CTO~Z
