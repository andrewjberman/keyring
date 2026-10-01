# MDPF_HEALGAP -- surprise channel (INVESTIGATION_v1)

Legacy flat channel: MDPF_HEALGAP has no tree home (register `org/projects/MDPF_HEALGAP.json`; 1.0.0_SA_CTO rulings
batch 75 item 7). Investigation rows are lane ANY; remediation rows stay `3.0.0_SA_CVO`'s. No tally is kept in this header.


## MDPF_HEALGAP-S1 -- two runtimes start at 13:30Z and both can call the Cottonwood gold builder; which one writes the day's partition is read here, the other's schedule is not

```json
{
  "id": "MDPF_HEALGAP-S1",
  "project": "MDPF_HEALGAP",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~M",
  "surfaced_at": "2026-10-01T11:55:00Z",
  "one_line": "The Cottonwood gold builder has two callers: the consolidator's run_cottonwood_family (mdpf_gold_consolidator.py:2078, in the mdpf-gold-lambda) and the EC2 dispatch (infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:554). Both runtimes started at 13:30Z on 2026-09-30: the Lambda's last scheduled log event reads 13:31:19Z and the instance mdpf-daily-runner reads LaunchTime 13:30:35Z, stopped 18:46:18Z. The gold partitions carry LastModified 13:30:39Z-13:30:40Z, five seconds after the instance launched, so the Lambda wrote them; the EC2 path left no later write on them.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws logs describe-log-streams /aws/lambda/mdpf-gold-lambda, 2026-10-01 11:5xZ: newest scheduled stream 2026/09/30 last event 2026-09-30T13:31:19Z (two later streams at 02:12Z and 02:18Z on 10-01 are not at the schedule's hour).",
      "aws ec2 describe-instances i-02448edb624a7a7cf (mdpf-daily-runner), 11:5xZ: stopped, 'User initiated (2026-09-30 18:46:18 GMT)', LaunchTime 2026-09-30T13:30:35Z.",
      "head-object on five gold dim partitions (date=08-19, 08-21, 08-24, 09-24, 09-25): LastModified 13:30:39Z or 13:30:40Z on each object's own date; an instance launched at 13:30:35Z cannot have written at 13:30:40Z.",
      "Source: mdpf-daily-dispatch.sh:548-556 runs the builder, the pair and the slice only when build_cottonwood_mdpf_slice.py is present in the runner's staged assets_gold directory; whether it is staged there is not read.",
      "CTO half on the catch-up half request @9fb81ec9f6, item 2: 'THE EC2 NIGHTLY WRITER'S SCHEDULE is not measured ... its schedule state is one row for the round.'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The catch-up half (NEVER_WIDEN_HALF_REQUEST_HEALGAP_COTTONWOOD_CATCHUP_20261001.md) names 2 writers of gold/dim_model_portfolio, both writing only the NEWEST assignment date, and says the EC2 instance 'reads stopped'; the trace names the consolidator as the daily writer.",
  "world_is": "The EC2 runner is not retired: it launches every day at the same minute as the Lambda. On the days read, the Lambda wrote the day's gold partition and the runner did not rewrite it. If the runner's staged tree does carry the slice script, its dispatch would re-run the builder, the pair and the slice later the same day WITHOUT the catch-up step, on the newest assignment date only; that cannot rewrite a caught-up partition, but it would re-publish the slice from whatever partitions exist at that moment.",
  "notes": "Not measured: which schedule starts the instance (mdpf-scheduled-floor is the candidate), and whether assets_gold is staged on it. Owner of the answer: the runner's lane (0.7.0_AE_CloudOps, dark). The half's sign-off stands on the source reading (newest date only)."
}
```
