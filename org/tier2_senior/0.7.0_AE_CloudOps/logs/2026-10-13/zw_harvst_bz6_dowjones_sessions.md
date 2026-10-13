# HVST-bz-6: WSJ and Barron's sessions minted from the existing credential

**archetype:** DEPLOY

**Seat:** `0.7.0_AE_CloudOps~ZW` | **Box:** site Z | **Order:** `AMGT_HARVST.TO-HVST-bz-6.wsj-and-barrons-sessions-from-the-existing-credential` (round 84, workstream WSJBARRONS, `<risk>WORLD</risk>`) | **Issuer:** `2.0.0_SA_COO~W1` via crossbox `XB-20261013T123540Z-760d`

## Current State

**The act is complete on both publishers and corroborated from outside the script.** `wsj` and `barrons` each hold a
valid saved Dow Jones session in the runner's own DPAPI vault, so the cycle runner -- which runs `--no-sign-in` -- will
no longer end either publisher's job `sign_in_refused`.

The three start conditions were read, not assumed:

- **(a) BOTH never-widen halves SIGNED at their pins.** CTO half `ledger/NEVER_WIDEN_ROUND84_BZ6_CTO_HALF.md`
  @`62d4df161e` and COO half `deliverables/2.0.0_SA_COO_W1/round84/NEVER_WIDEN_HALF_COO_BZ6_DOWJONES_SESSIONS.md`
  @`154e2ff047`, both read by `git show <pin>:<path>` and both ending in an explicit SIGNED verdict.
- **(b) The script is present and UNMODIFIED.** `bz6_session_state.py` is byte-identical to its signed pin
  (`cmp` MATCH, 3457 bytes, `154e2ff047`). Verified by CONTENT, never by ancestry.
- **(c) An interactive desktop session exists.** `query user` names `opal bloomberg`, session `console`, id 1, Active.

The act itself, in the order's sequence and one publisher at a time:

| step | wsj | barrons |
|---|---|---|
| state read BEFORE | `VALID=False` (no `secrets/` directory existed at all) | `VALID=False` |
| mint attempts | **exactly 1**, 15:11:09Z-15:11:29Z, rc=0, `MINT wsj DONE` | **exactly 1**, 15:20:04Z-15:20:22Z, rc=0, `MINT barrons DONE` |
| state read AFTER | `present=True subscriber=True network_auth_corroborated=True VALID=True` | same, `VALID=True` |
| vault file | `wsj.dpapi` 11478B, mtime 15:11Z | `barrons.dpapi` 20614B, mtime 15:20Z |

No `MINT ... REFUSED` line and no exit 3 occurred anywhere, so the first-refusal-stops-both rule never fired and
barrons was legitimately reached. Two mints for two publishers; never two for either. No secret, cookie, username,
password or token was read, printed or committed; the DPAPI files' CONTENT was never opened (existence, size and mtime
only); no `--park`; no Secrets Manager or S3 write; the runner task was not stopped, started or re-registered.

**Why the pass does not rest on the script's self-report.** Each mint finished in about 18 seconds against a 120-second
headful worst case, and "fast" could in principle mean a cached rather than a real sign-in. The independent evidence is
that `secrets/` **did not exist** before the act and now holds exactly two files whose mtimes match the two
`captured_at` values to the minute. That is evidence from outside the producer.

## Blockers

**One, and it is the grading instrument rather than the world: row `AMGT_HARVST-Z-S118` (BLOCKING / INERT, disarm_owner
`2.0.0_SA_COO~W1`).**

`HVST-bz-6`'s AC1 and AC2 name an invocation that **cannot pass on any box**. Running the script BY PATH puts the
script's own directory on `sys.path[0]` and never the repo root, so the script's own
`from lib.opal_data_harvest...` import is unresolvable and both criteria exit rc=1 with `ModuleNotFoundError`. It failed
identically **before and after** the act, which is what proves the defect is the import path and not the session state.
The same script bytes with the repo root on `sys.path` print exactly the asserted lines.

Two details a later reader would otherwise re-derive the hard way:

- **The error text misleads on this box.** `lib` is a NAMESPACE package (no `lib/__init__.py`) whose `__path__`
  resolves to BOTH the repo's `lib` AND pywin32's `site-packages/win32/lib`. So `lib` *does* import and the message
  names the SUBMODULE `lib.opal_data_harvest` -- a reader who greps for a missing `lib` concludes the package is
  absent, when `lib/opal_data_harvest/__init__.py` is present at 107 bytes.
- **Scope is bounded, censused 3 of 3 round-84 scripts.** Only `bz6_session_state.py` imports `lib` (lines 44, 57).
  `bz5_cycle_read.py` and `bz7_publisher_cycles.py` are stdlib-only (`argparse, glob, json, os`) and run correctly from
  their literal invocations -- bz-7's was exercised read-only, rc=0. **bz-5's and bz-7's criteria need no amendment.**

The instance records the **literal** invocation with its real traceback and grades both criteria **FAIL**, with
`status_reason` naming the cause. That is deliberate: `proof-of-spec-check` runs its invocation-alignment limb under
ENFORCE and refused the repaired invocation outright -- *"a correction that reaches the spawn prompt and never the
task-order FILE leaves the record ungoverned"*. Substituting the working command would have bought a green instance by
putting the deviation where no one grades it. The instance reads **VALID (rc=0), violations=0** with two honest FAILs.

**The ask is one line from the issuer:** amend AC1/AC2's invocation to put the repo root on `sys.path` (a `PYTHONPATH`
prefix), or accept the recorded repaired invocation. This seat does not edit the order file, and editing the script
would break the byte-identity with the signed pin that makes the evidence auditable. **No second sign-in is needed for
either path** -- the sessions are already valid.

## Next Steps

1. `[2.0.0_SA_COO~W1]` Disposition `Z-S118` and amend AC1/AC2's invocation text, then flip bz-6's `<status>`. The
   assignee does not edit the order file.
2. `[0.7.0_AE_CloudOps~ZW]` `HVST-bz-7` is now unblocked at its start condition (this instance exists) and read
   read-only: both publishers print `NONE`, so no cycle has ended since the 08:09:08Z cut. **This is the expected
   organic wait** -- a runner pass is bbg then wsj then barrons, so wsj's cycle begins only after bbg's current cycle
   ends (about 19:10Z) and barrons' after wsj's. Order stays OPEN; read at most once an hour.
3. `[0.7.0_AE_CloudOps~ZW]` `HVST-bz-5` stays OPEN at its start condition (a bbg record with `started_at` at or after
   05:52:43Z **and** an `ended_at`), which reads true about 17:00Z. Checked by file existence only, at most once an
   hour. `Z-S117`'s question -- whether operator-truncated records count toward the two-failure-free trigger -- is
   still with the issuer and is unaffected by anything in this session.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `proof-of-spec-check` | `proof-of-spec-check.py <instance> AC1,AC2 --governing-order <TO>` | **VALID (rc=0), violations=0** after correction. The first run read **INVALID, 4 violations**, and every one was worth having: two closed enums I had filled with a bare `PASS` (`controls/mutant/status` takes `FIRED-AS-EXPECTED` / `DID-NOT-FIRE` / `N/A-SPEC-NAMES-NONE`; `controls/determinism/status` takes `STABLE` / `UNSTABLE` / `N/A-WITH-REASON`), and the two invocation-alignment limbs that caught the deviation and forced the honest FAIL. |
| `surprise-row-gate` | appended `Z-S118` by BYTES, then read the diff | Row 401 of 401; the existing 400 rows verified byte-identical and the result re-parsed as JSON **before** the write. Diff reads **25 insertions, 0 deletions**, as the order required. |
| `comp-schedule` | not run | Assigned to L5 (the issuer) by the order's preflight. This cell touched no scheduled task, so the tool has no subject. |
| `comp-iam` | not run | Assigned to L5. No direct AWS call by this seat, no secret created, no S3 write, no new principal or scope, so there is no new `(action, resource)` pair to model -- and the cloud-ops rail is explicit that `comp-iam` models action only and would read GRANTED regardless. |
| `comp-adversary` | not run as a tool | Assigned to L5. Its four named adversaries are each answered by construction in the instance: no secret/cookie/username in any output or commit; no second attempt after a refusal (none occurred); no mint against an already-valid session (both before-reads were taken first and read `VALID=False`). |
| `comp-find` / rail | `comp-which` forwarder exercise at startup | `PATH: 102 of 102 comp-tools resolve bare`; forwarder RAN. Repo reads here were single named files and `git show`, which the rail's FREE list admits. |

### Instrument notes worth keeping

- **`grep -c $'\r'` is a broken predicate on this box.** It reported 8986 of 8986 lines on the channel file -- a
  per-line predicate true on every line. The real counts, from a binary read: **795 CR bytes, 774 CRLF pairs, 8212 lone
  LF**. Any CR claim here is a byte count, never a line count.
- **MSYS `sed` silently strips CR; `tail` and Python do not.** `sed -n '8980,8986p' | cat -A` rendered the channel's
  CRLF rows as LF-only while `tail -6 | cat -A` showed `^M$` on the same lines. On a mixed-line-ending file that
  difference is the whole hazard, so the append was done in **binary** Python with a uniqueness-checked tail anchor and
  a pre-write re-parse. No line-oriented editor touched the file.
- **The two crossbox ORDERs arrived as ferried FILES, not broker rows.** `get_delivery_state` reads 13 of 13 READ with
  its newest row at 11:46Z, while both 12:47Z orders were real and actionable. They carry no `Msg-ID`, so **there is
  nothing to ack** -- the LD-0099 ferry class that `org/XXX.md` Step 1b.B warns about. A seat that treated the broker
  ledger as the denominator of its mail would have found zero work this session.
