# NFRA_TRNSPT -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~T` at the L5 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_TRNSPT-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a
seat's row is `NFRA_TRNSPT-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `NFRA_TRNSPT-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
{
  "id": "NFRA_TRNSPT-S1",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~T",
  "surfaced_at": "2026-09-30T13:35:00Z",
  "one_line": "The three gateway mail tools the PRD names as NFRA_OPLGTW's (site Z) build are being built UNCOMMITTED in laptop worktrees wt-gw-f2, wt-gw-f3 and wt-gw-int by seats (4.0.0_SA_CRO~T / 0.7.0_AE_CloudOps) that the 2026-09-30 07:52Z reboot killed and the relaunch word did not restart.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO (owns the S12 relay to site Z and the seating of the laptop gateway work; this seat only surfaces)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C C:/Users/AndrewBerman/Desktop/wt-gw-f2 status --porcelain (2026-09-30 13:2xZ): M app/data_entitlement.py, M app/destructive_ops.py, M app/tools.py, M tests/test_entitlement_admin.py, ?? tests/test_list_email_filtered.py",
      "git -C C:/Users/AndrewBerman/Desktop/wt-gw-f3 status --porcelain: M app/data_entitlement.py, M app/destructive_ops.py, M app/tools.py, ?? tests/test_inspect_email_attachment.py",
      "git -C C:/Users/AndrewBerman/Desktop/wt-gw-int status --porcelain: three files staged (M in the index), nothing committed; branch gw-mail-tools-int at 2ab90bf162 = CLOUD",
      "org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md: 'wt-gw-f1 / f2 / f3 / int -- gateway mail tools (CRO~T / CloudOps)'; neither seat is in the relaunch table",
      "PRD C-GATEWAY-TOOLS (org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:110): the three tools are NFRA_OPLGTW's (site Z), requested through MSTR's bus at L6"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The attachment-download tool, the filtered paged mail list and ccRecipients are built by NFRA_OPLGTW on site Z; this project does not build them.",
  "world_is": "Uncommitted implementations of at least the filtered list and an attachment inspector sit in three laptop worktrees whose owning seats are dead; nothing on CLOUD carries them; site Z's state is unread from this seat.",
  "notes": "Not touched by this seat (a worktree with uncommitted work is never removed; COO_STARTUP.md worktree-wipe edict). The L6 relay to the CTO names the worktrees so site Z and the laptop do not build the same tools twice."
},
{
  "id": "NFRA_TRNSPT-S2",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~T",
  "surfaced_at": "2026-09-30T13:48:00Z",
  "one_line": "The deployed gateway's read_email returns the raw HTML body but no internetMessageId, ccRecipients, conversationId or sentDateTime, so C-DEDUP's primary key cannot be computed this round and every round-1 mail row carries id_source=fallback.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~T (round-1 bronze contract in the decomposition uses the fallback id; the primary key rides the S12 tools)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mcp opalgateway read_email on message AAMkAGJl...fhTyRAAA= (2026-09-30 13:4xZ, as Andrew@opalinvest.com): keys returned = @odata.context, @odata.etag, id, receivedDateTime, subject, body{contentType:html, content}, from, toRecipients",
      "mcp opalgateway list_email_attachments on the same message: per attachment id, name, size, contentType, isInline; no contentBytes; four non-inline image/png charts, zero PDFs",
      "PRD C-DEDUP (org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:112): record_id = sha256(internetMessageId); fallback = hash of (sent_at, sender domain, subject, body hash) flagged id_source=fallback"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "record_id = sha256(internetMessageId); conversationId groups threads; partition by sent date.",
  "world_is": "Today's tool exposes none of those three fields; the round-1 contract partitions by receivedDateTime and derives the id from sender, receivedDateTime, subject and the body hash, flagged fallback on every row.",
  "notes": "Also observed: the v3 brief's claim that raw HTML needs a NEW gateway call is not so -- body.content is the raw HTML; the cut rules (Signature, appendonsend, divRplyFwdMsg, the 49 compliance boilerplate) are visible in it."
},
{
  "id": "NFRA_TRNSPT-S3",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~T",
  "surfaced_at": "2026-09-30T14:45:00Z",
  "one_line": "All 12 generated naming targets at CLOUD HEAD are stale: stamped registry@5576b01fd4684bfa while infra/logic/registry at HEAD hashes ffa41913935c3281, so a `python lib/opal_naming.py generate --out .` moves every target before NFRA_TRNSPT adds a row.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO (the registry lane's owner decides who restamps; round-1 cell TR-g-1's regenerate will carry the restamp for its own rows and the issuer names it to 2.0.0_SA_COO~P/~M before the drain)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_registry_check.py targets at HEAD a7a6d286f2+ (2026-09-30 14:4xZ): TARGETS-STALE n=12 moved=[all 12]; git diff --stat: 11 workspace files, 12 insertions 12 deletions, each a GENERATED stamp line only; the portal target moved likewise (10-line diff)",
      "data/firm_registry.json:2 at HEAD: '_generated ... registry@5576b01fd4684bfa'; regenerated: 'registry@ffa41913935c3281'",
      "git log -- infra/logic/registry/: 0146e0c954 (2026-09-30 06:48Z, MSTR merge of origin/CLOUD 33c1d096a3, 1460 site Z commits) and d451070fb1 (4.0.0_SA_CRO~Z, rivalfunds row) postdate the last target regenerate f13d9e9222 (2026-09-29 20:10Z)",
      "the tree was restored to HEAD's bytes with git restore after the dry-run; nothing of this drift is committed by this seat"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Every generated target is byte-identical to what the registry at HEAD produces (LGIC_ENFORCE: per-view registry hashes, 39cbad4214).",
  "world_is": "The 12 targets carry the pre-merge registry hash; the site Z registry change landed without a laptop regenerate, and no gate refused the merge.",
  "notes": "Blast radius per CTO placement 2026-09-29 step 1: a restamp moves blob hashes that signed IRPT packets pin; the issuer names TR-g-1's drain to ~P and ~M first. Whether a merge-time gate should regenerate is the CTO's, not this project's."
},
{
  "id": "NFRA_TRNSPT-W4-S1",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T15:15:00Z",
  "one_line": "Both public name-list fetches Andrew's word covers were refused by the hosts' bot protection, so names/given_names.txt and names/surnames.txt do not exist and TR1-a1-AC1/AC2 cannot pass.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "2026-09-30T15:00:59Z curl -L -A Mozilla/5.0 https://www.ssa.gov/oact/babynames/names.zip -> HTTP 403 'Access Denied' (399-byte HTML, Akamai reference #18.e537c517.1790780459.2aa1f01); python requests retry at ~15:01Z -> 403 again",
      "2026-09-30T15:01:00Z same client https://www2.census.gov/topics/genealogy/2010surnames/names.zip -> HTTP 200 with a 247-byte 'Request Rejected ... support ID 13427891564882941819' HTML page, not a zip (starts b'<htm'); python requests retry -> same body",
      "sha256 of the SSA refusal body 4903db40d959d09244de08efa4c5004cc1306b46d9b9b6c2af3f9f896ee71091; of the Census refusal body adcd2c1213a905d5c1481b523a3f0f1c789c1f9885d1f31f410d86ec5cdb91d0 (neither is committed; no archive was obtained)",
      "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_assets_check.py -> ASSETS-BAD name dictionary entries=0 (< 50000)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "ONE fetch each of the SSA names.zip and Census 2010 surnames names.zip yields the archives to distil into the name dictionary (>= 50,000 entries); 'if a fetch fails, stop on that file and file a surprise row: never substitute a hand-typed list'.",
  "world_is": "Both hosts refuse a non-browser client (SSA 403, Census a 200 rejection page); the worker used its one bounded retry per host and stopped; no name file was written and none was hand-typed. The other five assets, README, lock (name_dictionary_entries 0) and tests are committed; the size and Will/Grant tests fail honestly.",
  "notes": "Unblock is the issuer's or Andrew's: a browser-mediated download placed for the worker, a different public mirror Andrew names (egress word is per-use), or an operator-run fetch; then the worker re-runs pin.py-style pinning and AC1/AC2. The tests were not weakened."
},
{
  "id": "NFRA_TRNSPT-W4-S2",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T15:16:00Z",
  "one_line": "The task order asks for a null-address row for Yang's unmeasured 49financial address inside authors.json's authors list, but the issuer's r1_assets_check.py calls a['address'].lower() on every authors row and would raise on null.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_assets_check.py: addrs = {a[\"address\"].lower() for a in authors[\"authors\"]}",
      "task order build item 1 and 'Measured at the cut': carry a null row with claim: absent"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "authors.json {\"authors\":[{name,address,role,claim,basis}]} carries Yang's unmeasured 49financial row with address null and claim absent, and the issuer's check accepts the file.",
  "world_is": "A null address inside authors[] makes the issuer's check raise AttributeError; the worker put the null/absent row under a separate top-level key 'unmeasured' in authors.json so the checker and the wipe's read of authors[] stay total.",
  "notes": "If the issuer prefers the row inside authors[], the checker needs a None guard; the wipe (TR-w-1) should read both keys."
},
{
  "id": "NFRA_TRNSPT-W4-S3",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T15:35:00Z",
  "one_line": "The commit-time naming gate (LGIC_ENFORCE) REFUSES the two ordered data assets authors.json and client_domains.json as NEW hand-kept carriers of the firm tokens 49financial, 49f, inflection and cottonwood, so they cannot be committed within this order's grant.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/safe-commit.sh ... at 2026-09-30 ~15:2xZ: 'NAMING-GATE: REFUSE 5 graded' -- data/transcripts/assets/authors.json:12 manav.shah@49financial.com -> lookup('49financial'); client_domains.json:4 49financial.com, :5 49f -> lookup('49financial'); :12 inflection -> lookup('inflection'); :19 cottonwood -> lookup('cottonwood'); commit aborted",
      ".tools/naming-gate.py header: a firm token outside registry files, builder-call arguments and generated blocks is a hand-kept carrier and a NEW one is refused; the waiver kind is an R20 declared exception (a register entry outside this order's paths)",
      "infra/logic/registry/scopes.json:44 already carries email_domain '49financial.com' on the 49financial scope, so the domain table overlaps the registry"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Build items 1-2: authors.json and client_domains.json carry the measured addresses, domains and firm keys (49f, inflection, cottonwood) as versioned data assets committed under data/transcripts/assets/.",
  "world_is": "The gate grades JSON string values; the two files hold exactly those tokens by design. The worker did NOT obfuscate the strings to slip past the gate. Committed subset: allowlist, model_aliases, README, lock (pinning only what is committed), tests, rows, proof. authors.json and client_domains.json sit UNCOMMITTED in the worktree (copies in .scratch/held); the lock on disk is re-pinned over all six for the release.",
  "notes": "Unblock is the CTO's/issuer's: an R20 declared exception for the two files (register row plus a read_context entry), or a ruling that the client-domain and firm-key data are read from the registry (lookup) so the file carries none. Either way the order's paths may need to widen."
},
{
  "id": "NFRA_TRNSPT-W4-S4",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T15:50:00Z",
  "one_line": "safe-commit's missions-tree check refuses every org/missions commit from this worktree with INDEX-DRIFT org/projects/NFRA_TRNSPT.json (index PRD vs tree EXECUTING) because the worktree branch predates CLOUD 17ad3ea043, the issuer's index fix.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/safe-commit.sh ... (2026-09-30 ~15:4xZ): 'BLOCKED: missions-tree-check ... [INDEX-DRIFT] org/projects/NFRA_TRNSPT.json: dep_stage: index=PRD tree=EXECUTING'; all other gates (commit-gate, naming-gate PASS 0 graded, surprise-row-gate, to-pipeline-gate) passed on the subset",
      "git merge-base --is-ancestor 17ad3ea043 HEAD -> rc 1 (HEAD daee98b79f); git show --stat 17ad3ea043: org/projects/NFRA_TRNSPT.json only, 2 insertions 2 deletions, authored by 2.0.0_SA_COO~T"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The worker commits its deliverables on its worktree branch with safe-commit.sh (order notes and standing worker rules: never merge, never widen the grant).",
  "world_is": "The order's own base lacks the issuer's index fix, org/projects/NFRA_TRNSPT.json is outside this order's grant and merging CLOUD is forbidden to a worker, so nothing could be committed; all work sits uncommitted in the worktree and the ROW ITSELF is uncommitted.",
  "notes": "Unblock: the issuer/integrator merges CLOUD 17ad3ea043 into wk-NFRA_TRNSPT-4 (sibling ~3 records the same remedy in its row W3-S1) or tells the worker to; then the worker commits the prepared set (msg in .scratch/msg.txt) after re-checking naming-gate on the two firm-token assets (W4-S3)."
},
{
  "id": "NFRA_TRNSPT-W4-S5",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T16:40:00Z",
  "one_line": "The issuer's three rulings on W4-S1, W4-S3 and W4-S4 were applied as amended: CLOUD merged (17ad3ea043 in), client_domains.json retired with the table read from registry email_domain, authors.json reshaped with no firm token, name lists vendored from the PyPI sdist names 0.3.0.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~T",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "issuer message to 0.9.0_WK_NFRA_TRNSPT~4 (amended order face, 2026-09-30): RULING 1 merge CLOUD; RULING 2 retire client_domains.json, authors.json shape with firm_domain_rule; RULING 3 pip download names, one fetch",
      "git merge --no-edit CLOUD twice: 17ad3ea043 in HEAD; infra/logic/registry/scopes.json already carries email_domain on the three FIRM rows (49financial.com, inflectionwealth.com, cottonwoodmail.com) plus demo.test; issuer's recut r1_assets_check.py printed 'ASSETS-PINNED n=5 names=93962 registry_domains=4' rc=0",
      "pip download names --no-deps --no-binary :all: -> names-0.3.0.tar.gz sha256 726e46254f2ed03f1ffb5d941dae3bc67c35123941c29becd02d48d0caa2a671; surnames.txt 88799 lines + given_names.txt 5163 lines = 93962 (dist.all.last, dist.female.first, dist.male.first)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The original order face named authors.json and client_domains.json as carriers of firm tokens and a SSA/Census name-list fetch.",
  "world_is": "The amended face replaced all three; W4-S1, W4-S3 and W4-S4 stand as written and are superseded by these applied rulings. W4-S2 is moot (Yang's second address is covered by firm_domain_rule)."
},
{
  "id": "NFRA_TRNSPT-W4-S6",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T17:30:00Z",
  "one_line": "lib.opal_naming.address() refuses object=\"\", so the order's bronze prefix call address('outlook','transcripts','bronze','analysis_commentary','date=<d>','') cannot run as written.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming.py address() at HEAD 4ef97cc7dd: `if not isinstance(object, str) or not object ...: raise ValueError`",
      "python call address('teams','transcripts','bronze','analysis_commentary','date=2026-09-30','') -> ValueError; object=None -> s3://opal-data-transcripts/teams/transcripts/bronze/analysis_commentary/date=2026-09-30"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-TR-w1 build item 2: the bronze partition prefix is address(source, scope, 'bronze', 'analysis_commentary', 'date=<d>', '') (a trailing empty object).",
  "world_is": "address() raises ValueError \"object must be a non-empty ASCII string not starting with '/'\" for object=''; object=None returns the partition address without a trailing slash. silver.py builds the prefix as address(..., partition) + '/' instead; the output key still uses the object argument."
},
{
  "id": "NFRA_TRNSPT-W4-S7",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T17:30:00Z",
  "one_line": "This branch's registry has no `outlook` source row (it is TR-g-1's, on wk-NFRA_TRNSPT-3 @8e9ed1b539), so address('outlook',...) raises here; the silver test borrows a registered source until that row drains.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python: opal_naming.address('outlook','transcripts','bronze','analysis_commentary','date=2026-09-30') -> ValueError source 'outlook' is not a systems.json key (worktree wk_nfra_trnspt_4 HEAD 4ef97cc7dd)",
      "git show 8e9ed1b539 -- infra/logic/registry/systems.json: adds rows outlook and sharepoint; git branch --contains 8e9ed1b539 -> wk-NFRA_TRNSPT-3 only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-TR-w1 build item 2: silver reads and writes under address('outlook','transcripts', ...) built by lib.opal_naming.",
  "world_is": "On this base the registry's systems.json has no key `outlook` (ValueError: source 'outlook' is not a systems.json key). silver.py takes the source from its own directory name; the test test_outlook_silver.py monkeypatches silver.SOURCE to the first registered source that resolves a bronze address ONLY when 'outlook' does not resolve, and uses the real one once TR-g-1 has drained. The real run at the drain must resolve address('outlook',...) for real; the issuer's run at the drain is that proof."
},
{
  "id": "NFRA_TRNSPT-W4-S8",
  "project": "NFRA_TRNSPT",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_NFRA_TRNSPT~4",
  "surfaced_at": "2026-09-30T17:30:00Z",
  "one_line": "Wipe limits found while building: a name is matched in another case only with same-message evidence (or ALL-CAPS in the dictionary); capitalised surnames that are also English words (Ask, Mail, Reach) are wiped at sentence start; capitalised non-stopword words (headings, labels) go to residual flags, so real messages will hold out often.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/outlook/wipe.py wipe_blocks (commit e555ef8ac9): pass 1 learns names per message, pass 2 applies; STOPWORDS list",
      "python: wipe_blocks('we asked ottoline today') with ottoline in the given-name set leaves it unchanged; 'Ask' and 'Mail' are members of surnames.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "C-WIPE: names applied case-sensitively behind an allowlist; anything capitalised and unknown goes to pii_residual_flags and is held out; C-WIPE-GATE plants a name 'in a different case'.",
  "world_is": "Case-sensitive dictionary matching means a standalone lower-case name (e.g. 'we asked ottoline') is NOT wiped unless the same message showed the name capitalised or ALL-CAPS; matching lower-case case-insensitively would wipe ordinary words (will, grant, mark, rate). The surnames list holds ordinary English words, so sentence-initial 'Ask'/'Mail' are wiped unless in the stopword list (a small one is in wipe.py). The planted-token test plants the lower-case name beside its ALL-CAPS form. The held-out rate on the real sample is unmeasured here; the issuer's real silver run prints held_out=<h>."
}
]
```
