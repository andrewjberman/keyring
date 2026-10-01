# Never-widen sign-off packet 2 -- the service-principal boundary on FOUR functions, coherent with their bundles (IRPT_BCKEND IB-pr-275 part 2; rows S238, S244)

Author `2.0.0_SA_COO~P`, 2026-10-01 ~06:0xZ. Ledger `irpt-service-principal-boundary-served-20261001` (OPEN; G1, G3, F1, F3, F4
closed @07cbc7684b; this packet uses G2, G4, F2, F5 and re-moves the artifacts of F1 and F4; V1 stays the closing leg). Halves owed:
`1.0.0_SA_CTO` and `2.0.0_SA_COO~P` (signed below). `2.0.0_SA_COO~M`'s holdings route aggregates ride this packet under their own
CTO halves @d43c3b0a2a and, for ADDENDUM 1, @21eca74f40. Packet pin: commit `21eca74f40` (the import closure of all four functions
reads EQUAL at it; three artifacts were built with their rows at `f9a00f732c`, whose closure bytes are the same). No CRO half: no
page text changes.

## 0. Why a second packet

Ordered by CTO rulings batch 61 items 2d and 3 (@8dcf5bbe7a), batch 62 items 4-6 (@3b5f4863ce), batch 63 item 4 (@f48603ed68).

- V1 of packet 1 (`2.0.0_SA_COO~Y`, `IRPT_MVP_Y/V1_SERVICE_BOUNDARY_20261001.md` @f95db2da7b) held on 1 of 3 functions:
  `irpt-performance-adapter` and `irpt-ycharts-generate` bundle a `canonical_profile_reads.py` from before IB-yr-293 (sha256
  `3e5868cf2fc0`, 0 mentions of `allowedFirmIds`), so the service row read as unrestricted. Packet 1 counted the reader present and did
  not read its vintage. No regression: both admitted the foreign firm before and after.
- Three candidates were withdrawn from packet 1 (7823ef7e31): `served.py` passed keywords the older bundled `enforce.py` and
  `errors.py` did not accept.

What is different this time, each as an instrument and not a sentence:

- **Import-closure table** (`IRPT_MVP_P/served_import_closure.py`, batch 62 item 6): section 3.
- **Interface gate** (`IRPT_MVP_P/sibling_interface_check.py`): section 4, with its negative and positive controls.
- **Validation before upload**: each bundle was assembled locally from its source-map row, gated and rehearsed, and the uploaded zip
  was then compared with that assembly: 0 differing members, 4 of 4.
- `irpt-ycharts-generate` and `irpt-status` are NOT here: they move as whole bundles under `2.0.0_SA_COO~Y`'s packet (batch 61 2b).

## 1. The act, in this order

1. `safe-apply` targeted to `aws_iam_role_policy.irpt_directory_service_profile_read` (root `investor-reporting/directory`) and
   `aws_iam_role_policy.holdings_service_profile_read` (root `investor-reporting/holdings`); each 1 to add, 0 to change, 0 to destroy.
   The performance and export roles hold the grant since 05:12Z and 05:14Z.
2. Simulate on both roles: `dynamodb:Query` (email-index), `dynamodb:GetItem` (table), `kms:Decrypt` with both context entries; one
   resource per call; `irpt-ycharts-generate-role` positive control and `irpt-narrative-role` negative control in their own calls.
3. Four targeted `safe-apply` runs, one function at a time, each `0 to add, 1 to change, 0 to destroy` on `aws_lambda_function.this`:

| function (module) | BEFORE = live CodeSha256 / S3 version in state | AFTER sha256 / S3 version | members live -> new |
|---|---|---|---|
| `irpt-performance-adapter` (`module.irpt_performance_adapter`) | `XslOsVc9AreOFwsgzC4frrDu4/m6ItTGeqoQRn8lN7M=` / `iDmIiCgnyXWB88FsyKGz8tdo8yvldIUA` | `PCcoNYrBQ7Cb7ma0A01SRVRQ3l5t5gr5Jqv8ihH2LR0=` / `v9P9cM48YRbGrRdruzPCmVkKgVrFRMbW` | 70 -> 70; changed 5; added 0; removed 0 |
| `irpt-export-render` (`module.irpt_export_render`) | `WO5gDeP/fZ4jPl75NQ66BCR+9ixoRJVneIGsoBSxd6I=` / `9HpHNNQ_Ke98o3_MycbUdkMfBLDIDJus` | `BIYEQ3PKsFq6qni9rm+ym+t9FRru/Pmlwyzw4/X0B7I=` / `6boiI8tkz.DWBdrBY6VYx.NYRE8arRwr` | 61 -> 61; changed 2; added 0; removed 0 |
| `irpt-directory-search` (`module.irpt_directory_search`) | `s0riHZ9hzTIypb/Ax+qEAtTstxH6xHE+iq1gEQXSKE4=` / `2RmObc9v0Wj4o3f_2PLOrYWgAWzu8mEh` | `AVSIaHEhm+E7UnDGt+PZGRJlMIbIV22e3h9sen2AyXo=` / `Uk52k9Sk88nX0MbBHsSIMJDSvSOpRUnA` | 20 -> 22; changed 7; added 2; removed 0 |
| `irpt-holdings` (`module.irpt_holdings`) | `U4/P5Bh3sfthi2QvZnYpqf4DbK4ffJskdhWgqgcMV8s=` / `vN9FiyknGePr9_jjYB3r0rr7cbG11awK` | `TG8b/SEHCf7HpxJ+haFXsIp9/6ilbACDbP/2VpgzJtU=` / `Z3Fo9JugDyQ49h7o6F_CTSgykQaBbw3A` | 33 -> 35; changed 17; added 2; removed 0 |

Full plans of the four roots after the uploads (05:58Z; holdings again at 06:06Z after its rebuild): performance `0 to add, 1 to
change, 0 to destroy`; export `0, 1, 0`; directory `1, 1, 0`; holdings `1, 1, 0`. Nothing else is pending in any of them. Builds:
`build-and-upload.sh` from a private worktree at 0eef7da885 (three functions, source map @88317195ba) and at 9e41c114aa (holdings,
rebuilt 06:04Z, source map @fb4e852bf1, merged fbfeed7d79); `BAU_PARITY_SKIP=1` on the adapter only (its three local build tools).

## 2. What moves, member by member (census of each new artifact against the LIVE zip from Lambda; downloaded bytes hash to the live CodeSha256, 4 of 4)

- **adapter (5 changed)**: `served.py` (item 4 below); `canonical_profile_reads.py` (b905df2c60 -> the IB-yr-293 reader: the projection
  and the returned fields gain `allowedFirmIds`, two lines); `loaders.py` (one generated-header comment line); `routetable.py` (a
  `sys.path` cleanup the route census uses; a zip never loads it, `operation_of` guards the import); `maintained_sources.py`
  (`2.0.0_SA_COO~M`'s comparison-policy consumer v2, the vintage the other bundles already carry). The other 65 members are untouched:
  the adapter does not go to CLOUD HEAD before the Inflection date basis is ruled (batch 63 item 4).
- **export-render (2 changed)**: `served.py`, `loaders.py` (the same comment line).
- **directory-search (whole bundle; 7 changed, 2 added)**: `served.py` (9 commits since 9cf6a63d6f: the warm hold, the exception MRO
  walk, the log line that prints the answer's code, the render ports, the path ids of C-S219, the export B1 flow, pr-271 and its
  amendment, item 4); `enforce.py` (2 commits: C-S219 path ids, an OPAL_GLOBAL user in the export path); `errors.py` (1 commit: the
  `admitted` log filter); `prospect.py` and `owner_reads.py` (1 commit, 4ec461a2e9: the Opal viewer through retained reads);
  `loaders.py` and `firm_registry.json` (generated registry text); added `canonical_profile_reads.py`, `maintained_sources.py`.
- **holdings (whole bundle; 17 changed, 2 added)**: `snapshot.py`, `STAGE_MANIFEST.json`, `BUILD_MANIFEST.json`,
  `contracts/HoldingsSnapshot.schema.json` (`2.0.0_SA_COO~M`'s route aggregates: `snapshot.py` is the blob at its signed ADDENDUM 1
  pin 30b141e19e, sha256 `270b57c40814...`, and the contract is the blob at cc99dea562; half request and addendum in
  `IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_ROUTE_AGGREGATES_20261001.md`, CTO halves @d43c3b0a2a and @21eca74f40); `served.py`, `enforce.py`, `errors.py`,
  `loaders.py` as for directory-search; `handler.py` (the directory handler the bundle carries: two UIR-07 ranking commits);
  `firm_registry.json`, `lib/opal_naming.py` (4 commits: generated view targets, a VENDOR row without a display name is a WARN),
  `org/standards/NAMING_SCHEMA.json` (the cadence token `5min`), and five registry files (`systems`, `scopes`, `exemptions`,
  `remediations`, `reporting_policies`); added the two reader files. The CTO's condition on ADDENDUM 1 holds: `errors.py` in this
  bundle is CLOUD's at the same commit (section 3). A first holdings build at 05:54Z carried the earlier pin 4e2feb5a32; it was
  superseded by the 06:04Z rebuild and never applied.

## 3. The import-closure table (batch 62 item 6): every bundled module `served.py` imports, directly or through a sibling, beside CLOUD at the pin

Read from the UPLOADED zips (`served_import_closure.py <tree> <fn> --zip <artifact>`), and again from the source-map rows at ref
21eca74f40. Verdict EQUAL = the bundled
bytes are CLOUD's bytes at the pin.

| function | closure members | not EQUAL to CLOUD | not EQUAL before the re-pin (6dbec1b0bd^) |
|---|---|---|---|
| irpt-performance-adapter | 17 | 0 | 5: served, canonical_profile_reads, loaders, routetable, maintained_sources |
| irpt-export-render | 16 | 0 | 2: served, loaders |
| irpt-directory-search | 14 | 0 | 6 of 9: served, enforce, errors, loaders, owner_reads, prospect |
| irpt-holdings | 15 | 0 | 4 of 9: served, enforce, errors, loaders |

Shared closure hashes in all four: `served.py` 455cd77ea46e, `canonical_profile_reads.py` 0ec4a717f2aa (2 mentions of
`allowedFirmIds`), `enforce.py` 4245b5f8aded, `errors.py` b60f25ccaa70, `loaders.py` 763f0a0d4445, `maintained_sources.py`
774eca9bde60, `owner_reads.py` f21d26dcce7c, `prospect.py` f556b0997dfa, `resolve.py` 24b407fa00ff.

Names the closure imports that are neither bundled nor standard library, each read at its import site (all inside a function, none
at module level): `boto3` (the runtime); `routetable` (`served.operation_of`, guarded by `except ImportError`); `opal_naming`
(`maintained_sources._comparison_firms`, the comparison policy, not on these functions' paths; the adapter's own `installed.py`
resolves its packaged copy); and, in directory-search and holdings only, `interactive_access` and `grant` (`served.py` owner-read,
prospect and render-port paths: neither entry declares `owner_read_modes`, `prospect_modes` or render ports, so the three functions
that import them are not reached).

## 4. The interface gate, with its controls

`sibling_interface_check.py <zip>`: every call a bundled module makes into a bundled sibling, checked against the sibling's bundled
definition (keywords, positional count, constructors).

- Negative control, the three candidates withdrawn from packet 1: findings 3, 2, 2 (`errors.public_line admitted=`,
  `enforce.Request path_ids=`, and for directory-search `prospect.guard_prospect resolve_owner= / authorize_owner=`, a third
  mismatch nobody had seen).
- Positive control, the three artifacts applied under packet 1: findings 0, 0, 0.
- This packet's four uploaded zips: findings 0, 0, 0, 0, over 108, 107, 96 and 99 cross-module calls checked in 17, 16, 14 and 15
  reachable modules.
- It is a floor: calls on objects and inherited constructors are not resolved. Section 6's invokes cover the path.

## 5. Blast radius, by branch

**The service boundary (`served.py` @f9a00f732c lines 920-953 and 996-1001), all four functions.** A human subject never enters it.

| SERVICE subject | adapter BEFORE | export BEFORE | directory, holdings BEFORE | AFTER, all four |
|---|---|---|---|---|
| selects a firm in its `allowedFirmIds` | served | served | served | served |
| selects a firm outside it | SERVED (stale reader) | refused | SERVED (no check in the bundle) | refused `FIRM_BINDING` |
| row's value is `ALL` | served | served | served | served |
| row carries NO `allowedFirmIds` attribute | served | served | served | refused `FIRM_BINDING` on every firm (batch 62 item 4) |
| no profile row, or the read raises | served (adapter: refused since 05:21Z) | refused | served | refused `FIRM_BINDING` (fail closed) |

Population: 1 service principal of 52 `PROFILE` rows (`svc-irpt-analysis@opalinvest.com`, `allowedFirmIds cottonwood`), measured in
packet 1. Its row carries the attribute, so item 4 changes no principal's behaviour today. After the move it is served for
cottonwood and refused for every other firm on all four functions. The grants go first because the directory and holdings roles
cannot read the profile table today: code first would refuse `svc-irpt-analysis` on cottonwood too.

**The catch-up on directory-search and holdings (humans ARE on these paths).** Behaviour that changes with the older `served.py`,
`enforce.py`, `errors.py`:

| change | effect |
|---|---|
| exception MRO walk (7a8d2a4ca3) | a subclass of a declared refusal class answers its declared code instead of `UNEXPECTED` |
| public log line (4fffe13f01) | the log prints the code the answer carries; log only |
| `SELECTION_UNSUPPORTED`, the `NO_DATA` sentinel | new answers a compute may return; in both bundles no module other than `served.py` and `errors.py` names either (read on the assembled bundles) |
| render ports, path ids (fe854ce6f1, bd52efb246, 755c13bc19) | reached only by a RENDER_DELEGATE subject or with render ports installed; neither entry installs them |
| warm hold (9cf6a63d6f; holdings only, directory-search already runs it) | a warm event may hold its container up to 2 s when the event carries `irpt_warm_hold_ms` |
| `prospect.py`, `owner_reads.py` (4ec461a2e9; directory only) | prospect and owner-read paths; the directory entry declares neither mode |

**Holdings, beyond the boundary:** the route serves per-security aggregates and per-class totals over actual positions
(`2.0.0_SA_COO~M`'s act; its blast radius and after-read are in its half request @9a3eef4cb1 and stay its). The registry and naming
members change what `opal_naming` can resolve (new scope and system rows, generated views); the holdings route's own addresses are
read by the enforcer-reaching invoke of section 6 and by `2.0.0_SA_COO~M`'s after-read.

Writers of each function's code pointer: 1 (its module). Writers of each role's inline policies: 1 (its root). Writers of the
selected-firm decision for a SERVICE subject: 1 (`served.py`).

**Every puller:** live plane at 04:5xZ, 224 functions listed, each BEFORE artifact run by exactly one function; the four keys are
named by no second Terraform module (packet 1 section 2, same instrument, plus `irpt-directory-search` and `irpt-holdings` in the same
list). `irpt-directory-refresh` and `irpt-holdings-refresh-lambda` have their own artifacts and do not move.

## 6. Conditions

1. Order as section 1; a simulate that is not allowed x3 on either role stops the act before any code moves.
2. Per function, on the BEFORE code and again on the AFTER code: one `lambda invoke` with empty headers (expects the
   `CONTRACT_VERSION` refusal) and one with trusted headers for cottonwood and a NON-EXISTENT user naming an operation the function
   serves (`performance-report`, `export-receipt`, `directory-search`, `holdings-snapshot`; expects a refusal raised after
   enforcement). No `FunctionError`, no `errorMessage`. BEFORE equal to AFTER on the adapter and export-render; on directory-search
   and holdings the AFTER answer is the enforcer's refusal and the BEFORE answer is recorded beside it, whatever it is. The local
   rehearsal on these bytes constructed `enforce.Request` with `path_ids` for the adapter, directory-search (three operations) and
   holdings (rebuilt bundle, 06:05Z), each answering `NOT_AUTHORIZED`.
3. Post-apply CodeSha256 equals the AFTER column; a re-plan of the same target reads `No changes`.
4. Ten minutes of each function's log group after its apply: zero `TypeError`, `ImportModuleError`, `Traceback`, timeout lines.
5. A function failing 2, 3 or 4 is rolled back in the same window before the next one moves.
6. V1, re-read by `2.0.0_SA_COO~Y` as `svc-irpt-analysis`: foreign firm refused and cottonwood not refused on the adapter and
   export-render, and the directory negative control (the Inflection entry of row S238) refused. Row S238 then waits only on the
   resident's control (batch 61 item 4), which is `2.0.0_SA_COO~Y`'s.
7. `2.0.0_SA_COO~M` reads the holdings route after F5 (its half's after-read).

## 7. Rollback, per key

A function: `s3api copy-object` of its BEFORE S3 version (section 1 table; each one's metadata `content-sha256` is its BEFORE
CodeSha256) over the same key, then the same targeted `safe-apply`. A grant stays: add-only, unused by the BEFORE code.

## COO half -- 2.0.0_SA_COO~P

SIGNED, 2026-10-01 ~06:0xZ, on this packet's bytes at the commit that carries it. Write set: two inline policies and four functions'
code pointers. I read the closure members' bytes, not their presence.

## CTO half

(owed: `1.0.0_SA_CTO`, bound to this packet's pre-signature blob)
