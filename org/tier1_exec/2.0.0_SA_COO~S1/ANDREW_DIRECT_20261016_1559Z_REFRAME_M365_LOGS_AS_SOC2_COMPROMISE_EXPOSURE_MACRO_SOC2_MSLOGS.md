# Andrew-direct, 2026-10-16 ~15:5xZ (11:5x AM ET), the `2.0.0_SA_COO~S1` terminal on dell1 -- the Microsoft 365 audit logs, reframed

Five messages, in this order. VERBATIM:

1. "Yeah here is how i want to play this. we actually reframe this whole thing about audit monitoring for suspicious behavior. the premise is if any opal user is hacked, we want to be able to know the exposure; what was seen, what the duration period was, its really about disaster recovery/remediation. I want this all under a new macro called SOC2_MSLOGS. We should scrub all ticket center frameworks from this schema. What happens is everything should be in the trino audit bucket, and it does track activity, but the premise is not for workflows, its for identifying common patterns and establishing if a suspicious one appears. Silver is just formatted bronze in parquet for query, gold is effectively pattern baselines."
2. "Relay this over to CRO on this box"
3. "HAve them handle how to restructure this accordingly, its fairly cosmetic + cleaning up TCKT_MTADTA references"
4. "then CRO can handle the brief for this, and have it sent to CTO on this box and handled on this bxo"
5. "basically theyll bring it back to you once that plan is locked in and you will be the one driving it"

## What the issuer did (record, not adjudication)

- Recorded this file (messages 3 to 5 added ~16:0xZ); relayed it to `4.0.0_SA_CRO~DELL1` (the CRO on this box, live) and named the record to `1.0.0_SA_CTO~DELL1` in one line, as org/XXX.md requires.
- Changed NOTHING in the project: no order cut, no stage flipped, no resource touched. Scope is not the issuer's to take (surface, do not adjudicate).
- ROUTING (messages 4 and 5): the CRO on this box writes the brief and sends it to the CTO on this box (dell1), who handles it on this box; both bring the locked plan back to `2.0.0_SA_COO~S1`, who drives it. Until then the issuer cuts nothing for it.
- Held: no round-3 cut for TCKT_MTADTA until the CTO and CRO have this. "Them" is read as the CRO and the CTO (the brief and the endpoint, placement and macro); the issuer builds nothing on this until they say what the restructure is.
- Andrew calls the restructure "fairly cosmetic + cleaning up TCKT_MTADTA references". The four differences below are facts about the built system that the CRO and CTO decide whether his word covers; the issuer does not rule on that.

## Facts the reframe meets, for whoever carries it (measured or read this session, not rulings)

- **Live today:** the collector, the door (two aliases), `opal-data-trino/m365-metadata/trino/` (bronze/silver/gold-coverage/state), the Entra app with one permission, the group `globgrph-trino-access-group`
  with `Andrew_Berman`. Two clean scheduled fires; 7 days of the eight's events stored.
- **The premise differs from what is built in four places:**
  1. *Population.* Built: only Andrew's eight, every other account dropped before the first write and never stored (his 05:4xZ word; PRD C-POPULATION; R20 entry X18, PERMANENT). The new premise names "any opal user".
  2. *Bronze content.* Built: bronze is reduced before the write (subject hashed, addresses reduced to class tokens, IPs reduced to office/remote, a whitelist of fields). The new premise says silver is formatted bronze.
  3. *The sign-in feed.* Built: `Audit.AzureActiveDirectory` is deliberately NOT subscribed (PRD C-FIELDS (a)).
  4. *Purpose and gold.* Built: the project and its PRD are about workflows for Ticket Center (FWD-2..FWD-5, `C-TCKT`, placement D7/TCKT, related TCKT_VNEXT). The new premise: baselines and suspicious-pattern detection, exposure and duration after a compromise.
- **Carried to:** `4.0.0_SA_CRO~DELL1` (brief, L1) and `1.0.0_SA_CTO~DELL1` (endpoint/placement/macro, L2-L3). The macro `SOC2_MSLOGS` does not exist in `org/missions/MACROS.yaml` today.
