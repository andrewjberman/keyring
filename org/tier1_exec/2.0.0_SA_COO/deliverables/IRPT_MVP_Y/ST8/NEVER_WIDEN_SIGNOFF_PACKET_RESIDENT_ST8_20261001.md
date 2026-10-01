# Never-widen sign-off packet -- the resident st7 -> st8: the whole tree at CLOUD 9ac9b56d3c (the settings-row reader's repair)

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~11:5xZ.
**Authority:** CTO rulings batch 76 item 5 (the reader's repair is a member of the resident build, with the refused row
as its fixture) and batch 83 (the repair accepted as stated; item 3's identity condition built in before this packet).
**Ledger:** `irpt-resident-st8-20261001` (legs U1, D1, V1). No Lambda, IAM policy, queue, table or schema moves. One
host, one systemd unit. No vendor call.

## 1. What ships

Every member at ONE commit, `9ac9b56d3c6db8917581312c13d50c878dbfad99` (the merge of item 13, 4 of 4 files carried), no
member override. Built by `IRPT_MVP_P/build_resident_package.py --pin 9ac9b56d3c --enrolled-user-id 1276035`.

Member census against the RUNNING package (st7, S3 version `MH5dulKoCsbZS1Bd1wj7FjMR7xTT9rY0`, sha256 `c12a37d6..`,
downloaded and re-hashed here): **243 members; added 0, removed 0, changed 3, identical 240.**

| changed member | what it carries | numstat against a3b35fd376 |
|---|---|---|
| `ycharts/extract/extract.py` | `after_name()`: the name taken whole, or cut by the vendor (a proper prefix, three quarters or more of the name, holding the request id whole where the name carries one, directly followed by an ellipsis); `settings_row()` and the census use it; a row selected by a cut name carries `name_cut` | 42 added, 7 removed |
| `ycharts/generate/resident_worker.py` | the `TOLERANCE_TYPE` line ends `name=whole`, `name=cut` or `name=-`; the census line gains `cut=<n>` | 10 added, 7 removed |
| `reports/resident_bindings.json` | generated: the pin and the member pins | (generated) |

The capture library and wrapper are IDENTICAL to st7's (`9511060e..`, `55ddb8f7..`): the install script's library
step writes the same bytes over the host file.

## 2. The one move -- `a3b35fd376-st7` -> `9ac9b56d3c-st8`

- Tar `irpt-resident-9ac9b56d3c-st8.tar.gz`, sha256 `9c640e306f7c760abedf27226c19c349385de0a459dc88816d8148b49effd911`,
  758,484 bytes, S3 version `qMVedUlttPFVVOLsvmsx_mavt03zqkN8`. A NEW key (HeadObject 404 before the put). Read back by
  version: sha equal. The st7 key is untouched.
- Install script `ST8/resident_host_install_9ac9b56d3c-st8.sh`, sha256
  `6407b7cac436d264fb84399c57d504b9ecb00395d51ce3d17aeb7c88e8294b53`, S3 version `cDhKxZNv0XjSxGZ6kjyMfGBcM_Ab7e8L`,
  read back by version: sha equal. `bash -n` clean. Against st7's script with the names normalized it differs in the
  tar pin and two member pins (`resident_worker.py`, `extract.py`); no logic line differs.
- **Gate on the built package** (`ST8/GATE_OUTPUT_20261001.txt`): G1 243 of 243; G2 241 of 241 members equal
  `git show 9ac9b56d3c:<path>`; G3 98 of 98 `.py` members compile; G4 the route table and the installed boundary
  agree; G5 the census above. **PASS.**
- Suites at the branch tip the pin merges (82cdfe9802): `ycharts/generate/tests` 330 passed, 30 skipped;
  `ycharts/extract/tests` 39 passed; `ycharts/session/tests` 111 passed, 1 skipped; `intake/tests` 253 passed, 1
  skipped; `ops/tests` 186 passed, 22 skipped.
- **On the real bytes, offline, with the repaired reader:** the kept refused PDF of `REQ-7c7a9e45`
  (`ART-58f132884b3f5dc8..`) reads `Static`, `Custom`, `name_cut` true (census: 2 name lines, both cut, 1 accepted, the
  fee row refused as `PWNN`); a 2026-09-29 retained PDF reads `Static`, `Custom`, whole; the kept PDF read with ANOTHER
  job's name reads nothing (0 name lines). st7's extraction and certification of the kept PDF end PUBLISHED with the
  counts of the 09-29 control (`HOP8/OUTCOME_20261001.md`), and neither module changes here.

## 3. Blast radius, by branch (read from `extract.py` and `resident_worker.py` at the pin)

The printed-type check runs only for a job whose read-back carries a tolerated setting. One reader, one caller.

| the PDF's settings table, for the job's portfolio | BEFORE (st7) | AFTER (st8) |
|---|---|---|
| one row, the name printed whole, type Static | certifies | certifies; the line ends `name=whole` |
| one row, the name cut to a prefix of three quarters or more that holds the whole request id, ended by an ellipsis, type Static | REFUSED `TOLERANCE_REQUIRES_STATIC` (the 2026-10-01 jobs) | certifies; the line ends `name=cut` |
| the same cut row, type Dynamic | refused | refused (`type=Dynamic ... name=cut`), census printed, PDF kept |
| a cut shorter than three quarters, or one that loses part of the request id, or a prefix with no ellipsis, or a text that is not a prefix of the name | refused (no row) | refused (no row): unchanged |
| another portfolio's row (a comparison model, another request's portfolio) | not this job's row | not this job's row: a cut of another name is not a prefix of this one |
| two rows that pass for the name, on one page or two | refused (ambiguous) | refused (ambiguous): unchanged |
| no settings table | refused | refused: unchanged |
| a job with no tolerated setting | the check does not run | the check does not run |

What the change can newly ADMIT is exactly the second row: a Static row whose first cell is this job's own name, cut by
the vendor. It cannot admit a Dynamic portfolio, and it cannot take another portfolio's row for this one.

Not changed: the portfolio's name (`recipe.portfolio_name`), certification, publication, the kept-PDF rule, every
other member.

## 4. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. Before-read: running root `a3b35fd376-st7`, active; both queues 0/0; no non-terminal job.
3. One `head-object` of the script's key from the operator's side, printing VersionId
   `cDhKxZNv0XjSxGZ6kjyMfGBcM_Ab7e8L`; then the script is fetched on the host BY KEY, its sha256 checked there against
   `6407b7ca..`, and run through Systems Manager (`ST8/install_fetch_and_run.sh`, st7's wrapper with st8's names). Its
   refusals and its rollback to st7 are the script's own, as in the st6 and st7 packets.
4. V1 read-back on the host: running root `9ac9b56d3c-st8`; `resident_worker.py` `8ba63ba0fc0bff78..`; `extract.py`
   `c4c4908338fdce62..` naming `after_name`; the host library `9511060e04f45b51..` unchanged; the unit polls; queue 0/0.
5. The ledger closes at V1.

Not part of this act: any vendor call, any job. The one job attempt follows under its own window packet.

## 5. Rollback, per key

The root `a3b35fd376-st7` stays on the host; the script's rollback branch restores it with its receipt. The library
file is the same bytes before and after.

## 6. Not claimed

- That the next vendor PDF prints the name the way the last one did. If it prints it another way again, the job is
  refused, the census and the kept PDF say how.
- That the job then reaches READY: st7's certification of the kept PDF passes offline; publication on the host with
  the live stores has not run on a cut-name PDF.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~11:5xZ, on this packet's bytes at the commit that carries it. The write set is one new root
directory on one host, the host library (same bytes) with its backup, the cutover receipt with its backup, and the
unit's ExecStart. The blast radius is section 3; the rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

SIGNED, 2026-10-01T11:52Z, on the pre-signature blob `36f6cad885` (@c86ba1919c). Write set: one new root directory on one host,
the cutover receipt with its backup, the unit's ExecStart. The host library does not move. The apply protocol and the rollback
stand as written. No vendor call and no job is part of this act.

Read by this seat, from bytes (script `check_st8.py`, session scratch; reads only):

- Both tars by S3 version: st7 sha256 starts `c12a37d6`; st8 sha256 equals `9c640e30..d911`, 758,484 bytes.
- 244 file members in each; 0 added, 0 removed; 4 changed, which is the packet's 3 plus `SHA256SUMS`: `ycharts/extract/extract.py`
  (`c4c4908338fdce62`), `ycharts/generate/resident_worker.py` (`8ba63ba0fc0bff78`) and the generated bindings. The two digests equal
  the packet's read-back values. 242 of 244 members are byte-equal to `git show 9ac9b56d3c:` of a file of the same name.
- The diff of the two source members between the pins, line by line (42 added and 7 removed; 10 added and 7 removed):
  `after_name` accepts the whole name, or a proper prefix of at least three quarters of it followed directly by an ellipsis, and
  where the name carries a request id the prefix must reach past the END of that id; the settings-row pattern and the
  one-row rule are unchanged; the journal says `name=cut` whenever a cut name selected the row.

Batch 83 item 3 is met in the code as read (`len(head) >= identity.end()`); the test the packet names was not run by this seat.

Named by this half in addition:

1. A NAME WITH NO REQUEST ID (an advisor's or a comparison's portfolio) is accepted on the three-quarter prefix alone. The
   one-row rule is its only guard. That is accepted for this act because the job's own row is the one the tolerance check
   reads; it is one enrichment line for the round, not a condition here.
2. THE NEXT ATTEMPT'S JOURNAL LINE `IRPT_RESIDENT_TOLERANCE_TYPE ... name=cut` is read and quoted in its outcome: it is the first
   live use of the repair.
3. Not verified by this seat: the gate's G3 and G4, the suites, the repaired reader's run on the kept PDF, the install script.
