# AMGT_RESAPP.TO-AMGT-rd-7 -- THE STARRED WATCHLIST: shared across the firm, keyed PER-FIRM not per-user, and a PURE MARKER that triggers no refresh and queues no harvester

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~2</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, row S16, FWD-15)

```
AMGT-rd-7. THE STARRED WATCHLIST. Starring a security is SHARED ACROSS THE FIRM -- both PMs see the same
starred names -- and is keyed PER-FIRM, NOT per-user. Andrew ruled this 2026-09-11 and it is REVERSIBLE to
per-user on his word, so the key should make that reversal a change of key rather than a rewrite.

STARRING IS A PURE MARKER. It triggers NO refresh and queues NO harvester. Refresh is its own explicit
action. This is the sharp edge of the cell: the intuitive design -- "star a name and we start following
it" -- is exactly what Andrew's constraint forbids, because it turns a cheap UI gesture into unbounded
vendor egress that nobody authorized per-use. YOU MUST PROVE THE TWO ARE NOT WIRED TOGETHER, not merely
refrain from wiring them.

WHAT TO PRODUCE, under lib/research/ + the persistence AMGT-rd-2 landed +
.../deliverables/0.9.0_WK_AMGT_RESAPP~2/:

  (a) THE PER-FIRM STORE  starred state persisted keyed by FIRM, so two PMs at one firm see one list.
      Not per-user, and not global across firms.

  (b) THE MARKER SEMANTICS  star and unstar mutate only the marker. No refresh is triggered, no harvester
      is queued, no vendor call is made, directly or transitively.

  (c) THE NON-WIRING PROOF  a test that STARS a name and asserts that NOTHING downstream fired -- no
      harvest enqueued, no refresh invoked, no vendor request issued. A test that only asserts the star
      was stored does NOT satisfy this; the absence of the side effect is the thing being proven.
```

## DEPENDENCIES

**DEPENDS ON `AMGT-rd-2` (the metrics store)** for its persistence surface. Worked in slot ~2's queue after
`AMGT-rd-2` lands; independent of `AMGT-rd-5` and `AMGT-rd-6`.

## BOUNDS

```
BLOCK PER-FIRM, NOT PER-USER. Both PMs at a firm share one starred list. Key it so reversing to per-user
  is a key change, not a rewrite -- Andrew reserved that reversal.
BLOCK PURE MARKER. Starring triggers NO refresh and queues NO harvester, directly or transitively. Refresh
  is its own explicit action, built elsewhere.
BLOCK NEVER reference another firm's data from this surface -- BUCKET or KEY-PREFIX. A per-firm key is a
  tenancy boundary, not a label; a read that can see another firm's starred set is a hard stop.
BLOCK NO VENDOR EGRESS FROM THIS CELL AT ALL. C-VENDOR-EGRESS binds; availability is not authorization.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER. Standing moratorium.
BLOCK NO non-ASCII in code, logs or AWS.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
PRD s.3b C-STARRED-PER-FIRM (Andrew-direct 2026-09-11): "the starred watchlist is SHARED ACROSS THE FIRM
    (both PMs see the same starred names), keyed per-firm, not per-user ... reversible to per-user on his
    word. Starring is a PURE MARKER -- it triggers no refresh and queues no harvester; Refresh is its own
    explicit action."
CLAUDE.md standing law (cross-firm): NEVER reference another firm's data from a pipeline tree -- BUCKET or
    KEY-PREFIX. The mechanism is substrate-shaped and an enumerated ban list LAPSES SILENTLY when a name
    changes, so a per-firm key must be structural, not a filter applied by convention.
comp-cache collisions (at the cut): 415 of 415 portal files scanned; no AMGT key namespace exists. The
    starred read will become a query key in AMGT-rd-8 -- not your cell, but your key shape determines it.
comp-schedule --drift (at the cut): C3 = 12 standing NEVER clauses including the no-monitor moratorium.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/
infra/aws/terraform/amgt-resapp/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-7.starred-watchlist-per-firm-pure-marker.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~2/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W2-S<k>` continuing your prior sequence) and STOP on that criterion if you need a surface
not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from recall.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-7"><invocation>timeout 110 python -m pytest lib/research -q -k "starred or watchlist" 2>&amp;1 | tail -3</invocation><expect>a summary line with a passed count and no "failed" -- including a test that two DIFFERENT users at the SAME firm see the SAME starred set (per-firm sharing) and that a user at a DIFFERENT firm does NOT see it (the tenancy boundary). A suite proving only that a star persists is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-7"><invocation>timeout 110 python -m pytest lib/research -q -k "marker or no_side_effect or pure" 2>&amp;1 | tail -3</invocation><expect>a summary line with a passed count and no "failed" -- including the NON-WIRING test: starring a name fires NO refresh, enqueues NO harvester and issues NO vendor request. The assertion must be on the ABSENCE of the side effect (a spy/mock asserting not-called), not on the star having been stored. A suite without that arm is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-7"><invocation>timeout 110 comp-find "harvest|refresh|enqueue|trigger" lib/research --limit 20 2>&amp;1 | tail -12</invocation><expect>a printed denominator, and NO hit inside the starring code path that calls a harvest, refresh, enqueue or trigger -- NEGATIVE: the marker path is inert. Hits elsewhere in lib/research (the harvesters and producers legitimately contain these words) are expected and fine; a hit reachable FROM the star handler is the C-STARRED-PER-FIRM violation and is NOT met. A denominator of 0 files scanned is OUT-OF-CORPUS and is NOT met either</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-7" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, two arms): per-firm sharing holds AND the cross-firm boundary holds.
- **AC2** (mechanical, absence-of-effect): the non-wiring is proven, not merely intended.
- **AC3** (mechanical, NEGATIVE, denominator-bearing): no trigger is reachable from the star handler.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): is the per-firm key a STRUCTURAL tenancy boundary (so another firm's starred set is unreachable, not merely unfiltered), and is the marker genuinely inert -- including transitively, where a star writes a row that some other job later treats as a work queue? The transitive path is the one a direct test can miss.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED)
**Authority chain:** L10 round-4 analysis @959ba3e947 -> PRD s.3b `C-STARRED-PER-FIRM`, ANDREW-DIRECT 2026-09-11 -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13, AMGT-rd-7) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN B, slot ~2. Depends on `AMGT-rd-2`. Independent of `AMGT-rd-5` and `AMGT-rd-6`.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-7` row.
> **NOTE (2.0.0_SA_COO~ZZZ).** Andrew reserved the per-user reversal, so the key shape carries a decision he may revisit. The cell is told to make that a key change rather than a rewrite -- that is design guidance inside his constraint, not a widening of it.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers; C3 = 12 standing NEVER clauses incl. the no-monitor moratorium. BLIND: C4/C5 not decidable.
comp-iam: RUN -- 836 call(s) across 96 mapped role(s); persistence rides a role and a refused write is a finding filed as a row. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never checked, 51 GRANTED-BROAD excluded not cleared.
comp-cache: RUN -- 415 of 415 portal files; no AMGT key namespace; this cell's key shape determines AMGT-rd-8's starred query key. BLIND: declared keys only.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8). BLIND: author's stated evidence context only.
comp-blast: DECLARED-NOT-APPLICABLE -- no shared served artifact moves.
</preflight>
**Preflight disposition:** a small marker cell whose two real hazards are TENANCY (a per-firm key that is a filter rather than a boundary) and TRANSITIVE WIRING (a star row later consumed as a work queue). Both are carried as bounds, as mechanical arms, and in the judgment criterion.
