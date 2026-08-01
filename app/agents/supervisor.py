from app.state import AgentState


def supervisor_node(state: AgentState):
  print("---SUPERVISOR: ANALYZING TASK & BUILDING PLAN---")
  task = state["task_description"]

  # Mocking a dynamic technical plan generation
  plan = [
      "Step 1: Write clean, self-contained Python function.",
      "Step 2: Execute code inside secure sandbox environment.",
      "Step 3: Validate outputs against test assertions.",
  ]

  return {"plan": plan, "current_step": 0, "iteration_count": 0}