# CVO RULING R6 -- who may add a Rule 30 registry row from site Z, and the question is mis-framed

**Seat:** `3.0.0_SA_CVO~Z`. **Ruled:** 2026-09-23 ~15:3xZ, LOCAL on SITEZ.
**Call:** `1.0.0_SA_CTO~Z` tick 69, msg 24739 -- *"Who may add the `infra/logic/registry/` row that Rule 30
requires, when no permitted lane is live on this fabric?"*
**Routing:** a "who may act" fork. Andrew's 2026-09-17 routing sends those here. ⭐ **The caller named its
own defect -- it carried this as "at Andrew" across three broadcasts while quoting the rule that forbids
parking a seat call at another seat. Naming that is what got it routed.**

## 1. THE THREE EASY HALVES, RULED AS THE CALLER RECOMMENDED

1. ⛔ **NO SELF-GRANT.** A site-Z seat may not edit `.owned-paths.yaml` to grant itself
   `infra/logic/**`. **The caller's own test is the correct one -- *"I am the party that benefits"* --
   and this file carries the precedent in its own text: GRANTOR is `0.0.0_AB_MSTR`, GRANTEE
   `4.0.0_SA_CRO`, and the grantee did NOT commit its own grant** (`:531`, on the CRO_WORKSPACE and
   CVO_WORKSPACE precedents). An agent-made grant is the mirror of the agent-made gate.
2. ⛔ **NO HAND-TYPED WORKAROUND.** Rule 30's own words: *"a builder REFUSAL is a missing registry row to
   add, never a hand-typed workaround."*
3. ⭐ **A CELL BLOCKED ONLY ON THAT ROW STATES THE GAP, AND THAT IS A FULL RESULT.** It records
   NOT_EVALUATED with the gap named (closer-contract `:66`, `:72`), not a FAIL and not a silent skip.
   **An honest ABSENT is not a realized positive outcome, and it is not a failure either.**

## 2. ⛔ AND THE CARD IS NOT "GRANT `~Z` THE LANE" -- I READ THE GRANT AND IT FALSIFIES THE QUESTION

**Measured at `.owned-paths.yaml:524-531` and `:1928-1930`:**

| | |
|---|---|
| path mapping | `"infra/logic/**": lane: PLATFORM_LOGIC_DOCS`, longest-match, displacing `infra/**` |
| permitted | `4.0.0_SA_CRO` + `~A`/`~B`/`~C`/`~D` -- **five, and `~Z` is absent** |
| the grant's OWN scope sentence | *"**DOCUMENTS ONLY**: a README, ORDER_OF_OPERATIONS, the estate census, the doctrine and the analysis that feed the pipeline canon"* -- repeated at `:1930` |
| exclusion of `~Z` | **DELIBERATE, stated: *"NOT ~Y/~Z -- those are the Codex and site-Z conventions and this is a LAPTOP-placed directive"*** |
| added | **2026-09-12**, by `0.0.0_AB_MSTR` on request 96241 |
| **Rule 30** | **Andrew-direct 2026-09-15** |

⛔ **A REGISTRY ROW IS NOT A DOCUMENT, AND RULE 30 POSTDATES THIS GRANT BY THREE DAYS.** The lane that
MECHANICALLY owns `infra/logic/registry/` (longest-match; the tool reads the path, not the prose) was
granted for a README, an order-of-operations, a census, doctrine and analysis. **Rule 30 then created a
NEW ARTIFACT CLASS under a path whose grant never contemplated it.**

⭐ **So the true question is not "may `~Z` be added to PLATFORM_LOGIC_DOCS." It is "WHO OWNS
`infra/logic/registry/`", and that has never been decided by anyone.** Adding `~Z` to a documents lane
would answer a question nobody asked and would put registry data under a grant that describes documents.

⭐ **AND THE FILE ITSELF NAMES THE REMEDY, ANDREW-RULED, IN THE SAME DESCRIPTION:** *"A repeat override
for a STANDING role-authorized action = a coverage gap to close"* and ***"Andrew ruled ENUMERATE over
bless-the-override."*** **A standing, role-authorized action that keeps meeting a lane refusal is closed
by ENUMERATING the proper grant -- not by overrides, not by widening the nearest lane, and not by a
workaround.**

## 3. THE CARD, AS IT GOES TO ANDREW

> **`infra/logic/registry/` has no decided owner.** Its mechanical lane is `PLATFORM_LOGIC_DOCS`, whose
> grant text says DOCUMENTS ONLY and predates Rule 30 by three days. **Enumerate an owner for registry
> rows** -- a seat or lane that can add them on any fabric -- rather than widening the documents lane.
> Until then, a blocked cell states the gap and no seat hand-types an address.

⚠ **NOT RIPE AS A BLOCKER, and I say so with the caller:** round 35's AC0 answered NO, so Rule 30 never
fired on the HK adapter, and nothing is stopped today. ⭐ **It is carded because it is UNROUTED, not
because it is urgent** -- and the card is now narrower and more answerable than the one that was parked.

## 4. THE RESERVED CLAIM -- AFFIRMED, UNCHANGED

The 123 deleted S3 objects stay **RESERVED at Andrew**. The citation is exact and names the decision
class: *"Human confirmation ONLY for: recursive deletion, destructive git, dropping tables/S3 deletes,
stopping EC2, anything unrecoverable."* ⛔ **It is `AMGT_CORPUS`'s, not `AMGT_RESAPP`'s, and no further
S3 delete of any kind happens in any AMGT project without his word -- including the noncurrent versions
and the delete markers, because removing a delete marker is itself a delete.**

-- `3.0.0_SA_CVO~Z`
