gate-2(CVO~B): the (source_digest, fold_mode) key VERIFIED 6/6 -- but gate-2 STAYS OPEN on 3 residuals, one of which is a FAIL-OPEN inside the fix itself

KEY VERIFIED (harness: aor_r182_key_verify.py, hermetic, real lib, uncommitted working-tree). Each arm in its own
process (fold_mode() reads AOR_FOLD_ACTIVE at import):

  A1 artifact ABSENT                                    -> RAISED   ok
  A2 PRE-8.2 artifact (not self-describing)             -> RAISED   ok
  A3 MODE mismatch (FOLDED artifact, switch-OFF run)    -> RAISED   ok   <== THE DEFECT. The arm that killed it clears it.
  A4 DIGEST mismatch (partition REWRITTEN in place)     -> RAISED   ok   <== the 6/69 hazard; no other key saw it
  A5 LEGIT CACHE REUSE (same content+mode, no resolver) -> RETURNED ok   <== NON-PLACEBO: `--single INF_D_00c` still works
  A6 fresh servicing-only under OFF (control)           -> RETURNED ok   <== serves peter_lee (servicing), correct DELTA-0

A5+A6 are the controls that matter: the guard is a DISCRIMINATOR, not a brick. It does not over-condemn, so it will
not be disabled at 3am by the operator it condemns.

BUT GATE-2 DOES NOT CLOSE. Three residuals, all source-confirmed in the working tree:

R-A [FAIL-OPEN -- the sharpest, and it is INSIDE the new mechanism] source_digest() HEADs THE PIN, NOT THE PARTITION
THE LOADER ACTUALLY READ. aor_resolution.py:135-136 builds the key from run_as_of() (the pinned as-of), but
_load_latest_accounts_v2 WALKS BACK (inflection_rep_scope.py:272 -- "all candidates in the walk-back window"). If the
pinned partition is present-but-unusable and the loader walks back to P-1, the resolver STAMPS THE DIGEST OF P WHILE
THE FOLD WAS DERIVED FROM P-1. The stamp then names bytes the resolution was NOT derived from -- a FALSE IDENTITY.
And the failure DIRECTION is fail-OPEN: a later run pinning P finds stamped==expected, PASSES, and serves a resolution
derived from a different partition than it claims. The content-identity guarantee is void exactly in the walk-back case.
FIX: stamp the digest of the object the loader ACTUALLY READ (have the loader return it), and assert the resolver's
stamp against the dispatch's pin ONCE, at resolver time. Do not derive the digest from the pin independently.

R-B [FAIL-OPEN, latent -- base CVO's, and it is material] THE CODE IS A THIRD INPUT AND NOTHING COVERS IT.
resolution == f(source_content, fold_mode, THE CODE). code_digest references in the lib: 0 (measured). A resolver-lib
deploy lands mid-day; a resolverless run (--single/--from/group chain) then consumes the leftover artifact; ETag matches,
fold_mode matches -> the guard PASSES on a resolution computed by RETIRED LOGIC. This is our class a FOURTH time, and it
is not academic tonight -- aor_resolution.py has changed three times in the last hour. FIX: stamp a code digest too
(the lib is S3-synced, so it has an ETag). (source_digest, fold_mode, code_digest) = a digest of EVERY input.

R-C [correctness + cost] load_resolution() calls source_digest(s3) at :423 -> a LIVE S3 HEAD ON EVERY CALL, and it is
called INSIDE per-snapshot / per-leaderboard / 32-worker loops (B_00:734, D_00c:451 -- this is gate-1's F6). Two
consequences: a live HEAD per worker, and MID-CHAIN NONDETERMINISM (a partition rewritten mid-chain makes consumer A
pass and consumer B raise in the SAME run). FIX: the dispatch pins the expected digest ONCE at chain start and exports
it (exactly as it does INF_AOR_ASOF); consumers compare against the pin, never re-HEAD.

AND THE ORDERING POINT I NOW ENDORSE (base CVO's, and it changes the design pressure): every key we have proposed
tonight exists to answer "is this LEFTOVER artifact safe to reuse?" -- a question that ONLY ARISES BECAUSE A CHAIN CAN
RUN WITHOUT THE RESOLVER. The chain-wiring is not a precondition for the guard; THE CHAIN-WIRING IS THE FIX, and the
guard is defense-in-depth for the paths that can still skip it (--single, --from, operator bypass). R5's presence-gating
into CHAIN_INCREMENTAL (:429) and CHAIN_GOLD_A (:430) is therefore the load-bearing change, and I have verified those
literals now carry the resolver. Corollary: once no LEGITIMATE resolverless run exists, over-condemnation costs almost
nothing -- so ship the STRICTEST key you can build. Do not trade the key against the wiring; we spent the night
discovering that every key alone has a hole, because we kept asking a guard to do a wiring job.

VINTAGE WARNING: all of the above is against the UNCOMMITTED working tree. The lib moved under me THREE times tonight
(my citations went stale mid-analysis twice). I will RE-RUN the full matrix at DS's committed hash and will not sign
gate-2 off an uncommitted tree.

GATE-2 OPEN. WITHHELD. Nothing served; switch OFF; SERVE-HELD.
