# Never-widen sign-off packet -- the resident st5 -> st6: the whole tree at CLOUD 36dfa80058, and the host capture library at the same pin

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-01 ~05:5xZ.
**Authority:** CTO rulings batch 61 @8dcf5bbe7a item 2(c) ("the resident at CLOUD HEAD, ~Y's, under a ledger") and item 4
(row S244 accepted). **Ledger:** `irpt-resident-head-st6-20261001` (OPEN @36dfa80058; legs U1, D1, V1, R1).
No Lambda, IAM policy, queue, table or schema moves. One host, one systemd unit, one host file.

## 1. What ships

The package is every member at ONE commit, `36dfa80058dffc73213fed213ca5b626b9c91082`, with no member override (st5
carried 12). Built by `IRPT_MVP_P/build_resident_package.py --pin 36dfa80058 --enrolled-user-id 1276035`.

Member census against the RUNNING package (st5, S3 version `vJOIoCTh5mGuWbbLmMd43INv3t3FnEQ5`, sha256 `71998920..`):
**243 members; added 18, removed 0, changed 39, identical 186.** Each changed member was walked back to the commit its
running bytes equal (38 of 38 found; the 39th is the generated bindings file): `ST6/changed_members_history.json`.

What the changed and added members carry, by the path that reaches them:

| path | members | commits the package adds |
|---|---|---|
| the job's authority | `ycharts/generate/current_authority.py`, `_scope/canonical_profile_reads.py` | 2704705672 (IB-yr-293: the projection carries `allowedFirmIds`; `decide()` refuses `ACTOR_FIRM_NOT_ALLOWED`) |
| a permanently refused job | `ycharts/generate/resident_worker.py` | 62535e0fdc (ends the job ATTENTION with the refusal's own code) |
| the vendor request ledger | `ycharts/generate/job.py`, `transport.py` | b21aacec70 (IB-yr-291: the receipt carries `vendor_requests`, shapes only) |
| certification | `ycharts/extract/certify.py`, `publication.py`, `ycharts/generate/publisher.py` | b75e571a74 / 3a16cc442b (publication is handed the chosen comparisons and refuses `COMPARISON_NOT_PRINTED`) |
| the upload answer's words | `intake/uploads.py`, `ops/owned_report.py`, `ops/status.py` | 6b96d460f6, 57ebb7ac6c (correction words; no state or code changes) |
| the capture library (host file) | `ycharts-host/ycharts_session.js` | 4467f36184 (IB-yr-292: opt-in HAR recording behind `YC_RECORD_HAR=1`; section 3) |
| not on the resident's path (Lambda-side modules the package carries) | `_authz/{enforce,loaders,routetable,served}.py`, `ops/{entry,prospect_dates}.py`, `reports/{generate_installed,status_installed}.py`, `ycharts/generate/{entry,comparison_catalogue}.py` | the export, service-boundary and catalogue commits listed in the history file |
| registry and naming | `lib/opal_naming.py`, `infra/logic/registry/{exemptions,remediations,scopes,systems}.json`, `data/firm_registry.json` | transcripts and rivalfunds scope rows, VENDOR display names, one fence exemption; `reporting_policies.json` is IDENTICAL |
| contracts (data files) | 9 changed and 17 added schema and fixture files | Holdings, Performance, Directory, upload and catalogue contract edits; none is read by a job |

**Identical to st5, 186 members**, among them `recipe.py`, `resident_main.py`, `extract.py`, `templates.json`,
`ycharts/session/broker.py`, `ycharts/session/host_capture.py`, `_scope/maintained_sources.py`,
`reports/resident_installed.py` and the capture wrapper.

Two registry reads this seat made because a job's outcome depends on them:
- The foreign-firm name check (`publication.printed_firm_names`) reads client FIRM scopes from `scopes.json`. Running
  registry (14b52ca13a) and the pin: 3 client firms each, the printed-name sets EQUAL (49 Financial / 49F; Cottonwood
  Capital Advisors; Inflection Wealth Management).
- The reporting policy row is unchanged (`reporting_policies.json` is among the 186 identical members), so the
  destination revision a job's composition was accepted under still resolves.

## 2. The one move -- `fe64236bbb-st5` -> `36dfa80058-st6`

- Tar `irpt-resident-36dfa80058-st6.tar.gz`, sha256 `3eb86dd967db4b672c5243267f3142d53ee227d506f6a12e086e9d69755864b2`,
  753,160 bytes, at `ec2/investor-reporting-ycharts/resident/` in `opal-313476888478-lambda-artifacts`, S3 version
  `G6ZEskNLZl_v7QG_aZ9IfxOPrFVmDd3J`. A NEW key (HeadObject 404 before the put; the st5 key read 731,610 as the positive
  control). Read back by version: sha equal. The st5 key is untouched.
- Install script `ST6/resident_host_install_36dfa80058-st6.sh`, sha256
  `830682df93d1a05cc2618a16305783e0019636dc538d924e696832289b9af9a6`, staged at the same prefix, S3 version
  `Xxgbj.B9Yw4XiUUuDrKG4PGYmKIXtTm6`, read back by version: sha equal. `bash -n` clean. It is st5's script with three
  changes: the member pins (16, plus the library) are read from THIS package by the gate tool; the capture library
  moves (section 3); a rollback restores the library as well as the root and the receipt.
- **Gate on the built package** (`live_walk/resident_package_gate.py`, this seat's standing gate on built bytes):
  G1 243 of 243 members hash to their SHA256SUMS line; G2 241 of 241 members equal `git show 36dfa80058:<path>` (the two
  not compared are the generated bindings and the census, which the builder pins by its own sha); G3 98 of 98 `.py`
  members compile; G4 the route table and the installed boundary agree (2 operation constants, 0 unserved); G5 the
  census above. **PASS.**
- Suites at the pin, in a clean worktree: `ycharts/generate/tests` 314 passed, 30 skipped; `ycharts/session/tests` 100
  passed; `ycharts/extract/tests` 33 passed; `reports/tests/test_resident_installed.py` with the resident suite, 50
  passed, 8 skipped. Run ALONE that file reads 10 passed, 1 failed: the factory test cannot import `extract` because the
  file's own path setup omits `ycharts/extract` (the defect this seat repaired in two generate files; this file is
  `2.0.0_SA_COO~P`'s). The host's factory check sets that path, as st5's did.

## 3. The capture library moves with the package, and why

`reports/resident_installed.py:97-104` refuses `PINNED_FILE_DIFFERS:library` unless the host's
`/opt/investor-reporting-ycharts/ycharts_session.js` hashes to the bindings' pin, and `HostCapture.capture` re-checks it at
every capture. Measured on the host at 05:30:54Z (SSM `abea939c-be7b-48d9-bae8-9a350b4f16b2`): the host library is
`dfc87d83..` (the fe64236bbb blob); the wrapper is `55ddb8f7..`, equal to the pin's. At 36dfa80058 the library is
`0fec0ca9..`. A whole tree at the pin therefore pins a library the host does not have, and every capture would refuse.

So the script installs the package's own `ycharts-host/ycharts_session.js` over the host file, after `node --check`
passes on it and with the old file kept beside it. The one commit between the two versions is 4467f36184 (IB-yr-292):
`contextOptions()` adds a HAR recording ONLY when `YC_RECORD_HAR=1` and `YC_RECORD_HAR_PATH` are both set, and throws
if the first is set without the second. Neither is set on the host (`secret-ids.env` is the only env file, 0 timers), so
the default path builds the same context as before. Proven offline at IB-yr-292's drain (five arms,
`check_292_suite_control.js`). **Not proven live:** no capture has run on this library.

Rejected alternative: pin the library at the host's bytes. It would keep the failing hop's code unchanged for the
diagnostic, but it would make the package something other than the tree at the pin, and it would leave the HAR
recording (W27 packet condition 8) one more install away when the diagnostic job needs it.

## 4. Blast radius, by branch (the producer's own rules, read at the pin)

Writers of an Analysis job's state: the resident, one process. Inside it two code paths write a terminal state: the
generation worker (unchanged) and `_end_permanently_refused` (new, `resident_worker.py`), both through the same
fenced store under a claimed lease.

| case | BEFORE (st5) | AFTER (st6) |
|---|---|---|
| actor allowed, Overview | runs | runs; the READY receipt also carries `vendor_requests` (ten-key shapes, no values) |
| actor's profile row is gone (`ACTOR_NOT_FOUND`) | raised, retried at each redelivery, dead-lettered at the fifth receive | job ends ATTENTION `{"code": "ACTOR_NOT_FOUND"}`, one `IRPT_RESIDENT_ATTENTION` line, message deleted; a job already READY or ATTENTION keeps its state |
| actor's row carries `allowedFirmIds` that does not name the job's firm | **ran** (row S244: the limit was enforced nowhere) | job ends ATTENTION `{"code": "ACTOR_FIRM_NOT_ALLOWED"}`; no vendor call |
| actor's row carries no `allowedFirmIds`, or `ALL` | runs | runs (the helper returns None for both) |
| any other refusal (`ACTOR_INACTIVE`, firm or locator mismatch, created after acceptance, scope) | raised and retried | unchanged: raised and retried |
| Comparison whose PDF omits a chosen name | refused before the PDF is retained | the same, and also refused at publication of a retained PDF (`COMPARISON_NOT_PRINTED`) |
| Overview (no comparison) at publication | certifies | certifies; an empty comparison list asks nothing |
| a capture | runs on library `dfc87d83` | runs on library `0fec0ca9`; no HAR unless both env vars are set |

Population the two authority rows apply to, measured 05:5xZ: `opal-users-v2` scan, 81 items, 52 PROFILE rows; exactly
1 carries `allowedFirmIds` (`svc-irpt-analysis`, `cottonwood`); the other 51 keep today's behaviour. Jobs that will
take the `ACTOR_NOT_FOUND` branch at the redrive (section 5): the two in the dead-letter queue.

Every puller of what moves: the tar key is read by the install script and by nothing else; the unit is the only
consumer of `irpt-generation` (0 event-source mappings on the queue, read by `4.0.0_SA_CRO~X` at 04:5xZ); the host
library is read by the capture wrapper, which only this unit's `HostCapture` runs (0 timers).

## 5. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. Before-read on the host: running root `fe64236bbb-st5`, active; queue 0/0 (read 05:1xZ: 0 visible, 0 in flight).
3. The install script is fetched on the host by its S3 version, its sha256 checked there, then run through Systems
   Manager. It refuses on a non-empty queue (twice: before the library swap and before the stop), a tar or member that
   is not the built bytes, a library that does not parse, or a failed factory; each refusal restores what it moved.
   After the install it rolls back to st5, library and receipt included, on a non-zero install, an inactive unit, no
   poll in 30 s, or a Traceback.
4. V1 read-back on the host: the running `current_authority.py` digest equals `211e1c15af68bdb4..` and names
   `allowedFirmIds`; the running worker names `PERMANENT_AUTHORITY_REFUSALS`; the host library equals `0fec0ca9..`.
   This is row S244's disarm.
5. R1, the two dead-lettered messages, one at a time. Before each: read the job's recorded principal and whether its
   profile row exists, and write down which branch it will take. Then move that ONE message back to
   `irpt-generation` and read the jobs row and the journal.
   - `REQ-86f1ce7062356bc5c109ce12`: its actor is the deleted window principal (journal: four `ACTOR_NOT_FOUND`
     refusals). Expected: ATTENTION `ACTOR_NOT_FOUND`, one journal line, message deleted, no vendor call.
   - `REQ-3a1b73a8dead02a17a09043b` (2026-09-27): **redriven only if its actor's profile row is absent.** If the row
     exists the job would RESUME against the vendor (it is parked at a claimed session refresh), which is an Analysis
     attempt nobody asked for; in that case the message stays in the dead-letter queue and the question comes back to
     the CTO.
6. The ledger closes at R1, never at the install.

Not part of this act: any vendor call by this seat. The first capture on the new library is the hop-7 diagnostic job
(batch 61 item 5), which waits on (a), (b) and this move, and has its own ledger leg.

## 6. Rollback, per key

- The root: `fe64236bbb-st5` stays on the host. `systemctl stop`, restore the library and the receipt, then
  `install-resident.sh` on the st5 root (the script's own rollback branch, runnable by hand).
- The library: `/opt/investor-reporting-ycharts/ycharts_session.js.before-36dfa80058-st6` is the old file; restoring it
  is one `install`. The st5 root's bindings pin that file, so the two always move back together.
- The receipt: `cutover_receipt.fe64236bbb-st5.json`, copied before the write.
- A job ended ATTENTION by the new branch is terminal by design and is not un-ended by a rollback; the two redriven
  jobs are already unrunnable (their actor is gone).

## 7. Not claimed

- That a capture authenticates on the new library (no capture has run on it).
- That the hop-7 failure is repaired: nothing here addresses why the last three jobs died at the session.
- That the API half of the service-principal boundary holds: V1 of IB-pr-275 holds on 1 of 3 functions
  (`V1_SERVICE_BOUNDARY_20261001.md`). This move closes the RESIDENT half of row S244 only.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-01 ~05:5xZ, on this packet's bytes at the commit that carries it. The write set is one new root
directory on one host, one host file with its backup, the cutover receipt with its backup, and the unit's ExecStart.
The blast radius is section 4, each branch read from `resident_worker.py`, `current_authority.py` and
`publication.py` at 36dfa80058; the rollback is section 6.

## CTO half -- 1.0.0_SA_CTO

(owed)
