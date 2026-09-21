# AMGT_RESAPP round 16 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** HEAD `86cdd83111` on SITEZ, LOCAL (push state UNREAD this session; LD-0522
puts the push with `0.0.0_AB_MSTR~Z`). **Written:** 2026-09-21 ~15:5xZ, after all four round-16 cells drained.

**DRAIN-END, complete:** 4 of 4 terminal, 0 open. Round 16 was issued as ONE SLUG @`ce51efce21` (decomposition s.24
+ all four orders, drafted in one parallel batch) per Andrew-direct ~15:12Z (*"You need to have all task orders
created from outset for a given round ... you write them in slugs"*, record @1e2a54bf0f), and all four workers were
spawned in one wave per Andrew-direct ~14:58Z (*"allocate broadly ... as many subagents as you reasonably can"*,
record @9bf58c4b95). **This does NOT close the project:** `rk-32` + chain P, `rk-48`'s live arm and `rk-49` stand on
their three named words, untouched by round 16.

## 1. Round state, final

| cell (slot) | drain | second instrument (this seat's own, different from the worker's) |
|---|---|---|
| rk-65 (~65) one accession-ranking rule, both readers | 87972d37f0 | own pytest run 79 passed (73 + 4 + 2 new); the CENSUS'S ORIGINAL DISAGREEMENT PROBE re-run on merged code: roster and posture batch now AGREE (`filed_names -> ['X_US_Equity']`, was `[]`) -- a behavioural end-to-end read, not the worker's unit arms |
| rk-66 (~66) wk-provision self-test scoped cleanup | 86cdd83111 | own anchored static count (body 0, whole file 0, `bash -n` rc 0); a LIVE read of the real repos after the worker's self-test run: superproject prunable 0 of 31, nested portal prunable 3 of 12 -- the 3 pre-existing entries SURVIVED (the discriminator; HEAD's self-test would have cleared them); leftover self-test branches 0/0 |
| rk-67 (~67) comp-secrets `--json --reveal` contract | e93bd1ae4f | own pytest run 8 passed; a DIFF-LEVEL read: the only removed lines in `.tools/comp-secrets` are the usage string and the misleading `--reveal` help text (every other change additive -- the default text block the one real parser reads is untouched); `collect.py` diff empty; the sentinel is the only value literal in the test file |
| rk-68 (~68) crosswalk key-shape filter | 7978f4d04f | a LIVE, read-only `load_crosswalk(refresh=True)` through the NEW code against the real pool (the worker used stubs only): 3-tuple intact, `as_of 2026-09-19`, 96 records, `loaded_from() -> s3://opal-data-harvest/crosswalk/v1/2026-09-19.json`, no key injected into the document, `resolve('BA US') -> BA_US_Equity` |

Every drain: the worktree's own `proof-of-spec-check` rc 0, diff scope checked against the order's `<paths>` (no WALL
touched in any cell), then `safe-merge.sh` with the row gate on the merged index. Worktrees removed BY NAME after all
four drained (never a prune), verified by effect: 0 worktrees, 0 branches, nested prunable still 3.

## 2. Issuer notes the L9 grade should know

- **Two criterion defects were caught AT THE CUT, before issuance** (the round-14/15 "measure before you write a number"
  lesson, applied this time instead of discovered at drain): rk-66's static check, drafted as a plain-phrase grep,
  counts **5** at HEAD (ARM6's banner, grep pattern and error echo also contain the phrase) and would have failed on
  its own lines forever -- re-cut to an ANCHORED invocation regex that counts exactly 2 at HEAD; and rk-66's AC2 was
  given a concurrency-attribution qualifier because four workers shared the repository during its run (unused in the
  event -- the census matched exactly).
- **rk-68 departs from the LETTER of the CTO's R1 ruling, on purpose, and says so in its order (s.2 ISSUER RULE):** the
  ruling said the resolved key is "recorded on the returned document"; `crosswalk.py:693-694` states the invariant
  *"The index is held BESIDE the document, never inside it: a loaded document stays byte-faithful to what it was read
  from."* The key is held beside it (`loaded_from()`), which serves the ruling's stated purpose ("so a reader can see
  which vintage answered it") without breaking the invariant or risking persistence. Surfaced to `1.0.0_SA_CTO~Z` at
  issuance for overturn; none received.
- **rk-68 was issued only after this seat pre-measured AC6 at the cut** (the live `crosswalk/v1/` prefix: 2 keys, 2
  matching, 0 non-matching) -- a loud filter that fires on a real key would break the page route at the next adapter
  redeploy. **That next redeploy carries rk-68 to the served plane; its never-widen pair must name it.**
- **The S176 prose-binding pattern was measured on all four round-16 orders** at the CTO's request (msg 23931): each
  order's only `<proof_of_spec>` is its real block, and the sweep's own `_PROOF_BLOCK_RE` sees 16 of 16 criteria; the
  same instrument on rk-58 binds the prose mention and sees 0 of 5 (positive control). Round 16's acceptance read is
  unaffected. S176-anchor itself is round 17's, as ruled.

## 3. Rows dispositioned

- **Filed by this seat this round:** `Z-S191` (disarms `W46-S2` item 2, closes `Z-S179`'s `doc-` residual -- rk-65).
  Earlier this session, found by the subtraction census: `Z-S186`-`Z-S190` (W58-S2, W39-S2, W61-S1+W49-S3, W53-S1,
  W47-S2); `Z-S185` (the round-15 analysis's grain-mixing finding, owner the CTO).
- **Closed by a round-16 cell, disarm owed by ANOTHER seat (named, not filed here):** `W54-S2` (owner `1.0.0_SA_CTO~Z`)
  -- closed by rk-68; `W60-S3` (no owner; the CVO's L9) -- its residual self-test hazard closed by rk-66, the remove
  verb was already fixed @3795d4f487; `W50-S4`'s two CLI findings -- closed by rk-67, but the row itself lives only on
  the held branch `wk-amgt-14-50` and is untouched here.
- **Workers filed no rows** (4 of 4 reported no surprise).

## 4. Findings for the round-16 analysis

1. **A census by subtraction found what a recall-shaped close missed** -- the round-15 analysis's "nothing independent
   remains" was falsified by a 26-id subtraction and seven parallel read-only drafters; the CTO banked the correction
   itself (rulings s.0). Two of the drafters also corrected THIS seat's own premise (branches 48/49 are merged, not
   held -- named by worker slot, not cell). Parallel read-only drafting is cheap and it disagrees with the author.
2. **A static check that lives inside the function it inspects must match an INVOCATION, not a phrase** (rk-66): the
   self-test's own arms quote the phrase they forbid.
3. **"Record it on the returned document" can conflict with a module's own stated invariant** (rk-68) -- a ruling that
   names WHERE a value lives should be read against the target file before it is cut.
4. **A crossed message is a timing event, not a fault** -- the CTO's fifth cell arrived after the issuance commit; it
   was surfaced the same minute and ruled to round 17 (no late order, no manufactured override).

## 5. What this seat asks of L9/L10

- Grade the 4 terminal cells on their branch-HEAD criteria (s.1); no judgment criterion was declared in any of them.
- Disposition the census s.4/s.5 rows the CTO routed to you (evidence already printed there).
- Round 16's close does NOT move TERMINALITY; the three words stand. Round 17 is S176-anchor, cut after the CTO's
  round-16 analysis (LD-0521).
