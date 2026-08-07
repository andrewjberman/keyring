# comp-estate's C3.i view is CLASS-grain and catalog-backed; the substrate is INSTANCE-grain and graph-backed

**Serial:** 3.0.0_SA_CVO · **2026-08-07** · **FINDING, ROUTED, NOT BUILT.** C3.ii and the
C3.i↔C3.ii bridge are on this pass's CUT LIST. Nothing here builds either.

## Why this was measured

Andrew's north star names the destination explicitly: *"…ultimately filtering up into the Kimi
Pipeline work and **bridge between C3.i and C3.ii in Comp-Estate**."* The C2/C3.i layer is the
substrate that bridge stands on. So: **can comp-estate read the substrate we are about to land?**

## Measured at source

| | |
|---|---|
| engine references to `C2Motif` / `C3System` | **0** (`grain` appears only in footer prose) |
| any graph query path for the motif/system layer | **none** — 3 `kuzu` mentions, all prose |
| `cmd_structure()` (the C3.i drill view) source of truth | `legacy.ladder_context()` → `fam2sys`, **the catalog** |
| its own miss message | *"that is a statement about the catalog (N structures)"* |
| `cmd_layers()` | reads `C0_C1_C2_C3_C4_SYSTEM_LAYERS.md` and prints it **verbatim** |

So comp-estate's C3.i is the **~13 hand-legislated named structures**. The layer being built is
**1,255 composed instance-grain structures**. Different grain, different backing store, no join.

## What this is NOT

**It is not a serving-law violation.** The law says anything C3-or-below is never served from a
hand-written document. `--layers` does serve the ladder doc verbatim — but that doc no longer carries
its computed counts: they were de-pinned to `##` with a stated derivation. It serves STRUCTURE
(stable) and explicitly refuses to serve POPULATION. The `##` placeholders *are* the compliance
mechanism. Checked before claiming.

**It is not a defect in comp-estate.** The engine says so itself at line 44: *"This is the BRIDGE,
not the destination. The destination is comp-kuzu canonical."* Catalog-backing is a deliberate design
choice, not drift.

## What it IS

**The bridge Andrew named does not have a read path to the substrate being built for it.** When the
instance layer lands, `comp-estate --structure` will keep matching catalog names and will not see the
1,255. The two grains coexist without a join.

**The join mechanism already exists and is the thing that makes this cheap:** every node in the
composed layer carries `grain: class|instance`, and the 23 existing class nodes are marked with the
same discriminator (DONE-MEANS item 4). That was built to avoid an arch-gated `NODE_TYPE_LAYER`
registration; it doubles as the exact key a catalog↔graph join needs. **A `--structure` that reads
graph instances filtered by `grain` is a query, not an architecture.**

## Deliberately not done

- No build, no spec, no tool change. C3.ii and the bridge are CUT-LISTed this pass.
- No estimate. The last time a cost was published on this thread it moved twice in four hours
  (`1.0.0_SA_CTO~C`, VERTHARVEST v1→v2), and the honest state is that the substrate is not landed yet.
- **Nothing here gates anyone.** The C2/C3.i work does not depend on this and must not wait for it.

## Limits

- Measured on the engine source at HEAD, not by running every command against a landed layer —
  which is impossible, because the layer is not landed. This predicts a read gap; it does not
  observe one.
- `_legacy()` / `ladder_context()` were read for their SOURCE OF TRUTH, not audited for correctness.
- Whether the bridge *should* live in comp-estate or in comp-kuzu is an architecture call and
  Andrew's, not mine. The engine's own line 44 suggests comp-kuzu; I am recording that pointer, not
  endorsing it.

-- 3.0.0_SA_CVO
