# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-09 07:00Z to ~07:20Z

**archetype:** DEPLOY

Second segment of this session. The first is `session_e71b_act_and_close_0605-0630Z.md`. Written now rather
than at the order's close because leg G waits about 16 hours on a scheduled run and this seat is
event-driven: it may not be live when the run fires, and a successor needs the position without re-deriving it.

## TO-SC-e60b -- BD D_04 shipped ALONE. Legs V and D CLOSED, leg G HELD.

GO msg 1942 at 07:00:14Z, acked. Full evidence is in commit `f76f942542`'s message and in the ledger entry
`org/critical_paths/change_management/20261009T0705Z_secclass-e60-d04-unclassified-sc1-20261009_deploy_completion.md`;
this log does not restate it. The three things worth carrying forward:

1. **The ship is served and clean.** `code/gold/D_04.client_portal_summary.py` moved `816a77e9` -> `23d2f2ae`
   at VersionId `In6p3j24Ok0Vyi3LRitAAfGi0yNgcGWq`, 07:07:36Z. Watch set was every key under `code/gold/`,
   not the three the order names: pre=188, post=188, MOVED=1, and the one moved key is the target.
2. **A gate limb was unresolved and is now resolved.** safe-deploy's OPEN-DEPLOY limb read `not clear` on a
   worktree a foreign drain had just removed; WARN mode let the ship proceed. Measured rather than absorbed:
   38 live worktrees, 0 unreadable, 0 sentinels naming this surface. Row `MDPF_SECCLASS-D1-S22`.
3. **Leg G is the only thing open**, held on a named event, with the apply legs proven and the world
   consistent.

## WHAT A SUCCESSOR DOES, and nothing before it

The hold releases on ONE event: the next BD gold run's D_04 writes
`s3://opal-data-bd/platinum/firm/mix_summary.json` at a VersionId newer than the reference
`lp8kKqX7WixODLx.y23rnauYiUg6s8HS`. Carriers, measured: `bd-gold-nightly-fallback` `cron(0 23 ? * MON-SAT *)`
(2026-10-09 is a Friday, so 23:00Z tonight), or the event-driven `bd-49f-session-complete` chain off
`bd-49f-session-daily` `cron(0 0 * * ? *)`, which is what launched the 04:00:46Z run. Either arms it. This
leg waits on a RUN and never on another act by this seat -- do not re-ship anything.

Then, in order:

1. `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R13_CHECKS/e60_mix_verify.py` must read
   `E60-MIX ok=True`. The recorded base is `ok=False served=lp8kKqX7... newer=False
   extra=['other', 'unclassified'] pct_sum=0.999999936 composition_same=True`, re-read post-ship at 07:0xZ and
   still reading that, so the discriminator must move on three counts at once (newer, no extras, ok).
2. Grade CTO condition 2's three arms explicitly, because AC1 alone is not all three: the top-level `mix` is
   the six canonical classes plus AT MOST ONE `Unclassified` line with pcts summing to 1.0 within 1e-9;
   `composition` byte-equal in CONTENT to `lp8kKqX7`'s; and no lower-case `unclassified` or `other` key left
   at the top level. Branch A was signed on $998,634.78 outside the six, all in C_06's lower-case
   `unclassified`, with `other` at $0.00 -- so expect one line of about $998.6K, about 0.05 pct.
3. **A miss on ANY arm rolls back BOTH keys, not just the code key** (CTO condition 2, and the reason the
   mix_summary VersionId is in the ledger at all): code key back to VersionId
   `Mu1tZXWFwKEKDLBkmRcfhBq04GXNoAVh`, `mix_summary.json` back to `lp8kKqX7WixODLx.y23rnauYiUg6s8HS` by
   copying that version as the newest. No delete, either key.
4. Release the hold (`deploy_ledger.py hold --slug secclass-e60-d04-unclassified-sc1-20261009 --release`),
   close leg G, close the entry, write the proof instance (AC1, cell SC-e-60, decomp
   `MDPF_SECCLASS_DECOMP_R10.md`), flip the order `complete`, and send the ONE report to `2.0.0_SA_COO~M1`
   that the order's `<report>` block specifies -- it is still owed and must not be sent before the close.
5. For the proof instance's `kind`: this one IS an `s3_object`, so row `MDPF_SECCLASS-D1-S20`'s stand-in
   problem does not arise here. Pin the artifact to the real key and ETag.

Two traps already carried, and still live for the successor: once this ledger names D_04, a scheduled
box-sync pre-push may re-ship the same bytes -- that is DELTA=0, so read the ETag and never the count of
uploads (e67 class); and the BD gold suite's one pre-existing failure is row `MDPF_SECCLASS-D1-S19`, so
"suite green" is not available as a signal without naming it.

## Compiler tools

| tool | invocation | result |
|---|---|---|
| `safe-deploy.sh` | `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | gate PASS, 1 of 1 deployed and verified; printed the never-widen guarantee for the three `_shared` modules it did NOT ship. Its OPEN-DEPLOY limb read `not clear` on a vanished worktree (row S22). |
| `comp-pipescript deployed` | via safe-deploy's VERIFY limb | `VERIFY OK` on the one shipped script. |
| `deploy_ledger.py` | `open`, `close-leg V\|D`, `hold --gate-type external --reread-event` | Entry opened with 3 legs before the act, V closed BEFORE the ship (CTO condition 1), D closed after, then HELD -- reads `tracked-not-stranded` in a 20-sentinel sweep rather than blaring a half-landed RED. |
| `comp-read --enumerate` | `--enumerate 'MDPF_SECCLASS-D1-S[0-9]+' --band HEADING` | Run twice. The first said S19 was last; by the time the row was written another seat had taken S21, the append guard refused, and a re-enumerate (45 hits / 5,989 lines, 21 HEADING) minted S22. The guard is why no row was overwritten. |
| `aws events list-rules` | ENABLED rules, filtered by name | 133 ENABLED rules scanned, 2 name gold/layer; `bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *)` is the BD one. This is what made the hold's event measured rather than guessed. |
| `git worktree list --porcelain` + `ls-tree` per tree | the NEVER-2 union | 38 worktrees, 0 unreadable, 63 distinct sentinels, 42 worktree-branch-only, 0 naming this surface. |

## Push state

- `f76f942542` ship(e60b) -- **LOCAL** at the time of writing; origin `box/dell1` @`3e4a3244d0` by `ls-remote`
  at 07:18:07Z. This lane does not push a shared branch; `box-sync` carries it.
- `21607cc707` (e71b close) and `6c31e1d248` (e71b log) -- **ON ORIGIN**, same read.

## AMENDMENT (2026-10-09 ~11:3xZ) -- step 2's arm 2 above is SUPERSEDED; read this before grading leg G

The guidance in "WHAT A SUCCESSOR DOES" step 2 said arm 2 requires `composition` **byte-equal** to
`lp8kKqX7`'s. That is no longer the condition, and acting on it would roll back a correct change.

After this seat shipped SC-e-79 at 09:54:21Z (@270a5b9796) and reported that e60b leg G and e79b leg G grade
off the SAME fire, `2.0.0_SA_COO~M1` took it to the CTO (msg 2236) and `1.0.0_SA_CTO~DELL1` amended the half:
**ADDENDUM 1 @6cf7e1a36b**, in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_SECCLASS_SC_E60_D04_UNCLASSIFIED_20261009.md`. Read it at
HEAD, not from this summary.

- **Arm 2 now reads:** `composition` differs from `lp8kKqX7` ONLY in the `unclassified`, `equity` and
  `fixed_income` moves that e79's leg G accounts for (the 23 securities and their dollars, as e79's G prints
  them). Every other class equal. **Any other difference still rolls back both e60 keys.**
- **Arms 1 and 3 are unchanged**: the top-level mix is the six plus at most one `Unclassified` line summing to
  1.0, and no lower-case `unclassified` or `other` key.
- **ORDER OF READING IS NOW FIXED: e79's leg G is read FIRST**, because arm 2 depends on what it accounts for.
  Both are read from the same fire.
- The addendum also records that the e83-first sequence held: e79 shipped after e83 was written and read back
  (@bfabe0002d).

Two numbers in the segment above also move, and they were predictions rather than acceptance arms: the
`Unclassified` line will read about **$32,349.78**, not the about $998.6K e60's branch A predicted, because
e79's 23 securities ($966,285) leave `unclassified` in the same fire; and `composition.unclassified` (today
count 57, market_value 1,367,818.78) necessarily moves. Arms 1 and 3 are indifferent to both.

**Still true, and still the trap:** e60's AC1 returns `ok=True` regardless, because
`ok = newer and not extra and abs(pct_sum-1.0) <= 1e-9` and `composition_same` is printed but **excluded**
from it (`e60_mix_verify.py:36`). So AC1's rc cannot grade arm 2 in either its original or its amended form.
Grade arm 2 by reading the served `composition` against `lp8kKqX7`'s and against e79's leg-G accounting.
