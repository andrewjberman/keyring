# Lane ~MP: the A5 remedy is COMMITTED, MP-r-2 is down to one gate, and the ruff fault is invisible to BOTH Windows logs -- 0.7.0_AE_CloudOps~MP

**archetype:** MIXED

**Date:** 2026-10-10
**Task Orders:** `NFRA_MCPORTAL.TO-MP-r-2` `pending` -- steps 0-3 DONE and committed, step 4 waits on one gate
**Status:** IN PROGRESS (not blocked by anything this lane owns)

---

## Why this file exists

The previous entry (`2026-10-09/mp_lane_delta_x4_live_r2_stopped.md`) says MP-r-2 is STOPPED at step 2 on
a load bar and that the issuer must re-cut. That is now wrong twice over: the issuer's AMENDMENT 5
supplied the one permitted load remedy, the remedy's bar was met at 12 of 12 samples, and the remedy was
then held UNCOMMITTED for about 25 hours by a toolchain fault that had nothing to do with this cell. That
hold is over. A successor reading only the older entry would go looking for a re-cut nobody owes.

## What this session put in the world

**Nothing in AWS. Nothing deployed.** Live `FETCH_THREADS` on the gateway host is still 8, no deploy-ledger
entry exists for slug `nfra-mcportal-cp2-release`, and no POST was made to
`/api/admin/fabric/calls/close` (BOUNDS 2). Three commits, all in-repo:

| commit | branch | what |
|---|---|---|
| `ea58e3662d` | `wk-mcportal-cp2-r2` | the AMENDMENT 5 load remedy in `app/admin_fabric.py` |
| `9f4d3ccadb` | `box/sitez` | surprise row `Z-S34` (the issuer asked for it to land so it could adjudicate) |
| `73547dcfd1` | `wk-mcportal-cp2-r2` | `MP-r-2_PRE_ACT_RECORD.md` superseded in place |
| `c4a26554fa` | `box/sitez` | surprise row `Z-S36` |

Push state, measured by `git ls-remote` with a positive control (origin's own tip reads ON ORIGIN) and a
negative control (the `wk-` tip reads LOCAL): `9f4d3ccadb` is **ON ORIGIN**; `ea58e3662d` and `73547dcfd1`
are **LOCAL** on the worker branch, which is correct -- they reach the trunk at the drain, not by a push
from this seat. `c4a26554fa` was LOCAL at commit time and rides the next `box-sync`.

## The A5 commit, and why it took a measurement rather than a retry

AMENDMENT 5 is two changes in `app/admin_fabric.py` and nothing else: `FETCH_THREADS` 8 -> 32, and
`_s3_client()` passing `config=botocore.config.Config(max_pool_connections=FETCH_THREADS)` so botocore's
default pool of 10 does not cap the gain. The prior session measured the amendment's tightened bar MET at
**12 of 12 cold samples, worst 13.828 s** against 30 s, each in a fresh interpreter with
`body_cache_entries_at_start` 0 on all 12, and the issuer accepted it (msg 32995). The edit then could not
be committed: `commit-gate` refused with `OSError: [WinError 4551] An Application Control policy has
blocked this file`, reported as `BLOCKED: ruff check failed on <file>`.

This session did not retry blindly. Before committing: `.tools/commit-gate.sh` on that exact file in that
exact tree -> `pre-commit gate clean for 1 of 1 file(s)`, rc=0; then the suite at the bytes about to be
committed -> `tests/test_admin*.py tests/test_entitlement_admin.py` **58 passed, 0 failed**. Then
`safe-commit.sh` with **no override** -- `--force` covers contamination only and
`GIT_COMMIT_AUTHOR_OVERRIDE` covers the lane check, so neither would have reached a gate refusal anyway.
The issuer independently asked for the commit in msg 33012 and, usefully, said the fault was
**intermittent** (one refusal in seven runs at 20:57Z), which is why the gate's verdict was read per
invocation instead of being assumed from one clean read.

## The finding worth carrying off this cell: both candidate instruments are blind to this fault

Row `Z-S34` (this lane's, filed the prior session) diagnosed the refusal as interpreter-specific --
Python311's `-m ruff` admitted, Python314's refused, and `commit-gate.sh:59` execs bare `python` which is
Python314 here. That mechanism is now **falsified on the very interpreter it named**:

| trial | result | denominator |
|---|---|---|
| `python -m ruff --version`, Python314 | 20 rc=0, 0 WinError 4551 | 20 |
| `python -m ruff --version`, Python311 | 20 rc=0, 0 WinError 4551 | 20 |
| `.tools/commit-gate.sh` on the A5 file (the real consumer) | 5 rc=0, 0 refusals | 5 |

**45 clean trials is a NON-REPRODUCTION, not a fix**, and the row says so in those words. The issuer's own
row `Z-S35` reached the same intermittency verdict from 6 of 6; the single 20:57Z refusal stays unexplained
by either row.

Then the part neither prior row had. The obvious next instrument is the Windows event log, and **it cannot
see this fault at all**:

- `Microsoft-Windows-CodeIntegrity/Operational`, over the 30 hours from 2026-10-09 15:22Z (spanning the
  first refusals at ~2026-10-09 20:0xZ, the 20:57Z refusal AND the clean window): **1,185 events, of which
  0 name ruff or python.** The 395 `Id=3033` policy blocks in that set are all SentinelOne's
  `SentinelAmsi64.dll` refused into `svchost.exe` at status `0xC0000428` -- a separate standing condition
  this cell does not own and did not file.
- `Microsoft-Windows-AppLocker/EXE and DLL`: only `Id=8001` policy-application notices, **no block event**.
  `AppLocker/MSI and Script`: no events at all.

So both logs read clean *while the fault was demonstrably occurring*. That is an ABSENT reading from an
instrument that cannot see the object -- CLAUDE.md's `ABSENT != EXERCISED-AGAINST` corollary exactly -- and
it matters operationally: **whoever grades the gate fix must grade it by EXECUTING ruff over a printed
denominator, never by reading these logs.** Filed as `Z-S36` (OBSERVATION / INERT, adjudicating Z-S35 /
Z-S34 / Z-S31, six evidence items).

One correlate is recorded *as* a correlate: AppLocker applied a policy at **2026-10-10T20:49:42Z**, 8
minutes before the last observed refusal and ~13 minutes before the clean window. But the **onset** --
between `354d58bc30` passing the same gate and the 2026-10-09 20:0xZ refusals -- has no corresponding
event in either log. A correlation at one end and silence at the other is not a mechanism, and writing it
up as one would have been the error the row exists to prevent.

## A discipline that paid, and one that nearly cost

**Paid:** the surprise channel is a shared append-only file, so the next free row id is read at WRITE time.
Doing that is what revealed the issuer had already appended `Z-S35` covering the intermittency -- and that
its row was still UNCOMMITTED in the shared tree. Appending mine on top would have swept a peer's in-flight
row into my commit under my author line. I held, said so in the report, and the issuer committed `Z-S35`
and handed the file back (msg 33022) before `Z-S36` went in. CLAUDE.md 14b's inversion for append-only
shared files is about the merge conflict; this is the *other* cost of the same shape, and the remedy is the
same -- do not isolate, but do look before you append.

**Nearly cost:** a Windows path with single backslashes inside a JSON string field produced
`Invalid \escape` and would have left a malformed row block in the channel if the JSON had not been parsed
before committing. The parse is the check (`json.loads` on the extracted block, printing the row count and
the last id); the gate's own `surprise-row-gate` confirms field coverage but is not a substitute. Fixed by
writing the path with forward slashes, which also dodges the harness heredoc's backslash handling.

## MP-r-2: exactly where it stands

| step | state |
|---|---|
| 0 route hookup | DONE, `354d58bc30`, 58/58 tests |
| 1 release tree + census + manifest + bun | DONE, `74d2522f22`, 8 files / 0 outside the CP2 set, `bc37107` |
| 2 load condition | **MET under the remedy**, 12/12 <= 30 s; remedy now COMMITTED `ea58e3662d` |
| 3 rollback proof | DONE, content-verified, unexercised |
| 4 ledger + act | NOT STARTED -- **one** gate: MX-r-9's ledger close, which the issuer forwards |

The second gate named in the prior record -- a working `.py` commit path on this device -- is cleared.

At the act, per the issuer's ruling (msg 33000, relayed as 33004): **read the live base from the HOST by
md5 against the candidate build input**, not from the artifact's `-latest` label, which reads `1e32562729`
and is MISLABELLED until MX-r-9's re-stamp of `d3c31e972e` lands; not from the manifest alone. Re-cut the
release tree on that ref, then re-run the census. So the existing `C:/tmp/mp-r2-rel` tree is deliberately
NOT refreshed now -- it would be re-cut anyway and the base is still moving. **Do not remove `C:/tmp/mp-r2`
or `C:/tmp/mp-r2-rel`.**

## Compiler Tools

- `.tools/commit-gate.sh` -- run 6 times on `app/admin_fabric.py` (1 pre-commit read + 5 as the rate
  measurement): 6 of 6 clean, rc=0. This is the tool whose failure held the cell for 25 hours, so the
  **reusable finding** is about reading it: it reports a failure to EXECUTE ruff with the words `BLOCKED:
  ruff check failed on <file>`, which sends the author hunting a lint defect in correct code. Under an
  intermittent fault the right first response to that message is ONE re-run, not an investigation.
- `.tools/safe-commit.sh` -- 4 commits, no override on any. Its `[msg-verify] MATCH len=N` line is the
  thing to read: it confirms the `-F` message landed whole, which a positional `tail` of the output would
  not have told me (and a positional slice has given both a false LANDED and a false REFUSED before).
- `.tools/safe-commit.sh` embedded limbs worth naming: `surprise-row-gate` printed `1 new row of 56 total
  checked (55 pre-existing, NOT re-graded)` -- the denominator is what makes that a real check; and
  `surprise-corpus` printed `documents=398 rows=10784 failures=4 baseline=4 known=4 new=0`.
- `comp-find --files '<class tokens>' --limit 20` -- used to ask whether the A.2 audit-archive finding
  classes are already filed somewhere. **Read the bands before the hits:** `DENOMINATOR: 656 hit(s) across
  176742 file(s)`, `BANDS: HEAD=20 SURFACED=189 CONFIG=13 TEST=4 DOC=430`, and the HEAD band's rows are
  filename matches that are not the class token at all. The question was not answered by it and I did not
  pretend it was; see Blockers.
- `.tools/to-check.py --all --assignee <full serial>` -- `total=1 projects=1 blocked=0 scanned=5451`. The
  trap, which cost one wasted read: the long list AFTER the result line is the `THIRD-POPULATION` partition
  (91 of 5451 faces with a `<status>` and no recognised assignment field), NOT this lane's orders. A `tail`
  of this tool's output shows that partition and reads like a holdings list. Read the first 20 lines and the
  `TO-CHECK-RESULT` line; never the tail.
- `python .tools/sequence-check.py --project NFRA_MCPORTAL` -- the project is unlisted in SEQUENCE, which
  per `org/XXX.md` means unsequenced, not blocked.
- `python .tools/audit-archive-invoker.py` -- rc=1, 16 findings, baseline 0.1h old. Surfaced, not re-filed;
  see Blockers.
- Windows event log via `Get-WinEvent` -- used as an instrument and found BLIND to the subject fault. The
  `@( )` wrap and `[xml]$_.ToXml()` are needed to get at `EventData`; the rendered `Message` is what to
  regex, because the field name I first guessed (`File Name`) does not exist in this provider's schema and
  returned `distinct file names: 0` against 386 real events -- a zero produced by the wrong field name,
  which reads exactly like a zero produced by absence.

## Blockers

**None owned by this lane.** MP-r-2's step 4 waits on MX-r-9's ledger close (OPEN since 2026-10-09 19:09Z);
the owner is `2.0.0_SA_COO~MP`, which says it forwards the close, and `2.0.0_SA_COO~MI` re-seated its
applier at 21:07Z. A dated, owned wait is not a block, and this seat chases neither.

Two items open and owned elsewhere, each named with its owner so neither is stranded:

- **The commit-gate ruff fault** -- `0.0.0_AB_MSTR~Z` as gate owner, holding `Z-S31`, now adjudicated by
  `Z-S34` / `Z-S35` / `Z-S36`. Unconditionally true regardless of the intermittency: `commit-gate.sh:59`
  execs bare `python`, and the gate conflates "could not EXECUTE ruff" with "ruff REPORTED findings".
  Smallest fix is one function -- resolve the ruff BINARY with `shutil.which('ruff')` and fall back to
  `[sys.executable, '-m', 'ruff']`, the way `.tools/safe-apply.sh` resolves terraform device-agnostically.
- **The A.2 audit-archive findings (16, rc=1)** -- classes `COVERAGE/MANIFEST-ENTRY-MISSING-LIVE` (5),
  `COVERAGE/UNCOVERED-AUDIT-LOG` (2), `INTEGRITY/NON-APPEND-EDIT` (4), `INTEGRITY/ERROR-FAILCLOSED` (5).
  **Surfaced, NOT re-filed and NOT adjudicated**, per the Step A.2 instruction to surface only a class with
  no owner. I could not establish ownership cheaply (the `comp-find` census above did not answer it), so
  the honest state is **ownership UNREAD**, not "unowned". The baseline was 0.1h old at my run, so a peer
  on this box runs the same invoker and sees the same 16. Several `NON-APPEND-EDIT` rows have a baseline
  LARGER than live-head, which on a box that takes `box-sync` merges is the shape a merge produces rather
  than a tamper -- worth one read by whoever owns it, and out of this lane.

## Next Steps

1. `[2.0.0_SA_COO~MP]` Forwards MX-r-9's ledger close. That is the only thing MP-r-2's act waits on.
2. `[0.7.0_AE_CloudOps~MP]` On that message, same turn: read the live `deployed_commit` from the HOST by
   md5 against the candidate build input (never the `-latest` label), re-cut the release tree on that ref,
   re-run the census, then step 4 in order -- ledger open with the pointer line, commit the entry AND its
   sentinel, act from the release tree with ITS scripts, `/health` 200 inside 90 s or the named rollback AT
   ONCE, tool-surface counts before and after with an empty difference, manifest record, close every leg
   before the AC reads.
3. `[0.7.0_AE_CloudOps~MP]` Expect the cold times to depend on the hour: the activity store grows through
   the working day (`Z-S27`), so step 2's reads are re-taken at the act, not inherited from this record.
4. `[2.0.0_SA_COO~MP]` Appends its adjudication to `Z-S34`, now that it is committed and ON ORIGIN.
5. `[0.0.0_AB_MSTR~Z]` Owns the gate fix under `Z-S31`; `Z-S36` tells it how to grade one (execute ruff
   over a printed denominator) and that the event logs cannot.
