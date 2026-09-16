# LGIC_NAMING -- round 1 remediation slug

Author: 3.0.0_SA_CVO. Round: v1. Fabric: laptop. Recorded: 2026-09-14T18:42:49Z.

Input: `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba` (33 rows; 23 compiled at this L8). Adjudication: `ADJUDICATION_v2.md` (C-S3..C-S9), same slug. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md`.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. One row per graduated item (20). Three rows were dismissed (C-S4) and are not here. Every row is OPEN: this round measured and remedied nothing inside itself, except W6-S1's disarm (S12).

```json
[
 {
  "id": "LGIC_NAMING-W2-S1",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Namer A (LN-e-1): the two briefing files close scope, kind, cadence and system class but leave the FUNCTION / PURPOSE slot an open vocabulary, so 11 of 18 N3 names turn on a token the namer chose from the item's own words with no rule to choose between candidates (publish vs publisher, fetch vs session-fetch, compound vs function+qualifier).",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S1",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "org/standards/NAMING_SCHEMA.json@6a5b276f8b :56 resource.function = 'one or more kebab tokens naming what it does; a compound such as silver-chain is ONE function token' -- no closed list; :57 qualifier = 'optional narrowing: a table, a leg, or an environment'; :105 secret.purpose and :107 iam_policy.purpose_slot = function carry no list either. :81 names 'trigger, publisher, scanner' as FUNCTION tokens, the only function tokens either file spells.",
   "infra/logic/05_IDENTITY_SPINE.md@6a5b276f8b holds firms, products, vendors and masters only (sections 2-3); it mints no function token."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W3-S2",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "NAMING_SCHEMA v1.4 closes the kind and cadence slots but not the function/purpose slot ('one or more kebab tokens naming what it does'), so 14 of the 18 N3 names in n3-namer-b.tsv carry a function or purpose token this worker chose by a stated rule rather than looked up; the schema itself lists the noun 'publisher' as a function token beside the verb reading.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W3-S2",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "SCHEMA: org/standards/NAMING_SCHEMA.json:56 @6a5b276f8b, resource.function: 'one or more kebab tokens naming what it does; a compound such as silver-chain is ONE function token' -- no enumeration.",
   "SCHEMA: org/standards/NAMING_SCHEMA.json:57 @6a5b276f8b, resource.qualifier: 'optional narrowing: a table, a leg, or an environment (dev | prod)' -- no rule for whether it is written when an item names none."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W2-S2",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Namer A (LN-e-1), item i13: the entity partition slot {entity}={id} admits two readings of 'the entity is the advisor keyed advisor_id' -- advisor=A123 (the entity's name) or advisor_id=A123 (its key); neither briefing file says which token fills {entity}. Namer A wrote advisor_id=A123.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S2",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "org/standards/NAMING_SCHEMA.json@6a5b276f8b :41 key.partition third member = '{entity}={id} -- an entity partition; the file is the object under it (doctrine R2)'; :38 names 'the kebab-case and hive forms' as binding NEW served families. Neither line says whether {entity} is the entity's name or its key column.",
   "org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_ITEMS.json@6a5b276f8b item i13: 'the entity is the advisor keyed advisor_id, and the advisor id is A123'."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W3-S1",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "N3 item i13 is answered RAISE: NAMING_SCHEMA v1.4 key.partition writes an entity partition as '{entity}={id}' without saying whether {entity} is the entity's name or its key column, and the item states both (the entity 'the advisor', keyed 'advisor_id'), so advisor=A123 and advisor_id=A123 are each a faithful substitution.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W3-S1",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "SCHEMA: org/standards/NAMING_SCHEMA.json:41 @6a5b276f8b, key.partition: '{entity}={id} -- an entity partition; the file is the object under it (doctrine R2)'. No field names which token fills {entity}; the one worked partition, date=YYYY-MM-DD, is a case where the entity and its key are the same word.",
   "SCHEMA: org/standards/NAMING_SCHEMA.json:38 @6a5b276f8b, key.legacy_served_path: 'the kebab-case and hive forms bind NEW served families only' -- i13 is a NEW served family, so the hive form binds, but the form's left-hand token is still unnamed."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W2-S3",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Namer A (LN-e-1), item i14: for a key whose {source} is the product itself (mdpf) and which is shared across all firms, the briefing files do not say whether {scope} is the GLOBAL key (global) or the PRODUCT key (mdpf). Namer A wrote mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S3",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "org/standards/NAMING_SCHEMA.json@6a5b276f8b :33 key.scope_classes = FIRM, PRODUCT, MASTER, GLOBAL; :114 global_scope key 'global'; :32 source = 'a registry VENDOR key or, for derived tiers, a PRODUCT or SYSTEM key'; :40 code = '{source}/{scope}/code/{built_tier}/{file}'. No line maps 'shared across all firms' under a PRODUCT source to one scope class; the resource grammar's 'OMITTED' rule (:54) cannot apply because the key's five segments are ruled (:27).",
   "infra/logic/05_IDENTITY_SPINE.md@6a5b276f8b section 3 PRODUCTS and VENDORS: a PRODUCT key appears as a scope only beneath a vendor source (pathfinder, trueshares -> etfs); no row shows a product as both source and scope."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W2-S4",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Namer A (LN-e-1), item i15: an instance profile for 'the Orion runner host that builds Inflection's gold data' has no product in the spine, and the schema admits a vendor as {system} 'only when the resource IS the vendor integration' without saying whether a vendor-named runner building a DERIVED tier is. Namer A wrote orion-inf-gold-build-profile.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W2-S4",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "org/standards/NAMING_SCHEMA.json@6a5b276f8b :120-122 system.classes = PRODUCT, PLATFORM_SUBSYSTEM, VENDOR; vendor_as_system_only_when = 'the resource IS the vendor integration'; never_a_system includes 'a firm'. :32 lets a derived-tier KEY take a PRODUCT or SYSTEM source, but no line says which system a derived-tier RESOURCE takes when no product owns it.",
   "infra/logic/05_IDENTITY_SPINE.md@6a5b276f8b section 3: inflection has no product row; orion is a VENDOR with scope inflection. No platform subsystem is listed in either file."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W3-S3",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Three N3 names turn on a scope or system choice the two briefing files leave open, each resolved by this worker by a stated reading: i14's product-shared code key takes scope mdpf (PRODUCT) not global, because GLOBAL has no rule for when it applies; i11 and i15 take the vendor as system (pathfinder, orion) under 'only when the resource IS the vendor integration'.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W3-S3",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "SCHEMA: org/standards/NAMING_SCHEMA.json:33 and :114 @6a5b276f8b: key.scope_classes ['FIRM', 'PRODUCT', 'MASTER', 'GLOBAL'] and global_scope {key: global}; no field says when a key takes GLOBAL. :54 resource.scope_when_shared 'OMITTED' binds the resource grammar only; the five-segment key grammar (:26-27) has no omission.",
   "SEED: infra/logic/05_IDENTITY_SPINE.md:30 and :50-51 @6a5b276f8b: R2 'a scope is a firm, a product, or a master'; invariant 1 'every {scope} segment in the census resolves to exactly one FIRM, PRODUCT or MASTER key' -- no GLOBAL."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W5-S2",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "LN-e-3's E3-AC1 invocation (check_ln.py e3-identical) prints VERDICT: FAIL-DIFFERENT, not the expected PASS-IDENTICAL: the two blind namers wrote the identical string for 9 of 18 N3 items; of the 9 that differ, 7 part at the function or purpose slot, 1 (i14) at the scope slot, and 1 (i13) is namer B's RAISE against namer A's string.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S2",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S5",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e3-identical, 2026-09-14 ~17:0xZ, worktree HEAD 33131baf6f -> 9 DIFFERS lines (i01 i02 i04 i07 i09 i13 i14 i15 i16) / 'ITEMS: 18  IDENTICAL: 9  DIFFERENT: 9' / 'VERDICT: FAIL-DIFFERENT', rc=0. The sibling criterion E3-AC2 (e3-blind) printed 'VERDICT: PASS-BLIND': both recorded bases are 6a5b276f8b and neither holds the other namer's file.",
   "ANSWERS: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv @254a310135 and n3-namer-b.tsv @beaefc6cf5. The slot for each differing item, found by the first differing token under org/standards/NAMING_SCHEMA.json @33131baf6f :51 (resource), :105 (secret), :107 (iam_policy) and :26 (key): function for i01 publisher/publish, i02 session-fetch/fetch, i15 gold-build/build-gold and i16 exporter/export; purpose for i04 api-credentials/api and i07 gold-read/read-gold; function or qualifier for i09 (A adds 'failure'); scope for i14 global/mdpf; the whole recorded string for i13 (B wrote RAISE)."
  ],
  "remedy": "The schema text, by an L10 addendum ruling each of the four slots, as S6-S8 and S10 were ruled; then a re-run of the two namer cells in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W6-S1",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Blind reader (LN-e-4): the order's premise 'you have never seen this estate' fails before the first tool call -- the worker session loads the workspace CLAUDE.md and the user's auto-memory MEMORY.md, which name cot, bd, inf, 49financial, inflection and cottonwood as firms, so 9 of the reader's 18 marks are tokens its context had already named as firms and 3 more (49f) abbreviate one it named.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W6-S1",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S6",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "CONTEXT: CLAUDE.md:329 @64dd54e67f (Rule 13, loaded into this worker's context by the harness before any tool call): 'cot is a separate firm from bd -- never mirror/sync.'",
   "CONTEXT: C:/Users/AndrewBerman/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/MEMORY.md (outside the repo, no commit; loaded at session start 2026-09-14): index line 'Legacy bd/inf/cot buckets are the ACTIVE firm channels until the D14 move to -49financial/-inflection/-cottonwood'."
  ],
  "remedy": "Seat blind cells in a context that loads neither CLAUDE.md nor the auto-memory, or rule that the measure cannot be taken inside this fabric (1.0.0_SA_CTO, fabric); give blind cells a row-id path that does not read the channel (1.0.0_SA_CTO, worker definition); re-cut LN-e-4/LN-e-5 so the reader's question and the key's rule are one rule and E5-AC1/E5-AC2 are jointly satisfiable (2.0.0_SA_COO~G at the recut). FWD-2 is NOT EVALUATED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-14T17:26Z"
  }
 },
 {
  "id": "LGIC_NAMING-S12",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Issuer's disarm of LGIC_NAMING-W6-S1, widened to the dependency the blind cells share: every worker in this round starts with the workspace CLAUDE.md and the user's auto-memory MEMORY.md already in context, so all six cells that carry a blindness requirement run on one un-blinded context. The leak is MEASURED on LN-e-4 only; on the other five it is NOT-EVALUATED.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-S12",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S6",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "ROW: LGIC_NAMING-W6-S1@31edd82e0b (OBSERVATION, ARMED, disarm_owner 2.0.0_SA_COO~G): the measured leak on LN-e-4 -- 9 of the reader's 18 marks are tokens the preloaded context names as firms verbatim, and 3 more (49f) abbreviate one.",
   "MECHANISM, observed at this seat: when a Bash call of the COO session entered .worktrees/wk-lgic-naming-1-4 (~16:4xZ), the harness injected that worktree's CLAUDE.md into the session context. A worktree carries the tracked CLAUDE.md, so a worker spawned in one loads it; .claude/agents/worker.md@31edd82e0b has no field that suppresses it."
  ],
  "remedy": "Seat blind cells in a context that loads neither CLAUDE.md nor the auto-memory, or rule that the measure cannot be taken inside this fabric (1.0.0_SA_CTO, fabric); give blind cells a row-id path that does not read the channel (1.0.0_SA_CTO, worker definition); re-cut LN-e-4/LN-e-5 so the reader's question and the key's rule are one rule and E5-AC1/E5-AC2 are jointly satisfiable (2.0.0_SA_COO~G at the recut). FWD-2 is NOT EVALUATED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W6-S3",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Blind reader (LN-e-4): the order says to read column 2 of n3-namer-a.tsv and nothing else, but appending the row its <paths> grants requires reading this channel to mint the next unused id, and the channel quotes N3_ITEMS item text and the namer's per-item choices; the reader fixed every mark before the channel read returned.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W6-S3",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S6",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "SPEC: org/missions/D14/LGIC/LGIC_NAMING/task-orders/LGIC_NAMING.TO-LN-e-4.blind-reader.md:20 and :24 @64dd54e67f ('Do NOT open N3_ITEMS.json ... or any other exercise file'; 'Read: column 2 of n3-namer-a.tsv, and nothing else'), and :48, the <paths> line granting this channel.",
   "CHANNEL: org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md @64dd54e67f, row LGIC_NAMING-W2-S2's grounding quotes N3_ITEMS.json item i13 ('the entity is the advisor keyed advisor_id, and the advisor id is A123'), and rows W2-S1..S4 name the namer's choices for i01-i18."
  ],
  "remedy": "Seat blind cells in a context that loads neither CLAUDE.md nor the auto-memory, or rule that the measure cannot be taken inside this fabric (1.0.0_SA_CTO, fabric); give blind cells a row-id path that does not read the channel (1.0.0_SA_CTO, worker definition); re-cut LN-e-4/LN-e-5 so the reader's question and the key's rule are one rule and E5-AC1/E5-AC2 are jointly satisfiable (2.0.0_SA_COO~G at the recut). FWD-2 is NOT EVALUATED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W6-S2",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Blind reader (LN-e-4): the order asks for THE one token that is the firm or the product, but at least 4 of 18 names carry both a recurring product-like prefix (mdpf) and a firm-like token, and the order does not say which to mark; the reader marked the firm token whenever one was present and the product token otherwise.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W6-S2",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S6",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "SPEC: org/missions/D14/LGIC/LGIC_NAMING/task-orders/LGIC_NAMING.TO-LN-e-4.blind-reader.md:22 @64dd54e67f: 'For each name, mark the token that is the firm or the product it belongs to, exactly as it is spelled in the name, or none if no token is.'",
   "INPUT: n3-namer-a.tsv column 2 @64dd54e67f: mdpf-cot-exporter-sg, mdpf-cot-publisher-lambda, mdpf-inf-delivery-status-table and mdpf/49financial/platinum/advisor_books/advisor_id=A123 each carry mdpf and a firm-like token; mdpf-demo-publish-failure-alarm carries 'demo' in the slot where its mdpf siblings carry the firm token."
  ],
  "remedy": "Seat blind cells in a context that loads neither CLAUDE.md nor the auto-memory, or rule that the measure cannot be taken inside this fabric (1.0.0_SA_CTO, fabric); give blind cells a row-id path that does not read the channel (1.0.0_SA_CTO, worker definition); re-cut LN-e-4/LN-e-5 so the reader's question and the key's rule are one rule and E5-AC1/E5-AC2 are jointly satisfiable (2.0.0_SA_COO~G at the recut). FWD-2 is NOT EVALUATED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W5-S3",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "LN-e-5's E5-AC1 invocation (check_ln.py e5-correct) prints VERDICT: FAIL-MISREAD, not the expected PASS-ALL-CORRECT: the blind reader marked the key's token on 14 of 18 N3 names; the 4 misses are all shared rows -- i07, i08 and i17 are 'none' in the key and the reader marked the product token (mdpf, etfs, etfs), and i14 is 'global' in the key and the reader marked mdpf.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S3",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S6",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e5-correct, 2026-09-14 ~17:2xZ, worktree HEAD 23beb7751c -> 'WRONG: i07  name=mdpf-gold-read-policy  marked=mdpf  expected=none' / 'WRONG: i08  name=etfs-price-refresh-dlq  marked=etfs  expected=none' / 'WRONG: i14  name=mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz  marked=mdpf  expected=global' / 'WRONG: i17  name=etfs-pipeline-alerts  marked=etfs  expected=none' / 'ITEMS: 18  CORRECT: 14  WRONG: 4' / 'VERDICT: FAIL-MISREAD', rc=0.",
   "INPUTS: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv @254a310135, n3-reader.tsv @3c2910ac09, and deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_KEY.json @777770e6aa, whose key_rule (:4) gives 'global' for the shared product scope of a key and 'none' for a shared resource that carries no scope (S5)."
  ],
  "remedy": "Seat blind cells in a context that loads neither CLAUDE.md nor the auto-memory, or rule that the measure cannot be taken inside this fabric (1.0.0_SA_CTO, fabric); give blind cells a row-id path that does not read the channel (1.0.0_SA_CTO, worker definition); re-cut LN-e-4/LN-e-5 so the reader's question and the key's rule are one rule and E5-AC1/E5-AC2 are jointly satisfiable (2.0.0_SA_COO~G at the recut). FWD-2 is NOT EVALUATED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W5-S4",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "LN-e-5's E5-AC2 invocation (check_ln.py e5-consistent) prints VERDICT: FAIL-TWO-REFERENTS, not the expected PASS-CONSISTENT: 5 of 18 names carry a token the reader marked elsewhere, all five the token mdpf (marked on i07 and i14, read as the product prefix on i01, i09, i13, i16, i18); read, not run, the key's own marks would also print 2 clashes (token etfs on i08 and i17), so E5-AC1 and E5-AC2 cannot both pass on this key.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S4",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S6",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e5-consistent, 2026-09-14 ~17:2xZ, worktree HEAD 23beb7751c -> 'NAMES: 18  TOKENS MARKED AS A FIRM OR PRODUCT: 9  A MARKED TOKEN READ OTHERWISE ELSEWHERE: 5' with the five pairs (mdpf-cot-exporter-sg, mdpf-cot-publisher-lambda, mdpf-demo-publish-failure-alarm, mdpf-inf-delivery-status-table, mdpf/49financial/platinum/advisor_books/advisor_id=A123), each token 'mdpf' / 'VERDICT: FAIL-TWO-REFERENTS', rc=0. The list is capped at clash[:5] (check_ln.py:317) and the count is 5, so none is hidden.",
   "CHECKER: deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py:305-317 @777770e6aa e5_consistent collects every mark other than 'none', splits each name on [-/=.], and records a clash wherever a marked token is a token of a name whose own mark differs."
  ],
  "remedy": "Seat blind cells in a context that loads neither CLAUDE.md nor the auto-memory, or rule that the measure cannot be taken inside this fabric (1.0.0_SA_CTO, fabric); give blind cells a row-id path that does not read the channel (1.0.0_SA_CTO, worker definition); re-cut LN-e-4/LN-e-5 so the reader's question and the key's rule are one rule and E5-AC1/E5-AC2 are jointly satisfiable (2.0.0_SA_COO~G at the recut). FWD-2 is NOT EVALUATED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S13",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Issuer's MEASUREMENT of W5-S4: LN-e-5's two criteria cannot both pass as cut. A reader whose every mark equals N3_KEY.json passes E5-AC1 by construction and still FAILS E5-AC2 with 2 clashes (etfs-price-refresh-dlq and etfs-pipeline-alerts, both keyed none, while i11 is keyed etfs). So E5-AC2's FAIL on the live reader is not evidence against that reader alone.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-S13",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S6",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "INSTRUMENT: the e5_consistent loop of org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py:305-317@1a06d8ce3f, executed by the issuer over a key-perfect reader -- namer A's 18 names from deliverables/exercises/n3-namer-a.tsv@1a06d8ce3f, each marked with its N3_KEY.json value. Output: 'KEY-PERFECT READER: rows=18 marked_tokens=9 clashes=2', verdict FAIL-TWO-REFERENTS.",
   "THE CLASHES: name=etfs-price-refresh-dlq token=etfs mark=none; name=etfs-pipeline-alerts token=etfs mark=none. N3_KEY.json@777770e6aa keys i11 (ECS_TASK_DEFINITION, the Pathfinder ingest FOR the ETF product) as etfs, and i08 and i17 (resources SHARED by every firm whose system is the ETF product) as none."
  ],
  "remedy": "Seat blind cells in a context that loads neither CLAUDE.md nor the auto-memory, or rule that the measure cannot be taken inside this fabric (1.0.0_SA_CTO, fabric); give blind cells a row-id path that does not read the channel (1.0.0_SA_CTO, worker definition); re-cut LN-e-4/LN-e-5 so the reader's question and the key's rule are one rule and E5-AC1/E5-AC2 are jointly satisfiable (2.0.0_SA_COO~G at the recut). FWD-2 is NOT EVALUATED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W5-S1",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "LN-l-3's L3-AC1 invocation (check_ln.py l3-correct) prints VERDICT: FAIL-MISREAD, not the expected PASS-ALL-CORRECT: 5 of 6 conforming N5 addresses are labeled as N5_KEY reads them, and the one miss is a3, the v1.3 code-tier specimen, which the reader marked DOES-NOT-FIT where the key reads bucket,source,scope,tier,table,partition.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S1",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S7",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py l3-correct, 2026-09-14 ~16:5xZ, worktree HEAD 179884e46b -> 'WRONG: a3  labeled=DOES-NOT-FIT  expected=bucket,source,scope,tier,table,partition' / 'CONFORMING ADDRESSES: 6  CORRECT: 5  WRONG: 1' / 'VERDICT: FAIL-MISREAD', rc=0. The sibling criterion L3-AC2 (l3-control) printed 'VERDICT: PASS-CONTROL-FLAGGED', 1 of 1.",
   "ANSWER: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n5-reader.tsv:3 @15c38055ca 'a3<TAB>DOES-NOT-FIT'; the reader's reason, deliverables/0.9.0_WK_LGIC_NAMING~4/cross-bucket-reader.result.md:18 @15c38055ca: '6 segments. After code in the tier slot, the table slot holds a second tier word (gold), and there is no partition'."
  ],
  "remedy": "Rule whether key.code is a layout FWD-4 admits (then the briefing teaches it and LN-l-2 re-runs) or a second layout FWD-4 forbids (then the schema changes). FWD-4 is REALIZED on 5 of 6 specimens and NOT on the code tier.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W1-S3",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "grade.OUT-OF-PATTERN prints a canonical form, but three live name classes do not carry a slot that form needs -- a firm or other non-system first token with no system token anywhere in the name, an S3Key node name that carries no bucket (so no source or scope), and an event rule or schedule with no cadence token -- so GRADING_RULE.md prints those canonical forms with a {system}, {source}, {scope} or {cadence} placeholder.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S3",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S8",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "DATA: org/standards/NAMING_SCHEMA.json v1.4 grade.OUT-OF-PATTERN: 'the grammar fails (order, separator, case, a missing or unknown kind, a firm in the system slot); canonical_form is printed'.",
   "CENSUS: infra/logic/09_NAMING_CENSUS.md s.1 item 3(c): a firm token at position 0 'as if the firm were the system' in Lambda 47, role 55, rule 45, log 57 names; header: 'the live graph's 382 S3Key nodes are name-grain served-graph nodes without bucket ARNs'."
  ],
  "remedy": "Rule whether grade() takes the registry, bucket and schedule as inputs or FWD-5's 'correct name' limb admits placeholders (1.0.0_SA_CTO); exclude AWS-issued names in the data file (1.0.0_SA_CTO); add the step field to the N6 answer format (2.0.0_SA_COO~G at the recut).",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W1-S4",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Names AWS fixes sit inside three graded types with no exclusion in NAMING_SCHEMA.json -- the VPC default security group 'default' (1 of 26 SECURITY_GROUP), 9 of 417 IAM_POLICY names beginning AWS or Amazon, and 4 of 264 LOG_GROUP names (aws-waf-logs-*, RDSOSMetrics, /aws/ecs/containerinsights/*) -- so GRADING_RULE.md RAISEs them by name shape, and cannot see an AWS-managed policy without the prefix (ReadOnlyAccess is live).",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S4",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S8",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "DATA: org/standards/NAMING_SCHEMA.json v1.4 types_not_graded_by_kind and not_covered exclude AWS-issued identifiers by TYPE only (KMS_KEY, CLOUDFRONT_DISTRIBUTION, SERVICE_PRINCIPAL, VPC_ENDPOINT); SECURITY_GROUP and IAM_POLICY are kind.by_type keys, and LOG_GROUP is graded as derived.",
   "LIVE_NAMES.json (vintage 2026-09-14 12:13:53 UTC), counted by python over by_type: SECURITY_GROUP 'default' 1 of 26; IAM_POLICY AWSDataLifecycleManagerServiceRole, AWSLambdaBasicExecutionRole, AWSLambdaVPCAccessExecutionRole, AmazonDynamoDBFullAccess, AmazonEC2ContainerRegistryFullAccess, AmazonECSTaskExecutionRolePolicy, AmazonRDSEnhancedMonitoringRole, AmazonS3ReadOnlyAccess, AmazonSSMManagedInstanceCore = 9 of 417; LOG_GROUP /aws/ecs/containerinsights/opal-globgrph/performance, RDSOSMetrics, aws-waf-logs-opal-cloudfront, aws-waf-logs-opal-gateway = 4 of 264; ReadOnlyAccess present in IAM_POLICY with no prefix."
  ],
  "remedy": "Rule whether grade() takes the registry, bucket and schedule as inputs or FWD-5's 'correct name' limb admits placeholders (1.0.0_SA_CTO); exclude AWS-issued names in the data file (1.0.0_SA_CTO); add the step field to the N6 answer format (2.0.0_SA_COO~G at the recut).",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W5-S5",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "LN-h-3 has to trace each RAISE to the rule line it exposes, but neither N6 answer file records which step raised. The fourth field is empty on all 18 RAISE rows of n6-grader-a.tsv and n6-grader-b.tsv, and the files have no step column. Grader B named the step for each RAISE in its result file, and grader A did not. So n6-compare.md takes its step column from grader B's result file, which is not on the order's read list.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W5-S5",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S8",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md:26-27 @51b0952d71 -- 'RAISE -- the name cannot be placed. This is a defect in this rule, the data file or the registry, and the output names the step that raised (DATA.grade.unplaceable).'",
   "ANSWER FILES: deliverables/exercises/n6-grader-a.tsv @388b07f486 and n6-grader-b.tsv @40f445d92c are byte-identical (cmp rc=0, sha256 41c3de9d62f9c371b810dfaead0dd6bf4053f50b13e45588842d8e865ffde945). Each row is type, name, verdict, canonical_form. All 18 RAISE rows (17 discriminating and 1 overlap, ECS_CLUSTER opal-globgrph) have an empty canonical_form field, and no row names a step."
  ],
  "remedy": "Rule whether grade() takes the registry, bucket and schedule as inputs or FWD-5's 'correct name' limb admits placeholders (1.0.0_SA_CTO); exclude AWS-issued names in the data file (1.0.0_SA_CTO); add the step field to the N6 answer format (2.0.0_SA_COO~G at the recut).",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W1-S5",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "LN-f-1's output shape has two dispositions for a firm-token role, attributed (with a canonical form) or excluded (as no firm's principal); wp5-49f-feeder-scheduler-role fits neither -- its 49f token names 49 Financial, and GRADING_RULE R1.f RAISEs it (wp5 is in no vocabulary), so it has no canonical form. It is filed under excluded with a reason saying exactly that.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@d292bca3ba#LGIC_NAMING-W1-S5",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md (same slug) row LGIC_NAMING-C-S9",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND1_L8_L9_20260914.md (same slug) section 2",
   "LIVE_NAMES.json (vintage 2026-09-14 12:13:53 UTC), counted by python over by_type.IAM_ROLE: 240 roles, 69 carry a firm alias token split on - and _; graded by GRADING_RULE.md R1-R6: 68 to a canonical form, 1 RAISE (wp5-49f-feeder-scheduler-role).",
   "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@3d671ff59c R1.f 'Any other t1 is in no vocabulary. RAISE'; V3 lists the workstream codes wsb and wsd only; V1 and V2 do not carry wp5."
  ],
  "remedy": "A third disposition (RAISE, with the step) in LN-f-1's shape and its checker before LGIC_ENFORCE E9 consumes the list.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 }
]
```
