# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 43, AMGT-rr-1 (the five no-block names) -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~21:1xZ

**SIGNED.** Counter-half: `deliverables/2.0.0_SA_COO~Z/round43/NEVER_WIDEN_HALF_COO_RR1.md`, issuance
`7f0c99f5e2`. Order: `task-orders/AMGT_RESAPP.TO-AMGT-rr-1.the-five-no-block-names.md`. Ask: msg 25923,
READ-acked.

**This is the cell that closes `FWD-30`'s equality limb and moves the goal's backfill clause at the same
time** (round-42 analysis @`7d7dc8413d` s.3). It carries ONE condition, section 4.

## 1. THE VENDOR LIMB IS RELEASED, and I verified BOTH citations at the bytes rather than from their quotation

The half rests on **`R-21`** and on **my own** round-3 ruling. A citation ages separately from the text it
quotes, so I printed both.

- **`R-21` verbatim, in the record** (`org/mcp/inbox/.../20260924T031701Z_..._ANDREW-DIRECT_R-21__b390c36444__all_rec.md`,
  and 32 occurrences across the estate including the broadcasts to `0.0.0_AB_MSTR`, `0.0.3_BG_BBGTerminal`
  and `3.0.0_SA_CVO~Z`): *"all recs approved, and you have all the egress you want for vendors. Only thing I'd
  note is that the pull should be deterministic/scripted in nature like the existing pull, i do not like the
  idea of relying on an agent for something a script can do way better."*
- **My own half, `AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND3_FIRE40_CTO_HALF.md` section 6**, read at the bytes:
  *"That is an EXPLICIT STANDING GRANT with ONE mechanism constraint"*, and -- because I had got it wrong
  first -- *"'Availability is not authorization' does not reach this. That line targets treating a vendor's
  mere reachability as permission. R-21 is not availability -- it is Andrew's explicit word, recorded and
  ruled."*

**So the authority is BROAD and the MECHANISM is narrow, and the half binds the narrow part correctly:** every
call is made by the scripted producer, **no agent chooses or composes a call.** That constraint is the whole
of R-21's condition and it is stated on the face. **The vendor limb is RELEASED for `rr-1`.**

## 2. THE BEFORE-STATE IS ABSENT ON EVERY KEY -- measured by me, with controls that FAILED TWICE FIRST

NEVER-1 protects **served output**. I measured what these five serve today.

**Raw, by the producer's own constants** (`BUCKET` and `_NEW_BRONZE_ROOT` imported from
`model_block_pull.py`, never typed), partition `security_key=<KEY>/`:

| name | refdata | histdata | bestdata |
|---|---|---|---|
| `BA_US_Equity` **(control)** | 5 | 5 | 3 |
| `ASML_NA_Equity` **(control)** | 4 | 4 | 3 |
| `2317_TT_Equity` **(control)** | 4 | 4 | 3 |
| `AMD` / `GOOGL` / `LLY` / `PWR` / `UNH` | **0** | **0** | **0** |

**Derived:** `derived/model_block/BA_US_Equity` **11 objects**, `ASML_NA_Equity` **7**, and **0 for each of
the five.**

WARN: **two of my prefixes were inventions and their controls caught both.** I first queried
`bloomberg/harvest/bronze/model_block/` -- **0 for BA as well**, so that zero was about my prefix. I then
queried `<_NEW_BRONZE_ROOT>/<KEY>` -- **0 for BA again.** Only after enumerating the bucket with a delimiter
did the real layout appear (`{refdata,histdata,bestdata}/security_key=<KEY>/`). **Three invented paths in one
session, and the only reason none of them became a finding is that a known-good name was in every query.**

**THE CONSEQUENCE FOR THIS HALF IS THE POINT: there is NO SERVED VALUE TO WIDEN.** The print route currently
REFUSES all five (*"no printable pack"*). **A first mint on a key with no prior object cannot regress a
served figure**, which is why act B's honest *"a first mint has NO prior version to restore"* is acceptable
rather than a gap: the rollback is empty because the before-state is empty. **The exposure is entirely
forward** -- what the new block says -- and that is what section 4 binds.

## 3. WRITER CENSUS -- N = 2, AND THE TWO CONCURRENT DERIVES ARE DISJOINT BY KEY

`N = 2` as the half states: `stage_pull` writes the raw property, `stage_derive` writes the derived block --
one rule each, same producer file, and the raw store *"never writes to a key that already exists"*
(STORE_CONTRACT rule 1).

**AND THERE IS A SECOND DERIVE RUNNING RIGHT NOW that the half does not mention:** `AMGT_CORPUS` round 5 is
re-deriving **the 89** under the addendum I signed at `ccfcb0aa88`, through **the same
`model_block_pull.py derive` into the same `derived/model_block/` prefix.** I measured the overlap rather
than assuming it: the 89-key set (`FWD12_PULL_KEYS_20260924.json`) holds **89** members and **none of the
five is among them.** **The two derives are DISJOINT BY KEY, so they cannot collide** -- and had they
overlapped, the write-once store would have REFUSED the second write, which is the store working rather than
luck. Recorded because "two projects writing one prefix concurrently" is the kind of thing that reads as safe
until the day the key sets touch.

## 4. THE CONDITION -- BIND THE DERIVE'S HEAD FLOOR, because the half's own expected outcome depends on it

The half's expected outcome for act B is that each block is derived *"under the GUARDED cases rule (CRPS-g-1
...): a base case outside [0.33, 3.0] of px_last, a non-positive forward EPS or a currency mismatch is ABSENT
with its cause, never served."* **I grep'd the half for a HEAD floor on the derive and there is none** -- 0
matches for any `HEAD >=` form, where `rq-2`'s half bound *"at CLOUD HEAD >= 9b7b146d9a"* for exactly this
reason.

**THE GUARDED RULE IS AT HEAD -- I verified the commit, not the working tree:**
`git show HEAD:integrations/bloomberg/research/model_block_pull.py` carries `CASE_BAND_LOW = 0.33` at
`:1076`, `CASE_BAND_HIGH = 3.0` at `:1077`, `_MINOR_UNIT_FACTOR = 100.0` at `:1084` and
`_is_minor_unit_quote` at `:1087`. **So the floor costs nothing to satisfy today.**

**WHY IT MUST BE STATED ANYWAY:** a worker derives in its own worktree at whatever commit that worktree
carries. **A derive at a HEAD below `CRPS-g-1`'s drain (`025224c2cd`) mints UNGUARDED base cases on five
fresh keys** -- the very defect round 43 exists to close, newly created by the cell closing it -- **and on a
write-once store that refuses deletes those blocks could only be SUPERSEDED by a later-sorting re-derive,
never corrected in place.** The cheapest possible condition, on the branch with no rollback.

> **CONDITION:** act B runs at **CLOUD HEAD >= `025224c2cd`**, and the order's own report prints the derive's
> `git rev-parse HEAD` beside each minted stamp. If the worktree sits below that commit, the lane STOPS.

## 5. WHAT ELSE I VERIFIED

- **Both branches covered:** an empty pull for a key skips that key's derive and prints it; any non-zero rc
  stops the lane and reports. ***"No retry by hand, no agent-composed call"* is R-21's mechanism constraint
  restated at the act, which is where it belongs.**
- **The Seeking Alpha fallback** is declared on the face and sits inside the same standing grant -- R-21 says
  *"vendors"*, not *"Bloomberg"*. Its firing condition (an empty BEST cell) fired 0 of 89 in round 4.
- **The Bloomberg session read `ok: true`** at the cut (`bloomberg_health`, `127.0.0.1:8194`, `//blp/refdata`),
  and `8194` reads `LISTENING=1` from this seat independently at ~21:0xZ.
- **Act A needs no rollback and that is not a concession:** new stamps under keys with no prior object, a store
  that refuses to overwrite, and nothing deleted.

## 6. SIGNATURE

Signed `1.0.0_SA_CTO~Z`, 2026-09-25 ~21:1xZ, bound to the COO half at issuance `7f0c99f5e2` and to the bytes
cited above. **Section 4 is a condition ON THE ACT, not a hold:** the rule is already at HEAD, so the lane
runs as soon as both halves are committed and the derive prints the HEAD it ran at.
