from typing import List, TypedDict


class AgentState(TypedDict):
  task_description: str
  plan: List[str]
  current_step: int
  generated_code: str
  execution_output: str
  test_passed: bool
  error_message: str
  iteration_count: int