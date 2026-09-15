# LGIC_NAMING -- surprise channel, INVESTIGATION v1

**Opened by:** `1.0.0_SA_CTO` at L4-R, 2026-09-13. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only.**

**Why this file is opened before L5.** The first row was found while this project's PRD sat at L4-R: both review
halves moved only after the author relayed them by hand, and the reason is a mismatch between what the spine says the
L4 notifier does and what reaches a reviewer. That is a surprise, so it is a row, not a message.

**Denominator at this write: 5 rows** -- `LGIC_NAMING-S1` and `LGIC_NAMING-S2` (the disarm of S1's mechanism, carried as a
new row on 3.0.0_SA_CVO's ask 96495), both 1.0.0_SA_CTO; `LGIC_NAMING-S3`, `LGIC_NAMING-S4` and `LGIC_NAMING-S5`, all 2.0.0_SA_COO~G at L5.

```json
[
  {
    "id": "LGIC_NAMING-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-13T23:05Z",
    "one_line": "The L4 notifier's [L4-R REVIEW] requests are sent on the broker HTTP plane only and never land as inbox files, so a reviewer whose inbox monitor watches files never sees them; both halves of LGIC_NAMING's PRD moved only after hand relays.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- per PRD, by the author's hand relay of each owed half (DONE for both halves of LGIC_NAMING: 4.0.0_SA_CRO~D at 2026-09-13T22:24Z, 3.0.0_SA_CVO at 22:55Z); for the mechanism, as the author of the notifier's current version (.tools/prd-header-notify.py @fbfe03afe8, 2026-09-11)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: .tools/prd-header-notify.py:314-335 @fbfe03afe8, send(): 'Deliver through the broker's HTTP /send-message and return its message_id ... NOT codex-send.py. That path delivers through the broker LIBRARY in-process (its receipt says \"(filesystem)\"), and the ledger that /delivery-state and /ack-messages read never sees the message.' The notifier chose the ledgered plane on purpose, so its READ ack can be read; the file plane is the one it does not take.",
        "BROKER LEDGER, get_delivery_state 2026-09-13 ~22:5xZ: 96415 (v1.0) and 96421 (v1.1) to 3.0.0_SA_CVO both OFFER-EXHAUSTED, SENT, never READ; 96416 to 4.0.0_SA_CRO QUEUED, no clock stamps.",
        "FILE PLANE: org/mcp/inbox/3.0.0_SA_CVO (top and read/) holds 0 files stamped 22:15Z-22:54Z. Across every inbox file stamped since 2026-09-10 (2,929 scanned), exactly 2 carry an [L4-R REVIEW] subject, both hand-sent by 1.0.0_SA_CTO at 2026-09-11T04:20:14Z; none is a notifier send.",
        "POSITIVE CONTROL on the same recipients: messages sent through the MCP send_message path in the same hours landed as files and were read (e.g. 96391, 96412 to 3.0.0_SA_CVO; 96392 and the LGIC_NAMING relay to 4.0.0_SA_CRO~D, which 4.0.0_SA_CRO~D answered with a review within ~8 minutes).",
        "NOT MEASURED: the notifier state file org/mcp/.prd-notify/outstanding.jsonl holds 14 rows whose send times this seat did not parse, so no count of the notifier's sends since 2026-09-10 is claimed; nor whether the overdue re-offer and nudge path uses the same plane (read from the code, it calls the same send())."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine L4 (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md): the notifier 'delivers each HALF of a new or bumped PRD that is not already signed at its current bytes to the reviewer ROUTED for it ... re-offers until READ, nudges an overdue half with the CTO copied, and re-routes an overdue brief half to a live COO'.",
    "world_is": "The notifier's messages reach the broker ledger (SENT) but not the reviewer's inbox folder, which is the plane a seat's persistent inbox monitor watches. On LGIC_NAMING both review requests to 3.0.0_SA_CVO exhausted their offers unread, and neither half moved until the author sent the same request through the MCP path. L4-R therefore depends on an author remembering to relay by hand -- the notifier is the mechanism the spine names, and it is not the one that is working.",
    "notes": "OBSERVATION, not BLOCKING: the hand relay works, and was done for this PRD. ARMED because every PRD's L4-R has the same exposure and nothing in the estate relays on the author's behalf. Remedy options, not chosen here: the notifier also writes the recipient's inbox file beside the ledgered send (both planes, one message id), or the persistent inbox monitor also drains the broker queue. Either is a change to shared tooling outside LGIC_NAMING's scope."
  },
  {
    "id": "LGIC_NAMING-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-14T04:38Z",
    "one_line": "DISARM of LGIC_NAMING-S1's mechanism: the L4 notifier now writes the recipient's inbox file beside its ledgered send, under the same Msg-ID (.tools/prd-header-notify.py @2c964ca3a3), so an [L4-R REVIEW] reaches a seat's inbox monitor without a hand relay.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: .tools/prd-header-notify.py @2c964ca3a3 -- _inbox_dir() routes as org/mcp/server.py's _resolve_agent_folder + _deliver_to_one (the agent folder by base serial across org/tier*, a ~suffix nested at inbox/<folder>/~<suffix>/); _write_inbox_file() writes the broker's file shape plus the Msg-ID line, through a dot-named temp file and a rename; send() calls it after the ledgered send and WARNs rather than raising on a file-plane failure, so the next re-offer writes it again.",
        "EXERCISED: python .tools/prd-header-notify.py selftest -> 0 defect(s), 2026-09-14 ~03:45Z. Probe 96484 landed as exactly 1 inbox file carrying Msg-ID 96484 under org/mcp/inbox/1.0.0_SA_CTO, 1.0.0_SA_CTO's persistent inbox monitor fired on it (20260914T034528Z), and delivery_state read QUEUED before the ack and READ after it -- the file plane and the ledger ack on one message id.",
        "NEGATIVE ARM, from S1's own grounding: before the fix, 0 of 2,929 inbox files stamped since 2026-09-10 were notifier sends.",
        "NO BACKLOG RE-SENT: prd-header-notify.py status after the fix -- 15 outstanding rows, 10 at attempts=6 (no further re-offer) and 5 withheld COO deliveries still UNSENT; the inboxes of 3.0.0_SA_CVO, 4.0.0_SA_CRO, 4.0.0_SA_CRO~D and the COO lanes held no new notifier file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_NAMING-S1: the notifier's review requests reach the broker ledger and no reviewer's inbox folder, so L4-R depends on the author's hand relay.",
    "world_is": "The notifier writes both planes under one message id; the first request to arrive this way will be LGIC_ENFORCE's L4-R review. The broker's HTTP /send-message path is unchanged, so no other HTTP sender's behaviour moved.",
    "notes": "Carried as a NEW row, not an in-place edit of S1, on 3.0.0_SA_CVO's ask (96495): the channel is append-only and S1's ARMED record stands as written. 3.0.0_SA_CVO dispositions S1 against this row at LGIC_NAMING's first L8. Broadcast of the fix: 96489-96494."
  },
  {
    "id": "LGIC_NAMING-S3",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T07:55Z",
    "one_line": "The spine's L6 queue rule puts dependent cells in ONE worker's queue, but this PRD's N3 and N6 exercises need DIFFERENT workers on dependent cells (graders who did not write N2; namers who never confer), so the L5 decomposition serialises those cells by spawn-after-drain and supports a fan-out N above its chain count M.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC: org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:240-241 @0749183a0c (L6): 'Two task orders on one chain belong to one worker's queue; two chains may take two workers.' And .claude/skills/dispatch/SKILL.md:43-45: 'two task orders on one chain belong to ONE worker's queue ... So N is bounded above by M'.",
        "PRD: org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md @d6e0c3b74a, CELL CANDIDATES row N6: 'two workers who did not write N2 each grade the same sample of real live names'; row N3: 'two workers, briefed only with the schema and the registry seed, each name the same set of new resources ... without conferring; a third reads a set of conforming names'.",
        "THE CONFLICT, read from the two texts together: N6's graders depend on N2's rule, so the grading cells sit on the rule's chain, and under the queue rule the worker who wrote N2 would grade it -- the one thing N6 forbids."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine L6 and /dispatch: two task orders on one chain belong to one worker's queue, so the number of workers N is bounded above by the number of dependency-independent chains M.",
    "world_is": "LGIC_NAMING's hand-proof exercises need blind, distinct workers on cells that depend on each other: the N2 author may not grade, the two graders may not see each other, the two namers may not confer, and the reader may not have seen the items. The L5 decomposition (LGIC_NAMING_DECOMP.md v1, section 5) keeps the dependency edges but serialises them by spawning a dependent cell's worker only after its input's branch is merged, and supports N up to 8 over M = 5 chains, with the reason 'blindness'.",
    "notes": "OBSERVATION, INERT: nothing breaks, and the decomposition's resolution is stated where L6 will read it. Surfaced so the CVO and the CTO can judge whether the spine's queue rule should name an exception for exercises whose validity is the workers' independence, or whether this project's reading is wrong. Not a request to change the spine."
  },
  {
    "id": "LGIC_NAMING-S4",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T07:55Z",
    "one_line": "FWD-4's second clause (every older written description of a different layout says plainly that it has been replaced) cannot grade REALIZED inside this project's rounds: the PRD gives the docs/architecture/MDPF_CANON_PRD.md s.3 notice to MDPF_CANON's owner at MDPF_CANON's own L4, and MDPF_CANON reads dep_stage REGISTERED, held in sequence stage 2 behind LGIC_ENFORCE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md @d6e0c3b74a, SURFACE MANIFEST row 'docs/architecture/MDPF_CANON_PRD.md s.3 | text edit | N5 | MDPF_CANON, at its own L4', and PATHS row 'the replacement notice, landed by its owner at MDPF_CANON's L4'. FWD-4's ACCEPT line: 'and every older written description of a different layout says plainly that it has been replaced'.",
        "STATE: git show HEAD:org/missions/D8/MDPF/MDPF_CANON/project.json, read 2026-09-14 ~07:3xZ: dep_stage REGISTERED, prds ['docs/architecture/MDPF_CANON_PRD.md'].",
        "SEQUENCE: org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:27 at HEAD: 'This project's own admitted PRD is the first half of the hold on ADVI_FIRMBKTS (held at DECOMP) and MDPF_CANON (held at REGISTERED). The second half is DEC-4's fence, applied on the template.'",
        "ON-DEMAND ACT EXISTS: docs/architecture/MDPF_CANON_PRD.md is under the docs/architecture/** ANY_CTO catch-all (.owned-paths.yaml at HEAD, the notes on the INFLEC_*, INFETL_* and ADVI_FIRMSEP_* carve-outs name it) and last changed at 6e0a07d934 (2026-08-27), so 1.0.0_SA_CTO can write the notice in its own lane at any time. This seat did not open s.3."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 27, L2: 'NO FWD IS A WAIT -- every outcome is provable by an act a seat can take ON DEMAND ... a genuinely essential wait is EXPRESSLY QUALIFIED on the outcome with its reason and Andrew's word.'",
    "world_is": "FWD-4 carries no such qualifier, yet half of its evidence is sequenced behind another project's L4, which is itself held behind LGIC_ENFORCE's applied fence. LGIC_NAMING's close (every FWD REALIZED) therefore waits on sequence stage 2, although the act -- one replacement notice in a file in 1.0.0_SA_CTO's own lane -- can be taken on demand. The L5 decomposition cuts the .tf half of N5 (LN-l-1) and registers the s.3 half as gate G-A owned by 1.0.0_SA_CTO. It cuts no cell there, because the PRD names that file's owner.",
    "notes": "OBSERVATION, INERT: nothing breaks, and the round is not blocked. Remedy options, not chosen here, both 1.0.0_SA_CTO's: land the s.3 notice now in its own lane (S1 already carries the text it would cite), or qualify FWD-4 with the wait by an L10 addendum. A decomposition is not the place to cut a cell into another project's PRD."
  },
  {
    "id": "LGIC_NAMING-S5",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T08:15Z",
    "one_line": ".tools/prd-stamp.py records a stamp's prd_pin as the SHA-256 of the PRD's CHECKED-OUT bytes, so on this autocrlf box the L5 stamp written from a fresh linked worktree pins the CRLF copy (40f301d126b4), not the committed record (4df5e19624d2); two seats stamping one unchanged PRD from differently configured checkouts record different pins.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ARTIFACT: org/missions/D14/LGIC/LGIC_NAMING/prd/stamps/L5.json, written by 'python .tools/prd-stamp.py stamp ... --stage L5' under 2.0.0_SA_COO~G at 2026-09-14T08:08Z in the linked worktree .worktrees/coo-g-lgic-naming-l5: prd_pin 40f301d126b4.",
        "MEASURED, same worktree, same minute: sha256sum of the checked-out PRD = 40f301d126b4, and that copy carries 248 CR bytes; 'git show HEAD:<prd> | sha256sum' = 4df5e19624d2; 'git cat-file -t 40f301d126b4' = not a valid object. The PRD's blob is b83111f135 at both HEAD and d6e0c3b74a, so the record did not move -- only the checkout's line endings differ.",
        "NOT MEASURED: the stamp verb's source line that computes the pin (read from its behaviour, not its code); whether 'prd-stamp.py status' compares a pin to the record or to a checkout; the pins of any other project's stamps."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A stamp's prd_pin identifies the PRD bytes the stage owner stamped, so the next owner can tell whether the PRD moved since (the prd-stamp.py docstring: a SIGNED, TIMESTAMPED stamp the NEXT owner reads instead of a message; the sign verb's pin is the PRD's last-touching commit).",
    "world_is": "The stamp verb hashes the working-tree bytes. On a core.autocrlf checkout those carry CRLF, so the pin matches neither the record's hash nor another checkout's, and a reader comparing it against the record would see a moved PRD that did not move.",
    "notes": "OBSERVATION, INERT: the stamp is advisory by its own docstring and nothing gates on this pin that this seat knows of. Remedy options, not chosen here, the tool owner's: hash the committed bytes (git show HEAD:<prd>), or normalise line endings before hashing, or pin the last-touching commit as the sign verb does. Found while landing LGIC_NAMING's L5 stamp; the same trap class as hashing a linked worktree's checkout on this box."
  },
  {
    "id": "LGIC_NAMING-S6",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-14T09:32Z",
    "one_line": "NAMING_SCHEMA.json key.partition admits only 'date=YYYY-MM-DD' and 'a named leaf', so an ENTITY-KEYED served file -- a book per advisor, a view per client or account, written today at platinum/advisors/{id}/book.json -- has no form the builders can produce, and ADVI_FIRMBKTS's cutovers cannot write that family without a hand-spelled key.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- as the author of LGIC_NAMING's PRD and data file: an L10 addendum that admits (or refuses, with the family's alternative stated) a hive entity partition '{entity}={id}' in key.partition; until then ADVI_FIRMBKTS writes no key in that family (its PRD v1.0 DEC-1, DEC-16)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA: org/standards/NAMING_SCHEMA.json v1.2, key.partition = ['date=YYYY-MM-DD', 'a named leaf'], key.leaf = '{object} -- the file under {partition}', key.grammar = '{source}/{scope}/{tier}/{table}/{partition}' (read 2026-09-14 ~09:2xZ).",
        "BRIEF: docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md @2b64208047 IV.5 worked string 'opal-data-49financial/advi/49financial/platinum/advisors/{id}/book.json', and IV.3 class (a) 'platinum/{firm,advisors,clients,accounts}/...' -- per-entity served JSON is a live family in the three legacy buckets.",
        "CANON: infra/logic/02_DOCTRINE.md R2 non-application -- 'an entity id INSIDE a partition or key (date=.../account_id=...) is correct' -- so a hive entity partition does not break the scope-segment law; it is the schema's enumeration that does not list it.",
        "CONSEQUENCE: LGIC_ENFORCE's key() returns exactly five segments (its PRD v1.1 CONTRACTS and E3), so with a named leaf the entity id has no slot; the only builder-free form is a hand-spelled key, which that project's gate refuses once enforcing and its brief's Part V forbids in a migration."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_NAMING S1 and the data file's key.partition: a key's fifth segment is a date partition or a named leaf, and every new key is produced by the builders.",
    "world_is": "The estate serves per-entity JSON (per advisor, client, account) under platinum/, and ADVI_FIRMBKTS must move that family into the firm buckets. Neither partition form carries an entity id alongside a named file, so the family cannot be written through the builders until the schema admits a form for it.",
    "notes": "Raised by 1.0.0_SA_CTO while writing ADVI_FIRMBKTS's L4 PRD, after 4.0.0_SA_CRO refused MDPF_CANON v2.0 for the same class of mismatch (a declared address the builders cannot return). The proposal carried in ADVI_FIRMBKTS DEC-1 is '{source}/{firm}/platinum/{table}/{entity}={id}/{leaf}.json'; the decision is LGIC_NAMING's."
  },
  {
    "id": "LGIC_NAMING-S7",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-14T10:05Z",
    "one_line": "One family, two addresses: NAMING_SCHEMA.json v1.2 lists 'code' in key.tier, so key() would place a code object at {source}/{scope}/code/{table}/{partition}, while doctrine R1's non-application and R16 keep a ROOT code home code/{source}/gold/ (the D8 migration brief's own vector: opal-data-49financial/code/advi/gold/...), which no builder returns -- and ADVI_FIRMBKTS must move the three legacy buckets' code/gold/** to one of them.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- as the author of LGIC_NAMING's PRD and data file: an L10 addendum that rules ONE construction for code (either the schema's code tier, with doctrine R1's code/ non-application amended through LGIC_CANON, or the root code home, with 'code' removed from key.tier and its builder named); until then ADVI_FIRMBKTS writes no code object (its PRD v1.1 DEC-2, DEC-16, DEC-17), and MDPF_CANON writes no new code packaging (its PRD v2.3 M6)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA: org/standards/NAMING_SCHEMA.json v1.2 key.tier = ['bronze', 'silver', 'gold', 'platinum', 'state', 'code'], key.grammar = '{source}/{scope}/{tier}/{table}/{partition}' (read 2026-09-14 ~09:5xZ).",
        "CANON: infra/logic/02_DOCTRINE.md:103 R1 non-application 'code/ prefixes (R16)'; :275 R16 'ONE CODE HOME PER PIPELINE, in the product or firm bucket beside the gold code (R5)'; :279 census 'code/{bronze,silver,gold}/ in bd, cot, inf, mdpf CONFORMANT on the principle'.",
        "BRIEF: docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md @2b64208047 IV.5 (line 217) '(f) opal-data-49financial/code/advi/gold/... <- R16, one code home' and IV.6 (line 240) 'code/gold/** -> code/{source}/gold/**'.",
        "REVIEW: 4.0.0_SA_CRO's ADVI_FIRMBKTS v1.0 brief refusal R2, docs/briefs/sources/ADVI_FIRMBKTS_L4_BRIEF_REVIEW_v1_0_20260914.md @3454bdc77e: 'The consumed ENFORCE builder contract (152) returns exactly {source}/{scope}/{tier}/{table}/{partition} and derives the bucket; it cannot return the stated root-code destination with the same arguments.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NAMING_SCHEMA key.tier includes 'code', so a code object's address is {source}/{scope}/code/{table}/{partition}, produced by key() like every other new address.",
    "world_is": "The canon keeps code/ prefixes outside the grammar (R1 non-application, R16), and the migration brief places code at the bucket root under code/{source}/gold/. The schema and the canon give two different addresses for the same object, and the builder can produce only the schema's.",
    "notes": "Raised by 1.0.0_SA_CTO while absorbing 4.0.0_SA_CRO's refusal of ADVI_FIRMBKTS v1.0 (R2). Sibling of LGIC_NAMING-S6: both are families the builders cannot construct as the migration brief spells them. ADVI_FIRMBKTS v1.1 holds the family and leaves the runners on the legacy code home until this resolves. The same conflict sits in MDPF_CANON v2.2 (4.0.0_SA_CRO R4, review @436c1da148): its M6 packages new code at s3://opal-data-mdpf/code/ while its CONTRACTS require every new address from the builders."
  },
  {
    "id": "LGIC_NAMING-S8",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T09:58Z",
    "one_line": "NAMING_SCHEMA.json key.table_case says a platinum leaf is a kebab-case .json file '(the served names)', but 12 of the 15 ADVI served leaves the portal lists are snake_case (header_metrics.json among them), so ADVI_FIRMBKTS's platinum vector keeps a name the schema refuses while MDPF_CANON's sibling vector obeys the rule.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO -- as the author of LGIC_NAMING's PRD and data file: an L10 addendum that either admits a legacy served name byte-for-byte under the platinum leaf rule, or keeps the kebab rule and states that a migration renames the object behind a per-leaf edge mapping; until then ADVI_FIRMBKTS's platinum vector has no ratified case rule (its ratified-text half REFUSED on this at v1.0, review @10729854d0, and again at v1.1 @2a9ae97c19)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA: org/standards/NAMING_SCHEMA.json v1.2 @d6e0c3b74a :35 table_case = 'snake_case; a platinum leaf is a kebab-case .json file (the served names)'; :27 leaf = '{object} -- the file under {partition}'; :36 partition includes 'a named leaf'.",
        "PRD: org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md :125 (S1) 'Tables are snake_case; a platinum leaf is a kebab .json.'",
        "WORLD: portal @3ade1aba src/api/endpoints/adviKeyRepoint.ts lists 15 served leaves: 12 snake_case, 1 kebab-case (clients-tab-slim.json), 2 single-word; src/api/endpoints/advisor-intelligence.ts:302 requests /api/scoped/advisor-intelligence/platinum/firm/header_metrics.json.",
        "SIBLINGS: ADVI_FIRMBKTS_PRD.md v1.0 @ecac007bf3 and v1.1 @2a9ae97c19 CONTRACTS vector (byte-identical in both) key('advi', '49financial', 'platinum', 'firm', 'header_metrics.json'); MDPF_CANON_PRD.md v2.2 @ef21e34660 CONTRACTS vector key('mdpf', '49financial', 'platinum', 'aum_metrics', 'aum-metrics.json')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_NAMING S1 and NAMING_SCHEMA key.table_case: a platinum leaf -- the served name -- is a kebab-case .json file.",
    "world_is": "Most ADVI served names are snake_case and the frozen portal requests them by those names. Keeping them breaks the schema's case rule; renaming them needs an edge name mapping per leaf. The schema does not say which, and the two D8 PRDs read it differently.",
    "notes": "Filed with 3.0.0_SA_CVO's L4-R refusals of ADVI_FIRMBKTS's ratified-text half at v1.0 and v1.1 (R1); held here rather than committed at 09:58Z because 1.0.0_SA_CTO's S7 was uncommitted in the shared tree. The denominator is the portal's served-leaf list, not a bucket census. Same class as LGIC_NAMING-S6: an address the schema does not admit."
  },
  {
    "id": "LGIC_NAMING-S9",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-14T11:01Z",
    "one_line": "prd-stamp.py status renders the L4-R sign-offs VERSION-bound while prd-signoff.py and LIMB 6 bind each half to its HASH: on LGIC_NAMING v1.3 @7bd4ef6f27, prd-signoff reads the ratified-text half SIGNED current (3.0.0_SA_CVO signed v1.2's byte-identical half) and prd-stamp status prints 'sign-off CVO -- not signed at v1.3', so the next owner reading the stamp ledger sees a signature owed that is not.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TOOL, 2026-09-14 ~10:5xZ, same HEAD: 'python .tools/prd-signoff.py status LGIC_NAMING' -> 'v1.3 @7bd4ef6f27 ADMITTED; ratified-text SIGNED 3.0.0_SA_CVO current; brief SIGNED 4.0.0_SA_CRO current'; 'python .tools/prd-stamp.py status <PRD>' -> 'sign-off CRO 4.0.0_SA_CRO SIGNED v1.3' and 'sign-off CVO -- not signed at v1.3 (owner 3.0.0_SA_CVO)'.",
        "CODE: .tools/prd-stamp.py _signed_reviewers(signoff_files, prd_version) keeps a reviewer only when its sign-off file's prd_version equals the PRD's; its own self-test asserts 'version-bound -- CVO signed v0.3 -> only CRO'. The comment beside it says it 'mirrors LIMB 6's predicate'.",
        "LAW: CLAUDE.md Rule 27 (spine v3.15): each half is signed 'bound to the HASH of its sections, never to prd_version'; one rule for all three tools, .tools/prd_signoff_lib.py."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "prd-stamp.py status shows the next owner what L4-R still owes, mirroring LIMB 6's predicate.",
    "world_is": "LIMB 6's predicate moved to hash-bound halves (prd_signoff_lib, spine v3.15); prd-stamp's mirror stayed version-bound. After any bump that leaves a half's bytes unchanged, it reports the carried half as unsigned.",
    "notes": "INERT: no gate reads prd-stamp's sign-off view; LIMB 6 and the notifier use prd_signoff_lib. Found by 1.0.0_SA_CTO while verifying the S5 fix (@b09ed6c736) against this PRD. Remedy, the tool owner's (1.0.0_SA_CTO, whose ~Z lane wrote it): have _signed_reviewers take prd_signoff_lib's per-half status instead of comparing prd_version."
  },
  {
    "id": "LGIC_NAMING-S10",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T11:10Z",
    "one_line": "NAMING_SCHEMA v1.3's key.legacy_served_path makes a platinum key's verdict depend on whether it is a LEGACY served path (bytes kept) or a NEW one (kebab and hive forms bind), but that is not a property of (name, type) -- the grade's ratified signature -- and no field of v1.3 lists the legacy set, so two hand graders, or grade() and a grader, can reach different verdicts on the same key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA FILE: org/standards/NAMING_SCHEMA.json @7bd4ef6f27, key.legacy_served_path: 'below {source}/{scope}/platinum/, a LEGACY served path keeps its bytes -- the table, a bare entity-id segment in the partition slot, and the file name -- because the frozen portal requests it by path; the kebab-case and hive forms bind NEW served families only'. key.table_case: 'a NEW platinum leaf is a kebab-case .json file'. grade.signature is unchanged: '(name, type) -> (verdict, canonical_form)'.",
        "NO ENUMERATION: git diff d6e0c3b74a 7bd4ef6f27 -- org/standards/NAMING_SCHEMA.json adds key.legacy_served_path and key.code as prose and adds no field listing which served paths are legacy.",
        "CONTRACT: org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md CONTRACTS row 2 is byte-unchanged at v1.3 (the same diff touches only S1 and prd_version): 'the grading rule, (name, type) -> (verdict, canonical_form)'. FWD-5 ACCEPT: 'two people apply the written rule by hand to the same set of real names ... and reach the same answer for every one'.",
        "WHERE THE SET LIVES TODAY: outside the data file -- the CTO adjudication @7bd4ef6f27 cites '12 of 15 ADVI served leaves (3.0.0_SA_CVO's read)' and 'adviKeyRepoint.ts:37 @portal 3ade1aba'. Not measured by this seat: the portal's full request list, or how many legacy served paths exist estate-wide."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The grade is a function of (name, type) (NAMING_SCHEMA grade.signature; CONTRACTS row 2, SIGNED ratified text), exact enough that two people applying it by hand get the same answer (FWD-5).",
    "world_is": "Under v1.3 a snake_case leaf or a bare entity-id segment below {source}/{scope}/platinum/ is CONFORMANT when it is a legacy served path and OUT-OF-PATTERN when it is new, and the name does not say which. The deciding set -- what the frozen portal requests -- lives in portal source and in 3.0.0_SA_CVO's read, not in the data file. A smaller second instance: key.code's legacy root code/ homes 'stay until their pipelines move' without saying whether they grade OUT-OF-PATTERN with a canonical form or are outside the grade.",
    "notes": "OBSERVATION, INERT for this project's round: LGIC_NAMING decomposition v2 (section 0) makes LN-g-1's written rule enumerate the legacy served set it applies, source named and denominator printed, and state a verdict for a legacy root code/ key, so LN-h-1 and LN-h-2 grade from one list. The contract question stays open and is 1.0.0_SA_CTO's (the author of the data file and of CONTRACTS row 2): whether the legacy set becomes a data field, or grade()'s signature gains it as an input. LGIC_ENFORCE's grade() inherits whichever is chosen. Remedy not chosen here."
  },
  {
    "id": "LGIC_NAMING-S11",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T14:25Z",
    "one_line": "Decomposition v3 section 3a.4 states the N6 sample as 86 discriminating + 3 OVERLAP names, computed from per-type NODE counts; the stated rule applied to the type's distinct NAMES gives 85 + 3, because ROUTE53_RECORD's 3 nodes carry 2 distinct names (opalinvest.dev twice). The L6 issuance cuts 85 + 3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC: org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md v3 @62b5c0819f, section 3a.4: the rule (positions 1, ceil(n/2), n when n >= 4; 1 and n when n = 3; 1 when n = 2; OVERLAP when n = 1) and the line 'At vintage 2026-09-14 05:54:17 UTC that is 27 types x 3 + ROUTE53_RECORD 2 + VPC_ENDPOINT 2 + CLOUDFRONT_DISTRIBUTION 1 = 86 discriminating names, plus 3 OVERLAP'.",
        "MEASURED: comp-find --corpus aws '.' --all at vintage 'Built from the estate as of 2026-09-14 12:13:53 UTC' (manifest b578e47d733f): 2,531 nodes over 33 types. ROUTE53_RECORD has 3 nodes and 2 unique names (opalinvest.dev appears twice). The rule over node counts gives 86 + 3; over unique names it gives 85 + 3. Other types with duplicate names (API_ROUTE, EC2_INSTANCE, IAM_POLICY, S3Key, SECURITY_GROUP) stay at 3 positions either way.",
        "WHY UNIQUE NAMES: two nodes with one name grade identically, and the graders' answers are keyed by (type, name), so a duplicate adds no discrimination and could not be told apart in the comparison."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition v3 section 3a.4: the N6 sample is 86 discriminating + 3 OVERLAP names at the stated vintage.",
    "world_is": "The rule as written, applied to distinct names at the issuance pull, yields 85 discriminating + 3 OVERLAP. The issuance's N6_SAMPLE.json carries 85 + 3 and a count_note naming this row. The frozen decomposition is not edited.",
    "notes": "OBSERVATION, INERT: the rule binds and it is applied as written; only the derived count moved. No cell's criterion depends on the number 86 -- the checker reads the sample file's own denominator. For 3.0.0_SA_CVO's L8 disposition."
  },
  {
    "id": "LGIC_NAMING-W2-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~2",
    "surfaced_at": "2026-09-14T16:44Z",
    "one_line": "Namer A (LN-e-1): the two briefing files close scope, kind, cadence and system class but leave the FUNCTION / PURPOSE slot an open vocabulary, so 11 of 18 N3 names turn on a token the namer chose from the item's own words with no rule to choose between candidates (publish vs publisher, fetch vs session-fetch, compound vs function+qualifier).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/NAMING_SCHEMA.json@6a5b276f8b :56 resource.function = 'one or more kebab tokens naming what it does; a compound such as silver-chain is ONE function token' -- no closed list; :57 qualifier = 'optional narrowing: a table, a leg, or an environment'; :105 secret.purpose and :107 iam_policy.purpose_slot = function carry no list either. :81 names 'trigger, publisher, scanner' as FUNCTION tokens, the only function tokens either file spells.",
        "infra/logic/05_IDENTITY_SPINE.md@6a5b276f8b holds firms, products, vendors and masters only (sections 2-3); it mints no function token.",
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv (this worker's output, committed with this row): the function / purpose token was chosen from the item text for i01 publisher, i02 session-fetch, i04 api-credentials, i07 gold-read, i09 publish-failure, i10 platform-export, i12 download, i15 gold-build, i16 exporter, i17 pipeline, i18 delivery-status -- 11 of 18 items; the other 7 (i03 ingest, i05, i06, i08 price-refresh, i11 ingest, i13, i14) take the item's own single token or have no function slot."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-1 task order: 'If a name cannot be derived from those two files, the answer for that item is RAISE and a surprise row -- never a guess.'",
    "world_is": "Every closed slot derives from the two files, but the function / purpose slot is free by the schema's own text, so the namer derived it from the item description's verb or noun and chose among several defensible spellings. None was answered RAISE: the schema instructs 'naming what it does', which the item text supplies; the choice between spellings is not ruled by either file.",
    "notes": "OBSERVATION, INERT: form only. Whether the two namers' strings agree on these 11 items is LN-e-3's measurement, not this worker's. Remedy not chosen here."
  },
  {
    "id": "LGIC_NAMING-W2-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~2",
    "surfaced_at": "2026-09-14T16:44Z",
    "one_line": "Namer A (LN-e-1), item i13: the entity partition slot {entity}={id} admits two readings of 'the entity is the advisor keyed advisor_id' -- advisor=A123 (the entity's name) or advisor_id=A123 (its key); neither briefing file says which token fills {entity}. Namer A wrote advisor_id=A123.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/NAMING_SCHEMA.json@6a5b276f8b :41 key.partition third member = '{entity}={id} -- an entity partition; the file is the object under it (doctrine R2)'; :38 names 'the kebab-case and hive forms' as binding NEW served families. Neither line says whether {entity} is the entity's name or its key column.",
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_ITEMS.json@6a5b276f8b item i13: 'the entity is the advisor keyed advisor_id, and the advisor id is A123'.",
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv i13 = mdpf/49financial/platinum/advisor_books/advisor_id=A123 (the hive reading: key column = value)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-1 task order: a name not derivable from NAMING_SCHEMA.json and 05_IDENTITY_SPINE.md is RAISE plus a row, never a guess.",
    "world_is": "i13 derives through every slot except the partition's left-hand token, which reads as advisor (the literal {entity}) or advisor_id (the item's stated key, the hive convention the schema names). Namer A took the hive reading and records the other here; it was not answered RAISE.",
    "notes": "OBSERVATION, INERT: form only. The id value A123 is written verbatim (the schema states no case rule for an id)."
  },
  {
    "id": "LGIC_NAMING-W2-S3",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~2",
    "surfaced_at": "2026-09-14T16:44Z",
    "one_line": "Namer A (LN-e-1), item i14: for a key whose {source} is the product itself (mdpf) and which is shared across all firms, the briefing files do not say whether {scope} is the GLOBAL key (global) or the PRODUCT key (mdpf). Namer A wrote mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/NAMING_SCHEMA.json@6a5b276f8b :33 key.scope_classes = FIRM, PRODUCT, MASTER, GLOBAL; :114 global_scope key 'global'; :32 source = 'a registry VENDOR key or, for derived tiers, a PRODUCT or SYSTEM key'; :40 code = '{source}/{scope}/code/{built_tier}/{file}'. No line maps 'shared across all firms' under a PRODUCT source to one scope class; the resource grammar's 'OMITTED' rule (:54) cannot apply because the key's five segments are ruled (:27).",
        "infra/logic/05_IDENTITY_SPINE.md@6a5b276f8b section 3 PRODUCTS and VENDORS: a PRODUCT key appears as a scope only beneath a vendor source (pathfinder, trueshares -> etfs); no row shows a product as both source and scope.",
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv i14."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-1 task order: a name not derivable from NAMING_SCHEMA.json and 05_IDENTITY_SPINE.md is RAISE plus a row, never a guess.",
    "world_is": "The scope slot for an all-firm key under a product source reads as global (the GLOBAL class, 'shared across all firms') or mdpf (the PRODUCT class). Namer A took global and records the other here; it was not answered RAISE.",
    "notes": "OBSERVATION, INERT: form only. The leaf is included because key.code names the file or bundle as the named leaf in the partition position."
  },
  {
    "id": "LGIC_NAMING-W2-S4",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~2",
    "surfaced_at": "2026-09-14T16:44Z",
    "one_line": "Namer A (LN-e-1), item i15: an instance profile for 'the Orion runner host that builds Inflection's gold data' has no product in the spine, and the schema admits a vendor as {system} 'only when the resource IS the vendor integration' without saying whether a vendor-named runner building a DERIVED tier is. Namer A wrote orion-inf-gold-build-profile.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/NAMING_SCHEMA.json@6a5b276f8b :120-122 system.classes = PRODUCT, PLATFORM_SUBSYSTEM, VENDOR; vendor_as_system_only_when = 'the resource IS the vendor integration'; never_a_system includes 'a firm'. :32 lets a derived-tier KEY take a PRODUCT or SYSTEM source, but no line says which system a derived-tier RESOURCE takes when no product owns it.",
        "infra/logic/05_IDENTITY_SPINE.md@6a5b276f8b section 3: inflection has no product row; orion is a VENDOR with scope inflection. No platform subsystem is listed in either file.",
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv i15."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-1 task order: a name not derivable from NAMING_SCHEMA.json and 05_IDENTITY_SPINE.md is RAISE plus a row, never a guess.",
    "world_is": "orion is the only registry key the item names that can fill {system} (the firm cannot, and no product or platform subsystem is listed), so Namer A took orion, reading the Orion runner as the vendor integration's pipeline. Whether a derived-tier build counts as 'the vendor integration' is not stated; recorded here, not answered RAISE.",
    "notes": "OBSERVATION, INERT: form only. The function token gold-build is the silver-chain pattern (tier + verb as one compound, NAMING_SCHEMA :56) and is covered by row LGIC_NAMING-W2-S1."
  },
  {
    "id": "LGIC_NAMING-W3-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~3",
    "surfaced_at": "2026-09-14T16:45Z",
    "one_line": "N3 item i13 is answered RAISE: NAMING_SCHEMA v1.4 key.partition writes an entity partition as '{entity}={id}' without saying whether {entity} is the entity's name or its key column, and the item states both (the entity 'the advisor', keyed 'advisor_id'), so advisor=A123 and advisor_id=A123 are each a faithful substitution.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SCHEMA: org/standards/NAMING_SCHEMA.json:41 @6a5b276f8b, key.partition: '{entity}={id} -- an entity partition; the file is the object under it (doctrine R2)'. No field names which token fills {entity}; the one worked partition, date=YYYY-MM-DD, is a case where the entity and its key are the same word.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json:38 @6a5b276f8b, key.legacy_served_path: 'the kebab-case and hive forms bind NEW served families only' -- i13 is a NEW served family, so the hive form binds, but the form's left-hand token is still unnamed.",
        "ITEM: org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_ITEMS.json:19 @6a5b276f8b, i13: 'the table is advisor_books, the entity is the advisor keyed advisor_id, and the advisor id is A123'.",
        "SEED: infra/logic/05_IDENTITY_SPINE.md:25-26 @6a5b276f8b spells SmartX's live entity trees by the entity's NAME (account/{uuid}, allocation/{uuid}, model/{uuid}); that leans toward advisor=, but it describes a tree ruled a VIOLATION of R2, not the ruled partition form, so it does not decide the slot."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LGIC_NAMING.TO-LN-e-2 worker face: name every N3 item from NAMING_SCHEMA.json v1.4 and 05_IDENTITY_SPINE.md only; 'If a name cannot be derived from those two files, the answer for that item is RAISE and a surprise row -- never a guess.'",
    "world_is": "For i13 the two files fix every segment except the partition's left-hand token: mdpf/49financial/platinum/advisor_books/{advisor | advisor_id}=A123. Nothing in either file selects between the two, so org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-b.tsv carries 'i13<TAB>RAISE'.",
    "notes": "Form only; the significance is the grade's call. The rest of the i13 key as this worker derives it: source mdpf (a PRODUCT key for a derived tier, NAMING_SCHEMA.json:32), scope 49financial (LONG, :34), tier platinum (served), table advisor_books (snake_case as the item gives it, :37), partition {entity}=A123, leaf book.json excluded as the item says. The schema text's owner is 1.0.0_SA_CTO (ratified_by, NAMING_SCHEMA.json:4). For 3.0.0_SA_CVO at L8."
  },
  {
    "id": "LGIC_NAMING-W3-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~3",
    "surfaced_at": "2026-09-14T16:45Z",
    "one_line": "NAMING_SCHEMA v1.4 closes the kind and cadence slots but not the function/purpose slot ('one or more kebab tokens naming what it does'), so 14 of the 18 N3 names in n3-namer-b.tsv carry a function or purpose token this worker chose by a stated rule rather than looked up; the schema itself lists the noun 'publisher' as a function token beside the verb reading.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SCHEMA: org/standards/NAMING_SCHEMA.json:56 @6a5b276f8b, resource.function: 'one or more kebab tokens naming what it does; a compound such as silver-chain is ONE function token' -- no enumeration.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json:57 @6a5b276f8b, resource.qualifier: 'optional narrowing: a table, a leg, or an environment (dev | prod)' -- no rule for whether it is written when an item names none.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json:81 @6a5b276f8b, kind.closed_at_l4: 'The brief's measured suffixes trigger, publisher, scanner are FUNCTION tokens, not kinds.' -- a noun form admitted as a function token, beside :56's 'naming what it does'.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json:105 and :107 @6a5b276f8b, secret {purpose} and iam_policy purpose_slot 'function' -- the same open slot under two more grammars.",
        "SEED: infra/logic/05_IDENTITY_SPINE.md @6a5b276f8b holds firms, products, vendors and masters only (section 2 table, lines 39-44); it has no function vocabulary."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LGIC_NAMING.TO-LN-e-2: two namers name the same NEW resources without conferring and write the identical string for every one, each deriving names from NAMING_SCHEMA.json v1.4 and 05_IDENTITY_SPINE.md only.",
    "world_is": "Neither file enumerates function or purpose tokens. This worker applied one rule to every item: the process noun the item names (ingest, publish, export, price-refresh, platform-export, delivery-status, pipeline), otherwise the item's main verb in base form (fetch, download, read, build); a tier word the verb acts on is kept (read-gold, build-gold); generic verbs (runs, starts, fires, holds) and generic nouns (figures, files, data, credentials) are dropped; the optional qualifier is omitted. Items so named: i01 i02 i03 i04 i07 i08 i09 i10 i11 i12 i15 i16 i17 i18 (14 of 18; i05 is a bucket, i06 i13 i14 are keys). A namer applying a different rule (publisher for publish, fetch-sessions for fetch, api-credentials for api, a publish- prefix on i07) writes a different string for the same item.",
    "notes": "Form only. i04's purpose is 'api' because the generic-noun half of the rule drops 'credentials', read beside NAMING_SCHEMA.json:81's reason for dropping the secret kind (a suffix that repeats the type). The schema text's owner is 1.0.0_SA_CTO. For 3.0.0_SA_CVO at L8."
  },
  {
    "id": "LGIC_NAMING-W3-S3",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~3",
    "surfaced_at": "2026-09-14T16:45Z",
    "one_line": "Three N3 names turn on a scope or system choice the two briefing files leave open, each resolved by this worker by a stated reading: i14's product-shared code key takes scope mdpf (PRODUCT) not global, because GLOBAL has no rule for when it applies; i11 and i15 take the vendor as system (pathfinder, orion) under 'only when the resource IS the vendor integration'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SCHEMA: org/standards/NAMING_SCHEMA.json:33 and :114 @6a5b276f8b: key.scope_classes ['FIRM', 'PRODUCT', 'MASTER', 'GLOBAL'] and global_scope {key: global}; no field says when a key takes GLOBAL. :54 resource.scope_when_shared 'OMITTED' binds the resource grammar only; the five-segment key grammar (:26-27) has no omission.",
        "SEED: infra/logic/05_IDENTITY_SPINE.md:30 and :50-51 @6a5b276f8b: R2 'a scope is a firm, a product, or a master'; invariant 1 'every {scope} segment in the census resolves to exactly one FIRM, PRODUCT or MASTER key' -- no GLOBAL.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json:121 @6a5b276f8b, system.vendor_as_system_only_when: 'the resource IS the vendor integration'; :120 classes PRODUCT, PLATFORM_SUBSYSTEM, VENDOR.",
        "SEED: infra/logic/05_IDENTITY_SPINE.md:85 and :88 @6a5b276f8b: orion's scope is inflection; pathfinder's scopes resolve to etfs. The seed lists no platform subsystem and no product that owns Inflection's gold."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LGIC_NAMING.TO-LN-e-2: name every N3 item from NAMING_SCHEMA.json v1.4 and 05_IDENTITY_SPINE.md only; the outcome is that two namers write the identical string for every item.",
    "world_is": "(1) i14: this worker wrote mdpf/mdpf/code/gold/mdpf-accrual-bridge.tar.gz (scope = the product, per the seed's R2); a namer reading 'shared across all firms' as GLOBAL writes mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz. (2) i11: the Pathfinder ingest is the vendor integration, so system pathfinder with scope etfs: pathfinder-etfs-ingest-task; the product-as-system reading gives etfs-pathfinder-ingest-task or etfs-ingest-task. (3) i15: the item names the host 'the Orion runner', and orion is the only registry system that resolves for a host building Inflection's gold: orion-inf-build-gold-profile; a reading that denies a gold-building host the vendor slot finds no system in the seed and RAISEs.",
    "notes": "Form only. The schema text's owner is 1.0.0_SA_CTO; the registry rows (which products and subsystems exist) are LGIC_ENFORCE's under ruling (a) (NAMING_SCHEMA.json:18). For 3.0.0_SA_CVO at L8."
  },
  {
    "id": "LGIC_NAMING-W5-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~5",
    "surfaced_at": "2026-09-14T16:53Z",
    "one_line": "LN-l-3's L3-AC1 invocation (check_ln.py l3-correct) prints VERDICT: FAIL-MISREAD, not the expected PASS-ALL-CORRECT: 5 of 6 conforming N5 addresses are labeled as N5_KEY reads them, and the one miss is a3, the v1.3 code-tier specimen, which the reader marked DOES-NOT-FIT where the key reads bucket,source,scope,tier,table,partition.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py l3-correct, 2026-09-14 ~16:5xZ, worktree HEAD 179884e46b -> 'WRONG: a3  labeled=DOES-NOT-FIT  expected=bucket,source,scope,tier,table,partition' / 'CONFORMING ADDRESSES: 6  CORRECT: 5  WRONG: 1' / 'VERDICT: FAIL-MISREAD', rc=0. The sibling criterion L3-AC2 (l3-control) printed 'VERDICT: PASS-CONTROL-FLAGGED', 1 of 1.",
        "ANSWER: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n5-reader.tsv:3 @15c38055ca 'a3<TAB>DOES-NOT-FIT'; the reader's reason, deliverables/0.9.0_WK_LGIC_NAMING~4/cross-bucket-reader.result.md:18 @15c38055ca: '6 segments. After code in the tier slot, the table slot holds a second tier word (gold), and there is no partition'.",
        "KEY: deliverables/2.0.0_SA_COO~G/fixed_inputs/N5_KEY.json:9 @777770e6aa 'a3': 'bucket,source,scope,tier,table,partition'; :4 'a3 is the v1.3 code tier (the table slot carries the built tier and the file is the named leaf in the partition slot, with no object)'.",
        "BRIEFING: deliverables/2.0.0_SA_COO~G/fixed_inputs/N5_ADDRESSES.json:6 @777770e6aa 'the_layout': 's3://opal-data-assets/{source}/{scope}/{tier}/{table}/{partition}/{object}' (seven segments, ending in object); :13 partition 'a date=YYYY-MM-DD, or a named leaf, or an entity=id'. The briefing carries no statement that an address may end at the partition without an object, or that the table slot may carry a tier word.",
        "CHECKER: deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py:411-420 @777770e6aa l3_correct compares each non-DOES-NOT-FIT key entry to the TSV label as an exact string and prints FAIL-MISREAD on any mismatch."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-LN-l-3 L3-AC1: 'every conforming address is labeled as the ruled string reads it', invocation check_ln.py l3-correct, expect 'VERDICT: PASS-ALL-CORRECT'.",
    "world_is": "The invocation prints 'VERDICT: FAIL-MISREAD' with one WRONG line (a3). The cell scores and does not read, so the label cannot be changed inside LN-l-3; the order stays open on L3-AC1 FAIL. The reader's briefing describes only a seven-segment layout ending in an object, and a3 is a six-segment code-tier address with no object.",
    "notes": "Filed by the scoring worker because the named invocation did not produce the named result. No reading, re-labeling or fix was attempted: the answer file belongs to LN-l-2 and is outside this order's paths. For 3.0.0_SA_CVO's L8 disposition."
  },
  {
    "id": "LGIC_NAMING-W6-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~6",
    "surfaced_at": "2026-09-14T17:07Z",
    "one_line": "Blind reader (LN-e-4): the order's premise 'you have never seen this estate' fails before the first tool call -- the worker session loads the workspace CLAUDE.md and the user's auto-memory MEMORY.md, which name cot, bd, inf, 49financial, inflection and cottonwood as firms, so 9 of the reader's 18 marks are tokens its context had already named as firms and 3 more (49f) abbreviate one it named.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G -- as issuer and spawner of LN-e-4: disclose at this round's L8/L9 that the N3 reader was not blind to the firm vocabulary, and for any re-run either seat the reader in a context that does not load CLAUDE.md or the auto-memory, or state that the reader measure cannot be taken inside this fabric",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CONTEXT: CLAUDE.md:329 @64dd54e67f (Rule 13, loaded into this worker's context by the harness before any tool call): 'cot is a separate firm from bd -- never mirror/sync.'",
        "CONTEXT: C:/Users/AndrewBerman/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/MEMORY.md (outside the repo, no commit; loaded at session start 2026-09-14): index line 'Legacy bd/inf/cot buckets are the ACTIVE firm channels until the D14 move to -49financial/-inflection/-cottonwood'.",
        "OUTPUT: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-reader.tsv (committed with this row): 18 marks -- cot 3, inf 3, inflection 1, 49financial 1, cottonwood 1 (9, named as firms verbatim in the context), 49f 3 (an abbreviation of 49financial), etfs 3, mdpf 2, demo 1.",
        "INPUT READ: only column 2 of n3-namer-a.tsv @64dd54e67f (cut -f2), 18 names after the '# base' line; check_ln.py was run, not read, and no other fixed input or exercise file was opened before the marks were written."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-4 task order: 'You have never seen this estate, and you read the names alone.' and 'Read: column 2 of n3-namer-a.tsv, and nothing else.'",
    "world_is": "A worker spawned in this workspace starts with the workspace law file and the user's memory index in context, and both spell out which short and long tokens are firms. The reader read nothing but column 2, but it could not un-know that vocabulary, so its firm marks do not measure what a reader who had never seen the estate would mark.",
    "notes": "OBSERVATION: form only. Whether this moves FWD-2's grade is 3.0.0_SA_CVO's call at L8/L9, not this worker's. The reader's marking rule is stated in deliverables/0.9.0_WK_LGIC_NAMING~6/blind-reader.result.md so the exposure can be read against it."
  },
  {
    "id": "LGIC_NAMING-W6-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~6",
    "surfaced_at": "2026-09-14T17:07Z",
    "one_line": "Blind reader (LN-e-4): the order asks for THE one token that is the firm or the product, but at least 4 of 18 names carry both a recurring product-like prefix (mdpf) and a firm-like token, and the order does not say which to mark; the reader marked the firm token whenever one was present and the product token otherwise.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC: org/missions/D14/LGIC/LGIC_NAMING/task-orders/LGIC_NAMING.TO-LN-e-4.blind-reader.md:22 @64dd54e67f: 'For each name, mark the token that is the firm or the product it belongs to, exactly as it is spelled in the name, or none if no token is.'",
        "INPUT: n3-namer-a.tsv column 2 @64dd54e67f: mdpf-cot-exporter-sg, mdpf-cot-publisher-lambda, mdpf-inf-delivery-status-table and mdpf/49financial/platinum/advisor_books/advisor_id=A123 each carry mdpf and a firm-like token; mdpf-demo-publish-failure-alarm carries 'demo' in the slot where its mdpf siblings carry the firm token.",
        "OUTPUT: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-reader.tsv marks cot, cot, inf, 49financial and demo on those five names, and mdpf only on mdpf-gold-read-policy and mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz, whose second segment is a tier word or 'global'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-4 task order: mark the one token that is the firm or the product each name belongs to.",
    "world_is": "Where a name carries both a product token and a firm token there are two candidate marks, and a one-column output holds only one. The reader had to choose a precedence the order does not state (firm over product), so a comparison against a key that prefers the product would read those names as misses.",
    "notes": "OBSERVATION, INERT: form only. 'demo' is the reader's weakest mark: read as the tenant in the firm slot, not known to be a firm."
  },
  {
    "id": "LGIC_NAMING-W6-S3",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~6",
    "surfaced_at": "2026-09-14T17:07Z",
    "one_line": "Blind reader (LN-e-4): the order says to read column 2 of n3-namer-a.tsv and nothing else, but appending the row its <paths> grants requires reading this channel to mint the next unused id, and the channel quotes N3_ITEMS item text and the namer's per-item choices; the reader fixed every mark before the channel read returned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC: org/missions/D14/LGIC/LGIC_NAMING/task-orders/LGIC_NAMING.TO-LN-e-4.blind-reader.md:20 and :24 @64dd54e67f ('Do NOT open N3_ITEMS.json ... or any other exercise file'; 'Read: column 2 of n3-namer-a.tsv, and nothing else'), and :48, the <paths> line granting this channel.",
        "CHANNEL: org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md @64dd54e67f, row LGIC_NAMING-W2-S2's grounding quotes N3_ITEMS.json item i13 ('the entity is the advisor keyed advisor_id, and the advisor id is A123'), and rows W2-S1..S4 name the namer's choices for i01-i18.",
        "ORDER OF ACTS: n3-reader.tsv was written by a Write call issued in the same batch as the first read of this channel, its content fixed in that call; no later act changed a mark (after the mutant control the restored file was cmp-identical to the written one)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-4 task order: 'Read: column 2 of n3-namer-a.tsv, and nothing else.'",
    "world_is": "The worker definition obliges a channel read before a row can be appended, and this project's channel carries the item descriptions and the namers' reasoning. A blind reader that read the channel before marking would no longer be blind to the items.",
    "notes": "OBSERVATION, INERT for this cell because the marks were fixed first. The same exposure faces any later blind cell granted this channel. Remedy not chosen here."
  },
  {
    "id": "LGIC_NAMING-W5-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~5",
    "surfaced_at": "2026-09-14T17:11Z",
    "one_line": "LN-e-3's E3-AC1 invocation (check_ln.py e3-identical) prints VERDICT: FAIL-DIFFERENT, not the expected PASS-IDENTICAL: the two blind namers wrote the identical string for 9 of 18 N3 items; of the 9 that differ, 7 part at the function or purpose slot, 1 (i14) at the scope slot, and 1 (i13) is namer B's RAISE against namer A's string.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e3-identical, 2026-09-14 ~17:0xZ, worktree HEAD 33131baf6f -> 9 DIFFERS lines (i01 i02 i04 i07 i09 i13 i14 i15 i16) / 'ITEMS: 18  IDENTICAL: 9  DIFFERENT: 9' / 'VERDICT: FAIL-DIFFERENT', rc=0. The sibling criterion E3-AC2 (e3-blind) printed 'VERDICT: PASS-BLIND': both recorded bases are 6a5b276f8b and neither holds the other namer's file.",
        "ANSWERS: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv @254a310135 and n3-namer-b.tsv @beaefc6cf5. The slot for each differing item, found by the first differing token under org/standards/NAMING_SCHEMA.json @33131baf6f :51 (resource), :105 (secret), :107 (iam_policy) and :26 (key): function for i01 publisher/publish, i02 session-fetch/fetch, i15 gold-build/build-gold and i16 exporter/export; purpose for i04 api-credentials/api and i07 gold-read/read-gold; function or qualifier for i09 (A adds 'failure'); scope for i14 global/mdpf; the whole recorded string for i13 (B wrote RAISE).",
        "PRIOR ROWS: the namers' own rows LGIC_NAMING-W2-S1 and W3-S2 (open function slot), W2-S2 and W3-S1 (i13 partition token) and W2-S3 and W3-S3 (i14 scope) each name the reading that produced these differences.",
        "CHECKER: deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py:252-264 @777770e6aa e3_identical compares the two TSV strings per N3 item as exact strings and prints FAIL-DIFFERENT on any mismatch."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-LN-e-3 E3-AC1: 'the two namers wrote the identical string for every item', invocation check_ln.py e3-identical, expect 'VERDICT: PASS-IDENTICAL'.",
    "world_is": "The invocation prints 'VERDICT: FAIL-DIFFERENT' on 9 of 18 items identical. The cell compares and does not name, so neither string can be changed inside LN-e-3; the order stays open on E3-AC1 FAIL. n3-compare.md records both strings and the slot where they part for each of the 9.",
    "notes": "Filed by the comparing worker because the named invocation did not produce the named result. No winner is chosen and no answer is edited: both answer files belong to LN-e-1 and LN-e-2 and are outside this order's paths. For 3.0.0_SA_CVO's L8 disposition."
  },
  {
    "id": "LGIC_NAMING-W1-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~1",
    "surfaced_at": "2026-09-14T17:01Z",
    "one_line": "The portal census TO-LN-g-1 names, git grep -n platinum <sha> -- src (case-sensitive), prints 122 lines but shows a request line for only 7 of the 39 served platinum paths the frozen portal requests: the rest are built on PLATINUM_BASE, advisorBase, clientBase or perfrpLeafBase, or reach platinum/ through a router rewrite of /api/general/mdpf|etfs or /api/scoped/satellites, and none of those lines spells lowercase 'platinum'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "NAMED INSTRUMENT, portal @e85f6eb84f (git ls-tree HEAD portal at workspace 6a5b276f8b): git -C <workspace>/portal grep -n platinum e85f6eb84f -- src -> 122 lines; its request lines are advisor-intelligence.ts:302, :380, :397, :419, :456, :1366 and the platinum-summary route :957 -- 7 templates.",
        "WIDENED: git grep -n -i platinum e85f6eb84f -- src -> 401 lines across 33 files; git grep -n -E 'api/general/mdpf|PLATINUM_BASE|platinum-summary|/api/scoped/[a-z-]+/platinum' -> 47 lines; a third census for request builders without the token (advisors/${, clients/${, accounts/${, mix.json, /api/scoped/satellites, /api/general/(mdpf|etfs)) -> 30 lines.",
        "EXAMPLES the named census cannot print: advisor-intelligence.ts:725 const advisorBase = `${PLATINUM_BASE}/advisors/${advisorId}` and :736 `${advisorBase}/book.json`; aum.ts:614 `/api/general/mdpf/${firmId}/aum-metrics.json` (rewritten to platinum/mdpf/* per aum.ts:509); satelliteRegistry.ts:86 '/api/scoped/satellites/registry.json' (resolved to platinum/satellites/registry.json per :74-76).",
        "RESULT: org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json lists 39 templates, each with its request site, and 8 exclusions with reasons, from the widened census."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-LN-g-1, Deliverable 2: 'src/api/endpoints/adviKeyRepoint.ts is the known request site ...; census the rest with git -C .../portal grep -n platinum <sha> -- src and print the denominator.'",
    "world_is": "The named census finds only request lines that spell the token. In the frozen portal most platinum requests are assembled from a constant (PLATINUM_BASE = '/api/scoped/advisor-intelligence/platinum', advisor-intelligence.ts:489) or from a route the CDN router rewrites to platinum/, so a list built from that census alone would hold 7 of 39 entries and wrongly grade 32 legacy served paths OUT-OF-PATTERN. The list was built from the widened census; both denominators are printed in its census field.",
    "notes": "OBSERVATION, INERT: the list landed from the wider read. Recorded so the list's completeness can be judged against both instruments, and so a later re-read of the portal does not repeat the narrower one. Not measured: the router source (shared-advisor-router, public-data-router) that performs the rewrites; the mappings are the portal's own comments."
  },
  {
    "id": "LGIC_NAMING-W1-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~1",
    "surfaced_at": "2026-09-14T17:01Z",
    "one_line": "The system slot has no registry to resolve against: the seed 05_IDENTITY_SPINE.md holds 2 products and 8 vendors, no PLATFORM_SUBSYSTEM row, and marks find/harvest/imo UNRESOLVED, while the census's first-token table lumps platform subsystems with project codes; GRADING_RULE.md therefore grades against an INTERIM system table (seed + census s.3's products-and-feeds row) and RAISEs 14 tokens.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SEED: infra/logic/05_IDENTITY_SPINE.md s.3 @6a5b276f8b: PRODUCTS mdpf, etfs, and harvest/find 'UNRESOLVED: tick-list row 18' (imo with them); VENDORS schwab, blackdiamond, orion, eclipse, smartx, pathfinder, trueshares, ycharts; s.2 names four entity types (FIRM, PRODUCT, VENDOR, MASTER) and no PLATFORM_SUBSYSTEM.",
        "DATA: org/standards/NAMING_SCHEMA.json v1.4 system.classes = [PRODUCT, PLATFORM_SUBSYSTEM, VENDOR]; rows_owner: 'Seed until that registry exists: infra/logic/05_IDENTITY_SPINE.md'.",
        "CENSUS: infra/logic/09_NAMING_CENSUS.md s.3 row 3 calls irpt, mdpf, etfs, advi, smartx, yang, news, find, astn, amgt, trade, seeking, fred, ycharts 'the real {system} values'; row 4 lists estate, globgrph, semantic, agentbus, cmtque, opsec, firmsep, consolidation, canonical, gldinc, quartz as 'PLATFORM subsystems and PROJECT CODES used as systems' without saying which is which.",
        "EFFECT in the worked cases: globgrph-serving (ECS_TASK_DEFINITION) and opal-globgrph (ECS_CLUSTER) RAISE; every eligible live ECS_TASK_DEFINITION name begins globgrph."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD S6: 'Which systems exist is the registry's rows, not this document'; S11: 'a token no registry row resolves, RAISES as a defect in the rule or the registry'; the data file's rows_owner names the seed as the registry until it exists.",
    "world_is": "Read strictly against the seed, the rule would RAISE on most live names, because irpt, advi, yang, news, astn, amgt, trade, fred and seeking-alpha -- the census's own 'real {system} values' -- have no seed row. The rule admits them as INTERIM systems (V1 of GRADING_RULE.md, provenance stated, and its product-or-feed split is this worker's reading), and RAISEs the census's unsplit subsystem-or-project-code tokens and the seed's UNRESOLVED products (V2). LN-h-1 and LN-h-2 grade with the same table, so they can agree, but the table is not the registry.",
    "notes": "OBSERVATION, INERT for this round. The registry rows are LGIC_ENFORCE's (PRD CONTRACTS row 3, ruling (a)); a platform-subsystem row for each V2 token, or a word that a token is a project code, turns that token's RAISE into a verdict without changing the rule's text."
  },
  {
    "id": "LGIC_NAMING-W1-S3",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~1",
    "surfaced_at": "2026-09-14T17:01Z",
    "one_line": "grade.OUT-OF-PATTERN prints a canonical form, but three live name classes do not carry a slot that form needs -- a firm or other non-system first token with no system token anywhere in the name, an S3Key node name that carries no bucket (so no source or scope), and an event rule or schedule with no cadence token -- so GRADING_RULE.md prints those canonical forms with a {system}, {source}, {scope} or {cadence} placeholder.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA: org/standards/NAMING_SCHEMA.json v1.4 grade.OUT-OF-PATTERN: 'the grammar fails (order, separator, case, a missing or unknown kind, a firm in the system slot); canonical_form is printed'.",
        "CENSUS: infra/logic/09_NAMING_CENSUS.md s.1 item 3(c): a firm token at position 0 'as if the firm were the system' in Lambda 47, role 55, rule 45, log 57 names; header: 'the live graph's 382 S3Key nodes are name-grain served-graph nodes without bucket ARNs'.",
        "LIVE_NAMES.json (vintage 2026-09-14 12:13:53 UTC): LAMBDA inf-silver-chain (no token is a system), S3Key platinum/firm/header_metrics.json (no bucket; the bucket decides scope, SEED s.3), EVENT_RULE bd-49f-session-complete (no cadence token).",
        "WORKED CASES in GRADING_RULE.md @ this commit: {system}-inf-silver-chain-lambda, advi/{scope}/platinum/firm/header_metrics.json, blackdiamond-49f-session-complete-{cadence}, {source}/{scope}/code/gold/*."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NAMING_SCHEMA grade.OUT-OF-PATTERN: 'canonical_form is printed'; PRD FWD-5 ACCEPT: 'including the correct name for each one that breaks the pattern'.",
    "world_is": "From (name, type) alone, the canonical form of these names cannot be completed. The missing slot lives in the registry (which system a firm pipeline belongs to), in the bucket that holds the key, or in the rule's schedule expression or event pattern, and none of those is an input to grade(). A placeholder canonical form is deterministic, so two hand graders agree on it (G6 V-2 makes it OUT-OF-PATTERN), but it is not the full correct name FWD-5 asks for.",
    "notes": "OBSERVATION, INERT: nothing breaks and the verdict is decided. The open question, not chosen here, is the contract's (1.0.0_SA_CTO's, the author of CONTRACTS row 2): whether a placeholder canonical form satisfies FWD-5, or grade() needs more than (name, type) -- the bucket for a key, the registry's system for a principal -- as v1.4 did for legacy membership by making it data."
  },
  {
    "id": "LGIC_NAMING-W1-S4",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~1",
    "surfaced_at": "2026-09-14T17:01Z",
    "one_line": "Names AWS fixes sit inside three graded types with no exclusion in NAMING_SCHEMA.json -- the VPC default security group 'default' (1 of 26 SECURITY_GROUP), 9 of 417 IAM_POLICY names beginning AWS or Amazon, and 4 of 264 LOG_GROUP names (aws-waf-logs-*, RDSOSMetrics, /aws/ecs/containerinsights/*) -- so GRADING_RULE.md RAISEs them by name shape, and cannot see an AWS-managed policy without the prefix (ReadOnlyAccess is live).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA: org/standards/NAMING_SCHEMA.json v1.4 types_not_graded_by_kind and not_covered exclude AWS-issued identifiers by TYPE only (KMS_KEY, CLOUDFRONT_DISTRIBUTION, SERVICE_PRINCIPAL, VPC_ENDPOINT); SECURITY_GROUP and IAM_POLICY are kind.by_type keys, and LOG_GROUP is graded as derived.",
        "LIVE_NAMES.json (vintage 2026-09-14 12:13:53 UTC), counted by python over by_type: SECURITY_GROUP 'default' 1 of 26; IAM_POLICY AWSDataLifecycleManagerServiceRole, AWSLambdaBasicExecutionRole, AWSLambdaVPCAccessExecutionRole, AmazonDynamoDBFullAccess, AmazonEC2ContainerRegistryFullAccess, AmazonECSTaskExecutionRolePolicy, AmazonRDSEnhancedMonitoringRole, AmazonS3ReadOnlyAccess, AmazonSSMManagedInstanceCore = 9 of 417; LOG_GROUP /aws/ecs/containerinsights/opal-globgrph/performance, RDSOSMetrics, aws-waf-logs-opal-cloudfront, aws-waf-logs-opal-gateway = 4 of 264; ReadOnlyAccess present in IAM_POLICY with no prefix.",
        "CENSUS: infra/logic/09_NAMING_CENSUS.md s.2 lists 'the two default SGs' in the residue, and PRD N2's fixture requires the 'default security groups' residue class graded.",
        "N6 SAMPLE: fixed_inputs/N6_SAMPLE.json carries IAM_POLICY AWSDataLifecycleManagerServiceRole and LOG_GROUP aws-waf-logs-opal-gateway among the 85 discriminating names, so LN-h-1 and LN-h-2 meet this class."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NAMING_SCHEMA grade.unplaceable: 'A name the tokeniser cannot place ... is a defect in the tokeniser, this file or the registry and is fixed there'; types_not_graded_by_kind excludes AWS-issued identifiers type by type.",
    "world_is": "These names are fixed by AWS (a VPC's default group cannot be renamed; AWS-managed policy names and service-mandated log-group names are AWS's), so no canonical form can be minted for them, yet their types are graded. The rule RAISEs them (G2) as a data-file defect. The name is its only evidence: an AWS-managed policy without the AWS/Amazon prefix, such as ReadOnlyAccess, cannot be told from a camel-case customer policy and is graded OUT-OF-PATTERN.",
    "notes": "OBSERVATION, INERT. Remedy options, not chosen here, the data file's author's (1.0.0_SA_CTO): exclude AWS-owned names within graded types by an enumerated rule in NAMING_SCHEMA.json (an AWS-managed ARN prefix, the default group, the service-mandated log-group forms), or accept the RAISE as their standing output."
  },
  {
    "id": "LGIC_NAMING-S12",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T17:26Z",
    "one_line": "Issuer's disarm of LGIC_NAMING-W6-S1, widened to the dependency the blind cells share: every worker in this round starts with the workspace CLAUDE.md and the user's auto-memory MEMORY.md already in context, so all six cells that carry a blindness requirement run on one un-blinded context. The leak is MEASURED on LN-e-4 only; on the other five it is NOT-EVALUATED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_NAMING-W6-S1@31edd82e0b (OBSERVATION, ARMED, disarm_owner 2.0.0_SA_COO~G): the measured leak on LN-e-4 -- 9 of the reader's 18 marks are tokens the preloaded context names as firms verbatim, and 3 more (49f) abbreviate one.",
        "MECHANISM, observed at this seat: when a Bash call of the COO session entered .worktrees/wk-lgic-naming-1-4 (~16:4xZ), the harness injected that worktree's CLAUDE.md into the session context. A worktree carries the tracked CLAUDE.md, so a worker spawned in one loads it; .claude/agents/worker.md@31edd82e0b has no field that suppresses it.",
        "CONTENT: CLAUDE.md@31edd82e0b names the firm tokens (Rule 13, 'cot is a separate firm from bd -- never mirror/sync'; the cross-firm hard stop) and discusses bucket and key layout; the memory index names 'Legacy bd/inf/cot buckets ... -49financial/-inflection/-cottonwood'.",
        "POPULATION, by subtraction over org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md@62b5c0819f section 5: 14 cells, minus 4 authoring cells with no blindness requirement (LN-g-1, LN-f-1, LN-l-1, LN-t-1), minus 4 mechanical scorers (LN-e-3, LN-e-5, LN-l-3, LN-h-3) = 6 blindness-bearing cells: LN-e-1, LN-e-2, LN-e-4, LN-l-2, LN-h-1, LN-h-2.",
        "DISCRIMINATOR on what is and is not broken: E3-AC2 printed PASS-BLIND @a39139aa81 (neither namer's base carries the other's answer file), so MUTUAL blindness between paired workers holds; blindness to the ESTATE'S VOCABULARY is what the preloaded context breaks."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_NAMING decomposition v3 section 5: 'a cold start is a fresh context. The constraint binds on context, never on the slot number'; the LN-e-4 face: 'You have never seen this estate, and you read the names alone.'",
    "world_is": "A fresh subagent context is not an empty one. Every worker loads the workspace law file and the memory index before its first tool call, so a requirement that a worker not know the estate's vocabulary cannot be met by spawn timing or by instruction inside this fabric.",
    "notes": "DISARM of W6-S1, done per that row's own disarm clause: (1) DISCLOSED here, on the L8 compile's input, so 3.0.0_SA_CVO grades FWD-1, FWD-2, FWD-4 and FWD-5 at L9 with it in view -- no blind cell's PASS is REALIZED evidence of an unaided reader or namer while this stands; (2) the re-run remedy (seat readers and graders in a context that loads neither file, or state that the measure cannot be taken inside this fabric) is the round-N analysis's, carried to 1.0.0_SA_CTO in this round's drain-end read. The spec is frozen, so LN-h-1 and LN-h-2 run as cut, under this disclosure. W6-S3's second exposure (the channel a blind cell must read to mint a row) reaches LN-h-1 and LN-h-2 as well, once LN-g-1's rows are merged. INERT because the harm W6-S1 names -- an undisclosed non-blind measurement graded as REALIZED -- now has its disclosure on the grader's input."
  },
  {
    "id": "LGIC_NAMING-W5-S3",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~5",
    "surfaced_at": "2026-09-14T17:25Z",
    "one_line": "LN-e-5's E5-AC1 invocation (check_ln.py e5-correct) prints VERDICT: FAIL-MISREAD, not the expected PASS-ALL-CORRECT: the blind reader marked the key's token on 14 of 18 N3 names; the 4 misses are all shared rows -- i07, i08 and i17 are 'none' in the key and the reader marked the product token (mdpf, etfs, etfs), and i14 is 'global' in the key and the reader marked mdpf.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e5-correct, 2026-09-14 ~17:2xZ, worktree HEAD 23beb7751c -> 'WRONG: i07  name=mdpf-gold-read-policy  marked=mdpf  expected=none' / 'WRONG: i08  name=etfs-price-refresh-dlq  marked=etfs  expected=none' / 'WRONG: i14  name=mdpf/global/code/gold/mdpf-accrual-bridge.tar.gz  marked=mdpf  expected=global' / 'WRONG: i17  name=etfs-pipeline-alerts  marked=etfs  expected=none' / 'ITEMS: 18  CORRECT: 14  WRONG: 4' / 'VERDICT: FAIL-MISREAD', rc=0.",
        "INPUTS: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/n3-namer-a.tsv @254a310135, n3-reader.tsv @3c2910ac09, and deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_KEY.json @777770e6aa, whose key_rule (:4) gives 'global' for the shared product scope of a key and 'none' for a shared resource that carries no scope (S5).",
        "READER'S RULE: row LGIC_NAMING-W6-S2 states the reader 'marked the firm token whenever one was present and the product token otherwise'; none of i07, i08, i14 or i17 carries a firm token.",
        "CHECKER: deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py:287-302 @777770e6aa e5_correct compares the reader's mark on each namer-A name with the key's token as exact strings and prints FAIL-MISREAD on any mismatch."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-LN-e-5 E5-AC1: 'the reader marked the expected firm or product token on every name', invocation check_ln.py e5-correct, expect 'VERDICT: PASS-ALL-CORRECT'.",
    "world_is": "The invocation prints 'VERDICT: FAIL-MISREAD' on 14 of 18 correct. The cell scores and does not read or name, so no mark can be changed inside LN-e-5; the order stays open on E5-AC1 FAIL. n3-reader-score.md records every WRONG line with the name, the mark and the expected token.",
    "notes": "Filed by the scoring worker because the named invocation did not produce the named result. The task order calls a wrong mark 'the outcome's evidence, not a defect to fix'; nothing is edited. For 3.0.0_SA_CVO's L8 disposition."
  },
  {
    "id": "LGIC_NAMING-W5-S4",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~5",
    "surfaced_at": "2026-09-14T17:25Z",
    "one_line": "LN-e-5's E5-AC2 invocation (check_ln.py e5-consistent) prints VERDICT: FAIL-TWO-REFERENTS, not the expected PASS-CONSISTENT: 5 of 18 names carry a token the reader marked elsewhere, all five the token mdpf (marked on i07 and i14, read as the product prefix on i01, i09, i13, i16, i18); read, not run, the key's own marks would also print 2 clashes (token etfs on i08 and i17), so E5-AC1 and E5-AC2 cannot both pass on this key.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: cd .worktrees/wk-lgic-naming-1-5 && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py e5-consistent, 2026-09-14 ~17:2xZ, worktree HEAD 23beb7751c -> 'NAMES: 18  TOKENS MARKED AS A FIRM OR PRODUCT: 9  A MARKED TOKEN READ OTHERWISE ELSEWHERE: 5' with the five pairs (mdpf-cot-exporter-sg, mdpf-cot-publisher-lambda, mdpf-demo-publish-failure-alarm, mdpf-inf-delivery-status-table, mdpf/49financial/platinum/advisor_books/advisor_id=A123), each token 'mdpf' / 'VERDICT: FAIL-TWO-REFERENTS', rc=0. The list is capped at clash[:5] (check_ln.py:317) and the count is 5, so none is hidden.",
        "CHECKER: deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py:305-317 @777770e6aa e5_consistent collects every mark other than 'none', splits each name on [-/=.], and records a clash wherever a marked token is a token of a name whose own mark differs.",
        "READ, NOT RUN: deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_KEY.json:8 @777770e6aa has 'etfs' for i11 and 'none' for i08 and i17; the namer-A names for i08 (etfs-price-refresh-dlq) and i17 (etfs-pipeline-alerts), n3-namer-a.tsv:9 and :18 @254a310135, both carry the token etfs. Under check_ln.py:308-314 a reader marking exactly the key's 18 tokens therefore records 2 clashes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-LN-e-5 E5-AC2: 'no token the reader marked as a firm or product is read otherwise in another name', invocation check_ln.py e5-consistent, expect 'VERDICT: PASS-CONSISTENT'.",
    "world_is": "The invocation prints 'VERDICT: FAIL-TWO-REFERENTS' with 5 clashes. And a reader who met E5-AC1 exactly would still fail E5-AC2 on 2 names, because the key marks a product token on one name and 'none' on two names that carry it. The order stays open on E5-AC2 FAIL.",
    "notes": "Filed by the scoring worker because the named invocation did not produce the named result. The joint-satisfiability observation is read from the key, the names and the checker source, not measured by a run; whether it is its own finding is 3.0.0_SA_CVO's call at L8, not this worker's. Nothing is edited."
  },
  {
    "id": "LGIC_NAMING-S13",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T17:39Z",
    "one_line": "Issuer's MEASUREMENT of W5-S4: LN-e-5's two criteria cannot both pass as cut. A reader whose every mark equals N3_KEY.json passes E5-AC1 by construction and still FAILS E5-AC2 with 2 clashes (etfs-price-refresh-dlq and etfs-pipeline-alerts, both keyed none, while i11 is keyed etfs). So E5-AC2's FAIL on the live reader is not evidence against that reader alone.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INSTRUMENT: the e5_consistent loop of org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_ln.py:305-317@1a06d8ce3f, executed by the issuer over a key-perfect reader -- namer A's 18 names from deliverables/exercises/n3-namer-a.tsv@1a06d8ce3f, each marked with its N3_KEY.json value. Output: 'KEY-PERFECT READER: rows=18 marked_tokens=9 clashes=2', verdict FAIL-TWO-REFERENTS.",
        "THE CLASHES: name=etfs-price-refresh-dlq token=etfs mark=none; name=etfs-pipeline-alerts token=etfs mark=none. N3_KEY.json@777770e6aa keys i11 (ECS_TASK_DEFINITION, the Pathfinder ingest FOR the ETF product) as etfs, and i08 and i17 (resources SHARED by every firm whose system is the ETF product) as none.",
        "ROW: LGIC_NAMING-W5-S4 (surfaced by 0.9.0_WK_LGIC_NAMING~5, BLOCKING INERT) stated this from reading the files and said it had not run it; this row is the run, by a different instrument (the checker's own loop over a constructed key-perfect input, not a reading).",
        "LIVE RESULT, for contrast: the reader's E5-AC2 printed FAIL-TWO-REFERENTS with 5 clashes, all on token mdpf (W5-S4); its E5-AC1 printed FAIL-MISREAD 14 of 18 (W5-S3). The mdpf clashes are the reader's; the 2 etfs clashes above would occur for ANY reader that matches the key."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LN-e-5 task order (issued by 2.0.0_SA_COO~G at L6 @777770e6aa): E5-AC1 'the reader marked the expected firm or product token on every name' AND E5-AC2 'no token the reader marked as a firm or product is read otherwise in another name', both as mechanical criteria the same order can pass.",
    "world_is": "The key itself reads the token etfs two ways: as the scope of a product-scoped resource (i11) and as the SYSTEM of two shared resources that carry no scope (i08, i17). E5-AC2's check treats any second reading of a marked token as a clash, so the criteria are jointly unsatisfiable on this key.",
    "notes": "TWO READINGS, NOT ADJUDICATED HERE: (a) an ISSUER DEFECT in the cut -- E5-AC2's grammar should exempt a product token in the system slot, or the key should mark i08/i17 differently; or (b) a genuine FWD-2 finding about the schema -- when a product key can sit in both the system slot and the scope slot, a reader cannot tell the owning firm or product from the name alone. Which one is the round-N analysis's (1.0.0_SA_CTO), carried in this round's drain-end read. The spec is frozen: LN-e-5 stays OPEN as cut and is not re-scored mid-round. Consequence for L9: 3.0.0_SA_CVO should not grade E5-AC2's FAIL as the reader's failure alone."
  },
  {
    "id": "LGIC_NAMING-W1-S5",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~1",
    "surfaced_at": "2026-09-14T17:44Z",
    "one_line": "LN-f-1's output shape has two dispositions for a firm-token role, attributed (with a canonical form) or excluded (as no firm's principal); wp5-49f-feeder-scheduler-role fits neither -- its 49f token names 49 Financial, and GRADING_RULE R1.f RAISEs it (wp5 is in no vocabulary), so it has no canonical form. It is filed under excluded with a reason saying exactly that.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE_NAMES.json (vintage 2026-09-14 12:13:53 UTC), counted by python over by_type.IAM_ROLE: 240 roles, 69 carry a firm alias token split on - and _; graded by GRADING_RULE.md R1-R6: 68 to a canonical form, 1 RAISE (wp5-49f-feeder-scheduler-role).",
        "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@3d671ff59c R1.f 'Any other t1 is in no vocabulary. RAISE'; V3 lists the workstream codes wsb and wsd only; V1 and V2 do not carry wp5.",
        "ORDER: org/missions/D14/LGIC/LGIC_NAMING/task-orders/LGIC_NAMING.TO-LN-f-1.firm-patterns.md@3d671ff59c:24-29 -- attributed entries carry 'canonical: its canonical form by the rule'; excluded entries carry 'reason: why it is no firm's principal'; no third list.",
        "CHECKER: fixed_inputs/check_ln.py@3d671ff59c f1_covered counts a population name as covered only when it is attributed or excluded with a non-empty reason, so a separate RAISE list would read as uncovered."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LN-f-1: 'Grade each by GRADING_RULE.md to its canonical form and its firm ... A role that is no firm's principal goes to excluded, with its reason.'",
    "world_is": "One of the 69 grades RAISE, not a canonical form: wp5-49f-feeder-scheduler-role. Its firm is legible (49f) but the rule cannot place its system slot, so it can be neither attributed with a canonical form nor honestly called no firm's principal.",
    "notes": "OBSERVATION, INERT: the patterns and the other 68 attributions do not depend on it, and its live name already matches *-49f-*-role. Remedy options, not chosen here: (a) the rule's owner adds wp5 to V3 as a workstream code (S6 never a system), which gives {system}-49f-wp5-feeder-scheduler-role, caught by *-49f-*-role; or (b) the order shape gains a RAISE disposition beside attributed and excluded."
  },
  {
    "id": "LGIC_NAMING-W5-S5",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~5",
    "surfaced_at": "2026-09-14T17:58Z",
    "one_line": "LN-h-3 has to trace each RAISE to the rule line it exposes, but neither N6 answer file records which step raised. The fourth field is empty on all 18 RAISE rows of n6-grader-a.tsv and n6-grader-b.tsv, and the files have no step column. Grader B named the step for each RAISE in its result file, and grader A did not. So n6-compare.md takes its step column from grader B's result file, which is not on the order's read list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md:26-27 @51b0952d71 -- 'RAISE -- the name cannot be placed. This is a defect in this rule, the data file or the registry, and the output names the step that raised (DATA.grade.unplaceable).'",
        "ANSWER FILES: deliverables/exercises/n6-grader-a.tsv @388b07f486 and n6-grader-b.tsv @40f445d92c are byte-identical (cmp rc=0, sha256 41c3de9d62f9c371b810dfaead0dd6bf4053f50b13e45588842d8e865ffde945). Each row is type, name, verdict, canonical_form. All 18 RAISE rows (17 discriminating and 1 overlap, ECS_CLUSTER opal-globgrph) have an empty canonical_form field, and no row names a step.",
        "GRADER B: deliverables/0.9.0_WK_LGIC_NAMING~8/grader-b.result.md:25-35 @c17d7d09c9 has a table headed 'The step that raised each RAISE (18)': R1.c 7, R2 1, L3 -> R1.c/R2 2, R1.f 4, G2.2 1, G2.3 1, K1 2.",
        "GRADER A: deliverables/0.9.0_WK_LGIC_NAMING~7/grader-a.result.md @c17d7d09c9 gives the RAISE count (18) in its tally table and names no raising step.",
        "ORDER: task-orders/LGIC_NAMING.TO-LN-h-3.grading-agreement.md:22 @c17d7d09c9 lists 'Read: n6-grader-a.tsv, n6-grader-b.tsv, GRADING_RULE.md, N6_SAMPLE.json' and asks for 'a table of every disagreement and every RAISE with the line of GRADING_RULE.md it exposes'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "GRADING_RULE.md:26-27 @51b0952d71: a RAISE output 'names the step that raised'.",
    "world_is": "The N6 answer-file format has no field for the raising step, and both graders' TSV rows carry only the verdict RAISE. One grader recorded the steps in prose outside the answer file, and the other recorded none. The rule-line column of n6-compare.md section 4 therefore uses grader B's recorded steps, located in the rule text by this worker. For grader A, the same step is inferred from its identical verdict, not read from A's output.",
    "notes": "Filed by the comparing worker because the order's table needed a fact that the named inputs do not carry. The two graders agree on every verdict, so no disagreement depends on this. Nothing is edited. Whether the answer format or the rule's clause should change is not this worker's call. For 3.0.0_SA_CVO at L8, and for the rule's author."
  },
  {
    "id": "LGIC_NAMING-S14",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "4.0.0_SA_CRO",
    "surfaced_at": "2026-09-14T19:28Z",
    "one_line": "prd-signoff.py refuse exited rc=1 when a foreign commit landed on the shared index 16 s after the review commit. It left the new signoff JSON written to the worktree but uncommitted, and prd-signoff.py status then read that uncommitted file and reported the brief half REFUSED while HEAD still held the v1.4 SIGNED record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: python .tools/prd-signoff.py refuse LGIC_NAMING --half brief --review docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_5_20260914.md@f6172f7dfa at ~19:27Z returned rc=1. git log -1 then read 928a3df671 (1.0.0_SA_CTO, 15:27:17-04:00), 16 s after f6172f7dfa (15:27:01-04:00). The stamp's failure text was not captured; the output was truncated by tail.",
        "STATE: git status --short read ' M org/missions/D14/LGIC/LGIC_NAMING/prd/signoff/4.0.0_SA_CRO.json'. The worktree JSON read verdict REFUSED, prd_version v1.5, half_hash be7cb62c... git show HEAD: of the same path read verdict SIGNED, prd_version v1.4, half_hash 3cf0e30a... The staged set was empty and there was no MERGE_HEAD.",
        "READ: python .tools/prd-signoff.py status LGIC_NAMING, in the same call, printed 'brief REFUSED 4.0.0_SA_CRO review: ...@f6172f7dfa' while the refusal was uncommitted.",
        "RECOVERY: the identical command re-run at ~19:29Z returned rc=0 and committed 3a9a0c2f91; the file then read clean."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 27 L4-R: 'status <CODE> is the one read of what is owed', and the stamp 'writes prd/signoff/<your serial>.json bound to this half's bytes and commits it'.",
    "world_is": "The stamp can write the signoff file and then fail its commit. Because status reads the worktree file, not HEAD, it reports a stamp as landed when nothing was committed. A seat that trusts status over the stamp's rc believes its signature landed, and a later seat's commit or a checkout can carry or drop the uncommitted file. INERT: recovered the same turn by re-running the stamp, and the committed record now matches.",
    "notes": "Filed by 4.0.0_SA_CRO during the LGIC_NAMING v1.5 L4-R. The failure's own error text was not captured, so the mechanism of the rc=1 is UNKNOWN; the concurrent foreign commit is a timing correlation, not a proven cause. Whether LIMB 6 and the L4 notifier read the worktree or HEAD was not measured. For the owner of .tools/prd-signoff.py."
  },
  {
    "id": "LGIC_NAMING-S15",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T20:23Z",
    "one_line": "The namers' briefing for the round-2 re-run carries 2 of the 18 ruled names verbatim: i05's bucket in the registry seed, and i15's ruled name as SY1's worked example in NAMING_SCHEMA.json v1.6. An identical answer on those two items can come from copying the briefing, so it is not independent evidence that two people derive the same name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CENSUS: each of the 18 ruled names in the round-1 analysis's s.2 table (org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md@de52d3db04) searched verbatim in the namers' two briefing files at HEAD 8f4106a7f2: 2 of 18 found.",
        "i05 opal-data-cottonwood at infra/logic/05_IDENTITY_SPINE.md:68: the registry seed names the firm's bucket, which is what a registry is for.",
        "i15 orion-inf-build-gold-profile at org/standards/NAMING_SCHEMA.json:125 (v1.6, @2706014705): SY1's example, written from the round-1 dry-run, is item i15's ruled name.",
        "The other 16 ruled names appear in neither file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD FWD-1 ACCEPT: two people each write 'the identical name' from the schema. Decomposition v3 s.3a.1: the items are 'described in plain words that never spell a schema token'.",
    "world_is": "The schema, which is the namers' ratified briefing, now spells one item's full answer as a worked example, and the registry seed spells another's. The items themselves still spell no token; the briefing does.",
    "notes": "Filed by the issuer at the round-2 cut, for 3.0.0_SA_CVO at L9 (FWD-1) and for the schema's author, 1.0.0_SA_CTO. The cut does not edit the schema: it is ratified data and the namers' whole briefing. The round-2 namers run on it as it stands, and FWD-1's agreement is read as 16 items plus these two under this disclosure. INERT: nothing breaks, and the grader has the disclosure on its input."
  },
  {
    "id": "LGIC_NAMING-W1-S6",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~1",
    "surfaced_at": "2026-09-14T22:04:44Z",
    "one_line": "The e1 seat files are committed LF under core.autocrlf=true with no eol attribute, and check_ln_r2.py hashes e1.prompt.txt and e1.answer.txt byte-exact, so a checkout that git renders CRLF fails E1R-AC1 and E1R-AC2 on a seat that was clean.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "spec_asserts": "TO-LN-e-1-r2 BOUNDS: the checker re-derives the prompt and re-parses the reply, so a hand edit FAILs the seat criterion; a proof row's invocation is re-runnable by a verifier (PROOF_OF_SPEC.schema.json acceptance.invocation). The criteria are meant to fail on an edit, not on a checkout.",
    "world_is": "check_ln_r2.py:107-109 @619dec559f reads seats/<cell>.prompt.txt and .answer.txt with exact=True (newline='' keeps CR), then compares their sha256 to the seat record at :133-136 and :152. The blobs at eaafb46486 are LF (git ls-files --eol: i/lf w/lf), core.autocrlf=true, git check-attr shows no text/eol attribute. In this same worktree the tracked INVESTIGATION_v1.md is checked out i/lf w/crlf (820 CRLF of 820 LF), so git does render CRLF here; the seat files read LF only because blind_seat.py wrote them and git has not re-checked them out. In-memory test on the HEAD blobs: as-is matches result_sha256 / prompt_sha256 = True for both files; the same blob rendered CRLF = False for both. A verifier re-running E1R-AC1 (prompt and reply conditions) and E1R-AC2 (FAIL-NO-CANARY) on a checkout git wrote reads FAIL with no edit. The same read path serves the e2, e4 and l2 seat files.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py:42-46,107-109,133-136,152 @619dec559f",
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/seats/e1.seat.json @eaafb46486 (prompt_sha256 84ac10b1..., result_sha256 47cda3fa...)",
        "git ls-files --eol in worktree wk-lgic-naming-2-1 @eaafb46486: seat files i/lf w/lf; INVESTIGATION_v1.md i/lf w/crlf; git config core.autocrlf = true",
        "in-memory hash of git show HEAD:<seat file>: LF as-is matches the record (2 of 2), CRLF-rendered matches (0 of 2)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Filed as form, not significance. The fixed inputs are read-only to this worker, so nothing was changed. The candidate disarms belong to the issuer: an eol/-text attribute on exercises/r2/seats/, or the checker reading the committed blob or normalizing CR. Not exercised: the checker run on a fresh checkout (no extra worktree was made); the CRLF-render half is grounded by the channel file's own checkout in this worktree."
  },
  {
    "id": "LGIC_NAMING-W2-S5",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~2",
    "surfaced_at": "2026-09-14T22:05Z",
    "one_line": "The round-2 checker grades the seat's prompt and reply files byte-exact, but this box writes LF blobs as CRLF on checkout (core.autocrlf=true, no eol attribute). Once any checkout rewrites exercises/r2/seats/e2.prompt.txt and e2.answer.txt, re-running E2R-AC1 and E2R-AC2 will grade a clean seat FAIL.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ: org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py@619dec559f:42-46: read(path, exact) opens with newline='' when exact is true, so no newline is translated. :107-109: seat_parts reads <cell>.prompt.txt and <cell>.answer.txt with exact=True. :133-136: it grades prompt == want, sha(prompt) == prompt_sha256 and sha(answer) == result_sha256. :152: canary() returns FAIL-NO-CANARY when sha(answer) != result_sha256.",
        "READ: org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/blind_seat.py@619dec559f:65-70: build() reads its sources through git show, which gives the committed LF bytes. :153-156: write() writes the seat files with newline='', which gives LF.",
        "MEASURED: git ls-files --eol in worktree wk-lgic-naming-2-2 after commit 59f68115a4: the six exercises/r2 files read i/lf w/lf attr/ with the attribute empty, and core.autocrlf=true. In the same fresh worktree, org/standards/NAMING_SCHEMA.json, infra/logic/05_IDENTITY_SPINE.md and fixed_inputs/N3_ITEMS.json read i/lf w/crlf attr/, which is what a checkout on this box does to an LF blob.",
        "MEASURED: the safe-commit that made 59f68115a4 printed 'LF will be replaced by CRLF the next time Git touches it' for all six seat files.",
        "RUN: check_ln_r2.py e2-seat and e2-canary, run in this worktree on the LF bytes the seat wrote, printed VERDICT: PASS-CLEAN-SEAT (10 of 10) and VERDICT: PASS-CANARY-BLIND. The checker was NOT run on a CRLF copy. The FAIL is derived from the source lines above; it was not observed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_NAMING.TO-LN-e-2-r2 BOUNDS: 'the checker re-derives the prompt and re-parses the reply, so a hand edit FAILs the seat criterion', and 'Commit everything the seat wrote'. Criteria E2R-AC1 and E2R-AC2 are invocations a verifier re-runs.",
    "world_is": "Git makes, on every checkout, the edit the order forbids by hand. The seat files are committed LF, exactly as the seat wrote them. No .gitattributes rule pins their line endings, so every checkout on this box (the drain into the shared tree, or a verifier's worktree) writes them CRLF. check_ln_r2.py then compares those CRLF bytes against the LF prompt it rebuilds from git and against the LF hashes in e2.seat.json. E2R-AC1 then fails 'the prompt is the builder's' and 'the reply file is the session's reply, verbatim', and E2R-AC2 returns FAIL-NO-CANARY. E2R-AC3 and E2R-AC4 read through tsv(), which opens with universal newlines, so they are unaffected. seat_parts serves all four seat cells (e1, e2, e4, l2), so each has the same exposure.",
    "notes": "Filed by the operator of the seat, after its own run passed. ARMED: left alone, an ordinary L9 re-run of the order's own invocations inside a checkout grades a clean seat FAIL. Disarm owner is 2.0.0_SA_COO~G, the author of the fixed inputs and the seat that drains this branch. Two remedies are named here but not chosen: an eol=lf or -text attribute on exercises/r2/seats/, or normalizing CRLF inside read(exact). Both are outside this worker's grant, and nothing was edited. For 3.0.0_SA_CVO at L8/L9: grade E2R-AC1 and E2R-AC2 on LF bytes (git show 59f68115a4:<path>) or after the disarm."
  },
  {
    "id": "LGIC_NAMING-W3-S4",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~3",
    "surfaced_at": "2026-09-14T22:06Z",
    "one_line": "The seat files blind_seat.py writes (l2.prompt.txt, l2.answer.txt) are LF with no eol attribute on this core.autocrlf=true box, and check_ln_r2.py reads both with exact=True and compares them byte-for-byte with the builder's LF text and the recorded sha256. So a checkout other than the writing worktree renders them CRLF, and l2-seat and l2-canary would re-grade FAIL on a clean seat.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G -- the author of the read-only fixed inputs (check_ln_r2.py, blind_seat.py @b9ea6f3686) and the seat that drains and re-grades this branch. Remedy not chosen here: an eol=lf attribute on deliverables/exercises/r2/seats/** (as blind_seat.py itself carries), or the checker normalising line endings before it compares and hashes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py @b9ea6f3686 :42-46 read(path, exact) opens with newline='' when exact, so CR bytes are kept; :107-109 seat_parts() reads <cell>.prompt.txt and <cell>.answer.txt with exact=True; :133-134 requires prompt == the builder's output and sha(prompt) == prompt_sha256; :135-136 requires raw.json's result == answer and sha(answer) == result_sha256; :152 canary() returns FAIL-NO-CANARY when sha(answer) != result_sha256.",
        "ATTRIBUTES, this worktree at base 619dec559f: git config core.autocrlf = true; git check-attr text eol on n5-reader.tsv, l2.prompt.txt, l2.raw.json and l2.answer.txt = unspecified for all four; as written by the seat, all 6 files carry 0 CR bytes (l2.prompt.txt 50 LF, l2.answer.txt 9 LF).",
        "POSITIVE CONTROL, same worktree: git ls-files --eol reads 'i/lf w/crlf attr/' for a committed round-1 file without an attribute (deliverables/0.9.0_WK_LGIC_NAMING~3/namer-b.result.md, 40 CR bytes; fixed_inputs/r2/N5_R2.json, 38 CR bytes) and 'i/lf w/lf attr/text eol=lf' for fixed_inputs/r2/blind_seat.py (0 CR). A checkout on this box renders an unattributed LF text file CRLF.",
        "SIMULATION, 2026-09-14 ~22:0xZ: the checker's :133-136 comparisons, re-typed and run on the seat files as written, give prompt_sha_ok=True, answer_eq_raw=True, answer_sha_ok=True; the same comparisons on in-memory CRLF renderings give False, False, False. The checker itself was not run on a CRLF checkout, and this worker's files were not edited.",
        "AS WRITTEN: in the writing worktree all three criteria print PASS (l2-seat 'SEAT CONDITIONS: 10  HELD: 10', l2-canary 'CANARY ANSWERS: 2 of 2', l2-labeled 'ADDRESSES: 7  LABELED: 7'), twice each."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LGIC_NAMING.TO-LN-l-2-r2 BOUNDS: 'the checker re-derives the prompt and re-parses the reply, so a hand edit FAILs the seat criterion'; commit everything the seat wrote with the proof instance, which the COO drains.",
    "world_is": "The checker also FAILs on a line-ending change that git makes at checkout, with no hand edit. The records committed from this worktree grade PASS here, and would grade FAIL-SEAT-NOT-PROVED and FAIL-NO-CANARY when re-run from a checkout that renders them CRLF (the shared tree after the drain, or a verifier's fresh worktree), so a re-grade there cannot tell a clean seat from a doctored one.",
    "notes": "OBSERVATION, not BLOCKING: every criterion of this order passes by output in the writing worktree, and the committed blobs are LF (the seat's bytes). ARMED because the next normal act on these files (the COO's drain, then 3.0.0_SA_CVO's L8/L9 re-grade) is a different checkout. Shared dependency, NOT MEASURED here: the round-2 cells e1, e2 and e4 use the same blind_seat.py and seat_parts(), so their seat files should carry the same exposure; their files are not in this worktree. Nothing was edited to work around it: the fixed inputs are read-only and .gitattributes is outside this order's paths."
  },
  {
    "id": "LGIC_NAMING-W4-S1",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~4",
    "surfaced_at": "2026-09-14T22:09Z",
    "one_line": "LN-f-1-r2's worker face paraphrases the bd step as 'the vendor Black Diamond in a system or source position, and the firm 49 Financial otherwise -- as the rule says', but GRADING_RULE R3's test is ADJACENCY to a firm token, not position; read literally, the paraphrase reverses the reading of the 12 bd-* roles whose bd sits first with no firm token next to it. The r2 record follows R3's text.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D14/LGIC/LGIC_NAMING/task-orders/LGIC_NAMING.TO-LN-f-1-r2.firm-patterns.md@619dec559f:30 -- '`bd` is the vendor Black Diamond in a system or source position, and the firm 49 Financial otherwise -- as the rule says.'",
        "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@619dec559f:160-163 R3 -- 'It is the VENDOR blackdiamond when a V4 firm token is next to it, before or after, and the FIRM 49financial otherwise. CENSUS s.1 item 4 gives both readings: in bd-49f-session-trigger it is the vendor, in bd-allocations the firm.' bd-allocations carries bd in the first (system) position and the rule reads it as the FIRM.",
        "EFFECT, counted by python over org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json (vintage 2026-09-14 12:13:53 UTC, by_type.IAM_ROLE, 69 of 240 in the population): 20 roles carry bd; the two readings agree on the 7 whose bd sits first next to a firm token (bd-49f-* 6, bd-cot-keepalive-role); they part on the 12 whose bd sits first with no firm next to it (bd-allocation-checker-lambda-role ... bd-silver-merge-role). By R3 those 12 are {system}-49f-...-role, attributed to 49financial; by the paraphrase read literally, bd is the vendor in the system slot, the name carries no firm token, and S5 leaves it unscoped.",
        "DATA: org/standards/NAMING_SCHEMA.json@619dec559f v1.6 refused_tokens.bd ('The vendor is blackdiamond; the firm is 49financial') and PRD S10 give the two readings and no position test."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LGIC_NAMING.TO-LN-f-1-r2 worker face: '`bd` is the vendor Black Diamond in a system or source position, and the firm 49 Financial otherwise -- as the rule says.'",
    "world_is": "The rule's test is adjacency to a firm token. The paraphrase states a position test that the rule's own census example (bd-allocations, bd first, read as the firm) contradicts. Under R3, 49financial has 24 attributed roles; under the literal paraphrase it would have 12, and 12 more would be no firm's principal. The r2 record (deliverables/exercises/r2/n4-firm-patterns.md) follows R3, because the same sentence defers to the rule and the order's J1 grades against GRADING_RULE.md.",
    "notes": "OBSERVATION, INERT: no disposition of this cell is in doubt, since the order defers to the rule. The paraphrase is the issuer's, 2.0.0_SA_COO~G's, to align with R3. Whether R3's firm reading of these 12 is right is the rule's own interim choice (round 1's judgment point 1) and the registry's (LGIC_ENFORCE), and this row does not decide it."
  },
  {
    "id": "LGIC_NAMING-W4-S2",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~4",
    "surfaced_at": "2026-09-14T22:09Z",
    "one_line": "LN-f-1-r2 says both 'grade by GRADING_RULE.md' and 're-grade under NAMING_SCHEMA.json v1.6', and they part on the function slot. v1.6 resource.function (FN1, v1.5) writes an agent noun as its verb and never a kind word in the function. GRADING_RULE.md, written at v1.4 and not re-cut, reads the function as free vocabulary (R5) and keeps another type's kind in it (R6). 31 of LN-f-1's 68 canonical forms carry a kind word there. The r2 record follows the rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DATA: org/standards/NAMING_SCHEMA.json@619dec559f v1.6 resource.function -- 'an agent noun is always written as its verb (publisher -> publish, exporter -> export, scanner -> scan), because the kind names the thing ... A kind word (queue, host, topic, table, alarm) is never written in the function slot (FN1, v1.5)'.",
        "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@619dec559f:173-181 -- R5 'The function is free vocabulary.'; R6 'Otherwise the type's kind is APPENDED, and that token stays in the function. This includes a token that is another type's kind, such as -runner on a LAMBDA.' The header (:7) cites NAMING_SCHEMA v1.4; git log on the file at 619dec559f shows one commit, 51b0952d71.",
        "DIFF: NAMING_SCHEMA.json v1.4 (git show e04b802fe9) against v1.6 (@619dec559f), top-level field by field, by python: resource.function and resource.qualifier changed; firm_forms, refused_tokens, kind.by_type, resource.scope_form and system.reserved are unchanged.",
        "EFFECT, counted by python over the 68 canonical forms R1-R6 print for LN-f-1's population (org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json, vintage 2026-09-14 12:13:53 UTC): 31 carry a kind word of DATA.kind.by_type in the function slot (lambda 18, runner 6, api 5, layer 4, task 1). Agent nouns also appear (exporter, scheduler, processor, checker). Two examples that would read differently under FN1: advi-49f-floor-scheduler-role is CONFORMANT by the rule; bd-49f-runner-role is ALIAS to blackdiamond-49f-runner-role, and runner is EC2_INSTANCE's kind.",
        "ANALYSIS: org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md@619dec559f s.2 states FN1 for naming 'Where the item DESCRIBES the action'; s.5 rules no re-run for LN-g-1, so the rule's text stands as cut at v1.4."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LGIC_NAMING.TO-LN-f-1-r2 worker face: 'Grade each by ... GRADING_RULE.md to its canonical form and its firm' and 're-grade under NAMING_SCHEMA.json v1.6'; F1R-J1: 'each attribution and canonical form follows GRADING_RULE.md'.",
    "world_is": "FN1 is phrased for naming from an item's description, but as data it reads as a constraint on every resource name's function slot, and the grading rule's text does not apply it. For LN-f-1 the two part ONLY in the function slot. No firm, scope slot, attribution or pattern catch moves, because each pattern reads only the firm token after the system. The r2 record prints the rule's canonical forms and states the divergence in its section 4.",
    "notes": "OBSERVATION, INERT for this cell: FWD-3's patterns and its three dispositions do not depend on the function slot. One question stays open: does a grade's canonical form apply FN1 (the rule gains a step), or does FN1 bind only a namer? That belongs to the rule's owner and the schema's author, 1.0.0_SA_CTO. INFERRED, not counted: the same question reaches the canonical forms the rule prints for any kind-graded type, not only roles."
  },
  {
    "id": "LGIC_NAMING-S16",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T23:18Z",
    "one_line": "Issuer's disarm of LGIC_NAMING-W1-S6, W2-S5 and W3-S4: the seat records are now checked out byte-exact on every tree, and the round-2 checker PASSES the three drained seats on the merged shared tree, which has core.autocrlf=true.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROWS: W1-S6, W2-S5 and W3-S4 (all ARMED, disarm_owner 2.0.0_SA_COO~G): the seat records are committed LF, core.autocrlf=true rewrites them to CRLF on checkout, and fixed_inputs/r2/check_ln_r2.py compares each prompt and reply byte for byte against its seat record.",
        "FIX @ca44748a44, landed before any seat branch merged: one line in the root .gitattributes, org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/seats/** binary, following that file's own precedent for hash-pinned assets. The lane refused a .gitattributes inside the seats folder (TREE_DELIVERABLES); owned-paths-validate admits this seat only at the root and in its own serial folder.",
        "DISCRIMINATOR, on the merged shared tree (core.autocrlf=true), after the drains @a25a26ee34, @866f250fec and @24460c0114: git ls-files --eol reads i/lf w/lf attr/-text on all ten e1 and e2 seat records. The checker printed PASS-CLEAN-SEAT and PASS-CANARY-BLIND for e1, e2 and l2 on those bytes.",
        "HEAD at this write: f6d71f6b29."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition v4 s.0c: the checker 're-derives the prompt with the same builder and re-parses the verbatim reply, which the seat record hashes'. A clean seat grades PASS wherever the checker runs.",
    "world_is": "Before the fix, a clean seat graded PASS only in the worktree that wrote it; every checkout git wrote would have graded it FAIL. After the fix, the records keep their bytes on every checkout, and the measured PASS holds on the shared tree.",
    "notes": "DISARM, per the three rows' own clause, by their disarm owner. The checker (a frozen fixed input) and the seat files were not edited. The round's later seat (e4) is covered by the same rule, because its records land under the same folder. For 3.0.0_SA_CVO at L8/L9: the seat criteria can be re-run on any checkout. INERT: no clean seat can now read FAIL for its line endings, and none has."
  },
  {
    "id": "LGIC_NAMING-W6-S4",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~6",
    "surfaced_at": "2026-09-14T23:58:27Z",
    "one_line": "LN-e-5 round 2's E5R-AC1 invocation (check_ln_r2.py e5-correct) prints VERDICT: FAIL-MISREAD, not the expected PASS-ALL-CORRECT: the reader marked the key's firm-or-none token on 16 of 18 N3 names; i09 (mdpf-demo-publish-failure-alarm) is marked none where N3_KEY_R2.json reads demo, and i11 (pathfinder-etfs-ingest-task) is marked pathfinder where the key reads none.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: cd C:/Users/AndrewBerman/Desktop/ajb_workspace/.worktrees/wk-lgic-naming-2-6c && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py e5-correct, worktree HEAD 5fb93bb734 -> 'WRONG: i09  name=mdpf-demo-publish-failure-alarm  marked=none  expected=demo' / 'WRONG: i11  name=pathfinder-etfs-ingest-task  marked=pathfinder  expected=none' / 'ITEMS: 18  CORRECT: 16  WRONG: 2 (key: N3_KEY_R2.json, firm or none)' / 'VERDICT: FAIL-MISREAD', rc=0.",
        "INPUTS: org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-namer-a.tsv @eaafb46486 (i09 -> mdpf-demo-publish-failure-alarm, i11 -> pathfinder-etfs-ingest-task); r2/n3-reader.tsv @9096ea3c49 (those names marked none and pathfinder); deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/N3_KEY_R2.json @b9ea6f3686 (key i09 demo, i11 none; changed_from_round_1 i11 etfs -> none).",
        "CHECKER: deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_ln_r2.py:237-252 @b9ea6f3686 e5_correct compares the reader's mark on each namer-A name with the key's token as exact strings and prints FAIL-MISREAD on any mismatch.",
        "E5R-AC2 on the same inputs printed VERDICT: PASS-ONE-REFERENT-EACH (0 clashes across 18 names, 7 tokens marked), so only E5R-AC1 holds the order open."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-LN-e-5-r2 E5R-AC1: 'the reader marked the expected firm, or none, on every item', invocation check_ln_r2.py e5-correct, expect 'VERDICT: PASS-ALL-CORRECT'.",
    "world_is": "The invocation prints 'VERDICT: FAIL-MISREAD' with 16 of 18 correct. The cell scores and does not read or name, so no mark can be changed inside LN-e-5, and the order stays open on the E5R-AC1 FAIL. r2/n3-reader-score.md records every WRONG line with the name, the mark and the expected token.",
    "notes": "Filed by the scoring worker because the named invocation did not produce the named result. The task order calls a wrong mark 'the outcome's evidence, not a defect to fix', so nothing is edited. For 3.0.0_SA_CVO's L8 disposition."
  },
  {
    "id": "LGIC_NAMING-W2-S6",
    "project": "LGIC_NAMING",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_NAMING~2",
    "surfaced_at": "2026-09-15T07:23:44Z",
    "one_line": "TO-LN-e-2-r3 names its result file namer-b.result.md, beside the round-3 instance in deliverables/0.9.0_WK_LGIC_NAMING~2/. That path already holds round 2's namer-B result (TO-LN-e-2-r2), so writing the order's file replaces round 2's record at HEAD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ: org/missions/D14/LGIC/LGIC_NAMING/task-orders/LGIC_NAMING.TO-LN-e-2-r3.namer-b.md@6705066c68, <proof_of_spec> block: instance at deliverables/0.9.0_WK_LGIC_NAMING~2/LGIC_NAMING.TO-LN-e-2-r3.namer-b.proof_of_spec.json, 'Result file `namer-b.result.md` beside it'.",
        "READ: org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~2/namer-b.result.md@6705066c68:1 reads '# LGIC_NAMING.TO-LN-e-2-r2 -- namer B, round 2 -- result'.",
        "READ: org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~2/LGIC_NAMING.TO-LN-e-2-r2.namer-b.proof_of_spec.json@6705066c68:66-73 pins that result file at 59f68115a4. Round 2's text therefore stays in git at that pin after the overwrite."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-LN-e-2-r3 <proof_of_spec>: 'Result file `namer-b.result.md` beside it', meaning beside the round-3 instance in deliverables/0.9.0_WK_LGIC_NAMING~2/. The order says nothing about a file already at that path.",
    "world_is": "deliverables/0.9.0_WK_LGIC_NAMING~2/namer-b.result.md is already tracked at base 6705066c68 as round 2's namer-B result. Following the order rewrites it with round 3's result. Round 2's text survives at 59f68115a4, where round 2's own proof pins it.",
    "notes": "Filed because doing what the order said also overwrote a record the order did not mention. The round-3 proof does not list the result file as an artifact: .tools/proof-of-spec-check.py:383-386 @6705066c68 refuses, in a dry run, a tracked file pinned PENDING-THIS-COMMIT that is not staged, and this file is tracked. INERT: nothing is lost from git, and round 2's proof still resolves at its pin."
  }
]
```
