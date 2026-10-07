# NFRA_OPLGTW -- remediation v14 (site Z): round 29 -- two rows graduated in ADJUDICATION_v21.Z

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-07T22:29:59Z.

```json
[
 {
  "id": "NFRA_OPLGTW-Z-S67",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A gateway deploy restarts the service. On r28 the scoped concierge's refresh-token family was revoked in the minute of the restart with reason refresh_token_reuse, and that client must sign in again by hand; another identity refreshing in the same minute stayed signed in; r26 and r27 revoked none. INFERRED by the issuer, not observed: a refresh that straddles the restart has its rotation committed and its answer lost, and the retry presents the rotated token.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S67",
   "adjudications/ADJUDICATION_v21.Z.md#NFRA_OPLGTW-Z-C-S55"
  ],
  "remedy": "OPEN and ARMED: the hazard stands for every gateway deploy until the token rules change (a short grace for the immediately previous generation, or a drain of in-flight refreshes before the restart), which the CTO rules. Mitigation in place: the release form names the re-authentication a deploy can cost and who performs it, and bars a deploy inside the 12 hours before the 07:00 America/New_York send without it named.",
  "owner": "2.0.0_SA_COO~O",
  "round": "v14",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~O",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~O",
   "round": "v14"
  },
  "closed": false
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S33",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "R45 counts bun cache entries, bytes and files before and after a deploy. It measures writes to the cache. A request to the package registry that writes nothing (a metadata or manifest check by a frozen install with every entry cached) is invisible to it. The first deploy under the pre-check read clean on R45, and the question stays undetermined.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S33",
   "adjudications/ADJUDICATION_v21.Z.md#NFRA_OPLGTW-Z-C-S55"
  ],
  "remedy": "OPEN: a network-side read decides it (a proxy or packet log on the deploying box during one install, or bun's own verbose network log if it has one that needs no fetch). Until then each release's record states the question is undetermined, as the release form requires.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v14",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v14"
  },
  "closed": false
 }
]
```
