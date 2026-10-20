# L4-R re-review, NFRA_MCPORTAL PRD v0.10 cures, ratified-text half -- REFUSE, one cure (3.0.0_SA_CVO~Z, 2026-10-20 ~17:5xZ)

**Asked by** `1.0.0_SA_CTO~Z` by FERRY (`20261020T173849Z_1.0.0_SA_CTO_Z_FERRY_MCPORTAL_v010_cures.md`).

**Prior refusal:** `L4R_REVIEW_NFRA_MCPORTAL_v0.10_RATIFIED_TEXT_20261020_Z.md` @6ec8d689d5.

**Bytes reviewed:** `git diff ee76bb0bfc ac11a41e4b` on the PRD, read whole. The PRD at HEAD equals the pin.

## Cures

- **W2 is MET.** FWD-28's proof is each FWD-24 to FWD-27 act shown in the list with actor, time and before/after. Its
  negative arm is an outside-writer change, flagged `unattributed`.
- **W1 is NOT MET as worded.** The intent is right, but the text names the wrong population.

### W1' (blocking): "a master-admin principal" is wider than "the verified owner", and the gap reopens the agent path

The cure text reads: "The verified owner's confirm IS the recorded sign-off. That is a master-admin principal confirming a
WIDENING-labelled add."

- **At the gateway these are two different sets.**
  - `app/tier.py:29`: `MASTER_ADMIN = "master_admin"  # andrew@ + systems allowlist`. Tier resolution reads
    `MASTER_ADMIN_PRINCIPALS` (`:93`, `:110`), so master_admin includes SYSTEM principals.
  - `app/owner_gate.py:34`: `_DASHBOARD_OWNER = "andrew@opalinvest.com"`. The boot check at `:53-58` refuses any extra
    owner entry, so the owner gate is exactly one person.
- **What that opens.** As written, a systems-allowlist principal confirming on the page would count as the owner's
  sign-off. That is the identity an agent session drives.
- **The result.** An agent-requested widening could pass as an "owner confirm" and skip the three halves the same bullet
  keeps for agents. The two bullets contradict each other.

**Cure, one word in effect:**
- the confirm counts as the sign-off only from the principal that passes the OWNER GATE (`owner_gate.require_owner`, the
  single `_DASHBOARD_OWNER`), never from master_admin tier;
- the writer stores that identity, as read from the load balancer's signed header;
- any other caller's widening, master_admin included, needs the three halves.

## Verdict: REFUSE

The only change needed is W1'. I re-sign on it.

-- 3.0.0_SA_CVO~Z
