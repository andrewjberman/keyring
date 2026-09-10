# CTO WATCH -- IRPT round 1 -- signal quality of the two COO lanes' decompositions, task orders and first deliverables

**Standing:** Andrew-direct 2026-09-10 ~20:0xZ, *"silently watch COO~B (Backend) and COO~F (Frontend) as they run decomp and
TOs and critically assess the signal quality of their documents/deliverables."* Watch only; no gate, no message to either lane.
**Read at:** CLOUD `d1f613fff3` (both L4-R sign-offs present; LIMB 6 admits both PRDs on real bytes, measured this turn).
**Denominator:** 2 decompositions, 30 task orders (11 FE + 19 BK), 2 worker results, 2 surprise channels (3 + 7 rows).

## VERDICT

Both lanes cut execution documents, not governance documents. Nothing is lossy from PRD to cell to order. The two first
deliverables are the strongest worker artifacts this fabric has produced. Three residues are named below; none warrants
an intervention mid-round.

## L5 -- the decompositions

| | `IRPT_FNTEND_DECOMP.md` v0.1 @8ace3a2596 (COO~F) | `IRPT_BCKEND_DECOMP.md` v0.1.1 @261c8d2080 (COO~B) |
|---|---|---|
| carriage | 14 PRD candidates re-cut to 11 cells, map printed 14 of 14; every cell carries ACT / SERVES / CROSSES / DEPENDS / PROOF with the brief's content restated in the cell | "one carrier": the PRD row is inlined VERBATIM at L6; L5 adds only order, roots, seating, fence, battery and five findings. Non-lossy by construction |
| subtraction | three domains (8 outcomes, 14 candidates, 8 manifest rows), each printed and closed to 0 | 10 of 10 outcomes, 18 of 18 candidates; 37 edges, M=52, depth 11, acyclic |
| bounds | one BOUNDS block, inlined into every face | nine bounds, inlined verbatim into every face |
| bureaucracy | none in the cells; Rule 24 record and battery are compact and load-bearing | precedent citations (ETFS_GUARDRAIL, RULING 1) in the seating prose; harmless |

## L6 -- the task orders

- **FE (11):** WORKER FACE separated from RECORD FACE; the worker face is ~80 lines; criteria are `<criterion>` rows with the exact
  invocation and expectation; governance tokens inside the worker face: 0 to 3 per order. Judgment criteria are marked and routed
  to L9, never self-graded.
- **BK (19):** no face separation -- the whole document, including a `<preflight>` block carrying comp-schedule and comp-iam
  census numbers and "137 prose blocking fields unread", is the worker's context. That is record-face content the worker cannot
  act on. RESIDUE 1. The eleven "bounds every order carries" repeat verbatim in every order (about 1.5 KB x 19); correct, and
  the only part of a BK face a worker would be right to skim.
- **Compound criteria, BK:** each mechanical criterion is ONE battery invocation that prints ONE token when N arms hold
  (S18-AC1 five arms, S15-AC1 six). One invocation, one expectation, so it passes the cut; but a failing arm does not surface
  as its own criterion, and the arm ledger lives in the committed transcript, not in the proof instance. RESIDUE 2. The FE
  shape (one test file per criterion, `0 fail`) surfaces the failing clause by name.
- **Self-authored instruments, both lanes:** the worker writes the test and the code. Both lanes answer this the right way --
  mutants, difference controls, positive controls beside every absence verdict -- and the CVO grades the judgment rows.

## L7 -- the two deliverables that exist

- **FE-s-1** (`0.9.0_WK_IRPT_FNTEND~1`, portal `0322a04a4d`, 43 files): 6 of 6 PASS by output; three mutants FIRED; determinism
  5 of 5; a second non-incremental instrument beside the cached `tsc -b`; every count with its denominator; the 31-fixture count
  read from disk and reconciled against the manifest in both directions. Two surprise rows, both grounded at a pin.
- **IB-s-18** (`0.9.0_WK_IRPT_BCKEND~1`, `c4214773c9`): 11 schemas GENERATED from the PRD CONTRACTS table at the pin, 72 of 72
  required-meaning items carried, 384 of 384 description quotes resolved backward against the table (anti-fabrication); 11 of
  11 invalid fixtures aimed at each contract's own hazard; PATH_MANIFEST at 74 of 74 tokens with presence recorded as five
  measured states, not a boolean. Nothing deployed, 0 of 9 roots initialised.

## WHAT THE LANES FOUND THAT REACHES THE PRD (carried as rows; the CTO's L10 read answers them)

1. **`IRPT_BCKEND-S1` -- the PRD's SURFACE MANIFEST homes the directory and holdings PLATINUM in `opal-data-portal-v2`, which is
   the origin of CloudFront behavior 19 with NO auth Lambda.** The lane re-homed both to the FIRM's bucket. My read now, so
   L10 is a formality: the lane is right and the manifest row was my carriage of the brief's proposal; it also contradicts
   Andrew's own word on FWD-10 ("gated to 49 Financial buckets"). The PRD addendum lands at L10; the cells already write to the
   firm bucket, so nothing re-cuts.
2. **`IRPT_BCKEND-S2` -- routes alone are unreachable; the prefix needs a CloudFront behavior in `portal-auth`.** Real, and the
   PRD missed it. `IB-s-15` (wave 10, slot ~2, far off) will have a WORKER apply one behavior to the live portal distribution
   under a ledger with a "plan shows exactly one change or STOP" bound. A served-surface act by a worker serial; the bound is
   the right one. Flagged for Andrew's awareness, not gated.
3. **`IRPT_BCKEND-W1-S2` -- 12 of 74 PATHS tokens are unreadable from a fresh worktree:** three brand sources are gitignored
   under `deck_generation/`, nine portal files sit in the unchecked-out submodule. Bites `IB-s-14`, `IB-s-15`, `IB-s-2`, and on
   the FE side `FE-s-4` / `FE-s-11` (brand.json, the logo SVG). COO~B holds the disarm. RESIDUE 3: the PRD PATHS table did not
   carry presence-in-a-worktree, and this is the second time that shape has bitten (`.tools/terraform.exe`).
4. **`IRPT_FNTEND-W1-S1`** -- test files need ambient types the portal tsconfig excludes; solved inside the grant with type-only
   shims; COO~F assigned the disarm to `FE-s-2` by amendment at the drain. Correct handling.

## LIVE ARMS THAT WILL NEED ANDREW'S PER-USE WORD (not yet due)

`IB-s-6` the mailbox read; `IB-s-8` the YCharts login; `IB-s-9` the YCharts calls; `IB-s-11` the Black Diamond / Orion calls.
Each proves its mechanism on recorded fixtures with a difference control and carries the live arm as an express qualification
read at L10, exactly as the endpoint requires. No order waits on him.

## STATE AT THIS READ

FE: 1 of 11 complete (FE-s-1), 10 blocked on the chain, slot ~1 on FE-s-2. BK: 1 of 19 complete (IB-s-18), 3 pending as slot
heads (IB-s-1, IB-s-8, IB-s-11), 15 staged. Both issuances were cut 17:15Z-17:23Z local, before the L4-R gate landed at 17:33Z;
non-retroactive by the spine's own v3.13 rule, and both PRDs are now signed anyway.

Push state: LOCAL; Andrew holds the push.
