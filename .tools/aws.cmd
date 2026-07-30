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
@rem PORTABILITY (2026-07-30, 0.7.0_AE_CloudOps~Z): this was ONE hardcoded pip-install path.
@rem It exists on the primary laptop and DOES NOT EXIST on site Z, where the CLI is the native
@rem v2 installer under a different root. The breakage was invisible where anyone would look:
@rem `aws` from bash kept working (that is the OTHER shim, .tools/aws), so every hand-run call
@rem read healthy. Only NATIVE-PYTHON callers that resolve via shutil.which -> this .cmd broke
@rem -- which is exactly comp-tagauthz's sh(), so `safe-apply` fail-closed with "could not
@rem evaluate" on EVERY default_tags module on this device. A device-specific absolute path in
@rem a TRACKED, CROSS-DEVICE file is the defect class; resolve, do not assume.
@rem The laptop path stays FIRST, so its behavior is byte-unchanged.
setlocal
set "_OPAL_AWS=%LOCALAPPDATA%\Programs\Python\Python312\Scripts\aws.cmd"
if not exist "%_OPAL_AWS%" set "_OPAL_AWS=%LOCALAPPDATA%\Programs\AWSCLIV2\Amazon\AWSCLIV2\aws.exe"
if not exist "%_OPAL_AWS%" set "_OPAL_AWS=%ProgramFiles%\Amazon\AWSCLIV2\aws.exe"
if not exist "%_OPAL_AWS%" (
    echo aws.cmd: FATAL -- no AWS CLI found. Checked %%LOCALAPPDATA%%\Programs\Python\Python312\Scripts\aws.cmd, %%LOCALAPPDATA%%\Programs\AWSCLIV2\Amazon\AWSCLIV2\aws.exe, %%ProgramFiles%%\Amazon\AWSCLIV2\aws.exe 1>&2
    exit /b 127
)
"%_OPAL_AWS%" %*
