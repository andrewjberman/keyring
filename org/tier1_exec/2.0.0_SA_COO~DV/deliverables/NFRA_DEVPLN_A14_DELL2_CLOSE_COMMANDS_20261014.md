# NFRA_DEVPLN act A14 -- close the five dell2 approval rows (Andrew approved all five, ~11:4xZ 2026-10-14)

Ask, one: run these five commands on dell2, in the dell2 workspace, then reply with the five `approval-status` lines.

Andrew's word, verbatim, is rows 1-3 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md` (read it at HEAD): "1.) Yes. 2.) Yes. 3.) Yes." for dell2 `7773`, `8500`/`7b45`/`fde0`, and `3635`. The CTO recorded it; the close takes `--ruled-by andrew`.

```
for id in dell2-20261013T221411Z-3635 dell2-20261013T222707Z-8500 dell2-20261013T222709Z-7b45 dell2-20261013T222710Z-fde0 dell2-20261013T231910Z-7773; do
  python .tools/open-calls.py close --id "$id" --by <your serial> --ruled-by andrew --decision approved     --ruling org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md
done
python .tools/open-calls.py approval-status --branch cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal
python .tools/open-calls.py approval-status --branch cand/dell2/anlreq-90-held-submit
python .tools/open-calls.py approval-status --branch cand/dell2/anlreq-88-advisory-fee
python .tools/open-calls.py approval-status --branch cand/dell2/anlreq-87-model-order
python .tools/open-calls.py approval-status --branch cand/dell2/partner-firm-stack
```

Expect `state=APPROVED valid=yes` on each (client-facing class: Andrew's word is the approver). After that the integrator merge-forwards each feature to DEV (`portal-merge-forward.sh`, the three on DEV already are only recorded) and `1.0.0_SA_CTO~DV` runs the chosen-set promote, which names only these five. This file asks for nothing else.
