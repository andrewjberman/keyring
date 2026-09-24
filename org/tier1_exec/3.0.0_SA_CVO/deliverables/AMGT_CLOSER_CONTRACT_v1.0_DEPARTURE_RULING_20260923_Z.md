# AMGT closer CONTRACT v1.0 -- RULING ON THE OFFERED DEPARTURE

**Reviewer** `3.0.0_SA_CVO~Z`. **Date** 2026-09-23. **Artifact** CONTRACT.md @`0e33cea24b` s.3.

## VERDICT: THE DEPARTURE IS **NOT OVERTURNED**. UPHELD, with its reasoning corrected and two residuals named.

`/closer` Step 2 requires `1.0.0_SA_CTO~Z` to land each s.3 ownership row as an `.owned-paths.yaml`
lane granting only the named seat, in the contract's own commit. It is not done. The contract offered
that departure to this seat for overturn. **It stands.**

## 1. WHAT THIS SEAT MEASURED, ON ITS OWN INSTRUMENT

`.tools/owned-paths-validate.py` loaded at HEAD `1059957fd1` and driven directly
(`resolve_lane` + `check_agent`) against the s.3 table's own paths. `OWNED_PATHS_MODE` defaults to
**`block`**, not warn (`.tools/git-hooks/owned-paths-check.sh:41`), so a refusal is hard.

**The four Python shared surfaces -- the departure's reasoning is CONFIRMED:**

| surface | resolved lane | `~X` / `~Y` / `~Z` permitted |
|---|---|---|
| `lib/research/corpus/report_input.py` | `BASE_EXEC` | True / True / True |
| `lib/research/coverage/pool_reader.py` | `BASE_EXEC` | True / True / True |
| `lib/research/metrics/generation_writer.py` | `BASE_EXEC` | True / True / True |
| `lib/research/api/scoped_amgt.py` | `BASE_EXEC` | True / True / True |

`resolve_lane` is **longest-match-wins** (`:254-273`, sorted descending by specificity). A new narrow
row for any of these paths therefore **overrides** `BASE_EXEC` rather than adding to it, and would
refuse the other two lanes **and the base**. **OK: writing lane-only rows here would narrow three
live seats mid-drive, exactly as the contract states, and in `block` mode that is a hard refusal at
their next commit.**

## 2. A CORRECTION THIS SEAT OWES ON ITS OWN FIRST READING

Driving the same instrument over the six **portal** surfaces returns lane `POD_DE_ANY`, whose
`permitted_agents` are `['0.1.0_DE_MarketIntelligence', '0.2.0_DE_PortfolioAnalytics',
'0.3.0_DE_TradingOperations', '0.4.0_DE_ClientPlatform']` -- so `2.0.0_SA_COO~Z`, **named sole writer
of every one of them**, reads `False`, as does its base.

**This seat first read that as a live hard blocker in front of `B00`/`E0`. THAT READING IS WRONG and
is corrected here before it reaches anyone**, because the alarming version is the one that would have
sent a lane chasing a refusal that cannot occur. Measured:

- `portal` is a **gitlink** (`git ls-tree HEAD portal` -> mode `160000`), not a directory of the
  parent repo.
- Its own toplevel is `.../ajb_workspace/portal` and **it carries no `.owned-paths.yaml`**.
- `core.hooksPath` is **unset at system, global and local scope, and unset in the submodule**.
- `portal/.git/hooks/` contains **only `.sample` files -- no active hook**. The parent carries live
  `pre-commit`, `commit-msg`, `pre-push`, `post-commit`; the submodule carries none.

**So no hook evaluates a commit made inside `portal`, and the parent's path-to-lane table never runs
against portal paths.** The `POD_DE_ANY` / `False` result is a number my own invocation produced, not
a state any commit is graded against. **`2.0.0_SA_COO~Z` is NOT blocked from its portal surfaces.**
The parent-side gitlink pointer bump stages the path `portal` (no trailing slash), which resolves to
lane `ANY` and permits that seat.

This is the submodule grain trap: parent-repo path logic applied to paths the parent's hook never sees.

## 3. WHAT THAT MAKES THE ACTUAL STATE

**Across all ten shared surfaces in s.3, one-writer-per-surface is mechanically UNENFORCED** -- four
by over-permission (`BASE_EXEC` admits all three lanes), six by the total absence of any hook. The
directions differ; the enforcement is absent either way.

**The departure did not create this. It predates the contract and is total**, which is the strongest
argument for upholding it: landing the rows would not close the gap, it would only move four surfaces
from over-permissive to over-restrictive while the six portal surfaces stayed exactly as they are.

## 4. RESIDUAL 1 -- THE COMPENSATING CONTROL IS ONE-DIRECTIONAL, AND THE CONTRACT SHOULD SAY SO

The departure's named fallback is *"a seat refused at a path this table gives it reports the refusal
as a blocker and the grant is added same-turn."* **That covers only the false-REFUSE direction.**
The exposure that actually exists is the **false-PERMIT** direction -- two lanes writing one shared
surface -- and **nothing detects it**, because no refusal is ever emitted. A seat that writes another
lane's surface gets a clean commit and no signal.

**DISCRIMINATOR, one command per shared surface, run at each drain:**
`git log --format='%an' <since>..HEAD -- <surface>` and require **exactly one distinct author**.
**COST:** one command per surface in s.3. **NON-APPLICATION:** a surface with no commits in the
window. This seat is naming the control, not building it; `1.0.0_SA_CTO~Z` integrates.

## 5. RESIDUAL 2 -- A LANDMINE IN THE OBVIOUS WAY TO "FINISH" STEP 2

⛔ **Do NOT discharge `/closer` Step 2 for the portal rows by installing the parent hook into the
submodule.** `owned-paths-check.sh:137-143` -- when `.owned-paths.yaml` is absent and `MODE` is
`block`, it logs `YAML missing -- block mode` and **`exit 1`**. With no `portal/.owned-paths.yaml`,
installing that hook would hard-fail **every** portal commit, converting an absent control into a
total outage on the lane that owns `B00`/`E0`, the one thread the contract says nothing counts before.
Landing rows in the parent's file is, separately, **inert** for portal.

**So `/closer` Step 2 is only PARTIALLY dischargeable on this estate**, and the contract should record
that the portal rows bind **by reading only** rather than leave them reading as governed. That is a
one-line addition, not a re-cut.

## 6. SCOPE AND LIMITS OF THIS RULING

- Measured on **repo bytes and git config at HEAD `1059957fd1` on site Z**. Device-scoped: hook
  installation is per-clone, so another device may differ and this ruling does not speak for it.
- This seat did **not** census `.owned-paths.yaml` in full; it drove the resolver against the ten
  paths the contract's own table names. The denominator is those ten, not the file.
- Nothing here touches the never-widen pair, the deploy gates, or any acceptance ID.

## 7. SEPARATELY, AND NOT PART OF THIS RULING

The s.3 table names `2.0.0_SA_COO~Y` sole writer of `lib/research/coverage/pool_reader.py`. That is
the surface carrying **R5** of this seat's AMGT_HARVST L4-R refusal (`59d833bd88`) -- the missing
`NO_COVERAGE` key that flips `gold_window_read`'s `complete` from False to True. Ownership is
coherent: the remedy lands in the lane that already owns the file.
