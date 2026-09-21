# /self-drive IRPT_FNTEND IRPT_BCKEND -- ticks 2-3 + mid-cycle event (2026-09-21 ~15:1xZ-15:5xZ)  state: ARMED

Driver `1.0.0_SA_CTO`; carrier `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_1503Z_SELF_DRIVE_IRPT_FNTEND_IRPT_BCKEND.md`
@`c9ccd9f4e3`; cadence 30m (cron `46e545b7`, `7,37 * * * *`); `paired_with: solo`. Previous log:
tick 1 @`6467101f2c`.

## Ticks 2-3: quiet

Both ticks printed to the terminal, neither written/committed -- zero unread mail, zero open
calls, open-TO denominators unchanged (10 `IRPT_BCKEND` / 2 `IRPT_FNTEND`) at both reads
(15:11Z, 15:41Z). No sequence flags. Per the skill's own delta-driven policy, a quiet tick
writes nothing.

## Mid-cycle event: `IB-rth-5` never-widen half DECLINED, a real finding filed

`2.0.0_SA_COO~B` (msg `99072`, tick 10 of its own loop) reported `IB-rth-5` (session-establishment
tooling for the export render host) drained clean and asked for the CTO never-widen half. Before
signing, re-derived all five touched files' hashes via git plumbing (not a disk read, since the
packet claims to pin committed bytes), then raw disk bytes for every file `.gitattributes` doesn't
protect, to see the full shape rather than stop at the COO's own already-disclosed instance.

**Result: the packet's `COMMITTED-FILE-SHA256` table is inconsistent for 2 of 5 files, not the 1
COO disclosed.** `capture-session.cjs` correctly pins the git blob (COO's own finding, confirmed
independently). `render_export.cjs` and `package.json` pin the local CRLF DISK hash instead -- the
git blob differs for both, and neither file was touched again after the packet's own commit
(`a05d2dcaaf..HEAD` empty for both paths), so the table was wrong from the commit that introduced
it, not stale. The COO's own deploy-mechanics fix for the one file it found (`git show
HEAD:<path>`, never a raw local `aws s3 cp`) is correct and, applied uniformly across a deploy step,
produces git-blob bytes for all five files -- matching the packet's claim for 3 of 5 but NOT for
these two, which would either false-fail a deploy-time hash verify or, if "fixed" by sourcing those
two from disk instead, recreate the exact CRLF-mix problem one file over.

**DECLINED to sign.** Finding filed: `CTO_FINDING_IRPT_BCKEND_IB-rth-5_PACKET_HASH_TABLE_INCONSISTENT_20260921.md`
@`f5b8c0ac2e`. Sent to `2.0.0_SA_COO~B` asking for the table corrected to the git-blob hash for the
two files, re-committed; will sign against the corrected blob the same tick it lands. Not disputing
the wiring, the MFA boundary, or the blast-radius reasoning -- all sound on their own merits.

Handled under this loop's own CALL ROUTING (any open call closes on the driver's own rec, same
tick) -- this is not a governance or design fork, it is a factual/mechanical correction request, so
no CVO pitch.

## Scope state at this write (denominators printed)

- `IRPT_BCKEND`: `status: active`, `dep_stage: EXECUTING`, 10 PENDING TOs (unchanged this window;
  `rth-5` itself already drained/signed on the COO side, one function's build-and-apply sequence
  otherwise unaffected by this hold).
- `IRPT_FNTEND`: `status: active`, `dep_stage: EXECUTING`, 2 PENDING TOs (unchanged this window).
- **REACHABLE: 2 of 2.**
- **COMPLETION TEST: NOT DONE** -- 0 of 2 projects `status: complete`.

## RESERVED cards still at Andrew (unchanged)

`irpt-ycharts-runner` EC2 stop-confirmation; the non-MFA portal service-account question.

## Next tick (~16:07Z) watches

Whether `2.0.0_SA_COO~B` re-commits the corrected packet (then this seat signs same-tick); `rth-1`'s
7-function apply completing; `IRPT_FNTEND` wave-A drain progress.

Push state: LOCAL on CLOUD (`f5b8c0ac2e` this loop's latest own commit); `origin/CLOUD` `d32d3ad8b8`
per `ls-remote` read this write; only `0.0.0_AB_MSTR` pushes.

## Compiler Tools

`get_agent_status`/inbox read x3 (ticks 2, 3, mid-cycle); `to-check --all --project` x2 per tick;
`sequence-check --project`; `git hash-object` (packet blob); `git rev-parse HEAD:<path>` + `git
cat-file -p` + `sha256sum` (5 files, git-blob method); `git show HEAD:<path> | sha256sum`
(cross-check, same method, different command); `git log --oneline -- <path>` x2 (staleness check);
`git show <commit>:<path> | sha256sum` (pin the packet's own commit, not just HEAD); `python`
raw-bytes `sha256` (disk-read method, `encoding` not needed -- binary mode); `git check-attr text
eol --` (5 files, one call); `git ls-remote`.
