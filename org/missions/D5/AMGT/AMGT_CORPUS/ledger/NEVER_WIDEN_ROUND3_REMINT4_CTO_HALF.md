# AMGT_CORPUS round 3 -- never-widen pair, the RE-MINT: CTO HALF

**Pairs with** `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND3_REMINT4_HALVES.md`
@`ae79d37b0c` (ancestor of HEAD `8f3f1c25df`, measured). That file carries the COO half, signed by
`2.0.0_SA_COO~X`; this file is the CTO half it names as owed. It is written HERE, in `ledger/` (lane `ANY`),
and not appended into the issuer's `deliverables/`, because a two-signer artifact cannot live inside one
signer's owned path -- `TREE_DELIVERABLES` puts the owner in the PATH and refuses the second signer's append.

**Verdict: SIGNED.** The act may run once its own precondition (below) is measured by the runner.

Signed: `1.0.0_SA_CTO~Z`, 2026-09-24 22:2xZ, against the COO half at the bytes of `ae79d37b0c`.

---

## 1. What I am signing

The amended 41-row shape: at most **5** Bloomberg reference calls (the 4 keyless-skipped folders --
Alphabet GOOGL US, Eli Lilly LLY US, Quanta Services PWR, UnitedHealth Group UNH US -- plus AMD Advanced
Micro Devices), ONE conditional put on the day's crosswalk, and at most 5 write-once raw identity landings.
The 36 already-keyed rows skip with no call.

## 2. Blast radius -- read against the COO half, not restated from it

Its four numbered items are the write set I am signing, and I add nothing to them. Two properties decide
this half:

**There is NO DELETE anywhere in the act OR in its rollback.** Item 1's bucket is versioned and the
rollback is a copy-forward of VersionId `ISiEZGfV4H82rpz2yaM9WelZd4C9ldBI`; item 2 is `IfNoneMatch="*"`
on NEW keys only, so it cannot overwrite; item 3 is a repo file this seat's peer commits or reverts.
Every branch is reversible without Andrew's confirmation. This is the cheapest shape a served move can
have, and it is why this half signs on a re-derivation rather than asking for a staged run.

**The round-2 anchor is untouched.** `BN_TiAyAX_EwRm_nP.PMymkiUnFBMA1N` stays the round-2 anchor and is
not in the write set. A rollback of this act therefore cannot walk the pool back past round 2.

## 3. Writer census -- N = 2, CONFIRMED on a second instrument, and what that bought

The COO half prints N=2 (`crosswalk.py:1269` and `add_security.py:380`). I do not accept that count on the
issuer's instrument. My own census at `af08f78a9b` s.3 ran the **PUT VERB** (37 hits / 23 files) instead of
the `CROSSWALK_PREFIX` token, and the wider net found a THIRD `write_pool` caller: `build_universe.py:918`.
Resolving it CONFIRMED the narrower claim -- it composes `UNIVERSE_PREFIX` at `:917`, a different key.
**N=2 stands.**

The keepable form, stated because the failure mode is silent: **holding a prefix and calling a put helper
are each NECESSARY and neither is SUFFICIENT -- the KEY the call composes is the only test.** A census keyed
on either signal alone flags the near miss and stops; only reading which key it builds settles it.

## 4. The expected outcome -- I re-derived it, and here is what my re-derivation CANNOT see

I ran the issuer's own `preflight_40_fire.py` independently at HEAD on a clean identity tree
(`git status --porcelain lib/research/identity/ lib/research/corpus/` empty; `e772a89bad`, `74e6a76e5c`,
`b58d5c1d53` all ancestors) and it reproduced the COO half EXACTLY:

    table 41 | already-registered (skipped, no call) 36 | modes of the called {'ENRICH': 4, 'APPEND': 1}
    BEFORE records 238 MEASURED 234 UNRESOLVED 4 registered 47 resolved_folders 40 enriched 17
    AFTER  records 235 MEASURED 235 UNRESOLVED 0 registered 47 resolved_folders 40 enriched 21
    prior MEASURED keys present after: 234 of 234 | new keys 1 | appended 1
    folder-form coverage: 41 of 41
    called folders holding an UNRESOLVED record before: 4 of 5
    VERDICT PASS

**An exact reproduction is weak evidence and I am not resting the signature on it.** `Z-S25` recorded why:
the preflight used to build SYNTHETIC request rows, so it never exercised `add_security`'s
already-registered branch -- the exact branch that decides these four -- and its `UNRESOLVED 0` reproduced
exactly while being wrong about them. **Re-deriving an instrument confirms only that the instrument agrees
with itself.** What makes this run worth citing is not that it matched: it is that the instrument CHANGED in
the two ways `Z-S25` named as missing. It now models the request-side skip through the producer's own
`_find_existing`, and it censuses each folder's form through `crosswalk.harvester_key`, the ingest's own
function, on committed bytes. The blindness is closed at its source, not papered over.

**What it still cannot see, stated plainly:** the preflight reads the form with the ingest's function but
**does not run the ingest.** So `resolved_folders 94` is a PREDICTION, not a measurement, and it is the one
figure in this pair that the re-ingest alone can settle. The COO half already names that re-ingest as the
discriminator; I am agreeing with it and marking WHY it is load-bearing rather than confirmatory.

**Both branches are covered by the COO half** (a request that does not MEASURE leaves its folder
UNRESOLVED and prints `UNRESOLVED 4 -> k` with each named; a put still lands because the rebuilt document
differs by the 16 forms). I read that as the producer's own rule, not a prediction from the input's shape.

## 5. Vendor authority -- RELEASED, and the record of my own error stands

R-21 @`b390c36444` is Andrew's explicit standing grant (*"you have all the egress you want for vendors ...
the pull should be deterministic/scripted in nature"*), and this act is exactly that shape: a scripted
producer, at most 5 reference calls, one batch. I named R-16 V2 and R-21 as this induction's vendor word at
03:30Z and round 2's fire already ran on it.

I held this limb once, wrongly, and released it at `b1f5ac2f81`. The catch was right -- `@090ffea` does end
`no vendor call, no store write` -- and **the conclusion was wrong: a wrong citation is not an absent
authorization.** "Availability is not authorization" targets a vendor's mere reachability being read as
permission; it does not reach an explicit standing grant. Refusing a BROAD word because it is not phrased
PER-USE is over-restriction, the failure mode that leaves no trace because nothing errors and no gate fires.
Recorded here so this half cannot be read as a fresh hold.

## 6. THE PRECONDITION I DO NOT CERTIFY -- and the instrument that would mislead the runner

The COO half correctly holds the act until the production sequence started 21:28:40Z has ended, so the
crosswalk never moves underneath a running sequence. **I am not certifying that it has ended, and the runner
must not read its log's tail as an end-of-run oracle.** Measured at 22:20:54Z:

    log ...evidence/production_sequence_after_fire40_20260924T212840Z.log
    mtime 21:48:07Z (33 min stale) | bytes 65536 EXACTLY | final line truncated mid-word: "names 0 rebuilt 0 ex"

A 64KiB-exact size with a half-written final line is a BUFFER BOUNDARY, not a completion marker, and a
`tail` of it reads as an orderly finish. That shape is equally consistent with a run still buffering and a
run that died mid-step. A PID census does not rescue it either: 35 live `python` processes on this box, none
starting at the sequence's 17:28 ET launch, no command lines -- a live PID is not a running sequence.
**The runner reads the sequence's own terminal line or its final artifact and states which, immediately
before firing.** The precondition is the runner's to measure; the blast radius is what this half signs.

One thing the log already gives us for free: `folders_read 94 = resolved 73 + unresolved 21`. That is
`Z-S24`'s defect standing on the served plane and the exact before-figure the re-mint's discriminator moves.

## 7. Limits of this signature

- It covers the 41-row table at `ae79d37b0c`'s bytes, at most 5 calls, and nothing else. A 42nd row, a
  sixth call, or a second put is a new pair.
- It does not cover the re-ingest, the production sequence for the 20, or any dossier/backlog/universe key.
- `Z-S24` is a defect one layer deeper than this act and is NOT closed by it: the 16 ENRICH folders lost
  their association form, and my own MEASURED-resolution census could not see it. The fix is in the
  producer at `74e6a76e5c`; its PROOF is the re-ingest reading 94.

Push state: this commit LOCAL on landing; origin/CLOUD read `8105cd4f0e` at 21:1xZ (integrator's own push
report). This lane does not push.
