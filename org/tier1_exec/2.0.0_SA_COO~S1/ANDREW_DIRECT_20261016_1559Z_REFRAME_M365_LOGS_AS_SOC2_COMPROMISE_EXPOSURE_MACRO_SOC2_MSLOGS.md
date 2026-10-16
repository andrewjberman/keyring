# Andrew-direct, 2026-10-16 ~15:5xZ (11:5x AM ET), the `2.0.0_SA_COO~S1` terminal on dell1 -- the Microsoft 365 audit logs, reframed

Two messages, in this order. VERBATIM:

1. "Yeah here is how i want to play this. we actually reframe this whole thing about audit monitoring for suspicious behavior. the premise is if any opal user is hacked, we want to be able to know the exposure; what was seen, what the duration period was, its really about disaster recovery/remediation. I want this all under a new macro called SOC2_MSLOGS. We should scrub all ticket center frameworks from this schema. What happens is everything should be in the trino audit bucket, and it does track activity, but the premise is not for workflows, its for identifying common patterns and establishing if a suspicious one appears. Silver is just formatted bronze in parquet for query, gold is effectively pattern baselines."
2. "Relay this over to CRO on this box"

## What the issuer did (record, not adjudication)

- Recorded this file; relayed it to `4.0.0_SA_CRO~DELL1` (the CRO on this box, live) and named the record to `1.0.0_SA_CTO~DELL1` in one line, as org/XXX.md requires.
- Changed NOTHING in the project: no order cut, no stage flipped, no resource touched. Scope is not the issuer's to take (surface, do not adjudicate).
- Held: no round-3 cut for TCKT_MTADTA until the CTO and CRO have this.

## Facts the reframe meets, for whoever carries it (measured or read this session, not rulings)

- **Live today:** the collector, the door (two aliases), `opal-data-trino/m365-metadata/trino/` (bronze/silver/gold-coverage/state), the Entra app with one permission, the group `globgrph-trino-access-group`
  with `Andrew_Berman`. Two clean scheduled fires; 7 days of the eight's events stored.
- **The premise differs from what is built in four places:**
  1. *Population.* Built: only Andrew's eight, every other account dropped before the first write and never stored (his 05:4xZ word; PRD C-POPULATION; R20 entry X18, PERMANENT). The new premise names "any opal user".
  2. *Bronze content.* Built: bronze is reduced before the write (subject hashed, addresses reduced to class tokens, IPs reduced to office/remote, a whitelist of fields). The new premise says silver is formatted bronze.
  3. *The sign-in feed.* Built: `Audit.AzureActiveDirectory` is deliberately NOT subscribed (PRD C-FIELDS (a)).
  4. *Purpose and gold.* Built: the project and its PRD are about workflows for Ticket Center (FWD-2..FWD-5, `C-TCKT`, placement D7/TCKT, related TCKT_VNEXT). The new premise: baselines and suspicious-pattern detection, exposure and duration after a compromise.
- **Carried to:** `4.0.0_SA_CRO~DELL1` (brief, L1) and `1.0.0_SA_CTO~DELL1` (endpoint/placement/macro, L2-L3). The macro `SOC2_MSLOGS` does not exist in `org/missions/MACROS.yaml` today.
