# /self-drive D11 — tick 5 · THE R2-2 DESIGN WENT THROUGH FOUR ATTACK ROUNDS IN 50 MINUTES, AND TWO OF THE CATCHES WERE MINE TO EAT

**Driver:** `1.0.0_SA_CTO~X` · **Device:** LAPTOP · **Cadence:** 30m · **Job:** `b7128813`
**state: ARMED** · covering 22:27Z–23:48Z (tick 5 fired 22:55Z; this log is the delta-driven
one — the window carried eleven commits under this author line, so a quiet-tick skip would have
been the wrong call)

---

## SCOPE

```
D11   1 project: NFRA_SUBSTRATECARDING   status=active   dep_stage=EXECUTING
COMPLETION: NOT DONE — 0 of 1 complete   REACHABLE 1 / UNREACHABLE 0
CALLS: 0 adjudicable · 0 RESERVED · re-classed by CVO: 0 · at Andrew: 0
```

## THE WINDOW, in the order it happened

1. **R2-2 DESIGN DRAFT @1061546c63** (tick-5 act) — events are the truth, status is a projection;
   the four routed CVR2-2 findings resolved by design. Cited landing 76930-76933.
2. **CRO~X inputs 1-4 + migration receipt -> @eeb0e6ab51.** The draft's OWN denominator was wrong
   (four records; it is FIVE records / SIX axes). Field-scoped basis ruled on the bridge forcing
   case; contest events with stable ids; `retirement` kind with object forbidden; receipts on
   every rewrite.
3. **CVO~X AT-1..AT-6 -> @65ed5c07ad** (AT-3/4 convergent with CRO, already cured). Migration
   obeys the kernel's own rule (rule_derived + map ref); the one-value enum admits it is a vintage
   discriminator; the superseded_by-freezes promise DECLARED unenforced pre-WP-3.
4. **RE-1 (CVO~X, MEASURED): my disposition claimed the AT-5 split landed — the doc carried ZERO
   tokens of it.** Root cause: an unasserted `str.replace` whose target did not match a wrapped
   line no-opped silently while the script's "applied" print reported the SCRIPT's progress, not
   the FILE's state (parses-the-tool's-prose, at the fix grain). Remedy at both grains
   @c733ac9819: the six-axis two-class table landed explicitly, and every patch since is
   match-asserted (count==1 before write). Also in that commit: CRO RA-1..RA-4 (typed contest
   target — a binding cannot be named by a serial-pair relation; upheld requires its consequence;
   the per-kind direction table — the blanket subject rule RETIRED THE REPLACER on `replaces`;
   post-boundary absence is INVALID, never vintage) + exact-key status_basis maps.
5. **RA-5 (CRO~X) + CVO~X's retraction of their own early-stop dry:** my direction row said
   `canonicalized_as: NEITHER` against the live contract's semantic arm. Contract wins
   @5b15802d0f: subject retires into the canonical target. CVO's 7-of-7 sweep found nothing further.
   **CVO~X DRY @5b15802d0f (77022).** Landing checklist (8 lines, incl. the class-D flip)
   @bfcebc58c5.
6. **ARM-4 ADJUDICATED @8f8fe7db5f** — 25 of 25: 4 forbid-mirrors cut, 21 NO by class with the
   reason a future run must overcome. Then **CRO~X's re-dry caught CUT #4 over-constraining
   `unverified`** — I narrowed @c1edaf9638, CVO~X (CV-3's author) supplied the rubric (FREE = free
   of REQUIRED WARRANTS, not of forbids), and the disposition became **option (B) @05086d045c**:
   wide forbid stands with the citation the first cut lacked (§3.14's remedy column defines
   `unverified` as check-not-run), doctrine sentence fixed, THREE surfaces one commit.
7. **RUN_GATES six of six exit 0** at 8f8fe7db5f AND 05086d045c (atomic extracts); COO~X
   reproduced at 05086d045c — the first all-green run OF THE PASS, their labels gate included.
   COO-R2-1 went live on that same run: 15 open candidates ride inside "overall exit 0" — the
   count-on-the-summary-line remedy is mine as the runner's author (executing this tick).

## TWO MERGE WINDOWS inside the window (MSTR 76946/76964, then a short second): commits held at
OPEN, resumed at CLOSE; origin/CLOUD @f201b50307 at last read. One instrument slip of mine: a
stray `cat > /tmp/x` in a compound command blocked on stdin and timed the commits out — the
message files never got written; re-cut clean. Trivial, named because it cost a re-run.

## OPEN AT ANDREW: **0** · verdicts this window: 0 (all seat-level attack/disposition traffic)

## Compiler Tools

| tool | result | note |
|---|---|---|
| run_gates.sh <commit> (atomic) | PASS | 8f8fe7db5f and 05086d045c, six gates each |
| validate_isck.py --self-test | PASS | 65 -> 69 mutants, all reason+path-asserted |
| isck_coverage_probes.py | PASS | ARM-4 25 -> 21 residual, all 21 disposed by ARM4_ADJUDICATION.md |
| match-asserted python patches | PASS (after RE-1) | the instrument fix for the silent no-op class |
| git show <hash>:<path> \| grep -c | PASS | how RE-1 was CONFIRMED before I believed it |

**What failed (mine):** a silent-no-op patch that reported success (RE-1); a table row contradicting
the contract I wrote (RA-5); an uncited semantic premise in an adjudication (CUT #4). All three
caught by a second seat reading the artifact, none by me. **What worked:** every catch became a
mechanical control or a cited sentence the same turn.

**state: ARMED** · next log on delta or the 6-tick floor
