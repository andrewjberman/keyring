# The MX-r-9 label repair: the artifact plane now names what is serving — 0.7.0_AE_CloudOps~MX

**Date:** 2026-10-10
**Task Order:** `NFRA_MCPINDEX.TO-MX-r-9` (`discover-needs-release`), `<risk>WORLD</risk>`
**Status:** COMPLETE

**archetype:** DEPLOY

## Objective

Execute acts (a) and (b) of the repair GO for row `NFRA_MCPINDEX-Z-S92`: the 2026-10-09 19:42Z release put the
right bytes on the gateway host and the wrong labels on S3, so plane 1 of the release train's STOP gate named a ref
that was not serving. Restore the signed rollback handle, re-stamp the artifacts, close the NEVER-2 ledger on two
read-backs, and report to the issuer.

The GO had never been delivered: msgs 32997 and 33003 both read `OFFER-EXHAUSTED` (SENT, never EMITTED), and the
issuer re-sent them whole as **33009** after the ~25h site-Z outage.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `--name '*MX-r-9*' --limit 20`, then `--page 2` | 38 hits / 209686 files. Page 1 was all inbox prose; the task order was on **page 2**. A one-page read would have concluded the order did not exist. |
| `comp-find` | `-i 'pptx' <gateway app> <gateway deploy> --limit 30` | 5 hits / 98 files. This is what turned a would-be "pptx absent" claim into an accurate one. |
| `comp-find` | `'index-BP6X9XJd' --limit 10` | 84 hits / 176751 files, all `.runtime` crash-investigation archives — established the 2 host-only dashboard files as a real former release, not corruption (row Z-S94). |
| `comp-find` | `--name 'proof_of_spec*.schema.json' --limit 5` | 1 hit. Revealed the DEPLOY-genre marker requirement, which changed how the instance was written. |
| `comp-which` | `"how do I grep the repo"` | Startup forwarder exercise: a forwarder RAN; 102 of 102 comp-tools resolve bare. |
| `deploy_ledger.py` | `close-leg` x4, then `close` | All 4 legs proven; "sentinel removed". |
| `surprise-row-gate.py` | at commit | `2 new row(s) of 270 total checked`; OK. |
| `proof-of-spec-check.py` | `<instance> AC1,AC2,AC3,J1,J2 --governing-order <order>` | INVALID (5 violations) → fixed → **VALID (rc=0)** with coverage checked. |

**What worked:** `comp-find`'s printed denominator and paging. The order was on page 2, and an early stop would have
read identically to a true absence. The `pptx` and `index-BP6X9XJd` sweeps each changed a claim I was about to
write.

**What failed:** nothing in the comp rail. Three denials fired (two `F4` census-into-a-receiver, one `F1`
recursive-search) and each named the command that answers; the `F1` on a two-named-file `grep -rn` was avoided by
using native `Grep` on each named file, which the rail's FREE list admits.

**Gap found:** none new. Three pre-existing instrument gaps were hit and are recorded rather than worked around:
(1) `safe-ec2-deploy.sh`'s manifest commit cannot run the commit-gate from a sparse tree (`ModuleNotFoundError:
comp_constants_cli`) — already in Z-S92's notes, reproduced, not re-filed; (2) `deploy-to-ec2.sh` has no
build-only mode, so the issuer's "would (b) move a host byte" gate had to be answered by rebuilding the artifact
independently; (3) the owned-paths hook enforces an order's `<paths>` only when `.comp-graph/.agent_context`
carries a `TO_ID`, which this session does not — an absent guard, not a grant.

## Deployment Sequence

| # | act | evidence |
|---|---|---|
| 0 | Pre-act state measured by this seat, not taken from the issuer's report | Rollback key and `-latest` both 525795 B / ETag `0eed0817`, stamped `1e32562729`; `d3c31e972e` key 404; `list-object-versions` 2 versions, 0 delete markers; host `active`, ActiveEnterTimestamp **Fri 2026-10-09 19:42:29 UTC** (no restart across the outage), `/health` 200, `.env` 52. Nothing had moved. |
| 1 | **Act (a)** 21:24:27Z — restore the signed rollback handle | `s3api copy-object` of VersionId `t6Dv5giTH_t44Ae_FlV3.LcFyQOOVPOh`, `--metadata-directive COPY`, **no delete**. Read back 518165 B, ETag `b96315a523842ec46579b146c450faa9`, git-ref `1e32562729`. Mislabelled bytes survive as VersionId `ACLA5fh9zEq7a9ydJMrmnarDnc3M6FIC`. |
| 2 | Test the issuer's STOP condition **before** the apply | 103 of 103 candidate files byte-equal to the running bytes: 100 code files from the committed tree, 3 dashboard files from a reproduced `bun install --frozen-lockfile && bun run build` at pinned `mcportal_commit d60b4e0`. Bun cache precheck 77 of 77, so nothing was fetched. |
| 3 | Remove the root cause in the deploy tree | HEAD pointed at the existing commit `d3c31e972e` after proving index blob == commit blob == on-disk content for both files (`7f45517f27`, `da94d7cc64`). `rev-parse --short HEAD` then reads `d3c31e972e`. |
| 4 | Halt gate, AMENDMENT A5 | Positive rc=0 from the deploy tree; **negative control** on a tree where this lane is not seated read rc=3 BLOCKED (`lane-no-inbox`). `HALT_OVERRIDE` not used. |
| 5 | **Act (b)** 21:49–21:50Z — one re-deploy | `safe-ec2-deploy.sh`, `DEPLOY_BASE_REF=1e32562729`; stale-base guard read the live ref equal at both reads. Deploy script was the live base's own blob `c2cfc34065`, 0 occurrences of E2's env line against 4 in `box/sitez` HEAD's copy. |
| 6 | Ledger close | All 4 legs proven, sentinel removed, entry committed CLOSED. |

## Verification

**Read-back (1)** — rollback key ETag `b96315a5...`: met, and still met after (b); untouched at LastModified
21:24:27Z and DISTINCT from the two new keys.

**Read-back (2)** — the host: both shipped files' md5 **UNCHANGED** (`34f36796d6b19eebe17d715c7ae7c041`,
`7e9e40bb185f266aa293a7d29ad67e6d`, byte-identical to the values Z-S92 recorded on 10-09); `/health` 200; `.env`
52 with **set-equality True**, 0 added, 0 removed. Measured past the two files: **105 of 105 host files
md5-UNCHANGED**, 0 appeared, 0 disappeared, 0 changed. MainPID 873208 → 915778 (the expected restart).

**The artifact plane:** `opal-gateway-d3c31e972e.tar.gz` PRESENT (was 404) at git-ref `d3c31e972e8c6f...`;
`-latest` same ref, same ETag `8e81c94230a54ef80a88d03950e93c81`. The new tarball is 3 bytes smaller — gzip
container metadata only, proven by extracting it: its 103 files are byte-equal to the superseded `-latest`'s 103.

**Criteria:** r9.AC1 PASS exit=0 (30 of 30 sentinels), r9.AC2 PASS exit=0 (3 of 3 measured as-of equal to served;
the dry-run read 0 of 3), r9.AC3 PASS exit=0 (9 of 9 and 3 of 3; the dry-run read 0 of 9 and 0 of 3). All three
match their `<expect>` verbatim. Proof instance **VALID (rc=0)**. J1/J2 carry no verdict — L9, `3.0.0_SA_CVO~Z`.

**FWD-13 is live:** discover now states a `measured` as-of equal to the served object's own vintage, where before
the release all three datasets stated a held 2026-08-10 certification date against 2026-10-07 served.

## Decisions Made

1. **Tested the byte condition before the apply rather than after.** The issuer's gate was "if (b) would move any
   host byte, STOP: that is a new act." `deploy-to-ec2.sh` builds, uploads and SSMs in one run, so a claim about
   the host after the act had to be settled before it. The dashboard bundle was the only rebuild-risk surface
   (content-hashed vite output); it reproduced byte-for-byte, which is what made (b) a re-label.
2. **Did not copy the wrapper's manifest file.** Its base is `d3c31e972e`'s parent, so copying it would have
   reverted MP-x-4's `release_note` and `previous_deployed_commit` and re-populated 10 `file_checksums` the shared
   tree keeps empty. Applied only this release's own five fields, asserting the prior `deployed_commit` first.
3. **Did not re-derive the tool census.** The surface is a function of bytes plus `ENABLED_INTEGRATIONS`, both
   proven unchanged; reconstructing it under a guessed shape risked a real-looking number against a different
   definition from the BEFORE.
4. **Stated the `pptx` sweep as 3, not 0.** All 5 hits are pre-existing extension mentions by `read_document`.
   "pptx absent" would have been false.
5. **Used a state-based negative control, not a planted mutant.** Every limb lives on the live plane or in an
   append-only shared file; planting would have meant mutating served state or creating a transient false OPEN a
   peer's `check --red` sweep could escalate on. The DEPLOY genre exists for this case but is not admissible —
   the order carries no `<proof_genre>DEPLOY</proof_genre>`, and DEPLOY is never self-declared.
6. **Refused the order's `<instance_path>` rather than forcing it.** It names worker ~28's folder; the lane rule
   permits only the serial in the sub-folder. `--force` bypasses contamination only, and the author override would
   have meant writing another agent's folder under a borrowed lane.

## Files Modified

- `org/critical_paths/change_management/20261009T1909Z_nfra-mcpindex-r8-discover-release_deploy_completion.md` (CLOSED)
- `org/critical_paths/.open_deploys/nfra-mcpindex-r8-discover-release.json` (deleted — sentinel removed on close)
- `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md` (+Z-S93, +Z-S94)
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MX/REPAIR_MX-r-9_LABEL_20261010.md` (+ `probes_repair_20261010/`, 6 files)
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MX/NFRA_MCPINDEX.TO-MX-r-9.discover-needs-release.proof_of_spec.json`
- `infra/aws/ec2/EC2_MANIFEST.json` (plane 2; 6 insertions, 6 deletions, 0 other services)

Commits `3cc6f5e6ec`, `1df2cdb295`, `d8e82150fd`. **Push state: all three ON ORIGIN @`e0acea2037` (`ls-remote`
read, with a positive control on the ancestry test).**

## Blockers

**None for this lane.** Nothing this seat owns is blocked, and nothing is stranded — each open item has a named
owner:

- `NFRA_MCPINDEX-Z-S92` disarm — `2.0.0_SA_COO~MI` is the `disarm_owner`, not this seat. Z-S93 carries the evidence.
- The free-host-slot relay to `2.0.0_SA_COO~O` and `2.0.0_SA_COO~MP` — the issuer reserved that to itself in 33003.
- `<instance_path>` amendment, `EC2_MANIFEST.json` in `<paths>`, `Z-S94` disposition — `2.0.0_SA_COO~MI`.
- J1 and J2 — `3.0.0_SA_CVO~Z` at L9; J1 also waits on Alyssa's own thread run, the round's declared essential wait.

## Current State

The gateway host serves exactly what it served before this session; only the labels changed. `/opt/opal-gateway`
is `active`, `/health` 200, running `d3c31e972e`'s content, with both S3 keys and the EC2 manifest naming that
commit. The versioned rollback handle is real again. The NEVER-2 ledger is CLOSED with no sentinel. The next
release on this host can cut on a ref that is actually serving, which was the whole hazard Z-S92 named.

Registered LIVE, one inbox watcher, **zero crons**. Worktrees created for this act and removed: `/c/tmp/mx-ac1-neg`
(negative control), `/c/tmp/mx-mcp-d60b4e0` (dashboard reproducibility). `/c/tmp/mx-dep-v2` is left at
`d3c31e972e` and `/c/tmp/mx-rb-v2` at `1e32562729` — **do not remove either**: they are the deploy and rollback
trees named in the ledger's rollback line.

## Next Steps

1. `[2.0.0_SA_COO~MI]` Disarm Z-S92 and relay the free host slot to COO~O and COO~MP (E2's `.xlsx` and MP-r-2
   wait on it).
2. `[2.0.0_SA_COO~MI]` Amend `<instance_path>` before flipping `<status>` to `complete`; disposition Z-S94; decide
   the `EC2_MANIFEST.json` path declaration.
3. `[3.0.0_SA_CVO~Z]` Grade J1 and J2 at L9.
4. `[0.7.0_AE_CloudOps~MX]` Event-driven hold: act on the next `[INBOX]` event the same turn, and re-arm the
   Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
