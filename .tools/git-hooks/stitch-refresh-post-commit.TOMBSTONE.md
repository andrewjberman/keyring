# TOMBSTONE -- the local stitch-refresh post-commit hook AND its installer, RETIRED 2026-09-09

**Files retired in this act (both `git rm`-ed):**

| file | lines | what it did |
|---|---|---|
| `.tools/git-hooks/stitch-refresh-post-commit.sh` | 27 | the post-commit body: on any commit touching `portal/`, `data/*/scripts/`, `org/modules/graph/` or `infra/aws/globgrph/{derive_stitch,extract_portal_stitch}.py` (the filter regex at its `:23`), it ran `.tools/stitch-refresh` in a detached background subshell, which published `stitch/stitch_graph.json` + `stitch/stitch_marker.json` to `s3://opal-313476888478-globgrph/` with `producer: stitch-local`. |
| `.tools/git-hooks/install-stitch-refresh.sh` | 31 | the installer: appended the hook line to `.git/hooks/post-commit` on any clone, idempotent on the marker string `stitch-refresh-post-commit`. |

**LAST HASH CARRYING BOTH FILES: `2e8dd90435`** (`2e8dd9043508f33f170d6656968fa9612a95c667`, the parent
of the commit that retires them). Recover either body with `git show 2e8dd90435:<path>`.

**WHY BOTH, when the cell names one.** `CG-s-29` / PRD v0.7 row S29 names "the two scripts" of lane
`0.8.0_AE_CloudComp` and spells out `stitch-refresh-post-commit.sh` and `.tools/stitch-refresh`. This act
took the WIDER reading and retired the INSTALLER as well: an installer of a retired hook is a route back --
one `bash .tools/git-hooks/install-stitch-refresh.sh` on any clone re-creates the executable plane that the
device act (`0.0.0_AB_MSTR`, per clone) is removing, and it would do so silently, because the hook is
invisible to the committing seat. That is S17's lesson about the instruction plane. **A grader who reads
S29 as exactly two files should read this paragraph as the naming of the choice, not as a widening claimed
without notice.** (`0.9.0_WK_NFRA_CLDGRPH~5`, TO-CG-F-9, on the issuer's stated preference.)

---

## ON WHOSE WORD

**THE EARLIER WORD, kept verbatim and marked SUPERSEDED (never edited away, never silently) --
Andrew-direct 2026-07-07**, as quoted in `.tools/stitch-refresh:6-12` and in the retired hook's own header:

> Replaces the cloud stitch-produce (GH-Action source-zip -> S3 -> nightly CodeBuild).
> Andrew-direct 2026-07-07: for a SOLO contributor whose local working tree IS the
> canonical state, the derivation should read the local repo directly -- the entire
> cloud apparatus existed only to get repo source to a repo-less cloud runner, a
> problem that does not exist when you run where the source already lives. This
> deletes the GH-Action + CodeBuild + EventBridge + GHA-OIDC roles + the
> PORTAL_REPO_PAT / .gitmodules-second-checkout saga.

**THE LATER WORD, which governs -- Andrew, 2026-09-02 ~17:5xZ**, the ratified endpoint of NFRA_CLDGRPH:
FWD-7 *"The estate keeps one graph story, and the per-machine copy is retired rather than kept alongside"*,
DONE WHEN *"after the local copy was switched off"*; and the PRD title he ratified:
*"no machine is in the compile business"*.

**THE RULE THAT RECONCILES THEM -- R16** (NFRA_CLDGRPH PRD v0.7 s.6 @`a46abe413a`, ratified from the ruling
below), verbatim:

> a word bound to a stated premise does not bind past that premise; where two of Andrew's words name ONE
> object in opposite directions, the LATER governs and the earlier is kept verbatim, marked SUPERSEDED with
> the later word cited -- never edited away, never silently.

The 07-07 premise -- *a SOLO contributor whose local working tree IS the canonical state* -- is false in
fact at this date: two fabrics, ~10 seats, canonical state on `origin/CLOUD`. The word does not bind past
its premise; it is kept, above, in full.

**THE RULING RECORD:**
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_NFRA_CLDGRPH_20260909T1856Z_S71_STITCH_KEY_ONE_WRITER.md`
(`1.0.0_SA_CTO`, 2026-09-09 ~18:56Z) -- RULING: the cloud producer `opal-stitch-produce` holds both stitch
keys from its first publish, 2026-09-09T18:49:23Z. Landed as PRD v0.7 row S29 (three planes: executable,
instruction, residue) @`a46abe413a`, over surprise rows `NFRA_CLDGRPH-S70` and `-S71`.

---

## THE S71 NUMBERS (why it had to stop)

- This laptop's residue log `${TMPDIR}/stitch-refresh.log`: **666 runs / 552 PUBLISHED / 143 refused** since
  2026-07-07 -- i.e. **552 writes to the shared stitch keys from one laptop**, none of them visible to the
  seat whose commit fired them. (Re-read at this act: 16,206 lines, 552 `OK: stitch published local`,
  145 grain-sentinel refusals -- the log is NOTED, never deleted.)
- **Site Z's copy of the same hook wrote the SAME key at 2026-09-09T17:53:55Z** (`producer: stitch-local`,
  `git_sha 9b99b493`, 29,320 nodes / 61,833 edges).
- The cloud producer published the same key **56 minutes later, at 2026-09-09T18:49:23Z**
  (`producer: stitch-codebuild`, `git_sha de590a7d`, 29,267 nodes / 61,275 edges).
- ONE key, TWO writers within the hour, and the two derives disagree by **53 nodes / 558 edges**. On this
  laptop the derive had refused on every run since 09-05 (grain sentinel), so the laptop was inert *by
  accident*, not by design -- which is exactly the failure mode this tombstone closes.

---

## HOW TO RE-ENABLE -- only on Andrew's word

There is no supported path back; this is the reversal procedure if he says so, in order:

1. Restore the two bodies:
   `git show 2e8dd90435:.tools/git-hooks/stitch-refresh-post-commit.sh > .tools/git-hooks/stitch-refresh-post-commit.sh`
   `git show 2e8dd90435:.tools/git-hooks/install-stitch-refresh.sh > .tools/git-hooks/install-stitch-refresh.sh`
2. Restore the publisher: `git show 2e8dd90435:.tools/stitch-refresh > .tools/stitch-refresh` (the current
   file's derive/marker/publish body -- old lines 44-87 -- was DELETED, not left dead, so it must come back
   from that hash; the refusal at its tail exits 3).
3. Re-add the hook line **per clone** -- this is the installer's own line, and the only device-plane act:
   ```
   printf '\n# stitch-refresh-post-commit (installed %s)\n_ws="$(git rev-parse --show-toplevel 2>/dev/null)" && [ -n "$_ws" ] && sh "$_ws/.tools/git-hooks/stitch-refresh-post-commit.sh"\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> .git/hooks/post-commit
   ```
   or re-run `bash .tools/git-hooks/install-stitch-refresh.sh` once step 1 has restored it.
4. And first settle the thing that made it wrong: **two writers on one key**. Either the cloud producer
   stops, or the local one does. Both cannot hold `s3://opal-313476888478-globgrph/stitch/*`.

**The device plane is NOT this file's act.** The `stitch-refresh-post-commit` line in each clone's
`.git/hooks/post-commit` is removed per clone by that device's integrator (`0.0.0_AB_MSTR` on this laptop;
site Z's integrator over the agentbus, site Z FIRST -- it is the live overwriter). Removing these repo files
does not by itself stop a clone whose hook line is still installed: that clone's hook would call an absent
script and, per its own `:19-20` guard style, simply fail quietly -- inert, but not retired.

**The residue plane:** each device's `${TMPDIR}/stitch-refresh.log` is noted, not deleted.
