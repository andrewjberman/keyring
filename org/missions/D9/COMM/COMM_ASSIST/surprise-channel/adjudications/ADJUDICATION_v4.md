# COMM_ASSIST -- surprise channel, ADJUDICATION v4 (laptop) -- round 17, the CVO's residual row on the replay fix

**Author:** `3.0.0_SA_CVO~L`, 2026-10-14 ~01:1xZ, written with the CVO never-widen half for CA-i-12
(`deliverables/3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17B_DEPLOY_20261014.md`, SIGNED). C-S5's named path is closed by
that build; this INERT row carries what remains for the round-17 slug.

```json
[
 {
  "id": "COMM_ASSIST-C-S6",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T01:15Z",
  "one_line": "Residual after the replay fix (8a480805e5): drafts with no seq (End of Day, mail, job) are bound only by tag, version and a 200-entry hash window; End of Day tags (E+MMDD) repeat yearly on a fresh object and mail tags M000-M999 are reusable, so a retained signed answer can match a later draft. Closure: refuse a payload whose signed_at is older than a stated bound.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD v0.7 FWD-7: nothing else can answer in Andrew's place; a muse answer acts once, for the draft it was given for.",
  "world_is": "At 8a480805e5, on_muse_reply binds seq only when the pending draft has one (chat drafts). eod_tag (tenant.py:76-77) is 'E' + MM + DD, so the tag repeats each year on a new eod:<day> object with an empty muse_acted; mail_tag hashes M000-M999 and allows reuse within the mail object, and muse_acted keeps the last 200 hashes. No signed_at age is checked. Reaching it needs a retained signed answer, a direct muse.reply send and a tag collision; no forwarder exists yet.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show 8a480805e5:data/transcripts/scripts/teams_chat/tenant.py lines 76-77, 493, 570-656",
    "git show 8a480805e5:data/transcripts/scripts/teams_chat/mail_requests.py lines 165-173",
    "deliverables/3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17B_DEPLOY_20261014.md"
   ]
  },
  "disposition": "UNDER_INVESTIGATION"
 }
]
```

-- 3.0.0_SA_CVO~L
