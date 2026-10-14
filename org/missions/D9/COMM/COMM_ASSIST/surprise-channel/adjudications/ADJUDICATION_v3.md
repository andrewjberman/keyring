# COMM_ASSIST -- surprise channel, ADJUDICATION v3 (laptop) -- round 17, the CVO's own row

**Author:** `3.0.0_SA_CVO~L`, 2026-10-14 ~00:0xZ, written with the CVO never-widen half for CA-i-4
(`deliverables/3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17_DEPLOY_20261014.md`). The half is SIGNED; this row is the
hazard it carries to CA-i-5, ARMED until its owner disarms it.

```json
[
 {
  "id": "COMM_ASSIST-C-S5",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-14T00:06Z",
  "one_line": "A muse-signed answer can be replayed: the signature binds tag and (optional) version, a chat's tag is stable and a new draft restarts at version 1, so one signed 'send' verifies against a later draft Andrew never saw; the dell2 account can read answers/ and send muse.reply directly. Not reachable until CA-i-5's forwarder; must be closed before it.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~CA: before CA-i-5 installs the forwarder, the receiver requires version and binds the answer to the draft's seq (or refuses a signature it has already acted on), and drafts.json carries seq; disarmed when a fixture replay of a signed send against a later draft at the same tag and version is refused",
  "spec_asserts": "PRD v0.7 FWD-7: Andrew answers from muse and nothing else can answer in his place; an answer acts only when it is shown to come from muse.",
  "world_is": "At b19849b51c: _muse_fields (tenant.py) accepts an answer with no version; chat_tag (tenant.py:56-66) is stable per chat; a new chat draft after a send is version 1 (:238); seq is unique per chat draft (assign_seq, :119-122) but not signed and not in drafts.json (refresh.py has no seq). Without version, unseen() uses a window over the envelope's sent_at, which the sender writes. A signed send for tag C and version 1, read from dell2's answers/ by the agents' account and sent as muse.reply later, acts on a newer version-1 draft under C. No forwarder and no signed answer exist at the round-17 deploy, so the path is not reachable at that act.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git show b19849b51c:data/transcripts/scripts/teams_chat/tenant.py lines 56-66, 119-122, 238, 570-622",
    "git show b19849b51c:data/transcripts/scripts/muse_reader/refresh.py (no seq field)",
    "deliverables/3.0.0_SA_CVO~L/NEVER_WIDEN_HALF_CVO_COMM_ASSIST_R17_DEPLOY_20261014.md, Carried section"
   ]
  },
  "disposition": "UNDER_INVESTIGATION"
 }
]
```

-- 3.0.0_SA_CVO~L
