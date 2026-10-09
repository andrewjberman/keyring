# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-09 02:26Z to ~05:20Z

Seat instantiated 02:26Z on box dell1. `/watcher` armed at load, `/cloud-ops` oriented once, `org/XXX.md`
A-F completed. Two orders worked: `MDPF_SECCLASS.TO-SC-e65b` (closed) and `MDPF_SECCLASS.TO-SC-e71b`
(in flight, act held for its window).

## TO-SC-e65b -- the two-key cash-token ship. COMPLETE.

One safe-deploy at 02:37:33Z moved `code/gold/lib/_shared/etf_classification_scheduled.py` in
`opal-data-bd` and `opal-data-cot` from ETag `3f1e6be8910952f33c88bf100c610ab6` to md5
`40ffa3fac380551704637adc8a3b6ff3`. AC1 `E65-SHIPPED ok=True ... control=MATCH`, against a stated base of
`ok=False`. Ledger `secclass-e65b-namekey-ship-dell1-20261009` CLOSED, all 3 legs proven, sentinel removed.
No rollback was needed and none was performed; both handles stayed live and unused.

**The mechanism had moved since signing, and that was the one thing worth getting right.** CTO condition 1
directed the carrier route because a literal `_shared` safe-deploy was reported to ship nothing (msg 499).
Under `1.0.0_SA_CTO` msg 107147 the carriers no longer ship this module, so that route is closed. Rather
than inherit the issuer's measurement I called `shipped_artifacts_for()` myself with the order's exact
arguments: exactly the two signed keys, `unrouted` 0, and a no-`--tree` negative control returning 0 --
which is also the explanation of msg 499, since a named form with no tree ships nowhere. The named form is
strictly narrower than the carrier route (2 keys, not 8) and reaches the same signed end state.

**The watch set was widened deliberately.** The order names two watch keys; the signed halves name six and
make "any other moved key is a STOP" their acceptance. An order does not narrow a signed half, so leg V
measured the superset -- 12 keys, 12 of 12 read, no absences. All six half-named keys came back at exactly
the pre-act ETags the WITHDRAWN e65b ledger recorded, measured here rather than inherited. Post-act, 10 of
10 watch keys were unmoved on BOTH ETag AND VersionId -- stronger than the halves required, because under
msg 107147 the unnamed members were never re-uploaded at all. Compared by script, not by eye. STOPS=0.

**Behaviour was proven, not just bytes.** The served file was pulled back out of S3 and
`cash_token_match()` exercised in those bytes: 9 of 9 across a LANDS arm, a NEGATIVE arm (no
over-narrowing) and 2 controls. Then both module versions were run over real keys -- OLD from git
`@03f7f8fb5c`, md5 verified equal to the measured pre-act ETag, vs the served NEW bytes -- over all 331
real `NAME::`-keyed cash rows: OLD-yes/NEW-no = 8, **OLD-no/NEW-yes = 0**. Narrowing-only confirmed on live
data, not merely by reading the diff.

**Leg G.** The second BD fire of the day is data-arrival driven, not a cron: there is no 04:00Z EventBridge
rule and the only enabled bd-gold cron is `bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *)`. The runner
came up 04:00:46Z and E_18 ran as PHASE_B3b, run_id `80c0f41545a1`, 05:07:56-05:08:02Z, checkpoint
`gold/.checkpoints/2026-10-09/E_18.done` (corroborated by an independent head-object, 123 B, 05:08:03Z).
`Scheduled rows written / refused: 0 / 0`, so condition 3 passes on the half's branch B.

The absent-is-not-exercised-against trap was closed on two arms, because a zero from stale code reads
identically to a zero from new code. BY CODE: both on-instance copies were md5'd at 04:0xZ, *before* E_18
executed, and both read `40ffa3fa` at 35,360 B with mtime 02:37:33Z -- the S3 LastModified carried down by
the runner's copy, i.e. this seat's upload; the sibling `etf_classification.py` read `3a033c04` as a
positive control, equal to its served ETag. BY CONTENT: the 3 truly-unresolved names carry no CASH token at
all, so the rule had nothing to act on either way. Qualifier kept rather than dropped: E_18 is in
`NONFATAL_IDS`, so `rc=0` was read from E_18's own block, never inferred from the chain surviving it.

The ledger was HELD on the named external gate while only the verify leg was open, so it read KNOWN-HELD
instead of blaring a false half-landed RED at 02:36Z+24h, then released when the gate was met. Peer entries
in the same state use exactly that verb.

## Surprise row MDPF_SECCLASS-D1-S17

Filed while building leg G's method from the predecessor leg. The e65 ledger's L4 cites a scan filtered
`input=cash_token`, 0 of 9,155, as "THE TABLE AGREES". That filter cannot return non-zero: zero of 11,361
rows carry an `input` attribute, and the same filter returns 0 for `bd-securities`, `gics`, `schwab` and a
nonsense control. The module's `write()` strips the label; the persisted field is `classified_by`, which
names the writer. A wrong-domain census, with the printed denominator supplying the false assurance -- the
narrowing is in FIELD, which a denominator cannot show. e65's conclusion is undisturbed: its primary
evidence (stdout plan lines plus on-instance md5) is independent and sound. One corroborating limb is void.
Row carries the sound substitute and an explicit warning that its naive reading ("330 violations") is wrong,
because the module is put-on-absence and condition 3 governs only what the next run plans.

## TO-SC-e71b -- one re-seed of 15 rows. IN FLIGHT, act held.

Steps 0-2 done, ledger `secclass-e71-seed-names-sc1-20261009` opened with an 8h window (not 24h: the act
must land before the 10:30Z COT fire, so a RED at ~12:1xZ is the correct alarm), leg V CLOSED.

The dispatch line held step 4 until the issuer confirmed the 36-reader census, and cross-adjudication
XA-20261009T034916Z-ccd1 is why: its ruling ADDED that the issuer must write the reader verdict into the COO
half's record *before* the act. So the hold was the ruling's requirement, not a dispatch preference, and I
did not adjudicate the recorded census as sufficient and proceed. GO msg 1622 cited the census
`@1a4eb4ca66`; I verified it at that pin by printing the bytes rather than grepping for the quote, confirmed
byte-identity with my worktree copy, and confirmed the pin is an ancestor of HEAD.

Leg V: `SEED-NAMES ok=True keys=12 match=12`; all 15 snapshot rows re-read with individual
`--consistent-read` get-items and compared on every field *including* `last_updated` -- 15 of 15 equal, 0
moved, 0 absent. Dry run reads `15 of 197` with a CONFLICT census parsed rather than eyeballed: 12
conflicts, all of field `name`, on exactly the 12 signed tickers, nothing beyond -- CTO condition 4
satisfied.

**Neither exit code in this order discriminates**, and both were avoided as oracles: the dry run exits
`rc=3` on BLOCKED, and AC1 exits `rc=0` while reading `ok=False`. Verdicts were read from the
`[DRY RUN MODE]` marker, the MERGE SUMMARY table and the `ok=` token. Row D1-S18's trap ("Items written: N"
prints under `--dry-run` too) was avoided by construction.

AC1 was run pre-act as a live-discriminator control: `E71-RESEED ok=False rows=15 names_ok=0/12
class_moved=[]`, exactly the base the order predicts, with `name_miss` byte-identical to the dry run's
CONFLICT set and the halves' list -- three independent instruments agreeing on the same 12 tickers.

Remaining: step 4 after the BD run ends (runner stopped, no `trigger-pending`) and before 10:30Z, then AC1,
a second dry run reading `0 of 197`, close, flip.

## Compiler tools

- `comp-read --for` on `safe_deploy_core.py`, `proof-of-spec-check.py`, `surprise-row-gate.py` and the
  served module; `comp-read --enumerate` for the `D1-S<n>` row-id census (34 hits, 16 headings, denominator
  printed) so the new row minted as S17 rather than colliding.
- `comp-find` for the `cash_token` reader census.
- `safe-deploy.sh`, `deploy_ledger.py` (open/close-leg/hold/close), `proof-of-spec-check.py`,
  `commit-gate.sh`, `safe-commit.sh`, `sequence-check.py`, `xadj.py show`.
- Rail denials hit twice on piped comp-tool output and aborted the whole call both times; re-run unpiped
  with `--width`. Noted because the abort is silent for later segments.

## Push state

Commits this session: `a575721bb6`, `5832bb9bba`, `f5268f3c7f`, `94c75966cf`, `c7a2d076d1`, `985c5081be`,
plus this log's commit. Measured at close by `git ls-remote`; the first two reached origin via box-sync,
the rest were LOCAL at last read. This seat does not push `box/dell1`.
