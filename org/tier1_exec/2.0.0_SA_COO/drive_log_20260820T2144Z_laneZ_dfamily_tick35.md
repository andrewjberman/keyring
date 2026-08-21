# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T21:39–21:44Z (day tick 35)

**archetype:** VALIDATE

| Item | Class | Action |
|---|---|---|
| W-F delivery surface | **half-resolved by ruling** | channel EXCLUDED (gate's own axis); positive surface still open |
| W-D hold | ⛔ **MINE WAS OVER-BROAD** | narrowed to limb (1); gate confirmed |
| W-A | **BUILT** @81c502cff2 | received; GSI obligation folded to WC-2c @068246ed97 |

## My over-broad hold, and what it would have cost

I marked W-D **NOT BUILDABLE AS SPECIFIED** wholesale, citing a **channel** prohibition. `3.0.0_SA_CVO~Z`
caught it: **W-D is TWO ACTS ON TWO SURFACES** (the v2 record's own O8 row says so verbatim — *"one
nudge, two acts"*). The thread confirmation is a Teams post the prohibition reaches. **The SUMMARIZE
write is a field on the DDB row rendered in the CLIENT'S PORTAL and never touches Teams at all.**

⛔ **Holding limb (2) would have been actively harmful, not merely over-broad:** it is **Andrew's own
C4 requirement**, *and* it is **the mechanism behind the `superseded` exception** in the adopted
closure-reason record — the exception I had restored into W-C twenty minutes earlier after a mis-ack
nearly cost me the clause. **Hold it wholesale and the one ticket class whose client legitimately GOT
an answer is exactly the class that silently loses its answer.**

>> **A HOLD INHERITS THE SCOPE OF ITS REASON.** W-D was bundled as one workstream because the two
acts fire on **one nudge** — a **sequencing** fact, not a **surface** fact — and a surface-scoped
prohibition then read as workstream-scoped. *Same shape as "row-scoped is not field-scoped": the
bundling was right for the purpose it was made for and wrong for the purpose it was then used for.*

Narrowed with **both** falsifiers named: separability is an **engine fact I do not hold**, and limb (2)
is **not thereby cleared** (its Rule-24 row, deny-by-default scoping, and client projection all still
gate it). The gate confirmed limb-(1)-only.

## W-A: the control that mattered most is the one that failed first

**WA-6 was a real finding** — the role could not read the directory **at all** (implicitDeny, with a
separately-invoked positive control allowed). The enrichment W-A exists to deliver could not have
worked, and **only the live-primitive check would have said so.**

>> **AND THE BUILDER'S OWN STUB HAD ENCODED THE BUILDER'S OWN WRONG ASSUMPTION** — keying a fake
directory on `email` when the table is single-table PK/SK. **The battery passed 22/22 while the real
call could never have worked.** *A fixture built from the same assumption as the code cannot test
that assumption.* Rebuilt from the measured table, with the original bug re-run as a **mutant** —
a better artifact than the green run ever was.

**The two defects compounded in the same invisible direction:** wrong key shape → raises on every
claim → **swallowed by a by-design soft-fail** → permanently blank claimer names that look exactly
like *"this user has no directory record."* The IAM deny and the key defect shared one failure
signature, and neither would have surfaced as an error.

**Apply-leg sequencing recorded** because missing it converts a real grant into a false green:
WA-6's grant must be applied **before** the deployed enrichment exercise means anything, or that
exercise reads *"works, no names"* — a pass proving the opposite of what it appears to.

**GSI transferred, not deferred:** no index in W-A because the requester-keyed pattern's correct key
depends on W-C's unsettled query shape, and **a guessed index is a second home for an unspecified
pattern.** WC-2c is now the named obligation-holder: **list by scan → print the bound.**

Dispatches: 2. Gate: **PASS** — an over-broad hold of mine was narrowed before it removed a sovereign
requirement, and a built lane's findings were folded where the next builder reads them.

## Compiler Tools
None new; this tick consumed peers' live-primitive evidence (IAM simulate with a separate positive
control, describe-table, mutants) and folded it into the TOs that depend on it.
