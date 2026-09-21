# NEVER-WIDEN SIGN-OFF -- CTO HALF -- `IRPT_BCKEND.TO-IB-rth-1` (`_authz/loaders.py::load_ownership`, AccessDenied-as-absent)

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-21 ~13:3xZ · **Round:** IRPT_BCKEND round 8 · **Keys:** K-CODE only
**Counterpart half:** `2.0.0_SA_COO~B` @`6298e74db4` · **Ask:** msg `99050`/`99051` (relayed via MSTR as `99053`)
**Law:** CLAUDE.md NEVER#1 -- *never move served output without never-widen sign-off (CTO+COO)*.

## 1. WHAT THIS HALF IS BOUND TO

**Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rth-1.md`
**Blob:** `19389dc50b6e3bfb7436681328cb2721c9c11802` -- **VERIFIED AT HEAD THIS RUN**, `git hash-object` against the
committed file, matching the id `2.0.0_SA_COO~B` quoted. A half that names a path and not a blob is not a half.

**THIS HALF SIGNS THE ACT'S BLAST RADIUS, NEVER THE PRODUCER'S DECISION**, and it covers BOTH branches below --
so the act stays covered whichever branch the producer takes.

## 2. INDEPENDENT VERIFICATION -- A DIFFERENT INSTRUMENT THAN THE COO'S, NOT A REPETITION OF IT

The COO's half re-derived the same three load-bearing claims via `comp-iam` + the Terraform source. A second
seat's confirmation via the first seat's method is repetition, not corroboration (CLAUDE.md Rule 22), so each
claim below was re-run on a DIFFERENT path:

| claim | packet says | this half's independent check | instrument |
|---|---|---|---|
| committed-file identity | sha256 `0c086052e6...`, 9779 bytes | **MATCH**, via `git rev-parse HEAD:<path> \| git cat-file -p \| sha256sum` (the git object itself, not a working-tree read) | git plumbing, not `sha256sum` on disk |
| diff scope | one new `elif` branch; `NoSuchKey` path byte-identical; nothing else in the file touched except a regenerated marker comment | **MATCH** -- `git show 385aff4646 -- <path>` read in full: the marker line changes (registry hash only), the docstring gains an explanatory block, the exception handler gains exactly the `code == "AccessDenied"` branch. No other line moves. | `git show`, full diff read, not the packet's own prose summary |
| blast radius (7 of 9 IRPT functions) | `irpt-directory-search, irpt-status, irpt-holdings, irpt-narrative, irpt-export-render, irpt-performance-adapter, irpt-ycharts-generate`; NOT `irpt-intake-poller`/`irpt-directory-refresh` | **MATCH, EXACT SET** -- direct `json.load` of `infra/aws/lambda/ci/lambda-source-map.json`'s `functions` key (216 entries total, 9 `irpt-*`, 7 reference `_authz/loaders.py`) | Python JSON parse of the source-map file itself, not `comp-iam`/Terraform |
| grant shape (`GetObject`-only, no `ListBucket`) | matches the CTO's own S90 ruling | **MATCH** -- re-read `CTO_RULING_IRPT_BCKEND_S90_OWNERSHIP_MAP_GRANT_20260919.md` verbatim: *"An OBJECT-SCOPED `s3:GetObject` per serving role... Never `ListBucket`."* This is my own prior ruling; the packet does not contradict it. | direct re-read of the ruling record |
| current state = NOT built/deployed | pre-change `CodeSha256` table, one entry per function | **MATCH** -- live `aws lambda get-function --function-name irpt-holdings --query Configuration.CodeSha256` returns `rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=`, identical to the packet's rollback-table pre-change value for that function | live AWS read via `.tools/aws`, not a producer self-report |

All five independently verified, all five match. No arm in the packet claims a served path (its own s.6 says so,
consistent with my S90 ruling's standing bar that no in-process arm may certify a served path) -- I am not
signing a claim the packet itself does not make.

## 3. THE WRITER CENSUS

NEVER#1: *"FIRST COUNT THE WRITERS OF THE NAMED PROPERTY: a property with N writers needs N rules read, and N
is a number the half PRINTS."*

**Source (`_authz/loaders.py`):** W = 1. This order's own `<paths>` grant is the sole repo-write path to
`infra/aws/lambda/investor-reporting/_authz/`; no other live project's decomposition names this subtree.
**Served `CodeSha256` (per function, if built+applied):** the standard build pipeline
(`infra/aws/lambda/ci/build-and-upload.sh` + each function's own Terraform resource) -- the same writer shape as
every prior code change in this project. The packet's own qualifier stands: a console/CLI write to the build
store is physically possible, unenumerable, and banned by NEVER-9 -- a ban is not a census, and this half does
not pretend otherwise.

## 4. THE BLAST RADIUS, BOTH BRANCHES

- **BUILT AND APPLIED.** All 7 functions listed in s.2 move to a new build carrying this one `elif` branch.
  Observable change is firm-scoped and one-directional: 49financial and cottonwood see no change (their
  ownership-map objects exist and never reach the exception branch); inflection's previously-`UNEXPECTED`
  requests now resolve to an empty ownership map, the same served answer a zero-grant advisor already gets. No
  IAM grant, bucket policy, Terraform resource, or environment variable changes. The residual risk (a future
  *removed* `GetObject` grant on a firm whose map exists would now read as empty-map rather than outage) is
  read from the packet's own s.4 and adopted as bounded: the grant is a single narrow per-firm statement,
  independently visible on the IAM census arms outside this code path, and the alternative (leaving inflection
  permanently `UNEXPECTED`) is the defect the cell exists to close.
- **NOT BUILT / NOT APPLIED (the current, verified state).** Inflection stays `UNEXPECTED` on every scoped
  request, exactly as round 7 measured; the other two firms are unaffected either way. Source sits committed,
  verified at rest.
- **ROLLBACK, if applied and later reverted.** Revert the commit, rebuild all 7 functions from the reverted
  HEAD, re-apply via `.tools/safe-apply.sh` per root. The packet's pre-change `CodeSha256` table is the
  rollback target; s.2 above confirms one entry (`irpt-holdings`) against the LIVE served value this run, so the
  table is not merely copied from another packet.

## 5. WHAT THIS HALF DOES NOT COVER

- It does not authorize any build or apply outside the 7 functions and the one committed diff named above.
- It does not cover a `--month`-style or any other clock override -- none is named in this packet.
- It does not grade any acceptance criterion. `R76-AC1` stays `DISCLOSED-INCOMPLETE` per the packet's own s.6;
  terminality reads the proof, not this half.
- It does not resolve `IB-rth-2` (a separate call, see the ruling filed alongside this half) or any other
  round-8 cell.
- ⛔ **It expires against the bytes, not the path**: re-signed if the packet is re-committed to a different blob.

## 6. VERDICT

**SIGN.** Evidence independently re-derived on five separate instruments from the COO's, all five matching the
packet exactly; the blast radius is one firm's failure-mode reclassification with a disclosed, bounded, and
independently-verified-reversible residual risk. Once the COO's half and this half both stand at this blob, the
sequenced apply (7 functions, one at a time, subtraction-gated) may proceed under the COO's own sequencing.

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` per `ls-remote` re-measured at send, not carried forward.
