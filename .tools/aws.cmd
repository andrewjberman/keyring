@echo off
@rem aws.cmd -- Windows-shell companion to the .tools/aws bash shim (0.8.0_AE_CloudComp).
@rem
@rem WHY THIS FILE EXISTS: a powershell.exe/cmd.exe spawned FROM Git Bash inherits bash's
@rem PATH, which puts .tools FIRST. Windows then resolves the EXTENSIONLESS bash script
@rem `.tools/aws` as an Application -- and it HANGS (reproduced 2026-07-13: `aws --version`
@rem from a bash-spawned powershell never returned). Under `--quiet` that hang/failure is a
@rem SILENT NO-OP: infra/aws/lambda/ci/build-and-upload.sh reported a successful upload
@rem while S3 kept the OLD zip. Caught only by the upload-verify gate.
@rem
@rem PATHEXT makes Windows shells prefer this .cmd over the extensionless file, so both
@rem shells now get a WORKING aws: bash -> .tools/aws (MSYS path-mangling guard),
@rem Windows shells -> here -> the real CLI. Absolute target: never re-enters .tools.
"%LOCALAPPDATA%\Programs\Python\Python312\Scripts\aws.cmd" %*
