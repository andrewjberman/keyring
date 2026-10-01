# Never-widen sign-off packet -- the resident st6 -> st7: the whole tree at CLOUD a3b35fd376, and the host capture library at the same pin

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~10:1xZ.
**Authority:** CTO rulings batch 76 item 5 ("the next resident build, before any further job attempt ... The release is
its own packet with both halves"), with its members ordered in batch 70 item 5, batch 72 item 12, batch 76 items 5 and
6, batch 65 and PRD ruling 21. **Ledger:** `irpt-resident-st7-20261001` (legs U1, D1, V1).
No Lambda, IAM policy, queue, table or schema moves. One host, one systemd unit, one host file. No vendor call.

## 1. What ships

Every member at ONE commit, `a3b35fd3765a24c597827544f42278a1b2bbb3cc` (the merge of items 7 to 12, 16 of 16 files
carried), no member override. Built by `IRPT_MVP_P/build_resident_package.py --pin a3b35fd376 --enrolled-user-id 1276035`.

Member census against the RUNNING package (st6, S3 version `G6ZEskNLZl_v7QG_aZ9IfxOPrFVmDd3J`, sha256 `3eb86dd9..`,
downloaded and re-hashed here): **243 members; added 0, removed 0, changed 11, identical 232.**

| changed member | what it carries | commit |
|---|---|---|
| `ycharts/generate/current_authority.py` | a SERVICE row with no `allowedFirmIds` is refused `ACTOR_FIRM_NOT_ALLOWED` on every firm (PRD ruling 21) | ffb94090dc |
| `ycharts/generate/resident_worker.py` | a permanent authority refusal at the RESOLVE phase ends the upload by name (batch 65); the resolve line carries the lookup's refusal class; on a printed-type refusal the row census is printed and the PDF is kept as evidence (batch 76 items 5, 6) | ffb94090dc, 2775cae84b |
| `intake/resolution_broker.py` | the lookup port keeps the closed class of the answer it refused | ffb94090dc |
| `ycharts/session/operation_lease.py`, `resident_session.py` | the upload's ticker lookup is made with NO session, under the provider lease (batch 72 item 12) | 1253002a2f |
| `ycharts/session/host_capture.py` | the capture wrapper's stderr is kept in `last-capture.stderr` (0600, last 64 KiB) instead of `/dev/null` | 25c32c3b58 |
| `ycharts-host/ycharts_session.js` (the host file) | each of the 7 `AuthError` sites carries a closed `reason` (batch 70 item 5); section 3 | 25c32c3b58 |
| `ycharts/extract/extract.py` | `settings_census()` and `row_shape()`: counts and closed shapes, no text | 2775cae84b |
| `ycharts/generate/comparison_catalogue.py` | a model-written classifications row is never listed (MDPF_SECCLASS ruling 1); not on a job's path, no route serves the catalogue | e118089403 |
| `_authz/served.py` | `2.0.0_SA_COO~P`'s fail-closed service boundary (batch 62 item 4); a Lambda-side module the package carries, not on the resident's path | f9a00f732c |
| `reports/resident_bindings.json` | generated: the pin, the member pins and the library pin below | (generated) |

**Identical to st6, 232 members**, among them `recipe.py`, `resident_main.py`, `job.py`, `transport.py`,
`publisher.py`, `templates.json`, `ycharts/session/broker.py`, `certify.py`, `publication.py`,
`_scope/canonical_profile_reads.py`, `reports/resident_installed.py`, `infra/logic/registry/reporting_policies.json`
and the capture wrapper (`55ddb8f7..`).

## 2. The one move -- `36dfa80058-st6` -> `a3b35fd376-st7`

- Tar `irpt-resident-a3b35fd376-st7.tar.gz`, sha256 `c12a37d6934840691d98d93e4b8196f8744a09f02dbce4682e7cc2c8b024bf01`,
  757,559 bytes, at `ec2/investor-reporting-ycharts/resident/` in `opal-313476888478-lambda-artifacts`, S3 version
  `MH5dulKoCsbZS1Bd1wj7FjMR7xTT9rY0`. A NEW key (HeadObject 404 before the put). Read back by version: sha equal; 244
  file members (243 plus `SHA256SUMS`). The st6 key is untouched.
- Install script `ST7/resident_host_install_a3b35fd376-st7.sh`, sha256
  `ad9f91d5acd87bd2bf4627265dd3cb00d9da14a24da07f86b77a3c18401ec7a2`, same prefix, S3 version
  `cYhOzVvvcvFik2D7W419SBuZGVa98nw8`, read back by version: sha equal. `bash -n` clean. Against st6's script with the
  root names normalized it differs in the ledger name, the tar and library pins, and four member pins
  (`resident_worker.py`, `current_authority.py`, `extract.py`, `host_capture.py`); no logic line differs.
- **Gate on the built package** (`live_walk/resident_package_gate.py`; output in `ST7/GATE_OUTPUT_20261001.txt`):
  G1 243 of 243 members hash to their SHA256SUMS line; G2 241 of 241 members equal `git show a3b35fd376:<path>` (not
  compared: the generated bindings and the census, pinned by the builder); G3 98 of 98 `.py` members compile; G4 the
  route table and the installed boundary agree (2 operation constants, 0 unserved); G5 the census above. **PASS.**
- Suites at the branch tip the pin merges (2775cae84b): `ycharts/generate/tests` 329 passed, 30 skipped;
  `ycharts/session/tests` 111 passed, 1 skipped (the one node that runs a real wrapper needs a POSIX host);
  `ycharts/extract/tests` 35 passed; `intake/tests` 253 passed, 1 skipped; `ops/tests` 186 passed, 22 skipped; the
  capture library's offline suite `all_pass` true. `reports/tests/test_resident_installed.py` run alone: 10 passed, 1
  failed, the same pre-existing path defect the st6 packet named (the file is `2.0.0_SA_COO~P`'s).

## 3. The capture library moves with the package again

The bindings pin the host's `ycharts_session.js`; `resident_installed.py` and every capture refuse a file that differs.
The host file is `0fec0ca910ee5fb1..` (st6). At a3b35fd376 it is
`9511060e04f45b51744f7eef68f4a1c4921367b3388fe9acee8b83d708ddcc90`. The one commit between them is 25c32c3b58: 9 lines
added and 2 removed by numstat, all inside the record literals of the seven `AuthError` throws (a `reason:` token each; the
re-presented-form record also carries the submission's own booleans and the step list). No control flow, selector,
route or wait changes. The script installs it over the host file after `node --check`, with the old file kept beside
it. **Not proven live:** no sign-in has run on this library. The library signed in at 08:21Z as `0fec0ca9`.

## 4. Blast radius, by branch (each read from the code at the pin)

Writers of an Analysis job's state and of an upload's normalization row on the host: the resident, one process.

| case | BEFORE (st6) | AFTER (st7) |
|---|---|---|
| an upload's ticker lookup | made on the stored session: reads `ycharts/session/current`, sends its cookies | made with NO session: no secret read, no cookie; the same provider lease, spacing and deadline; a caller with no cookie was answered 200 JSON at 08:42Z |
| the lookup is refused | `RESOLVE state=RETRY code=PROVIDER_READ_UNAVAILABLE`; at the fourth receive `RESOLVE_RETRY_EXHAUSTED` | the same states and receive count; the code also carries the closed class (`:STATUS_403`, `:WAF_CAPTCHA`, `:LOGIN_DESTINATION`, `:ROUTE`, `:CONTENT_TYPE`, `:BODY`, `:ROWS_UNVERIFIED`, or a lease code) |
| upload whose actor's row is gone, or whose row does not allow the firm | raised at the resolve phase, retried, dead-lettered at the fifth receive | the row ends NEEDS_CORRECTION with the refusal's own code, the message is deleted, one `RESOLVE state=ATTENTION code=<code>` line; no vendor read |
| upload whose actor is refused reversibly (`ACTOR_INACTIVE` and the rest) | raised and retried | unchanged |
| a job by a SERVICE actor whose row carries `allowedFirmIds` naming the firm | runs | runs |
| a job or upload by a SERVICE actor whose row carries NO `allowedFirmIds` | runs (read as unrestricted) | ends by name `ACTOR_FIRM_NOT_ALLOWED`; population: 1 service principal of 52 profile rows, and its row carries the attribute, so no principal changes behaviour |
| a person's row with no `allowedFirmIds` | runs | runs |
| a sign-in the resident makes fails | `CAPTURE_FAILED:AUTH_FAILED`; stderr discarded | `CAPTURE_FAILED:AUTH_FAILED:<REASON>`; stderr in `/opt/investor-reporting-ycharts/last-capture.stderr` (0600); same one-refresh allowance, same cooldown, same outcome |
| a job whose PDF passes the printed-type check | certifies | certifies; no new line, nothing extra stored |
| a job whose PDF fails the printed-type check | ATTENTION `TOLERANCE_REQUIRES_STATIC`; nothing kept | the same state and code; plus `IRPT_RESIDENT_TOLERANCE_ROWS` (counts and shapes) and the PDF stored as `ORIGINAL_VENDOR_PDF` in the job's own firm under a logical id carrying `-refused-`, `IRPT_RESIDENT_REFUSED_PDF kept=1`. No `pdf` checkpoint, no accepted pointer, no route: the status answer stays UNAVAILABLE with no document (tests named in commit 2775cae84b). The family's existing 30-day rule for an unreferenced artifact applies |
| every other path of a job (session, holdings upload, portfolio, read-back, validate, generate, download, certify, publish) | as run today by `REQ-602834fd` | byte-identical members (`recipe.py`, `job.py`, `transport.py`, `publisher.py`, `broker.py`) |

Every puller of what moves: the tar key is read by the install script only; the unit is the only consumer of
`irpt-generation`; the host library is read by the capture wrapper, which only this unit's `HostCapture` and an
operator run invoke (0 timers).

## 5. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. Before-read on the host: running root `36dfa80058-st6`, active; both queues 0/0; no non-terminal job.
3. One `head-object` of the script's key from the operator's side, printing that the latest VersionId is
   `cYhOzVvvcvFik2D7W419SBuZGVa98nw8`; then the script is fetched on the host BY KEY, its sha256 checked there against
   `ad9f91d5..`, and run through Systems Manager (the st6 addendum's form: the host role holds no `GetObjectVersion`).
   It refuses on a non-empty queue (twice), a tar or member that is not the built bytes, a library that does not
   parse, or a failed factory; each refusal restores what it moved. After the install it rolls back to st6, library
   and receipt included, on a non-zero install, an inactive unit, no poll in 30 s, or a Traceback.
4. V1 read-back on the host: the running root is `a3b35fd376-st7`; the running `resident_worker.py` digest is
   `2ba09afaa8a2fc9e..` and names `keep_refused_pdf` and `_with_lookup_class`; `current_authority.py` is
   `5291b3be7e0006ad..`; `host_capture.py` is `8288e724e843cb89..`; `extract.py` is `3f5e2bb0bc2299f6..`; the host
   library is `9511060e04f45b51..`; the unit polls; both queues 0/0.
5. The ledger closes at V1.

Not part of this act: any vendor call, any job. The one job attempt batch 76 item 5 names follows under its own window
packet.

## 6. Rollback, per key

- The root: `36dfa80058-st6` stays on the host; the script's own rollback branch restores it, runnable by hand.
- The library: `ycharts_session.js.before-a3b35fd376-st7` is the old file; the st6 bindings pin it, so root and
  library always move back together.
- The receipt: `cutover_receipt.36dfa80058-st6.json`, copied before the write.
- `last-capture.stderr` and a kept refused PDF are evidence files; a rollback leaves them and nothing reads them.

## 7. Not claimed

- That the sessionless lookup works on the host through the resident's own child process: its transport and lease
  are proven offline, and a cookie-less GET was answered at 08:42Z by a plain client. Its first live run is the next
  attempt's upload; a refusal there costs no vendor mutation and now names its class.
- That a sign-in succeeds on the new library, or that the resident's own sign-in is repaired: the four failures are
  unnamed until one happens on this build.
- That hop 8 passes: nothing here changes the printed-type check's verdict. The build makes its refusal readable.
- The node of `test_host_capture.py` that runs a real wrapper did not run on this device.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~10:1xZ, on this packet's bytes at the commit that carries it. The write set is one new root
directory on one host, one host file with its backup, the cutover receipt with its backup, and the unit's ExecStart.
The blast radius is section 4, each branch read from the members at a3b35fd376; the rollback is section 6.

## CTO half -- 1.0.0_SA_CTO

SIGNED, 2026-10-01T10:20Z, on the pre-signature blob `101d821fe8` (@9b1ff6fb28). Write set: one new root directory on one host,
the host library with its backup, the cutover receipt with its backup, the unit's ExecStart. The apply protocol of section 5 and
the rollback of section 6 stand as written. No vendor call and no job is part of this act.

Read by this seat, from bytes (script `check_st7.py`, session scratch; reads only):

- Both tars downloaded by S3 version. st7: sha256 equal to `c12a37d6..`, 757,559 bytes. st6: sha256 starts `3eb86dd9`.
- 244 file members in each; 0 added, 0 removed; 12 changed, which is the packet's 11 plus `SHA256SUMS`.
- 242 of 244 st7 members are byte-equal to `git show a3b35fd376:` of a file of the same name; the two that are not are the
  generated `SHA256SUMS` and `reports/resident_bindings.json`, as the packet says of its gate G2.
- The changed members' digests equal section 5's read-back values: `resident_worker.py` `2ba09afaa8a2fc9e`,
  `current_authority.py` `5291b3be7e0006ad`, `host_capture.py` `8288e724e843cb89`, `extract.py` `3f5e2bb0bc2299f6`, the host
  library `9511060e04f45b51`.
- The library's diff between the two pins, line by line: 9 added, 2 removed, every one inside an `AuthError` record (a `reason`
  token, and on the re-presented-form site the submission's booleans and the step list). No control flow, selector or wait moves.
- `resident_worker.py`'s diff: the refused PDF is put through the job's own artifact port for the record's own owner, with the
  composition's retention reference; a failure to keep it prints one line and never changes the refusal; the tolerance census
  prints counts and closed shapes; a permanent authority refusal at the resolve phase ends the upload by name.

All eleven branches of section 4 are covered. Section 7's four statements are accepted as limits of this act, not as conditions.

Named by this half in addition:

1. THE KEPT PDF IS STORED AS KIND `ORIGINAL_VENDOR_PDF`, the same kind a READY job's retained PDF carries. This seat did not read
   every reader of that kind. The test named in commit 2775cae84b (the status and reopen routes return no document for a job
   that has only refused evidence) is the cover; at the first kept PDF, one live status read of that job shows UNAVAILABLE with
   no document before the PDF is used for anything.
2. THE NEXT JOB ATTEMPT is the first live run of three changed things at once: the sessionless lookup, the refusal classes, and
   (if it reaches hop 8 and is refused) the kept PDF. Its window packet says which of the three each stop reads.
3. Not verified by this seat: the gate's G3 and G4, the five test suites' counts, the install script's own refusals and rollback
   branches (read as described, not exercised here), the host's state before the install.
