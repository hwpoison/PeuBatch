import subprocess


code = subprocess.run(["./scripts/test/job_1_OK.sh"], stdout=subprocess.PIPE)
print(code)
