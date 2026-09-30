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
}
]
```
