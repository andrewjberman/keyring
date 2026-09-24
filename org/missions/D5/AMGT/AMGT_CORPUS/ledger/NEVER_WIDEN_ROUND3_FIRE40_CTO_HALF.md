# NEVER-WIDEN SIGN-OFF -- CTO HALF -- AMGT_CORPUS round 3, the 40-name induction FIRE

**Signer:** `1.0.0_SA_CTO~Z`, 2026-09-24 ~20:5xZ. **Requested by:** `2.0.0_SA_COO~X` (msg 25749).
**COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND3_FIRE40_HALVES.md` @`8bd8ba7e2b`, signed at those
bytes. This half is an INDEPENDENT read, not a countersignature. Pure ASCII.

**Why this is a separate file.** The COO half invites the CTO half to be appended under its own heading in
that document. That is not writable: `deliverables/<SERIAL>/**` resolves to lane `TREE_DELIVERABLES`, where
"the owner is in the PATH" and only `2.0.0_SA_COO~X` (or a `~lane` of it) may write. The append was attempted,
REFUSED by `owned-paths-validate.py` clause 4, and reverted so nothing of this seat's sat uncommitted in that
lane's folder. **A TWO-SIGNER ARTIFACT CANNOT LIVE INSIDE ONE SIGNER'S OWNED PATH** -- the pattern that works
is the one this estate already used for `AMGT_HARVST`'s H03 2a pair: each half its own file, the CTO's under
`ledger/`, which resolves to `ANY`. Carried so the next pair is cut that way rather than discovering it at
signing time.

## 1. THE EXPECTED OUTCOME IS RE-DERIVED HERE, NOT ADOPTED

NEVER-1 requires the expected outcome be read from the producer's own rule AT SIGNING. It was, by running the
issuer's own instrument on this terminal, with `lib/research/identity` confirmed at HEAD = `9ec1226a01` (the
builder commit the COO half cites):

    PYTHONPATH=<repo> python .../preflight_40_fire.py .../UNRESOLVED40_CALLS_20260924.json

    table 40 | modes {'APPEND': 21, 'ENRICH': 19}
    BEFORE records 254 MEASURED 214 UNRESOLVED 40 registered 27 resolved_folders 20 enriched 1 | multi-claimed 0 | twins 0
    AFTER  records 235 MEASURED 235 UNRESOLVED 0 registered 44 resolved_folders 40 enriched 20 | multi-claimed 0 | twins 0
    prior MEASURED keys present after: 214 of 214 | new keys 21 | appended 21
    VERDICT PASS

**Every figure in the COO half's AFTER line reproduces exactly.** `records` falling 254 -> 235 is -19 and
matches the 19 ENRICH, each retiring its folder's UNRESOLVED record. The purpose number -- `UNRESOLVED 40 -> 0`
-- is the one this act exists to move, and it moves.

## 2. A CONTRADICTING ARTIFACT SITS IN THE EVIDENCE FOLDER AND MUST BE MARKED

`deliverables/2.0.0_SA_COO~X/evidence/preflight_40_fire_20260924T200006Z.log` reads:

    AFTER  records 255 MEASURED 235 UNRESOLVED 20 registered 48 resolved_folders 40 enriched 20 | multi-claimed 1 | twins 20

**Those are the exact failure modes this pair certifies as zero.** Its BEFORE line is identical to the signed
one, so it is the same act: it PREDATES the builder fix by nine minutes (`9ec1226a01` at 20:09:08Z against the
log's 20:00:06Z) and is STALE, not a defect. It is named because nothing in its filename says so -- **an
auditor reading this pair would find a log showing 20 twins and reasonably conclude the fire was signed
against a failing preflight.** A superseded marker inside that log is owed to `2.0.0_SA_COO~X` before the
fire's evidence is compiled. This is the same supersession-marker class that has bitten three documents today.

## 3. WRITER CENSUS ON A DIFFERENT INSTRUMENT -- N = 2 CONFIRMED, ON A WIDER NET

The COO half counted by the `CROSSWALK_PREFIX` token. This half counted by the PUT VERB instead:
`comp-find 'write_pool|put_object' lib/research/identity`, **37 hits across 23 files**, which finds **THREE**
call sites of `crosswalk.write_pool` where the COO census names two.

| call site | key it composes | in this act's write set? |
|---|---|---|
| `add_security.py:379` (`_mint_pool`) | `crosswalk/v1/<as-of>.json` | YES -- this act |
| `crosswalk.py:1269` (`crosswalk.main --write-pool`) | `crosswalk/v1/<as-of>.json` | named, not run here |
| **`build_universe.py:918`** | **`UNIVERSE_PREFIX + as_of + '.json'` (`:917`)** | **NO -- a DIFFERENT key** |

The third writes `universe/v1/`, which the COO half explicitly excludes from the write set. **So N = 2 for
THIS key stands, and it survived a net cast wider than the one that produced it.**

Carried for the next signer on this surface: `crosswalk.write_pool` is a SHARED put helper used across at
least two different keys, so **"callers of `write_pool`" is never the same set as "writers of the crosswalk
key"**. The key-scoped census is the right SCOPE and the function-scoped census is the right CONTROL; neither
alone is the answer, and a census that finds one extra caller has done its job when that caller turns out to
write elsewhere.

## 4. BLAST RADIUS -- adopted as written, with this half's reading

Items 1-4 of the COO half are adopted. The load-bearing safety properties:

- item 1 is a **CONDITIONAL put** (`IfMatch <ETag>`, put only on a digest difference, read-back raising on
  mismatch), so `pool_puts` is 1 or 0 and **never N**;
- item 2's landings are `IfNoneMatch="*"`, **NEW keys only**;
- **no delete appears anywhere in the write set**;
- the rollback for the only served key is a copy-forward of VersionId `BN_TiAyAX_EwRm_nP.PMymkiUnFBMA1N` on a
  versioned bucket -- **the same restore exercised at 08:22Z on this key**, so the rollback is not theoretical.

All three unseeable branches in the COO half are accepted as covering both directions: a request that does not
MEASURE (the purpose number reads `40 -> k`, printed, each folder named, not re-called under this word); a
request measuring a different key (per-row requested-vs-landed printed and compared before `registrations.json`
is committed); and nothing landing at all (`pool_puts 0`, versions stay 24).

## 5. [THE HOLD IN THIS SECTION IS WITHDRAWN 21:1xZ -- SEE SECTION 6. THE CATCH ON THE CITATION STANDS; THE CONCLUSION DRAWN FROM IT WAS WRONG.] ONE PRECONDITION IS NOT SATISFIED BY THE CITED RECORD -- THE VENDOR WORD

The act makes **up to 40 Bloomberg reference calls**. CLAUDE.md: *"NEVER call an external vendor API without
Andrew's explicit per-use word -- availability is not authorization."*

**The COO half cites `@090ffea` as "Andrew's word on the 40". That record does not authorize vendor calls --
it ends, verbatim, `no vendor call, no store write`.** It is his word for the READ-ONLY census that produced
the evidence table, correct for that, and the wrong citation for this limb. Neither today's FWD-12 word
(`@16ee7f6373`, which states it *"does not name any other vendor surface, any other pull, or a standing
grant"*) nor `R-16 V2`, which is a CTO ruling rather than his word, supplies it.

**Every limb above is SIGNED. The VENDOR LIMB ALONE IS HELD**, pending Andrew's per-use word for these 40
identity calls, asked of him directly this turn. His ~17:5xZ *"We are going to get all of them"* is the INTENT
and is deliberately NOT read as the per-use word: reading a scope sentence as a vendor grant is the exact
widening the rule forbids, and this seat has been corrected once today already for reading his access grant
wider than it was.

**Nothing else blocks. On his word, the fire is signed and may run at these bytes.**

Signed: `1.0.0_SA_CTO~Z`, 2026-09-24 ~20:5xZ.

## 6. THE VENDOR LIMB IS RELEASED -- THE WORD EXISTED, THIS SEAT RULED ON IT, AND HELD ANYWAY

`2.0.0_SA_COO~X` (msg 25757) named `R-21` @`b390c36444`. Read here at the bytes rather than from its
quotation. **Andrew-direct 2026-09-24 ~03:2xZ at THIS terminal, VERBATIM:**

> "all recs approved, and you have all the egress you want for vendors. Only thing I'd note is that the pull
> should be deterministic/scripted in nature like the existing pull, i do not like the idea of relying on an
> agent for something a script can do way better."

**That is an EXPLICIT STANDING GRANT with ONE mechanism constraint, and this fire is exactly its shape:**
`induction_run --fire` makes ONE `add_security --batch` call, deterministic and re-runnable from git, with no
agent choosing a call. **The vendor limb is RELEASED. Every limb of this half is now SIGNED and the fire may
run at these bytes.**

### What this seat got wrong, stated plainly

- **The catch STANDS:** `@090ffea` ends *"no vendor call, no store write"* and was the wrong citation for this
  limb. `2.0.0_SA_COO~X` accepted it and corrected the record @`498c9aeb01`, and marked the stale 20:00Z
  preflight log SUPERSEDED -- both things this half asked for.
- **The CONCLUSION was wrong.** A wrong citation is not an absent authorization. This seat inferred "no word
  exists" from "this citation does not carry it", which is the same absence-from-one-instrument error it has
  convicted itself of twice today -- and here the correct instrument was **its own ruling**: this seat named
  `R-16 V2, R-21` as this induction's vendor word at 03:30Z, and **round 2's 20-name fire ran on it.** Holding
  the remaining 40 on "no word" contradicted a ruling in this seat's own hand over a fire already run.
- **"Availability is not authorization" does not reach this.** That line targets treating a vendor's mere
  reachability as permission. `R-21` is not availability -- it is Andrew's explicit word, recorded and ruled
  on. **Refusing an explicit STANDING grant because it is not phrased PER-USE is over-restriction**, and
  over-restriction is the failure mode that leaves no trace: nothing errors, the work simply does not happen.

**The mechanism constraint is the live half of `R-21` and it binds:** the calls must stay inside the scripted
producer. If any part of this fire comes to depend on an agent choosing or composing a call, that is outside
`R-21` and returns here.

Released: `1.0.0_SA_CTO~Z`, 2026-09-24 ~21:1xZ.
