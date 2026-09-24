# self-drive AMGT_RESAPP -- ticks 66-70, `1.0.0_SA_CTO~Z`, 2026-09-24 ~21:2xZ

**Arming record:** `ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` @`a8a62f4f5c`.
**state: ARMED.** Covers ticks 66-70; last log tick 65 @`14f3e1b5dc` (20:09:22Z), so this lands on the
one-hour floor. ASCII detector run in its own call before the commit.

## The block in one line

The deployed surface was measured for the first time in three rounds -- with Andrew signing in -- and **both
never-widen pairs were signed**, including one where this seat held a vendor limb against its own prior
ruling and had to be corrected by the issuer it was blocking.

## Acts, with hashes

| act | hash |
|---|---|
| `Z-S269` -- item 7 OBTAINED, the deployed authenticated render | `a0ac64ad61` |
| CTO never-widen half, `AMGT_CORPUS` 40-name fire | `af08f78a9b` |
| its vendor-limb RELEASE (this seat's hold withdrawn) | `b1f5ac2f81` |
| CTO never-widen half, `AMGT_RESAPP` round 40 `ro-7` (WORLD) | `94f72e3cd4` |
| `opal_ai` park closed -- un-park fired, outcome TRANSFER | `1529508abb` |
| Law-lock merge ruling (no exemption) + the `--abort` defect | msgs 25763-25764 |

## ITEM 7 IS OBTAINED -- the finding three rounds of local grading could not produce

Andrew signed in interactively at 20:25:29Z in a headed Edge window (pattern copied from
`2.0.0_SA_COO~Z`'s own traces; scratch profile, his Work profile untouched, bearer presence recorded and its
value never read). **The deployed app is healthy where it has data**: 14 of 15 API calls 2xx, the only 401
the pre-sign-in `/auth/refresh` probe, and a genuinely polished Thesis tab with a real BCA deliveries chart.

**And the deployed Peers table carries NO P/E VALUES AT ALL** -- every member reads `not carried` under P/E
2025 and 2026, P/E 2027 is `(ABSENT)`, while Mkt Cap carries values on the same rows. Round 39's LOCAL render
after `rn-2` carries 34.70 / 21.40 / 15.03 / 27.96. **So `Z-S265`'s fix is neither confirmed nor contradicted
on the served plane -- it is UNOBSERVABLE there, and the 12-of-12 clean grid measures a data state the served
surface does not have.** Every grade in rounds 37-39 stands exactly as bounded, LOCAL, and no stronger.
Why is NOT claimed: the panel's own provenance reads `universe vintage 2026-08-06, as of 2026-09-24T0310Z`,
which predates `rn-2`; a stale artifact, a different CSC vintage and genuinely absent columns are all live.

**Two instrument findings from the same run.** `getByRole('tab')` returns ZERO -- the five tabs are plain
buttons with no ARIA role, an accessibility defect on a client-facing page. And the first Peers capture came
back **byte-identical to Exec Management** (same sha256, same 198,781 bytes) because
`getByText('Peers').first()` collides with the lead panel's non-interactive `PEERS` label. **Two screenshots
that differ to the eye cannot be told apart from two that do not without a digest** -- hashing caught it,
looking did not.

## THE VENDOR LIMB -- this seat's worst call of the session, and it blocked the goal's critical path

The `AMGT_CORPUS` fire's half cites `@090ffea` as "Andrew's word on the 40". **That catch was right**: the
record ends, verbatim, `no vendor call, no store write`. `2.0.0_SA_COO~X` accepted it and corrected the
record, and marked the stale preflight log SUPERSEDED -- both things the half asked for.

**The conclusion was wrong.** A wrong citation is not an absent authorization. This seat inferred "no word
exists" from "this citation does not carry it" -- the absence-from-one-instrument error it had convicted
itself of twice the same day -- and **the correct instrument was its own ruling**: it named `R-16 V2` and
`R-21` as this induction's vendor word at 03:30Z, and **round 2's 20-name fire already ran on it.** `R-21`
@`b390c36444` carries Andrew verbatim: *"you have all the egress you want for vendors ... the pull should be
deterministic/scripted in nature"* -- an explicit STANDING grant with one mechanism constraint, and the fire
is exactly that shape.

**"Availability is not authorization" targets a vendor's mere reachability being read as permission. It does
not reach an explicit standing grant. Refusing a BROAD word because it is not phrased PER-USE is
over-restriction -- the failure mode that leaves no trace, because nothing errors and no gate fires; the work
simply does not happen.** The per-use reading guards against WIDENING a narrow word; it was never a licence
to NARROW a broad one. Released @`b1f5ac2f81`, with the marker on s.5's own heading so a reader of that
section alone cannot take the hold as live.

## WHAT THE SECOND SIGNATURE ACTUALLY BOUGHT -- two censuses, both confirming the other seat

Both pairs' writer counts were re-run on a DIFFERENT instrument, and **both times the wider net found an
extra candidate and resolving it CONFIRMED the narrower claim**:

| pair | their instrument | this seat's | extra candidate | resolution |
|---|---|---|---|---|
| CORPUS key | `CROSSWALK_PREFIX` token | the PUT VERB (37 hits / 23 files) | `build_universe.py:918` | writes `UNIVERSE_PREFIX` (`:917`) -- different key. **N=2 stands** |
| `ro-7` peers pool | the function name | the PREFIX (26 hits, 4 modules) | `run_scores.py:231` | composes `SCORES_PREFIX` (`:227`) -- different key. **N=1 stands** |

**The keepable form: holding a prefix and calling a put helper are each NECESSARY and neither is SUFFICIENT
-- the KEY the call composes is the only test.** A census keyed on either signal alone flags the near miss;
only reading which key it builds settles it. The check pays for itself even when the half is right both
times, because the failure mode is silent.

## Two mechanism findings

1. **A TWO-SIGNER ARTIFACT CANNOT LIVE INSIDE ONE SIGNER'S OWNED PATH.** The CORPUS half invited an append
   into `deliverables/2.0.0_SA_COO~X/`, which is lane `TREE_DELIVERABLES` where "the owner is in the PATH".
   The append was REFUSED and reverted so nothing of this seat's sat uncommitted in that lane's folder. The
   working pattern is `AMGT_HARVST`'s H03 2a pair: each half its own file, the CTO's under `ledger/` (`ANY`).
   Applied prospectively for `ro-7` rather than re-discovered.
2. **THE LAW LOCK'S REFUSAL BREAKS `git merge --abort`.** Ruled: **no merge exemption** -- a merge carries a
   FOREIGN seat's edits under the MERGING seat's authorship, and CLAUDE.md 14a already records that property
   for the owned-paths merge exemption; a second such hole on the law files would make the lock decorative.
   Naming the incoming order is the intended path and `0.0.0_AB_MSTR~Z` proved it (`c167ac136c`). **But the
   defect is real and separate:** the lock appends to a TRACKED file while refusing, so `--abort` fails
   ("Entry 'org/law-edit-audit.log' not uptodate") and the refusal strands the shared tree. **This seat hit
   that exact merge** -- it is what forced a wait-then-commit at 21:1xZ. Fix routed: a merge refusal writes
   its row to an untracked sidecar; PASS rows unchanged.

## Scope state, denominators printed

| project | orders | non-terminal |
|---|---|---|
| `AMGT_RESAPP` | 221 | **7** -- round 40 cut; `ro-7` WORLD, CTO half SIGNED |
| `AMGT_CORPUS` | 22 | **0** -- round 3 FULLY DRAINED; the 40-name fire is released and may run |
| `AMGT_HARVST` | 18 | 0 -- round 6 ruled PARTIAL-shaped, queued behind `~Y` at the 3-COO cap |

Inbox 0. **New 0.8 instrument exercised** (`active-commitments.py`, Andrew-direct ~18:4xZ): 1 line across 23
ledgers, `0.7.0_AE_CloudOps~A`'s `rm-7 blocked` from 15:11:31Z -- **STALE**, since rm-7 completed and its
blockers were resolved by the face amendments. One stale line in a one-line output is the whole signal; that
lane owns clearing it. This seat carries no line of its own, which is its own gap in a new mechanism.

## COMPLETION TEST

**NOT DONE -- 0 of 3 projects `status: complete`.** Round 39 was not zero-graduation (eight items, one a
retracted outcome); round 3's fire has not run.

## Cards at Andrew

**TWO.** `org/XXX.md`'s stale double-stop (locked; awaiting his order; item 4 of that card overstated against
a reverted copy). And **ft and barrons**, whose refusals authorization cannot reach -- a 403 and a post-auth
rejection -- where his grant moved one publisher of three; `data_status COMPLETE` needs all five, which is
why round 6 is PARTIAL-shaped.

## Compiler Tools

Headed Edge via `playwright-core` `launchPersistentContext` (channel msedge, scratch profile) -- PNG digests
as the capture discriminator -- `getByRole` vs `getByText` as the collision control -- the issuer's own
`preflight_40_fire.py` re-run at HEAD -- `comp-find` by PUT VERB and by PREFIX as writer-census controls --
`resolve_lane` with a known-governed positive control -- `active-commitments.py` -- `git log` as the commit
oracle, never the tool's exit.
