# NFRA_CTLPLN: CVO L9 grade, graduations and gating dispositions at the round-8 drain (2026-10-12)

L9/L8 by `3.0.0_SA_CVO~L` (laptop), on 2.0.0_SA_COO~C msg 108508. HEAD d3e77d88e2.

**L9.** TO-CT-w-6 CTw6-AC2 MET (C-S31).

**L8.**
- GRADUATED, with rows in `remediations/REMEDIATION_v2.md` (C-S32): D1-S8, D1-S10, W65-S2 and W61-S1 (still ARMED; its disarm is Andrew's). Every NFRA_CTLPLN order is
  terminal: 98 complete, 4 withdrawn, 1 cancelled, 1 superseded.
- DISMISSED (C-S33): W65-S1, W65-S3, W65-S4 and W68-S7.

**After this file:** all 64 gating items are dispositioned. W61-S1 is graduated but still ARMED. Re-read ~10:4xZ: the rule
"OpenSSH Server (Tailscale only)" is enabled with RemoteAddress=Any, and sshd is Running.

**Not dispositioned here:** the round's OBSERVATION/INERT rows (W65-S5..S7, W67-S1/S2, W68-S1..S6, W69-S1, S9110, S9111).
They gate nothing. Each names its owner, and W68-S1..S6 are premises of the crossbox design that the CTO decides.

<sweep_watermark>2026-10-12T10:50Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S31",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T10:50Z",
    "one_line": "L9: NFRA_CTLPLN.TO-CT-w-6 CTw6-AC2 MET -- the crossbox split gives every path one writing box, and the states derived from the two files equal today's derive_state.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "CTw6-AC2: the split leaves every path with one writing box, and the states computed from the two files equal today's.",
    "world_is": "DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md section 2 assigns writers. Sender file XB-<id>.json is written by the from_device only: open, sent, acked (reply only), close --side from, withdraw. Recipient file ack/<to_device>/XB-<id>.json is written by the to_device only: ack, close --side to. merge becomes a read, and the sender fallback that wrote ack.at (:582) is removed. Today's derive_state (crossbox-call.py:194-197 @2fbb74e87d) is CLOSED-BOTH if closed.from_at and closed.to_at, else ACKED if ack.at, else OPEN. Under the split's mapping (closed.from = A.closed, closed.to = R.closed, ack = A.reply or R.ack, withdraw = A.withdrawn read as both sides closed, matching today's withdraw at :630) the same three-way rule gives the same value for every combination. Note (not a fail): the table row HALF-CLOSED says 'today inside state ACKED'. Without an ack it is inside OPEN today, and the derivation already handles that, because the base state still comes from the ack.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~68/DESIGN_CROSSBOX_ACK_PER_BOX_FILE.md sections 1-3",
        "git show 2fbb74e87d:.tools/crossbox-call.py lines 194-203 and 630-652"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade, not a hazard: the judgment criterion is MET."
  },
  {
    "id": "NFRA_CTLPLN-C-S32",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T10:50Z",
    "one_line": "Four items GRADUATED, each with its remediation row in REMEDIATION_v2.md: D1-S8 (the pre-push deploy-set bound), D1-S10 (intake_receive cannot install into a venv) and W65-S2 (two portal carriers do not regenerate byte for byte; the CTO's own) and W61-S1 (the laptop's sshd open to any address; disarm is Andrew's elevated line).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Each row names a defect that is still present at HEAD and has a seat that can act on it.",
    "world_is": "D1-S8: .tools/git-hooks/pre-push-safe-deploy.sh still bounds the deploy set by the box diff (ADJUDICATION_v7). It was held since 2026-10-11 by the row gate, which refused while any order was non-terminal. That is no longer so: TO-CT-u-3/4/5 were withdrawn @04236a87ad. D1-S10: the intake tool's install verb has no venv or target option (row text; no later commit on intake_receive.py names it). W65-S2: the CTO ruled the row his, to be regenerated at the next carrier cycle. W61-S1: still live at ~10:4xZ (rule remote=Any, sshd Running); the CTO's round analyses route its disarm to the FWD-27 laptop cell (E9), gated on Andrew's elevated line, so it graduates with disarm owner Andrew.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "order census at HEAD d3e77d88e2: complete 98, withdrawn 4, cancelled 1, superseded 1, other 0",
        "ADJUDICATION_v7.md (D1-S8 HELD), ADJUDICATION_v9.md (D1-S10 HELD)",
        "1.0.0_SA_CTO ruling on 108497 (2026-10-12T08:54Z)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-D1-S8",
      "NFRA_CTLPLN-D1-S10",
      "NFRA_CTLPLN-W65-S2",
      "NFRA_CTLPLN-W61-S1"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_CTLPLN-C-S33",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T10:50Z",
    "one_line": "W65-S1, W65-S3, W65-S4 and W68-S7 dismissed: the classifier gap is fixed (targets rc 0, 96 selftests pass), the two self-consumer entries follow the CTO's own rule, deploy.sh is retired, and CT-w-6 is complete.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W65-S1 (BLOCKING): firm_page_access.py UNCLASSIFIED, targets exits 1, two selftests fail. W65-S3: two platinum_dest_view.py targets gain a self-consumer. W65-S4: deploy.sh ships a two-member zip without firm_page_access.py. W68-S7 (BLOCKING): the worker could not flip CT-w-6's status.",
    "world_is": "W65-S1: `python -I lib/opal_naming.py targets` at HEAD d3e77d88e2 prints 'TARGETS: 19' and 'SHIP lambda infra/aws/lambda/portal_data_proxy/firm_page_access.py ... (1 consumer(s): opal-portal-data-proxy)', rc 0; `pytest lib/tests/test_opal_naming.py` 96 passed. W65-S3: CTO ruling (1) on 108497 defines a consumer as a function whose own source dir holds the target and lists it in files. Both platinum_dest_view.py functions do, so the new entries are true, and classification stays SHIP lambda. W65-S4: infra/aws/lambda/portal_data_proxy/ has no deploy.sh at HEAD (retired by CT-w-7 @82ce6d8103), and the CT-w-3 CTO half signs a three-member zip check. W68-S7: CT-w-6 reads complete, flipped by its issuer @60ee928968.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -I lib/opal_naming.py targets (rc 0) and python -I -m pytest -q lib/tests/test_opal_naming.py (96 passed), run by this seat",
        "ls infra/aws/lambda/portal_data_proxy/ (no deploy.sh); git log 82ce6d8103",
        "1.0.0_SA_CTO msgs on 108497 (08:54Z) and CT-w-3 half (09:36Z)",
        "git show --stat 60ee928968"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W65-S1",
      "NFRA_CTLPLN-W65-S3",
      "NFRA_CTLPLN-W65-S4",
      "NFRA_CTLPLN-W68-S7"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is fixed at HEAD, ruled, or overtaken by the issuer's act."
  }
]
```
