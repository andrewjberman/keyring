# CTO half -- the Comparison GRANT release, generate + resident (packet blob b6c264b3) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-28 ~00:5xZ. **Request:** 2.0.0_SA_COO~P msg 102282.
**Authority:** Andrew-direct "call 1 yes" (record @`fce766f6ed`), for firms that see Opal's models in Model Portfolios.
**Rulings it executes:** CTO 102142/102151 (the benchmark proof; the cross-firm name check) and 102169 (firm ids from the
registry, never typed).

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_GENERATE_RESIDENT_GRANT_20260928.md`
@`59af14a585`, blob `b6c264b3`. Read at HEAD: `git hash-object` equals `git rev-parse 59af14a585:<path>`.

## What was read

- **Four commits:**
  - the GRANT: `templates.json` carries NO typed firm (`permitted_firm_ids` stays []);
  - the consumer takes firms from `lib/opal_naming.lookup()` and pins 4/4 policy hashes;
  - the catalogue port wiring;
  - the publisher's foreign-firm-name refusal, with forms from `scopes.json`.
  The naming gate (ENFORCE) passed every commit, which meets my ruling 102169.
- **D1, generate** `ykJltfTd` -> `AdE17rT6`:
  - census 111/111, five files;
  - built-zip smoke PASS;
  - **~Y's module census:** every collision winner is the intended source, so tonight's errors.py class is checked;
  - the one-member `_scope` pin skew is stated and already served live;
  - plan 0/1/0; rollback to `Iu3nADja`.
- **D2, resident** st -> st2:
  - 225/225, four files plus bindings;
  - member shas checked, the factory pre-check on resident_main's own path, a stop only on a 0/0 queue, and an
    automatic roll back to st.
- **Blast radius, both branches:**
  - Comparison and Multi-Comp go from refused to ADMITTED under the pinned policy; unknown keys and edits are refused;
  - a foreign firm's printed name refuses publishing;
  - Overview is unchanged.
  - Reachable only by walk windows today.
- **The success path is exercised on the BUILT zip before D1** (Comparison and Multi-Comp ACCEPT, an unknown key
  REFUSED), which meets the CRO's 102280 standard. There are live before/after reads on each move, and a same-turn
  rollback on any unnamed difference.

## Named item

**No false foreign-firm refusal.** Before the name check is relied on, one certified report per firm is run through
the served publisher's check (from existing certified PDFs; no vendor call):
- a 49financial report;
- an Inflection report that prints "Inflection";
- a Cottonwood report that prints "Cottonwood".
The firm's OWN name must never refuse. A false refusal is a BLOCKING row, and D2 rolls back to st.

**CTO half: SIGNED on blob b6c264b3.** The CRO half is separate.
