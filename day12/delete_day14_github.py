"""Delete day14 folder on GitHub only. Does not touch local files."""

import json
import subprocess

OWNER = "noraidk001009-crypto"
REPO = "ai-training"
BRANCH = "main"
FOLDER = "day14"


def gh_api(method, endpoint, fields=None):
    cmd = ["gh", "api", "-X", method, endpoint]
    if fields:
        for key, value in fields.items():
            cmd.extend(["-f", f"{key}={value}"])
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return json.loads(result.stdout) if result.stdout.strip() else {}


def list_contents(path):
    endpoint = f"repos/{OWNER}/{REPO}/contents/{path}?ref={BRANCH}"
    return gh_api("GET", endpoint)


def collect_files(path):
    files = []
    for item in list_contents(path):
        if item["type"] == "file":
            files.append((item["path"], item["sha"]))
        elif item["type"] == "dir":
            files.extend(collect_files(item["path"]))
    return files


def delete_file(path, sha):
    endpoint = f"repos/{OWNER}/{REPO}/contents/{path}"
    gh_api(
        "DELETE",
        endpoint,
        {
            "message": f"Remove {path}",
            "sha": sha,
            "branch": BRANCH,
        },
    )
    print(f"Deleted: {path}")


def main():
    try:
        files = collect_files(FOLDER)
    except RuntimeError as exc:
        if "Not Found" in str(exc):
            print(f"'{FOLDER}' not found on GitHub - already deleted.")
            return
        raise

    if not files:
        print(f"'{FOLDER}' is empty on GitHub.")
        return

    print(f"Deleting {len(files)} file(s) from GitHub {OWNER}/{REPO} ...")
    for path, sha in files:
        delete_file(path, sha)
    print("Done. day14 removed from GitHub.")


if __name__ == "__main__":
    main()
