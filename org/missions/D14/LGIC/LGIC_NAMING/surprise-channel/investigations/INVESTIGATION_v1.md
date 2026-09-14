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
  }
]
```
