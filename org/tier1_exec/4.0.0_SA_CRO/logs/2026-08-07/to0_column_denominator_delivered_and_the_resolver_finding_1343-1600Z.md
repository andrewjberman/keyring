# 4.0.0_SA_CRO -- reinstantiated, held, then delivered TO-0: a column denominator with an error bar, and a finding that the binding-side headline number belongs to the resolver rather than the corpus (2026-08-07 13:43Z -> 16:00Z)

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, COORDINATE

## Window

13:43Z -> 16:00Z. Fresh-context reinstantiation. Prior log:
`coherence_base_tested_3x_routed_and_my_own_figure_refuted_0605-0735Z.md`.

## What happened

**1. Startup, and I did NOT pull.** The LD-0367/LD-0368 gate refused `git pull` on CLOUD --
integrator-only, correctly. Fetched instead: local 2 ahead / 0 behind, so nothing to pull. Flagged
the 2 unpushed predecessor commits to MSTR so they are not stranded in the integration window.
Registered, armed the Monitor (`bdus4zjn5`, confirmed `running` -- it delivered both queued messages
on arm), session-serial written, zero crons. A.3: 96/97 comp-tools resolve **and one was exercised**
(`comp-claimlink` is the miss).

**2. HELD, then released on the GO -- and the release is the part worth recording.** Andrew's 13:33Z
word via MSTR put all base seats on hold until he and base CTO set the plan. COO's 15:03Z GO cited
*today's plan* plus two base-CTO rulings from this session. That is the hold's own stop-condition met
on its terms, so I started. **Holding further would have been manufacturing a gate nobody asked for**
-- the exact class CLAUDE.md bans. I wrote the reasoning into the ACK so the authorization is
auditable rather than assumed.

**3. COO corrected a claim about me and I could confirm the negative precisely.** Base CTO's capacity
read said my TO-0 was "written but never issued." It was never written -- and from this seat I could
prove no time was lost: `to-check --all` returned 0 TOs at 13:43Z and CTO~D's 13:18Z heads-up said
explicitly that nothing starts until COO issues it.

**4. My broker summary went stale while I worked, and COO caught it.** It still read
"not issued, not started" after I had started. Fixed on the spot. **This one is mine and the failure
direction is bad**: COO plans capacity off `get_live_agents`, so a stale summary scores me idle and
invites double-booking the seat that was just dispatched.

**5. TO-0 delivered: 2,744 of 4,406 = 62.3% [95% CI 56.8-68.3]**, vintage 2026-08-07T152209Z,
pandas 2.3.3. Method = evidence extractor -> stated three-state procedure over 100% of sites ->
systematic hand audit (262 sites, first-per-file alphabetical per stratum) -> audited rate applied
to the undecidable mass with Wilson intervals. **The audit measures the procedure; it does not get to
edit it** -- folding the findings back into the rules would tune the scorer to its own eval cases
(Andrew-direct 08-06) and make the interval a fiction.

**6. THE FINDING I WENT LOOKING FOR BECAUSE THE FIRST ANSWER WAS SUSPICIOUS.** v1 gave 61.4%
undecidable. Rather than publish it I asked which claim it was -- *corpus ambiguity* or *analyzer
weakness* -- because one rate conflates two very different statements. The residue was dominated by
`gains.copy` / `merged.groupby().agg()` / `end.merge`: operations on names that ARE DataFrames but
that my fixed point never seeded. Adding parameter annotations + one-hop local return summaries
(neither is type inference; both are things the author already wrote down) moved binding reach
**9.9% -> 35.3%** and undecidable **61.4% -> 43.0%**.

> **So the binding-side headline number is a property of the RESOLVER, not the corpus: 9.9% /
> 27.6% (the PRD's spike) / 35.3% on one identical population -- a 3.6x swing.** The PRD had already
> proved the column FLOOR moves 5.5x with the marker set. **Both headline numbers are instrument
> properties, and the PRD closed only one half.** A bar of "resolve X% of columns" is unstateable
> without pinning the resolver AND the marker set.

**7. The sensitivity test cashed out, and it went AGAINST the PRD's worry.** MINIMAL 228/228 column
(clean positive control). The re-derivable band (WIDE minus MINIMAL, 836 sites) resolves at 97.1%
[85.5-99.5]. The PRD feared "not a dict method != is a DataFrame"; measured, WIDE is a good
predictor here. **`known_negative` recorded so 97.1% is not read as 100%:**
`composed["dates"].index(...)` -- `.index` is a LIST method and the marker fired on a list, once in 35.

**8. The 68 undecidables hand-read: 67 were human-decidable, exactly ONE genuinely ambiguous.** That
is the honest reading of the remaining 43% -- reachable headroom, not corpus noise.

**9. The ~507 band could not be reproduced and I said so rather than approximating it.** It is
bounded by `MID`, a hand-chosen marker set that no longer exists (scratchpad-only, died with its
session). I substituted the re-derivable `WIDE - MINIMAL` = 836, a **superset**, so the census
strictly dominates the one requested.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | "how do I find python subscript call sites in gold scripts" | **COVERAGE GAP** | routes NOWHERE -- top hit `comp-blast` (function-level). **Recorded per the TO's `if_mismatch`, not worked around.** Its footer also still advertises `comp-grep`/`comp-glob`, so the Rule-21 repoint has not reached it |
| `comp-which` | "what consumes the NFRA_PYFIELD column denominator" | near-tie, orientation only | no blast radius: this TO writes zero production code |
| `comp-find` | `"\[['\"]" data/inf/scripts/gold data/assets/scripts/gold` | 4,336 LINE hits | used per the base-CTO ruling. **Different grain from my 4,897 NODE count** -- reported as a unit difference, not a disagreement |
| `comp-estate --definitions` | ratified term registry | 51 terms | `column`/`field`/`subscript` NOT ratified (no re-coin conflict), but `denominator_grain`, `boundary_declaration`, `known_negative` ARE -- **adopted rather than re-coined** (BUILD LADDER rung 2) |
| `commit-gate.sh` | 3 .py files | BLOCKED x3, then PASS | ambiguous `l`, two placeholder-less f-strings, and strict-utf8 `.jsonl` reads. **All fixed, none overridden**; numbers verified identical after every edit |
| `safe-commit.sh` | 1 commit, `-F` | PASS @7a5be4b4c7 | risk-reflex CLEAN with its denominator printed (8 files vs 1,659 danger nodes) |
| probe `--self-test` | 19 assertions | 19/19 | incl. a **mutant** (empty constructor set -> axis goes dark), a negative control, and **both directions** of the v1/v2 split |

**What worked:** refusing to publish 61.4% undecidable before asking whether it was the corpus or me
-- that one question produced the session's main finding. And enumerating **all 33** definitions of
`_read_s3`/`_read_s3_parquet` instead of the 3 I had read, before resting 219 sites on them.
**What failed:** my broker summary went stale while I worked and a peer had to catch it. Also my
self-test's very first assertion was wrong (expected 8 subscripts in a 6-subscript fixture) --
recorded in the file rather than quietly corrected, since the fixture count is the one number
nothing else cross-checks.
**Gap found:** `comp-which` has no route for python call-site search (above).

## Blockers

**None at me.** At **Andrew**, unchanged and untouched by today: whether my reading of the
atom_decomp proceed-condition stands. Nothing depends on it and it unwinds cleanly if reversed.

## Current State (zero-context handoff)

- **TO-0 COMPLETE** @7a5be4b4c7 -- status flipped, deliverable + 3 scripts + 4,897 per-site records
  + 68 hand adjudications committed. **Unpushed** (lanes commit, integrators push).
- **Next at this seat, per COO's sequencing:** C3.ii generation strategy arrives as its own TO;
  `4.0.0_SA_CRO~A` spawns separately for the ATOM_DECOMP audit; RCG cycle-4 still live.
  **TO-0 was first and alone and it is done.**
- **Cheapest open check on my own work:** a second seat re-deriving one stratum. My procedure and my
  audit are both mine, so the intervals do not cover a shared blind spot.
