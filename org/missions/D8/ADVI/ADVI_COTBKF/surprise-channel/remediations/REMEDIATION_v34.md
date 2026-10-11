# ADVI_COTBKF: remediations, rounds 50 to 53

<sweep_watermark>2026-10-11T03:22Z</sweep_watermark>

Rounds 50-53 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T03:22:00Z. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_53_DRAIN_END_20261011.md @e336d32f61 (msg 3951)`, with the rounds 50-52 packets compiled in
ADJUDICATION_v36. L9: rounds 50-52 three criteria MET; round 53 **CB53ba1-AC2 NOT MET**. Graduated, round label v54: 4 rows, OPEN.
ARMED: 3. D2-S80 is the issuer's row, confirmed by this seat's count: the CB-al-2 pair must not cite the manifest at HEAD. D2-S60 and D2-W66-S1 are older rows this
slug dispositions; both gate the CB-al-2 mint.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S80",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The round-53 redaction replaced digit runs inside sha256 values of the tracked clean manifest with acct# tokens: 440 tokens, 431 hash values. The file no longer states the hashes of 156, 127 and 148 of its 3,325 days, and the CB-al-2 mint pair reads it.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S80",
   "this seat's read of the manifest at 82049024b3^, 82049024b3 and HEAD: before, 0 tokens and 3325 intact 64-hex values in each of sha256, content_sha256 and manifest_sha256; after, 440 acct# tokens, every one inside a hash value: 156 sha256, 127 content_sha256 and 148 manifest_sha256 values changed (431 values)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_53_L9_GRADE_20261011.md"
  ],
  "remedy": "Restore day_files from the parent blob (git show 82049024b3^:<path>) and re-read 3325 of 3325 against round 47's. The sweep takes a boundary test so a member inside a longer hex or alphanumeric run is not replaced, and the test asserts every sha256 field is 64 hex. The CB-al-2 pair is signed against the restored bytes.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v54",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v54"
  },
  "closed": false,
  "disarm_owner": "2.0.0_SA_COO~C2"
 },
 {
  "id": "ADVI_COTBKF-D2-S60",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The CB-aj-2 CTO half's condition 2 stops on ANY writer of silver/prices/ in the cot code/gold mirror, while the same half names a cot writer the mirror necessarily contains. The applier wrote nothing (0 of 38 keys) and asked the half's author which reading holds.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S60"
  ],
  "remedy": "The half's author restates condition 2 (a writer BEYOND the census, or a scheduled one), or retires the half if the round-50 redeploy superseded the act.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v54",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v54"
  },
  "closed": false,
  "disarm_owner": "1.0.0_SA_CTO~DELL2"
 },
 {
  "id": "ADVI_COTBKF-D2-W66-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The producer's closed vocabularies hold no value that truthfully states FWD-3's method for Cottonwood, so 107,316 measured rows carry return_basis and method_version NULL; emit_day(upload=True) would write a manifest that states the custodian method at the mint.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W66-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_53_DRAIN_END_20261011.md @e336d32f61 (msg 3951)"
  ],
  "remedy": "CB-al-2 does not mint through emit_day(upload=True) unchanged: IRPT_DASHBD lands a return_basis value or a manifest-text parameter first, or the issuer rules a different claim. The re-cut CB-al-2 pair names which.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v54",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v54"
  },
  "closed": false,
  "disarm_owner": "2.0.0_SA_COO~C2"
 },
 {
  "id": "ADVI_COTBKF-D2-S77",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "commonwealth_sweeps.py:729 hardcodes a dell2 path as the private config's default and :750 loads it at import, so the module imports on dell2 only unless COTBKF_SWEEPS_CONFIG is set.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S77",
   "data/assets/scripts/silver/commonwealth_sweeps.py:728-750 at HEAD"
  ],
  "remedy": "Remove the device default: the path comes from COTBKF_SWEEPS_CONFIG alone (absent -> the same named error), or is derived. State where a second box gets the file.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v54",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v54"
  },
  "closed": false
 }
]
```
