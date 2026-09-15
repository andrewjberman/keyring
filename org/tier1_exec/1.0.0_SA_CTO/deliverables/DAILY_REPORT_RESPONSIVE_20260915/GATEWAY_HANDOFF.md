# Gateway source commit handoff

From `1.0.0_SA_CTO~A` to `0.7.0_AE_CloudOps`; base CTO and MSTR copied.

Andrew directly authorized the one-page report rework and said:

> You don't need a task order to do this, you should just go do it.

Authority and scope: `ANDREW_DIRECT.md` in this directory; Msg96840 and the
correcting Msg96849/96851. This covers the report template, presigned entry and
Gateway narrow-screen hop. It does not authorize an ALB change by this seat.

The implementation is complete and tested. The repository's owned-paths hook
refused this seat's commit of these two exact files because they are in
`CLOUD_OPS_OR_ETL`; no hook bypass or ownership grant was attempted:

- `infra/aws/ec2/opal-gateway/app/sprint_view.py`: skip the legacy narrow hop
  only when the report carries the responsive-layout marker; retain archive behavior.
- `infra/aws/ec2/opal-gateway/tests/test_sprint_view.py`: positive and negative
  regression checks for that behavior. Eight tests pass; lint passes.

Please review and pathspec-commit these exact tested working-tree changes under
your owning seat, then return the commit evidence. This asks for a source commit,
not a Gateway service deployment. The report publication works through the
existing Gateway because both filenames now contain responsive HTML.

CTO~A is committing and publishing the report-side change. CLOUD push and
CLOUD-to-SITEZ merge remain held. Live ALB sign-in verification remains separate.
