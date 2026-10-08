# Andrew-direct 2026-10-08 ~19:3xZ at the dell1 0.0.0_AB_MSTR~DELL1 terminal -- backfill data queue project, incoming, runs on dell1

**Verbatim:** "There is also an incoming project that should be coming over the wire at some point which I need you to stay aware
of. From SITEZ and from DELL2, each CRO on those fabrics is writing a brief/analysis about what is effectively a backfill data
queue project, with the SITEZ brief being the more organization-wide project and the DELL2 one being the more Cottonwood-shaped
version. All of this needs to get wrapped up into a registered project which will be run on this device. Be on the loookout for
those."

**What it sets:**
- Two inputs are expected over the bus: a site Z CRO brief (organization-wide backfill data queue) and a dell2 CRO brief
  (the Cottonwood-shaped version).
- Both fold into ONE registered project, placed on dell1.
- 0.0.0_AB_MSTR~DELL1 watches for both, carries each to 1.0.0_SA_CTO~DELL1 on arrival, and asks the site Z and dell2 managers
  to route them here. Registration (L3) and its shape are the CTO's.

**Related, already in flight:** the dell1/dell2 Yahoo price backfill agreement (1.0.0_SA_CTO~DELL1 msg 1073; dell2 CRO research
@e112184d3b). The CTO decides how it relates to the registered project.
