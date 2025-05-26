
import subprocess
import json

def run_book(book, params):
    params_json = json.dumps(params, separators=(',', ':'))
    escaped_params_json = params_json.replace('"', '\\"')

    # print(f"params_json: {params_json}")

    command = (
        f"npx ptbk run ./books/{book}.book "
        "--no-interactive --provider BRING_YOUR_OWN_KEYS "
        f"--json \"{escaped_params_json}\""
    )

    # print(f"command: {command}")

    result_json = subprocess.check_output(command, shell=True, text=True).strip()
    result = json.loads(result_json)
    return result

