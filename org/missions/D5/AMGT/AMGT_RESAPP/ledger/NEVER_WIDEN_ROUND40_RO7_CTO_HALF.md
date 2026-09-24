# NEVER-WIDEN SIGN-OFF -- CTO HALF -- AMGT_RESAPP round 40, AMGT-ro-7 (the served acts)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-09-24 ~21:0xZ. **Requested by:** `2.0.0_SA_COO~Z` (msg 25748).
**COO half:** `deliverables/2.0.0_SA_COO~Z/round40/NEVER_WIDEN_HALF_COO_RO7.md`, signed at its bytes.
**Order:** `task-orders/AMGT_RESAPP.TO-AMGT-ro-7.the-served-acts.md`, `<risk>WORLD</risk>`.
Independent read, not a countersignature. Pure ASCII.

**Placement, applied prospectively.** This half is its own file under `ledger/` (lane `ANY`) rather than an
append into the issuer's `deliverables/` folder, which is lane `TREE_DELIVERABLES` and writable only by the
serial in the path. That was learned an hour ago by being REFUSED on the `AMGT_CORPUS` pair; it is not
re-discovered here.

## 1. WRITER CENSUS -- the property with the widest blast radius, re-counted on a different instrument

The COO half prints **N = 3**, one per property. This half re-counted the one whose act rewrites SERVED
objects for every name -- the peers pool -- using the PREFIX rather than the function name:

`comp-find 'peers/v1|PEERS_PREFIX' lib` -> **26 hits across 322 files, FOUR modules defining the prefix**,
where the COO half names one writer:

| module | what it does with `peers/v1/` | writer? |
|---|---|---|
| `lib/research/peers/engine.py:76` | `client.put_object` (`:1146`), `write_pool_object` (`:1303`) | **YES -- this act** |
| `lib/research/api/scoped_amgt.py:170` | `read_pool_object(PEERS_PREFIX, ...)` (`:1305`) | no -- reader |
| `lib/research/posture/comparable.py:39` | no write verb anywhere in the file | no -- reader |
| `lib/research/scores/run_scores.py:71` | **calls `crosswalk.write_pool` (`:231`)** -- but on `pool_key = SCORES_PREFIX + ...` (`:227`), i.e. `scores/v1/`; its `PEERS_PREFIX` builds a READ base at `:121` | no -- writes a DIFFERENT key |

**N = 1 for the peers/v1 objects CONFIRMED, on a net four times wider than the one that produced it.**
`run_scores.py` is the near miss worth recording: it holds the peers prefix AND calls the shared put helper,
so a census keyed on either signal alone would have flagged it, and only reading which KEY it composes
settles that it writes `scores/v1/`. **Holding a prefix and calling a put helper are each necessary and
neither is sufficient** -- the key the call composes is the only test.

Properties 1 and 2 (the rich export body, the thesis payload) are ADOPTED from the COO half's count rather
than re-derived: both are code paths inside the single function act B deploys, and act B's blast radius is
already stated at its widest -- every one of that function's 16 routes. Stated as adopted, not measured here.

## 2. BLAST RADIUS -- adopted, with the load-bearing properties named

Acts A, B and C of the COO half are adopted as written. What carries the safety:

- **A** is ONE artifact object in a versioned bucket; the prior VersionId stays and a re-point is a COPY of
  the prior version, **never a delete**.
- **B** is ONE `safe-apply` moving ONLY that function's code. **Its expected outcomes are read from each
  producer's own rule and BOTH branches are covered**, including the honest one: `/print` default pdf **MAY**
  change where the thesis section reads the verdict -- *stated, not promised equal*. A half that promised
  equality there would be predicting from the input's shape, which NEVER-1 forbids.
- **C** writes **NEW partitions only** -- `peers/v1/<key>/<write_as_of>.json`, which sorts after every
  existing one, so **no existing object is overwritten and no delete occurs**; rollback is a later-sorting
  partition written by the engine at the pre-`rn-2` commit.
- The STOP conditions are real and are the issuer's: B stops if the closure diff touches a route this half
  does not name; C stops if the batch count differs from the pre-run census.

## 3. THE EGRESS LIMB -- declared, and signed with its reasoning stated

The COO half declares that `build-and-upload-scoped-amgt.sh` **pip-downloads pinned wheels from PyPI**, an
egress off Opal infrastructure, limited to that script's own pins.

**Signed.** This is a BUILD DEPENDENCY FETCH against pinned versions, not a vendor DATA API call: it returns
no Opal-relevant data, reads no firm information, and its egress surface is fixed by the pins in the script.
It is also **the same script that ran today under `rm-7`'s deploy**, inside that leg's own NEVER-2 ledger
entry -- so this is a repeat of an exercised path rather than a new reachable state.
**Distinguished deliberately from the `AMGT_CORPUS` fire's vendor limb, which this seat HELD the same hour:**
there the act makes up to 40 **Bloomberg reference calls** returning firm data, which is squarely the class
CLAUDE.md reserves to Andrew's per-use word. A pinned-wheel build fetch is not that class, and conflating
them would make the vendor rule unusable rather than stronger.

## 4. THE ACT'S PURPOSE NUMBER, AND WHAT THIS HALF EXPECTS TO SEE MOVE

`ro-7` exists so the served objects carry `rn-2`'s units. The discriminator after C is therefore not "the
batch ran" but **the served P/E**: `Z-S269` measured, on the DEPLOYED surface at 20:25Z with Andrew signed
in, that the Peers table reads `not carried` under P/E 2025 and P/E 2026 for every member while Mkt Cap
carries values. **After this act those columns must carry numbers, and the issuer's own
`P/E x yield = 100` relation -- which round 40 adopts in place of the magnitude band this seat ruled in
round 39, because a band of [0.5,200] passes a raw percent yield -- is the check that they are the RIGHT
numbers.** A post-act read that leaves them `not carried` means C did not reach the objects the page reads,
and that is a finding rather than a retry.

## 5. PRECONDITIONS CARRIED FROM THE COO HALF

`_harvest_prefixes.py` restamped if `gen_harvest_prefixes.py --check` reads rc 1 (it did at the cut); ro-1
and ro-3 merged on CLOUD before C; a NEVER-2 ledger entry opened before the apply and closed at completion.

**SIGNED. `ro-7` may run at these bytes once ro-1 and ro-3 are merged.**

Signed: `1.0.0_SA_CTO~Z`, 2026-09-24 ~21:0xZ.
