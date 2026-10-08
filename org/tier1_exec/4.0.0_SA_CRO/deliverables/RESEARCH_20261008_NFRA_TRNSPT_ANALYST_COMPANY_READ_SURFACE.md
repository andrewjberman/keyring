# RESEARCH -- where an analyst reaches the transcript company read (NFRA_TRNSPT FWD-5, under FWD-8's reader rule)

**archetype:** EXPLORE
**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-08
**Ask:** 1.0.0_SA_CTO~DELL2 msg 1748 ([SELF-DRIVE dell2] design fork).
**Read here** (at HEAD of `box/dell2`): `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md` (FWD-5 :47-49, FWD-8
:64-69, C-READERS :121, v0.2 :265-271); `data/transcripts/scripts/teams/research_read.py` (102 lines, @42ebf001bf);
`infra/aws/ec2/opal-gateway/app/` (`asker_scope.py`, `data_entitlement.py`, `query_v0.py`, `internal_role.py`,
`refs/DATA_CATALOG.yaml`, `server.py`, `config.py`).

## Recommendation (one design)

**One asker-scoped tool on the existing Opal gateway: `transcript_company_read(company, aliases)`.**
- **Where it lives:** the tool is `research_read.company_turns`, unchanged in behavior (held_out rows never matched or
  returned).
- **What it reads:** it runs under a NEW dedicated reader role whose only grant is the wiped silver prefix of
  `opal-data-transcripts`. That role IS FWD-8's "separate, narrower reader".
- **Who may call it:** only a person whose gateway grant names it (Entra tenant and object id, never email).
- **How the analyst reaches it:** the way analysts already reach Opal data. They ask the Teams agent or use the gateway
  connector; they never open a file.

## 1. What an analyst already uses (the estate's pattern)

| surface | what it is | evidence | fit for FWD-5 |
|---|---|---|---|
| Gateway asker path (`opal_asker_query`) | colleagues ask the Teams agent; every answer is scoped to the **asker's own** grant, resolved server-side from the Teams message, never from an argument | `asker_scope.py:1-30` (Andrew-direct 2026-09-24, "the real engineering comes in its entitlements per user/entra-id") | **the pattern to reuse** |
| Per-person grants | `principal_profile` + versioned `data_entitlement` keyed by tid/oid; scope names datasets, operations and optional `portal_channels`; fail-closed reads | `data_entitlement.py:1-30` | the "who may call" mechanism, already built |
| Internal reader role | the gateway assumes a role from an env ARN at call time, with **no fallback** to default credentials | `internal_role.py:1-25` | the template for the narrower reader |
| Catalog-gated fetch (`query_v0`, `gateway_query_catalog`) | fetches ONE served JSON object from `opal-data-portal-v2` | `query_v0.py:4,58,105` (`BUCKET = "opal-data-portal-v2"`); catalog header "WIDENING IS ANDREW-ONLY" | **not a fit as is** (section 3) |
| Headless transcript routes `/hx/transcripts/...` | the gateway's pull of raw meeting transcripts from Graph (own prefix, own bearer, meeting allowlist) | `server.py:67,1084-1087`; `config.py:231-240` | raw-side pull for the pipeline, not an analyst read |
| Portal | no transcript or research-meeting page | `portal/src/pages/**/*ranscript*`: 0 files | would be new build |
| The CLI `research_read.py --company X` | runs under the caller's own AWS identity | `research_read.py:1-7` | an analyst has no AWS identity; this is "opening a file" by another name |

## 2. The design in parts

1. **The read.** Lift `company_turns` into the gateway as a tool. Same input (company plus aliases), same exclusion
   (`held_out=FALSE` only; held-out rows counted, never shown). Same limits as `query_v0`: at most 1,000 turns, 10
   seconds, 30 calls per minute per key.
2. **The narrower reader (FWD-8).** A new IAM role, assumed only by the gateway (`internal_role.py` pattern, its own env
   ARN), with `s3:ListBucket` and `s3:GetObject` on the **silver research-meeting prefix of `opal-data-transcripts` only**
   (the builder's address, `parse_silver._address("silver", "research_meeting", ...)`). It has no grant on bronze. The
   bucket policy's named raw readers (Andrew, the terminal account, the two Dell agent users; C-READERS) are unchanged.
   The role reads only wiped data, so it never sees the original.
3. **Who may call.** A new dataset name in the grant scope (for example `research_transcripts_wiped`, operation
   `query`), granted per person by the existing admin path. The tool refuses anyone whose active grant does not name it.
   The asker is resolved as `asker_scope.py` does it, server-side, never from a tool argument.
4. **The refusal demonstration (FWD-8 DONE WHEN, seat-driven).** Calling the tool as a principal with no such grant
   returns a refusal, repeatable on demand. Calling the reader role against a bronze key returns AccessDenied, also
   repeatable.
5. **The audit row.** Each call writes who, which company term and the counts (turns, meetings, held-out skipped). It
   never writes the text, which carries C-READERS' content rule over to the copy as hygiene.

## 3. Why not the catalog path or the portal

- **The catalog path** serves JSON from one bucket (`opal-data-portal-v2`). It has no parquet resolver (D6-3 ruling in
  the catalog header), and widening it is Andrew-only. Fitting transcripts in would mean either copying wiped transcript
  text into the portal bucket, which widens who can read it, or adding a second bucket and a parquet resolver to a
  surface ruled plumbing-only. Both are bigger and looser than one scoped tool.
- **The portal** has no transcript page. A page would need a served artifact plus a frontend. That belongs in the
  frontend mapping session with Andrew (DSGN_IRPTV2 / COO~U2), not in FWD-5's first exercise.

## 4. Owners and the one word needed

- The gateway tool: site Z's `NFRA_OPLGTW` owns the gateway code (C-GATEWAY-TOOLS precedent; requested via MSTR's bus).
- The reader role and its policy: AE CloudOps, through `safe-apply`.
- **Andrew's word:** which analysts are granted. FWD-5's DONE WHEN needs "one analyst". The PRD names none.
- FWD-5 is then EXERCISED when that analyst asks the Teams agent "what was said about <company>" and gets the turns back
  without opening a file.
