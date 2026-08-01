import os
import subprocess
import tempfile
from app.state import AgentState


def executor_node(state: AgentState):
  print("---EXECUTOR: RUNNING CODE IN SECURE SANDBOX---")
  code = state["generated_code"]

  # Write code to a secure temporary file
  with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
    f.write(code)
    temp_file_path = f.name

  try:
    # Execute with a strict 5-second timeout
    result = subprocess.run(
        ["python", temp_file_path], capture_output=True, text=True, timeout=5
    )
    if result.returncode == 0:
      output = result.stdout
      test_passed = True
      error_message = ""
    else:
      output = result.stdout
      test_passed = False
      error_message = result.stderr
  except subprocess.TimeoutExpired:
    output = ""
    test_passed = False
    error_message = "Execution timed out (possible infinite loop)."
  finally:
    if os.path.exists(temp_file_path):
      os.remove(temp_file_path)

  return {
      "execution_output": output,
      "test_passed": test_passed,
      "error_message": error_message,
  }