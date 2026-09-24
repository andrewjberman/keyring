# Literal projection delta for P

Source basis: M portal e5604c03. Two P-owned files, provided as a patch only;
not applied to shared code by M. P should apply/reconcile against its current pin.

The current adapter drops classification.hierarchy_path and falls through to an
opaque node_id even for the Client sleeve. This blocks the actual producer's
Client category from reaching the UI. Patch preserves hierarchyPath as an optional
view property (old view fixtures remain valid) and uses its final component as the
SLEEVE label. Security/product identity and model identity remain preferred labels;
UNKNOWN fee/advisory and authoritative=false stay exactly as received.

Targeted consumer checks for P: (1) an observed ACCOUNT75 -> SLEEVE75 with
hierarchy_path=["Client"] -> signed SECURITY100/-25/0 must show Client75;
(2) the security's name remains native security id, not "Client", even while its
hierarchyPath is ["Client"]; (3) absent classification leaves the old node_id label
and empty hierarchyPath, not invented Client; (4) false authoritative remains
false, independent of the path. Expected first real INF category totals use this
exact mapping. No new public wire field, runtime request or inferred namespace.

Quantity/name and distinct custody/overlay clocks remain separate requested shared
projection/schema additions; this small patch alone does not claim those complete.
