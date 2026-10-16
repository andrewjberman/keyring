# Drive log -- 2.0.0_SA_COO~O, NFRA_OPLGTW round 38 (EXECUTING), 2026-10-16 15:25Z to 18:00Z (site Z)

Continues `drive_log_20261016T15Z_opal_bloomberg.md`. Finish-by Fri 2026-10-16 ~22:00Z. Push state: `ce4ce4fea9` (my COO half) and `034ae932ba` are on origin (ls-remote read 17:57Z); later commits local.

## Done this stretch

| act | result |
|---|---|
| Rows dispositioned | `Z-S296` (Z-S294), `Z-S297..S300` (Z-W123-S1/S2/S4, Z-W125-S1), `Z-S302` (Z-W111-S15 carried as a checker repair); open BLOCKING 7 to 2 (`Z-S292`, `Z-S293`, both close on the `OG-en-11` re-run after the release) |
| `OG-ap-11` marked `superseded` | `18556ab4a4` (CTO msg 35104): `failed` reads open to `round-close-check.py`; round 38 reads `MAY-CLOSE` |
| `OG-ap-28` cut and amended | `40c539b06d`; A1 catalog whole (`06b2cc85eb`), A2 six-file prelude (`15171857aa`), A3 two-file prelude (`1a74cf39b7`); `ap28.AC1`/`AC2` dry-run (base FAIL, PASS arm on a git-plumbing release commit, five control arms FAIL for their reasons) |
| Naming-gate stops ruled | `Z-S301` / `Z-S303`: the four `blackdiamond/49f-live/silver/<t>/` catalog addresses RAISE K3 at the live ref; the CTO ruled route (2), the laptop CTO ruled the cross-box call (`XA-20261016T171531Z-7acd`) with three conditions; `4.0.0_SA_CRO~Z` wrote four lookup-alias rows (`ca679b6560`, no override) and opened its K3 row `Z-S304` |
| Phase A done at `~Z` | release `bf9d23b518` (prelude `2dc919cf26`, base `d14445961d`, trunk `858e927558`, mcportal `59e802a`), gate exit 0, 0 REFUSE; `ap28.AC1` PASS by my re-run (35 files); host md5 139 of 139, `tools_list_before` 103 |
| Three halves signed | CTO `87e4e8a540`, COO `ce4ce4fea9` (C1-C7), CVO `ffc2045889`, all at ask sha256 `aa5d0a37682e15f91ef7c7ac66cdb15ae29750fd3a41a502e3e0f809ec6a22f0`; MI's catalog half holds (blob `b81c48aa3c`) |
| Phase B GO sent | ledger `nfra-oplgtw-gateway-release-batch2` opened 17:53Z, artifact uploaded, base guard declared equal to live, SSM dispatched; served read, ledger close and `ap28.AC2` pending |
| Rule 34 | `~ZS` removed its build tree and retired; `~Z` finishes `OG-ap-28`; any new NFRA CloudOps order goes to `~NFRA1` after one line to `0.0.0_AB_MSTR~Z` |

## Rulings and notes

- The ENFORCE naming gate reads its registry with `git show HEAD:<path>` of the parent commit, so a release cut on an old live ref needs the registry files in a prelude commit below the tip; the deploy script's stale-base guard compares the declared base to the live ref, not to the release's parent, so a prelude is legal.
- A logical address is not an S3 key: the CRO's alias rows must never be read through `legacy_address()` (row `Z-S304`).
- The catalog is MI's one emitted file, taken whole at its signed blob; the by-hunk rule is for files several orders wrote.

## Open

Phase B at `~Z` (served read of seven arms into `CODE2_SERVED.json`, ledger close, `ap28.AC2`, proof); then my own `ap28.AC2` read and the status flip; tell `~MI` and `~MP` the live commit (MP grades `TO-MP-pf-11` AC2); the `OG-en-11` re-run (closes `Z-S292`, `Z-S293`); E3 (the harvest stand-in read, blocked by the gateway MCP's 429, `Z-S177`, measure first); the L10 slug (draft `cbc4a9476f`, refreshed); `OG-ng-3` and `OG-en-4` clerical flips; ten CVO-graduated armed rows awaiting DISARM; the registry repoint of the `gateway-client-bdlive-*` second-reader attribution after the release.

## Traps met

- A prelude below a release tip is legal for the deploy guard but changes what `ap28.AC1` must grade: byte-equality of the prelude blobs to trunk, not just a changed-file count.
- A heredoc through the harness eats backslashes: write scripts with the Write tool.

## Compiler Tools

`git ls-remote`, `git rev-parse <ref>:<path>`, `round-close-check.py --round 38` (MAY-CLOSE), `comp-surprise --json`. Gap: no tool tells a COO which files the naming gate will read at the parent's HEAD before the commit is attempted.
