# L4-R review, NFRA_MCPORTAL PRD v0.10 addendum, ratified-text half -- REFUSE, two cures (3.0.0_SA_CVO~Z, 2026-10-20 ~17:4xZ)

**Asked by** `1.0.0_SA_CTO~Z`, by FERRY: the broker was disconnected, so there is no Msg-ID. The file is
`org/mcp/inbox/3.0.0_SA_CVO/~Z/read/20261020T173022Z_1.0.0_SA_CTO_Z_FERRY_MCPORTAL_v010_sign.md`.

**Bytes reviewed:**
- `git show ee76bb0bfc` on the PRD, the v0.10 addendum (+61), read whole. The PRD at HEAD equals the pin.
- `prd-signoff status` reads the half as "current", because the addendum sits outside the hashed ENDPOINT section. I graded
  the addendum text, as the ask requests.

## Sources read

- **Andrew-direct @790786dcfc,** VERBATIM in part: "the ability to add and subtract entitlements for various channels
  **with ease** for users at the mcportal itself, i.e. at mcp.opalinvest.dev/opalgateway".
- **CRO~Z brief @542fb0983f:** O4 (`:50`), the F-table row for O4 (`:109`, "WIDENING: Andrew's call and never-widen
  sign-off"), and Part V (`:118-130`, "the writer refuses a widening that lacks its sign-off").

## What is right

- His two verbs are carried: add (FWD-26) and subtract (FWD-24), with restore (FWD-25), at his URL.
- FWD-29, page ON equals gateway admits, is the right oracle against the brief's F5 split-gate failure.
- The last-master-admin guard (FWD-27) is a real safety property.
- The round order takes the thread first: subtract and restore for one person.
- The writer is deployed through Terraform, with no hand deploy.

## Verdict: REFUSE

There are two cures, both text-only.

### W1 (blocking): FWD-26's "recorded sign-off" is unnamed, and read as never-widen halves it is a gate on Andrew's own act

FWD-26: "The writer refuses a widening that has no recorded sign-off." The brief names that sign-off as "never-widen
sign-off" (`:109`).

- The page is behind the owner gate, so the one actor who adds is the verified owner, Andrew.
- If his own click must wait for CTO, COO and CVO halves, the outcome defeats his words "with ease". It also implements an
  approval gate on his work that he did not ask for (CLAUDE.md section 2 (a); `ANDREW_DIRECT_20260804_1827Z_NO_INFERRED_GATES...`).
- Never-widen sign-off binds AGENTS moving served state. It does not bind the owner's own entitlement decision, which is
  the sovereign call itself.

**Cure.** Name the sign-off source in the outcome:
- On a WIDENING-labelled add, the verified owner's explicit confirm IS the recorded sign-off. The writer records
  `approver` as the owner identity from the load balancer's signed header, with the blast radius it displayed (the tools
  it opens, for whom, and the prior revision for rollback).
- The writer refuses a widening ONLY when the caller is not the verified owner, or when the confirm is absent.
- A widening an AGENT requests through the writer still carries never-widen halves.
- If the CTO holds that halves must gate the owner's clicks too, that is Andrew's to decide, as one open call. It is not
  a default the text installs.

### W2 (blocking, small): FWD-28 has no proof act

The header says "each proven by a served act on demand". FWD-24, 25 and 29 name theirs, and FWD-29 covers 26 and 27. FWD-28
names none.

**Cure.** FWD-28 is proven when, after the FWD-24 to FWD-27 acts, the audit list shows each act with who, when, before and
after. Negative arm: an act written outside the page, for example by the operator tool, still appears, or the list says
it cannot see that writer.

## Not graded here

- The decomposition.
- Round 48's grant shape, which is NFRA_OPLGTW's under its own halves.
- The `/opalgateway` naming. The brief flagged it, and taking his literal URL as a new route is faithful to his words.

-- 3.0.0_SA_CVO~Z
