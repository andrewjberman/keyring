# ANDREW-DIRECT — pre-deploy EDICT: Global shows the complete-data frontier; Cottonwood pipeline named priority

**Channel:** Andrew-direct, CTO terminal, 2026-08-04 ~16:46Z (~12:46 ET).
**VERBATIM:**
> "I need an edict to go out to DE and DT before new PROD portal is deployed. WE cannot have
> this weird UI and stripped Cottonwood figure. What we do is just show the last date for which
> we have all the data for the 'Global' scope aggregate-aua-timeseries.json. Furthermore, we
> really need to get on the Cottonwood pipeline because it is insane that it is still frozen
> at 7-27."

**Scope as surfaced (CTO read):**
1. **DEPLOY GATE (DE + DT):** no new PROD portal deploy ships a Global view whose latest
   displayed date lacks any firm's data. The Global scope's `aggregate-aua-timeseries.json`
   display anchors to the **last date for which ALL firms' data is present** (the complete-data
   frontier) — no mixed-frontier tail where cottonwood's freeze strips the figure.
2. **Cottonwood pipeline = named priority:** the staged cottonwood spine is frozen at 07-27
   while the vendor feed itself is current (the 08-04 BD dim partition exists and was read
   today). The unfreeze path is the in-flight round-2 chain + the composition disposition; the
   edict makes cottonwood-leg completion the named priority.

**Mechanism (CTO, so the edict is executable, not aspirational):** immediate form = FE clamps
the Global displayed axis to the complete-data frontier (DE, rides the pending deploy); durable
form = the global fold emits `complete_through` explicitly and FE reads it (canon-route program,
L3 fold contract — Phase-B item). The deploy gate binds on the IMMEDIATE form.

**ADDENDUM ~16:48Z, VERBATIM (third edict item):**
> "In addition to that, we have three different timestamps, two non-canonical that just got
> added to the 'Portfolio Analytics' panel in Model Portfolios portal page, in addition to the
> canonical one that sits on the bottom right. The two non-canonical ones need to not be there.
> Any non-canonical timestamps are not acceptable and must be cleared."

**Scope as surfaced:** 3. **TIMESTAMP HYGIENE (DE, same deploy gate):** the Portfolio Analytics
panel shows exactly ONE timestamp — the canonical bottom-right one. The two newly-added
non-canonical timestamps are removed before the deploy, and the GENERAL RULE binds forward: no
non-canonical timestamp ships on any portal surface.

**Broadcast:** DE 0.4.0 + DT 0.4.0 + DT 0.2.0 (authority question still open at Andrew — the
edict binds WHOEVER deploys) + COO (dispatch) — same turn.
