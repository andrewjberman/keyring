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
  }
]
```
