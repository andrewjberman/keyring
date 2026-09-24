# Andrew-direct: the signed-in Anna test at localhost:5174 renders NOT_READY / "No source age yet"

**Channel:** the `0.0.0_AB_MSTR` terminal (laptop), 2026-09-24 ~00:5xZ.
**Recorded by:** `0.0.0_AB_MSTR`. This is the test `1.0.0_SA_CTO` asked Andrew for (rulings batch d78fdb2f1c item 3 / batch 2 item 8: "the signed-in Anna selection and reload is Andrew's act at localhost:5174").

## Verbatim

> "Just tried anna on localhost, did get a new error message this time, so change is happening of some kind; Unavailable
> No source age yet
> NOT_READY"

## What it records

- Screen text seen: `Unavailable` / `No source age yet` / `NOT_READY`, on the signed-in Anna selection at `localhost:5174`.
- His read: the message is NEW relative to his previous attempt, so a change has reached the screen. He does not say which change; that is the seats' to measure (candidates known to this seat: the deployed Holdings reader at CodeSha `l/GQrFcE...` applied 23:00:52Z, the expanded COT publication `ac3adb97` verified by the CTO, the reason-code render fix `c1ac41ec` on the portal live-data branch).
- Not a PASS: the journey did not render holdings. `NOT_READY` is a defined public_reason_code in the v1 contract; "No source age yet" is the render's reason text.

## Routing

`1.0.0_SA_CTO` (owner of the review), `2.0.0_SA_COO~M` (Holdings journey), `2.0.0_SA_COO~P` (shared runtime and render). `0.0.0_AB_MSTR` adjudicates nothing here.
