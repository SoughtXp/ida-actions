# ida-actions

[![IDA Analysis](https://github.com/SoughtXp/ida-actions/actions/workflows/main.yml/badge.svg)](https://github.com/SoughtXp/ida-actions/actions/workflows/main.yml)

GitHub Actions workflow to analyse a file with **IDA Pro 9.0** in headless mode.
It downloads a target binary from Google Drive, runs the IDA auto-analysis,
optionally generates C pseudocode, and uploads the results as workflow
artifacts.

## Prerequisites

- A copy of the **IDA Pro 9.0 Linux installer** (`idapro_90_x64linux.run`),
  uploaded to Google Drive and shared with "anyone with the link".
- The target binary you want to analyse, also uploaded to Google Drive and
  shared the same way.

## Workflow inputs

| Input            | Required | Description                                            |
| ---------------- | -------- | ------------------------------------------------------ |
| `target_file`    | yes      | Name to save the analysed file as.                     |
| `file_link`      | yes      | Google Drive link/ID of the file to analyse.           |
| `installer_link` | yes      | Google Drive link/ID of the IDA Pro installer.         |
| `generate_c`     | no       | Generate C pseudocode (`.c`). Defaults to `false`.     |

## Steps to run

1. Upload the file to Google Drive.

2. Set the file access to anyone with the link.

   ![](assets/gdrive_access.png)

3. Open the **Actions** tab of this repo and select the **IDA Analysis**
   workflow.

4. Click **Run workflow**, fill in the inputs, and run it.

   ![](assets/sample_params.png)

5. Wait for the run to finish and download the artifacts:
   - `<target_file>-Database` — the IDA database (`.i64`).
   - `<target_file>-Pseudocode` — the C pseudocode (only when `generate_c` is enabled).

## Contact

Open an issue in this repository.
