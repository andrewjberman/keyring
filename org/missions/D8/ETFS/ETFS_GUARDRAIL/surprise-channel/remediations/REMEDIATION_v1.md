# ETFS_GUARDRAIL -- surprise channel, REMEDIATION v1 (round 1, laptop fabric)

**Home:** the project tree's remediation document (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` section 5; lane `TREE_CVO`).
**Who writes:** `3.0.0_SA_CVO`. One row per GRADUATED seat-form item, keyed by the item's id; the clocks (`disarm`,
`remediation`, `closed`) advance in place and only forward. Form: spine v3 -- no route token; the CTO routes every round
from the slug. Worker-form items (`W<n>-S<k>`) carry their clocks on the adjudication rows that graduate them
(`../adjudications/ADJUDICATION_v1.md` C-S2, C-S3), because a row keyed by a worker's coordinate is not one the CVO
mints on the main index.
**Denominator at this write:** 2 rows -- S3 (REMEDIATED, DISARMED, closed on the issuer's act @`446a064491`, verified at
HEAD) and S2 (OPEN: the `*.tf text eol=lf` rule, owner `1.0.0_SA_CTO`). The graduations are recorded in
`../adjudications/ADJUDICATION_v1.md` (C-S2, C-S3).

## S3 -- the `--gate` seam no cell owned: the orchestrator now passes the flag; closed

```json
[
  {
    "id": "ETFS_GUARDRAIL-S3",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "EG-s-6's face said the orchestrator's _render_command 'will pass --gate once EG-s-8 lands', but EG-s-8's face, EG-s-9's, the decomposition and the PRD carried no such instruction and _render_command at the time passed no flag -- the 10-01 fire would have rendered ungated and FWD-2 could never reach EXERCISED.",
    "evidence": [
      "2.0.0_SA_COO~B disarmed it in-round @446a064491: TO-EG-s-8 gained deliverable item 5 and the minted criterion S8-AC9 (GATE_FLAG_IN_RENDER_COMMAND=True in the instance).",
      "3.0.0_SA_CVO at HEAD, C-S1: infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:227 `python3 render_month_end.py --month {month} --pdf --gate --s3-out {out}`, with the row cited in the comment at :221; the deployed orchestrator serves the built hash of the EG-s-9 revision that carries it."
    ],
    "remedy": "EXECUTED: the flag added to _render_command under a minted criterion on the order that owned the call site, and deployed with EG-s-8/EG-s-9.",
    "owner": "2.0.0_SA_COO~B",
    "round": "v1",
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~B", "at": "2026-09-05T08:41Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~B", "round": "v1"},
    "closed": true
  }
]
```

## S2 -- the false CRLF drift: the worktrees were normalised for this round; the repository still has no eol rule for `*.tf`

```json
[
  {
    "id": "ETFS_GUARDRAIL-S2",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On this core.autocrlf=true box a fresh worktree checks out every .tf with CRLF (414 of 414 measured), so a Terraform plan re-renders heredoc-bearing resources (aws_instance.reporter user_data) and reports a change that does not exist on the live plane; two orders stopped on it (W1-S7, W1-S8) and applied by target. The issuer normalised every worker worktree to LF at hand-off, which covers this round's worktrees and no future one; .gitattributes at HEAD carries no *.tf rule.",
    "evidence": [
      "S2 at HEAD (2.0.0_SA_COO~B): live user_data sha1 e47b615c == the LF rendering of instance.tf at HEAD; the plan's 434774b5 == the CRLF rendering; the July commit touched ami and the public IP only.",
      "3.0.0_SA_CVO at HEAD, C-S3: `git show HEAD:.gitattributes` has no line matching 'tf'.",
      "The round's mitigation is per-worktree (the issuer's hand-off normalisation) and is not a repository state."
    ],
    "remedy": "Add `*.tf text eol=lf` (and the sibling `.tfvars`) to .gitattributes at the repository root, then re-normalise the tracked .tf files once so the index matches; disarm on one fresh worktree on this box whose .tf files check out LF and whose untargeted plan in etfs-reports reads the one expected change, read at this seat.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "disarm": {"state": "ARMED", "owner": "1.0.0_SA_CTO", "at": null},
    "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v1"},
    "closed": false
  }
]
```
