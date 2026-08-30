# 0.8.0_AE_CloudComp~Y -- P2-1-AE deployed and CLOSED, and a timestamp trap that inverted a conclusion

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

Window 0827Z-0940Z 2026-08-30. Delta since `session_0320-0827Z`. One task order executed end
to end and closed at the grader: `ADVI_BDPARITY.P2-1-AE`, PA-1..PA-4.

## Objective

Apply `0.6.0_DS_Reporting~C`'s per-feed selector to the DEPLOYED BD reporting puller
(`opal-assets-bd49f-reporting-pull`) under the AE lane, plan it as a code-only change, apply it,
and verify the selector in the RUNNING bytes -- with no vendor call at any point (a live pull is
P2-2 and is gated on Andrew's per-use word).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `.tools/commit-gate.sh` | on the patched `lambda_function.py` | PASS 1/1 | py_compile + ds-precommit + ruff py39 |
| `infra/aws/lambda/ci/build-and-upload.sh` | canonical build + S3 upload | PASS | write VERIFIED: size 33,902, sha256 metadata match |
| `terraform plan -target` | saved plan file | PASS | 0 add / 1 change / 0 destroy, asserted from plan JSON not prose |
| `.tools/safe-apply.sh` | on the SAVED plan file | PASS | HALT-gate fired FIRST and blocked; `HALT_ACK=1` |
| `.tools/deploy_ledger.py` | open at apply, close at verify | PASS | 6 legs, all proven; sentinel removed |
| `.tools/proof-of-spec-check.py` | instance vs corrected face | VALID rc=0 | checker vintage 3948c766a7 |
| `.tools/safe-commit.sh` | 3 commits, own author line | PASS | pathspec-scoped, no pre-`git add` |

**What worked.** Applying `safe-apply.sh` to the SAVED PLAN FILE rather than re-planning: exactly
the plan the gate reviewed landed, and no drift could enter between review and apply. The
HALT-gate was not ceremony -- it surfaced five pending messages and one of them CHANGED AN ACT
(below).

**What failed.** Nothing in the deploy. Two instrument traps bit during verification and both were
caught before anything was filed (below).

**Gap found.** `record-terraform-deploy.sh` carries a live half-write candidate (CVO's ARMED item:
its commit-derivation limb silently no-ops under bun while the tool STILL COMMITS). I did not run
it. Consequence stated rather than left: the source map's `last_deployed_commit` for this function
remains `f559cbc516` and is STILL STALE after this deploy. That is the (k) carrier item's, not
this face's.

## Work Completed

### ADVI_BDPARITY.P2-1-AE -- PA-1..PA-4, all four PASS (3.0.0_SA_CVO 87173)

**PA-1, and I REFUSED the artifact the face named.** The face and the dispatch both cited sha256
`a3120670...`. The bytes on disk hashed to `ab417c45...`, so I stopped rather than applying an
artifact whose identity failed, and traced it: `d9ac9dc597` (5,002 B, `a3120670`) was SUPERSEDED
eight minutes later by `d981d2366a` (5,145 B, `ab417c45`). The declared digest pinned a superseded
revision. Tested every byte-form -- raw, CR-stripped, CRLF-ified, at both pins and in the worktree
-- before concluding. Issuer, DS~C and the gate then confirmed `ab417c45` as final and corrected
the face. Applied at `49a851ea2e`; 11 of 11 arms re-run AT THIS SEAT (not inherited), rc=0.

**PA-2.** Targeted plan, asserted from the plan JSON: the code row alone, zero env/trigger/IAM
rows, `environment` before == after, 0/1/0. The built zip's `lambda_function.py` LF sha
`c1278acb...` == the committed INDEX blob, raw CR count 0 printed beside it so an LF-normalised
digest could not hide a CRLF ship.

**PA-3.** `safe-apply.sh` on the saved plan -> `Apply complete! Resources: 0 added, 1 changed, 0
destroyed` on the one address `module.bd49f_reporting_pull.aws_lambda_function.this`.

**PA-4, read on the RUNNING artifact** (live plane, never the apply report):

```
CodeSha256    GMfBZrn/elvrVJCY... -> yO0R5JDSL86L1cp+V3qla1NsYWjvAL4lYi1drQvesIk=
LastModified  2026-08-30T02:54:33Z -> 09:14:51Z   (post-dates the apply)
CodeSize      33,102 -> 33,902
ENV           set-identical by dict equality over all 5 keys
              DRY_RUN '0'->'0'; INSURANCE_EGRESS '1'->'1'  -- neither egress switch moved
RUNNING BYTES downloaded from the RUNNING function via the presigned get-function URL --
              not S3, not the worktree: lambda_function.py 28,533 B, raw CR 0,
              LF sha c1278acb... == the committed index blob.
              Selector present in the live bytes: resolve_feeds / feeds_requested / event.get("feeds")
RE-PLAN       "No changes" AND -detailed-exitcode rc=0 (machine-readable, not prose)
```

**The proof.** `proof-of-spec-check.py <instance> "PA-1,PA-2,PA-3,PA-4"` -> 4 acceptance rows, 0
violations, VALID rc=0 against the issuer-corrected face `@be4645f6bd`. The two
`PENDING-THIS-COMMIT` rows were re-verified by `git show --stat 3f439d2e4e` rather than trusted
from my own build-time derivation -- because that arm's own frame line says it cannot see a stale
PENDING (it only checks the path EXISTS), so that check belongs to the seat.

## Two instrument traps, both caught before filing

**1. A literal `Z` in a `--time-style` format INVERTED a conclusion.** Investigating why
`infra/aws/lambda/ci/build-and-upload.sh` was dirty, I read its mtime with
`--time-style=+%Y-%m-%dT%H:%M:%SZ` and got `2026-08-30T05:30:15Z`. That renders LOCAL time and
stamps a UTC marker -- the trap CLAUDE.md Rule 22a names explicitly. Read at face value it puts
the edit at 05:30Z, **three hours BEFORE my 08:57Z build**, i.e. "I executed a dirty CI script and
my PA-2 'canonical build-and-upload' claim is compromised." The true UTC is **09:30:15Z, 33
minutes AFTER the build**. The disambiguator was a second carrier on the same output: `git log`
printed `-0400` explicitly against a commit whose UTC time I independently knew (`da9afee96d` at
09:03Z), fixing the device at UTC-4.

The point is not that the trap exists -- it is written down. The point is that **the trap's damage
here was an ORDERING inversion, not a display nuisance**, and an ordering inversion is exactly the
shape that flips a self-exonerating conclusion into a self-incriminating one and back.

Two independent lines then agreed: (a) my own PRE-BUILD `git status --porcelain infra/aws/lambda/`
returned exactly 6 lines, ALL `.pyc` deletions -- `build-and-upload.sh` was CLEAN when I executed
it; (b) the true-UTC mtimes post-date the build. The edits were `0.7.0_AE_CloudOps`'s manifest
gate, now committed at `eb0694d45b`. My source-map entry is untouched and my PA-2 claim stands.

**2. cp1252 again.** `subprocess.run(..., text=True)` decodes with the ANSI codepage and dies on
byte 0x9d at position 31,662 of `lambda-source-map.json`. Same trap I had already documented in
the PA-2 message one hour earlier, in a different call shape (`open()` there, `subprocess` here).
Loud failure, not wrong data -- the better direction, but I wrote the second occurrence anyway.

**And a third thing I checked instead of assuming:** a log file
`session_0050-0914Z_...` sits in this seat's log directory covering a window overlapping mine. It
is `0.8.0_AE_CloudComp~X`'s -- a DIFFERENT lane sharing the base seat's folder. A name in my
directory is not my artifact.

## Decisions Made

1. **Refused the face's declared digest and traced the supersession** rather than applying it or
   silently applying the newer bytes. The refusal-then-trace was graded the correct act.
2. **Did NOT run `record-terraform-deploy.sh`** -- using a tool with a live half-write defect to
   record an irreversible act is the wrong call. The face does not require it (PA-3 requires
   `safe-apply` + the NEVER#6 ledger via `deploy_ledger.py`). Consequence stated, not hidden.
3. **Did not edit the face** to fix its five carrier defects -- it is the issuer's artifact and
   the deploy was done either way. Reported on the channel; issuer corrected `@be4645f6bd`.

## Files Modified

See commit messages: `49a851ea2e` (PA-1 patch), `da9afee96d` (PA-2 source map), `3f439d2e4e`
(PA-3+PA-4 deploy, proof instance, builder, NEVER#6 ledger).

## Deployment Sequence + Verification (AE role section)

```
1  commit-gate.sh on lambda_function.py            PASS 1/1
2  safe-commit 49a851ea2e                          patch ab417c45 applied, +40/-3, CR 0 before and after
3  build-and-upload.sh                             zip 33,902 B, sha yO0R5JD..., write VERIFIED
4  safe-commit da9afee96d                          source-map artifact_sha256, 2 changed lines, 1 entry
5  terraform plan -target -out=<planfile>           0 add / 1 change / 0 destroy (asserted from JSON)
6  safe-apply.sh <planfile>                         HALT-gate: 5 pending, all read, none STOP-class -> HALT_ACK=1
                                                    tombstone-gate CLEAN (2 planned creates vs 7 tombstones)
                                                    "Apply complete! Resources: 0 added, 1 changed, 0 destroyed"
7  aws lambda get-function-configuration            CodeSha256 == the uploaded zip; LastModified 09:14:51Z
8  presigned get-function package download          selector present in RUNNING bytes; LF sha == index blob
9  terraform plan -detailed-exitcode                rc=0
10 deploy_ledger.py close                           6 of 6 legs proven; ledger CLOSED
```

Ledger: `org/critical_paths/change_management/20260830T0910Z_advi-bdparity-p2-1-ae-selector_deploy_completion.md`

## MCP traffic

12 handled. Significant: discharge to CVO/COO/CTO (87067-87069); gate closed the apply leg
(87038); issuer accepted the substance (87051); **grade 87173 -- PA-1..PA-4 PASS**, proof VALID on
the grader's OWN unpiped run, PA-4 discriminated on a second live read reproducing every figure I
printed; release line 87183. Acks READ: 87109, 87140, 87169, 87173, 87183.

## Blockers

None. Nothing owed by this seat on ADVI_BDPARITY.

## Current State

- `ADVI_BDPARITY.P2-1-AE` **CLOSED at the grader**, PA-1..PA-4 PASS (`3.0.0_SA_CVO` 87173). The
  seat is RELEASED from ADVI_BDPARITY (`2.0.0_SA_COO` 87183).
- The per-feed selector is **LIVE** on `opal-assets-bd49f-reporting-pull`. `feeds=None` still
  returns all three feeds -- a performance-only default would have starved `OPAL_TAXSMA_PT2`'s
  silver build. `DRY_RUN=0` and `INSURANCE_EGRESS=1` are unmoved. **P2-2 (a live vendor pull)
  waits on Andrew's word; no vendor call was made at any point in this unit.**
- CARRIED, not mine: the source map's `last_deployed_commit` for this function is stale at
  `f559cbc516` (the (k) carrier item). Owner of `build-and-upload.sh`'s new manifest gate:
  `0.7.0_AE_CloudOps` (`eb0694d45b`).
- Seat holds `NFRA_C3MATERIALIZE` for the sec-7b unit's duration (Rule 27). 0 active TOs.
- Watcher LIVE (Monitor task `b5p9udcd5`), zero crons, event-driven. All 3 commits on origin
  (`416a116c8b` at the 09:36Z window CLOSE).

## Next Steps

- [2.0.0_SA_COO~X] cuts the sec-7b `symbol_to_file` declaration unit; this seat is the base's
  allocation to it. The next unit arrives from that seat.
- [0.7.0_AE_CloudOps] owns the index-sourced manifest gate now wired into `build-and-upload.sh`.
- [0.6.0_DS_Reporting~C] owns the BUILD_MANIFEST-vs-shipped-zip discrepancy, due after P2-1 closed.

## The thing worth carrying out of this session

**A timestamp read in the wrong frame does not look wrong -- it looks like a different verdict.**
The `Z` I typed produced a well-formed, plausible, precise UTC string that said I had executed a
dirty script. Nothing about it was malformed; the only tell was that a second carrier on the same
screen (`git log`'s explicit `-0400`) disagreed once I anchored it to a commit whose true time I
already knew. Precision is not provenance. Where an ordering carries the verdict, read the clock
in a frame you did not type yourself, and anchor it to a value you independently know.
