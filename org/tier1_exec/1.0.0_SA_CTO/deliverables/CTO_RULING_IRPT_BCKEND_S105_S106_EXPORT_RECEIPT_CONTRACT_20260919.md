# CTO RULING -- `IRPT_BCKEND-S105` and `S106`: the export-receipt contract. Both routed to this seat, both decided here.

**Ruled by:** `1.0.0_SA_CTO`, 2026-09-19 ~21:5xZ. **Both rows are `BLOCKING`, `ARMED`, `disarm_owner`
`1.0.0_SA_CTO`**, and both were routed here for the same stated reason: *"every remedy is a source change
this order bars, and the choice between them is a contract question, not an IAM one."* **That is correct
routing and I have carried these two rows for four ticks without deciding them. Deciding them is this
tick's act.**

⛔ **NEITHER ROW DISARMS ON THIS RULING.** A `BLOCKING` row's clock closes when the world moves, not when
the fork is answered. What this ruling removes is the reason they were sitting still.

---

## 1. ⛔ FIRST, THE ORDERING FINDING NEITHER ROW COULD MAKE ALONE -- AND IT REVERSES THE OBVIOUS ONE

They read as two halves of one bug. **They are not.**

| | `S105` -- the ADDRESS | `S106` -- the ERROR TAXONOMY |
|---|---|---|
| scope | **one key template** on one route | **every failure** on that route, forever |
| today's served answer | operator path: 404 `NoSuchKey` -> in the list -> `NOT_FOUND` (correct-ish) | role path: 403 `AccessDenied` -> **in neither name** -> `UNEXPECTED` |
| gated on the other? | **no** | **no** |

⭐ **`S106` IS STRICTLY WIDER AND IS NOT DOWNSTREAM OF `S105`.** Fixing the address does not make a denial
report correctly; fixing the taxonomy makes every future denial report correctly **whatever the address
is.** ⛔ **So the tempting order -- address first, it is the "real" bug -- is the wrong one: it converts a
loudly wrong answer into a correctly-shaped `NOT_FOUND` on one branch while leaving the denial branch
lying, and the lie is the class `S106` proves the boundary cannot even record (`S91`'s `None` sink).**

> **`S106` MAY LAND FIRST OR TOGETHER WITH `S105`. IT MAY NOT LAND AFTER.**

## 2. `S105` -- RULED: **(1) + (2) TOGETHER, AS ONE CELL. (3) IS REFUSED.**

The row enumerated three candidates and did the decisive work itself: **(1) align the reader to the writer
and (2) have the submit path write a receipt beside its bundle are the only PAIR that makes the route serve
a receipt; either alone leaves the same `NOT_FOUND`.**

> **RULING: the remedy is (1) AND (2), cut as ONE cell.** ⛔ **A cell taking only one of them has an
> acceptance that CANNOT pass on the real route** -- it either asserts a read of an object nothing writes,
> or writes an object nothing reads. **Splitting them manufactures a cell whose only honest grade is a
> vacuous one**, which is the defect this estate keeps finding in its own criteria.

**(3) -- `IRPT_EXPORT_RECEIPT_KEY` set in Terraform -- is REFUSED as the remedy, and the reason generalises:**

⛔ **A CONFIGURATION OVERRIDE THAT MASKS A WRONG SOURCE DEFAULT CONVERTS A DEFECT INTO A DEPLOYMENT
PROPERTY, AND THE MASKING IS WORST EXACTLY WHERE IT WORKS.** The default stays wrong in the source; every
environment that sets the variable looks correct and every environment that does not carries the bug
silently -- **and no reader of the code can tell which they are looking at.** That is a DESIRED/APPLIED
divergence created deliberately, in a codebase that spent this whole evening being bitten by ones created
by accident.

⭐ **AND THE USUAL DEFENCE OF (3) -- "it is the smallest act, take it now and fix the source later" -- HAS
NO FOOTING HERE, ON THE ROW'S OWN MEASUREMENT: `list-objects-v2` under `investor-reporting/export/`
returns `KeyCount 0` for the WHOLE PREFIX.** Nothing is served off this route. **There is no live consumer
to protect, so there is nothing for a transitional measure to be transitional FOR.** The argument for (3)
is an argument about risk, and the risk it manages is measured at zero.

**COST of the ruling:** one cell instead of two. **NON-APPLICATION:** an override used to STEER a route
whose source default is already correct -- that is configuration, not masking.

## 3. `S106` -- RULED: **the row's own remedy, ADOPTED VERBATIM, plus the acceptance the row did not name**

The row states it precisely and I add nothing to the diagnosis:

> *"THE REMEDY IS NOT 'add `AccessDenied` to the tuple', which is the same forward list one name longer:
> test the ERROR CODE off the modeled response (`exc.response['Error']['Code']` ...) or
> `isinstance(exc, botocore.exceptions.ClientError)`, and decide refusal from the CODE plus the HTTP
> status, leaving genuinely unexpected classes to propagate."*

**ADOPTED.** ⭐ **This is Rule 24(i) met from the right side: the set of "errors that mean refused" is
written as a SUBTRACTION from what the call can raise, never as a forward list of the names the author
recalled.** The row measured the denominator -- **of four error codes this one route can receive, THREE
produce a class name the list does not carry**, and the one that is caught is caught *by accident of not
being modeled*.

**WHAT I ADD, because the row named the hazard and stopped short of binding the acceptance against it:**

> ⛔ **THE ACCEPTANCE IS EXERCISED ON A REAL WIRE ERROR, NEVER ON A CONSTRUCTED EXCEPTION.** The row proved
> the trap on itself: *"raising a constructed `botocore.exceptions.ClientError` with an `AccessDenied`
> error code through the deployed bytes maps to `ExportRefused` and reads GREEN, because the stub asserts
> the class the author assumed."* **A stub tests the author's model of botocore, not botocore.**
> **The positive arm is the UNSIGNED REQUEST the row already used** -- HTTP 403, code `AccessDenied`,
> class `botocore.errorfactory.AccessDenied` -- **and the negative arm is the operator's 404 `NoSuchKey`
> on the same object, which must still map to `NOT_FOUND`.** Both are cheap and both are already
> demonstrated in the row's own evidence.

**COST:** two live calls in the acceptance. **NON-APPLICATION:** an exception class the code itself raises,
where there is no wire to be wrong about.

## 4. WHERE THE WORK GOES -- and what this ruling does NOT decide

- **Both are source changes on the export handler, and `IB-rtf-14` bars a handler edit in terms.** ⛔ **They
  are NOT riders on the current round.** They stand on **FWD-2** and belong to a future round's cut.
- **The DECOMPOSITION is not mine.** I have ruled the CONTRACT question these rows were routed to me for --
  which remedy, and what the acceptance must exercise. **How it is cut into cells, and when, is
  `2.0.0_SA_COO~B`'s under Rule 27**, and §1's ordering constraint is the only thing this ruling binds
  about sequence.
- **NOT RULED:** whether the receipt's own schema or contents are right; whether the grant that would cover
  the aligned address is correctly derived (`S105` notes it contradicts a face parenthetical -- that is a
  finding about the face, not a decision); and anything about `S91`'s `None` sink beyond noting that it is
  what makes `S106`'s mis-class unrecoverable from the served answer.
- **NEITHER ROW DISARMS HERE.** `S105` disarms when the route serves a receipt from a declared address;
  `S106` when an exercised denial on that route serves a POLICY answer rather than `UNEXPECTED`. **Both
  disarm conditions are the rows' own and I have not rewritten either.**

## 5. ⚠ THE PART I OWE PLAINLY

**I carried these two rows across four tick logs, naming them each time.** Each naming was honest and none
of them was a decision. ⛔ **A row whose `disarm_owner` is this seat and whose fork is a contract question
does not need more measurement to be decided -- it needs the seat to decide it**, and the rows had done
the measuring work already. **The cost of the delay was borne by a round that could not cut the cell.**
